#!/usr/bin/env python3
"""
meta_ad_library.py — fetch Meta Ad Library active ads for a brand.

Usage:
    python meta_ad_library.py --brand "AG1" --country US

## API access requirements (as of 2025/2026)

The Meta Ads Archive API (graph.facebook.com/ads_archive) requires:
1. A Meta Developer app with "Ads Management Standard Access" feature enabled
2. Business verification of the developer account (Meta Business Manager)
3. The APP_ID|APP_SECRET token format (set META_ADS_TOKEN in .env)

Without business verification, the API returns error 2332004 ("App role required").

## Geographic limitation
The public API only returns ads from EU countries and global political/social cause
ads. US commercial ads are NOT accessible via the free API tier regardless of token.
For US ad data: use the web UI at facebook.com/ads/library (manual) or a paid tool
(AdSpy, Foreplay, Minea).

Strategy (in order, stops at first success):
1. Meta Ads Archive API  — requires META_ADS_TOKEN + business verification
2. OpenAI web search     — searches for brand's active ad count via web
3. URL stub               — emits the URL + manual instructions

Output JSON (same schema regardless of method):
  {url, country, brand, method, active_ad_count, longest_running_ad_days,
   creative_fatigue_signal, top_formats, earliest_ad_date, raw_ads, note}
"""
from __future__ import annotations
import argparse
import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import urlencode

import requests

sys.path.insert(0, str(Path(__file__).parent))
from _openai_search import load_env, web_search, parse_json_from_text
load_env()

TIMEOUT = 20
META_GRAPH_VERSION = "v19.0"

BROWSER_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}


# ---------------------------------------------------------------------------
# Strategy 1 — Meta Graph API
# ---------------------------------------------------------------------------

def try_graph_api(brand: str, country: str, token: str) -> dict | None:
    """
    Query the public Ads Archive endpoint.
    Docs: https://developers.facebook.com/docs/marketing-api/reference/ads_archive
    """
    params = {
        "search_terms": brand,
        "ad_type": "ALL",
        "ad_reached_countries": f'["{country}"]',
        "fields": "id,ad_creation_time,ad_delivery_start_time,ad_delivery_stop_time,"
                  "ad_creative_bodies,ad_creative_link_captions,ad_snapshot_url,"
                  "publisher_platforms,impressions,spend",
        "limit": 50,
        "access_token": token,
    }
    url = f"https://graph.facebook.com/{META_GRAPH_VERSION}/ads_archive"
    try:
        r = requests.get(url, params=params, timeout=TIMEOUT, headers=BROWSER_HEADERS)
        if r.status_code != 200:
            return None
        data = r.json()
        ads = data.get("data", [])
        if not ads:
            return None
        return _summarise_graph_ads(ads, brand, country)
    except Exception:
        return None


def _summarise_graph_ads(ads: list[dict], brand: str, country: str) -> dict:
    import datetime

    dates = []
    formats: dict[str, int] = {}
    for ad in ads:
        start = ad.get("ad_delivery_start_time") or ad.get("ad_creation_time")
        if start:
            try:
                dates.append(datetime.datetime.fromisoformat(start.replace("Z", "+00:00")))
            except ValueError:
                pass
        for p in ad.get("publisher_platforms", []):
            formats[p] = formats.get(p, 0) + 1

    now = datetime.datetime.now(datetime.timezone.utc)
    days_running = []
    if dates:
        for d in dates:
            delta = (now - d).days
            if delta >= 0:
                days_running.append(delta)

    earliest = min(dates).date().isoformat() if dates else None
    longest = max(days_running) if days_running else None
    median = sorted(days_running)[len(days_running) // 2] if days_running else None
    fatigue = round(median / longest, 2) if longest and median else None

    ad_library_url = (
        f"https://www.facebook.com/ads/library/?"
        + urlencode({
            "active_status": "active",
            "ad_type": "all",
            "country": country,
            "q": brand,
            "search_type": "keyword_unordered",
            "media_type": "all",
        })
    )
    return {
        "url": ad_library_url,
        "country": country,
        "brand": brand,
        "method": "graph_api",
        "active_ad_count": len(ads),
        "longest_running_ad_days": longest,
        "creative_fatigue_signal": fatigue,
        "top_formats": sorted(formats, key=formats.get, reverse=True)[:3],
        "earliest_ad_date": earliest,
        "raw_ads": ads[:5],  # first 5 for context
        "note": f"Graph API: {len(ads)} ads returned (limit 50). Fatigue = median/max days running.",
    }


# ---------------------------------------------------------------------------
# Strategy 2 — HTML scrape
# ---------------------------------------------------------------------------

def try_html_scrape(brand: str, country: str) -> dict | None:
    params = {
        "active_status": "active",
        "ad_type": "all",
        "country": country,
        "q": brand,
        "search_type": "keyword_unordered",
        "media_type": "all",
    }
    url = f"https://www.facebook.com/ads/library/?{urlencode(params)}"
    try:
        r = requests.get(url, headers=BROWSER_HEADERS, timeout=TIMEOUT)
        html = r.text
    except Exception as e:
        return {"_scrape_error": str(e)}

    # Look for ad count in embedded JS payloads
    count = None
    # Pattern 1: "total_count":N
    m = re.search(r'"total_count"\s*:\s*(\d+)', html)
    if m:
        count = int(m.group(1))
    # Pattern 2: "adCount":N
    if count is None:
        m = re.search(r'"adCount"\s*:\s*(\d+)', html)
        if m:
            count = int(m.group(1))

    # Look for earliest ad date
    dates = re.findall(r'"ad_delivery_start_time"\s*:\s*"(\d{4}-\d{2}-\d{2})', html)

    if count is None and not dates:
        return None  # nothing useful extracted

    return {
        "url": url,
        "country": country,
        "brand": brand,
        "method": "html_scrape",
        "active_ad_count": count,
        "longest_running_ad_days": None,
        "creative_fatigue_signal": None,
        "top_formats": [],
        "earliest_ad_date": min(dates) if dates else None,
        "note": (
            "Extracted from initial HTML payload. JS-rendered — count may be incomplete. "
            "Verify by opening the URL manually."
        ),
    }


# ---------------------------------------------------------------------------
# Strategy 3 — OpenAI web search
# ---------------------------------------------------------------------------

def try_openai_search(brand: str, country: str) -> dict | None:
    params = {
        "active_status": "active",
        "ad_type": "all",
        "country": country,
        "q": brand,
        "search_type": "keyword_unordered",
        "media_type": "all",
    }
    lib_url = f"https://www.facebook.com/ads/library/?{urlencode(params)}"

    prompt = f"""Search the Meta Ads Library for active ads from "{brand}".

Check: {lib_url}
Also search for: "{brand}" facebook ads active 2024 2025

Return ONLY valid JSON:
{{
  "active_ad_count": <integer or null>,
  "earliest_ad_date": "<YYYY-MM-DD or null>",
  "longest_running_ad_days": <integer or null>,
  "top_formats": ["image", "video"],
  "creative_themes": ["theme1", "theme2"],
  "notes": "brief summary of what ads show"
}}

If no ads found or data unavailable, return {{"active_ad_count": null, "notes": "no ad data found via web search"}}"""

    raw = web_search(prompt)
    if not raw:
        return None
    return parse_json_from_text(raw)


# ---------------------------------------------------------------------------
# Strategy 4 — URL stub (always succeeds)
# ---------------------------------------------------------------------------

def url_stub(brand: str, country: str) -> dict:
    params = {
        "active_status": "active",
        "ad_type": "all",
        "country": country,
        "q": brand,
        "search_type": "keyword_unordered",
        "media_type": "all",
    }
    url = f"https://www.facebook.com/ads/library/?{urlencode(params)}"
    return {
        "url": url,
        "country": country,
        "brand": brand,
        "method": "stub_only",
        "active_ad_count": None,
        "longest_running_ad_days": None,
        "creative_fatigue_signal": None,
        "top_formats": [],
        "earliest_ad_date": None,
        "note": (
            "All strategies failed. Manual fallback: open the URL above. "
            "API requires Meta Business Verification + Ads Management Standard Access. "
            "Note: free API only returns EU ads; US ad data requires paid tools (AdSpy, Foreplay)."
        ),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--brand", required=True)
    ap.add_argument("--country", default="US")
    ap.add_argument("--token", default=None,
                    help="Meta app access token (APP_ID|APP_SECRET). "
                         "Falls back to META_ADS_TOKEN env var.")
    args = ap.parse_args()

    brand = args.brand
    country = args.country
    token = args.token or os.getenv("META_ADS_TOKEN", "")

    # Strategy 1 — Graph API
    if token:
        result = try_graph_api(brand, country, token)
        if result:
            print(json.dumps(result, indent=2, default=str))
            return 0

    # Strategy 2 — HTML scrape
    result = try_html_scrape(brand, country)
    if result and "active_ad_count" in result and result.get("method"):
        print(json.dumps(result, indent=2, default=str))
        return 0

    # Strategy 3 — OpenAI web search
    result = try_openai_search(brand, country)
    if result:
        params = {
            "active_status": "active", "ad_type": "all", "country": country,
            "q": brand, "search_type": "keyword_unordered", "media_type": "all",
        }
        print(json.dumps({
            "url": f"https://www.facebook.com/ads/library/?{urlencode(params)}",
            "country": country,
            "brand": brand,
            "method": "openai_web_search",
            "active_ad_count": result.get("active_ad_count"),
            "longest_running_ad_days": result.get("longest_running_ad_days"),
            "creative_fatigue_signal": None,
            "top_formats": result.get("top_formats", []),
            "earliest_ad_date": result.get("earliest_ad_date"),
            "creative_themes": result.get("creative_themes", []),
            "note": result.get("notes", "retrieved via OpenAI web search"),
        }, indent=2))
        return 0

    # Strategy 4 — stub
    print(json.dumps(url_stub(brand, country), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

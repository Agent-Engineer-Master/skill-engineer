#!/usr/bin/env python3
"""
similarweb_lookup.py — fetch SimilarWeb traffic snapshot for a domain.

Usage:
    python similarweb_lookup.py --domain example.com

Strategy:
1. Direct HTML fetch — SimilarWeb is JS-rendered; catches occasional embedded JSON.
2. OpenAI web search fallback — searches SimilarWeb cached data + other traffic sources.

Output JSON: {domain, url, monthly_visits_est, accuracy, top_sources, method, note}
If monthly_visits_est < 50000, accuracy = "directional only". Always carry this caveat.
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).parent))
from _openai_search import web_search, parse_json_from_text

BROWSER_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}
TIMEOUT = 20
ACCURACY_FLOOR = 50_000


def accuracy_label(visits: int | None) -> str:
    if visits is None:
        return "fetch failed — directional only"
    if visits < ACCURACY_FLOOR:
        return f"directional only (<{ACCURACY_FLOOR:,}/mo) — quote a range, do not cite point estimate"
    return "point estimate acceptable; still triangulate with ad count + review velocity"


def try_direct(domain: str) -> int | None:
    url = f"https://www.similarweb.com/website/{domain}/"
    try:
        r = requests.get(url, headers=BROWSER_HEADERS, timeout=TIMEOUT)
        html = r.text
        m = re.search(r'"visits"\s*:\s*"?(\d[\d,.]*)"?', html)
        if m:
            return int(float(m.group(1).replace(",", "")))
    except Exception:
        pass
    return None


def try_openai_search(domain: str) -> dict | None:
    prompt = f"""Find web traffic data for {domain}.

Search SimilarWeb (similarweb.com/website/{domain}), Semrush, Ahrefs, or any traffic intelligence tool.

Return ONLY valid JSON:
{{
  "monthly_visits_est": <integer or null>,
  "visit_range_low": <integer or null>,
  "visit_range_high": <integer or null>,
  "top_traffic_sources": {{"direct": "X%", "organic_search": "X%", "paid_search": "X%", "social": "X%", "referral": "X%"}},
  "top_countries": ["US", "UK"],
  "bounce_rate": "<percent or null>",
  "avg_visit_duration": "<seconds or null>",
  "global_rank": <integer or null>,
  "category_rank": "<category: rank or null>",
  "notes": "source and recency of data"
}}

If no data is available, return {{"monthly_visits_est": null, "notes": "no traffic data found"}}"""

    raw = web_search(prompt)
    if not raw:
        return None
    return parse_json_from_text(raw)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--domain", required=True)
    args = ap.parse_args()

    domain = args.domain.replace("https://", "").replace("http://", "").strip("/")
    url = f"https://www.similarweb.com/website/{domain}/"

    # Strategy 1: direct
    visits = try_direct(domain)
    if visits is not None:
        print(json.dumps({
            "domain": domain, "url": url,
            "monthly_visits_est": visits,
            "accuracy": accuracy_label(visits),
            "top_sources": [],
            "method": "direct_fetch",
            "note": "extracted from initial HTML; JS-rendered values may be missing",
        }, indent=2))
        return 0

    # Strategy 2: OpenAI web search
    result = try_openai_search(domain)
    if result:
        visits = result.get("monthly_visits_est")
        low = result.get("visit_range_low")
        high = result.get("visit_range_high")
        # Build a sources list from the traffic breakdown
        sources_raw = result.get("top_traffic_sources", {})
        top_sources = [f"{k}: {v}" for k, v in sources_raw.items() if v] if sources_raw else []
        print(json.dumps({
            "domain": domain, "url": url,
            "monthly_visits_est": visits,
            "visit_range": f"{low:,}–{high:,}" if low and high else None,
            "accuracy": accuracy_label(visits),
            "top_sources": top_sources,
            "top_countries": result.get("top_countries", []),
            "global_rank": result.get("global_rank"),
            "category_rank": result.get("category_rank"),
            "method": "openai_web_search",
            "note": result.get("notes", "retrieved via OpenAI web search"),
        }, indent=2))
        return 0

    # Fallback
    print(json.dumps({
        "domain": domain, "url": url,
        "monthly_visits_est": None,
        "accuracy": accuracy_label(None),
        "top_sources": [],
        "method": "failed",
        "note": "direct fetch failed (JS-rendered), web search unavailable",
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

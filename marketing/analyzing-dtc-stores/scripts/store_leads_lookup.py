#!/usr/bin/env python3
"""
store_leads_lookup.py — fetch Store Leads data for a Shopify store.

Usage:
    python store_leads_lookup.py --domain example.com

Store Leads covers 11M+ ecommerce stores: Shopify plan, app stack, revenue
bracket, traffic range, employee count, launch date. Feeds §11 Tech Stack
and §6 Pricing.

Strategy:
1. Direct HTTP fetch of storeleads.app (works if not paywalled/blocked)
2. OpenAI web search fallback — finds Store Leads and BuiltWith cached data

Output JSON: {domain, url, shopify_plan, app_stack[], revenue_bracket,
              traffic_range, launch_date, method, note}
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

STORE_LEADS_PATTERNS = [
    "https://storeleads.app/l/{domain}",
    "https://storeleads.app/reports/shopify/{domain}",
]


def try_direct(domain: str) -> tuple[str, int, str]:
    for pattern in STORE_LEADS_PATTERNS:
        url = pattern.format(domain=domain)
        try:
            r = requests.get(url, headers=BROWSER_HEADERS, timeout=TIMEOUT, allow_redirects=True)
            if r.status_code == 200 and len(r.text) > 1000:
                return r.text, r.status_code, url
        except Exception:
            pass
    return "", 404, STORE_LEADS_PATTERNS[0].format(domain=domain)


def parse_store_leads(html: str) -> dict:
    result: dict = {}
    # Shopify plan
    m = re.search(r'shopify[_ ]plan["\s:>]+([A-Za-z0-9 _-]+)', html, re.IGNORECASE)
    if m:
        result["shopify_plan"] = m.group(1).strip()
    # Revenue bracket
    m = re.search(r'revenue["\s:>]+(\$[\d,]+ ?[-–] ?\$[\d,]+|\$[\d,]+\+?)', html, re.IGNORECASE)
    if m:
        result["revenue_bracket"] = m.group(1).strip()
    # Monthly traffic
    m = re.search(r'(monthly )?traffic["\s:>]+([\d,]+ ?[-–] ?[\d,]+|[\d,]+)', html, re.IGNORECASE)
    if m:
        result["traffic_range"] = m.group(2).strip()
    return result


def try_openai_search(domain: str) -> dict | None:
    prompt = f"""Search for information about the Shopify store at {domain}.

Find data from: Store Leads (storeleads.app), BuiltWith, Wappalyzer, or similar tech intelligence tools.

I need:
- Shopify plan tier (Basic, Shopify, Advanced, Plus)
- Apps installed (Klaviyo, Recharge, Gorgias, Triple Whale, Judge.me, etc.)
- Revenue bracket or estimate
- Monthly traffic range
- Approximate launch/founding date
- Employee count if available

Return ONLY valid JSON:
{{
  "shopify_plan": "<plan or null>",
  "app_stack": ["app1", "app2"],
  "revenue_bracket": "<range or null>",
  "traffic_range": "<range or null>",
  "launch_date": "<year or date or null>",
  "employee_count": <int or null>,
  "notes": "any other relevant operational details"
}}"""

    raw = web_search(prompt)
    if not raw:
        return None
    return parse_json_from_text(raw)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--domain", required=True)
    args = ap.parse_args()

    domain = args.domain.replace("https://", "").replace("http://", "").strip("/")

    # Strategy 1: direct fetch
    html, status, url = try_direct(domain)
    if html and status == 200:
        parsed = parse_store_leads(html)
        print(json.dumps({
            "domain": domain,
            "url": url,
            "method": "direct_fetch",
            "shopify_plan": parsed.get("shopify_plan"),
            "app_stack": [],
            "revenue_bracket": parsed.get("revenue_bracket"),
            "traffic_range": parsed.get("traffic_range"),
            "launch_date": None,
            "employee_count": None,
            "note": "fetched directly; verify by opening URL",
        }, indent=2))
        return 0

    # Strategy 2: OpenAI web search
    result = try_openai_search(domain)
    if result:
        print(json.dumps({
            "domain": domain,
            "url": url,
            "method": "openai_web_search",
            "shopify_plan": result.get("shopify_plan"),
            "app_stack": result.get("app_stack", []),
            "revenue_bracket": result.get("revenue_bracket"),
            "traffic_range": result.get("traffic_range"),
            "launch_date": result.get("launch_date"),
            "employee_count": result.get("employee_count"),
            "note": result.get("notes", "retrieved via OpenAI web search"),
        }, indent=2))
        return 0

    # Fallback
    print(json.dumps({
        "domain": domain,
        "url": url,
        "method": "failed",
        "shopify_plan": None,
        "app_stack": [],
        "revenue_bracket": None,
        "traffic_range": None,
        "launch_date": None,
        "employee_count": None,
        "note": f"direct fetch {status}, web search unavailable",
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

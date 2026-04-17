#!/usr/bin/env python3
"""
importyeti_lookup.py — fetch ImportYeti public company page and extract supplier signals.

Usage:
    python importyeti_lookup.py --brand "Brand Name"

ImportYeti is the #1 skipped source in amateur DTC teardowns. This script is
MANDATORY — the validator fails the report if there is no ImportYeti entry in
the Sources section. A "no records found" result still counts.

Strategy:
1. Direct HTTP fetch (works when ImportYeti's CDN doesn't block)
2. OpenAI web search fallback (OPENAI_API_KEY required) — searches ImportYeti
   results via web, extracts supplier + country data from cached/indexed content

Output JSON: {brand, url, status, top_suppliers[], countries[], raw_html_len, note}
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

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


def try_direct(slug: str) -> tuple[str, int]:
    url = f"https://www.importyeti.com/company/{slug}"
    try:
        r = requests.get(url, headers=BROWSER_HEADERS, timeout=TIMEOUT)
        return r.text, r.status_code
    except Exception:
        return "", 0


def parse_suppliers(html: str) -> tuple[list[str], list[str]]:
    suppliers: list[str] = []
    countries: list[str] = []
    for m in re.finditer(r'href="/supplier/([^"]+)"[^>]*>([^<]+)</a>', html):
        name = m.group(2).strip()
        if name and name not in suppliers:
            suppliers.append(name)
        if len(suppliers) >= 10:
            break
    for m in re.finditer(r'country[^>]*>([A-Z][a-zA-Z ]{2,30})<', html):
        c = m.group(1).strip()
        if c and c not in countries:
            countries.append(c)
    return suppliers, countries


def try_openai_search(brand: str, slug: str) -> dict | None:
    url = f"https://www.importyeti.com/company/{slug}"
    prompt = f"""Search ImportYeti for "{brand}" and return what you find.

Look at: {url}
Also search: site:importyeti.com "{brand}" suppliers

Extract and return ONLY valid JSON:
{{
  "found": true/false,
  "top_suppliers": ["supplier1", "supplier2"],
  "countries": ["China", "USA"],
  "shipment_count": <int or null>,
  "notes": "any other relevant supply chain info"
}}

If no records are found on ImportYeti for this brand, return {{"found": false, "top_suppliers": [], "countries": [], "shipment_count": null, "notes": "no records found on ImportYeti"}}"""

    raw = web_search(prompt)
    if not raw:
        return None
    parsed = parse_json_from_text(raw)
    return parsed


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--brand", required=True)
    args = ap.parse_args()

    slug = quote(args.brand.strip().lower().replace(" ", "-"))
    url = f"https://www.importyeti.com/company/{slug}"

    # Strategy 1: direct fetch
    html, status = try_direct(slug)
    suppliers, countries = [], []
    if html and status == 200:
        suppliers, countries = parse_suppliers(html)

    if suppliers or (status == 200 and html):
        note = ("suppliers extracted via regex; verify by visiting url"
                if suppliers else "fetched but no supplier data extracted")
        print(json.dumps({
            "brand": args.brand, "url": url, "status": status,
            "method": "direct_fetch",
            "top_suppliers": suppliers, "countries": countries,
            "raw_html_len": len(html), "note": note,
        }, indent=2))
        return 0

    # Strategy 2: OpenAI web search
    result = try_openai_search(args.brand, slug)
    if result:
        print(json.dumps({
            "brand": args.brand, "url": url, "status": status,
            "method": "openai_web_search",
            "top_suppliers": result.get("top_suppliers", []),
            "countries": result.get("countries", []),
            "raw_html_len": 0,
            "note": result.get("notes", "retrieved via OpenAI web search"),
        }, indent=2))
        return 0

    # Fallback
    print(json.dumps({
        "brand": args.brand, "url": url, "status": status,
        "method": "failed",
        "top_suppliers": [], "countries": [], "raw_html_len": len(html),
        "note": f"direct fetch {status}, web search unavailable — check URL manually",
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

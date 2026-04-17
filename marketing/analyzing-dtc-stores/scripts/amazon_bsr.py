#!/usr/bin/env python3
"""
amazon_bsr.py — find Amazon BSR and review data for a brand.

Usage:
    python amazon_bsr.py --brand "Brand Name"

Amazon BSR (Best Seller Rank) is the best independent revenue signal for brands
selling on Amazon. This script tries to find BSR + review data via OpenAI web
search (Amazon blocks direct scraping), then falls back to a URL stub.

Output JSON: {brand, search_url, method, amazon_present, top_skus[], note}
top_skus: [{asin, title, bsr, bsr_category, est_monthly_units, reviews, rating, price}]
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).parent))
from _openai_search import web_search, parse_json_from_text


def try_openai_search(brand: str) -> dict | None:
    q = quote(brand)
    prompt = f"""Search Amazon for "{brand}" products and find their BSR (Best Sellers Rank) data.

Search: https://www.amazon.com/s?k={q}

For each product you find, extract:
- ASIN (product ID, format B0XXXXXXX)
- Product title
- BSR (Best Sellers Rank) and category
- Star rating and review count
- Price
- Estimate monthly unit sales from BSR using these rough benchmarks:
  BSR 1-100: 3,000-10,000+ units/month
  BSR 100-1000: 500-3,000 units/month
  BSR 1000-5000: 100-500 units/month
  BSR 5000-20000: 20-100 units/month
  BSR 20000+: <20 units/month

Return ONLY valid JSON:
{{
  "amazon_present": true/false,
  "top_skus": [
    {{
      "asin": "B0XXXXXXX",
      "title": "Product name",
      "bsr": <integer or null>,
      "bsr_category": "Pet Supplies",
      "est_monthly_units": <integer or null>,
      "reviews": <integer or null>,
      "rating": <float or null>,
      "price": "<$XX.XX or null>"
    }}
  ],
  "brand_store_url": "<url or null>",
  "notes": "any relevant Amazon channel observations"
}}

If the brand has no Amazon presence, return {{"amazon_present": false, "top_skus": [], "notes": "no Amazon listings found"}}"""

    raw = web_search(prompt)
    if not raw:
        return None
    return parse_json_from_text(raw)


def url_stub(brand: str) -> dict:
    q = quote(brand)
    return {
        "brand": brand,
        "search_url": f"https://www.amazon.com/s?k={q}",
        "method": "stub_only",
        "amazon_present": None,
        "top_skus": [],
        "note": (
            "OpenAI web search unavailable. Manual protocol: "
            "1. Search the URL above. "
            "2. Open each product page → Product Details section → BSR. "
            "3. Convert BSR to est. monthly units via FBAct.com free estimator. "
            "4. Cross-check units × price against DTC traffic to sanity-check channel mix."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--brand", required=True)
    args = ap.parse_args()

    brand = args.brand
    q = quote(brand)
    search_url = f"https://www.amazon.com/s?k={q}"

    result = try_openai_search(brand)
    if result:
        print(json.dumps({
            "brand": brand,
            "search_url": search_url,
            "method": "openai_web_search",
            "amazon_present": result.get("amazon_present"),
            "top_skus": result.get("top_skus", []),
            "brand_store_url": result.get("brand_store_url"),
            "note": result.get("notes", "retrieved via OpenAI web search"),
        }, indent=2))
        return 0

    print(json.dumps(url_stub(brand), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

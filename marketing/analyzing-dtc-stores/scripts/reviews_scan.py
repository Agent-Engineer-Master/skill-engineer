#!/usr/bin/env python3
"""
reviews_scan.py — emit URLs for multi-source review scan (Trustpilot, Amazon, Reddit, YouTube).

Usage:
    python reviews_scan.py --brand "Brand Name" --domain example.com

Output JSON: {brand, sources: [{name, url, expected_fields}]}
Claude opens each URL with WebFetch and fills the `expected_fields` into the
§10 Customer voice section. Review velocity (new reviews/month) is the key
triangulation number — compare against SimilarWeb and ad count.

NOTE: For Reddit, prefer calling reddit_search.py directly instead of WebFetching the URL:
    python reddit_search.py --brand "Brand Name"
It uses OpenAI web search (OPENAI_API_KEY required) and returns structured JSON.
"""
from __future__ import annotations
import argparse
import json
import sys
from urllib.parse import quote


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--brand", required=True)
    ap.add_argument("--domain", required=True)
    args = ap.parse_args()

    q = quote(args.brand)
    domain = args.domain.replace("https://", "").replace("http://", "").strip("/")

    sources = [
        {
            "name": "Trustpilot",
            "url": f"https://www.trustpilot.com/review/{domain}",
            "expected_fields": ["total_reviews", "average_rating", "top_praise_theme", "top_complaint_theme", "reviews_last_30_days"],
        },
        {
            "name": "Reddit brand search",
            "url": f"https://www.reddit.com/search/?q=%22{q}%22+review&sort=new",
            "expected_fields": ["thread_count", "sentiment", "top_complaint"],
        },
        {
            "name": "Amazon reviews (hero SKU)",
            "url": f"https://www.amazon.com/s?k={q}",
            "expected_fields": ["review_count_hero", "average_rating_hero", "top_complaint_hero"],
        },
        {
            "name": "YouTube haul/review",
            "url": f"https://www.youtube.com/results?search_query={q}+review",
            "expected_fields": ["influencer_count", "sentiment", "notable_creators"],
        },
        {
            "name": "Google reviews (if retail)",
            "url": f"https://www.google.com/search?q=%22{q}%22+reviews",
            "expected_fields": ["presence", "average"],
        },
    ]

    print(json.dumps({"brand": args.brand, "domain": domain, "sources": sources}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

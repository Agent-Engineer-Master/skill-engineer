#!/usr/bin/env python3
"""
reddit_search.py — search Reddit for brand mentions using OpenAI web search.

Usage:
    python reddit_search.py --brand "Little Hunter" [--limit 10]

Requires OPENAI_API_KEY in environment (or .env file in cwd / project root).

Uses the OpenAI Responses API with the web_search_preview tool to find Reddit
threads mentioning the brand, then summarises sentiment and top themes.

Output JSON:
  {brand, method, thread_count, sentiment, top_praise_theme, top_complaint_theme,
   threads: [{title, url, date, upvotes, summary}], raw_search_output}
"""
from __future__ import annotations
import argparse
import json
import os
import sys
from pathlib import Path


def load_env() -> None:
    """Load .env from cwd or two levels up (project root)."""
    for candidate in [Path.cwd() / ".env", Path.cwd().parent.parent / ".env"]:
        if candidate.exists():
            with open(candidate, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, _, v = line.partition("=")
                        os.environ.setdefault(k.strip(), v.strip())
            break


def search_reddit(brand: str, limit: int) -> dict:
    load_env()

    api_key = os.getenv("OPENAI_API_KEY", "")
    if not api_key:
        return {
            "brand": brand,
            "method": "openai_web_search",
            "error": "OPENAI_API_KEY not set",
            "thread_count": None,
            "sentiment": None,
            "top_praise_theme": None,
            "top_complaint_theme": None,
            "threads": [],
        }

    try:
        from openai import OpenAI
    except ImportError:
        return {
            "brand": brand,
            "method": "openai_web_search",
            "error": "openai package not installed",
            "thread_count": None,
            "sentiment": None,
            "top_praise_theme": None,
            "top_complaint_theme": None,
            "threads": [],
        }

    client = OpenAI(api_key=api_key)

    prompt = f"""Search Reddit for discussions about "{brand}".

Find up to {limit} relevant Reddit threads that mention "{brand}" — including reviews, complaints, recommendations, comparisons, and general discussions.

For each thread found, extract:
- title
- URL
- approximate date (if visible)
- approximate upvotes/score (if visible)
- 1-sentence summary of what the thread says about the brand

After listing threads, provide a structured summary:
- overall_sentiment: positive / mixed / negative / insufficient_data
- top_praise_theme: the most common positive thing people say (or null)
- top_complaint_theme: the most common complaint (or null)
- thread_count: total number of relevant threads found
- notable_quote: one verbatim quote from a Reddit comment about the brand (if found)

Return ONLY valid JSON in this exact structure:
{{
  "thread_count": <int or null>,
  "sentiment": "<positive|mixed|negative|insufficient_data>",
  "top_praise_theme": "<string or null>",
  "top_complaint_theme": "<string or null>",
  "notable_quote": "<string or null>",
  "threads": [
    {{"title": "...", "url": "...", "date": "...", "upvotes": <int or null>, "summary": "..."}}
  ]
}}"""

    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            tools=[{"type": "web_search_preview"}],
            input=prompt,
        )

        # Extract text output from response
        raw_text = ""
        for item in response.output:
            if hasattr(item, "content"):
                for block in item.content:
                    if hasattr(block, "text"):
                        raw_text += block.text

        # Try to parse the JSON block from the response
        # Strip markdown code fences if present
        json_text = raw_text.strip()
        if json_text.startswith("```"):
            json_text = json_text.split("```")[1]
            if json_text.startswith("json"):
                json_text = json_text[4:]
            json_text = json_text.strip()

        parsed = json.loads(json_text)
        parsed["brand"] = brand
        parsed["method"] = "openai_web_search"
        return parsed

    except json.JSONDecodeError:
        # Return raw text if JSON parsing fails
        return {
            "brand": brand,
            "method": "openai_web_search",
            "thread_count": None,
            "sentiment": "parse_error",
            "top_praise_theme": None,
            "top_complaint_theme": None,
            "threads": [],
            "raw_output": raw_text,
        }
    except Exception as e:
        return {
            "brand": brand,
            "method": "openai_web_search",
            "error": str(e),
            "thread_count": None,
            "sentiment": None,
            "top_praise_theme": None,
            "top_complaint_theme": None,
            "threads": [],
        }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--brand", required=True)
    ap.add_argument("--limit", type=int, default=10,
                    help="Max Reddit threads to find (default: 10)")
    args = ap.parse_args()

    result = search_reddit(args.brand, args.limit)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

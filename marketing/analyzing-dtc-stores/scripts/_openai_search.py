#!/usr/bin/env python3
"""
_openai_search.py — shared OpenAI web search helper for DTC teardown scripts.

Not called directly — imported by other scripts.
"""
from __future__ import annotations
import json
import os
from pathlib import Path


def load_env() -> None:
    for candidate in [Path.cwd() / ".env", Path(__file__).parent.parent.parent.parent.parent / ".env"]:
        if candidate.exists():
            with open(candidate, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, _, v = line.partition("=")
                        os.environ.setdefault(k.strip(), v.strip())
            break


def web_search(prompt: str, model: str = "gpt-4o-mini") -> str:
    """
    Run a web search via OpenAI Responses API.
    Returns raw text output, or empty string on failure.
    """
    load_env()
    api_key = os.getenv("OPENAI_API_KEY", "")
    if not api_key:
        return ""
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        response = client.responses.create(
            model=model,
            tools=[{"type": "web_search_preview"}],
            input=prompt,
        )
        raw = ""
        for item in response.output:
            if hasattr(item, "content"):
                for block in item.content:
                    if hasattr(block, "text"):
                        raw += block.text
        return raw.strip()
    except Exception:
        return ""


def parse_json_from_text(text: str) -> dict | None:
    """Extract first JSON object from a text blob (handles markdown fences)."""
    import re
    # Strip markdown fences
    text = re.sub(r"```(?:json)?", "", text).strip()
    # Find first {...} block
    m = re.search(r"\{[\s\S]*\}", text)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError:
        return None

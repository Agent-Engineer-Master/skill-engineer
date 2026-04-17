#!/usr/bin/env python3
"""
recon.py — fetch store homepage, robots.txt, sitemap.xml, and detect platform + apps.

Usage:
    python recon.py --url https://example.com

Writes JSON to stdout and caches raw HTML at ../.cache/recon-<slug>.json.

Output JSON keys: url, slug, platform, apps[], has_llms_txt, jsonld_blocks,
                  has_shop_pay, has_apple_pay, robots_txt_present, sitemap_present,
                  errors[].

Exits 0 even on partial failure — research continues with whatever was captured.
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

UA = "Mozilla/5.0 (compatible; dtc-break-down/1.0; +research)"
TIMEOUT = 15

# Regex signatures for popular DTC stack apps. Each pattern fires if present in view-source.
SIGNATURES = {
    "shopify": r"cdn\.shopify\.com|Shopify\.theme",
    "woocommerce": r"woocommerce|wp-content/plugins/woocommerce",
    "bigcommerce": r"cdn\d*\.bigcommerce\.com",
    "klaviyo": r"klaviyo\.com/onsite|static\.klaviyo",
    "gorgias": r"gorgias\.chat|gorgias\.com",
    "recharge": r"rechargepayments|recharge\.js",
    "skio": r"skio\.com|skio\.js",
    "triple_whale": r"triplewhale|tripleshopify",
    "northbeam": r"northbeam",
    "yotpo": r"yotpo",
    "okendo": r"okendo",
    "loop_returns": r"loopreturns\.com",
    "shop_pay": r"shop-pay|shoppay",
    "apple_pay": r"apple-pay|applepay",
    "meta_pixel": r"fbq\(|facebook\.net/.*/fbevents\.js",
    "tiktok_pixel": r"analytics\.tiktok\.com",
}


def fetch(url: str) -> tuple[str, int]:
    """Fetch a URL, return (body, status). Empty body on failure."""
    try:
        req = Request(url, headers={"User-Agent": UA})
        with urlopen(req, timeout=TIMEOUT) as r:
            return r.read().decode("utf-8", errors="replace"), r.status
    except (HTTPError, URLError, TimeoutError, ValueError) as e:
        return "", getattr(e, "code", 0)


def slugify(netloc: str) -> str:
    host = netloc.lower().removeprefix("www.")
    return re.sub(r"[^a-z0-9]+", "-", host).strip("-")


def extract_jsonld(html: str) -> list[dict]:
    """Extract JSON-LD blocks — signal for agentic-readiness."""
    blocks = []
    for m in re.finditer(
        r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        html, re.DOTALL | re.IGNORECASE,
    ):
        try:
            blocks.append(json.loads(m.group(1).strip()))
        except (json.JSONDecodeError, ValueError):
            # Malformed JSON-LD is common; ignore silently.
            pass
    return blocks


def detect_apps(html: str) -> list[str]:
    return [name for name, pat in SIGNATURES.items() if re.search(pat, html, re.IGNORECASE)]


def detect_platform(apps: list[str]) -> str:
    for p in ("shopify", "woocommerce", "bigcommerce"):
        if p in apps:
            return p
    return "unknown"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--cache-dir", default=str(Path(__file__).parent.parent / ".cache"))
    args = ap.parse_args()

    parsed = urlparse(args.url if "://" in args.url else f"https://{args.url}")
    base = f"{parsed.scheme}://{parsed.netloc}"
    slug = slugify(parsed.netloc)

    errors: list[str] = []

    home, status = fetch(base + "/")
    if not home:
        errors.append(f"homepage fetch failed (status={status})")

    robots, _ = fetch(base + "/robots.txt")
    sitemap, _ = fetch(base + "/sitemap.xml")
    llms, _ = fetch(base + "/llms.txt")

    apps = detect_apps(home)
    platform = detect_platform(apps)
    jsonld = extract_jsonld(home)

    result = {
        "url": base,
        "slug": slug,
        "platform": platform,
        "apps": apps,
        "has_llms_txt": bool(llms.strip()),
        "jsonld_blocks": len(jsonld),
        "has_shop_pay": "shop_pay" in apps,
        "has_apple_pay": "apple_pay" in apps,
        "robots_txt_present": bool(robots.strip()),
        "sitemap_present": bool(sitemap.strip()),
        "errors": errors,
    }

    cache_dir = Path(args.cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    (cache_dir / f"recon-{slug}.json").write_text(
        json.dumps({**result, "homepage_html_len": len(home)}, indent=2),
        encoding="utf-8",
    )

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Initialize an industry-analysis run.

Creates the industry folder structure under 08-knowledge/world-model/industries/[slug]/
and writes the initial run-log entry.

Usage:
    python init_analysis.py --slug <industry-slug> --question "<scope-question>" --mode <quick|deep>

Expected stdout:
    Path to the created industry folder.

Error taxonomy:
    - SlugExists: folder exists and --force not set
    - InvalidSlug: slug fails lowercase-hyphen validation
"""

import argparse
import datetime
import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[5]
INDUSTRIES_DIR = REPO_ROOT / "08-knowledge" / "world-model" / "industries"


def validate_slug(slug: str) -> bool:
    return bool(re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", slug))


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize industry-analysis run.")
    parser.add_argument("--slug", required=True, help="Industry slug (lowercase, hyphens).")
    parser.add_argument("--question", required=True, help="Scope question for this analysis.")
    parser.add_argument("--mode", choices=["quick", "deep"], default="quick")
    parser.add_argument("--force", action="store_true", help="Overwrite existing folder.")
    args = parser.parse_args()

    if not validate_slug(args.slug):
        print(f"ERROR InvalidSlug: '{args.slug}' must be lowercase with hyphens only.", file=sys.stderr)
        return 2

    industry_dir = INDUSTRIES_DIR / args.slug
    if industry_dir.exists() and not args.force:
        print(f"ERROR SlugExists: {industry_dir} exists. Use --force to overwrite or pick a different slug.", file=sys.stderr)
        return 2

    (industry_dir / "working").mkdir(parents=True, exist_ok=True)

    metadata = {
        "industry_slug": args.slug,
        "scope_question": args.question,
        "mode": args.mode,
        "created": datetime.datetime.utcnow().isoformat() + "Z",
        "events": [{"event": "initialized", "ts": datetime.datetime.utcnow().isoformat() + "Z"}],
    }
    (industry_dir / "run-log.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    (industry_dir / "signals-log.md").write_text(
        f"# Signals Log — {args.slug}\n\nAppend-only catalysts and discontinuities.\n",
        encoding="utf-8",
    )

    print(str(industry_dir))
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Append an event to the industry-analysis run log.

Usage:
    python log_run.py --slug <industry-slug> --event <event-name> [--note "..."]

Appends to <industry-dir>/run-log.json.
"""

import argparse
import datetime
import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[5]
INDUSTRIES_DIR = REPO_ROOT / "08-knowledge" / "world-model" / "industries"


def main() -> int:
    parser = argparse.ArgumentParser(description="Log an event to the industry-analysis run log.")
    parser.add_argument("--slug", required=True)
    parser.add_argument("--event", required=True)
    parser.add_argument("--note", default="")
    args = parser.parse_args()

    industry_dir = INDUSTRIES_DIR / args.slug
    log_path = industry_dir / "run-log.json"
    if not log_path.exists():
        print(f"ERROR RunLogMissing: {log_path} not found — run init_analysis.py first.", file=sys.stderr)
        return 2

    metadata = json.loads(log_path.read_text(encoding="utf-8"))
    metadata.setdefault("events", []).append({
        "event": args.event,
        "ts": datetime.datetime.utcnow().isoformat() + "Z",
        "note": args.note,
    })
    log_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    print(f"Logged: {args.event}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

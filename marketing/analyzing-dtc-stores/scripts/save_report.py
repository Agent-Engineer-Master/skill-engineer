#!/usr/bin/env python3
"""
save_report.py — save a validated DTC teardown to 08-knowledge/resources/.

Usage:
    python save_report.py --path draft.md --slug brand-name [--no-save] [--root /path/to/EA]

Writes to:
    <root>/08-knowledge/resources/YYYY-MM-DD-dtc-teardown-<slug>.md

If --no-save is passed, prints the would-be path but does NOT write. This
supports ad-hoc inline runs.

Convention: librarian naming — dated filename, kebab-case slug, resources dir.
"""
from __future__ import annotations
import argparse
import datetime as dt
import sys
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", required=True, help="draft markdown file")
    ap.add_argument("--slug", required=True, help="brand slug, e.g. 'true-norma'")
    ap.add_argument("--no-save", action="store_true")
    ap.add_argument(
        "--root",
        default=str(Path(__file__).resolve().parents[4]),  # .../executive-assistant
        help="EA root directory",
    )
    args = ap.parse_args()

    draft = Path(args.path)
    if not draft.exists():
        print(f"ERROR: draft not found: {draft}", file=sys.stderr)
        return 2

    date = dt.date.today().isoformat()
    target_dir = Path(args.root) / "08-knowledge" / "resources"
    target = target_dir / f"{date}-dtc-teardown-{args.slug}.md"

    if args.no_save:
        print(f"[--no-save] would write: {target}")
        return 0

    target_dir.mkdir(parents=True, exist_ok=True)
    target.write_text(draft.read_text(encoding="utf-8"), encoding="utf-8")
    print(str(target))
    return 0


if __name__ == "__main__":
    sys.exit(main())

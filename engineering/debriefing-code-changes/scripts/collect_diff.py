#!/usr/bin/env python3
"""Collect a compact git change manifest for the debriefing-code-changes skill."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str]) -> str:
    result = subprocess.run(cmd, text=True, capture_output=True)
    if result.returncode != 0:
        raise SystemExit(f"Command failed: {' '.join(cmd)}\n{result.stderr.strip()}")
    return result.stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Collect git diff facts for a learning debrief")
    parser.add_argument("range", nargs="?", default=None, help="Git range, e.g. main...HEAD or HEAD~1..HEAD. Omit for working tree diff.")
    parser.add_argument("--max-diff-chars", type=int, default=20000)
    args = parser.parse_args()

    if not Path(".git").exists():
        raise SystemExit("Run from the root of a git repository.")

    if args.range:
        name_status = run(["git", "diff", "--name-status", args.range])
        stat = run(["git", "diff", "--stat", args.range])
        diff = run(["git", "diff", "--find-renames", "--find-copies", args.range])
        commits = run(["git", "log", "--oneline", args.range])
    else:
        name_status = run(["git", "diff", "--name-status"])
        stat = run(["git", "diff", "--stat"])
        diff = run(["git", "diff", "--find-renames", "--find-copies"])
        commits = "working tree"

    payload = {
        "range": args.range or "working tree",
        "commits": commits.splitlines(),
        "files": [line for line in name_status.splitlines() if line],
        "stat": stat,
        "diff_truncated": len(diff) > args.max_diff_chars,
        "diff": diff[: args.max_diff_chars],
    }
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

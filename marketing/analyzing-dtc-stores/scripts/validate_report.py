#!/usr/bin/env python3
"""
validate_report.py — hard gate before saving a DTC teardown.

Usage:
    python validate_report.py --path path/to/draft.md

Exit 0 if the report passes. Exit 1 and print a remediation list otherwise.
Claude MUST fix every failure and re-run before Step 7 (save).

Checks:
    1. All 16 sections present (headers matching §0 — §16)
    2. Sources section has at least 5 entries
    3. ImportYeti appears somewhere in Sources (even 'no records found')
    4. No banned hype words
    5. Verdict has a numerical 'change my mind' anchor (regex for $/£/€ or %)
    6. No unsourced numeric claims — every '$X', 'Y%', 'N×' is followed
       within 60 chars by either a citation [N] or the '~ (est.' marker
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

BANNED = [
    "revolutionary", "disruptive", "game-changing", "game changing",
    "cutting-edge", "cutting edge", "seamless", "unparalleled",
]

REQUIRED_SECTIONS = [f"§{i}" for i in range(0, 17)]  # §0..§16

NUMERIC_CLAIM = re.compile(
    r"(\$\s?\d[\d,.]*\s*[KMB]?|\d[\d,.]*\s*%|\d[\d,.]*\s*×|\d[\d,.]*\s*x\b)"
)
CITATION_OR_EST = re.compile(r"\[\d+\]|~\s*\(est\.")


def check(report: str) -> list[str]:
    failures: list[str] = []

    # 1. Sections
    for s in REQUIRED_SECTIONS:
        if s not in report:
            failures.append(f"missing section marker: {s}")

    # 2. Sources — look for numbered sources in §16
    m = re.search(r"§16[^§]*", report, re.DOTALL)
    sources_block = m.group(0) if m else ""
    source_entries = re.findall(r"^\s*\[\d+\]", sources_block, re.MULTILINE)
    if len(source_entries) < 5:
        failures.append(
            f"sources section has {len(source_entries)} entries, need ≥5 — "
            "add more cited sources, or mark missing ones explicitly"
        )

    # 3. ImportYeti mention
    if "importyeti" not in report.lower() and "import yeti" not in report.lower():
        failures.append(
            "no ImportYeti entry in Sources — mandatory check. "
            "If no records found, cite 'ImportYeti — no shipment records found, accessed YYYY-MM-DD'"
        )

    # 4. Banned hype words
    lower = report.lower()
    for word in BANNED:
        if word in lower:
            failures.append(f"banned hype word: '{word}' — rewrite the sentence")

    # 5. Verdict numerical anchor
    m = re.search(r"§15[^§]*", report, re.DOTALL)
    verdict_block = m.group(0) if m else ""
    if "change my mind" not in verdict_block.lower():
        failures.append("verdict missing 'change my mind' line in §15")
    if not re.search(r"\$[\d,]+|£[\d,]+|€[\d,]+|\d+\s*%", verdict_block):
        failures.append(
            "verdict has no numerical anchor — add a valuation $ range or margin % threshold"
        )

    # 6. Unsourced numeric claims — scan analytical sections only, skip §16 sources and template placeholders
    analytical = re.sub(r"§16.*", "", report, flags=re.DOTALL)
    analytical = re.sub(r"\{\{[^}]+\}\}", "", analytical)  # strip template vars
    lines = analytical.splitlines()
    unsourced = 0
    for line in lines:
        line_stripped = line.strip()
        if not line_stripped or line_stripped.startswith(("|", "#", "-", "*")):
            # Skip table rows and list markers — they're checked as blocks above
            continue
        for m in NUMERIC_CLAIM.finditer(line):
            # Look within 60 chars of the match for a citation or est marker
            window = line[max(0, m.start() - 60): m.end() + 60]
            if not CITATION_OR_EST.search(window):
                unsourced += 1
                if unsourced <= 3:  # only show first 3
                    failures.append(
                        f"unsourced numeric claim: '{m.group(0)}' — add [N] citation or ~ (est., method: …)"
                    )
    if unsourced > 3:
        failures.append(f"...and {unsourced - 3} more unsourced numeric claims")

    return failures


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", required=True)
    args = ap.parse_args()

    p = Path(args.path)
    if not p.exists():
        print(f"ERROR: report not found: {p}", file=sys.stderr)
        return 2

    report = p.read_text(encoding="utf-8")
    failures = check(report)

    if not failures:
        print("OK: report passes all validation checks")
        return 0

    print("VALIDATION FAILED — fix each issue and re-run:")
    for f in failures:
        print(f"  - {f}")
    return 1


if __name__ == "__main__":
    sys.exit(main())

"""Validate a five-forces output against the map-five-forces discipline.

Checks (v2):
- All 5 classical forces present + Complementors + AI-as-force
- Governing force sentence present (the single causal sentence)
- At least one force is High or Low (not universal-Moderate)
- V/C/A/I tag coverage
- AI sub-checks present (cost-structure / new-entry / data-intermediary)
- Direction-of-travel arrows present on all 7 forces (NEW v2)
- Focal-layer specification present (NEW v2)
- AI reshape matrix present (NEW v2)
- All-stable warning (soft, non-failing) — flags lack of trajectory engagement (NEW v2)
- Heatmap table present with required column headers (NEW v3)
- Inline AI-reshape commentary near each of the 5 classical forces (NEW v3)
- Structured next_skills YAML block at end (NEW v3)

Usage:
    python validate_forces.py --output-path <path-to-five-forces.md>

Exit codes:
    0 — pass
    1 — fail
    2 — file missing
"""

import argparse
import re
import sys
from pathlib import Path


REQUIRED_FORCES = [
    ("Rivalry", r"\brivalry\b"),
    ("Supplier Power", r"\bsupplier power\b"),
    ("Buyer Power", r"\bbuyer power\b"),
    ("Threat of New Entry", r"\b(new entry|new entrants|threat of (new )?entry)\b"),
    ("Threat of Substitutes", r"\bsubstitutes?\b"),
    ("Complementors", r"\bcomplementors?\b"),
    ("AI as Force", r"\bAI\b"),
]

# Direction-of-travel markers: arrows OR explicit words.
# Accepts either Unicode arrows or the words intensifying/stable/weakening.
DIRECTION_PATTERN = r"(↑|↔|↓|intensifying|stable|weakening)"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-path", required=True)
    args = parser.parse_args()

    path = Path(args.output_path)
    if not path.exists():
        print(f"ERROR FileMissing: {path}", file=sys.stderr)
        return 2

    content = path.read_text(encoding="utf-8")
    failures = []
    warnings = []

    # Check 1: all six forces present (5 + complementors + AI)
    for name, pattern in REQUIRED_FORCES:
        if not re.search(pattern, content, re.IGNORECASE):
            failures.append(f"Missing required force: {name}")

    # Check 2: governing force sentence
    if not re.search(r"governing force", content, re.IGNORECASE):
        failures.append("Missing 'governing force' sentence. Must name THE force that determines profit distribution in one causal sentence.")

    # Check 3: not universal-moderate (at least one High or Low rating in addition to Moderates)
    high_count = len(re.findall(r"\bhigh\b", content, re.IGNORECASE))
    low_count = len(re.findall(r"\blow\b", content, re.IGNORECASE))
    moderate_count = len(re.findall(r"\bmoderate\b", content, re.IGNORECASE))
    if high_count == 0 and low_count == 0 and moderate_count >= 5:
        failures.append("Universal-Moderate detected. At least one force must be High or Low. Five 'Moderate' forces = checklist analysis, not insight.")

    # Check 4: AI sub-checks
    ai_sub_checks = [
        ("cost-structure", r"cost[- ]structure"),
        ("new-entry vector", r"new[- ]entry"),
        ("data-intermediary", r"data[- ]intermediary"),
    ]
    for sub_name, sub_pattern in ai_sub_checks:
        if not re.search(sub_pattern, content, re.IGNORECASE):
            failures.append(f"AI section missing sub-check: {sub_name}")

    # Check 5: V/C/A/I tag coverage
    tag_count = len(re.findall(r"\[(V|C|A|I):", content))
    if tag_count < 6:
        failures.append(f"Insufficient provenance tag coverage. Found {tag_count} V/C/A/I tags. Each force should have at least 1 tagged evidence claim.")

    # Check 6 (NEW v2): direction-of-travel arrows present.
    # Require at least 5 distinct direction markers — one per major force minimum.
    # Look for 'Direction:' lines specifically; fall back to arrow count if format varies.
    direction_lines = re.findall(r"(?i)direction[:\s]+(?:\*+)?\s*" + DIRECTION_PATTERN, content)
    if len(direction_lines) < 5:
        failures.append(
            f"Insufficient direction-of-travel coverage. Found {len(direction_lines)} 'Direction:' arrows; "
            f"need at least 5 (one per classical force + complementors + AI). See references/dynamism.md."
        )

    # Check 7 (NEW v2): focal-layer specification.
    # Accepts 'Focal layer:', 'Focal-layer:', or 'Layer:' near the top.
    if not re.search(r"(?im)^.*\b(focal[- ]?layer|focal[- ]?layer specification|layer)\s*[:\-]", content):
        failures.append(
            "Missing focal-layer specification. Five Forces output must declare the value-chain layer "
            "(e.g., 'Focal layer: OEM' or 'Focal layer: fabless design'). Same industry has different forces at different layers."
        )

    # Check 8 (v3): AI reshape matrix present AND inline AI-reshape commentary
    # near each of the 5 classical forces (the word 'AI' within ~500 chars of each
    # classical force section header).
    reshape_present = bool(re.search(r"(?i)reshape", content))
    if not reshape_present:
        failures.append(
            "Missing AI reshape matrix. AI is not just a sixth force — it transforms each classical force. "
            "Add the 'AI Reshape Matrix' section per references/ai-as-force.md."
        )

    # Inline per-force AI commentary: for each classical force header, the word 'AI'
    # must appear within 500 chars after the header.
    CLASSICAL_FORCE_HEADERS = [
        ("Rivalry", r"(?im)^#{1,6}[^\n]*\brivalry\b"),
        ("Supplier Power", r"(?im)^#{1,6}[^\n]*\bsupplier power\b"),
        ("Buyer Power", r"(?im)^#{1,6}[^\n]*\bbuyer power\b"),
        ("Threat of New Entry", r"(?im)^#{1,6}[^\n]*\b(new entry|new entrants|threat of (new )?entry)\b"),
        ("Threat of Substitutes", r"(?im)^#{1,6}[^\n]*\bsubstitutes?\b"),
    ]
    missing_inline_ai = []
    for force_name, header_pattern in CLASSICAL_FORCE_HEADERS:
        m = re.search(header_pattern, content)
        if not m:
            # Header style not found — skip (other checks will catch missing force).
            continue
        window = content[m.start(): m.start() + 500]
        if not re.search(r"\bAI\b", window):
            missing_inline_ai.append(force_name)
    if missing_inline_ai:
        failures.append(
            "Missing inline AI-reshape commentary near classical force(s): "
            f"{', '.join(missing_inline_ai)}. Each classical force section must include how AI "
            "is reshaping that force (intensifying / weakening / no material effect) inline — "
            "the consolidated matrix is a summary, not a substitute. See SKILL.md step 2(d)."
        )

    # Check 10 (NEW v3): heatmap table present near top of output with required column headers.
    # Required signature: a markdown table row containing Force, Intensity, Direction, Governs?.
    heatmap_header_pattern = (
        r"\|\s*Force\s*\|[^\n]*\bIntensity\b[^\n]*\bDirection\b[^\n]*\bGoverns\?\s*\|"
    )
    if not re.search(heatmap_header_pattern, content, re.IGNORECASE):
        failures.append(
            "Missing at-a-glance heatmap table. Output must include a markdown table near the top "
            "with column headers 'Force', 'Intensity', 'Direction', and 'Governs?'. "
            "See assets/heatmap-template.md."
        )

    # Check 11 (NEW v3): structured next_skills YAML block at end of file.
    # Look for a YAML fence near the end containing 'next_skills:' with at least one '- <skill>' entry.
    tail = content[-2000:]
    next_skills_match = re.search(
        r"---\s*\n\s*next_skills\s*:\s*\n((?:\s*-\s*[^\n]+\n)+)\s*---",
        tail,
    )
    if not next_skills_match:
        failures.append(
            "Missing structured next_skills YAML block at end of file. Output must end with a "
            "'---\\nnext_skills:\\n  - <skill-name>\\n---' block listing at least one recommended "
            "next skill for orchestrator Phase 2 handoff. See SKILL.md step 9."
        )

    # Check 9 (NEW v2, soft warning): all-stable trajectory.
    # If every detected direction marker is 'stable' or '↔', warn — real industries always have at least one trajectory.
    if direction_lines:
        non_stable = [d for d in direction_lines if d.lower() not in ("stable", "↔")]
        if not non_stable:
            warnings.append(
                "All-stable trajectory detected. Every direction-of-travel arrow says 'stable'. "
                "Real industries always have at least one intensifying or weakening force. See references/dynamism.md."
            )

    # Report.
    if failures:
        print("VALIDATION FAILED:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        if warnings:
            print("\nWARNINGS:", file=sys.stderr)
            for w in warnings:
                print(f"  - {w}", file=sys.stderr)
        return 1

    if warnings:
        print(f"VALIDATION PASSED with {len(warnings)} warning(s): {path}")
        for w in warnings:
            print(f"  WARN: {w}")
    else:
        print(f"VALIDATION PASSED: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

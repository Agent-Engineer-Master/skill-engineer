"""Validate a competitive-arena output against the map-competitive-arena discipline.

Checks:
- >=3 strategic groups identified (single-group or 2-group analysis usually wrong)
- 2-axis visualization present (markdown table OR coordinate notation)
- Axis-selection rationale present
- Each group has a named basis of competition
- Each group has a named winner archetype (or explicit 'none emerging')
- Mobility-barrier matrix present with >=1 barrier per adjacent-group pair
- V/C/A/I tag coverage >=6
- Focal-layer specification present
- Arenas-overlay section present (or explicit 'not applicable')
- Trailing next_skills YAML block with >=1 entry

Usage:
    python validate_arena.py --output-path <path-to-competitive-arena.md>

Exit codes:
    0 — pass
    1 — fail
    2 — file missing
"""

import argparse
import re
import sys
from pathlib import Path


WINNER_ARCHETYPES = [
    r"consolidator",
    r"innovator[- ]?(specialist)?",
    r"specialist",
    r"platform[- ]?orchestrator",
    r"vertically[- ]?integrated",
    r"asset[- ]?light",
    r"none[- ]?emerging",
]

ARENAS_CLASSIFICATIONS = ["arena", "pre-arena", "mature", "contested mature", "declining"]


def count_strategic_groups(content: str) -> int:
    """Count strategic groups via 'Group N' or 'Group [N]' markdown headings."""
    # Look for headings like "### Group 1", "### Group 2 — Name", etc.
    matches = re.findall(r"(?im)^#{2,6}\s+Group\s+\d+", content)
    return len(matches)


def has_2axis_viz(content: str) -> bool:
    """Detect a 2-axis visualization: either a grid markdown table with axis labels,
    or a coordinate notation block."""
    # Grid table: look for 'Axes:' declaration AND a markdown table.
    has_axes_decl = bool(re.search(r"(?im)^\*?\*?Axes\*?\*?\s*:", content))
    has_table = bool(re.search(r"\n\|[^\n]+\|[^\n]+\|", content))
    if has_axes_decl and has_table:
        return True
    # Coordinate notation: look for fenced block with axis arrows
    if re.search(r"(?s)```[^`]*↑[^`]*→[^`]*```", content):
        return True
    return False


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

    # Check 1: >=3 strategic groups
    group_count = count_strategic_groups(content)
    if group_count < 3:
        failures.append(
            f"Insufficient strategic groups. Found {group_count} 'Group N' headings; need >=3. "
            "Single- or two-group analysis usually indicates correlated axes or non-discriminating "
            "axis selection. See references/strategic-groups.md."
        )

    # Check 2: 2-axis visualization
    if not has_2axis_viz(content):
        failures.append(
            "Missing 2-axis visualization. Output must include either a grid markdown table with "
            "an 'Axes:' declaration, or a coordinate notation block. See assets/strategic-group-template.md."
        )

    # Check 3: axis-selection rationale
    if not re.search(r"(?i)axis[- ]?(selection )?rationale|axis rationale|why these (two )?axes", content):
        failures.append(
            "Missing axis-selection rationale. Output must explain WHY these two axes were chosen "
            "(discriminating, uncorrelated, choice-based — not outcomes). See references/strategic-groups.md."
        )

    # Check 4: each group has 'basis of competition'
    basis_count = len(re.findall(r"(?i)basis of competition", content))
    if basis_count < group_count and group_count >= 3:
        failures.append(
            f"Each group must name a 'basis of competition'. Found {basis_count} occurrences "
            f"vs {group_count} groups. Add to each group profile block."
        )

    # Check 5: each group has a winner archetype
    archetype_pattern = r"(?i)winner[- ]?archetype\s*[:\-]?\s*[*_`]*\s*(" + "|".join(WINNER_ARCHETYPES) + ")"
    archetype_count = len(re.findall(archetype_pattern, content))
    if archetype_count < group_count and group_count >= 3:
        failures.append(
            f"Each group must name a winner archetype. Found {archetype_count} explicit "
            f"'winner_archetype:' declarations vs {group_count} groups. Use one of: consolidator, "
            "innovator-specialist, platform-orchestrator, vertically-integrated, asset-light, "
            "or 'none-emerging' with reason. See references/winner-archetypes.md."
        )

    # Check 6: mobility-barrier section + per-pair detail
    if not re.search(r"(?i)mobility[- ]barrier", content):
        failures.append(
            "Missing mobility-barriers section. Output must assess what prevents firms from moving "
            "between adjacent groups. See references/mobility-barriers.md."
        )
    else:
        # Require at least one mobility-barrier mention per (group_count - 1) adjacent pair
        # (minimum 2 adjacent pairs for 3 groups).
        # Simple heuristic: look for the mobility-barrier matrix table OR adjacent-pair elaboration.
        has_barrier_matrix = bool(
            re.search(r"(?im)^\|[^\n]*From[^\n]*To[^\n]*\|", content)
            or re.search(r"(?i)adjacent[- ]pair", content)
        )
        if not has_barrier_matrix:
            failures.append(
                "Mobility-barriers section present but lacks per-pair detail. Add either a "
                "'From \\ To' matrix or 'Adjacent-pair elaboration' subsections naming >=1 barrier "
                "per adjacent group pair. See assets/strategic-group-template.md."
            )

    # Check 7: V/C/A/I tag coverage
    tag_count = len(re.findall(r"\[(V|C|A|I):", content))
    if tag_count < 6:
        failures.append(
            f"Insufficient provenance tag coverage. Found {tag_count} V/C/A/I tags; need >=6. "
            "Each group profile should carry >=1 tagged evidence claim (size, profitability, etc.). "
            "See _shared/provenance-tagging.md."
        )

    # Check 8: focal-layer specification
    if not re.search(r"(?im)\b(focal[- ]?layer|focal[- ]?value[- ]?chain[- ]?layer|layer)\s*[:\-]", content):
        failures.append(
            "Missing focal-layer specification. Strategic-group structure differs by value-chain "
            "layer; declare which layer this analysis covers (e.g., 'Focal layer: OEM')."
        )

    # Check 9: arenas-overlay section present OR explicitly justified as N/A
    has_arenas_section = bool(re.search(r"(?i)arenas?[- ]overlay", content))
    has_classification = any(re.search(rf"(?i)\b{c}\b", content) for c in ARENAS_CLASSIFICATIONS)
    if not has_arenas_section:
        failures.append(
            "Missing 'Arenas overlay' section. Add the section with the upstream sizing's market "
            "classification and per-classification overlay, OR explicitly note 'Arenas overlay not "
            "applicable — market classified [X]'. See references/arenas-overlay.md."
        )
    elif not has_classification:
        failures.append(
            "Arenas overlay present but no market classification (Arena / Pre-arena / Mature / "
            "Contested mature / Declining) named. See references/arenas-overlay.md."
        )

    # Check 10: trailing next_skills YAML block
    tail = content[-2000:]
    next_skills_match = re.search(
        r"---\s*\n\s*next_skills\s*:\s*\n((?:\s*-\s*[^\n]+\n)+)\s*---",
        tail,
    )
    if not next_skills_match:
        failures.append(
            "Missing trailing next_skills YAML block. Output must end with "
            "'---\\nnext_skills:\\n  - <skill-name>\\n---' listing >=1 recommended next skill. "
            "See SKILL.md step 10."
        )

    if failures:
        print("VALIDATION FAILED:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1

    print(f"VALIDATION PASSED: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

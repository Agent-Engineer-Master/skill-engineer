"""Validate a strategic-environment output against the assess-strategic-environment discipline.

Checks:
- Classification is one of the 5 named environments (Classical / Adaptive / Visionary / Shaping / Renewal)
- All 3 diagnostic dimensions (predictability, malleability, harshness) each have a section
  with a rating (High/Medium/Low) AND at least one V/C/A/I tag in the same section
- Routing matrix table present, enumerating all 7 Phase 1+2 sub-skills with weight column
- `map-five-forces` is NOT weighted "skip" in the routing matrix
- V/C/A/I provenance tag coverage >= 3 overall
- Trailing `next_skills:` YAML block present with >= 3 entries
- Direction-of-travel statement present (one of: Stable, Transitioning)
- Ambidexterity either declared or explicitly noted as absent
- Causal classification sentence present (form: "[industry] is [Env] because ...")
- Default-failure guard: if every dimension is "Medium" the diagnosis is incomplete

Usage:
    python validate_environment.py --output-path <path-to-strategic-environment.md>

Exit codes:
    0 — all checks pass
    1 — one or more checks fail (details to stderr)
    2 — file missing or malformed
"""

import argparse
import re
import sys
from pathlib import Path

VALID_ENVIRONMENTS = ["Classical", "Adaptive", "Visionary", "Shaping", "Renewal"]
REQUIRED_DIMENSIONS = ["predictability", "malleability", "harshness"]
REQUIRED_SUB_SKILLS = [
    "size-market",
    "map-five-forces",
    "map-value-chain-profit-pools",
    "map-competitive-arena",
    "analyze-trajectory",
    "assess-moat-sources",
    "analyze-demand",
]
VALID_WEIGHTS = ["heavy", "light", "skip"]


def find_dimension_section(content: str, dim: str) -> str | None:
    """Return the text of the dimension's section (header through next header)."""
    # Match a heading line containing the dimension name PLUS following text until next heading.
    # Include the heading itself (rating often appears on the heading line: "## Predictability: Low").
    pattern = rf"(?im)^(#{{1,6}}\s*[^\n]*\b{dim}\b[^\n]*\n.*?)(?=^#{{1,6}}\s|\Z)"
    m = re.search(pattern, content, re.DOTALL)
    return m.group(1) if m else None


def check_dimensions(content: str) -> tuple[list[str], dict[str, str | None]]:
    """Each dimension needs a section, a rating, and a V/C/A/I tag in that section."""
    failures = []
    ratings: dict[str, str | None] = {}
    for dim in REQUIRED_DIMENSIONS:
        section = find_dimension_section(content, dim)
        if not section:
            failures.append(f"Missing dimension section for '{dim}'. Add a heading containing the word '{dim}'.")
            ratings[dim] = None
            continue
        # Rating present?
        rating_m = re.search(r"\b(High|Medium|Low)\b", section)
        if not rating_m:
            failures.append(f"Dimension '{dim}' section lacks an explicit High/Medium/Low rating.")
            ratings[dim] = None
        else:
            ratings[dim] = rating_m.group(1)
        # Tag present in section?
        if not re.search(r"\[(V|C|A|I):", section):
            failures.append(f"Dimension '{dim}' section lacks a V/C/A/I-tagged evidence claim.")
    return failures, ratings


def check_classification(content: str) -> list[str]:
    """Classification must be one of the 5 named environments, named in causal sentence form."""
    failures = []
    # Find an explicit classification statement
    env_present = [e for e in VALID_ENVIRONMENTS if re.search(rf"\b{e}\b", content)]
    if not env_present:
        failures.append(
            f"No environment classification found. Output must name one of: {', '.join(VALID_ENVIRONMENTS)}."
        )
        return failures
    # Look for a causal sentence pattern: "... is <Env> because ..."
    causal_pattern = rf"\bis\s+(?:{'|'.join(VALID_ENVIRONMENTS)})\b[^.]*\bbecause\b"
    if not re.search(causal_pattern, content, re.IGNORECASE):
        failures.append(
            "Missing causal classification sentence. Required form: '[Industry] is [Environment] because [evidence on all three dimensions].'"
        )
    return failures


def check_routing_matrix(content: str) -> list[str]:
    """All 7 sub-skills present in a routing-matrix table, each with a weight; map-five-forces != skip."""
    failures = []
    # Find the routing-matrix section (heading containing 'routing')
    routing_pattern = r"(?im)^#{1,6}\s*[^\n]*routing[^\n]*\n(.*?)(?=^#{1,6}\s|\Z)"
    m = re.search(routing_pattern, content, re.DOTALL)
    if not m:
        failures.append("Missing routing matrix section. Add a heading containing the word 'routing' with a table enumerating all 7 sub-skills.")
        return failures
    section = m.group(1)
    # Each sub-skill must appear in the routing section with a weight tag (heavy|light|skip) nearby
    for skill in REQUIRED_SUB_SKILLS:
        # Pattern: skill name on the same line as a weight word
        line_pattern = rf"(?im)^.*\b{re.escape(skill)}\b.*\b(heavy|light|skip)\b.*$"
        sm = re.search(line_pattern, section)
        if not sm:
            failures.append(f"Routing matrix missing sub-skill '{skill}' or its weight (heavy/light/skip).")
            continue
        weight = sm.group(1).lower()
        if skill == "map-five-forces" and weight == "skip":
            failures.append("map-five-forces is weighted 'skip' — never permitted; Five Forces is required in all environments.")
    return failures


def check_next_skills_yaml(content: str) -> list[str]:
    """Trailing YAML block with `next_skills:` and >=3 list items."""
    failures = []
    trailing = content.rstrip()
    block_match = re.search(r"---\s*\n((?:.*\n)*?)---\s*\Z", trailing, re.MULTILINE)
    if not block_match:
        failures.append("Missing trailing YAML block. Append a `---\\nnext_skills:\\n  - skill\\n  - skill\\n  - skill\\n---` block at end of file.")
        return failures
    block = block_match.group(1)
    if not re.search(r"^\s*next_skills:\s*$", block, re.MULTILINE):
        failures.append("Trailing YAML block missing `next_skills:` key.")
        return failures
    after = block.split("next_skills:", 1)[1]
    list_items = re.findall(r"^\s*-\s+\S+", after, re.MULTILINE)
    if len(list_items) < 3:
        failures.append(f"`next_skills:` requires >=3 entries (Phase 1 trio + environment-heavy Phase 2 skills). Found {len(list_items)}.")
    return failures


def check_default_failure_guard(ratings: dict[str, str | None]) -> list[str]:
    """All-Medium across the board = analyst dodged the call."""
    if all(r == "Medium" for r in ratings.values() if r is not None) and len([r for r in ratings.values() if r]) == 3:
        return [
            "All three dimensions rated 'Medium' — analytical dodge. Resolve to the leaning side per dimension OR declare ambidexterity."
        ]
    return []


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-path", required=True)
    args = parser.parse_args()

    path = Path(args.output_path)
    if not path.exists():
        print(f"ERROR FileMissing: {path}", file=sys.stderr)
        return 2

    content = path.read_text(encoding="utf-8")
    failures: list[str] = []
    warnings: list[str] = []

    # Check 1: classification
    failures.extend(check_classification(content))

    # Check 2: dimensions
    dim_failures, ratings = check_dimensions(content)
    failures.extend(dim_failures)

    # Check 3: routing matrix
    failures.extend(check_routing_matrix(content))

    # Check 4: provenance tag coverage
    tag_count = len(re.findall(r"\[(?:V|C|A|I):", content))
    if tag_count < 3:
        failures.append(f"Insufficient V/C/A/I tag coverage. Found {tag_count}; need >=3 (one per dimension minimum).")

    # Check 5: trailing next_skills YAML
    failures.extend(check_next_skills_yaml(content))

    # Check 6: direction-of-travel
    if not re.search(r"\b(direction[- ]of[- ]travel|transitioning|stable)\b", content, re.IGNORECASE):
        failures.append("Missing direction-of-travel statement. Add: 'Stable' OR 'Transitioning from [X] toward [Y] because [evidence]'.")

    # Check 7: ambidexterity declared or noted absent
    if not re.search(r"\bambidext", content, re.IGNORECASE):
        failures.append("Missing ambidexterity declaration. Either declare it (with per-layer/segment evidence) or explicitly note 'No ambidexterity — single-environment industry'.")

    # Check 8: all-Medium dodge guard
    failures.extend(check_default_failure_guard(ratings))

    if warnings:
        print("VALIDATION WARNINGS:", file=sys.stderr)
        for w in warnings:
            print(f"  - {w}", file=sys.stderr)

    if failures:
        print("VALIDATION FAILED:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1

    print(f"VALIDATION PASSED: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

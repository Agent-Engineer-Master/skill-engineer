"""Validate disruption-dataset.yaml against the schema for a given phase.

Run after each phase to catch missing fields, untagged claims, and structural
failures BEFORE proceeding to the next phase. Validation is hard-fail by design.

Usage:
    python validate_dataset.py --slug <slug> --phase <1|2|3|4|5|6>

Exit codes:
    0  - validation passed
    1  - validation failed (specific failures printed to stderr)
    2  - dataset or schema missing

Note: this is a structural check, not semantic. It catches missing fields and
untagged claims; it doesn't grade whether a JTBD is well-written or a counter-
positioning trap is real. Semantic quality is graded by the bar test.
"""

import argparse
import sys
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[5]
INDUSTRIES_DIR = REPO_ROOT / "08-knowledge" / "world-model" / "industries"


# Provenance tag pattern — matches [V: source], [C: source + source], [A: ...], [I: ...]
TAG_PATTERN = re.compile(r"\[(V|C|A|I):\s*[^\]]+\]")


def load_yaml(path: Path) -> dict:
    """Minimal YAML loader without external dependencies.

    Uses pyyaml if available; otherwise returns the raw text for structural
    string-based checks. This keeps the script dependency-free in WSL/Windows
    both. For full structural validation pyyaml should be installed in the
    venv-linux per CLAUDE.md.
    """
    try:
        import yaml  # type: ignore
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except ImportError:
        return {"_raw_text": path.read_text(encoding="utf-8")}


def check_phase_1(data: dict, raw: str) -> list[str]:
    """Phase 1 — industry, value_chain, market_structure."""
    failures = []

    # Structural checks on raw text (works without pyyaml)
    required_blocks = ["industry:", "value_chain:", "market_structure:"]
    for block in required_blocks:
        if block not in raw:
            failures.append(f"Phase 1: missing required block '{block}'")

    required_industry_fields = ["name:", "definition:", "total_market_size:", "growth_rate:", "geography:"]
    industry_section = _extract_block(raw, "industry:")
    for field in required_industry_fields:
        if field not in industry_section:
            failures.append(f"Phase 1: industry block missing field '{field}'")

    # Numeric claims require tags — check the industry section
    if "total_market_size" in industry_section:
        if not TAG_PATTERN.search(industry_section):
            failures.append("Phase 1: industry.total_market_size missing V/C/A/I tag")

    # Value chain must have ≥3 nodes (heuristic: count "- id:" entries in value_chain block)
    vc_section = _extract_block(raw, "value_chain:")
    node_count = vc_section.count("- id:")
    if node_count < 3:
        failures.append(f"Phase 1: value_chain has {node_count} nodes; need ≥3")

    # Market structure must have ≥1 information asymmetry
    ms_section = _extract_block(raw, "market_structure:")
    if "information_asymmetries:" not in ms_section or "who_knows:" not in ms_section:
        failures.append("Phase 1: market_structure.information_asymmetries empty or missing — these are disruption signals")

    return failures


def check_phase_2(data: dict, raw: str) -> list[str]:
    failures = []
    if "value_chain_pain:" not in raw:
        failures.append("Phase 2: missing value_chain_pain block")
        return failures

    vcp_section = _extract_block(raw, "value_chain_pain:")

    # Must have customers AND ≥1 other entity type
    if "customers:" not in vcp_section:
        failures.append("Phase 2: value_chain_pain.customers missing")

    other_entities = ["suppliers:", "intermediaries:", "adjacent_players:"]
    other_count = sum(1 for e in other_entities if e in vcp_section)
    if other_count == 0:
        failures.append("Phase 2: only customers covered — must also cover ≥1 of suppliers, intermediaries, or adjacent_players (disruption surface is wider than just end-customer pain)")

    # Workarounds required on pain points
    pain_count = vcp_section.count("- activity:")
    workaround_count = vcp_section.count("workaround:")
    if pain_count > 0 and workaround_count < pain_count:
        failures.append(f"Phase 2: {pain_count} pain points but only {workaround_count} workaround fields populated — workarounds are load-bearing")

    # Non-consumption required per segment
    if "non_consumption:" not in vcp_section:
        failures.append("Phase 2: non_consumption map missing — new-market disruption foothold lens skipped")

    # Pain score variance check (heuristic): if all visible intensity scores are the same, flag
    intensities = re.findall(r"intensity:\s*(\d+)", vcp_section)
    if len(intensities) >= 3:
        unique_intensities = set(intensities)
        if len(unique_intensities) <= 2:
            failures.append("Phase 2: pain intensity scores show <3 distinct values — likely 'all-7s syndrome' (no real prioritization)")

    return failures


def check_phase_3(data: dict, raw: str) -> list[str]:
    failures = []
    if "enabling_conditions:" not in raw:
        failures.append("Phase 3: missing enabling_conditions block")
        return failures

    ec_section = _extract_block(raw, "enabling_conditions:")

    axes = ["technology_unlocks:", "cost_curves:", "behavioral_shifts:", "regulatory:", "supply_side:"]
    axes_with_content = []
    for axis in axes:
        if axis in ec_section:
            # Check it has at least one entry
            axis_block = _extract_subblock(ec_section, axis)
            if "- id:" in axis_block or "- " in axis_block:
                axes_with_content.append(axis)

    if len(axes_with_content) < 3:
        failures.append(f"Phase 3: only {len(axes_with_content)} of 5 axes populated — single-axis why-now is always weak; need ≥3 axes attempted (N/A with rationale acceptable)")

    # Intersections must have ≥1 with thesis
    if "intersections:" not in ec_section:
        failures.append("Phase 3: intersections block missing — load-bearing why-now requires 2-3-way intersection thesis")
    elif "thesis:" not in ec_section:
        failures.append("Phase 3: intersections present but no thesis populated")

    if "why_now_paragraph:" not in ec_section:
        failures.append("Phase 3: why_now_paragraph missing — quoted in every Phase 6 stress test")

    # Dates required — look for year patterns in conditions
    year_pattern = re.compile(r"when:\s*\d{4}")
    when_count = ec_section.count("when:")
    year_match_count = len(year_pattern.findall(ec_section))
    if when_count > 0 and year_match_count < when_count:
        failures.append(f"Phase 3: {when_count} 'when' fields but only {year_match_count} include a year — date specificity required")

    return failures


def check_phase_4(data: dict, raw: str) -> list[str]:
    failures = []
    if "framework_signals:" not in raw:
        failures.append("Phase 4: missing framework_signals block")
        return failures

    fs_section = _extract_block(raw, "framework_signals:")

    expected_frameworks = ["blue-ocean-errc", "aggregation-theory", "decoupling", "counter-positioning", "seven-powers", "thiel-secret"]
    for fw in expected_frameworks:
        if fw not in fs_section and f"N/A-{fw}" not in fs_section:
            failures.append(f"Phase 4: framework '{fw}' has no signals AND no N/A rationale")

    # Every signal must cite Phase 1-3 dataset
    signal_count = fs_section.count("- signal_id:")
    cites_count = fs_section.count("cites:")
    if signal_count > 0 and cites_count < signal_count:
        failures.append(f"Phase 4: {signal_count} signals but only {cites_count} have 'cites:' field — free-associated signals fail bar test")

    # Each signal must have entry_power + scale_power
    entry_power_count = fs_section.count("entry_power:")
    if signal_count > 0 and entry_power_count < signal_count:
        failures.append(f"Phase 4.5: {signal_count - entry_power_count} signals missing entry_power tag — 'feature, not company' risk unflagged")

    # ≥1 Thiel Secret must be human_endorsed
    if "thiel-secret" in fs_section and "human_endorsed: true" not in fs_section:
        failures.append("Phase 4.6: Thiel Secret signals present but none marked human_endorsed: true — AI cannot supply conviction")

    # Incumbents must have structural_constraints
    if "incumbents:" in raw:
        inc_section = _extract_block(raw, "incumbents:")
        if "structural_constraints:" not in inc_section:
            failures.append("Phase 4.4: incumbents listed but no structural_constraints — counter-positioning analysis impossible")

    return failures


def check_phase_5(data: dict, raw: str) -> list[str]:
    failures = []
    if "venture_concepts:" not in raw:
        failures.append("Phase 5: missing venture_concepts block")
        return failures

    vc_section = _extract_block(raw, "venture_concepts:")

    concept_count = vc_section.count("- concept_id:")
    if concept_count < 3:
        failures.append(f"Phase 5: only {concept_count} concepts kept — minimum 3 required for Phase 6 stress test to produce ranked shortlist")
    if concept_count > 5:
        failures.append(f"Phase 5: {concept_count} concepts kept — maximum 5 (Phase 6 stress test depth suffers across more)")

    # Each concept must have signals_cited, why_now, what_they_cant_copy, wedge, year_one_metric
    required_fields = ["signals_cited:", "why_now:", "what_they_cant_copy:", "wedge_product:", "year_one_metric:"]
    for field in required_fields:
        field_count = vc_section.count(field)
        if field_count < concept_count:
            failures.append(f"Phase 5: {concept_count - field_count} concepts missing '{field}' — required for Phase 6 stress test")

    # AI-washing screen — look for "AI for X" patterns in one_line fields
    one_lines = re.findall(r"one_line:\s*[\"']([^\"'\n]+)[\"']", vc_section)
    for line in one_lines:
        if re.search(r"^\s*An?\s+AI\s+(for|that)\b", line, re.IGNORECASE):
            failures.append(f"Phase 5: concept one_line appears AI-washed: '{line[:80]}...'")

    return failures


def check_phase_6(data: dict, raw: str) -> list[str]:
    failures = []
    if "stress_tests:" not in raw:
        failures.append("Phase 6: missing stress_tests on concepts")
        return failures

    # Every concept must have all four stress tests
    required_tests = ["why_now:", "idea_maze:", "incumbent_response:", "moat_durability:"]
    vc_section = _extract_block(raw, "venture_concepts:")
    concept_count = vc_section.count("- concept_id:")

    for test in required_tests:
        # Count occurrences after stress_tests: appearance
        test_count = vc_section.count(test)
        # Approximate: each concept should have one of each
        if test_count < concept_count:
            failures.append(f"Phase 6: {concept_count - test_count} concepts missing stress test '{test}'")

    # Overall verdict required per concept
    verdict_count = vc_section.count("overall_verdict:")
    if verdict_count < concept_count:
        failures.append(f"Phase 6: {concept_count - verdict_count} concepts missing overall_verdict")

    return failures


def _extract_block(text: str, block_marker: str) -> str:
    """Extract a top-level YAML block by its marker, stopping at the next top-level marker."""
    start = text.find(block_marker)
    if start == -1:
        return ""
    # Find next top-level marker (line starting with [a-z] followed by :)
    rest = text[start + len(block_marker):]
    lines = rest.split("\n")
    out_lines = []
    for line in lines:
        # Top-level YAML key (no leading whitespace, ends with :)
        if line and not line[0].isspace() and ":" in line and not line.startswith("#"):
            break
        out_lines.append(line)
    return "\n".join(out_lines)


def _extract_subblock(text: str, sub_marker: str) -> str:
    """Extract a sub-block by marker; less precise than _extract_block."""
    start = text.find(sub_marker)
    if start == -1:
        return ""
    rest = text[start + len(sub_marker):]
    # Stop at the next same-level marker (heuristic: a non-indented marker at the same indent)
    lines = rest.split("\n")
    if not lines:
        return ""
    # Take everything until a line at the same indent as sub_marker with a colon
    out_lines = []
    base_indent = None
    for line in lines:
        stripped = line.lstrip()
        if not stripped:
            out_lines.append(line)
            continue
        indent = len(line) - len(stripped)
        if base_indent is None:
            base_indent = indent
        elif indent < base_indent and stripped.endswith(":"):
            break
        out_lines.append(line)
    return "\n".join(out_lines)


PHASE_CHECKERS = {
    1: check_phase_1,
    2: check_phase_2,
    3: check_phase_3,
    4: check_phase_4,
    5: check_phase_5,
    6: check_phase_6,
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--slug", required=True)
    parser.add_argument("--phase", type=int, required=True, choices=[1, 2, 3, 4, 5, 6])
    args = parser.parse_args()

    dataset_path = INDUSTRIES_DIR / args.slug / "disruption-dataset.yaml"
    if not dataset_path.exists():
        print(f"ERROR DatasetMissing: {dataset_path}", file=sys.stderr)
        return 2

    data = load_yaml(dataset_path)
    raw = dataset_path.read_text(encoding="utf-8")

    # Run all checkers up to and including the requested phase
    all_failures = []
    for phase in range(1, args.phase + 1):
        failures = PHASE_CHECKERS[phase](data, raw)
        all_failures.extend(failures)

    if all_failures:
        print(f"VALIDATION FAILED — Phase {args.phase} (and prior) — {len(all_failures)} issues:", file=sys.stderr)
        for f in all_failures:
            print(f"  - {f}", file=sys.stderr)
        print(file=sys.stderr)
        print("Fix: address each issue in disruption-dataset.yaml, then re-run validation.", file=sys.stderr)
        return 1

    print(f"VALIDATION PASSED — Phase {args.phase}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

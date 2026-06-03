"""Validate an analyze-trajectory output against the discipline.

Checks (v1):
- Dual S-curve: BOTH market AND tech assessed with named stage each
- ≥3 H1/H2/H3 sub-segment classifications
- ≥2 discontinuities with explicit year-range timing windows
- Power Progression mapping: all 7 Powers covered with state
- Base/bear/bull scenarios with ≥3 named swing variables
- V/C/A/I tag coverage ≥6
- next_skills YAML block at end
- Warns (non-failing) on universal-H1 classification, and on
  vague timing language ("soon", "eventually", "coming years")
- Warns (non-failing) on hyper-cycle / sentiment-driven keywords
  (crypto, web3, defi, nft, meme-stock, etc.) prompting switch to
  cycle methodology — unless the output already discloses it
- Quantitative scenarios: REQUIRED in orchestrator mode (output sits
  inside .../industries/<slug>/working/ with sibling market-sizing.md);
  soft warning in standalone mode

Usage:
    python validate_trajectory.py --output-path <path-to-trajectory.md>

Exit codes:
    0 — pass
    1 — fail
    2 — file missing
"""

import argparse
import re
import sys
from pathlib import Path


HELMER_POWERS = [
    "Scale Economies",
    "Network Economies",
    "Counter-Positioning",
    "Switching Costs",
    "Branding",
    "Cornered Resource",
    "Process Power",
]

STAGE_PATTERN = r"(introduction|growth|maturity|decline)"
YEAR_RANGE_PATTERN = r"\b20[2-4]\d\s*[-–to]+\s*20[2-4]\d\b"
VAGUE_TIMING = [r"\bsoon\b", r"\beventually\b", r"\bin (the )?coming years\b", r"\bin a few years\b"]

# Hyper-cycle / sentiment-driven markets — standard S-curve doesn't apply.
# Emit a soft warning prompting the analyst to switch to cycle methodology.
HYPER_CYCLE_KEYWORDS = [
    "crypto",
    "web3",
    "nft",
    "meme-stock",
    "meme stock",
    "consumer-llm",
    "defi",
    "blockchain",
    "token",
    "governance token",
    "gamestop-style",
    "sentiment-driven",
]

# Quantitative-scenario regex helpers (orchestrator mode).
DOLLAR_FIG_PATTERN = re.compile(r"\$[\d,.]+\s*(B|M|bn|mn)\b", re.IGNORECASE)
CAGR_PATTERN = re.compile(r"\d+(?:\.\d+)?\s*%\s*CAGR", re.IGNORECASE)


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

    # Check 1: dual S-curve — both market AND tech S-curve sections present,
    # each with a named stage.
    market_section = re.search(
        r"(?is)market[- ]?(adoption )?S[- ]?curve[^\n]*\n.{0,800}",
        content,
    )
    tech_section = re.search(
        r"(?is)tech(nology)?[- ]?S[- ]?curve[^\n]*\n.{0,800}",
        content,
    )
    if not market_section:
        failures.append("Missing market-adoption S-curve section. Dual S-curve assessment is mandatory.")
    if not tech_section:
        failures.append("Missing technology S-curve section. Dual S-curve assessment is mandatory.")
    if market_section and not re.search(STAGE_PATTERN, market_section.group(0), re.IGNORECASE):
        failures.append("Market S-curve section present but no stage named (introduction/growth/maturity/decline).")
    if tech_section and not re.search(STAGE_PATTERN, tech_section.group(0), re.IGNORECASE):
        failures.append("Tech S-curve section present but no stage named (introduction/growth/maturity/decline).")

    # Check 2: Three Horizons — ≥3 sub-segment classifications.
    # Look for "H1", "H2", "H3" markers (each at least once) AND ≥3 occurrences total of
    # an H[1-3] classification pattern within the same line as a sub-segment name.
    h_classifications = re.findall(r"\bH[1-3]\b", content)
    if len(h_classifications) < 3:
        failures.append(
            f"Insufficient Three Horizons classifications. Found {len(h_classifications)} H1/H2/H3 markers; need ≥3 sub-segment classifications."
        )
    distinct_horizons = set(h_classifications)
    if len(distinct_horizons) < 2:
        warnings.append(
            f"Only {len(distinct_horizons)} distinct horizons used ({sorted(distinct_horizons)}). "
            "Universal-single-horizon classification (e.g., all H1) is rare in real industries."
        )

    # Check 3: ≥2 discontinuities with explicit year-range timing windows.
    year_ranges = re.findall(YEAR_RANGE_PATTERN, content)
    if len(year_ranges) < 2:
        failures.append(
            f"Insufficient explicit year-range timing windows. Found {len(year_ranges)}; need ≥2. "
            "Each discontinuity must carry an explicit year range (e.g., '2026-2028')."
        )

    # Vague timing — fail (not warn) if found in a discontinuities/timing context.
    vague_hits = []
    for v in VAGUE_TIMING:
        for m in re.finditer(v, content, re.IGNORECASE):
            # Ignore false positives inside known boilerplate ("soon" in references etc.).
            window_start = max(0, m.start() - 100)
            window = content[window_start: m.end() + 100]
            if re.search(r"(?i)(discontinuit|window|timing|year)", window):
                vague_hits.append(m.group(0))
    if vague_hits:
        failures.append(
            f"Vague timing language in discontinuity context: {vague_hits[:3]}. "
            "Use explicit year ranges (e.g., '2026-2028'), not 'soon' / 'eventually' / 'coming years'."
        )

    # Check 4: Power Progression — all 7 Powers present.
    missing_powers = []
    for power in HELMER_POWERS:
        # Allow some name flexibility (e.g., "Counter Positioning" without hyphen).
        flex_pattern = power.replace("-", "[- ]?")
        if not re.search(rf"\b{flex_pattern}\b", content, re.IGNORECASE):
            missing_powers.append(power)
    if missing_powers:
        failures.append(
            f"Power Progression incomplete. Missing Powers: {missing_powers}. All 7 must be mapped to a state (open now / Year 3 / Year 5+ / closed)."
        )

    # Power-state markers — at least one of {open, closed, year 3, year 5}.
    state_markers = re.findall(
        r"(?i)\b(open now|open year [0-9]|closed|year ?3|year ?5\+?)\b",
        content,
    )
    if len(state_markers) < 4:
        failures.append(
            f"Power Progression state markers missing or too few ({len(state_markers)}). "
            "Each Power should carry a state: 'open now', 'open Year 3', 'open Year 5+', or 'closed'."
        )

    # Check 5: Scenarios — base/bear/bull AND ≥3 named swing variables.
    has_base = bool(re.search(r"(?i)\bbase\b", content))
    has_bear = bool(re.search(r"(?i)\bbear\b", content))
    has_bull = bool(re.search(r"(?i)\bbull\b", content))
    if not (has_base and has_bear and has_bull):
        missing = [n for n, h in [("base", has_base), ("bear", has_bear), ("bull", has_bull)] if not h]
        failures.append(f"Missing scenario case(s): {missing}. Base / bear / bull all required.")

    # Swing variables — look for "swing variable" mentions or a swing-variable table.
    swing_mentions = len(re.findall(r"(?i)swing variable", content))
    # Or look for a labeled list/table — count lines that look like "- <NAME>: <range>" within a swing variables section.
    if swing_mentions < 1:
        failures.append(
            "No 'swing variable' label found. Scenarios must name ≥3 swing variables explicitly. See references/scenario-methodology.md."
        )
    # Try to find at least 3 distinct named swing variables (heuristic: lines containing 'swing' or
    # bullets under a Swing Variables heading).
    swing_section = re.search(
        r"(?is)swing variables?[^\n]*\n((?:[-*]\s+[^\n]+\n){3,})",
        content,
    )
    if not swing_section:
        # Alternative: a markdown table with "Swing var" columns and ≥3 data rows.
        table_swing = re.search(
            r"(?is)\|\s*scenario\s*\|.*?swing var[^\|]*\|.*?\n(?:\|[^\n]+\n){3,}",
            content,
        )
        if not table_swing:
            failures.append(
                "Could not detect ≥3 named swing variables in a Swing Variables list or scenario table. "
                "Provide a bulleted list of ≥3 named swing variables (e.g., '- EU AI Act enforcement: light vs strict')."
            )

    # Check 6: V/C/A/I tag coverage.
    tag_count = len(re.findall(r"\[(V|C|A|I):", content))
    if tag_count < 6:
        failures.append(
            f"Insufficient provenance tag coverage. Found {tag_count} V/C/A/I tags; need ≥6 (S-curve signals + discontinuities + Power assessments)."
        )

    # Check 7: next_skills YAML block at end of file.
    tail = content[-2000:]
    next_skills_match = re.search(
        r"---\s*\n\s*next_skills\s*:\s*\n((?:\s*-\s*[^\n]+\n)+)\s*---",
        tail,
    )
    if not next_skills_match:
        failures.append(
            "Missing structured next_skills YAML block at end of file. Output must end with a "
            "'---\\nnext_skills:\\n  - <skill-name>\\n---' block listing ≥1 recommended next skill."
        )

    # Soft warning: hyper-cycle / sentiment-driven markets.
    # Triggered when content OR the industry slug in the path matches any keyword.
    path_str = str(path).lower()
    content_lower = content.lower()
    matched_keywords = [
        kw for kw in HYPER_CYCLE_KEYWORDS
        if kw in content_lower or kw in path_str
    ]
    if matched_keywords:
        # Only emit if the output does not already disclose cycle-methodology handling.
        if not re.search(r"(?i)cycle methodology|cycle period|peak[- ]to[- ]trough|sentiment driver", content):
            warnings.append(
                "Hyper-cycle / sentiment-driven keywords detected "
                f"({matched_keywords[:3]}). Standard linear S-curve methodology is unreliable "
                "for these markets — switch to cycle methodology: capture (1) cycle period in "
                "months, (2) amplitude (peak-to-trough %), (3) dominant sentiment driver "
                "(Fed policy, regulatory event, viral catalyst), (4) where in the current "
                "cycle the market sits. See references/s-curve-methodology.md 'Cycle "
                "methodology' sub-section."
            )

    # Conditional quantitative-scenario rigor.
    # Orchestrator mode: output sits inside 08-knowledge/world-model/industries/<slug>/working/
    # AND a sibling market-sizing.md exists. In that mode REQUIRE quantitative scenarios.
    # Standalone mode (or market-sizing.md absent): emit a soft warning instead.
    parent = path.parent
    norm_parent = parent.as_posix().lower()
    in_orchestrator_path = bool(
        re.search(r"08-knowledge/world-model/industries/[^/]+/working/?$", norm_parent)
    )
    sibling_market_sizing = parent / "market-sizing.md"
    orchestrator_mode = in_orchestrator_path and sibling_market_sizing.exists()

    dollar_hits = DOLLAR_FIG_PATTERN.findall(content)
    cagr_hits = CAGR_PATTERN.findall(content)
    quant_ok = len(dollar_hits) >= 3 and len(cagr_hits) >= 3

    if orchestrator_mode:
        if not quant_ok:
            failures.append(
                f"Orchestrator mode (sibling market-sizing.md present) requires quantitative "
                f"scenarios. Found {len(dollar_hits)} dollar figures ($XB/M) and "
                f"{len(cagr_hits)} CAGR figures (X% CAGR); need >=3 of each across "
                "base/bear/bull combined. See references/scenario-methodology.md."
            )
    else:
        if not quant_ok:
            warnings.append(
                "Scenario rigor limited without `market-sizing.md` data; consider running "
                "`size-market` first or use this analysis as directional only."
            )

    # Soft warning: universal-H1.
    if h_classifications:
        h1_only = all(c == "H1" for c in h_classifications)
        if h1_only and len(h_classifications) >= 3:
            warnings.append(
                "Universal-H1 classification detected. Real industries with >0% growth typically have at "
                "least one H2 or H3 sub-segment. Re-cut the G3 decomposition or state declining-industry explicitly."
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

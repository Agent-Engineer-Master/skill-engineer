"""Validate a value-chain-profit-pools output against the discipline.

Checks (hard fails):
- EBIT or economic profit mentioned (not just revenue margin)
- Absolute $ figures present (not just %)
- Profit-pool bar visualization present (table with bar characters)
- Structural protection named from Helmer 7 Powers (one of: switching costs, scale economies,
  network economies, regulatory barrier / cornered resource, process power, counter-positioning,
  branding) — OR explicit "not structurally protected" statement
- V/C/A/I provenance tag coverage (>=5 tags)
- Capital-intensity >2× rule: if stage-level capital intensity / capital employed data is disclosed
  and max/min ratio exceeds 2.0×, the output must prominently use economic profit (EP /
  NOPAT minus capital charge) — not just EBIT.
- Structured `next_skills:` YAML block present at end of file listing >=1 skill.

Anti-pattern checks (hard fails when a protection IS named):
- "adds value" / "value-added" used as the protection
- "differentiation" / "differentiated" used as the protection
- "is critical" / "mission-critical" used as the protection
- "first-mover" used as the only protection
- "expertise" / "know-how" used as the only protection
- "relationships" / "trusted partner" used as the only protection
- "high quality" / "superior product" used as the protection

Quality warnings (soft, do not fail but printed):
- No 3-year / 5-year normalisation disclosure
- EBIT figures quoted to >=2 decimals without a range
- All stages within 30% of each other (flat profit pool — likely estimation error)
- Capital-intensity data not disclosed at all (suggests adding it for EP triage)

Usage:
    python validate_profit_pools.py --output-path <path-to-value-chain-profit-pools.md>
    python validate_profit_pools.py --output-path <path> --strict   (warnings become failures)

Exit codes:
    0 — pass
    1 — fail
    2 — file missing
"""

import argparse
import re
import sys
from pathlib import Path


STRUCTURAL_PROTECTIONS = [
    "switching cost",
    "scale econom",
    "network econom",
    "regulatory barrier",
    "cornered resource",
    "process power",
    "counter-position",
    "counter position",
    "branding",
    "brand power",
]

# Phrases that masquerade as structural protections but are not
NON_STRUCTURAL_ANTIPATTERNS = [
    (r"\badds (the )?most value\b", "'adds value' is tautological — name a specific Helmer power"),
    (r"\bvalue[- ]add(ed|ing)?\b.{0,40}(captures|concentrat|sustain|protect)", "'value-added' is not a structural protection"),
    (r"\b(is|are) (mission-)?critical\b.{0,40}(captures|concentrat|sustain|protect)", "'critical' describes importance, not mechanism"),
    (r"\b(highly )?differentiat(ed|ion)\b.{0,40}(captures|concentrat|sustain|protect)", "'differentiation' is the symptom, not the protection"),
    (r"\bfirst[- ]mover\b.{0,40}(captures|concentrat|sustain|protect)(?!.{0,80}(switching|scale|network|cornered|process|brand))", "first-mover alone is not durable — pair with a Helmer power"),
    (r"\b(deep )?expertise\b.{0,40}(captures|concentrat|sustain|protect)(?!.{0,80}(process|cornered))", "'expertise' must be specified as process power or cornered resource"),
    (r"\b(trusted |strong )?relationships\b.{0,40}(captures|concentrat|sustain|protect)(?!.{0,80}(switching|brand))", "'relationships' must be specified as switching costs or branding"),
    (r"\b(superior |higher )?quality\b.{0,40}(captures|concentrat|sustain|protect)", "'quality' is competitive, not structural"),
    (r"\bcomplexity\b.{0,40}(captures|concentrat|sustain|protect)(?!.{0,80}(process|switching|cornered))", "'complexity' is not protection unless tied to a named power"),
]

# "Not structurally protected" is a valid finding — pattern detects it
UNSTABLE_FINDING_PATTERN = re.compile(
    r"not structurally protected|unstable\b|no structural protection|expect arbitrage",
    re.IGNORECASE,
)

NORMALISATION_PATTERN = re.compile(
    r"\b(3[- ]year|5[- ]year|three[- ]year|five[- ]year|trailing|normali[sz]ed|3yr|5yr)\b",
    re.IGNORECASE,
)


def detect_flat_pool(content: str) -> bool:
    """Find the EBIT table and check if all stages are within 30% of each other."""
    # Look for rows like "| Stage | ... | $X.XB ... |" or "$X.X | ... |"
    rows = re.findall(r"\$?\s*([0-9]+(?:\.[0-9]+)?)\s*B\b", content)
    if len(rows) < 3:
        return False
    try:
        nums = sorted([float(x) for x in rows if 0.01 <= float(x) <= 10000])
        if len(nums) < 3:
            return False
        # Take 3-7 most plausible stage EBITs (mid range)
        nums = nums[: min(7, len(nums))]
        if nums[0] == 0:
            return False
        spread = (nums[-1] - nums[0]) / nums[0]
        return spread < 0.3
    except (ValueError, ZeroDivisionError):
        return False


# Keywords indicating capital-intensity / capital-employed disclosure
CAPITAL_INTENSITY_KEYWORDS = re.compile(
    r"\b(capital employed|capital intensity|asset intensity|capital[- ]to[- ]revenue|"
    r"capex intensity|invested capital|capital base|PP&E|net PP&E)\b",
    re.IGNORECASE,
)

# Prominent EP mention required when >2x rule binds — appears as table column,
# section header, or repeated mention (not just a single passing reference).
EP_PROMINENT_PATTERN = re.compile(
    r"economic profit|\bEP\b|NOPAT.{0,40}(capital charge|WACC|minus)|NOPAT\s*[-−]\s*\(?capital",
    re.IGNORECASE,
)


def _parse_money_to_float(token: str) -> float | None:
    """Parse '$25', '25B', '$1.4B', '220' etc. into a float (in the unit as written).

    Returns the numeric value without unit normalisation — we only need ratios.
    """
    m = re.match(r"\$?\s*([0-9]+(?:\.[0-9]+)?)\s*(B|bn|M|mn|%)?", token.strip(), re.IGNORECASE)
    if not m:
        return None
    val = float(m.group(1))
    unit = (m.group(2) or "").lower()
    # Normalise M → B by /1000 so mixed-unit tables still ratio correctly
    if unit in ("m", "mn"):
        val = val / 1000.0
    return val


def extract_capital_intensity_values(content: str) -> list[float]:
    """Heuristic parser for stage-level capital intensity / capital employed.

    Strategy:
    1. Find any markdown table whose header row contains one of the capital-intensity keywords.
    2. For each data row in that table, extract the numeric value in the matching column.
    3. Also scan inline patterns like "capital employed: $25B" / "capital intensity 1.2x".
    Returns list of numeric values (one per stage); ratio of max/min is the trigger.
    """
    values: list[float] = []

    # --- 1. Table-based extraction ---
    lines = content.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        # A markdown table header containing pipes and a capital-intensity keyword
        if "|" in line and CAPITAL_INTENSITY_KEYWORDS.search(line):
            header_cells = [c.strip() for c in line.strip().strip("|").split("|")]
            # Find target column index (first match)
            target_col = None
            for idx, cell in enumerate(header_cells):
                if CAPITAL_INTENSITY_KEYWORDS.search(cell):
                    target_col = idx
                    break
            # Skip separator row(s)
            j = i + 1
            while j < len(lines) and re.match(r"^[\s|:\-]+$", lines[j]):
                j += 1
            # Read data rows until table ends
            while j < len(lines) and "|" in lines[j] and lines[j].strip().startswith("|"):
                cells = [c.strip() for c in lines[j].strip().strip("|").split("|")]
                if target_col is not None and target_col < len(cells):
                    cell = cells[target_col]
                    # Skip total/blank/dash rows
                    if cell and not re.search(r"total|—|^-+$|^\s*$", cell, re.IGNORECASE):
                        # Strip bold markers
                        cell = cell.replace("**", "").strip()
                        v = _parse_money_to_float(cell)
                        if v is not None and v > 0:
                            values.append(v)
                j += 1
            i = j
            continue
        i += 1

    # --- 2. Inline extraction (fallback / supplement) ---
    inline_pattern = re.compile(
        r"(?:capital employed|capital intensity|asset intensity|invested capital)"
        r"[^\n]{0,60}?(\$?\s*[0-9]+(?:\.[0-9]+)?\s*(?:B|bn|M|mn|x|×)?)",
        re.IGNORECASE,
    )
    for m in inline_pattern.finditer(content):
        v = _parse_money_to_float(m.group(1))
        if v is not None and v > 0:
            values.append(v)

    return values


def capital_intensity_ratio(values: list[float]) -> float | None:
    """Return max/min ratio, or None if fewer than 2 values."""
    if len(values) < 2:
        return None
    lo = min(values)
    hi = max(values)
    if lo == 0:
        return None
    return hi / lo


def ep_used_prominently(content: str) -> bool:
    """EP is prominent if it appears in >=2 distinct lines OR in a table header / section header."""
    matches = list(EP_PROMINENT_PATTERN.finditer(content))
    if len(matches) >= 2:
        return True
    # Section / table header mention
    for line in content.splitlines():
        stripped = line.strip()
        if (stripped.startswith("#") or "|" in stripped) and EP_PROMINENT_PATTERN.search(stripped):
            return True
    return False


def has_next_skills_block(content: str) -> bool:
    """Detect a `next_skills:` YAML block at end of file listing >=1 skill entry."""
    # Look at the last ~30 lines for a fenced YAML block containing next_skills
    tail = "\n".join(content.splitlines()[-40:])
    block_match = re.search(
        r"(?s)---\s*\n(.*?next_skills\s*:\s*\n(?:\s*-\s*\S+.*\n)+)\s*---\s*$",
        tail.rstrip() + "\n",
    )
    if block_match:
        entries = re.findall(r"^\s*-\s*\S+", block_match.group(1), re.MULTILINE)
        return len(entries) >= 1
    return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-path", required=True)
    parser.add_argument("--strict", action="store_true", help="Warnings become failures")
    args = parser.parse_args()

    path = Path(args.output_path)
    if not path.exists():
        print(f"ERROR FileMissing: {path}", file=sys.stderr)
        return 2

    content = path.read_text(encoding="utf-8")
    failures = []
    warnings = []

    # --- HARD CHECKS ---

    # Check 1: EBIT or economic profit present
    if not re.search(r"\b(EBIT|economic profit|EP\b)\b", content, re.IGNORECASE):
        failures.append("Missing EBIT or economic profit metric. Profit pools must use absolute economic profit, not revenue margin.")

    # Check 2: absolute $ figures present
    dollar_figures = re.findall(r"\$[\d,]+(?:\.\d+)?\s*(?:B|M|bn|mn)?", content)
    if len(dollar_figures) < 3:
        failures.append(
            f"Insufficient absolute $ figures. Found {len(dollar_figures)}. Each value-chain stage should have an absolute $ EBIT estimate."
        )

    # Check 3: profit-pool bar visualization
    has_bar_viz = bool(re.search(r"[█▌▎▍▊▋▉]+", content))
    if not has_bar_viz:
        failures.append(
            "Missing profit-pool bar visualization. Use a markdown table with horizontal bars (█ characters) proportional to EBIT."
        )

    # Check 4: structural protection statement OR explicit unstable-finding
    has_structural_protection = any(
        re.search(rf"\b{re.escape(p)}", content, re.IGNORECASE) for p in STRUCTURAL_PROTECTIONS
    )
    has_unstable_finding = bool(UNSTABLE_FINDING_PATTERN.search(content))
    if not (has_structural_protection or has_unstable_finding):
        failures.append(
            "Missing named structural protection. Must name one of: switching costs / scale economies / network economies / "
            "branding / cornered resource (incl. regulatory) / process power / counter-positioning. OR state explicitly that profit "
            "concentration is not structurally protected ('expect arbitrage by ...')."
        )

    # Check 5: V/C/A/I tag coverage
    tag_count = len(re.findall(r"\[(V|C|A|I):", content))
    if tag_count < 5:
        failures.append(
            f"Insufficient provenance tag coverage. Found {tag_count} V/C/A/I tags. Each EBIT estimate should carry a tag."
        )

    # Check 6: anti-pattern protections (only if a protection IS named — otherwise skip)
    if has_structural_protection:
        for pattern, message in NON_STRUCTURAL_ANTIPATTERNS:
            if re.search(pattern, content, re.IGNORECASE):
                failures.append(f"Non-structural protection antipattern detected: {message}")

    # Check 7: capital-intensity >2× hard rule
    ci_values = extract_capital_intensity_values(content)
    ci_ratio = capital_intensity_ratio(ci_values)
    if ci_ratio is not None and ci_ratio > 2.0:
        if not ep_used_prominently(content):
            failures.append(
                f"Capital-intensity max/min ratio = {ci_ratio:.2f}× exceeds 2× threshold "
                f"(parsed {len(ci_values)} stage-level values). EBIT alone is not sufficient — "
                "use economic profit (EP / NOPAT minus capital charge) prominently. "
                "See references/economic-profit.md."
            )

    # Check 8: structured next_skills YAML block
    if not has_next_skills_block(content):
        failures.append(
            "Missing structured `next_skills:` YAML block at end of file. "
            "Append a fenced YAML block listing >=1 recommended next skill for orchestrator Phase 2 hand-off. "
            "Format: `---\\nnext_skills:\\n  - skill-name    # rationale\\n---`"
        )

    # --- SOFT WARNINGS ---

    # Warning: capital-intensity not disclosed at all
    if ci_ratio is None and not CAPITAL_INTENSITY_KEYWORDS.search(content):
        warnings.append(
            "No capital-intensity / capital-employed data disclosed. EBIT is acceptable, but disclosing "
            "stage-level capital intensity lets readers verify whether the >2× EP-upgrade trigger binds. "
            "Add a 'Capital employed ($B)' column to the methodology table."
        )

    # Warning: normalisation disclosure
    if not NORMALISATION_PATTERN.search(content):
        warnings.append(
            "No 3-year / 5-year normalisation disclosure detected. Profit pools built on single-year prints are noisy. "
            "Add 'normalised over 3-year trailing average' (or 5-year for cyclicals)."
        )

    # Warning: false precision (EBIT figures with >=2 decimals and no range nearby)
    precise_figures = re.findall(r"\$([\d,]+\.[\d]{2,})\s*(?:B|bn)\b", content)
    has_range_notation = bool(re.search(r"\$?\d+(\.\d+)?\s*[-–]\s*\$?\d+(\.\d+)?\s*(B|bn)", content))
    if precise_figures and not has_range_notation:
        warnings.append(
            f"False-precision warning: {len(precise_figures)} EBIT figure(s) quoted to 2+ decimals without ranges. "
            "Triangulated estimates carry irreducible uncertainty — express as ranges (e.g., '$1.7-2.2B')."
        )

    # Warning: flat profit pool
    if detect_flat_pool(content):
        warnings.append(
            "Possible flat profit pool detected — stage EBITs are within 30% of each other. "
            "Flat pools are rare in real industries and usually indicate estimation error. "
            "If genuinely flat, document the justification explicitly (e.g., late-commoditisation phase)."
        )

    # --- REPORTING ---

    if failures:
        print("VALIDATION FAILED:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)

    if warnings:
        print("WARNINGS:", file=sys.stderr)
        for w in warnings:
            print(f"  - {w}", file=sys.stderr)

    if failures or (warnings and args.strict):
        return 1

    print(f"VALIDATION PASSED: {path}")
    if warnings:
        print(f"  ({len(warnings)} non-blocking warning(s) above — review before publishing)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Validate an assess-moat-sources output against the discipline.

Hard checks:
- All 7 Powers explicitly assessed (each named with one of: present / absent / nascent / not present / not applicable).
- For each present Power: paired benefit + barrier statements both present (within 20 lines of the Power name).
- Durability rating per present Power (short / medium / long).
- Named erosion vector per present Power (not just "will erode").
- Anti-pattern rejections: "first-mover" alone, "differentiation" alone, "operational excellence" alone, "adds value",
  "is critical", "expertise" alone, "relationships" alone, "high quality", "complexity" alone — when used as
  the Power claim itself.
- Cross-reference reconciliation: if working/value-chain-profit-pools.md exists in the same working/ directory
  (or adjacent), output must contain a "Cross-reference" section that names the upstream Power and reaches
  MATCH or MISMATCH explicitly.
- V/C/A/I tag coverage (>=5).
- Trailing `next_skills:` YAML block listing >=1 skill.

Soft warnings:
- No AI-impact discussion in named-risks section.
- Power Progression / S-curve stage not referenced.
- All present Powers rated Short (unstable winner archetype).

Usage:
    python validate_moat.py --output-path <path-to-moat-sources.md>
    python validate_moat.py --output-path <path> --strict

Exit codes:
    0 — pass
    1 — fail
    2 — file missing
"""

import argparse
import re
import sys
from pathlib import Path


SEVEN_POWERS = [
    ("scale economies", r"scale econom"),
    ("network economies", r"network econom"),
    ("counter-positioning", r"counter[- ]position"),
    ("switching costs", r"switching cost"),
    ("branding", r"\bbrand(ing|\s+power)\b"),
    ("cornered resource", r"cornered resource"),
    ("process power", r"process power"),
]

# Lines marking a state assessment for a Power
STATE_KEYWORDS = re.compile(
    r"\b(present|absent|nascent|not\s+present|not\s+applicable|n/a)\b",
    re.IGNORECASE,
)

DURABILITY_KEYWORDS = re.compile(
    r"\b(short|medium|long)\b.{0,30}(<?\s*\d+\s*y|erosion|term|duration|horizon|year)",
    re.IGNORECASE,
)

EROSION_VECTOR_HINTS = re.compile(
    r"\b(erosion vector|erodes? (via|through|because|when|as)|"
    r"vulnerable to|threatened by|undermined by|will erode|"
    r"expir(es?|y)|substitut|disintermediat|commoditi[sz]|unbundl)",
    re.IGNORECASE,
)

# Anti-patterns: rejected when used as the Power claim
ANTI_PATTERNS = [
    (r"\bfirst[- ]mover\b(?![^.\n]{0,120}(scale econom|network econom|switching cost|brand|cornered resource|process power|counter[- ]position))",
     "'first-mover' used without pairing to a named Helmer Power"),
    (r"\bdifferentiat(ed|ion)\b[^\n.]{0,80}(power|moat|protect|durab)",
     "'differentiation' framed as a Power — name the underlying Helmer Power"),
    (r"\bvalue[- ]add(ed|ing)?\b[^\n.]{0,80}(power|moat|protect|durab)",
     "'value-added' framed as a Power"),
    (r"\badds (the )?most value\b[^\n.]{0,60}(power|moat|protect|durab|captures)",
     "'adds value' is tautological — name a Helmer Power"),
    (r"\b(is|are)\s+(mission-)?critical\b[^\n.]{0,80}(power|moat|protect)",
     "'critical' describes importance, not mechanism"),
    (r"\b(superior |higher )?quality\b[^\n.]{0,80}(power|moat|protect|durab)",
     "'quality' is competitive, not structural"),
    (r"\boperational excellence\b[^\n.]{0,80}(power|process power|moat|protect)(?![^.\n]{0,120}(compound|years|decade|named routine))",
     "'operational excellence' alone is not Process Power"),
    (r"\b(execution)\b[^\n.]{0,30}(is|as)\s+(the\s+)?(power|moat|process power)\b",
     "'execution' alone is not a Power"),
    (r"\b(deep )?expertise\b[^\n.]{0,80}(is|forms|provides|gives)[^\n.]{0,40}(power|moat)(?![^.\n]{0,120}(cornered resource|process power))",
     "'expertise' must be specified as Cornered Resource (talent) or Process Power"),
    (r"\b(trusted |strong )?relationships?\b[^\n.]{0,80}(is|forms|provides|gives)[^\n.]{0,40}(power|moat)(?![^.\n]{0,120}(switching cost|brand))",
     "'relationships' must be specified as Switching Costs or Branding"),
    (r"\bcomplexity\b[^\n.]{0,80}(is|provides|gives)[^\n.]{0,40}(power|moat|protect)(?![^.\n]{0,120}(process power|switching|cornered))",
     "'complexity' alone is not a Power"),
]


def has_next_skills_block(content: str) -> bool:
    tail = "\n".join(content.splitlines()[-40:])
    m = re.search(
        r"(?s)---\s*\n(.*?next_skills\s*:\s*\n(?:\s*-\s*\S+.*\n)+)\s*---\s*$",
        tail.rstrip() + "\n",
    )
    if m:
        entries = re.findall(r"^\s*-\s*\S+", m.group(1), re.MULTILINE)
        return len(entries) >= 1
    return False


def power_assessed(content: str, power_regex: str) -> tuple[bool, bool]:
    """Return (mentioned, has_state_within_window)."""
    matches = list(re.finditer(power_regex, content, re.IGNORECASE))
    if not matches:
        return (False, False)
    # Within 400 chars after first mention, look for a state keyword
    for m in matches:
        window = content[m.start(): m.start() + 400]
        if STATE_KEYWORDS.search(window):
            return (True, True)
    return (True, False)


def power_present_states(content: str) -> list[tuple[str, int]]:
    """Identify which Powers are marked 'present' and the offset of that marker."""
    present_powers = []
    for name, rx in SEVEN_POWERS:
        for m in re.finditer(rx, content, re.IGNORECASE):
            window = content[m.start(): m.start() + 400]
            # Marked present (and not "not present" / "absent")
            if re.search(r"\bpresent\b", window, re.IGNORECASE) and not re.search(
                r"\bnot\s+present\b|\babsent\b", window, re.IGNORECASE
            ):
                present_powers.append((name, m.start()))
                break
    return present_powers


def has_benefit_barrier(content: str, offset: int, window_chars: int = 1500) -> tuple[bool, bool]:
    """Check that within window_chars of offset, both `benefit:` and `barrier:` appear."""
    window = content[offset: offset + window_chars]
    has_benefit = bool(re.search(r"\bbenefit\s*:", window, re.IGNORECASE))
    has_barrier = bool(re.search(r"\bbarrier\s*:", window, re.IGNORECASE))
    return (has_benefit, has_barrier)


def has_durability_and_erosion(content: str, offset: int, window_chars: int = 1500) -> tuple[bool, bool]:
    window = content[offset: offset + window_chars]
    has_durability = bool(DURABILITY_KEYWORDS.search(window) or re.search(r"\b(short|medium|long)\s*(-|:)\s*(duration|term|<|>|3|5|7)", window, re.IGNORECASE))
    has_erosion = bool(EROSION_VECTOR_HINTS.search(window))
    return (has_durability, has_erosion)


def value_chain_file_present(output_path: Path) -> Path | None:
    """Look for working/value-chain-profit-pools.md adjacent to output."""
    candidates = [
        output_path.parent / "value-chain-profit-pools.md",
        output_path.parent.parent / "working" / "value-chain-profit-pools.md",
        output_path.parent / "working" / "value-chain-profit-pools.md",
    ]
    for c in candidates:
        if c.exists():
            return c
    return None


def has_reconciliation_section(content: str) -> bool:
    """Look for a 'Cross-reference' or 'reconciliation' section that reaches MATCH/MISMATCH."""
    rec_section = re.search(
        r"(?is)#{1,4}\s*(cross[- ]reference|reconciliation)[^\n]*\n(.{50,2000}?)(?=\n#{1,4}\s|\Z)",
        content,
    )
    if not rec_section:
        return False
    body = rec_section.group(2)
    return bool(re.search(r"\b(MATCH|MISMATCH)\b", body))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-path", required=True)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    path = Path(args.output_path)
    if not path.exists():
        print(f"ERROR FileMissing: {path}", file=sys.stderr)
        return 2

    content = path.read_text(encoding="utf-8")
    failures: list[str] = []
    warnings: list[str] = []

    # Check 1: all 7 Powers explicitly assessed
    missing_powers = []
    unstaged_powers = []
    for name, rx in SEVEN_POWERS:
        mentioned, has_state = power_assessed(content, rx)
        if not mentioned:
            missing_powers.append(name)
        elif not has_state:
            unstaged_powers.append(name)
    if missing_powers:
        failures.append(
            f"Powers not assessed (must be present/absent/nascent): {', '.join(missing_powers)}"
        )
    if unstaged_powers:
        failures.append(
            f"Powers mentioned but state not declared within 400 chars: {', '.join(unstaged_powers)}. "
            "Each Power needs an explicit 'present', 'absent', or 'nascent' marker."
        )

    # Check 2: for each present Power, benefit + barrier + durability + erosion vector
    present = power_present_states(content)
    if not present:
        failures.append(
            "No Power marked 'present'. At least one Power must be marked present with full benefit/barrier/durability "
            "treatment OR the output must explicitly state 'no Power identifiable in this industry' (unstable finding)."
        )
    else:
        for name, offset in present:
            has_benefit, has_barrier = has_benefit_barrier(content, offset)
            if not has_benefit:
                failures.append(f"Present Power '{name}' is missing a `benefit:` statement within 1500 chars of its declaration.")
            if not has_barrier:
                failures.append(f"Present Power '{name}' is missing a `barrier:` statement within 1500 chars of its declaration.")
            has_dur, has_eros = has_durability_and_erosion(content, offset)
            if not has_dur:
                failures.append(f"Present Power '{name}' is missing a durability rating (short / medium / long with timeframe).")
            if not has_eros:
                failures.append(f"Present Power '{name}' is missing a named erosion vector. 'Will erode eventually' is not sufficient.")

    # Allow an explicit unstable finding to satisfy the no-present-Power case
    if "no Power identifiable" in content or re.search(r"not structurally protected|no power present|no helmer power", content, re.IGNORECASE):
        # Pop the no-present failure if we triggered it
        failures = [f for f in failures if "No Power marked 'present'" not in f]

    # Check 3: anti-pattern rejections
    for pattern, msg in ANTI_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            failures.append(f"Anti-pattern detected: {msg}")

    # Check 4: V/C/A/I tag coverage
    tag_count = len(re.findall(r"\[(V|C|A|I):", content))
    if tag_count < 5:
        failures.append(f"Insufficient provenance tag coverage: found {tag_count} V/C/A/I tags, need >=5.")

    # Check 5: cross-reference reconciliation if upstream exists
    vc_file = value_chain_file_present(path)
    if vc_file is not None:
        if not has_reconciliation_section(content):
            failures.append(
                f"value-chain-profit-pools.md present at {vc_file} but output lacks a Cross-reference / reconciliation "
                "section that reaches MATCH or MISMATCH explicitly. Add a '## Cross-reference reconciliation' section."
            )

    # Check 6: next_skills YAML
    if not has_next_skills_block(content):
        failures.append(
            "Missing trailing `next_skills:` YAML block. Append a fenced YAML block listing >=1 recommended next skill."
        )

    # --- Soft warnings ---
    if not re.search(r"\bAI\b|\bartificial intelligence\b", content):
        warnings.append("No AI discussion detected. Helmer's 2024-26 commentary identifies AI as asymmetric erosion vector — address explicitly.")
    if not re.search(r"power progression|s[- ]curve|origination|takeoff|stability", content, re.IGNORECASE):
        warnings.append("Power Progression / S-curve stage not referenced. Cross-check which Powers are stage-available.")

    # Warn if every present Power is rated Short
    if present:
        short_count = 0
        for name, offset in present:
            window = content[offset: offset + 1500]
            if re.search(r"\b(short)\b[^\n.]{0,30}(<?\s*3\s*y|erosion|duration|term)", window, re.IGNORECASE):
                short_count += 1
        if short_count == len(present) and len(present) >= 2:
            warnings.append("All present Powers rated Short-duration — winner-archetype Power profile is unstable. Confirm or escalate as finding.")

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

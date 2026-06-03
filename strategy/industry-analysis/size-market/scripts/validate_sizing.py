"""Validate a market-sizing output against the size-market discipline.

Checks:
- >=3 sub-segment rows present in a markdown table (>=7 if classified as Arena)
- Software/SaaS markets must include value-theory triangulation
- Trailing `next_skills:` YAML block with >=1 listed skill
- "de-averaging" statement present in the output text
- Arenas classification present (one of: Arena, Pre-arena, Mature, Contested mature, Declining)
- V/C/A/I provenance tags on numeric claims (coverage check + malformed-tag detection)
- Triangulation gap statement present if both top-down and bottom-up cited
- TAM > SAM > SOM ordering (if all three present)
- No LLM-aggregator-only citations (Perplexity, ChatGPT, Claude, Bard, Gemini without underlying source)
- No stale sources (dated before stale_year cutoff, default 2024) without "still current" justification
- Currency normalization stated (base currency declared in intake/methodology section)
- Definition lock present (one-sentence inclusion/exclusion rule)

Usage:
    python validate_sizing.py --output-path <path-to-market-sizing.md> [--stale-year 2024]

Exit codes:
    0 — all checks pass
    1 — one or more checks fail (details to stderr)
    2 — file missing or malformed
"""

import argparse
import re
import sys
from pathlib import Path


# LLM aggregators that should never be sole-cited
LLM_AGGREGATORS = ["perplexity", "chatgpt", "claude", "bard", "gemini", "copilot"]

# Keywords that mark a market as software/SaaS — value-theory triangulation required.
SAAS_KEYWORDS = [
    "saas", "software", "cloud", "platform", "api",
    "developer tools", "observability", "security software", "fintech-software",
]


def parse_money(text: str) -> float | None:
    """Parse a money string like '$4.2B' or '$120M' into a float in $B."""
    m = re.match(r"\$?\s*([\d,.]+)\s*([BMK]?)", text.strip().upper())
    if not m:
        return None
    try:
        value = float(m.group(1).replace(",", ""))
    except ValueError:
        return None
    unit = m.group(2)
    if unit == "B":
        return value
    if unit == "M":
        return value / 1000.0
    if unit == "K":
        return value / 1_000_000.0
    return value  # assume already in $B


def check_tam_sam_som_ordering(content: str) -> list[str]:
    """If TAM, SAM, SOM money values appear labeled, ensure TAM >= SAM >= SOM."""
    failures = []
    # Look for patterns like "TAM: $4.2B" or "TAM = $4.2B" or "**TAM**: $4.2B"
    pattern = r"\*?\*?(TAM|SAM|SOM)\*?\*?\s*[:=]\s*\$?\s*([\d,.]+\s*[BMK]?)"
    matches = re.findall(pattern, content, re.IGNORECASE)
    values = {}
    for label, raw in matches:
        v = parse_money(raw)
        if v is not None:
            # keep first occurrence per label
            values.setdefault(label.upper(), v)
    if "TAM" in values and "SAM" in values and values["SAM"] > values["TAM"] * 1.01:
        failures.append(f"TAM/SAM ordering violation: SAM ({values['SAM']}B) > TAM ({values['TAM']}B).")
    if "SAM" in values and "SOM" in values and values["SOM"] > values["SAM"] * 1.01:
        failures.append(f"SAM/SOM ordering violation: SOM ({values['SOM']}B) > SAM ({values['SAM']}B).")
    if "TAM" in values and "SOM" in values and values["SOM"] > values["TAM"] * 1.01:
        failures.append(f"TAM/SOM ordering violation: SOM ({values['SOM']}B) > TAM ({values['TAM']}B).")
    return failures


def check_llm_aggregator_sourcing(content: str) -> list[str]:
    """Flag tags whose only cited source is an LLM aggregator."""
    failures = []
    # Pull all tag contents
    tags = re.findall(r"\[(?:V|C|A|I):\s*([^\]]+)\]", content)
    for tag_body in tags:
        body_lower = tag_body.lower()
        is_aggregator = any(agg in body_lower for agg in LLM_AGGREGATORS)
        if not is_aggregator:
            continue
        # Check whether an underlying source is also named (year, report, filing, analyst etc.)
        has_underlying = bool(re.search(r"\b(20\d{2}|10-K|filing|report|note|analyst|trade body|IFR|SEMI|IBIS|Gartner|Bernstein|Morgan|JPM|Statista|Forrester|IDC)\b", tag_body, re.IGNORECASE))
        if not has_underlying:
            failures.append(f"LLM-aggregator-only citation: '[{tag_body[:60]}...]'. Trace to underlying source and cite that.")
    return failures


def check_stale_sources(content: str, stale_year: int) -> list[str]:
    """Flag tags citing pre-stale_year sources without 'still current' justification."""
    failures = []
    tags_with_year = re.findall(r"\[(?:V|C|A|I):\s*([^\]]+?(20\d{2})[^\]]*)\]", content)
    for full_body, year_str in tags_with_year:
        try:
            year = int(year_str)
        except ValueError:
            continue
        if year < stale_year:
            # Look for "still current" or "extrapolated" or "adjusted" in nearby context
            if not re.search(r"\b(still current|extrapolated|adjusted|structurally unchanged)\b", full_body, re.IGNORECASE):
                failures.append(f"Stale source ({year}) without 'still current' justification: '[{full_body[:80]}...]'")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-path", required=True)
    parser.add_argument("--stale-year", type=int, default=2024,
                        help="Sources dated before this year are stale (default 2024 for 2026 analyses)")
    args = parser.parse_args()

    path = Path(args.output_path)
    if not path.exists():
        print(f"ERROR FileMissing: {path}", file=sys.stderr)
        return 2

    content = path.read_text(encoding="utf-8")
    failures = []
    warnings = []

    # Check 1: de-averaging statement
    if "de-averaging" not in content.lower():
        failures.append("Missing de-averaging statement. Add explicit sentence: 'Aggregate growth is X%, but sub-segment Y...'")

    # Check 2: >=3 sub-segments (>=7 if Arena-classified)
    sub_segment_mentions = len(re.findall(r"sub-segment", content, re.IGNORECASE))
    growth_rate_rows = len(re.findall(r"\|\s*[\d.]+\s*%\s*\|", content))
    # Detect Arena classification (exact match — "**Classification:** Arena", excluding "Pre-arena").
    arena_strict = bool(re.search(r"\*\*Classification:\*\*\s*Arena(?!-)\b", content))
    if arena_strict:
        if growth_rate_rows < 7 and sub_segment_mentions < 7:
            failures.append(f"Arena-classified market requires >=7 sub-segments. Found {sub_segment_mentions} sub-segment mentions and {growth_rate_rows} growth-rate rows.")
    elif sub_segment_mentions < 3 and growth_rate_rows < 3:
        failures.append(f"Insufficient sub-segment decomposition. Found {sub_segment_mentions} sub-segment mentions and {growth_rate_rows} growth-rate rows. Need >=3 sub-segments per G3 discipline.")

    # Check 3: arenas classification
    if not re.search(r"\b(Arena|Pre-arena|Mature|Contested mature|Declining)\b", content):
        failures.append("Missing arenas classification. Add a section with one of: Arena / Pre-arena / Mature / Contested mature / Declining.")

    # Check 4: V/C/A/I tags present (coverage)
    tag_count = len(re.findall(r"\[(?:V|C|A|I):", content))
    if tag_count < 5:
        failures.append(f"Insufficient provenance tag coverage. Found {tag_count} V/C/A/I tags. Numeric claims must each carry a tag.")

    # Check 5: malformed (vague) tags
    malformed_tags = re.findall(r"\[(?:V|C|A|I):\s*(industry report|analyst|source|report)\s*\]", content, re.IGNORECASE)
    if malformed_tags:
        failures.append(f"Malformed provenance tags found (too vague): {len(malformed_tags)} instances. Tags must name the report, year, and section.")

    # Check 6: TAM > SAM > SOM ordering
    failures.extend(check_tam_sam_som_ordering(content))

    # Check 7: LLM-aggregator-only citations
    failures.extend(check_llm_aggregator_sourcing(content))

    # Check 8: stale sources
    failures.extend(check_stale_sources(content, args.stale_year))

    # Check 9: currency declared
    if not re.search(r"\b(base currency|currency:|USD|EUR|GBP|JPY|CNY)\b", content):
        warnings.append("No base currency declared. Add a 'Base currency: USD' line in the intake/methodology section.")

    # Check 10: definition lock
    if not re.search(r"\b(definition|defined as|includes:|excludes:|scope:)\b", content, re.IGNORECASE):
        warnings.append("No definition lock found. Add a one-sentence inclusion/exclusion rule near the top.")

    # Check 11: triangulation if both methods cited
    has_top_down = bool(re.search(r"top.?down", content, re.IGNORECASE))
    has_bottom_up = bool(re.search(r"bottom.?up", content, re.IGNORECASE))
    if has_top_down and has_bottom_up:
        if not re.search(r"\btriangulat", content, re.IGNORECASE):
            failures.append("Top-down and bottom-up both cited but no triangulation statement present.")
        if not re.search(r"\bgap\b|\bdelta\b|\breconcil", content, re.IGNORECASE):
            warnings.append("Triangulation present but no explicit gap/reconciliation statement. State the gap percentage.")

    # Check 12: SaaS/software markets must include value-theory triangulation
    content_lower = content.lower()
    is_saas = any(kw in content_lower for kw in SAAS_KEYWORDS)
    if is_saas:
        if not re.search(r"value.?theory", content, re.IGNORECASE):
            matched = [kw for kw in SAAS_KEYWORDS if kw in content_lower]
            failures.append(f"Software/SaaS market detected (keywords: {matched[:3]}) but no value-theory triangulation mention found. Value-theory is REQUIRED for software/SaaS — unit counts are noisy, value-per-customer is more defensible.")

    # Check 13: trailing next_skills YAML block
    # Look for a `next_skills:` key inside a trailing YAML block (--- ... ---) at end of file.
    trailing = content.rstrip()
    next_skills_match = re.search(
        r"---\s*\n((?:.*\n)*?)---\s*\Z",
        trailing,
        re.MULTILINE,
    )
    has_next_skills = False
    if next_skills_match:
        block = next_skills_match.group(1)
        if re.search(r"^\s*next_skills:\s*$", block, re.MULTILINE):
            # Check at least one list item below it
            after = block.split("next_skills:", 1)[1]
            list_items = re.findall(r"^\s*-\s+\S+", after, re.MULTILINE)
            if list_items:
                has_next_skills = True
    if not has_next_skills:
        failures.append("Missing trailing `next_skills:` YAML block at end of file. Append a `---\\nnext_skills:\\n  - skill-name\\n---` block listing >=1 next recommended skill for orchestrator automation.")

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
    if warnings:
        print(f"  ({len(warnings)} warnings — see above)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

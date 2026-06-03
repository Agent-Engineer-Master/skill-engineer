"""Validate an analyze-demand output against the analyze-demand discipline.

Checks (v1):
- >=1 JTBD identified with all 3 components (functional / emotional / social) named
- >=2 customer segments defined by JTBD, not demographic attributes
- >=1 substitution risk with NAMED substitute candidate + switching cost + likelihood
- WTP drivers present
- >=1 named demand signal with measurement source
- V/C/A/I tag coverage (>=4)
- next_skills YAML block at end

Anti-pattern detection:
- Demographic-only segment names (e.g., "Young urban professionals", "Mid-market enterprises",
  "SMBs", "Enterprise IT buyers", "Gen-Z consumers"). If segment headings appear demographic
  without a "hiring ... to" JTBD clause, fail.
- Lagging-indicator demand signals (revenue, market share, NPS, churn). Warning at minimum.

Usage:
    python validate_demand.py --output-path <path-to-demand.md>

Exit codes:
    0 — pass
    1 — fail
    2 — file missing
"""

import argparse
import re
import sys
from pathlib import Path


# Demographic / firmographic phrases that, if used AS a segment name without a job clause,
# indicate demographic-only segmentation.
DEMOGRAPHIC_RED_FLAGS = [
    r"young (urban )?professionals?",
    r"gen[\s\-]?z",
    r"millennials?",
    r"baby boomers?",
    r"mid[\s\-]?market (enterprises|companies|firms|buyers)",
    r"\bSMBs?\b",
    r"\bSMEs?\b",
    r"enterprise (IT )?buyers?",
    r"fortune\s*\d+\s+(companies|enterprises|buyers)",
    r"tier[\s\-]?[123] (OEMs?|customers?|buyers?)",
    r"manufacturers? with [><]\s*\$?\d",
    r"companies with \d+\s*[\+\-]\s*employees",
    r"customers? in (north america|europe|apac|emea|dach)",
]

# Phrase that indicates a JTBD-based segment definition.
JTBD_SEGMENT_PATTERN = re.compile(
    r"(buyers?|customers?|users?)\s+(who\s+)?(are\s+)?hir(e|ing)\s+(the\s+)?(product|solution|service|category)\s+to\s+",
    re.IGNORECASE,
)

# Lagging-indicator phrases.
LAGGING_INDICATORS = [
    r"\brevenue (growth|trend)\b",
    r"\bmarket share (trend|movement|growth)\b",
    r"\bNPS\b",
    r"\bchurn (rate)?\b",
    r"\bARR (growth|trend)\b",
]


def find_segment_headings(content: str):
    """Find subsection headings under the 'Segments' or 'Customer Segments' section."""
    # Locate the segments section — heading containing 'Segment'
    seg_section = re.search(
        r"(?im)^#{1,6}\s+[^\n]*\bsegments?\b[^\n]*\n(.+?)(?=^#{1,6}\s+|\Z)",
        content,
        re.DOTALL,
    )
    if not seg_section:
        return []
    body = seg_section.group(1)
    # Find sub-headings (### or ####) inside the segments section
    sub_headings = re.findall(r"(?im)^#{2,6}\s+([^\n]+)$", body)
    # Also pull bolded segment names like **Segment 1: ...** at start of lines
    bold_headings = re.findall(r"(?m)^\s*[-*]?\s*\*\*([^*\n]+?)\*\*\s*[:\-—]", body)
    return [h.strip() for h in (sub_headings + bold_headings)]


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

    # Check 1: JTBD with all three components named.
    # Look for explicit naming of functional, emotional, social jobs.
    has_functional = bool(re.search(r"(?i)\bfunctional (job|jtbd)\b", content))
    has_emotional = bool(re.search(r"(?i)\bemotional (job|jtbd)\b", content))
    has_social = bool(re.search(r"(?i)\bsocial (job|jtbd)\b", content))
    missing_components = []
    if not has_functional:
        missing_components.append("functional")
    if not has_emotional:
        missing_components.append("emotional")
    if not has_social:
        missing_components.append("social")
    if missing_components:
        failures.append(
            f"JTBD missing required component(s): {', '.join(missing_components)}. "
            "All three components (functional / emotional / social) must be named, "
            "even if minimal. See references/jtbd-methodology.md."
        )

    # Check 2: at least 2 segments AND they are JTBD-based, not demographic.
    # Strategy: locate segments section, find sub-headings, test each.
    segment_headings = find_segment_headings(content)
    if len(segment_headings) < 2:
        # Fallback: count JTBD-style "hiring X to" clauses.
        jtbd_clauses = len(JTBD_SEGMENT_PATTERN.findall(content))
        if jtbd_clauses < 2:
            failures.append(
                f"Insufficient customer segments. Found {len(segment_headings)} segment heading(s) "
                f"and {jtbd_clauses} JTBD-style segment clause(s). Need >=2 segments defined by "
                "the job they hire the product to do. See references/customer-segmentation.md."
            )

    # Check 2a: demographic-only segment names
    demographic_violations = []
    for heading in segment_headings:
        # Skip if heading is a meta-heading like "Customer Segments" or "Segment Analysis"
        if re.match(r"(?i)^(customer\s+)?segments?(\s+analysis)?$", heading.strip()):
            continue
        # Test for demographic red flags
        is_demographic = any(
            re.search(p, heading, re.IGNORECASE) for p in DEMOGRAPHIC_RED_FLAGS
        )
        # Test for JTBD clause in the heading itself
        has_jtbd_in_heading = bool(JTBD_SEGMENT_PATTERN.search(heading))
        if is_demographic and not has_jtbd_in_heading:
            demographic_violations.append(heading)
    if demographic_violations:
        failures.append(
            "Demographic-only segment naming detected. Segments named by demographic / "
            "firmographic attributes without a JTBD clause: "
            + "; ".join(f"'{h}'" for h in demographic_violations)
            + ". Restate each segment as 'Buyers hiring the product to [verb] [object] "
            "[contextual qualifier]'. See references/customer-segmentation.md anti-patterns."
        )

    # Check 3: substitution risk with named candidate + switching cost + likelihood.
    sub_section = re.search(
        r"(?im)^#{1,6}\s+[^\n]*\bsubstitut[a-z]*\b[^\n]*\n(.+?)(?=^#{1,6}\s+|\Z)",
        content,
        re.DOTALL,
    )
    if not sub_section:
        failures.append(
            "Missing `## Substitution Risk` section. The validator requires the exact "
            "heading 'Substitution Risk' for downstream consumer consistency. Rename your "
            "section. See references/substitution-risk.md."
        )
    else:
        sub_body = sub_section.group(1)
        has_switching_cost = bool(re.search(r"(?i)switching cost", sub_body))
        has_likelihood = bool(
            re.search(r"(?i)\b(likelihood|likely|low|moderate|high)\b", sub_body)
        )
        # Reject the lazy 'general competition' / 'other vendors' framings as the only candidate.
        lazy_only = re.search(
            r"(?i)\b(general competition|other vendors|competitive pressure)\b", sub_body
        ) and not re.search(
            # Check that at least one specific named candidate exists — proxy: a proper noun,
            # an "e.g." example, or "such as" specific naming.
            r"(?i)(e\.g\.|such as|including|like|named:|substitute candidate:|candidate:)",
            sub_body,
        )
        if not has_switching_cost:
            failures.append(
                "Substitution-risk section missing 'switching cost' decomposition. "
                "Each named substitute must state switching cost (financial / workflow / skill / "
                "psychological). See references/substitution-risk.md."
            )
        if not has_likelihood:
            failures.append(
                "Substitution-risk section missing likelihood rating. Each named substitute must "
                "state Low / Moderate / High likelihood over a stated horizon."
            )
        if lazy_only:
            failures.append(
                "Substitution risk lists only 'general competition' or 'other vendors' without "
                "naming specific substitute candidates. Name candidates (cross-category preferred). "
                "See references/substitution-risk.md."
            )

    # Check 4: WTP drivers present.
    wtp_section = re.search(
        r"(?im)^#{1,6}\s+[^\n]*\b(willingness[\s\-]to[\s\-]pay|wtp|wtp driver)\b[^\n]*\n(.+?)(?=^#{1,6}\s+|\Z)",
        content,
        re.DOTALL,
    )
    if not wtp_section:
        failures.append(
            "No willingness-to-pay (WTP) section found. Output must include WTP drivers per "
            "segment. See references/wtp-drivers.md."
        )
    else:
        wtp_body = wtp_section.group(2)
        if not re.search(r"(?i)\bdriver", wtp_body):
            failures.append(
                "WTP section present but does not state DRIVERS. WTP must be expressed as "
                "drivers (regulatory penalty avoidance, procurement friction, category framing, "
                "etc.), not as a single price. See references/wtp-drivers.md."
            )

    # Check 5: >=1 named demand signal with measurement source.
    signal_section = re.search(
        r"(?im)^#{1,6}\s+[^\n]*\b(demand signal|leading indicator|signals?)\b[^\n]*\n(.+?)(?=^#{1,6}\s+|\Z)",
        content,
        re.DOTALL,
    )
    if not signal_section:
        failures.append(
            "No demand-signal section found. Output must name >=1 leading indicator with "
            "measurement source, threshold, and meaning. See references/demand-signals.md."
        )
    else:
        sig_body = signal_section.group(2)
        # Look for measurement-source language
        has_source = bool(
            re.search(
                r"(?i)(measurement source|source:|google trends|app[\s\-]?store|github|"
                r"job[\s\-]posting|reddit|hackernews|expert interview|filing|distributor "
                r"reorder|channel check|trade show|keyword|search trend)",
                sig_body,
            )
        )
        if not has_source:
            failures.append(
                "Demand-signal section present but no measurement source named. Each signal "
                "must specify where the indicator lives (Google Trends, GitHub, job postings, "
                "channel checks, etc.). See references/demand-signals.md."
            )
        # Warn if signal looks like lagging indicator
        for lag in LAGGING_INDICATORS:
            if re.search(lag, sig_body, re.IGNORECASE):
                warnings.append(
                    f"Lagging-indicator phrase ('{lag}') detected in demand-signal section. "
                    "Leading indicators are the point — revenue / share / NPS / churn are lagging."
                )
                break

    # Check 6: V/C/A/I tag coverage
    tag_count = len(re.findall(r"\[(V|C|A|I):", content))
    if tag_count < 4:
        failures.append(
            f"Insufficient provenance tag coverage. Found {tag_count} V/C/A/I tags; need >=4. "
            "Every fact-claim about external state must carry a tag."
        )

    # Check 7: next_skills YAML block at end.
    tail = content[-2000:]
    next_skills_match = re.search(
        r"---\s*\n\s*next_skills\s*:\s*\n((?:\s*-\s*[^\n]+\n)+)\s*---",
        tail,
    )
    if not next_skills_match:
        failures.append(
            "Missing structured next_skills YAML block at end of file. Output must end with "
            "'---\\nnext_skills:\\n  - <skill-name>\\n---' listing >=1 recommended next skill."
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

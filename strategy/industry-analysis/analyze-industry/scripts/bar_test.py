"""Run the fresh-context senior-analyst bar test on an industry brief.

This script is a STUB in Phase 1 — it writes a structured prompt file that the
orchestrator's calling agent uses to spawn a fresh-context sub-agent (via the
Agent tool with subagent_type='general-purpose' or a dedicated bar-test agent).

In Phase 2, this script will be upgraded to invoke the Claude API directly with
a fresh context window — eliminating the manual sub-agent step.

Usage:
    python bar_test.py --brief-path <path-to-brief> --industry "<industry-slug>"

The brief path is the markdown synthesis draft (working/industry-brief-draft.md) —
the bar test grades content depth before the HTML render. It accepts any text
file path; the fresh-context sub-agent reads whatever file is passed.

Output:
    Writes <industry-dir>/bar-test-prompt.md with the prompt for the fresh sub-agent.
    Prints the path to stdout.
"""

import argparse
import sys
from pathlib import Path


PROMPT_TEMPLATE = """# Bar Test Prompt — {industry}

You are a senior sub-sector analyst with 15 years of experience in {industry}.
You have NOT seen the drafting context that produced this brief — you are reading
it cold, as a peer reviewer.

You are being paid to find what is missing or weak. Generic praise is useless.

## The brief

Read the brief at: `{brief_path}`

## Your output — return as JSON

```json
{{
  "non_obvious_observations": [
    "Observation 1 — something this brief surfaces that you had not previously articulated.",
    "Observation 2 — ...",
    "Observation 3 — ..."
  ],
  "obvious_observations_correctly_captured": [
    "Obvious thing 1 the brief gets right",
    "Obvious thing 2 ...",
    "Obvious thing 3 ...",
    "Obvious thing 4 ...",
    "Obvious thing 5 ..."
  ],
  "obvious_observations_MISSING": [
    "Anything obvious that the brief fails to address — this list MUST be empty before the brief ships"
  ],
  "overconfidence_flags": [
    "Any factual claim that reads as overconfident given the cited evidence"
  ],
  "modernization_flags": [
    "Any 2005-era framing that should be modernized — raw SWOT, BCG matrix, value chain without profit pool, 'moat' without naming a 7 Power, etc."
  ],
  "internal_consistency_contradictions": [
    "Any place where the WTP/HTW recommendation OR any conclusion contradicts a structural finding earlier in the brief. Example: 'Sec 3 argues data moat is sub-segment-specific; Sec 5 recommends acquiring across 3 distinct sub-markets — contradiction.' This list MUST be empty before the brief ships. 'Defer to Phase 2' is NOT a valid resolution — the brief must either resolve the contradiction in-text or change the recommendation to be consistent with the structural analysis."
  ],
  "verdict": "PASS" | "ITERATE" | "REJECT",
  "verdict_reasoning": "One paragraph."
}}
```

## Pass criteria

- non_obvious_observations: ≥3
- obvious_observations_correctly_captured: ≥5
- obvious_observations_MISSING: empty
- overconfidence_flags: zero (or all resolved)
- modernization_flags: zero (or all resolved)

If any criterion fails, return verdict ITERATE and list specifically which sections of the brief require rework.
"""


REPO_ROOT = Path(__file__).resolve().parents[5]
INDUSTRIES_DIR = REPO_ROOT / "08-knowledge" / "world-model" / "industries"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--brief-path", required=True)
    parser.add_argument("--industry", required=True)
    args = parser.parse_args()

    brief_path = Path(args.brief_path)
    if not brief_path.exists():
        print(f"ERROR BriefMissing: {brief_path} not found.", file=sys.stderr)
        return 2

    industry_dir = INDUSTRIES_DIR / args.industry
    if not industry_dir.exists():
        print(f"ERROR IndustryDirMissing: {industry_dir} not found.", file=sys.stderr)
        return 2

    prompt_path = industry_dir / "bar-test-prompt.md"
    prompt_path.write_text(
        PROMPT_TEMPLATE.format(industry=args.industry, brief_path=brief_path.as_posix()),
        encoding="utf-8",
    )
    print(str(prompt_path))
    print("Next: orchestrator spawns fresh-context sub-agent with this prompt; sub-agent's JSON output is written to bar-test.md.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

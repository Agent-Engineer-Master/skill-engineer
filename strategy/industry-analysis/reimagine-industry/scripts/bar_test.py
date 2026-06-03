"""Write the reimagination-specific bar test prompt for a fresh-context sub-agent.

Inherits the fresh-context discipline from analyze-industry's bar_test.py but
applies reimagination-specific pass criteria (≥3 non-obvious concepts, zero
AI-washed, zero feature-not-company, etc.).

The script writes the prompt file; the orchestrator's host agent spawns the
fresh-context sub-agent via the Task tool with this prompt + the concepts file
(but NOT the drafting context). The sub-agent returns a JSON verdict which the
orchestrator writes to bar-test.md.

Usage:
    python bar_test.py --slug <slug> --concepts-path <path-to-venture-concepts.md>

Output:
    Writes <industry-dir>/bar-test-prompt.md
    Prints the prompt path to stdout.
"""

import argparse
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[5]
INDUSTRIES_DIR = REPO_ROOT / "08-knowledge" / "world-model" / "industries"


PROMPT_TEMPLATE = """# Reimagination Bar Test — {industry}

You are a senior strategist with 15 years of experience evaluating venture
concepts in {industry}. You have NOT seen the drafting context that produced
these concepts — you are reading them cold, as a peer reviewer.

You are being paid to find what is missing or weak. Generic praise is useless.
Specific kills are valuable.

## The concepts

Read venture-concepts.md at: `{concepts_path}`
Read the supporting disruption-dataset.yaml at: `{dataset_path}`

## Your output — return as JSON

```json
{{
  "non_obvious_concepts": [
    "concept_id and one-sentence explanation of why it strikes you as non-obvious"
  ],
  "ai_washed_concepts": [
    "concept_id where the description is 'an AI for X' without specifying job, pain, or counter-position"
  ],
  "feature_not_company_concepts": [
    "concept_id that solves a real pain but lacks a counter-position incumbents cannot copy"
  ],
  "idea_maze_failures": [
    "concept_id that appears novel but has been tried by [companies] and failed for [reasons not addressed]"
  ],
  "why_now_failures": [
    "concept_id whose why-now would not survive a partner-meeting because [specific reason]"
  ],
  "internal_consistency_contradictions": [
    "concept_id where a stress test answer contradicts the Phase 1-3 dataset"
  ],
  "consultantese_violations": [
    "concept_id and quoted phrase that reads as generic strategy-deck prose. Test: could this sentence appear in any strategy deck about any industry? If yes, flag it. Specific examples to flag: 'leverages', 'fundamentally reshapes', 'robust', 'meaningful value', 'stakeholders', 'ecosystem', 'unprecedented', 'paradigm shift', 'strategic' as modifier, empty triadic lists, 'it's not just X — it's Y' construction."
  ],
  "set_level_observations": {{
    "diversity": "Are concepts structurally different, or seven flavors of one idea?",
    "coverage": "Are there obvious disruption angles missing from the set?",
    "strongest": "Which concept would you bet on, and why?",
    "weakest": "Which concept would you cut, and why?"
  }},
  "verdict": "PASS | ITERATE | REJECT",
  "verdict_reasoning": "One paragraph."
}}
```

## Pass criteria

- non_obvious_concepts: ≥3
- ai_washed_concepts: empty
- feature_not_company_concepts: empty
- idea_maze_failures: empty
- why_now_failures: empty
- internal_consistency_contradictions: empty
- consultantese_violations: empty (or ≤2 minor and isolated)

If any failure list is non-empty: return ITERATE and specify which phase
needs rework (Phase 4 framework generation, Phase 5 filter, prose rewrite,
or specific concept).

If non_obvious_concepts < 3: return ITERATE — the concepts are competent but
not surprising; revisit Phase 4 framework signals for under-mined opportunities.

## Anti-patterns to actively look for

- AI-washed concepts: "an AI agent for X" with no further specification
- Feature-not-company: solves a pain but incumbents could absorb it as a feature
- Counter-positioning that's just speed: "we move faster than the incumbent"
- 7 Powers labels without mechanism: "network effects" without same-side/cross-side
- Thiel Secret as marketing slogan: "we believe AI changes everything"
- Why-now without dated specificity: "recently AI has matured"
- Idea-maze without prior attempts: claims novelty without research
- Consultantese prose: "leverages", "fundamentally reshapes", "robust",
  "meaningful value", "stakeholders", "ecosystem", "strategic" as modifier,
  empty triadic lists, "it's not just X — it's Y"

## The specificity test

For each concept, apply this test to the prose: could this sentence appear
in any strategy deck about any industry? If yes, flag it as consultantese
drift. A reader of venture-concepts.md should be able to tell from the prose
alone that this is THE industry at THIS moment — specific companies named,
specific numbers cited, specific dated conditions, specific worked examples.
Generic strategy language fails the bar test.
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--slug", required=True)
    parser.add_argument("--concepts-path", required=True)
    args = parser.parse_args()

    concepts_path = Path(args.concepts_path)
    if not concepts_path.exists():
        print(f"ERROR ConceptsMissing: {concepts_path} not found.", file=sys.stderr)
        print("Fix: complete Phase 5/6 and ensure venture-concepts.md is written.", file=sys.stderr)
        return 2

    industry_dir = INDUSTRIES_DIR / args.slug
    if not industry_dir.exists():
        print(f"ERROR IndustryDirMissing: {industry_dir} not found.", file=sys.stderr)
        return 2

    dataset_path = industry_dir / "disruption-dataset.yaml"

    prompt_path = industry_dir / "bar-test-prompt.md"
    prompt_path.write_text(
        PROMPT_TEMPLATE.format(
            industry=args.slug,
            concepts_path=concepts_path.as_posix(),
            dataset_path=dataset_path.as_posix(),
        ),
        encoding="utf-8",
    )
    print(str(prompt_path))
    print(
        "Next: orchestrator spawns fresh-context sub-agent (Task tool) with this prompt; "
        "sub-agent's JSON output is written to bar-test.md.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

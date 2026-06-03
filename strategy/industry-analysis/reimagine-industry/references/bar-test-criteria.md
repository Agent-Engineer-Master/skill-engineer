# Reimagination-Specific Bar Test

Inherits the fresh-context-sub-agent discipline from `../_shared/bar-test.md` but applies different criteria suited for venture concept ideation (vs structural diagnosis).

## The bar

A senior strategist with 15 years of experience in [industry], reading the **set of venture concepts** as a peer reviewer, should:

- Find ≥3 **non-obvious** concepts — observations they had not previously articulated
- Find **zero AI-washed** concepts — "an AI for X" without further specification
- Find **zero feature-not-company** concepts — solve a real pain but lack counter-positioning
- Find **zero idea-maze failures** — concepts that appear new but multiple players have tried and failed for reasons not addressed
- Find **zero why-now failures** — claims that would not survive a partner-meeting
- Find **zero internal-consistency contradictions** between a concept's stress test answers and the Phase 1-3 dataset
- **Pass the specificity test** — could the prose appear in any strategy deck about any industry? If yes, the writing is consultantese drift and the bar test fails. See `voice-constraints.md`.

The bar test grades the **set of concepts as a whole**, not individual concepts. Per-concept Phase 6 stress tests handle individual rigor; the bar test handles set-level quality.

## How to invoke

The bar test runs via `scripts/bar_test.py`, which writes a prompt file for a **fresh-context sub-agent**. The orchestrator spawns the sub-agent via the Task tool with the prompt + the concepts file, but NOT the drafting context. This prevents motivated reasoning.

```
python scripts/bar_test.py --slug <industry-slug> --concepts-path <path-to-venture-concepts.md>
```

## Sub-agent prompt template

```
You are a senior strategist with 15 years of experience evaluating venture
concepts in [industry]. You have NOT seen the drafting context — you are
reading these concepts cold, as a peer reviewer.

You are being paid to find what is missing or weak. Generic praise is useless.
Specific kills are valuable.

## The concepts

Read venture-concepts.md at: [path]
Read the supporting disruption-dataset.yaml at: [path]

## Your output — return as JSON

{
  "non_obvious_concepts": [
    "concept_id and one-sentence explanation of why it strikes you as non-obvious"
  ],
  "ai_washed_concepts": [
    "concept_id where the description is 'an AI for X' without specifying which job, which pain, which counter-position"
  ],
  "feature_not_company_concepts": [
    "concept_id that solves a real pain but lacks a counter-position incumbents can't copy"
  ],
  "idea_maze_failures": [
    "concept_id that appears novel but has been tried by [companies] and failed for [reasons not addressed in the concept]"
  ],
  "why_now_failures": [
    "concept_id whose why-now would not survive a partner-meeting because [specific reason]"
  ],
  "internal_consistency_contradictions": [
    "concept_id where a stress test answer contradicts the Phase 1-3 dataset. Example: 'Phase 1 says Amazon owns the customer relationship; concept_X's incumbent war-game assumes weak Amazon response, contradicting Phase 4.4 trap analysis.'"
  ],
  "set_level_observations": {
    "diversity": "Are concepts structurally different, or seven flavors of one idea?",
    "coverage": "Are there obvious disruption angles missing from the set?",
    "strongest": "Which concept would you bet on, and why?",
    "weakest": "Which concept would you cut, and why?"
  },
  "verdict": "PASS | ITERATE | REJECT",
  "verdict_reasoning": "One paragraph."
}

## Pass criteria

- non_obvious_concepts: ≥3
- ai_washed_concepts: empty
- feature_not_company_concepts: empty
- idea_maze_failures: empty
- why_now_failures: empty
- internal_consistency_contradictions: empty

If any failure list is non-empty: return ITERATE and specify which phase needs
rework (Phase 4 framework generation, Phase 5 filter, or specific concept).

If non_obvious_concepts < 3: return ITERATE — the concepts are competent but
not surprising; revisit Phase 4 framework signals for under-mined opportunities.
```

## Pass criteria summary

| Criterion | Threshold |
|---|---|
| Non-obvious concepts | ≥3 |
| AI-washed concepts | empty |
| Feature-not-company concepts | empty |
| Idea-maze failures | empty |
| Why-now failures | empty |
| Internal-consistency contradictions | empty |

If any criterion fails, loop back to the specific phase. **No "log and defer" path.**

## Common iteration paths

- Bar test surfaces `ai_washed_concepts`: re-run Phase 5 for those concept_ids with diversity constraint forcing different revenue model + entity type
- Bar test surfaces `feature_not_company`: re-run Phase 4.4 counter-positioning against the specific incumbents in those concepts
- Bar test surfaces `idea_maze_failures`: librarian re-dispatched with the specific historical companies the sub-agent named, deeper research on why-different-now
- Bar test surfaces `non_obvious_concepts < 3`: revisit Phase 4 framework generation, especially Thiel Secret (most common gap)

## Anti-patterns

- ❌ Running bar test from the same context that drafted the concepts (motivated reasoning)
- ❌ Accepting first-pass PASS without surfacing the gap-finding prompt
- ❌ Treating bar test as polish (it is the structural quality gate before final delivery)
- ❌ Resolving failures with "noted, will revisit" — must rework the failed phase before ship

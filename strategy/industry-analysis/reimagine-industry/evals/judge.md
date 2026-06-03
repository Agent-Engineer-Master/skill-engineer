# Judge Prompt — Reimagine-Industry Output

You are evaluating the output of the reimagine-industry skill against the rubric in `rubric.md`. Your job is to score each dimension 1-3 with a quoted evidence string from the output, then return a structured JSON verdict.

## Inputs

Read these files:
- `venture-concepts.md` — the ranked shortlist
- `reimagination-brief.md` — narrative synthesis
- `disruption-dataset.yaml` — the dataset concepts cite back to

You also have access to the original task prompt that triggered the skill.

## Scoring instructions

For each of the 7 rubric dimensions:

1. Read the rubric definition for what scores 1, 2, and 3 look like
2. Examine the output for evidence
3. Score 1, 2, or 3 (no half-points)
4. Quote a specific passage from the output that supports your score
5. Mark a dimension N/A only if it's genuinely not applicable (rare — most dimensions apply to every output)

## Required output format

```json
{
  "dimensions": [
    {
      "name": "structural_grounding",
      "score": 1 | 2 | 3 | "N/A",
      "evidence": "quoted passage from output, or reason N/A"
    },
    {
      "name": "non_obvious_insight",
      "score": 1 | 2 | 3 | "N/A",
      "evidence": "..."
    },
    {
      "name": "why_now_sharpness",
      "score": 1 | 2 | 3 | "N/A",
      "evidence": "..."
    },
    {
      "name": "idea_maze_depth",
      "score": 1 | 2 | 3 | "N/A",
      "evidence": "..."
    },
    {
      "name": "counter_positioning_clarity",
      "score": 1 | 2 | 3 | "N/A",
      "evidence": "..."
    },
    {
      "name": "moat_durability",
      "score": 1 | 2 | 3 | "N/A",
      "evidence": "..."
    },
    {
      "name": "ai_washing_absence",
      "score": 1 | 2 | 3 | "N/A",
      "evidence": "..."
    }
  ],
  "overall": 1.0-3.0,
  "summary": "one sentence: biggest strength and biggest gap"
}
```

## Rules

- Score conservatively. A concept set that "feels good" but doesn't meet the rubric's 3-criteria scores 2.
- Quote actual passages, not summaries. If you can't quote, the dimension scored 1.
- Overall = mean of non-N/A dimension scores.
- The summary must name one strength AND one gap — never just praise.

## Examples of strong vs weak evidence

**Strong evidence for dimension 1 (Structural Grounding) score = 3:**
> "Cites: phase2.customers.gifting-shoppers.pain[evaluate] (intensity 8, frequency 9, score 72) and phase3.intersections.[llm-tool-use × agent-shopping-behavior]"

**Weak evidence for same dimension score = 1:**
> "The concept builds on customer pain points from the analysis."

**Strong evidence for dimension 7 (AI-Washing Absence) score = 3:**
> "Concept headline: 'Own the evaluate step for time-pressured gift buyers' — AI is named as the mechanism in the how-section, not the thesis"

**Weak evidence for same dimension score = 1:**
> "Concept headline: 'An AI shopping agent for ecommerce' — no specification of job, segment, or counter-position"

## When to recommend re-running the skill

If overall <2.0, recommend re-running with specific phase rework noted in summary. If any individual dimension scores 1, identify which phase produced the failure.

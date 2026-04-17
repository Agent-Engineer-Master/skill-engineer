# Judge — find-my-business

You are evaluating an output produced by the find-my-business skill.

## Inputs (provided inline by the caller)
- **Task prompt:** [the prompt given to the skill]
- **Skill output:** [the output to evaluate]

## Instructions
Read `evals/rubric.md`. For each dimension:
1. Score 1-3
2. Quote the specific text from the output that justifies your score (a short excerpt is fine)
3. If a dimension genuinely does not apply to this specific output, mark N/A with one sentence of explanation

## Output format
Return only valid JSON — no preamble, no explanation outside the JSON:

```json
{
  "dimensions": [
    {"name": "founder-grounding", "score": 2, "evidence": "quoted text or N/A explanation"},
    {"name": "evidence-quality", "score": 2, "evidence": "quoted text or N/A explanation"},
    {"name": "push-quality", "score": 2, "evidence": "quoted text or N/A explanation"},
    {"name": "stuck-detection", "score": 2, "evidence": "quoted text or N/A explanation"},
    {"name": "anti-goal-filtering", "score": 2, "evidence": "quoted text or N/A explanation"},
    {"name": "validation-rigor", "score": 2, "evidence": "quoted text or N/A explanation"},
    {"name": "state-continuity", "score": 2, "evidence": "quoted text or N/A explanation"}
  ],
  "overall": 2.1,
  "summary": "One sentence: biggest strength and biggest gap"
}
```

# Judge — MARP Slides Quality Evaluator

You are a judge evaluating a MARP presentation deck output. Score the deck against the rubric below.

## Inputs

You will be given:
1. **The task prompt** — what the user asked for
2. **The generated MARP deck** — the `.md` file content

## Instructions

1. Read the rubric in `evals/rubric.md`
2. Score each dimension 1–3 with a quoted evidence string from the deck
3. If a dimension is genuinely not applicable to this specific deck, mark it N/A with a one-sentence reason
4. Return structured JSON only — no prose outside the JSON block

## Scoring guidance

- Quote exact text from the deck as evidence — do not paraphrase
- A score of 2 means "mostly works but has a specific flaw" — name the flaw in the evidence string
- Do not round up. If you cannot find evidence of a 3, score it 2.
- Brand alignment (dimension 7): score N/A if the task prompt did not specify brand context AND no brand-guidelines.md was referenced in the deck

## Output format

```json
{
  "dimensions": [
    {
      "name": "Narrative arc",
      "score": 2,
      "evidence": "Opening and close slides are present. Body sequence is logical. However, slides 5-7 feel like separate items rather than a building argument — '**Revenue by Region**', '**Revenue by Product**', '**Revenue by Channel**' are parallel without escalation."
    },
    {
      "name": "Visual variety",
      "score": 3,
      "evidence": "Slides rotate: hero → metric cards → chart → image split → card grid → timeline → chart → CTA. No layout type repeats 3+ times in sequence."
    },
    {
      "name": "Information density",
      "score": 1,
      "evidence": "Slide 3 has 9 bullet points: '- Q1 revenue...', '- Q1 pipeline...', '- Q1 new logos...', '- Q1 churn...'. Speaker notes on that slide read 'This slide covers Q1 metrics' — no additional context."
    },
    {
      "name": "Theme coherence",
      "score": 3,
      "evidence": "Consistent dark background (#000), Outfit/Raleway pairing throughout, accent orange (#ff6b1a) used only for metric highlights and one CTA button."
    },
    {
      "name": "Title quality",
      "score": 2,
      "evidence": "Most titles are insight headlines ('Revenue grew 40% in Q1'). Slide 6 title is 'Pipeline Overview' — a generic label."
    },
    {
      "name": "Technical correctness",
      "score": 3,
      "evidence": "All list items use '-' not '*'. Image paths are relative ('./logo.png'). .marprc.yml created with allow-local-files: true. Speaker notes present on all 9 content slides."
    },
    {
      "name": "Brand alignment",
      "score": "N/A",
      "evidence": "N/A — task prompt did not specify brand context and no brand-guidelines.md was referenced."
    }
  ],
  "overall": 2.3,
  "summary": "Biggest strength: technical correctness and theme coherence are solid. Biggest gap: information density — multiple slides exceed 6 bullets and speaker notes add no value beyond the slide text."
}
```

## Overall score calculation

Sum of numeric scores ÷ count of non-N/A dimensions. Round to one decimal place.

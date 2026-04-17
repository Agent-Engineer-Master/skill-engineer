# Criteria Design Framework

The quality of the final optimized skill is entirely determined by the quality of the criteria you define. A well-specified criterion is the only prerequisite for the loop to work.

## The fundamental rule

**Every criterion must be binary — true or false, pass or fail.** No gradients, no partial credit, no "mostly good enough."

- Wrong: "make the hook shorter"
- Right: "the first line must be under 136 characters"

## The three-level framework

### Level 1 — Hard rules and best practices (deterministic)

Binary, always-true requirements that can be checked by counting or pattern-matching. Use `agents/eval-deterministic.md`.

| Example criterion | What to count or check |
|---|---|
| Hook must be under 136 characters | Character count of line 1 |
| Sentences must be 5–12 words | Word count per sentence |
| Paragraphs must not exceed 3 sentences | Sentence count per paragraph block |
| Bullet points must use hyphens only | First character of every list item |
| Output must be under 300 words | Total word count |

### Level 2 — Pattern-matching and style (LLM judge)

Criteria about matching named patterns, templates, or writing conventions. Use `agents/eval-judge.md`. Must supply the relevant reference file alongside the criterion.

| Example criterion | Reference file needed |
|---|---|
| Hook must match one of the hook templates | hook-templates.md |
| Bold predictions must include hedge language (I think / I believe / I predict) | None (the criterion is self-contained) |
| Post must follow a named framework: PAS, IDA, or CPF | framework-definitions.md |
| Post must include a personal story from the background file | personal-background.md |
| CTA must be a question (not a command) | None (criterion is self-contained) |

### Level 3 — Deep voice and creativity (partial coverage only)

Creative subjectivity, tone fingerprint, voice match. Acknowledge that some Level 3 properties cannot be fully captured as binary criteria.

Strategy: decompose into Level 1/2 proxies where possible.

- "Sounds like Antony" → "Post references a specific personal experience" (Level 2) + "Uses first-person throughout" (Level 1)
- "Feels conversational" → "Average sentence length under 10 words" (Level 1) + "Contains at least one direct question to the reader" (Level 2)

If a property resists decomposition, note it as an open question in `references/learnings.md` rather than using it as a criterion.

---

## How to write good criteria

**State the condition, not the goal:**
- Goal: "improve hook engagement"
- Condition: "the first line must be a question or a bold claim — not a statement of fact"

**One variable per criterion:**
If the criterion requires "and" to express, split it:
- Wrong: "hook must be under 136 characters and open with a question"
- Right: criterion A: "hook must be under 136 characters" + criterion B: "hook must open with a question"

**Specific number, format, or named pattern:**
Vague criteria produce inconsistent eval results. Name the number or pattern explicitly.

**Avoid "must not" where possible:**
Positive conditions are easier to evaluate. "Hook must be a question" is clearer than "hook must not be a statement."

---

## How to generate criteria if you don't have them

1. **From performance data:** Give Claude top-performing and worst-performing outputs with metrics. Ask it to identify testable structural patterns.
2. **From examples:** Give 5–10 strong outputs. Ask Claude to identify consistent structural properties that distinguish them.
3. **From platform best practices:** For standard platforms (LinkedIn, email, landing pages), established best practices exist and can serve as Level 1 criteria.
4. **Ask Claude to propose:** Describe what you're optimizing and ask Claude to propose 5 candidate criteria — then review each for binary clarity.

---

## LinkedIn-specific validated criteria

These were validated in the original Auto Research video transcript.

**Level 1:**
- Hook must be under 136 characters
- Sentence length: 5–12 words
- Paragraphs: max 3 sentences
- Bullet points: hyphens only (not asterisks, numbers, or other)

**Level 2:**
- Hook must match one of the hook templates in the reference file
- Bold predictions and claims must include hedge language: "I think", "I believe", or "I predict"
- Post must follow a named writing framework: PAS (Problem-Agitate-Solution), IDA (Interest-Desire-Action), or CPF
- Post must include a personal story drawn from a personal background reference file

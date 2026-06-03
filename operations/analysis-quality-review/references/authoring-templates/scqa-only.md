# Authoring Template — SCQA Only (short communication)

> **When to use this framework.** Short documents — one-pagers, emails, single-message communications — where the full Minto pyramid is overkill. The reader needs the answer fast; you don't have space for MECE supporting reasons + evidence drill-downs. SCQA is enough. Typically under 500 words. See `references/framework-selection-guide.md`.
>
> **How to use this template.** Fill in BEFORE writing. The Answer = your recommendation/position. The Situation + Complication establish why this needs the reader's attention. The Question is the question the Answer resolves.

---

## Frontmatter

```yaml
spec_type: authoring-spec
structural_framework: scqa-only
doc_type: brief | memo | deck
intent_summary: |
  [One paragraph — what is this communication for, who is the reader, what action
  or response do you want from them.]
```

---

## SCQA

### Situation

> **One or two sentences establishing what the reader already knows.** Should land as agreeable — the reader nods. Don't recap things the reader already accepts as background; recap only what's needed to set up the Complication.

Your Situation:
```
[Fill in — 1-2 sentences]
```

### Complication

> **One or two sentences naming what has changed, what is at risk, or what the reader hasn't yet realized.** The Complication is what makes the Question worth asking. If the reader doesn't feel the friction here, the rest of the document falls flat.

Your Complication:
```
[Fill in — 1-2 sentences]
```

### Question

> **One sentence — the question the Complication raises that the Answer resolves.** Usually implicit ("so what should we do about it?") but worth stating explicitly here.

Your Question:
```
[Fill in — one sentence]
```

### Answer

> **One sentence — your recommendation, position, or assertion.** This is the document's apex claim. If the reader read only this sentence, they'd know what you're saying.

Your Answer:
```
[Fill in — one sentence]
```

---

## D5 — Evidence

> **For SCQA-only, evidence is light — typically 1-3 key citations or data points supporting the Answer.** List them here. If you have more than 3 key pieces of evidence, the document is probably long enough to warrant `minto-pyramid` instead.

Key evidence:
```
1. [Claim + V/C/A/I tag + source]
2. [Claim + V/C/A/I tag + source]
3. [Claim + V/C/A/I tag + source — optional]
```

---

## D5 (readability) — Handles for codes

For short documents, internal codes should generally be avoided entirely — use plain-English throughout. If a code is unavoidable (cross-reference to a known artifact), define the handle here.

| Code | Plain-English handle |
|---|---|
| ... | ... |

---

## Pre-write checklist

- [ ] Situation is recapped to the minimum needed
- [ ] Complication creates real friction
- [ ] Question is explicit
- [ ] Answer is one declarative sentence
- [ ] Evidence list is short (≤ 3 items); if longer, switch to minto-pyramid

---

## What the review pass will grade

**Pass 1 — framework = scqa-only:**
- D3 (SCQA) — mandatory
- D1 (governing observation = Answer) — mandatory
- D5 (evidence carries) — mandatory
- D2 (MECE) — N/A (no supporting-reasons grouping)
- D7 (Rumelt) — N/A
- D8 (issue-tree) — N/A
- D4 (dot-dash) — optional (short docs may not have multiple sections)
- D6 (Frankenstein) — high-only

**Pass 2 (readability):** applies normally — action titles if sectioned, so-what test, specificity, jargon discipline, no internal codes in prose, active voice.

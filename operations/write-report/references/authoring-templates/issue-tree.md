# Authoring Template — Issue Tree (problem-solving)

> **When to use this framework.** The document works through a complex problem by decomposing the root question into MECE sub-questions. The analysis IS the point — the reader follows the decomposition to understand how the answer was reached. Conn & McLean's McKinsey 7-step problem-solving structure. Not for documents that already have the answer and are presenting it (use `minto-pyramid` or `rumelt-kernel`). See `references/framework-selection-guide.md`.
>
> **How to use this template.** Fill in BEFORE writing the document. The discipline this framework enforces is decomposition depth (D8) and MECE rigor (D2) — at every level of the tree, the sub-questions must be MECE and each sub-question must decompose 2-4 more levels.

---

## Frontmatter

```yaml
spec_type: authoring-spec
structural_framework: issue-tree
doc_type: brief | memo
intent_summary: |
  [One paragraph — what problem is this document solving, who is the reader, what
  decision will the answer inform.]
supporting_artifacts:
  - path: [path]
    role: source-of-truth | evidence
    description: [one line]
```

---

## Root question

> **The single question the document answers.** Stated as a question, not a claim. Should be specific enough that a sophisticated reader recognizes it as the right question — not "is X good or bad" but "what is causing X to decline at rate Y across segments Z."

Your root question:
```
[Fill in]
```

---

## Level-1 decomposition (MECE sub-questions)

> **3-5 sub-questions that together fully address the root question.** Mutually exclusive (no overlap between branches), collectively exhaustive (no gap a sophisticated reader would expect). This is D2 — the highest-priority dimension for issue-tree.

Your level-1 sub-questions:
```
1. [Sub-question]
2. [Sub-question]
3. [Sub-question]
4. [Sub-question — optional]
5. [Sub-question — optional]
```

**MECE tests at level 1:**
- Can any two sub-questions be merged? (If yes, they're not exclusive — merge them.)
- Would a sophisticated reader expect a sub-question you haven't included? (If yes, you're not exhaustive — add it.)
- Does each sub-question's answer feed directly into resolving the root question? (If no, that branch is off-topic — strike it.)

---

## Level-2 decomposition (D8 — decomposition depth check)

> **For each level-1 sub-question, decompose into 2-4 more specific sub-questions.** This is the depth test — if a level-1 sub-question can't decompose into multiple level-2 questions, it's probably either too narrow (a leaf, not a question) or it's actually evidence. The McKinsey rule: every branch decomposes 2-4 levels before reaching evidence.

### Sub-question 1: [restate]

Level-2 decomposition:
```
1a. [Sub-sub-question]
1b. [Sub-sub-question]
1c. [Sub-sub-question — optional]
```

### Sub-question 2: [restate]

Level-2 decomposition:
```
2a. [Sub-sub-question]
2b. [Sub-sub-question]
2c. [Sub-sub-question — optional]
```

### Sub-question 3: [restate]

Level-2 decomposition:
```
3a. [Sub-sub-question]
3b. [Sub-sub-question]
3c. [Sub-sub-question — optional]
```

(Repeat for additional sub-questions.)

**D8 test:** Every level-1 sub-question must decompose into ≥2 level-2 sub-questions. If a branch can't decompose, either it's evidence (move it down a level) or the branch is too narrow (merge with adjacent branch).

---

## D5 — Evidence per leaf

For each level-2 sub-question, list the evidence that will resolve it. Flag branches that have only A/I-tagged evidence as load-bearing risks.

Sub-question 1a evidence:
```
- [V/C/A/I tag + source + claim]
```

Sub-question 1b evidence:
```
- [V/C/A/I tag + source + claim]
```

(Repeat for all level-2 sub-questions.)

---

## D4 — Dot-dash narrative

The document should walk the tree top-down. Sketch section titles in tree order.

```
1. The root question and why it matters
2. [Level-1 sub-question 1]
   2.1 [Level-2 sub-question 1a]
   2.2 [Level-2 sub-question 1b]
3. [Level-1 sub-question 2]
   ...
N. Synthesis: what the tree resolves
```

**Test:** Can a reader follow the tree just from the section titles?

---

## D1 (optional) — Apex synthesis

Issue-tree documents typically end with a synthesis — what the resolved tree means. If you intend to include one, sketch it here. If the document is purely a decomposition (the reader synthesizes), write N/A.

Synthesis sentence (if any):
```
[Fill in or N/A]
```

---

## D5 (readability) — Handles for internal codes

If branches will be referred to by code (e.g., SQ-1, L2-3a), define their plain-English handles here.

| Code | Plain-English handle |
|---|---|
| [e.g., SQ-1] | [e.g., "the demand-side question"] |
| ... | ... |

---

## Pre-write checklist

- [ ] Root question is specific and sophisticated
- [ ] Level-1 sub-questions are MECE (no overlap, no gap)
- [ ] Every level-1 sub-question decomposes into ≥2 level-2 sub-questions (D8)
- [ ] Evidence inventory per level-2 leaf; A/I-tagged risks flagged
- [ ] Dot-dash titles trace the tree
- [ ] Handles drafted for all internal codes
- [ ] Synthesis sentence drafted (or explicit N/A)

---

## What the review pass will grade

**Pass 1 — framework = issue-tree:**
- D2 (MECE) — mandatory, dominant check
- D8 (decomposition depth) — mandatory
- D4 (dot-dash narrative) — mandatory
- D5 (evidence carries per leaf) — mandatory
- D1 (apex synthesis) — optional
- D7 (Rumelt kernel) — N/A
- D3 (SCQA) — N/A
- D6 (Frankenstein) — high-only

**Pass 2 (readability):** standard set — applies regardless of framework.

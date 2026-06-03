# Authoring Template — Descriptive (state-of-X analysis)

> **When to use this framework.** The document describes the state of something — an industry, a market, a system, a problem — without recommending action. The reader needs to understand what is true; downstream readers will use the document as input to their own decisions. Examples: industry state-of-the-market reports, post-mortems that don't recommend changes, diagnostic analyses that hand off to a separate recommendation document. Descriptive documents live or die on evidence — that's where the rigor is. Not for recommendation-driven documents (use `minto-pyramid` or `rumelt-kernel`). See `references/framework-selection-guide.md`.
>
> **How to use this template.** Fill in BEFORE writing. The discipline is in the evidence inventory (D5) — every claim about the state of X must carry V/C/A/I provenance. The apex governing observation is OPTIONAL — descriptive documents do not require a recommendation thesis. If you find yourself drafting one, ask whether the document is actually descriptive or whether it has an implicit recommendation that should be made explicit (in which case, use `minto-pyramid` or `rumelt-kernel`).

---

## Frontmatter

```yaml
spec_type: authoring-spec
structural_framework: descriptive
doc_type: brief | memo
intent_summary: |
  [One paragraph — what is this document describing, who is the reader, what
  downstream decision will it inform (even if this document doesn't make it).]
supporting_artifacts:
  - path: [path]
    role: source-of-truth | evidence
    description: [one line]
```

---

## D1 (optional) — Phenomenon thesis

> **Optional one-sentence framing of what the document is about.** Not a recommendation — a focus statement. ("This brief describes the structural drivers of margin compression in tier-2 wholesale across 2024-2026.") If you'd be uncomfortable stating this as a thesis because the document is genuinely just a survey, write N/A.

Phenomenon thesis (or N/A):
```
[Fill in or N/A]
```

---

## D2 (optional) — Mechanism categories

> **Optional MECE-style categorization of the mechanisms or factors the document covers.** Most descriptive documents organize by mechanism category — different causes, different segments, different sub-systems. If you do organize this way, list the categories here and apply the MECE test (no overlap, no gap).

Mechanism categories (or N/A):
```
1. [Category]
2. [Category]
3. [Category]
4. [Category — optional]
```

**MECE test (if categories used):** Can any two be merged? Is there a category a sophisticated reader would expect that's missing?

---

## D5 — Evidence inventory (HIGHEST PRIORITY)

> **For each major claim about the state of X, list the V/C/A/I-tagged evidence.** Descriptive documents live or die here. If a load-bearing claim has only A or I evidence, flag it explicitly — the document should NAME those gaps in its own prose, not hide them.

Claim → Evidence table:

| Claim | Section | Evidence (V/C/A/I + source) |
|---|---|---|
| [claim text] | [section] | [source] |
| [claim text] | [section] | [source] |
| ... | ... | ... |

**Critical gap list (claims with only A/I evidence — must be flagged in the document itself):**
```
- [claim] — evidence is [A/I-tagged source] — load-bearing risk for downstream decisions
- [claim] — ...
```

---

## D3 (optional, recommended) — SCQA opening

Descriptive documents often benefit from a SCQA opening even though they don't have an apex recommendation. The Answer = phenomenon thesis (or "this brief describes X.")

- Situation: `[Fill in]`
- Complication: `[Fill in — why does the state of X matter now?]`
- Question: `[Fill in — what does the reader need to know?]`
- Answer: `[Same as phenomenon thesis OR "this brief describes ..."]`

---

## D4 — Dot-dash narrative

The document walks through the mechanisms in sequence. Sketch section titles.

```
[Section 1 title]
[Section 2 title]
[Section 3 title]
[Section 4 title]
```

**Test:** Reading titles only, does a reader get the shape of the description? For descriptive documents, the titles can be either claims ("Margin compression is driven by Amazon private-label cycles") or section labels ("Mechanism 1: Amazon private-label cycles"). Either works at standard strictness; high strictness prefers claim-titles.

---

## D5 (readability) — Handles for internal codes

| Code | Plain-English handle |
|---|---|
| ... | ... |

---

## Pre-write checklist

- [ ] Document genuinely is descriptive — no buried recommendation
- [ ] Phenomenon thesis drafted (or explicit N/A)
- [ ] Mechanism categories MECE (or explicit N/A)
- [ ] Evidence inventory complete — every claim has a V/C/A/I tag
- [ ] A/I-tagged claims flagged as critical gaps; document will name them
- [ ] Dot-dash titles drafted

---

## What the review pass will grade

**Pass 1 — framework = descriptive:**
- D5 (evidence carries) — mandatory, highest-priority check
- D4 (dot-dash narrative) — mandatory
- D1 (phenomenon thesis) — optional
- D2 (mechanism MECE) — optional
- D3 (SCQA) — optional (recommended at high)
- D7 (Rumelt) — N/A
- D8 (issue-tree) — N/A
- D6 (Frankenstein) — high-only

**Critical:** Pass 1 reviewer reads the document's own prose looking for **implicit recommendations**. If a descriptive-framed document is found to contain a buried recommendation, the reviewer FAILS with "framework mismatch — switch to minto-pyramid or rumelt-kernel." Choosing `descriptive` to dodge the rigor of an apex governing observation is a bad-faith framework choice.

**Pass 2 (readability):** applies normally.

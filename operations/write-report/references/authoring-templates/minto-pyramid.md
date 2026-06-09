# Authoring Template — Minto Pyramid (recommendation-driven)

> **When to use this framework.** Recommendation-driven analytical documents for a senior reader: executive briefs, partner decks, argumentative memos. The reader should be able to read the first sentence (the governing observation) and know what you're recommending. Not for strategy documents (use `rumelt-kernel`), problem-solving (use `issue-tree`), or descriptive analyses (use `descriptive`). See `references/framework-selection-guide.md`.
>
> **How to use this template.** You — the calling skill — fill this in using your subject context BEFORE writing the document. The goal is the ghost-deck discipline: fix the storyline FIRST, then write the prose. When this template is filled in, the result is a tailored authoring spec for your specific subject. You then submit that spec to `write-report` in `mode: spec-judge` for grading. If the judge returns PASS, you write the document. If FAIL, you fix the spec (not the document — there is no document yet) and re-submit. After 3 failed iterations, the judge returns ESCALATE — consult a human.
>
> Do NOT skip sections. Every section is graded. If a dimension does not apply, write `N/A — [specific reason]` rather than deleting the section.
>
> The spec-judge grades against `references/spec-judge-rubric.md`. Read it before filling this in if you want to optimise for first-pass clearance.

---

## Frontmatter

```yaml
spec_type: authoring-spec
doc_type: brief
intent_summary: |
  [One paragraph — what is this brief for, who is the reader, what decision does it
  inform. The judge calibrates severity against this. A venture shortlist for a
  partner has different tolerances than a working memo.]
supporting_artifacts:
  - path: [path]
    role: source-of-truth | evidence | framework-reference
    description: [one line]
  # ... add as many as relevant
load_bearing_codes:
  # List concept codes you intend to use in the brief and their canonical plain-English handles
  - code: [e.g., SECRET-02]
    handle: [e.g., "the retailer-AI dominance signal"]
    canonical_definition_at: [path#anchor in source-of-truth artifact]
```

---

## D1 — Governing observation

State the brief's apex claim as **one declarative sentence with a finite verb that takes a position**. The rest of the brief must defend this. Derive from the evidence inventory in D5 — do not invent.

**Fail modes the judge catches:**
- Question instead of claim ("Is X attractive?")
- Topic label without a verb ("The integrator layer")
- Two competing claims
- Hedge that takes no position ("There may be opportunity")

**Your D1 (write here):**

> [one sentence]

---

## D2 — Supporting axes (MECE)

List 3–5 supporting axes that, taken together, prove D1. Each axis is one of the brief's top-level sections. Mutually exclusive (no >20% overlap between any pair) and collectively exhaustive (no obvious axis missing for a senior reader).

For a recommendation brief, "risks and what could break the thesis" is almost always one of the axes — if you omit it, justify here.

**Your axes (3–5):**

1. **Axis 1 label.** [one-line description of what this axis argues]
2. **Axis 2 label.** [description]
3. **Axis 3 label.** [description]
4. **Axis 4 label (optional).** [description]
5. **Axis 5 label (optional).** [description]

**MECE self-check (write here):**
- Overlap probe: which two axes are closest? Why don't they overlap?
- Gap probe: what axis would a senior reader expect that you're not including? Why is omission defensible?

---

## D3 — SCQA opening

Fill in each of the four. The Answer MUST restate D1 verbatim or near-verbatim. The Question must follow logically from the Complication.

- **Situation.** [1–2 sentences of context the reader already agrees with]
- **Complication.** [1–2 sentences on what changed or is at risk]
- **Question.** [the explicit research question this brief answers]
- **Answer.** [restate D1 verbatim]

**Coherence self-check:** does the Question naturally arise from the Complication? Does the Answer = D1?

---

## D5-structure — Evidence inventory per axis

For each axis listed in D2, list ≥2 supporting evidence items. Tag each with `[V]` (verified) / `[C]` (cited) / `[A]` (asserted) / `[I]` (inferred) and a path into supporting_artifacts.

**Axis 1 evidence:**
- [V] [claim] — `path/to/artifact#anchor`
- [C] [claim] — `path/to/artifact#anchor`

**Axis 2 evidence:**
- [V] [claim] — `path/to/artifact#anchor`
- [A] [claim] — `path/to/artifact#anchor`   <!-- flag any axis where evidence is only [A]/[I] -->

[... repeat per axis]

**Load-bearing risk flag (write here):** which axes are supported only by `[A]` or `[I]` evidence? Those are at risk of failing Pass 1 D5 against the written document. Either upgrade evidence before writing or accept the risk explicitly.

---

## D5-readability — Plain-English handles for load-bearing codes

For every concept code declared in frontmatter `load_bearing_codes`, confirm the handle is plain English and telegraphs meaning on first read. A partner reading the brief cold should understand the handle without consulting the cross-reference table.

| Code | Handle | Telegraphs meaning to a cold reader? (yes/no) |
|---|---|---|
| SECRET-02 | the retailer-AI dominance signal | yes |
| M1-DTC | the APAC integrator roll-up option | yes |
| [your code] | [your handle] | [your judgment] |

**Fail modes the judge catches:**
- Handle is itself jargon ("the AUTH-DTC mechanism")
- Handle is generic ("the signal", "the option")
- Handle contradicts the canonical definition in source-of-truth

---

## D7 — Rumelt strategy kernel

For recommendation briefs. Fill in all three; coherence between them is what the judge grades.

- **Diagnosis.** [What is the situation? What is the OBSTACLE to overcoming it? Not a goal, not a market description — an obstacle.]
- **Guiding policy.** [The overall approach to overcoming the named obstacle. Must explicitly target the diagnosis.]
- **Coherent actions.** [Specific moves — verb + concrete object + time bound where possible. Not "become the leader". Not "achieve X share".]

**Coherence self-check:**
- Does the policy target the obstacle in the diagnosis?
- Does each action implement the policy (not a different policy)?
- Are any "actions" actually goals?

For informational briefs without a recommendation: write `N/A — informational brief, no recommendation`.

---

## Pre-write checklist

Tick all before submitting to `mode: spec-judge`:

- [ ] D1 is a single declarative sentence with a verb that takes a position.
- [ ] D2 has 3–5 axes that are MECE for this brief's intent_summary.
- [ ] D3 Answer = D1 verbatim; Question follows from Complication.
- [ ] D5-structure: every axis has ≥2 tagged evidence items pointing to declared artifacts.
- [ ] D5-readability: every load-bearing code has a plain-English handle that telegraphs meaning.
- [ ] D7: diagnosis names an obstacle, policy targets it, actions implement it (or marked N/A).
- [ ] All cited artifact paths exist and are readable.
- [ ] Concept codes referenced have canonical definitions in declared source-of-truth artifacts.

---

## What the review pass will then grade

After spec-judge returns PASS, you write the brief. The brief then goes through the standard two-pass review:

- **Pass 1 (structure):** D1 (single governing observation), D2 (MECE), D3 (SCQA), D4 (dot-dash narrative coherence in section titles), D5 (evidence carries against each reason), D6 (Frankenstein detection, high-strictness), D7 (Rumelt kernel in the written prose).
- **Pass 2 (readability):** D1 (action titles), D2 (so-what completion), D3 (specificity over abstraction), D4 (jargon discipline), D5 (no internal codes in narrative prose), D6 (Frankenstein, high-strictness), D7 (one-message discipline, high-strictness).

The spec stage exists so Pass 1 and Pass 2 don't have to catch structural problems that should never have made it into prose. A clean spec means a faster review loop.

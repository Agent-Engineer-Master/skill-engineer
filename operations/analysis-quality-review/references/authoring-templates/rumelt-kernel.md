# Authoring Template — Rumelt Kernel (strategy document)

> **When to use this framework.** The document is a strategy — it names what to do, *anchored in* a diagnosis of the situation, with coherent actions that follow from a guiding policy. Rumelt's central claim: strategy = Diagnosis + Guiding Policy + Coherent Actions. If your document lacks any of the three, it is not strategy — pick a different framework. The most common failure mode this framework catches: goal-masquerading-as-strategy ("be the leader in X" is a goal; "out-invest competitors in Y while letting Z atrophy because of diagnosis W" is a strategy). See `references/framework-selection-guide.md`.
>
> **How to use this template.** Fill in BEFORE writing the document. The kernel (D7) is the apex check — most of your work happens in defining the diagnosis crisply. Minto-style checks (D1, D2, D5) fire NESTED inside the guiding policy and coherent actions — the rubric handles that, you don't pick "rumelt + minto."

---

## Frontmatter

```yaml
spec_type: authoring-spec
structural_framework: rumelt-kernel
doc_type: brief | memo | deck
intent_summary: |
  [One paragraph — what is this strategy for, who is the reader, what decision does it
  inform. The reader needs to know: is this a 90-day operational plan, a 5-year strategy,
  a category strategy, etc.]
supporting_artifacts:
  - path: [path]
    role: source-of-truth | evidence | framework-reference
    description: [one line]
load_bearing_codes:
  - code: [e.g., DIAG-1]
    handle: [e.g., "the structural margin compression in Tier-2 wholesale"]
    canonical_definition_at: [path#anchor]
```

---

## D7 — The kernel

The kernel has three components. All three are mandatory. If any is missing, the document is not yet a strategy.

### Diagnosis

> **One paragraph describing the situation in a way that makes the strategy obvious.** The diagnosis is the hardest part of strategy work — it names the dominant pattern in the situation in a way that resolves ambiguity about what matters. A weak diagnosis lists symptoms; a strong diagnosis isolates the structural force driving them.

Your diagnosis:
```
[Fill in]
```

**Tests for the diagnosis:**
- Is this a STRUCTURAL claim, not a symptom list? ("Margins are compressing across all our tier-2 wholesale accounts because Amazon's private-label cycle has crossed the price-point threshold in our category" is structural. "We have a sales problem" is symptomatic.)
- Does it have a NAMED MECHANISM? (Not "the market is changing" but "X is shifting because Y, which means Z.")
- Does it sharpen the strategic question, or does it leave the question ambiguous? Strong diagnosis closes off options.

### Guiding Policy

> **The overall approach that responds to the diagnosis.** Not a goal ("be #1 in X"), not a vision ("become the leader"), not a slogan. A guiding policy names the approach — what we'll emphasize, what we won't, where we'll concentrate force.

Your guiding policy:
```
[Fill in]
```

**Tests for the guiding policy:**
- Does it respond directly to the diagnosis? (If you swapped a different diagnosis in, would this policy still make sense? If yes, the policy isn't anchored.)
- Does it have a "we WON'T" embedded — something the policy explicitly de-emphasizes? Strategy is choice; a policy that says yes to everything is not a strategy.
- Could a competitor copy this policy easily? If yes, it's probably a goal, not a strategy.

### Coherent Actions

> **The set of concrete actions that follow from the policy.** Each action must implement the policy, not contradict it. Actions must be MECE — they don't overlap, they collectively implement the policy.

Your actions (3-5 actions, MECE):
```
1. [Action]
2. [Action]
3. [Action]
4. [Action — optional]
5. [Action — optional]
```

**Tests for coherent actions:**
- Does each action follow from the policy? (Strike actions that don't.)
- Are the actions MECE? (Can two be merged? Is there an obvious action missing that the policy implies?)
- Are the actions concrete enough to assign and execute? ("Improve customer experience" is not an action; "Restructure the returns process to 2-day resolution" is.)

### Kernel coherence check

The three components must align:

- Does the **guiding policy respond to the diagnosis**? If a reader saw the policy without the diagnosis, would they understand WHY this approach?
- Do the **actions implement the guiding policy**? If a reader saw the actions without the policy, would they recognize the approach?
- Could you **swap in a different diagnosis and have the policy still make sense**? If yes, the kernel is loose — the policy isn't actually anchored in the diagnosis.

---

## D1 (nested) — Governing observation = Guiding Policy

In Rumelt-framed documents, the guiding policy IS the governing observation. The reader should be able to read the first paragraph after the diagnosis and know what you're recommending. State your guiding policy as a single sentence below — this becomes the document's apex claim.

Apex sentence:
```
[Fill in — should be a restatement of the guiding policy as one declarative sentence]
```

---

## D2 (nested) — MECE on coherent actions

Already addressed under "Coherent Actions" above. Apply the MECE test rigorously: actions must be mutually exclusive (no overlap) and collectively exhaustive (no gap a reader would expect).

---

## D3 (optional at standard, recommended at high) — SCQA opening

If you include a SCQA opening, the Answer = guiding policy. Draft it here:

- Situation: `[Fill in]`
- Complication: `[Fill in]`
- Question: `[Fill in]`
- Answer: `[Same as your apex sentence above]`

If the SCQA feels redundant with the diagnosis paragraph, skip it — at strictness `standard` it's optional for rumelt-kernel.

---

## D4 — Dot-dash narrative

Sketch the section titles your document will use, in sequence. Read them as a standalone narrative. Do they trace the kernel?

```
[Section 1 title]
[Section 2 title]
[Section 3 title]
[Section 4 title]
[Section 5 title]
[Section 6 title]
```

**Test:** Can a reader skim the titles and understand the strategy? If not, sharpen the titles to be claims, not labels.

---

## D5 — Evidence inventory

For each major claim in the diagnosis and each major action, list the V/C/A/I-tagged evidence you'll cite. Flag any claim that has only A or I evidence — these become load-bearing risk if not addressed before writing.

Diagnosis claims and evidence:
```
- Claim 1: [text] | Evidence: [V/C/A/I + source]
- Claim 2: [text] | Evidence: [V/C/A/I + source]
```

Action-implementation evidence (why this action will work):
```
- Action 1: [why it works] | Evidence: [V/C/A/I + source]
- ...
```

---

## D5 (readability) — Handles for internal codes

If you'll use any internal codes in the document (DIAG-1, ACTION-3, etc.), define their plain-English handles here. The codes can appear in parentheses for cross-reference, but the prose should use the handle.

| Code | Plain-English handle | Canonical definition |
|---|---|---|
| [e.g., DIAG-1] | [e.g., "the Amazon private-label crossing"] | [path#anchor] |
| ... | ... | ... |

---

## Pre-write checklist

- [ ] Diagnosis is structural and has a named mechanism
- [ ] Guiding policy responds to the diagnosis (would not make sense with a different diagnosis swapped in)
- [ ] Guiding policy has an explicit "we won't" — strategy is choice
- [ ] Coherent actions implement the policy (each one traces back)
- [ ] Coherent actions are MECE
- [ ] Apex sentence (= guiding policy as one declarative claim) drafted
- [ ] Dot-dash titles drafted; reads as standalone narrative
- [ ] Evidence inventory drafted; A/I-tagged risks flagged
- [ ] Handles drafted for all internal codes

When all items checked, submit to `mode: spec-judge`.

---

## What the review pass will grade

**Pass 1 (structure) — rubric-structure.md, framework = rumelt-kernel:**
- D7 (Rumelt kernel coherence) — mandatory, apex check
- D1 (governing observation = guiding policy) — mandatory
- D2 (MECE on coherent actions) — mandatory
- D4 (dot-dash narrative) — mandatory
- D5 (evidence carries) — mandatory
- D3 (SCQA) — optional at standard, recommended at high
- D6 (Frankenstein) — high-only

**Pass 2 (readability) — rubric-readability.md, applies regardless of framework:**
- D1 (action titles), D2 (so-what), D3 (specificity), D4 (jargon discipline), D5 (no internal codes in prose), D6/D7 (high-only)

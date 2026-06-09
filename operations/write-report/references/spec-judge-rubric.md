# Spec-Judge Rubric

Dimensions evaluated by `spec-judge` on a filled-in authoring spec BEFORE the calling skill writes the full document. The spec is the ghost-deck storyline scaffold.

**Which dimensions fire depends on the declared `structural_framework`.** The judge reads `structural_framework` from the spec's frontmatter (or from the orchestrator's input) and grades against the applicable dimensions per the table below. Wrong-framework grading (applying Minto checks to a descriptive document, or skipping the Rumelt kernel check on a strategy document) is the most common cause of judge over-application or under-application.

The rubric is closed — the judge must not invent dimensions. Calling skill is the spec writer AND the spec fixer; the judge only grades.

## Strict-mode template acceptance (gate)

Before grading any dimension, the judge checks that the spec follows the structure of the framework-matched template at `references/authoring-templates/<structural_framework>.md`. If not, the judge returns `VERDICT: REJECT` with rationale "spec does not follow template structure for framework=X".

Non-conforming specs are not graded. The caller must refill the template.

## Framework × dimension matrix

Which dimensions fire for each framework. **M** = mandatory at standard+, **O** = optional / recommended, **N/A** = does not apply, **partial** = limited scope.

| Dimension | minto-pyramid | rumelt-kernel | issue-tree | scqa-only | adr | concept-page | descriptive |
|---|---|---|---|---|---|---|---|
| D1 governing observation | M | M (= guiding policy) | O (apex synthesis) | M (= Answer) | M (= Decision) | O | O (= phenomenon thesis) |
| D2 MECE | M | M (on coherent actions; nested under policy) | M (high bar) | N/A | N/A | O | O (on mechanism categories) |
| D3 SCQA opening | M | O | N/A | M | partial | N/A | O |
| D5-structure evidence inventory | M | M | M (per leaf) | M | M | M | M (highest priority) |
| D5-readability handles | M | M | M | O | M | O | M |
| D7 Rumelt kernel coherence | N/A | M | N/A | N/A | partial (Decision implies diagnosis) | N/A | N/A |
| D8 issue-tree depth | N/A | N/A | M | N/A | N/A | N/A | N/A |
| Cross-reference plausibility (high-only) | H | H | H | H | H | H | H |

## Strictness gating

Strictness governs review depth ON TOP OF the framework filter. A dimension only fires if both the framework table and the strictness gate allow it.

| Strictness | Dimensions evaluated (within those the framework allows) |
|---|---|
| `low` | D1, D7 (where framework includes them) |
| `standard` | All M and O dimensions for the framework |
| `high` | All M, O, and H dimensions for the framework |

---

## D1 — Governing observation is a CLAIM, not a question

**Pass criterion.** The spec's D1 section contains exactly one declarative sentence with a finite verb that takes a position. The sentence is falsifiable in principle: a senior reader could disagree with it on substantive grounds.

**Common failure modes.**
- Sentence is a question ("Is the integrator layer attractive over a 5-year hold?").
- Sentence is a topic label without a verb ("The integrator layer in industrial robotics").
- Two competing claims ("Integrators are attractive. OEM software is also attractive.").
- Vague hedge that takes no position ("There may be opportunity in robotics depending on conditions").
- Restatement of intent_summary that doesn't actually conclude.

**`suggested_fix_shape` the judge writes.** "Rewrite D1 as a single declarative sentence containing a verb and a position the rest of the spec must defend. Derive the claim from the existing axes and evidence inventory — do not invent a thesis."

---

## D2 — Axes are MECE

**Pass criterion.** The spec lists 3–5 supporting axes that:
- **Mutually exclusive** — no pair of axes overlaps conceptually by >20%.
- **Collectively exhaustive** — no obvious axis a senior reader would ask about is missing for the stated `intent_summary`.

The judge ACTIVELY probes for overlap and gaps. It reads the one-line description under each axis label (not just the label) and asks: "Could content under axis A reasonably live under axis B instead?" and "What axis would I expect that isn't here?"

**Common failure modes.**
- Two axes with overlapping descriptions ("Customer demand" + "Demand-side trends").
- Recommendation spec with no risks-or-objections axis.
- Market spec with no competitive dynamics axis.
- Strategy spec with no implementation-cost axis.
- <2 axes (pyramid collapsed) or >7 axes (over-granular — the spec should group).

**`suggested_fix_shape`.** "Merge axes {A} and {B} into a single axis covering {union concept}; OR add a missing axis for {named gap, e.g., risk, competitive response, execution cost}; aim for 3–5 axes total."

---

## D3 — SCQA coherence

**Pass criterion.** The spec contains explicit S / C / Q / A entries. Three coherence rules:
- **Answer restates D1.** The Answer field equals D1 verbatim or near-verbatim. Different wording → drift.
- **Question follows from Complication.** The Question is the explicit research question that the Complication forces.
- **Situation introduces agreed-on ground.** Situation is not in tension with itself; the tension shows up only in Complication.

**Common failure modes.**
- Answer drifts from D1 (different claim, or softer version).
- Question is unrelated to Complication ("market is fragmenting" → "what's our brand strategy?").
- Situation contains the complication (no real tension build).
- Missing element (most common: no explicit Question).

**`suggested_fix_shape`.** "Rewrite SCQA so Answer = D1 verbatim; Question follows from Complication's tension; Situation is agreed-on context only."

---

## D5-structure — Evidence inventory per axis

**Pass criterion.** Each axis lists ≥2 supporting evidence items, each:
- Tagged with `[V]` (verified) / `[C]` (cited) / `[A]` (asserted) / `[I]` (inferred)
- Pointing to a path inside the declared `supporting_artifacts`
- Topically establishing the axis claim (not just topically adjacent)

**Common failure modes.**
- An axis has no evidence inventory (just an axis label).
- All evidence under an axis is `[A]` or `[I]` only — judge flags as **load-bearing risk for the Pass 1 stress test** ("this axis will likely fail Pass 1 D5 unless evidence is upgraded before writing").
- Evidence items reference artifacts not in the manifest.
- Evidence is topically related but doesn't establish the claim.

**`suggested_fix_shape`.** "Add ≥2 [V]/[C]-tagged evidence items per axis with explicit artifact paths. If only [A]/[I] available for an axis, either upgrade evidence before writing OR explicitly accept the Pass 1 risk in the spec."

---

## D5-readability — Handles are plain English

**Pass criterion.** Every load-bearing concept code (e.g., `SECRET-02`, `M1-DTC`, `CP-4`) declared anywhere in the spec carries a plain-English handle that telegraphs meaning on first read. A partner reading the spec cold should understand what the handle means without consulting the cross-reference table.

**Common failure modes.**
- Handle is itself jargon ("the AUTH-DTC mechanism", "the CP-4 layer").
- Handle is generic ("the signal", "the option", "the finding").
- No handle declared — spec uses the raw code in narrative slots.
- Handle contradicts the code's canonical definition in source-of-truth artifact (e.g., handle says "demand-side risk" but artifact says SECRET-02 is a supply-side observation).

**`suggested_fix_shape`.** "Replace the handle with a noun phrase a partner would understand on first encounter (e.g., 'the retailer-AI dominance signal' for SECRET-02). Derive from the code's canonical definition in the declared source-of-truth artifact."

---

## D7 — Rumelt kernel coherence

**Pass criterion.** For `structural_framework: rumelt-kernel`, and partial for `structural_framework: adr`: spec contains identifiable Diagnosis / Guiding Policy / Coherent Actions entries with three coherence checks:
- **Diagnosis identifies an obstacle.** Not a goal, not a market description — an obstacle.
- **Policy targets that specific obstacle.** Reading the diagnosis and policy back-to-back, the policy clearly addresses the named obstacle.
- **Actions implement that specific policy.** Each action is a move (verb + concrete object + time bound where possible), not a goal.

Mark N/A for any framework other than `rumelt-kernel` (and the partial check for `adr`).

**Common failure modes.**
- Goals-masquerading-as-strategy: actions like "become the leader", "achieve 20% share".
- Diagnosis describes the market generically, not an obstacle.
- Policy is platitudinal ("execute well", "stay focused").
- Diagnosis says obstacle X but policy targets obstacle Y.
- Bad-strategy hallmarks (Rumelt): fluff, failure to face the challenge, bad objectives.

**`suggested_fix_shape`.** "Rewrite diagnosis to name the specific blocker as an obstacle (not a goal, not a description). Ensure policy explicitly addresses that named blocker. Convert action goals into specific moves with verbs and time bounds (e.g., 'Submit X by Q3' instead of 'achieve Y share')."

---

## D8 — Issue-tree decomposition depth

**Applicable only when `structural_framework: issue-tree`.** Mark N/A for all other frameworks.

**Pass criterion.** The spec defines a root question, decomposes it into 3-5 MECE level-1 sub-questions, and EACH level-1 sub-question further decomposes into ≥2 level-2 sub-questions. The Conn & McLean rule: every branch decomposes 2-4 levels before reaching evidence. A level-1 sub-question that can't decompose is probably either (a) too narrow (it's evidence, not a question) or (b) the branch is mis-cut and should merge with an adjacent branch.

**Common failure modes.**
- Level-1 sub-question listed but no level-2 decomposition under it (depth = 1).
- Level-1 sub-question decomposes into a single level-2 sub-question (D8 fails: must be ≥2).
- Tree is flat — every branch is a leaf, with no MECE decomposition.
- Level-2 sub-questions overlap across different level-1 branches (the tree isn't MECE horizontally).
- Tree is unbalanced — one branch has 4 levels, others have 1 (uneven depth signals mis-cut).

**`suggested_fix_shape`.** "For each level-1 sub-question that doesn't decompose into ≥2 level-2 sub-questions: either merge it with an adjacent branch (if it's actually a sub-claim of another sub-question) or move it down a level (if it's evidence rather than a question). For unbalanced branches, identify the level-2 sub-questions under the deep branches that the shallow branches are silent on — they may belong elsewhere or they may indicate gaps in the shallow branches."

---

## Cross-reference plausibility (high-strictness only, light check)

**Pass criterion.** Each `supporting_artifact` cited in the spec is readable, and the spec's claims about what each artifact contains are plausible on a ~200-line spot check.

**Common failure modes.**
- Cited artifact path doesn't exist.
- Spec claims artifact contains X but spot check shows artifact is about Y.
- Concept code cited in D5-readability has no canonical definition findable in declared source-of-truth artifacts.

This is intentionally light. Full evidence-carries grading happens in Pass 1 against the real document, not against the spec. Spec-stage cross-reference grading is a sanity check, not a full audit.

**`suggested_fix_shape`.** "Update the supporting_artifacts citation to point to the correct artifact path OR add the missing canonical definition to the source-of-truth artifact before writing the document."

---

## Verdict rules

- `PASS` only if zero FAILs across evaluated dimensions AND template conformance passed.
- `FAIL` if ≥1 evaluated dimension fails (template conformed).
- `REJECT` if template conformance failed — calling skill must refill the template, not patch the spec.
- `ESCALATE` if `iteration >= 3` and verdict would otherwise be FAIL — caller should consult a human, not keep iterating.
- `BLOCKED` if required input missing.

## What this rubric does NOT grade

- **Full evidence carries** (Pass 1 D5 against the real document does this).
- **Action titles** (the spec is not yet the document — Pass 2 D1 against the written doc does this).
- **Active voice / jargon** (Pass 2 dimensions).
- **Frankenstein detection** (only sensible against written prose).

The spec-judge stage is upstream of those checks. Its job is to make sure the storyline is sound BEFORE writing — so Pass 1 and Pass 2 against the written doc don't fail on structural problems the spec stage should have caught.

# Pass 1 — Argument Structure Rubric

Dimensions evaluated by `argument-structure-reviewer`. Each test has a one-line restatement, an evaluation procedure, and a pass/fail criterion. The rubric is closed — the reviewer must not invent dimensions.

**Which dimensions fire depends on the declared `structural_framework`.** The reviewer reads `structural_framework` from the orchestrator's input and applies the framework × dimension matrix below. Wrong-framework grading (applying Minto checks to a descriptive document, or skipping the Rumelt kernel check on a strategy document) is the most common cause of over- or under-application. The framework filter is applied FIRST; strictness is applied on top of it.

## Framework × dimension matrix

**M** = mandatory at standard+, **O** = optional / recommended, **N/A** = does not apply, **partial** = limited scope (see per-dimension notes), **H** = high-strictness only.

| Dimension | minto-pyramid | rumelt-kernel | issue-tree | scqa-only | adr | concept-page | descriptive |
|---|---|---|---|---|---|---|---|
| D1 governing observation | M | M (= guiding policy) | O (apex synthesis) | M (= Answer) | M (= Decision) | O | O (= phenomenon thesis) |
| D2 MECE | M | M (on actions; nested under policy) | M (high bar) | N/A | N/A | O | O |
| D3 SCQA opening | M | O | N/A | M | partial | N/A | O |
| D4 dot-dash narrative | M | M | M | O | O | O | M |
| D5 evidence carries | M | M | M (per leaf) | M | M | M | M (highest priority) |
| D6 Frankenstein detection | H | H | H | H | H | H | H |
| D7 Rumelt kernel coherence | N/A | M | N/A | N/A | partial | N/A | N/A |
| D8 issue-tree decomposition depth | N/A | N/A | M | N/A | N/A | N/A | N/A |

## Strictness gating (applied on top of the framework filter)

Strictness governs depth WITHIN the dimensions a framework allows. A dimension fires only if BOTH the framework matrix and the strictness gate include it.

| Strictness | Effective dimensions |
|---|---|
| `low` | D1 + D7 (only where framework includes them — typically minto-pyramid, rumelt-kernel) |
| `standard` | All M and O dimensions for the framework |
| `high` | All M, O, and H dimensions for the framework |

Dimensions excluded by the framework filter are marked `N/A — framework=<X>`. Dimensions excluded by strictness are marked `SKIPPED (strictness=<level>)`. Dimensions actually evaluated produce PASS or FAIL.

---

## D1 — Single Governing Observation (Minto Pyramid)

**Rule:** The document must have ONE top-level claim that all other content supports.

**Test:**
1. Quote what you believe is the governing observation in one sentence.
2. Read each level-2 section. Does each support that single claim?
3. If you cannot identify a single observation in under 30 seconds of reading the top of the document — FAIL.

**FAIL causes:** Two competing thesis statements; a question at the top instead of an answer; a TL;DR that summarises rather than concludes; a list of "key findings" with no integration.

**Source:** Minto Pyramid Principle — the single governing thought.

---

## D2 — MECE Supporting Reasons

**Rule:** Supporting reasons under the governing observation must be Mutually Exclusive and Collectively Exhaustive.

**Test:**
1. List the level-2 claims (section headings or lead sentences).
2. For each pair: do they overlap? If yes — not mutually exclusive — FAIL.
3. Is there a glaring missing reason a senior reader would ask about? — not collectively exhaustive — FAIL.
4. 3–5 supporting reasons is the practical target; >7 means grouping is too granular; <2 means the pyramid collapsed.

**FAIL causes:** Two sections that overlap by 40%+ of content; a recommendation memo with no risk/objections section; a market analysis with no competitive dynamics.

---

## D3 — SCQA Opening

**Rule:** For `doc_type ∈ {brief, memo, decision-record}` at strictness ≥ standard: the document opens with a recognisable Situation / Complication / Question / Answer frame.

**Test:**
1. Situation — 1–2 sentences the reader already agrees with?
2. Complication — 1–2 sentences on what changed or is at risk?
3. Question — explicit statement of what this document answers?
4. Answer — the governing observation upfront?

Missing any element — FAIL. For `wiki` and `daily-note`: N/A.

**Source:** Minto's SCQA framework.

---

## D4 — Dot-Dash Narrative Coherence

**Rule:** Section headings, read alone in order, must tell a coherent story.

**Test:**
1. Extract H1/H2/H3 headings in document order.
2. Read them as a sequence with no body text.
3. Do they build to the conclusion logically?

**FAIL causes:** Noun-label titles ("Market", "Competitors", "Conclusion"); a sequence that doesn't argue toward the governing observation; sections that look like they were assembled from a template.

**Note:** D4 enforces title-level narrative arc. The readability rubric's D1 enforces title-level claim form (action titles). They are complementary.

---

## D5 — Evidence Carries Under Each Reason

**Rule:** Evidence under each supporting reason must actually establish that reason.

**Test:**
1. Pick 2–3 supporting reasons at random.
2. List evidence items under each.
3. Does each item, alone, support the supporting reason? Or is it a topically-related fact that doesn't carry?

**FAIL causes:** Generic citations dropped under reasons they don't establish; numbers that sound impressive but don't speak to the claim above them; quotes used as decoration.

**Load-bearing element interaction:** If `numeric_claims_with_citations` is declared in the manifest and a flagged evidence item is one of these, the reviewer MUST include a preservation_note (at standard+ strictness) — the fix must preserve the citation chain.

---

## D6 — Frankenstein / Section Independence (high-strictness only)

**Rule:** Sections do not depend on each other via "as discussed above" or unresolved pronouns; the document is one coherent argument, not assembled fragments.

**Test:**
1. Pick 2 non-introduction sections at random.
2. Read each standalone.
3. Are there cross-section dependencies that break standalone reading? Do sections feel cut-and-pasted from prior briefs?

**FAIL causes:** Mid-document "as we saw earlier"; pronouns whose antecedent is in a different section; tone/style discontinuities between sections; duplicate framings of the same point.

---

## D7 — Rumelt Strategy Kernel

**Rule:** For `structural_framework: rumelt-kernel` (apex check, mandatory). For `structural_framework: adr` (partial check — the Decision implies a diagnosis). For all other frameworks: N/A. The document contains Rumelt's three kernel elements:

- **Diagnosis** — what is the situation, what is the obstacle?
- **Guiding policy** — the overall approach to overcoming the obstacle.
- **Coherent actions** — specific moves that implement the policy.

**Test:**
1. Find and quote the diagnosis sentence.
2. Find and quote the guiding policy.
3. Find and quote at least one specific action.
4. **Coherence check:** would the guiding policy still make sense if a different diagnosis were swapped in? If yes, the policy is not anchored — FAIL.
5. **Coherence check:** does each action implement the policy? Strike any action that doesn't.

**FAIL causes:** Bad-strategy hallmarks (Rumelt) — fluff, failure to face the challenge, goals-as-strategy, bad objectives. Lists of wishes without diagnosis. Diagnosis without policy. Actions disconnected from policy. Policy without an explicit "we won't" — strategy is choice, and a policy that says yes to everything fails this dimension.

For frameworks other than `rumelt-kernel` and `adr`: N/A — do not grade.

**Source:** Richard Rumelt, *Good Strategy / Bad Strategy*.

---

## D8 — Issue-Tree Decomposition Depth

**Rule:** For `structural_framework: issue-tree` only — every level-1 sub-question under the root must decompose into ≥2 level-2 sub-questions before reaching evidence (Conn & McLean issue-tree depth test). For all other frameworks: N/A.

**Test:**
1. Identify the root question of the document.
2. Identify the level-1 sub-questions (the document's primary section headers, if the framework was followed correctly).
3. For each level-1 sub-question, count how many level-2 sub-questions decompose under it. PASS requires ≥2 per branch.
4. Apply a horizontal MECE check across level-2 sub-questions — they should not overlap across different level-1 branches.
5. Apply a balance check — branches should have roughly comparable depth (no branch is a leaf while another has 4 levels).

**FAIL causes:** Branch is flat (level-1 sub-question with no level-2 decomposition under it). Branch decomposes into a single level-2 sub-question (D8 requires ≥2). Tree is unbalanced — one branch has 4 levels, others have 1. Level-2 sub-questions overlap across different level-1 branches (the tree isn't MECE horizontally).

For frameworks other than `issue-tree`: N/A — do not grade.

**Source:** Charles Conn & Robert McLean, *Bulletproof Problem Solving*; McKinsey 7-step problem-solving / issue-tree discipline.

---

## Cross-rubric: load-bearing element interaction

For any failed dimension, before writing the violation entry, the reviewer checks the `load_bearing_index.yaml` produced by `artifact-loader`:

- If the failing region overlaps a load_bearing element AND `strictness ≥ standard` for cross-reference violations OR `strictness = high` for any load_bearing class — the violation MUST include `preservation_note` and `suggested_fix_shape` fields.
- If `strictness = low` — no preservation notes are produced (the calling skill defers load-bearing edits at this strictness).

See `load-bearing-architecture.md` for the design rationale.

## Fix-ordering hints (optional)

When multiple dimensions fail and the fixes interact, the reviewer MAY emit a `fix_order` hint in the report's `Notes` section naming the recommended sequence and a one-line reason per step. This is a bonus to the calling skill — not contractual, and the calling skill is free to ignore it.

Emit a `fix_order` hint when:

- A D1 fix (adding the governing observation) would partially resolve a D4 failure (headings encode the new claim once it exists). Recommend D1 → D4.
- A D1 fix would partially resolve a D3 SCQA opening (the Answer slot is now filled). Recommend D1 → D3.
- A D7 Diagnosis fix changes the Guiding Policy and Coherent Actions framing. Recommend D7-diagnosis → D7-policy → D7-actions, then re-check D1.
- Two failures share the same edit region — name the dependent dimension last so the calling skill does not double-edit.

Format inside the report's `Notes` section:

```
- fix_order: D1 → D3 → D4
  reason: D1 adds the Answer paragraph; D3 then needs only the Complication insert; D4 promotes the now-stated verdicts into headings.
```

Do not emit a `fix_order` hint when the failing dimensions are independent — the calling skill picks an order. Do not invent ordering rationale; if you can't name a real dependency, omit the hint.

## Verdict rules

- `PASS` only if zero FAILs across evaluated dimensions.
- `FAIL` if ≥1 evaluated dimension fails.
- `BLOCKED` if required input is missing or the document is unparseable.

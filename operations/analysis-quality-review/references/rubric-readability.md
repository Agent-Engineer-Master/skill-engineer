# Pass 2 — Readability Rubric

Dimensions evaluated by `readability-reviewer`. Two-phase evaluation: Phase A (cheap regex/grep checks) gates Phase B (model judgment). If Phase A returns ≥5 violations, return FAIL without running Phase B.

## Strictness gating

| Strictness | Dimensions evaluated |
|---|---|
| `low` | D1 (action titles), D5 (no internal codes) |
| `standard` | D1–D5 (action titles, so-what completion, specificity, code/jargon discipline, active voice) |
| `high` | D1–D7 (adds Frankenstein detection, consultantese drift, one-message discipline) |

---

## Phase A — cheap checks (run first)

### D1 — Action Titles

**Rule:** Section headings are claims (action titles), not noun labels.

**Phase A test:** Grep all H2/H3 headings. Reject any that are bare noun phrases ("Market", "Risks", "Recommendations", "Findings", "Conclusion"). Acceptable: "Market is consolidating around three players"; "The biggest risk is regulatory drift"; "Recommend a 90-day pilot before full commit".

**Doc-type override:** Wiki and daily-note allow noun-label headers. Skip D1 for those.

### D5 — No Internal Codes in Prose

**Rule:** Internal cross-reference codes (`M1-DTC`, `SECRET-02`, `CP-4`, `AUTH-DTC`) appear only in reference tables or footnotes, not in narrative sentences read by the senior reader.

**Phase A test:** Grep document for the `concept_ids` pattern from the manifest (typically `[A-Z][A-Z0-9]*-[A-Z0-9]+`, which matches `M1-DTC`, `SECRET-02`, `AUTH-DTC` — note the first segment may contain digits after the leading letter). For each hit, check whether it appears in a narrative sentence (the line starts with prose) vs a reference table cell (line is part of a markdown table or definition list).

**Load-bearing interaction (always fires):** D5 is the dimension most likely to touch `concept_ids`. EVERY D5 violation MUST include `preservation_note` and `suggested_fix_shape` at `standard` and `high` strictness. The fix shape is canonical:

> Introduce a plain-English handle on first mention (e.g., "the retailer-AI dominance signal (`SECRET-02`)"), then use the handle in subsequent narrative; preserve the code in reference tables and any cross-document index. Search-and-replace as a unit — never local-edit.

### D6 (high only) — Frankenstein Detection

**Phase A test:** Find duplicate or near-duplicate sentences (cosine-shingle proxy via grep for repeated 5-word phrases). Find abrupt voice/tone shifts between paragraphs.

---

## Phase B — model judgment (run only if Phase A returns <5 violations)

### D2 — So-What Completion

**Rule:** Every claim answers "so what?" — the implication for the reader is explicit, not left as homework.

**Test:** Pick 3 claims at random. For each, ask: does the next sentence (or clause) state the implication for a senior reader? If not — FAIL.

**Cause for FAIL:** "Market grew 12% YoY" — so what? "Three of the top 5 competitors raised in Q1" — so what? Claims without implications are observations, not analysis.

### D3 — Specificity over Abstraction

**Rule:** Concrete measurements and named entities over vague qualifiers.

**Test:** Grep for marketing adjectives without adjacent measurements: `significant, meaningful, robust, strategic, leading, premier, world-class, cutting-edge, best-in-class, transformative, scalable`. Each hit without an adjacent number, named entity, or specific time bound — evidence for FAIL.

**Load-bearing interaction:** If a flagged sentence contains a `numeric_claims_with_citations` element, the preservation_note must specify that the number, unit, and citation must remain a unit. Do not let the fix soften the claim while keeping the citation — that breaks the chain.

### D4 — Code and Jargon Discipline

**Rule:** Domain jargon (`MECE`, `Wardley map`, `7-Powers`, `kernel`) is defined on first use OR omitted in favour of plain language, depending on audience (see `intent_summary`).

**Test:** First-use scan for declared framework terms. If the document never introduces the term and the `intent_summary` doesn't position the reader as a domain expert — FAIL.

### D5 — Active Voice and Verb Strength

**Rule:** Active voice dominates; weak verbs (`is`, `has`, `provides`, `enables`, `supports`) are rare in argumentative sentences.

**Test:** Random-sample 5 sentences from argumentative sections. Count passive-voice constructions and weak-verb instances. >2 of 5 — FAIL.

### D6 (high only) — Frankenstein, Phase B

**Test:** Read whole document for tonal continuity. Does any section read like it was lifted from a different document? Are framing devices reused inconsistently?

### D7 (high only) — One-Message Discipline

**Rule:** Each section advances exactly one argumentative beat. Multi-beat sections fail.

**Test:** For each section, can you write its single argumentative beat in one sentence? If you need "and also" — FAIL.

---

## Cross-rubric: load-bearing element protocol

For each violation flagged in either phase:

1. Check the failing region against `load_bearing_index.yaml`.
2. If the region overlaps a load_bearing element class:
   - At `strictness = standard`: only `concept_ids` and `phase_citations` get preservation notes.
   - At `strictness = high`: all four element classes (`concept_ids`, `evidence_tags`, `phase_citations`, `numeric_claims_with_citations`) get preservation notes.
3. The preservation_note must state: (a) what the element references, (b) why it matters, (c) the rule for safely editing.
4. The `suggested_fix_shape` must describe the shape of an acceptable fix — not the exact text. The calling skill chooses the wording using its own context.

---

## Verdict rules

- `PASS` only if zero FAILs across evaluated dimensions in both phases.
- `FAIL` if ≥1 evaluated dimension fails.
- `BLOCKED` if required input is missing.

Phase A ≥5 violations short-circuits to FAIL without running Phase B (the document needs basic cleanup before nuanced judgment is worth the tokens).

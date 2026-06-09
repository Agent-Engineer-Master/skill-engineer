# Pass 2 — Readability Rubric

Dimensions evaluated by `readability-reviewer`. Two-phase evaluation: Phase A (cheap regex/grep checks) gates Phase B (model judgment). If Phase A returns ≥5 violations, return FAIL without running Phase B.

## Strictness gating

| Strictness | Dimensions evaluated |
|---|---|
| `low` | D1 (action titles), D5 (no internal codes) |
| `standard` | D1–D5 + D8 (concept density) + D9 (register fit) — action titles, so-what, specificity, active voice (D4), code/jargon incl. internal codes (D5), concept density, register fit |
| `high` | D1–D9 (adds Frankenstein detection D6, one-message discipline D7, and the D1 narrative-tension extension) |

D8 (concept density) and D9 (register fit) grade prose against `references/tone-of-voice.md` — the positive register target. They fire at `standard` and above. See that file for the worked examples behind both tests.

---

## Phase A — cheap checks (run first)

### D1 — Action Titles

**Rule:** Section headings are claims (action titles), not noun labels.

**Phase A test:** Grep all H2/H3 headings. Reject any that are bare noun phrases ("Market", "Risks", "Recommendations", "Findings", "Conclusion"). Acceptable: "Market is consolidating around three players"; "The biggest risk is regulatory drift"; "Recommend a 90-day pilot before full commit".

**Doc-type override:** Wiki and daily-note allow noun-label headers. Skip D1 for those.

**Narrative-tension extension (high strictness only):** at `high`, a header MAY carry narrative tension to pull the reader forward ("Three firms own the profit pool — and one regulation keeps it that way"). This is permitted, not required. Guardrail: the header must still state a real claim the section proves. Flag as a D1 FAIL only if a header reads as clickbait the body does not deliver (melodrama substituting for a finding). Do not flag a plain action title for *lacking* drama — tension is optional. See `references/tone-of-voice.md`.

### D5 (codes check) — No Internal Codes in Prose

D5 is **Code/Jargon Discipline**: it covers internal-code leakage (this Phase A check, load-bearing) and jargon/consultantese (the Phase B check below). Both report under D5.

**Rule:** Internal cross-reference codes (`M1-DTC`, `SECRET-02`, `CP-4`, `AUTH-DTC`) appear only in reference tables or footnotes, not in narrative sentences read by the senior reader.

**Phase A test:** Grep document for the `concept_ids` pattern from the manifest (typically `[A-Z][A-Z0-9]*-[A-Z0-9]+`, which matches `M1-DTC`, `SECRET-02`, `AUTH-DTC` — note the first segment may contain digits after the leading letter). For each hit, check whether it appears in a narrative sentence (the line starts with prose) vs a reference table cell (line is part of a markdown table or definition list).

**Load-bearing interaction (always fires):** D5 is the dimension most likely to touch `concept_ids`. EVERY D5 violation MUST include `preservation_note` and `suggested_fix_shape` at `standard` and `high` strictness. The fix shape is canonical:

> Introduce a plain-English handle on first mention (e.g., "the retailer-AI dominance signal (`SECRET-02`)"), then use the handle in subsequent narrative; preserve the code in reference tables and any cross-document index. Search-and-replace as a unit — never local-edit.

### D8 (standard+) — Concept Density, Phase A

**Rule:** One claim per sentence. Reasoning is unstacked, not laid bare all at once in the conclusion. Evidence tags sit in footnotes, not mid-sentence.

**Phase A tests:**
1. **Over-long sentences.** Grep argumentative sections for sentences over ~40 words. Each is a *candidate* for the Phase B concept-stacking check (length alone is not an automatic FAIL — a long sentence carrying one idea is fine).
2. **Clause stacking.** Flag any sentence containing ≥3 separately-delimited clauses (em-dash `—`, parenthetical `(...)`, or semicolon segments combined). Three or more stacked clauses in one sentence is strong evidence of concept stacking.
3. **Inline evidence tags.** Grep for evidence tags `\[[CIVA]:` appearing inside a narrative sentence (line begins with prose, tag is mid-line) rather than in a footnote, endnote, or reference table. Each inline tag in body prose is a D8 hit — the fix relocates it to a footnote (load-bearing: relocate as a unit, never strip).

≥1 inline-evidence-tag hit OR ≥1 clause-stacked sentence in argumentative prose → carry to Phase B for confirmation.

### D9 (standard+) — Register Fit, Phase A

**Rule:** Anglo-Saxon backbone; Latinate/jargon only where nuance demands; conversational-educated, not stuffy; acronyms spelled out on first use. Graded against `references/tone-of-voice.md`.

**Phase A tests:**
1. **Stuffy-word grep.** Grep for the default-Latinate list: `utilise|utilize|commence|terminate|endeavour|ascertain|facilitate|aforementioned|heretofore|pursuant|in order to|prior to|subsequent to|in the event that|with regard to`. Each hit is a candidate (some survive Phase B if nuance genuinely demands the formal word — e.g. "terminate a contract").
2. **Acronym-on-first-use.** Grep for all-caps tokens (`\b[A-Z]{2,6}\b`, excluding the load-bearing `concept_ids` from the index). For each distinct acronym, check whether its first occurrence is followed by a parenthetical expansion. First use with no expansion anywhere prior → candidate for FAIL (Phase B confirms it is not a universally-known acronym for this reader).

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

### D4 — Active Voice and Verb Strength

**Rule:** Active voice dominates; weak verbs (`is`, `has`, `provides`, `enables`, `supports`) are rare in argumentative sentences.

**Test:** Random-sample 5 sentences from argumentative sections. Count passive-voice constructions and weak-verb instances. >2 of 5 — FAIL.

### D5 (jargon check) — Code and Jargon Discipline

Second half of D5 (the first half is the Phase A internal-codes check above).

**Rule:** Domain jargon (`MECE`, `Wardley map`, `7-Powers`, `kernel`) and framework labels (SCQA, JTBD) are defined on first use, replaced with plain language, or kept backstage, depending on audience (see `intent_summary` and `tone-of-voice.md` "Frameworks stay backstage"). Acronyms are expanded on first use.

**Test:** First-use scan for declared framework terms and acronyms. If the document surfaces a framework label in a heading or sentence, or never introduces a domain term the reader won't know, and the `intent_summary` doesn't position the reader as a domain expert — FAIL.

### D8 (standard+) — Concept Density, Phase B

**Rule:** Each sentence carries one claim; the document reads at three depths (skim / argument / evidence). See `references/tone-of-voice.md` rules 1, 2, 5.

**Tests:**
1. **Concept-stacking.** For each sentence flagged in Phase A (over-long or clause-stacked), count the distinct analytical concepts it carries — a finding, a ranking, a mechanism, a second mechanism, a quantum, a citation each count. A sentence carrying ≥3 distinct analytical concepts plus evidence is a FAIL. The fix is to split: claim in its own sentence, each mechanism in its own sentence, evidence to footnotes.
2. **Skim-layer survival.** Read only the section action titles and the first sentence of each paragraph. Does that skim layer convey the document's argument coherently? If the first sentence of paragraphs routinely buries the claim behind setup or evidence, the skim layer is broken → FAIL.
3. **Inline evidence confirmed.** Any inline evidence tag in body prose (from Phase A) is confirmed as a D8 FAIL unless it sits in an explicit reference table or footnote.

≥1 confirmed concept-stacked sentence OR a broken skim layer OR ≥1 confirmed inline evidence tag = D8 FAIL.

**Load-bearing interaction:** the evidence-tag relocation touches `evidence_tags` / `phase_citations`. The `preservation_note` must state the tag is relocated to a footnote as a unit, content preserved verbatim, chain intact — never stripped, never locally rewritten.

### D9 (standard+) — Register Fit, Phase B

**Rule:** Conversational-educated register per `references/tone-of-voice.md` — Anglo-Saxon default, Latinate/jargon only where nuance refines the point, not stuffy, acronyms expanded on first use.

**Tests:**
1. **Stuffy-word confirmation.** For each Phase A stuffy-word hit, judge: does the formal word add a distinction the reader needs, or is it decoration? Decoration → FAIL with the plain-word swap. Genuine nuance (e.g. "institutional client," "marginal cost," "terminate a contract") → PASS, no flag.
2. **Acronym-on-first-use confirmation.** Each unexpanded first-use acronym is a FAIL unless it is universal for this reader (judge by `intent_summary` — `CEO`/`GDP` for a general reader, `API` for a technical reader).
3. **Register feel.** Sample 3 paragraphs. Do they read as an intelligent peer explaining something — or as a contract / academic abstract / consumer-app onboarding screen? Either extreme (stuffy OR over-plain) is a FAIL. The target is the midpoint described in `tone-of-voice.md`.

≥1 confirmed decoration-Latinate OR ≥1 unexpanded non-universal acronym OR a register-extreme reading = D9 FAIL.

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

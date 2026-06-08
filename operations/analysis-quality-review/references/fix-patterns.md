# Fix Patterns — Editorial Rules for the Calling Skill

This file is consumed by the upstream skill that called `analysis-quality-review`. The review skill does NOT apply fixes itself — it grades the document and returns a structured violation report plus the path to this file. For each violation dimension below, the calling skill applies the canonical fix pattern using its own context (which includes the supporting artifacts that produced the document and the original intent behind it).

## Input format — HTML or markdown

The reviewed document is typically **HTML** (the reader-facing deliverable produced by `html-output` or similar) at standard+ strictness. Markdown is acceptable at low strictness for working drafts. The fix patterns below describe the editorial change — the calling skill applies the change in whichever format the document uses:

- **Prose-level fixes** (introducing a handle on first mention, converting passive→active, sharpening a so-what, replacing an abstract label with a named specific) → apply directly via `Edit` calls on the HTML or markdown. The fix is the same in either format; only the surrounding syntax differs.
- **Structural fixes** (re-grouping MECE axes, adding an SCQA opening, splitting a section that carries two so-whats) → if the document is HTML and the fix changes the structural skeleton, the calling skill should regenerate the affected sections via the `html-output` skill rather than hand-editing HTML. If the document is markdown, edit directly.
- **Chart/diagram changes** (HTML deliverables embed charts via `html-output`) — when a violation implies the chart needs updating (e.g., the chart's caption claim is wrong, or the chart's data point doesn't match the prose), regenerate the chart via `html-output` rather than editing the embedded SVG/canvas by hand.

The rubric does not change based on format. The reviewer ignores HTML chrome and grades content (argument structure, prose quality, section flow). A violation report on an HTML file describes the prose-level or structural issue; the calling skill chooses the right editing path based on format.

## Why the calling skill is the natural fixer

The calling skill knows what the document is for. It generated the brief, holds the supporting artifacts in working memory, owns the cross-references, and can coherently update both the brief and any source dataset that needs to move with it. A separate fixer agent would have to reinvent that context through a manifest scaffold and would still guess on edge cases. The skill that produced the document is the skill best positioned to repair it.

## How to use this file

For each violation in the report:

1. Read the violation's `dimension`, `evidence`, `preservation_note`, and `suggested_fix_shape`.
2. Find the matching dimension below and apply the canonical fix pattern with targeted `Edit` calls on the document.
3. If the violation touches a load-bearing element and `preservation_note` is present, follow it exactly. If `preservation_note` is missing and the element class is declared in the manifest, treat the fix as DEFERRED (see "Bail rule" below).
4. After applying all safe fixes, re-invoke `analysis-quality-review` with the updated document and the previous report in `previous_violations`. The reviewer will grade whether each fix landed.

## Bail rule (replaces the old halt-rule-escalation)

The calling skill is accountable for preservation. If you cannot safely apply a fix — because the preservation_note is missing, the cross-reference target is unclear, or the named specific is not in your context — do NOT guess. Leave the violation in place and report it as DEFERRED in the next review pass by including it in `previous_violations` with `disposition: deferred` and a short reason. The reviewer will re-grade, and either:

- Re-issue the violation with a richer preservation_note (if higher strictness would help), or
- Mark the violation as ACCEPTED-WITH-KNOWN-DEFER and let you escalate to a human author.

Guessing on a load-bearing token (renaming `SECRET-02` locally, softening a cited number, stripping an evidence tag) is exactly the failure mode this skill exists to prevent.

---

# Framework-keyed dimensions — which fixes apply

The fix patterns below are organized by dimension (D1, D2, D3, D4, D5, D6, D7, D8). NOT every dimension fires for every document — the applicable set depends on the `structural_framework` declared by the caller. See `references/applicability-matrix.md` and `references/framework-selection-guide.md` for the framework × dimension matrix.

Practically: when the calling skill receives a violation report, the report names the dimension that failed. The calling skill looks up that dimension below and applies the canonical fix. The calling skill does NOT apply fixes for dimensions the framework doesn't include — those dimensions return N/A from the reviewer and aren't in the report.

Examples:
- For `structural_framework: rumelt-kernel`, D7 (Rumelt kernel coherence) is the apex check; D3 (SCQA) is optional; D8 (issue-tree) is N/A.
- For `structural_framework: descriptive`, D1/D2/D3/D7/D8 are all O or N/A; D5 (evidence carries) is the dominant fix surface.
- For `structural_framework: issue-tree`, D8 (decomposition depth) is the apex check; D7 is N/A.

The patterns below are written so they apply when the dimension does fire — they don't change shape per framework.

---

# Spec-Stage Fixes (`mode: spec-judge`)

When `spec-judge` returns FAIL on a filled-in authoring spec, the calling skill fixes the spec — not a document. Spec-stage fixes are structurally simpler than document-stage fixes for three reasons:

1. **No code-in-prose violations are possible.** Concepts haven't been named in document prose yet — they only exist as handle definitions inside the spec template (D5 readability). Fixes operate on the handle definitions themselves, not on hundreds of prose mentions.
2. **No cross-reference propagation problems.** The spec is a self-contained scaffold; supporting datasets and working files are not yet edited against it. A spec revision does not cascade.
3. **Spec text is short (typically 2-3K tokens).** Targeted edits are cheap; whole-section rewrites take seconds rather than tens of thousands of tokens.

The fix patterns for D1, D2, D3, D5-handles, D7 (rumelt-kernel only), and D8 (issue-tree only) below all apply at the spec stage too, but operate on shorter spec text. The bail rule still applies — if the calling skill cannot safely supply (for example) a concrete D2 axis because its subject context lacks the structural distinction, mark DEFERRED and let the judge re-issue with a richer suggestion.

**Spec-stage rubric:** see `references/spec-judge-rubric.md` for the dimension-by-dimension grading criteria. The fix patterns below are dimension-shared between spec and document stages; the rubric is dimension-shared in spirit but stage-specific in its tests.

---

# Pass 1 — Argument Structure Fix Patterns

## D1 — Single Governing Observation

**Description:** The document needs ONE top-level claim that all other sections support.

**Canonical fix pattern.** If the document lacks a governing observation: identify the claim the bulk of evidence already supports and write a 1–2 sentence governing observation at the top (after frontmatter, before SCQA or the first section). Derive the claim from existing content — never invent it. If two competing thesis statements exist, promote the dominant one and demote the other to a sub-section.

**Broken:**
```
# Industrial Robotics — NA Brief
The integrator layer is the most attractive part of the value chain.
Software-led entrants will reshape the OEM layer.
```

**Fixed:**
```
# Industrial Robotics — NA Brief
A roll-up of regional integrators captures the migrating profit pool created by
software-led unbundling at the OEM layer.
```

**Cross-reference safety.** If your skill's working artifacts already record a governing observation (e.g., the brief generator wrote `governing_observation:` to frontmatter), use that exact wording. Don't fork the thesis between brief and dataset.

**Common mistakes.** Inventing a thesis to satisfy D1 when none is recoverable. If the document genuinely lacks a thesis, mark D1 DEFERRED and ask the human author.

---

## D2 — MECE Supporting Reasons

**Description:** Level-2 sections must be mutually exclusive and collectively exhaustive.

**Canonical fix pattern.** If reasons overlap, merge them. If a reason is missing, add a section header for it and write one sentence flagging that evidence is needed (do not fabricate evidence). If there are >7 reasons, group into 3–5 higher-level reasons.

**Broken:** sections "Customer demand" + "Demand-side trends" (60% overlap).
**Fixed:** merge into "Demand is consolidating around modular-pricing buyers".

**Cross-reference safety.** When merging sections, check whether either section is the target of a cross-reference elsewhere (in the document or in supporting artifacts). Update the cross-reference to point at the merged section.

**Common mistakes.** Fabricating evidence to fill a missing reason. The fix for missing CE is to flag the gap, not invent material.

---

## D3 — SCQA Opening

**Description:** Briefs, memos, decision-records must open with Situation / Complication / Question / Answer.

**Canonical fix pattern.** Add an SCQA block (or inline equivalents) at the top. Draw Situation from existing context, Complication from stated tension, Question from the implicit research question, Answer from the governing observation. If any element cannot be inferred, leave a clear placeholder and ask the human.

**Cross-reference safety.** The Answer must equal the D1 governing observation verbatim. If you reword one, reword both — they are the same claim.

**Common mistakes.** Treating SCQA as four headers without checking that content actually fills each one.

---

## D4 — Dot-Dash Narrative Coherence

**Description:** Section titles, read alone in order, must tell a coherent story.

**Canonical fix pattern.** Rewrite section titles as complete claims derived from each section's lead paragraph. Read titles-only end to end and verify they argue toward the governing observation. If they don't, reorder sections to follow the argument's natural flow.

**Broken sequence:** `Market` → `Competitors` → `Risks` → `Conclusion`
**Fixed sequence:** `The market is growing at 12% but the OEM profit pool is shrinking` → `Three integrators are positioned to consolidate the fragmented mid-tier` → `The thesis is exposed to regulatory and currency risk` → `Acquire two integrators in 2026 to capture the migration`

**Cross-reference safety.** If reordering moves a section that other documents link into by section name, update the link targets. If section anchors are stable (`#integrator-consolidation`), prefer renaming the title over reordering.

**Common mistakes.** Inventing titles that don't match their section's actual content. Derive each title from the section's existing lead claim.

---

## D5 — Evidence Carries Under Each Reason

**Description:** Evidence under each supporting reason must actually establish that reason.

**Canonical fix pattern.** Move misplaced evidence to a reason it actually supports, or annotate orphan evidence as needing author review. Do NOT fabricate connective tissue.

**Cross-reference safety.** Evidence items tagged with `[V]`/`[C]`/`[A]`/`[I]` or carrying citations are load-bearing. When you move an evidence item, the tag and citation move with it as a unit. Never strip the tag; never soften the claim while keeping the citation.

**Common mistakes.** Writing a connector sentence to "make the evidence carry" when the evidence is simply wrong for the claim. The honest fix is to move or remove.

---

## D6 — Frankenstein / Section Independence (high-strictness only)

**Description:** Sections should not depend on each other via "as discussed above" or unresolved pronouns.

**Canonical fix pattern.** Add explicit transition sentences that tie back to the governing observation. Replace "as discussed above" with the specific claim being referenced. If a section is truly orphaned, surface it for the human author — do not delete autonomously.

**Cross-reference safety.** Resolving a pronoun means finding the actual antecedent — sometimes in a different section, sometimes in a supporting artifact. The replacement noun phrase must be one the reader can resolve without cross-document hunting.

**Common mistakes.** Deleting "orphan" sections that were actually load-bearing in some other context (a prior memo, a stress-test). Check before deleting.

---

## D7 — Rumelt Strategy Kernel

**Description:** Recommendation briefs and memos must contain Diagnosis / Guiding Policy / Coherent Actions.

**Canonical fix pattern.** If diagnosis is missing, extract the document's stated obstacle and write a 1–2 sentence diagnosis. If guiding policy is missing, extract the overall approach into 1–2 sentences. If actions are missing, extract recommended moves into an explicit list. If any element genuinely does not exist in the document, surface to the author — do not invent strategy.

**Cross-reference safety.** The diagnosis and guiding policy must be consistent with the strategy-thesis row in any upstream framework artifact (e.g., a 7-Powers chain, a Wardley map). If you fix the brief's diagnosis, check whether the framework artifact agrees; if not, both move together.

**Common mistakes.** Inventing a diagnosis to satisfy the dimension. Bad strategy with a forced kernel is still bad strategy.

---

# Pass 2 — Readability Fix Patterns

## D1 — Action Titles

**Description:** Section headings must be complete-sentence claims, not noun labels.

**Canonical fix pattern.** Replace each noun-label heading with a complete-sentence conclusion derived from the section's content. Rules:

- ≤15 words. If it doesn't fit, the section probably carries two messages — surface as a D7 issue.
- Contains a verb.
- No "and" joining two distinct claims (the "and" test).
- No em-dashes for clause fusion.

**Broken:** `## Market Overview`
**Fixed:** `## The market is consolidating around three integrators`

**Broken:** `## Findings and Implications` (fails the "and" test)
**Fixed:** split into two sections, one per finding, one per implication.

**Cross-reference safety.** If other documents link to a section by its anchor slug, prefer renaming via title-text-change (anchor follows) consistently across both docs, or maintain a stable anchor manually.

**Common mistakes.** Inventing a claim to populate the title. Derive from the section's existing lead claim.

---

## D2 — So-What Completion

**Description:** Every claim must answer "so what?" for the reader.

**Canonical fix pattern.** For each flagged claim, append a 1-sentence implication: "state finding, ...which means [actionable implication]." Derive the implication from the document's existing recommendations or conclusions. If none is recoverable, mark DEFERRED for the author.

**Broken:** "Three of the top 5 incumbents raised capital in Q1 2026."
**Fixed:** "Three of the top 5 incumbents raised capital in Q1 2026 — meaning the integrator-layer roll-up must move before incumbent capital re-shapes the M&A market."

**Cross-reference safety.** The implication you append must be consistent with the document's own recommendations section and with any upstream strategy artifact. Don't append a so-what that contradicts the brief's own conclusion.

**Common mistakes.** Inventing implications. If the document doesn't state what the reader should do differently, neither should the fix.

---

## D3 — Specificity over Abstraction

**Description:** Concrete measurements and named entities replace vague qualifiers.

**Canonical fix pattern.** Replace abstractions with named specifics, but only when the named specific is available in your working context:

- "stakeholders" → "the procurement team and the CFO"
- "various players" → "Fanuc, ABB, and KUKA"
- "the customer" → named persona or segment
- "key segments" → the named segments

If a flagged sentence contains a `numeric_claims_with_citations` element, the number, unit, and citation are a unit — edit all three together or none.

**Common mistakes.** Replacing an abstraction with a guessed specific. If you don't know who "the stakeholders" are, surface to the author.

---

## D4 — Active Voice and Verb Strength

**Description:** Active voice dominates argumentative sentences; weak verbs (`is`, `has`, `provides`) are rare.

**Canonical fix pattern.** Convert passive to active in recommendations and findings:

- "It is recommended that..." → "We recommend..."
- "It was found that..." → "The data shows..." or "We found..."
- "It has been observed..." → "Our research observed..."

Body narration that legitimately uses passive (describing a measurement process) is acceptable — only fix what was flagged.

**Common mistakes.** Forcing active voice on descriptive prose where passive is natural. Only fix flagged occurrences.

---

## D5 — Code and Jargon Discipline (incl. no internal codes — LOAD-BEARING)

D5 covers two related fixes the reviewer reports under one number: jargon/consultantese (swap for plain language) and internal cross-reference codes leaking into prose (the load-bearing case).

### D5a — Jargon / consultantese

**Description:** Domain jargon is defined on first use or replaced with plain language.

**Canonical fix pattern.** Replace consultantese with concrete language:

- "leverage" (verb) → "use", "apply", "draw on"
- "ecosystem" → name the actual actors
- "stakeholders" → name the actual groups
- "at the end of the day" → delete; the sentence stands without it
- "provide color" → "explain", "detail"
- "key X" → drop "key" or replace with a specific modifier
- "buckets" / "silos" → "categories", "groups"
- "using 7 Powers, we find Y" → "Y is a [specific power], because [mechanism]"
- Framework labels (SCQA, JTBD, MECE, 7-Powers / Helmer) in headings or prose → replace with the insight, often in the reader's own words. See `tone-of-voice.md` "Frameworks stay backstage".

For domain jargon (`MECE`, `Wardley map`, `kernel`) used in audience-appropriate contexts: define on first use OR omit, based on `intent_summary`. Acronyms: expand on first use with the acronym in parentheses, then use the acronym freely.

**Common mistakes.** Flattening voice while removing jargon. The fix removes consultantese, not personality.

### D5b — No internal codes in reader-facing prose (LOAD-BEARING)

**Description:** Internal cross-reference codes (`M1-DTC`, `SECRET-02`, `CP-4`, `AUTH-DTC`) belong in reference tables, not in narrative sentences.

**Canonical fix pattern.** Introduce a plain-English handle on first mention while preserving the code in parentheses. Use the handle in subsequent narrative. Preserve the code verbatim in reference tables and cross-document indexes. Search-and-replace as a unit — NEVER local-edit one occurrence.

**Broken:**
> SECRET-02 shows retailers will gain dominance because CP-4 creates switching costs.

**Fixed:**
> The retailer-AI dominance signal (`SECRET-02`) shows retailers will consolidate market power, because the switching-cost layer (`CP-4`) makes vendor-side moves expensive.

Subsequent paragraphs use only "retailer-AI dominance signal" and "switching-cost layer"; codes survive in the reference table at the document footer.

**Cross-reference safety (the load-bearing case).** This is the dimension most likely to break supporting artifacts. Rules:

- Never rename a code locally. If `SECRET-02` appears at lines 12, 47, 89, the rename moves all three together — or none.
- Never strip a code. Codes are pointers to upstream datasets; stripping breaks the chain.
- The descriptive handle you introduce must match the code's canonical definition in the source-of-truth artifact (e.g., `disruption-dataset.yaml#framework_signals[6]`). If your skill doesn't know the canonical definition, mark DEFERRED.
- If the code label genuinely needs to change (e.g., the team renamed it), update the code in BOTH the brief AND every supporting artifact in the same edit pass. Use `Edit replace_all: true` or sequential edits across files.

**Common mistakes.**
- Inferring "reasonable intent" for an unknown code. This is exactly the failure mode the bail rule prevents.
- Renaming locally and breaking the cross-reference chain.
- Stripping `[V]` / `[C]` / `[A]` / `[I]` evidence tags adjacent to load-bearing codes during the cleanup.

---

## D6 — Frankenstein / Consultantese Drift (high-strictness only)

**Description:** The document reads as authored, not assembled — no copy-pasted phrasing, abrupt voice shifts, or slide-deck-flattened-into-paragraphs density.

**Canonical fix pattern.** This is a structural-readability fix the calling skill applies because it owns the broader narrative: rewrite transitions between the stitched sections so each follows from the last; collapse duplicate framings of the same point; convert "and also" triadic lists into a progression. Do not flatten the author's register while smoothing — see general rule 2.

**Common mistakes.** Treating Frankenstein as a sentence-level fix. It is a section-flow fix; smoothing one paragraph rarely resolves it.

---

## D7 — One-Message Discipline (high-strictness only)

**Description:** Each section advances exactly one argumentative beat.

**Canonical fix pattern.** When a section carries two distinct so-whats, split it into two sections. This is a structural change — the calling skill applies it because it knows the broader argument structure. Update the dot-dash narrative (Pass 1 D4) after splitting and verify titles still tell the story.

**Broken:** `## The market is consolidating and the regulatory environment is tightening`
**Fixed:** `## The market is consolidating around three integrators` + `## Regulatory tightening could erode integrator margins by 200-300bps`

**Cross-reference safety.** Splitting a section creates a new anchor. Update any cross-references that pointed at the old anchor.

**Common mistakes.** Leaving the original section heading and just splitting body prose — the heading still claims two beats. Rewrite the heading.

---

## D8 — Concept Density (standard+)

**Description:** One claim per sentence; evidence in footnotes; the document reads at three depths (skim / argument / evidence). The positive target is `references/tone-of-voice.md` rules 1, 2, 5 — read it before applying.

**Canonical fix pattern — unstack the sentence.** When a sentence stacks a finding, its mechanisms, and its evidence, split it:
1. Lead with the claim in its own short sentence.
2. Give each supporting mechanism its own sentence.
3. Relocate every inline evidence tag (`[C: ...]`, `[I: ...]`, `[V: ...]`, `[A: ...]`) to a numbered footnote — content verbatim, never stripped.

**Broken (one sentence, ~5 concepts + 2 tags):**
> Commercial valuation firms (Savills, CBRE, JLL, Knight Frank) capture approximately £79M EBIT at 13–17% margins [C: Savills Annual Report 2024] — the largest single profit pool — protected by switching costs (institutional clients face 6–18 months of onboarding friction [I: estimated from framework agreements]) and a regulatory cornered resource (RICS Red Book + MRICS credential, legally required for lender-accepted valuations).

**Fixed (claim leads, mechanisms separated, evidence footnoted):**
> **Commercial valuation is the market's largest profit pool.** Four firms — Savills, CBRE, JLL and Knight Frank — earn about £79M EBIT on it, at margins of 13–17%.¹
>
> Two things protect that pool. Switching is slow: an institutional client needs six to eighteen months to onboard a new valuer.² And regulation gates the work — only an MRICS-credentialled valuer using the RICS Red Book can sign a valuation a lender will accept.³

**Load-bearing safety (the critical case).** The evidence-tag relocation touches `evidence_tags` / `phase_citations`. Relocate as a unit: the tag's full content moves to the footnote body unchanged. Never strip a tag, never split its content, never local-rewrite. If you cannot place the footnote without breaking the chain, mark DEFERRED.

**Common mistakes.** Shortening the sentence by *deleting* a mechanism or a citation rather than relocating it — that loses analysis or breaks the evidence chain. The fix redistributes; it does not cut content.

---

## D9 — Register Fit (standard+)

**Description:** Anglo-Saxon backbone; Latinate/jargon only where nuance refines the point; conversational-educated, not stuffy; acronyms expanded on first use. Positive target: `references/tone-of-voice.md` rule 4 and its word-swap table.

**Canonical fix pattern.** Swap the default-Latinate word for the plain one — UNLESS the formal word carries a distinction the reader needs:

- "utilise / leverage (verb)" → "use", "draw on" (always)
- "in order to" → "to"; "prior to" → "before"; "subsequent to" → "after"
- "a number of" → "several" or the actual count; "the majority of" → "most"
- "facilitate" → "help", "ease"; "ascertain" → "find out", "check"

**Keep the formal word when nuance demands it.** Do NOT flatten "institutional client" → "big client", "marginal cost" → "extra cost", or "terminate a contract" → "end a contract". The longer word is carrying a real distinction. The test: does the word add a distinction the reader needs, or is it decoration?

**Acronyms.** On first use, expand with the acronym in parentheses: "Royal Institution of Chartered Surveyors (RICS)". Afterwards use the acronym. Skip expansion only for acronyms universal to this reader (judge by `intent_summary`).

**Common mistakes.** Over-correcting toward consumer-app plainness — stripping every technical term until the prose loses the nuance a sophisticated reader came for. This register is the *midpoint*, not Monzo. Flattening voice while swapping words: the swap removes stuffiness, not the author's register.

---

# General editorial rules for the calling skill

1. **Apply the smallest edit that satisfies the dimension.** Prefer `Edit` with narrow `old_string` over rewriting paragraphs.
2. **Preserve voice and evidence.** Restructuring is moving and re-labelling; voice cleanup is sentence-level. Never flatten the author's register.
3. **Touch only flagged regions.** "While I'm here" cleanups break the diff and risk regressions.
4. **Don't invent.** Theses, implications, named specifics, descriptive handles, diagnosis sentences — derive from existing content or defer.
5. **Cross-references move together.** If a load-bearing token changes in the brief, it changes in every artifact that references it, in the same edit pass.
6. **Defer rather than guess.** Missing preservation_note + load-bearing element = DEFERRED, not an inferred fix.
7. **Update artifacts when prose-level fixes have knock-on effects.** The calling skill owns the upstream dataset and can do this; the review skill cannot.
8. **Re-invoke the review skill after applying fixes.** Pass `previous_violations` so the reviewer can grade whether each fix landed.

---
name: reimagine-industry
description: "Produces a ranked shortlist of venture concepts for disrupting an industry via a 6-phase workflow (Industry Deconstruction → Value Chain Pain Audit → Enabling Conditions Scan → Framework Application → Idea Generation via Seven Structural Moves → Stress Test). Applies Blue Ocean ERRC, Aggregation Theory, Decoupling, Counter-positioning, 7 Powers, and Thiel's Secret against a disruption-dataset.yaml built from inherited analyze-industry outputs or fresh librarian research. Three approval gates. Reimagination-specific bar test (≥3 non-obvious concepts, zero AI-washed). V/C/A/I provenance. Triggers on 'reimagine the [industry]', 'find disruption angles in [industry]', 'venture concepts for [industry]', 'how would we disrupt [industry]', 'blue ocean for [industry]'. Do NOT activate for single-company analysis (use build-company-model), structural industry diagnosis (use analyze-industry), DTC category go/no-go (use assess-category), or decision pressure-testing (use stress-test)."
---

# Reimagine Industry

For a single industry, generate a ranked shortlist of venture concepts for disrupting it. Most commonly runs AFTER `analyze-industry` has produced a structural brief, inheriting its outputs from `08-knowledge/world-model/industries/[slug]/working/`. Works standalone if given enough raw data — Phase 2/3 dispatch the librarian for missing inputs.

Three-layer output: ranked venture concepts (`venture-concepts.md`), narrative synthesis (`reimagination-brief.md`), and the structured dataset that powers both (`disruption-dataset.yaml`). Three approval gates. Reimagination-specific bar test from fresh-context sub-agent.

**The bar (per `references/bar-test-criteria.md`):** a senior strategist reading the shortlist should find ≥3 non-obvious concepts, zero AI-washed concepts, zero feature-not-company concepts, and every concept's why-now must survive a partner-meeting test.

**Iron rules:**
- Every external fact-claim carries a V/C/A/I tag — see `../_shared/provenance-tagging.md`.
- Each concept cites specific Phase 1-3 dataset entries AND ≥1 Phase 4 signal — no free-association.
- Each concept ships with all four stress test answers (why-now, idea-maze, incumbent response, moat) — no partial concepts.
- The Seven Structural Moves are templates, not prompts — one concept per move, then filter.
- Synthesis structured Pyramid + SCQA — see `../_shared/pyramid-scqa.md`.
- 2026 terminology only — see `../_shared/2026-terminology.md`.
- Human-facing prose follows `references/voice-constraints.md` — no consultantese in `venture-concepts.md` or `reimagination-brief.md`. The dataset YAML is exempt.
- **All human gate reviews render via the html-output skill** with diagrams + plain-English concept explainers — see `references/gate-html-output.md`. Markdown gate reviews are forbidden.
- **Every concept, framework signal, and endorsed Thiel Secret carries a memorable 3-5 word handle** alongside its structured ID — see `references/edge-cases.md` RULE-1.
- **Thiel Secrets are scenario lenses, not conviction filters**, unless the user explicitly signals high conviction — see `references/edge-cases.md` RULE-2.
- **Y1 metrics must be bottoms-up**, not goal-seeked to clear an industry projection — see `references/edge-cases.md` RULE-3.
- Shortlist never ships without bar test pass — see `references/bar-test-criteria.md`.

## Process

### 1. Intake
Ask: industry slug, scope question ("how would we disrupt [X]?" / "venture concepts for [X]?"), whether `analyze-industry` outputs exist at `08-knowledge/world-model/industries/[slug]/`, and what primary data the user has (interviews, operational experience, surveys). Run `python scripts/init_reimagination.py --slug <industry-slug> --question "<scope-question>"` to create or extend the industry folder.

### 2. Gate 1 — Scope + data sources (STOP)
Read `references/gate-prompts.md` Gate 1 template AND `references/gate-html-output.md`. Render the gate review via the html-output skill (archetype: `report.html`) to `08-knowledge/world-model/industries/<slug>/gates/gate-1-<date>.html`. Present in chat: link to the HTML + the four-line decision prompt (Why we're asking / Default / Tradeoff / Or). User confirms scope + data plan. `python scripts/log_run.py --slug <slug> --event gate-1-approved`.

### 3. Phase 1 — Industry Deconstruction
Read `references/dataset-schema.md` section "value_chain + market_structure". Populate the `industry`, `value_chain`, and `market_structure` blocks of `disruption-dataset.yaml` from `working/value-chain-profit-pools.md` if present, else from inherited `industry-brief.yaml` if present, else dispatch the librarian for a structural scan. Every numeric claim gets a V/C/A/I tag. Output: `disruption-dataset.yaml` populated through `market_structure`. Render the populated structure as an HTML diagram review (`diagram-mermaid.html` embedded in `report.html`) via html-output — value chain as Mermaid flowchart with margin pools shaded, customer-relationship-owner highlighted. See `references/gate-html-output.md` for the diagram spec.

### 4. Phase 2 — Value Chain Pain Audit
Read `references/dataset-schema.md` section "value_chain_pain". For each entity type in the value chain (customers, suppliers, intermediaries, adjacent players, non-consumers), build a structured pain inventory.

**Data path:** if `working/demand.md` exists, seed from it. If the user lacks primary data, dispatch the librarian via `python scripts/dispatch_pain_research.py --slug <slug>` — this generates a structured brief covering all value chain entities (not just customers) and writes it to `working/value-chain-pain-audit.md`.

For each entity:
- **Segments** — define behavioral or situational segments (not demographic)
- **Jobs to be done** — functional, emotional, social per segment, with importance and satisfaction scores (Ulwick ODI)
- **Pain points** — score intensity × frequency along the journey; every top pain has a named workaround OR is flagged as hypothetical
- **Non-consumption map** — at least one excluded group per segment across exclusion types (cost, complexity, access, formality)

Run `python scripts/validate_dataset.py --slug <slug> --phase 2` before proceeding. Hard-fails: flat job map, all-7s pain syndrome, untagged claims, missing non-consumption.

### 5. Phase 3 — Enabling Conditions Scan
Read `references/dataset-schema.md` section "enabling_conditions". Walk five axes: technology unlocks, cost curves, behavioral shifts, regulatory changes, supply-side availability. For each, populate 2-4 specific dated conditions.

**Data path:** if `working/trajectory.md` exists, inherit S-curve inflections and discontinuities. Else dispatch the librarian via `python scripts/dispatch_pain_research.py --slug <slug> --mode enabling-conditions` to do a 5-axis scan.

After population, run intersection analysis: identify 2-3-way intersections of conditions that create a window that didn't exist before (this is the load-bearing why-now for Phase 6). Classify each intersection by window timing (wide-open / open with competition / closing / closed) and Benedict Evans access-vs-use phase.

Run `python scripts/validate_dataset.py --slug <slug> --phase 3` before proceeding. Hard-fails: single-axis why-now, untagged dates, missing intersection thesis, missing window timing.

### 6. Phase 4 — Framework Application
Read `references/frameworks-cheatsheet.md`. Run six frameworks in parallel against the populated dataset:

- **Blue Ocean ERRC** — applied to industry competitive factors, not abstractly. Output: 3-5 Create candidates + 2-3 Eliminate candidates.
- **Aggregation Theory fit test** — three diagnostic conditions + Thompson 2024 AI margin-cost overlay. Output: 2-4 aggregation candidates OR explicit non-fit rationale.
- **Decoupling candidates** — take Phase 2 top pains; apply Teixeira 3-test. Output: 3-5 decoupling candidates citing specific pains.
- **Counter-positioning analysis** — per major incumbent, walk Helmer trap analysis. Output: 2-4 counter-position candidates with named structural traps.
- **7 Powers early-stage mapping** — runs AFTER frameworks 1-4 complete; tags each signal with entry power + projected scale power.
- **Thiel's Secret as scenario lens** — AI generates 5-10 contrarian hypothesis candidates, each with a **memorable 3-5 word handle** + plain-English distillation. Frame the human prompt explicitly per `references/edge-cases.md` RULE-2: "Which of these contrarian positions do you want to use as STRATEGIC LENSES that suggest experiments to run?" Endorsing a Secret as a lens does NOT filter out concepts that bet against it — Phase 5 generates concepts spanning the hypothesis space. Only if the user explicitly signals high conviction ("I'd bet the company on this") does the original Thiel filter discipline apply. Output: 1-3 endorsed Secrets with handle + distillation + falsifiability + endorsement-type (lens / conviction).

Every framework signal gets a memorable handle alongside its structured ID. All signals land in `framework-signals.yaml`. Run `python scripts/validate_dataset.py --slug <slug> --phase 4` — hard-fails: skipped frameworks without N/A rationale, untagged signals, AI-washed Aggregation, counter-positioning that incumbents could copy, 7 Powers labels without mechanism, Thiel Secrets without endorsement-type recorded.

### 7. Gate 2 — Dataset + framework signals (STOP)
Read `references/gate-prompts.md` Gate 2 template AND `references/gate-html-output.md`. Render via html-output skill (archetype: `slide-deck.html` — McKinsey consulting-deck style). Required elements: value chain diagram repeated for orientation, per-framework signal cards each with **memorable handle + plain-English explainer + structured ID**, counter-positioning trap diagrams per incumbent, 7 Powers trajectory diagram per signal, pain heatmap, JTBD opportunity scatter, why-now timeline with intersection Venn. Plain-English explainers for every framework named (Aggregation Theory, Counter-positioning, etc.) per `gate-html-output.md` glossary. Save to `gates/gate-2-<date>.html`. Surface link + four-line decision prompt in chat. Flag any signal resting on `[A]/[I]`-tagged claims as load-bearing risk for Phase 6. `python scripts/log_run.py --slug <slug> --event gate-2-approved`.

### 8. Phase 5 — Idea Generation via Seven Structural Moves

**8a. Authoring spec (ghost-deck discipline) — BEFORE drafting concepts.** Invoke `analysis-quality-review` in `mode: spec` to retrieve the authoring template for the document you're about to produce. Pick `structural_framework: minto-pyramid` (recommendation-driven brief — default). Fill in the template using subject context from the populated dataset: governing observation, MECE supporting axes (the structural moves you'll generate against), SCQA opening, evidence inventory per axis, plain-English handles for all concept_ids and framework signals. Write the filled-in spec to `working/authoring-spec.md`.

Then invoke `analysis-quality-review` in `mode: spec-judge` with the filled-in spec + supporting_artifacts manifest pointing at `disruption-dataset.yaml` and the `working/` folder + `intent_summary` describing the reader and the decision the brief informs. If the judge returns FAIL, revise the spec (you have the subject context — apply the suggested_fix_shape per `fix-patterns.md`) and re-invoke. Loop until PASS or `max_spec_iterations: 3` ESCALATE. Most structural failures (broken governing observation, MECE-overlap, weak evidence inventory) are caught at this stage and save 60-70% of the iteration cost of post-hoc structure fixes.

**8b. Generate concepts.** Read `references/seven-structural-moves.md` AND `references/voice-constraints.md` before drafting concepts. Generate one venture concept per move applied to `framework-signals.yaml` — in parallel across all seven moves. A move that cannot be executed against this industry returns `"not viable because [specific reason citing dataset]"` — that's a valid output, do NOT force.

**Each concept MUST carry a memorable 3-5 word handle** (e.g., "Wirecutter-for-niche, AI-citation-first") that captures the core idea, alongside its `concept_id` (e.g., M4-OWN-EVALUATE). The handle is what surfaces in HTML gate reviews; the ID is for the dataset. Per `references/edge-cases.md` RULE-1.

**Concepts that depend on endorsed Thiel Secrets** record the dependency as `endorsed_secrets_dependency: {depends-on | survives-falsification | counter-bet}` per Secret. Per RULE-2, `depends-on` means "this is the concept that wins if Secret is true" — NOT "Secret must be true for the concept to be considered." Phase 5 composes a portfolio that spans the Secret hypothesis space.

Run automated diversity check: concepts must differ across ≥2 segments, ≥2 entity types, ≥2 revenue models, ≥2 incumbents. If diversity is thin, re-run underweighted moves with structural-difference constraint.

**Filter to 3-5 concepts** (human-led) using three questions: conviction (do I believe this?), strategic fit (does this fit our context?), non-obviousness (would a senior strategist recognize this as fresh?). The human owns this filter; the AI cannot supply conviction. Render the move-fit pre-screen and filter options via html-output (`comparison-table.html`) for the human review.

Enrich each kept concept with market-size hypothesis, wedge product, and year-1 success metric. **Y1 metric must be bottoms-up per RULE-3** — if it implies outperforming a Phase 3 industry projection, include explicit bottoms-up justification (conversion deltas, competing-merchant counts, precedent operator timelines). Run `python scripts/validate_dataset.py --slug <slug> --phase 5` — hard-fails: free-associated concepts, AI-washing in one-liners, missing memorable handle, missing enrichment fields, goal-seeked Y1 metrics, fewer than 3 or more than 5 kept concepts.

### 9. Phase 6 — Stress Test
Read `references/stress-test-prompts.md`. Run four stress tests per kept concept:

1. **Why-now sharpness** — single paragraph with dated specificity, falsifiability, window honesty
2. **Idea Maze** — librarian-dispatched per concept; identify prior attempts + failure cluster + what's different now. Verdict: PASS / ITERATE / KILL.
3. **Incumbent war-game** — Y1/Y2/Y3 response per major incumbent, constraint-grounded by Phase 4.4 counter-pos analysis
4. **Moat durability** — entry power → wedge-to-platform → scale moat trajectory; counter-positioning must name expiry plan

Aggregate verdict per concept (SHIP / PROCEED / RECONSIDER / KILL). Concepts that die get appended to `signals-log.md` with rejection rationale — append-only.

Run reimagination-specific bar test via `python scripts/bar_test.py --slug <slug> --concepts-path 08-knowledge/world-model/industries/<slug>/venture-concepts.md`. The script writes the prompt for a fresh-context sub-agent; the orchestrator spawns the sub-agent and captures its JSON verdict. If bar test returns ITERATE, loop back to the specific Phase that failed — no "log and defer" path.

**Working markdown drafts.** Stress-test outputs, per-concept analyses, and prose drafts live in `working/` as markdown. These are scaffolding artifacts — not reader-facing — and do NOT go through `analysis-quality-review`. They exist for audit trail and for the next step to consume as input. Files in this phase: `working/venture-concepts-draft.md`, `working/reimagination-brief-draft.md`, per-concept stress-test reports, etc.

### 10. Phase 7 — Render the final HTML deliverable

The reader-facing deliverable is a single combined HTML report — prose argument with charts and diagrams integrated inline at the points where they support the argument. This is the canonical output the founder-COO reads; the markdown drafts in `working/` are the audit substrate.

Read `references/gate-html-output.md` for the consulting-deck visual conventions. Invoke the html-output skill to render `<slug>-reimagination-report.html` at the industry root (`08-knowledge/world-model/industries/<slug>/<slug>-reimagination-report.html`). Combine into a single HTML report:

- **Cover** — title, scope question, generation date, verdict summary
- **SCQA opening** — Situation / Complication / Question / Answer
- **Governing observation** — single-sentence apex claim
- **Three supporting observations** — each a section, each anchored by a chart or diagram that supports the argument (value chain Mermaid diagram under the citation/attribution/vertical-spine framing; framework signal landscape under the disruption-thesis section; why-now intersection Venn under the enabling-conditions section)
- **Ranked shortlist** — concept cards with **memorable handles as card titles** + verdict badges + non-obvious-reason + top-risk + required-iteration. Comparison table renders the 5 concepts across the 4 stress-test dimensions, color-coded.
- **Idea-maze timelines** for top concepts (Mermaid timeline diagrams)
- **Incumbent war-game timelines** for top concepts (Mermaid timeline diagrams)
- **Coverage gaps + rejected concepts** — kill list with rationale
- **Sequencing recommendation** — what to ship first, second, gated, partner-dependent
- **Methodology footer** — link to dataset, signals-log, audit dir, bar-test verdict

Plain-English explainers for every framework name (Aggregation Theory, Counter-positioning, etc.) per `gate-html-output.md` glossary. Charts must support arguments, not decorate — every diagram earns its place by illustrating a specific load-bearing point in the prose.

### 11. Mandatory quality review on the HTML deliverable

Now invoke `analysis-quality-review` against the HTML report — the reader-facing artifact. The markdown drafts in `working/` are NOT reviewed; only the HTML is.

1. `mode: review, pass: 1, structural_framework: minto-pyramid, strictness: standard` on `<slug>-reimagination-report.html`. Supply the manifest (supporting_artifacts pointing at `disruption-dataset.yaml` + `working/`; `load_bearing_elements` declaring concept_ids `[A-Z]+-[A-Z0-9]+`, evidence_tags `\[(V|C|A|I): [^\]]+\]`, phase_citations `Phase [0-9]+(\.[0-9]+)?`; `intent_summary` describing the reader and decision). If FAIL, read the violation report + fix-patterns.md, apply targeted Edit calls to the HTML directly (prose-level fixes) OR regenerate sections via html-output (structural fixes that need the renderer). Re-invoke with same `audit_dir` and `previous_violations`. Loop until PASS.
2. `mode: review, pass: 2` against the same HTML and same audit_dir (Pass 2 is gated on Pass 1 PASS). Same apply-fixes-yourself loop. Expected pattern: code-in-prose violations on D5 readability — apply the canonical handle-on-first-mention fix per fix-patterns.md.

**Optional humanizer pass:** AFTER analysis-quality-review clears both passes, optionally run the humanizer skill on the HTML's prose sections to strip residual AI tells. Skip for `disruption-dataset.yaml` (machine-readable) and `working/` drafts (not reader-facing). Recommended when the drafting model is Opus or when the user has flagged prose drift in prior runs.

### 12. Gate 3 — Ranked shortlist (STOP)
The HTML report IS the Gate 3 review artifact. No separate render needed. Save a copy of the cleared HTML to `gates/gate-3-<date>.html` for audit trail. Surface link to the canonical `<slug>-reimagination-report.html` + four-line decision prompt (Why we're asking / Default / Tradeoff / Or) in chat. User reviews the HTML report and approves / iterates / rejects. If iterate: caller applies fixes to the HTML and re-runs quality review; if approve: log gate-3-approved. `python scripts/log_run.py --slug <slug> --event gate-3-approved`.

### 13. Closing feedback gate
Ask the four-routing question: any feedback for **learnings** (behavioral preferences) / **edge-cases** (industry-specific exceptions) / **rules** (never again) / **approved-examples** (save as reference output)? Save outputs accordingly.

## Update mode
If invoked with `--update <industry-slug>`, skip Phases 1-3 (inherit existing dataset) and re-run Phases 4-6. Use when enabling conditions have shifted or new framework signals warrant re-ideation.

## Integrates with
- **`analyze-industry`** — natural upstream. Reimagination consumes its working/ outputs and brief.yaml; the reimagination brief is the creative "so what" layer that follows the structural diagnosis.
- **`stress-test`** — natural downstream. The top-ranked concept feeds into a three-phase stress-test pressure round.
- **`assess-category`** — adjacent. Reimagination produces concepts; assess-category produces GO/NO-GO on a specific category bet. Do not call each other.
- **`analysis-quality-review`** — quality gate on reader-facing artifacts. Called twice in the pipeline: (1) `mode: spec` + `mode: spec-judge` at Phase 5 start as ghost-deck discipline before drafting (the spec is a private scaffold — markdown — not reader-facing); (2) `mode: review pass: 1` and `pass: 2` at Phase 7 against the HTML deliverable (`<slug>-reimagination-report.html`). Markdown drafts in `working/` are NOT reviewed — they're audit substrate. Use `structural_framework: minto-pyramid`. See `.claude/skills/analysis-quality-review/references/calling-contract.md` for the manifest schema.
- **`html-output`** — renders the canonical reader-facing deliverable at Phase 7 and the intermediate gate reviews (Gate 1, Gate 2). The HTML report IS the deliverable; markdown lives in `working/` for audit only.

## Gotchas

- **Symptom:** every concept is "an AI agent for [industry]". **Cause:** Phase 3 was AI-heavy and Phase 5 diversity check didn't enforce structural difference. **Fix:** diversity check requires ≥2 distinct revenue models and ≥2 distinct entity types across concepts; re-run underweighted moves with structural-difference constraint.
- **Symptom:** concepts read compellingly but die under stress test. **Cause:** Phase 5 conviction filter was permissive; non-obviousness wasn't enforced. **Fix:** human filter must strip to 3-5 concepts before Phase 6; if 6+ survive the filter, Phase 6 depth suffers and bar test fails.
- **Symptom:** idea-maze test passes with only 1-2 prior attempts found. **Cause:** librarian research was shallow OR concept is in a novel category. **Fix:** require ≥3 prior attempts surfaced OR explicit "novel category" justification with evidence; lazy idea-maze is the most common stress-test failure mode.
- **Symptom:** incumbent war-game assumes incumbent passivity ("Amazon won't notice for 3 years"). **Cause:** Phase 4.4 counter-pos analysis didn't supply a structural trap; war-game requires incumbent passivity instead of being grounded in trap. **Fix:** every Y1/Y2/Y3 response must cite the Phase 4.4 structural constraint that delays it; passivity-without-trap fails validation.
- **Symptom:** moat declared as "network effects" without mechanism. **Cause:** 7 Powers used as label rather than mechanism. **Fix:** Phase 4.5 and Phase 6.4 require specifying the increasing-returns mechanism (same-side, cross-side, what flows between users); generic Power labels fail validation.
- **Symptom:** Thiel Secret reads as marketing slogan. **Cause:** AI-generated Secret kept without human conviction check. **Fix:** Phase 4.6 requires human to mark each Secret `human_endorsed: true` AND specify what would falsify it; un-endorsed Secrets are excluded from Phase 5 generation.
- **Symptom:** bar test passes on first pass without iteration. **Cause:** drafter's context grading itself. **Fix:** `bar_test.py` spawns a fresh sub-agent with concepts but NOT the drafting context; if first-pass PASS, re-run with a different sub-agent role prompt to verify.
- **Symptom:** rejected concepts get re-proposed in next run. **Cause:** signals-log.md not consulted at Phase 5 start. **Fix:** Phase 5.1 reads `signals-log.md` rejected concepts and either skips them OR explicitly justifies re-proposal based on changed conditions.
- **Symptom:** `venture-concepts.md` or `reimagination-brief.md` reads like a McKinsey deck — "leverages", "fundamentally reshapes", "robust", "meaningful value", "stakeholders". **Cause:** strategy work on Opus drifts to consultantese; the source material (Stratechery, McKinsey, Helmer) is already jargon-laden, compounding the drift. **Fix:** Phase 5 drafting reads `references/voice-constraints.md` first; bar test sub-agent applies the specificity test ("could this sentence appear in any strategy deck about any industry?"); optionally run the humanizer skill before Gate 3.
- **Symptom:** user asks for plain-English re-explanation during gate review. **Cause:** review surfaced concept_ids + framework jargon without recognition layer. **Fix:** RULE-1 in `edge-cases.md` — every gate review is HTML via html-output with memorable handle as card title + one-sentence distillation + framework explainer on first mention. See `references/gate-html-output.md`.
- **Symptom:** user endorses many Thiel Secrets but clarifies "this is not high conviction, just open empirical bets." **Cause:** Phase 4.6 framed endorsement as conviction filter. **Fix:** RULE-2 in `edge-cases.md` — default endorsement framing is "strategic lenses that suggest experiments to run"; Phase 5 spans the hypothesis space, doesn't pre-filter. Conviction-filter discipline only on explicit user signal.
- **Symptom:** Y1 metric flagged by bar test as contradicting the brief's own industry-wide projections. **Cause:** Phase 5 enrichment goal-seeked the metric. **Fix:** RULE-3 in `edge-cases.md` — Y1 metrics implying outperformance of Phase 3 projections require bottoms-up justification (conversion deltas, competing-merchant counts, precedent operators).
- **Symptom:** gate review rendered as markdown in chat. **Cause:** orchestrator skipped html-output skill call. **Fix:** all human-review gate content MUST render via html-output with diagrams per `references/gate-html-output.md`. Markdown gate reviews are forbidden — strategy work needs visual layout.

## Rules

- Never skip Gate 1, 2, or 3 — user approval at every stop.
- Never proceed past Phase 2 with all-`[A]` pain points — load-bearing pain requires V or C provenance via librarian research.
- Never skip the intersection analysis in Phase 3 — single-axis why-now is always weak.
- Never apply a structural move that doesn't fit — "not viable because…" is a valid output.
- Never let the AI filter Phase 5 concepts — conviction is the human's contribution.
- Never ship a concept missing any of the four Phase 6 stress test answers.
- Never ship the brief without running the bar test from a fresh-context sub-agent.
- Never ship Gate 3 outputs without `analysis-quality-review` clearing Pass 1 (structure) and Pass 2 (readability) on the HTML deliverable (`<slug>-reimagination-report.html`) at standard strictness — see Phase 7 + Phase 11.
- Reader-facing artifacts are HTML; machine/audit artifacts are markdown. The HTML deliverable goes through `analysis-quality-review`; markdown drafts in `working/` do NOT. The `disruption-dataset.yaml` and `signals-log.md` are machine artifacts and never reviewed.
- Never overwrite `signals-log.md` — append-only, including rejected concepts with rationale.
- Never ship human-facing deliverables with consultantese jargon — see `references/voice-constraints.md` blocklist.
- Never render a gate review as markdown — always use html-output skill per `references/gate-html-output.md`.
- Never ship a concept, framework signal, or endorsed Thiel Secret without a memorable 3-5 word handle alongside the structured ID — `references/edge-cases.md` RULE-1.
- Never apply the Thiel filter discipline to Secrets unless the user explicitly signals high conviction; default is scenario-lens framing — `references/edge-cases.md` RULE-2.
- Never accept a Y1 metric that implies outperforming a Phase 3 industry projection without explicit bottoms-up justification — `references/edge-cases.md` RULE-3.
- Every external fact-claim carries a V/C/A/I tag.
- All file reads use `encoding='utf-8'`.
- Synthesis structured Pyramid + SCQA — see `../_shared/pyramid-scqa.md`.
- 2026 terminology only — see `../_shared/2026-terminology.md`.

## Old patterns
None yet — v1.

---
<!-- Built with Agent Engineer Master — get your own production-ready skill: www.agentengineermaster.com/skill-engineer -->

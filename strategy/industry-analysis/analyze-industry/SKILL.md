---
name: analyze-industry
description: "Produces a senior-analyst industry-structure brief by orchestrating MBB sub-skills (BCG Strategy Palette, McKinsey G3 sizing, Porter Five Forces with complementors and AI-as-force, Bain profit pools on Porter value chain; Phase 2 adds arenas, S-curve, Helmer 7 Powers, JTBD). Three-layer output to 08-knowledge/world-model/industries/[slug]/. Quick or Deep mode. Three approval gates. Fresh-context bar test. V/C/A/I provenance. Pyramid + SCQA synthesis shipped as a quality-reviewed HTML report (rendered via html-output, audited by analysis-quality-review). Concludes with where-to-play/how-to-win. Triggers on 'analyze the [industry] industry', 'industry brief for [industry]', 'is [industry] structurally attractive', 'industry analysis for [PE deal/market entry]', 'industry-structure analysis'. Do NOT activate for single-company analysis (use build-company-model), DTC category go/no-go (use assess-category), decision pressure-testing (use stress-test), or buyer/investor universe (use building-buyer-shortlists)."
---

# Analyze Industry

For a single industry-structure question (attractiveness, entry, allocation, roll-up thesis), produce a thesis-grade industry brief synthesizing 4-8 MBB analytical lenses. Three-layer output: narrative synthesis rendered as an HTML report (`industry-brief.html`), structured filters (`industry-brief.yaml`), append-only catalysts (`signals-log.md`). Three approval gates. Fresh-context senior-analyst bar test.

**The bar (per `_shared/bar-test.md`):** a senior sub-sector analyst reading the brief should find ≥3 non-obvious observations and zero obvious-missing.

**Iron rules:**
- Every external fact-claim carries a V/C/A/I tag — see `../_shared/provenance-tagging.md`.
- Synthesis structured Pyramid + SCQA — see `../_shared/pyramid-scqa.md`.
- 2026 terminology only — see `../_shared/2026-terminology.md`.
- Brief never ships without bar test pass — see `../_shared/bar-test.md`.
- The reader-facing brief ships as a single self-contained HTML report (`industry-brief.html`) rendered via the `html-output` skill — never markdown. Machine/audit artifacts (`industry-brief.yaml`, `signals-log.md`, `bar-test.md`, `working/*.md`) stay markdown/YAML — see `../_shared/output-conventions.md`.
- The HTML brief clears `analysis-quality-review` Pass 1 (structure) and Pass 2 (readability) before Gate 3 — see step 9.

## Process

### 1. Intake
Ask: industry slug, scope question (e.g., "is industrial robotics attractive for a sponsor-backed roll-up?"), mode (Quick / Deep), optional docs folder (industry reports, expert interview notes, target company materials). Run `python scripts/init_analysis.py --slug <industry-slug> --question "<scope-question>" --mode <quick|deep>` to create the industry folder.

### 2. Gate 1 — Scope + market definition (STOP)
Read `references/gate-prompts.md` Gate 1 template. Present: 3 candidate market framings (broad/sharpened/surgical) using the four-test discipline (specificity, measurability, supply-side coherence, customer coherence) + the sub-skill battery proposed for the chosen mode. User confirms framing + sub-skill cut. `python scripts/log_run.py --event gate-1-approved`.

### 3. Strategic environment diagnosis (sub-skill: `assess-strategic-environment`)
Call the `assess-strategic-environment` sub-skill against the confirmed scope from Gate 1. It diagnoses the competitive environment type — Classical / Adaptive / Visionary / Shaping / Renewal — using the three-question discipline (predictability, malleability, harshness), flags any ambidexterity, and emits a routing matrix that drives sub-skill weighting in step 5. Output written to `working/strategic-environment.md` with V/C/A/I tags.

### 3a. Ambidexterity checkpoint (STOP — only if triggered)
If `working/strategic-environment.md` declares ambidexterity (industry genuinely spans two environments at different layers / geographies / customer segments), STOP and present `references/gate-prompts.md` "Ambidexterity Checkpoint" template. User chooses: single-focus / dual analysis / re-scope. Do NOT auto-proceed; do NOT auto-run sub-skills twice. After resolution: `python scripts/log_run.py --event ambidexterity-resolved`. If single-environment, skip this step.

### 4. Sub-skill battery (parallel where independent)
Read `references/sub-skill-orchestration.md` for the routing matrix.

**Quick mode (always):**
- `size-market` — must run before `map-value-chain-profit-pools` (sizing calibrates pool dollars)
- `map-five-forces`
- `map-value-chain-profit-pools`

**Deep mode (full battery — Phase 1 + Phase 2 built):**
- All of Quick mode, plus:
- `map-competitive-arena` — runs in parallel with `analyze-trajectory` after Quick-mode 3 complete
- `analyze-trajectory` — reads `size-market` G3 output
- `assess-moat-sources` — runs AFTER `map-five-forces` AND `map-value-chain-profit-pools` (cross-skill reconciliation enforced at Gate 2)
- `analyze-demand` — conditional per routing matrix (skip if mature + stable demand + no Five Forces substitution flag)

Each sub-skill writes its output to `working/[sub-skill-name].md` with V/C/A/I tags. Run independent sub-skills in parallel where the orchestrator can spawn them concurrently.

### 5. Gate 2 — Factual base review (STOP)
Read `references/gate-prompts.md` Gate 2 template. User validates each sub-skill output before synthesis. Flag any sub-skill output where the V/C/A/I tag distribution is >50% A or I (asserted/inferred) — that signals weak evidence base. If the Helmer power consistency check returns MISMATCH (per `references/sub-skill-orchestration.md` output reconciliation), Gate 2 is BLOCKED — require rework on the weaker sub-skill before proceeding. `python scripts/log_run.py --event gate-2-approved`.

### 6. Synthesis

**6a. Authoring spec (ghost-deck discipline) — before drafting.** Invoke `analysis-quality-review` in `mode: spec` (`doc_type: brief`, `structural_framework: minto-pyramid`) to retrieve the authoring template. Fill it in using the validated sub-skill outputs: the governing observation, the MECE supporting reasons, the SCQA opening, the evidence inventory per reason. Write the filled-in spec to `working/authoring-spec.md`. Then invoke `analysis-quality-review` in `mode: spec-judge` with the spec + the `supporting_artifacts` manifest (point at `working/` and `industry-brief.yaml`) + an `intent_summary` naming the senior-analyst reader and the attractiveness/entry decision. If the judge returns FAIL, revise the spec and re-invoke; loop until PASS or `max_spec_iterations: 3` ESCALATE. Catching a broken governing observation or MECE overlap here costs 2-3 lines of spec; catching it post-render costs a full re-synthesis.

**6b. Draft the brief.** Read `../_shared/pyramid-scqa.md`. Using the approved spec as scaffolding, draft the brief content into `working/industry-brief-draft.md` (markdown — audit substrate, not the reader-facing deliverable):
- **SCQA opening** — Situation / Complication / Question / Answer
- **Pyramid body** — one main answer per section, MECE supporting reasons, evidence with provenance tags
- **Where-to-play / how-to-win recommendation** — the closing section, framed in Lafley/Martin language. This is the "so what" the senior reader is paying for.

**6c. Structured + log outputs.** Generate `industry-brief.yaml` (machine-readable filter fields per `references/output-schema.md`) and seed `signals-log.md` with dated catalysts/discontinuities surfaced during analysis. Both stay machine/append-only artifacts — never rendered to HTML.

### 7. Senior-analyst bar test
Read `../_shared/bar-test.md`. Run `python scripts/bar_test.py --brief-path 08-knowledge/world-model/industries/<slug>/working/industry-brief-draft.md --industry "<slug>"`. The script spawns a fresh-context sub-agent. If non-obvious observations <3 OR obvious-missing list non-empty OR modernization flags non-zero, iterate the relevant sub-skill outputs, re-draft, and re-run. The bar test runs on the markdown draft — content depth is settled before the HTML render.

### 8. Render the HTML deliverable
Once the bar test passes, invoke the `html-output` skill to render `working/industry-brief-draft.md` as a single self-contained HTML report — `industry-brief.html` at the industry root (`08-knowledge/world-model/industries/<slug>/industry-brief.html`). Use the `report` archetype. The HTML report is the canonical reader-facing deliverable; the markdown draft stays in `working/` as audit substrate. Render the sub-skill exhibits inline where they support the argument — Five Forces heatmap, profit-pool bars, S-curve position, strategic-group map.

### 9. Quality review — analysis-quality-review
Invoke `analysis-quality-review` against `industry-brief.html` (the HTML deliverable only — the `working/` markdown drafts are NOT reviewed):
1. `mode: review, pass: 1` — `structural_framework: minto-pyramid`, strictness `standard` (Quick mode) or `high` (Deep mode). Supply the manifest: `supporting_artifacts` pointing at `working/` (role: `evidence`) and `industry-brief.yaml` (role: `source-of-truth`); `load_bearing_elements` declaring `evidence_tags` (pattern `\[(V|C|A|I)\]`), `phase_citations`, `numeric_claims_with_citations`; `intent_summary` naming the senior-analyst reader and the attractiveness/entry decision. On FAIL, read the violation report + `fix-patterns.md`, apply targeted `Edit` calls to the HTML (or regenerate a section via `html-output` for structural fixes), and re-invoke with the same `audit_dir` + `previous_violations`. Loop until PASS.
2. `mode: review, pass: 2` against the same HTML + same `audit_dir` (gated on Pass 1 PASS). Same apply-fixes-yourself loop until PASS.

### 10. Gate 3 — Full draft + bar-test + quality-review review (STOP)
Read `references/gate-prompts.md` Gate 3 template. User reads `industry-brief.html` + `industry-brief.yaml` + `bar-test.md` + the `analysis-quality-review` audit summary together. Approve / rework specific sections / reject. `python scripts/log_run.py --event gate-3-approved`.

### 11. Closing feedback gate
Ask the four-routing question: any feedback for **learnings** (behavioral preferences) / **edge-cases** (factual exceptions) / **rules** (never again) / **approved-examples** (save as reference output)? Save outputs accordingly.

## Update mode
If invoked with `--update <industry-slug>`, skip steps 2-10. Run `python scripts/update_signals.py --slug <slug>` — researches recent industry activity since last signals entry, appends date-stamped entries to `signals-log.md`. Single user-confirmation gate at end.

## Integrates with

- **`build-company-model`** — downstream consumer. A sell-side mandate in an industry with an existing `industry-brief.yaml` inherits the granular market sizing, profit-pool map, and 7 Powers assessment as priors, removing the most expensive recall variance from company-model drafting.
- **`stress-test`** — recommended follow-up. The WTP/HTW recommendation is the natural input to a three-phase stress-test pressure round.
- **`assess-category`** — adjacent but distinct. DTC verdict skill operates at a different output contract (GO/NO-GO with weighted scoring). `analyze-industry` produces structural diagnosis; `assess-category` produces investment verdict. Do not call each other.
- **`html-output`** — renders the reader-facing deliverable. The orchestrator hands the synthesized brief content to `html-output` (`report` archetype) at step 8; the HTML report (`industry-brief.html`) is the canonical output. Markdown drafts stay in `working/` for audit.
- **`analysis-quality-review`** — quality gate on the reader-facing artifact. Called in `mode: spec` + `mode: spec-judge` at step 6a (ghost-deck discipline before drafting — the spec is a private `working/` scaffold, not reviewed as a deliverable) and `mode: review pass: 1` + `pass: 2` at step 9 against the HTML deliverable. Use `doc_type: brief`, `structural_framework: minto-pyramid`. Working markdown drafts in `working/` are NOT reviewed. See `.claude/skills/analysis-quality-review/references/calling-contract.md` for the manifest schema.

## Gotchas

- **Symptom:** brief reads structurally complete but reaches no clear WTP/HTW recommendation. **Cause:** synthesis step skipped the Lafley/Martin closing section in favor of generic "key takeaways." **Fix:** `industry-brief.html` must end with a Where to Play / How to Win section that names (a) which segment to enter or focus, (b) the capability + structural-power combination that wins there. Generic takeaways fail Gate 3.
- **Symptom:** Five Forces analysis declares every force "moderate" with no governing force named. **Cause:** sub-skill ran as a checklist, not an inquiry. **Fix:** `map-five-forces` validation requires the analyst to name THE force that governs this industry's profit distribution in one causal sentence before validation passes.
- **Symptom:** market sizing presents one TAM number for the whole industry. **Cause:** G3 granular decomposition was skipped. **Fix:** `size-market` validation rejects any sizing without ≥3 sub-segment growth rates and an explicit de-averaging statement.
- **Symptom:** value chain mapped but profit shown as revenue margin, not absolute EBIT/economic profit. **Cause:** drafter conflated revenue concentration with profit concentration. **Fix:** `map-value-chain-profit-pools` validation requires EBIT or economic profit per value-chain stage. Revenue-only profit pools fail validation.
- **Symptom:** bar test returns "no obvious observations missing" on first pass without iteration. **Cause:** same context that drafted the brief is grading itself with motivated reasoning. **Fix:** `bar_test.py` spawns a fresh sub-agent with the brief but NOT the drafting context, prompted to actively find gaps.
- **Symptom:** brief uses 2005-era framing (raw SWOT, BCG matrix, "moat" without naming a Power). **Cause:** drafter defaulted to legacy vocabulary. **Fix:** bar test's modernization watchlist (per `../_shared/bar-test.md`) flags these; brief cannot ship until all flags resolved.
- **Symptom:** brief delivered as a markdown file. **Cause:** synthesis stopped at the `working/` draft and skipped the html-output render. **Fix:** the reader-facing deliverable is always `industry-brief.html` rendered via `html-output` (step 8). Markdown lives in `working/` as audit substrate only.
- **Symptom:** `analysis-quality-review` Pass 2 surfaces dozens of readability nits but the brief has no clear governing observation. **Cause:** the ghost-deck spec-judge (step 6a) was skipped, so a broken D1 reached the render. **Fix:** never skip step 6a — the spec-judge loop catches governing-observation and MECE failures at the 2-3K-token spec stage, before the expensive render.

## Rules

- Never skip Gate 1, 2, or 3 — user approval at every stop.
- Never skip the strategic environment diagnosis (step 3) — wrong environment = wrong toolkit = useless output.
- Never auto-proceed when ambidexterity is detected (step 3a). Always stop and surface the choice to the user.
- Never write the brief without running the bar test from a fresh-context sub-agent.
- The reader-facing brief is HTML (`industry-brief.html`), rendered via `html-output`. Machine/audit artifacts (`.yaml`, `signals-log.md`, `bar-test.md`, `working/*.md`) stay markdown/YAML.
- Never ship Gate 3 without `analysis-quality-review` clearing Pass 1 (structure) and Pass 2 (readability) on the HTML brief — see step 9.
- Never skip the ghost-deck spec-judge at step 6a — it is the cheap pre-catch for structural failures.
- Every external fact-claim carries a V/C/A/I tag.
- All file reads use `encoding='utf-8'`.
- Industry brief always concludes with a WTP/HTW recommendation, not generic takeaways.
- Synthesis structured Pyramid + SCQA — see `../_shared/pyramid-scqa.md`.
- 2026 terminology only — see `../_shared/2026-terminology.md`. Legacy frames flagged by bar test must be resolved before ship.

## Old patterns
v2 (2026-05-21) — synthesis now renders the brief as a self-contained HTML report via the `html-output` skill and clears `analysis-quality-review` Pass 1 + Pass 2 before Gate 3; ghost-deck `spec` + `spec-judge` discipline added at step 6a; the markdown brief was demoted to `working/industry-brief-draft.md` audit substrate.
v1 — markdown `industry-brief.md` as the deliverable; no quality-review gate.

---
<!-- Built with Agent Engineer Master — get your own production-ready skill: www.agentengineermaster.com/skill-engineer -->

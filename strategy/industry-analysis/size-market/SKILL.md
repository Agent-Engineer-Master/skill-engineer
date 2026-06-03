---
name: size-market
description: "Produces a granular market sizing for a defined industry/sub-segment using McKinsey G3 granular-growth decomposition + arenas qualification screen, with top-down and bottom-up triangulation. Output: market-sizing.md with TAM/SAM/SOM, ≥3 sub-segment growth-rate decomposition, explicit de-averaging statement, and V/C/A/I provenance tags on every numeric claim. Sized to PE-CDD speed. Triggers on 'size the [industry] market', 'TAM SAM SOM for [industry]', 'how big is the [industry] market', 'market sizing for [industry]', 'granular market sizing'. Sub-skill of analyze-industry but invocable standalone. Do NOT activate for single-company revenue forecasting (use build-company-model), customer-segment demand analysis (use analyze-demand), or competitive share analysis (use map-competitive-arena)."
---

# Size Market

For a defined industry or sub-segment, produce a granular market sizing using McKinsey G3 decomposition + arenas qualification screen. Output: `market-sizing.md` with explicit de-averaging.

**The discipline (McKinsey G3 / granular growth):** aggregate market growth rates are misleading. G3-level sub-segment portfolio choice explains ~65% of organic top-line growth. Always decompose before accepting any aggregate rate.

**Iron rules:**
- Every numeric claim carries a V/C/A/I tag — see `../_shared/provenance-tagging.md`.
- ≥3 sub-segment growth rates required (Quick mode) or ≥5 (Deep mode). Single-rate sizing fails validation.
- Top-down + bottom-up triangulation required; gap >25% triggers reconciliation; gap <5% triggers circular-sourcing check.
- Arenas screen run — does the market qualify (high growth + high dynamism) per McKinsey 2024 criteria?
- Definition locked at intake; base currency declared; sources <24mo old (or justified as still current).

## Process

### 1. Intake — lock the analysis frame
Confirm and write to output header: industry slug, geographic scope, base currency (default USD), reporting year (current 2026), time horizon (current + 3-5yr), depth (Quick = TAM+SAM + ≥3 G3 / Deep = TAM+SAM+SOM + ≥5 G3 + share-shift data), and a **one-sentence definition lock** (what's in, what's out). Read `references/sizing-methodology.md` "Intake" before research.

### 2. Top-down sizing
Read `references/sizing-methodology.md` "Top-down" + `references/data-sources.md`. Source order: regulatory filings, trade bodies, government stats, syndicated paid (IBISWorld, Gartner, etc.), sell-side analyst notes. **Never cite an AI aggregator (Perplexity, ChatGPT) without the underlying source.** Capture: total market value, currency, year, geographic basis, definition used. Reconcile to locked definition. Every figure tagged V/C/A/I with report name + year + section.

### 3. Bottom-up sizing
Read `references/sizing-methodology.md` "Bottom-up". Estimate via volume × price, customers × spend × penetration, or value-theory (benefit × capture rate). Use **independent** sources — not the same report as top-down (circular sourcing fails). Apply the 10-customer test: can you name 10 specific customers in this market? Every assumption tagged. **Software/SaaS markets** (industry slug or definition contains any of: `saas, software, cloud, platform, api, developer tools, observability, security software, fintech-software`) **must include value-theory as a required third triangulation leg** — unit counts are noisy and value-per-customer is more defensible.

### 4. Triangulation
Compare top-down vs bottom-up. Bands: <5% suspect circular → re-verify independence; 5-25% normal → pick primary; >25% reconcile to specific assumption(s). Document gap %, reconciliation, primary choice, and rationale in output.

### 5. G3 granular decomposition
Decompose into ≥3 (Quick) or ≥5 (Deep) sub-segments at G3 level (sub-industry × geography × customer-segment). **If the arenas screen (step 6) classifies the market as `Arena` (the highest-dispersion case), require ≥7 sub-segments regardless of mode** — arena markets have the highest within-market dispersion and benefit most from finer-grained decomposition. For each: current size, 5yr CAGR, source tag. Sub-segments must sum to within ±10% of TAM (sanity check). Required output: an explicit **de-averaging statement** — "Aggregate growth is X%, but sub-segment Y grows at Z% vs sub-segment W declining at -V% — the aggregate is misleading because [reason]." If sub-segments cluster, state that explicitly.

### 6. Arenas qualification
Read `references/arenas-screen.md`. Apply McKinsey's two-axis screen: high growth (>10% CAGR) AND high competitive dynamism (top-5 share movement >5pp over 5yr). Classify: Arena / Pre-arena / Mature / Contested mature / Declining. Note if the market maps to one of McKinsey's 12 current or 18 future arenas. Single sentence on strategic implication.

### 7. Scenario range (Deep mode; recommended for Quick)
Produce Conservative / Base / Aggressive figures for headline TAM and SAM with 3-5 swing variables. For Deep + SOM: apply realism check (Year-1 SOM >5% of SAM needs justification; >10% rejected for new entrants without backlog).

### 8. Validate + write output
Run `python scripts/validate_sizing.py --output-path <path>` — checks tag coverage, ≥3 sub-segments (≥7 for Arena-classified), de-averaging statement, triangulation, arenas classification, value-theory mention for SaaS/software, TAM>SAM>SOM ordering, no LLM-aggregator-only citations, no stale sources, currency + definition declared, and presence of trailing `next_skills:` YAML block. Write to `working/market-sizing.md` (orchestrator mode) or `standalone/size-market-YYYY-MM-DD.md` (standalone mode).

**HTML on request (standalone only):** markdown is the default and the only format the validator and the orchestrator consume. If the user explicitly asks for an HTML version of a standalone run, then after validation passes, also render the output via the `html-output` skill and review it per `../_shared/output-conventions.md` § "HTML deliverables and quality review". Never produce HTML automatically.

### 9. Append structured `next_skills` YAML block
End the output file with a YAML block declaring the next recommended skills for Phase 2 orchestrator automation. Format:

```
---
next_skills:
  - map-five-forces    # to assess industry structure given the sizing
  - map-value-chain-profit-pools    # to map where profits sit in this market
  - analyze-trajectory    # for Three-Horizons portfolio overlay (Phase 2)
---
```

At least one skill must be listed. Validator enforces presence.

## Gotchas

- **Symptom:** sizing presents a single TAM number with a single growth rate. **Cause:** G3 decomposition skipped — drafter accepted the headline IBISWorld figure. **Fix:** validator rejects outputs without ≥3 sub-segment growth rates AND an explicit de-averaging statement.
- **Symptom:** top-down and bottom-up land within 5% on first pass. **Cause:** bottom-up used the same source as top-down (circular sourcing). **Fix:** bottom-up must use independent volume × price or customer × spend × penetration; source must be distinct from the top-down report.
- **Symptom:** every figure tagged `[V: industry report]` with no specificity. **Cause:** lazy provenance tagging. **Fix:** tags must name report, year, and page/section. Validator flags vague tags as malformed.
- **Symptom:** arenas screen skipped or classification asserted without the two-axis test. **Fix:** validation requires arenas classification + both underlying metrics (growth rate AND top-5 share movement) with sources.
- **Symptom:** figures cited as `[C: Perplexity Finance 2026]` or `[V: ChatGPT]`. **Cause:** AI aggregator cited as source. **Fix:** validator flags any tag whose only source is an LLM aggregator. Always trace to the underlying syndicated report and cite that.
- **Symptom:** SAM > TAM, or SOM > SAM. **Cause:** wrong filter chain or mixed-basis figures. **Fix:** validator auto-checks ordering.
- **Symptom:** all sources dated 2021-2022 for a 2026 sizing. **Cause:** stale data carried forward without adjustment. **Fix:** validator flags pre-2024 sources unless justified as "still current" / "extrapolated by trailing CAGR".
- **Symptom:** Year-1 SOM = 15% of SAM with no contract backlog cited. **Cause:** aspirational SOM. **Fix:** Deep-mode SOM section enforces realism bands (0.1-0.5% Y1, 1-5% Y3 for new entrants).
- **Symptom:** sub-segments sum to 130% of TAM. **Cause:** definitional overlap or wrong G3 cut. **Fix:** sub-segment table must sum to ±10% of TAM; flag in reconciliation if not.

## Rules

- Never present a sizing without ≥3 sub-segment growth rates and an explicit de-averaging statement.
- Never accept circular sourcing between top-down and bottom-up.
- Never cite an AI aggregator (Perplexity, ChatGPT, etc.) as the primary or sole source.
- Lock the definition, base currency, and reporting year at intake; do not switch mid-analysis.
- All file reads use `encoding='utf-8'`.

## Old patterns

None yet — v1.1 (2026-05-18 refinement: added data-sources reference, scenario discipline, stale-data/aggregator/ordering checks, contested-mature classification, value-theory triangulation option).

---
<!-- Built with Agent Engineer Master — get your own production-ready skill: www.agentengineermaster.com/skill-engineer -->

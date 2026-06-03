---
name: map-value-chain-profit-pools
description: "Produces a paired Porter value-chain decomposition + Bain/Gadiesh-Gilbert profit-pool overlay for a defined industry. Output: value-chain-profit-pools.md with value-chain stages (inbound logistics through service + support activities), absolute EBIT/economic profit (not revenue margin) per stage, horizontal-bar profit-pool visualization in markdown, identification of which stage has structural profit concentration and why, plus V/C/A/I provenance tagging. The pairing is deliberate — value chain alone is incomplete; profit pool alone lacks structural context. Sub-skill of analyze-industry but invocable standalone. Triggers on 'value chain analysis for [industry]', 'profit pool analysis for [industry]', 'where does the money sit in [industry]', 'where do profits concentrate in [industry]', 'value chain and profit pools'. Do NOT activate for single-company P&L decomposition (use build-company-model), customer-level economics (use analyze-demand), or competitive share analysis (use map-competitive-arena)."
---

# Map Value Chain + Profit Pools

For a defined industry, decompose the value chain (Porter) and overlay absolute economic profit (Bain / Gadiesh-Gilbert) by stage. Output: `value-chain-profit-pools.md` with stage-by-stage profit map and identification of where structural profit concentration sits.

**The discipline:** profit and revenue are frequently inverted along the value chain. Mapping revenue without economic profit produces a misleading picture. Use EBIT or economic profit (not gross margin, not revenue share).

**Iron rules:**
- Profit measured as **absolute EBIT or economic profit** per stage, not revenue margin or revenue share.
- **Normalised** over 3-year trailing average margin (5-year for cyclical industries).
- **Ranges, not point estimates** — every stage EBIT carries a low–base–high range.
- Horizontal-bar visualisation required (markdown table with bar-width proxy).
- Structural protection statement required: name a Helmer 7 Power for the highest-EBIT stage. If none identifiable, state "not structurally protected — expect arbitrage" explicitly.
- Cross-references to `working/five-forces.md` if present (the governing force should correctly predict the profit-pool location).
- **When stage capital intensity varies >2×, escalate metric from EBIT to economic profit (EP) — see `references/economic-profit.md`.** This is a hard rule, not a recommendation: validator fails if capital-intensity data is disclosed with >2× max/min ratio and only EBIT is used.
- Append a structured `next_skills:` YAML block at end of file for orchestrator hand-off.

## Process

### 1. Intake
Confirm: industry slug, geographic scope, value-chain definition (which stages — use a sector-appropriate template from `references/value-chain-templates.md`, including the vertical-integration and platform Z-shape notes). Read `references/profit-pool-methodology.md`.

### 2. Decompose the value chain
List 5-9 stages from raw inputs to end customer. For each: brief description, 2-3 representative players, estimated revenue contribution to total industry revenue as a **range** (low–base–high), V/C/A/I-tagged.

### 3. Estimate absolute economic profit per stage
For each stage, estimate EBIT in absolute dollars, normalised over 3-5 years, expressed as a range. **If stage capital intensity is disclosed and max/min ratio >2×, you MUST use economic profit (EP / NOPAT minus capital charge) — not EBIT — see `references/economic-profit.md`.** If capital intensity is not disclosed, EBIT is acceptable but the validator will warn you to disclose it. Method: listed-comparable triangulation — see `references/listed-comparable-triangulation.md` for the 5-step protocol (pure-play ≥70% revenue concentration; GAAP EBIT including SBC; 3-year average; median across n≥3 comparables; disclose dispersion). Document method + comparables per stage.

### 4. Generate profit-pool visualisation
Use the template in `assets/profit-pool-template.md`. Produces a horizontal-bar markdown table where bar width is proportional to absolute EBIT (base case). Optional executive river-chart variant for orchestrator hand-off.

### 5. Identify structural profit concentration
Name the stage with highest absolute profit concentration. Then answer: **why does profit concentrate here?** The answer must name a Helmer 7 Power — scale economies / network economies / counter-positioning / switching costs / branding / cornered resource (incl. regulatory) / process power. Apply the per-power diagnostic questions in `references/structural-protections.md` — do not just assert the label. If no structural reason is identifiable, state: "not structurally protected — expect arbitrage by [named entrant] within [horizon]."

### 6. Cross-reference Five Forces
If `working/five-forces.md` exists, reconcile: does the named governing force correctly predict the profit-pool location? E.g., "buyer power high" should NOT coexist with "the customer-facing stage captures the most profit." If contradictory, flag for orchestrator Gate 2 reconciliation.

### 7. Validate + write output
Run `python scripts/validate_profit_pools.py --output-path <path>` — checks: EBIT or EP used, absolute $ figures, bar visualisation, named Helmer power (or explicit unstable-finding), V/C/A/I tag coverage ≥5, anti-pattern protections rejected ("adds value", "critical", "differentiation", etc.), capital-intensity >2× requires EP, structured `next_skills:` YAML block present. Soft warnings on missing normalisation disclosure, false precision, flat pools, and missing capital-intensity disclosure. Write to `working/value-chain-profit-pools.md` (orchestrator) or `standalone/map-value-chain-profit-pools-YYYY-MM-DD.md` (standalone).

**HTML on request (standalone only):** markdown is the default and the only format the validator and the orchestrator consume. If the user explicitly asks for an HTML version of a standalone run, then after validation passes, also render the output via the `html-output` skill and review it per `../_shared/output-conventions.md` § "HTML deliverables and quality review". Never produce HTML automatically.

### 8. Append `next_skills` YAML block
At the very end of the output file, append a fenced YAML frontmatter block declaring next recommended skills for orchestrator Phase 2 automation. Minimum one entry. Example:

```
---
next_skills:
  - assess-moat-sources    # to assess durability of the structural protection identified
  - map-five-forces        # if Five Forces not yet present, for cross-reference reconciliation
---
```

## Gotchas

- **Symptom:** profit pool shown as revenue margin % per stage instead of absolute EBIT $. **Cause:** drafter confused gross margin with economic profit. **Fix:** validator rejects any output where the profit metric is a percentage. Absolute $ is required because two stages with identical margins can have very different profit concentration when revenue scales differ.
- **Symptom:** structural protection statement reads "the manufacturing stage captures most profit because it adds the most value." **Cause:** circular / non-structural reasoning. **Fix:** the protection must be a Helmer power. Validator rejects "adds value", "is critical", "differentiated", "first-mover" (alone), "expertise" (alone), "relationships" (alone), "quality", "complexity" (alone). See `references/structural-protections.md` for the full anti-pattern list and per-power diagnostics.
- **Symptom:** profit pool location contradicts Five Forces governing force without flagging. **Cause:** sub-skills run independently without cross-reference. **Fix:** step 6 requires reconciliation; orchestrator's Gate 2 surfaces the contradiction.
- **Symptom:** every stage shows similar EBIT (flat profit pool). **Cause:** likely an estimation error or comparable-set contamination. **Fix:** validator warns on flat pools. Justify explicitly (e.g., "late-commoditisation phase — see evidence") OR re-estimate with tighter pure-play comparables.
- **Symptom:** stage EBIT quoted as "$1.94B" with no range. **Cause:** false precision — triangulated estimates carry ±20-30% irreducible uncertainty. **Fix:** validator warns; express as low–base–high ranges.
- **Symptom:** EBIT compared across stages with materially different capital intensity (e.g., fabless vs. foundry). **Cause:** EBIT understates profitability of capital-light stages relative to capital-heavy. **Fix:** upgrade to economic profit per `references/economic-profit.md` when capital intensity varies >2×.
- **Symptom:** single-year margin print used. **Cause:** noisy in cyclical industries. **Fix:** normalise over 3-year trailing average (5-year for cyclicals).

## Rules

- Never use revenue margin or revenue share where absolute EBIT/economic profit is required.
- Never declare a profit-pool location without naming the Helmer power that sustains it (or declaring it unstable).
- Never quote stage EBIT without a range.
- Never use a single-year margin without normalisation justification.
- Never skip the Five Forces cross-reference when both files exist.
- Every numeric claim carries a V/C/A/I tag.
- All file reads use `encoding='utf-8'`.

## Old patterns
v1.2 (2026-05-18) added hard rule: capital-intensity >2× forces EP (not just EBIT); validator parses capital-employed columns and inline numbers. Added structured `next_skills:` YAML block for orchestrator Phase 2 hand-off. v1.1 hardened Helmer-power vocabulary, added economic-profit + listed-comparable + structural-protections references, strengthened validator with anti-pattern rejection and quality warnings.

---
<!-- Built with Agent Engineer Master — get your own production-ready skill: www.agentengineermaster.com/skill-engineer -->

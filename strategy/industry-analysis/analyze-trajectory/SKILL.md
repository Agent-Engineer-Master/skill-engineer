---
name: analyze-trajectory
description: "Produces a forward-looking industry trajectory analysis: dual S-curve (market-adoption + technology lifecycle with diagnostic signals), Three Horizons overlay on G3 sub-segments (consumes size-market when present), discontinuities catalog (regulatory/tech/behavioral with year-range timing windows), Helmer Power Progression (which 7 Powers are buildable now / Year 3 / Year 5 / closed), and base/bear/bull scenarios with ≥3 named swing variables for the 5-year horizon. Output: trajectory.md with V/C/A/I tags. Sub-skill of analyze-industry but invocable standalone. Triggers on 'industry trajectory for [industry]', 'where is [industry] on the S-curve', 'three horizons for [industry]', 'scenario analysis for [industry]', 'discontinuities facing [industry]'. Do NOT activate for company-specific moat assessment (use assess-moat-sources), market sizing (use size-market), or competitive arena mapping (use map-competitive-arena)."
---

# Analyze Trajectory

For a defined industry, analyze direction of travel: dual S-curve position, Three Horizons portfolio overlay on G3 sub-segments, discontinuities, Helmer Power Progression, and base/bear/bull scenarios. Output: `trajectory.md`.

**The discipline:** trajectory is not extrapolation. Linear continuation past an inflection is the most common failure mode. Every assessment must name the diagnostic signal, the timing window, and the swing variable that could falsify it.

**Iron rules:**
- Every claim about trajectory carries a V/C/A/I tag — see `../_shared/provenance-tagging.md`.
- **Dual S-curve mandatory** — assess BOTH market-adoption lifecycle AND technology lifecycle. They desynchronize. Skipping either = analysis failure.
- ≥3 G3 sub-segments classified into H1 / H2 / H3 (consume from size-market when present).
- ≥2 discontinuities named with explicit **year-range timing windows** (e.g., "2026-2028"). "Soon" / "coming" / "eventually" fail validation.
- Power Progression: name which of Helmer's 7 Powers are buildable NOW, in YEAR 3, in YEAR 5, and which are CLOSED. Late entrants cannot build Counter-Positioning in a mature industry.
- Scenarios: base / bear / bull with ≥3 **named** swing variables (not "growth higher / growth lower"). Swing variables must be independent and falsifiable.
- 5-year forward horizon is the default; longer horizons require explicit justification.

## Process

### 1. Intake
Confirm: industry slug, geographic scope, 5-year horizon (or justified alternative), and **G3 sub-segment source**. Check `working/market-sizing.md` in the same industry folder. If present, extract the G3 sub-segment table for Step 3 consumption. If absent (standalone mode), ask the user to supply ≥3 named sub-segments OR run `size-market` first. Record the source in the output header ("G3 source: working/market-sizing.md" or "G3 source: user-supplied at intake").

### 2. Dual S-curve assessment
Read `references/s-curve-methodology.md`. Produce TWO assessments:

- **Market-adoption S-curve** — penetration of the underlying customer need. Classify stage (Introduction / Growth / Maturity / Decline). Name ≥2 diagnostic signals from the reference (penetration %, CAC trajectory, share concentration, capex character). Each signal carries a V/C/A/I tag.
- **Technology S-curve** — capability / cost frontier of the production technology. Classify stage independently. Name ≥2 diagnostic signals.

Then explicitly state whether the two are SYNCHRONIZED or DESYNCHRONIZED, and what the desynchronization implies. (Example: autos market = late maturity, tech = EV/AV early growth → tech S-curve will reshape the market S-curve within 5yr.)

### 3. Three Horizons portfolio overlay
Read `references/three-horizons.md`. Classify each G3 sub-segment (from Step 1) into H1 / H2 / H3:

- **H1** — today's profit engine, defend/extend, scale economies dominate
- **H2** — 2-5yr horizon, scaling new business with proven model
- **H3** — 5-10yr options/experiments, unproven model, high optionality

Universal-H1 classification fails the bar test (real industries always have at least one H2 or H3 sub-segment unless explicitly declining). State the implied portfolio resource allocation as a single sentence (e.g., "70/20/10 conventional; this industry warrants 60/30/10 because [reason]").

### 4. Discontinuities catalog
Read `references/discontinuities-catalog.md`. Identify ≥2 discontinuities across the three types (regulatory / technology / behavioral). For each:

- **Type** (regulatory / technology / behavioral)
- **Description** — one sentence, named not generic
- **Timing window** — explicit year range (e.g., "2026-2028 likely, 2028-2030 possible"). "Soon", "eventually", "in the coming years" fail validation.
- **Leading indicator** — the named signal that resolves the timing window
- **Direction of impact** on the industry profit pool (compress / expand / redistribute)
- V/C/A/I tag on the underlying evidence

If only one discontinuity is identifiable across all three types in a 5yr horizon for a real industry, the search was incomplete — return to the reference and re-scan.

### 5. Helmer Power Progression assessment
Read `references/power-progression.md`. Using the lifecycle stage from Step 2, map each of Helmer's 7 Powers to one of four states:

- **Open now** — buildable today
- **Open Year 3** — window opens as the industry transitions
- **Open Year 5+** — accumulates slowly, long-dated
- **Closed** — window shut; cannot be built by a new entrant

Hand off the Power-availability table to `assess-moat-sources` (which assesses which Powers a specific firm can build). This skill establishes the menu of available Powers; `assess-moat-sources` selects from the menu.

### 6. Base / bear / bull scenarios
Read `references/scenario-methodology.md`. Produce three 5-year scenarios with **≥3 named swing variables**:

- **Base** — modal trajectory under current discontinuities
- **Bear** — what plays out if 1-2 swing variables resolve against the industry
- **Bull** — what plays out if 1-2 swing variables resolve for the industry

Each swing variable is named, independent, and falsifiable. Examples: "EU AI Act enforcement intensity (light vs strict)", "GPU $/hour ($0.50 vs $0.20 by 2028)", "ambient-scribe EHR-integration mandate (yes/no by 2027)". Generic "growth could be higher or lower" fails validation.

**Conditional rigor:** If `working/market-sizing.md` exists (orchestrator mode), scenarios MUST be quantitative — ≥3 dollar figures (`$XB` / `$XM`) AND ≥3 CAGR figures (`X% CAGR`) across base/bear/bull combined. Validator fails the output otherwise. In standalone mode (no sibling `market-sizing.md`), qualitative scenarios pass with a soft warning. See `references/scenario-methodology.md` "Quantitative rigor" section.

### 7. Reconcile with size-market growth rates (when present)
If `working/market-sizing.md` exists, check that the S-curve stage assessed in Step 2 is consistent with the aggregate growth rate sized. Examples: growth-stage classification with <3% CAGR is contradictory; maturity-stage classification with 25% CAGR is contradictory. Flag mismatches as Gate 2 issues. If `market-sizing.md` is not present, add "size-market reconciliation deferred — market-sizing.md not present."

### 8. Append the structured `next_skills` YAML block
End the output with:

```
---
next_skills:
  - assess-moat-sources    # consumes the Power-availability menu from Step 5
  - analyze-demand    # if behavioral discontinuities flagged in Step 4
---
```

At least one skill required. Omit `analyze-demand` if no behavioral discontinuity was flagged.

### 9. Validate + write output
Run `python scripts/validate_trajectory.py --output-path <path>` — checks dual S-curve (both market AND tech assessed with named stages), ≥3 H1/H2/H3 classifications, ≥2 discontinuities with explicit year-range timing windows, Power Progression mapping (all 7 Powers covered), scenarios with ≥3 named swing variables, V/C/A/I tag coverage ≥6, `next_skills:` YAML block. Write to `working/trajectory.md` (orchestrator) or `standalone/analyze-trajectory-YYYY-MM-DD.md` (standalone).

**HTML on request (standalone only):** markdown is the default and the only format the validator and the orchestrator consume. If the user explicitly asks for an HTML version of a standalone run, then after validation passes, also render the output via the `html-output` skill and review it per `../_shared/output-conventions.md` § "HTML deliverables and quality review". Never produce HTML automatically.

## Gotchas

- **Symptom:** S-curve assessed only on market lifecycle; tech S-curve omitted or asserted as "same stage." **Cause:** drafter conflated the two. **Fix:** validator requires both assessments with named stages; a copy-paste identical assessment for both is detected.
- **Symptom:** every G3 sub-segment classified H1. **Cause:** drafter treated Three Horizons as descriptive instead of portfolio-forcing. **Fix:** validator warns on universal-H1; real industries with >0% growth always have at least one H2 or H3.
- **Symptom:** discontinuities listed as "AI will disrupt this industry soon" without timing or leading indicator. **Cause:** discontinuity-as-decoration. **Fix:** validator rejects any discontinuity without an explicit year range; "soon" / "eventually" / "in coming years" flagged.
- **Symptom:** Power Progression skipped or asserted as "all Powers available." **Cause:** drafter doesn't know Counter-Positioning windows close. **Fix:** validator requires all 7 Powers mapped to one of {open now / Year 3 / Year 5+ / closed}; universal-open fails.
- **Symptom:** bear/bull scenarios narrated as "things go worse" / "things go better" without named swing variables. **Cause:** scenario-as-adjective. **Fix:** validator requires ≥3 named swing variables, each with a falsifiable resolution criterion.
- **Symptom:** trajectory contradicts size-market growth rates (e.g., maturity stage + 25% CAGR). **Cause:** drafter didn't reconcile. **Fix:** Step 7 mandates explicit reconciliation when market-sizing.md exists.

## Rules

- Never assess only one S-curve. Both market AND tech mandatory.
- Never classify all sub-segments as H1. Three Horizons is a portfolio forcer, not a description.
- Never write "soon" / "eventually" as a discontinuity timing. Year ranges only.
- Never assert all 7 Powers as available. Power Progression closes windows over the lifecycle.
- Never produce scenarios without named, independent, falsifiable swing variables.
- Every external-state claim carries a V/C/A/I tag.
- All file reads use `encoding='utf-8'`.

## Old patterns

None yet — v1 (initial build 2026-05-18).

---
<!-- Built with Agent Engineer Master — get your own production-ready skill: www.agentengineermaster.com/skill-engineer -->

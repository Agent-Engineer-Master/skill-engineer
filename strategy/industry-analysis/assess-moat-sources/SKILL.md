---
name: assess-moat-sources
description: "Assesses which of Helmer's 7 Powers (scale economies, network economies, counter-positioning, switching costs, branding, cornered resource, process power) protect incumbents in a defined industry, how durable each is over the analysis horizon, and which Power combination the winning archetype must hold. Output: moat-sources.md with per-Power present/absent + intensity, benefit + barrier decomposition for each present Power, durability rating (erosion timeframe + vector), buildability for a new entrant or roll-up, winner-archetype Power profile, durability risks, and reconciliation against value-chain-profit-pools.md if present. Sub-skill of analyze-industry; invocable standalone. Triggers on 'assess moat for [industry]', '7 powers analysis of [industry]', 'how durable is the moat in [industry]', 'moat durability [industry]', 'will the moat hold'. Do NOT use for single-company moat (use build-company-model), customer-lock-in only (use analyze-demand), or share analysis (use map-competitive-arena)."
---

# Assess Moat Sources

For a defined industry, assess which of Helmer's 7 Powers protect incumbents (and which can be built by a new entrant), how durable each is, and what Power combination the winning archetype must hold. Output: `moat-sources.md` with per-Power assessment + durability + buildability + winner-archetype profile.

**The discipline:** moat is not a vibe. Helmer's 7 Powers is the canonical taxonomy: each Power requires a **benefit** (cash-flow improvement via higher price, lower cost, or reduced investment) AND a **barrier** (an obstacle that prevents competitors from arbitraging the benefit away). Without both, it is not a Power — it is operational excellence, branding aspiration, or wishful thinking.

**Iron rules:**
- All 7 Powers explicitly assessed (present / absent / nascent) — none silently omitted.
- For each **present** Power: explicit `benefit:` statement + `barrier:` statement. Both required.
- Durability rating per present Power: erosion timeframe (short <3y / medium 3-7y / long >7y) with named erosion vector.
- Buildability for new-entrant / roll-up archetype: per Power, can a well-resourced entrant build it within horizon? Conditions required?
- Winner-archetype Power profile: name the minimum Power combination an industry winner must hold.
- Power Progression alignment: cross-reference industry/company stage (per `analyze-trajectory` if present) — origination vs takeoff vs stability Powers.
- **Cross-reference reconciliation:** if `working/value-chain-profit-pools.md` exists, the structural protection named there MUST match this skill's dominant Power. Mismatch flagged explicitly for Gate 2.
- V/C/A/I tagging on every fact-claim per `../_shared/provenance-tagging.md`.
- 2026 vocabulary per `../_shared/2026-terminology.md` — "strategic power" not "moat" in body prose; "moat" only in shorthand.
- Append `next_skills:` YAML at end of output.

## Process

### 1. Intake
Confirm: industry slug, analysis horizon (5y / 10y default), whether a roll-up / new-entrant archetype is in scope. Read `references/seven-powers-canonical.md` for the verified Helmer definitions.

### 2. Per-Power diagnostic sweep
For each of the 7 Powers, run the diagnostic in `references/power-diagnostics.md`. Mark **present** / **absent** / **nascent** with one-line evidence. For each present Power, write paired:
- `benefit:` what does the customer/holder get (higher price extracted / lower cost / lower investment)?
- `barrier:` why specifically cannot competitors replicate this within the horizon?

Both lines required. Missing either = not a Power.

### 3. Durability assessment
For each present Power, rate erosion timeframe per `references/durability-assessment.md`:
- **Short (<3y):** named erosion vector active now (e.g., AI agent reducing switching costs; expiring patent; commoditising standard)
- **Medium (3-7y):** erosion vector visible but not yet binding
- **Long (>7y):** no credible erosion vector identified within horizon

Name the erosion vector specifically. "Will erode eventually" is not an assessment.

### 4. Buildability for new entrant / roll-up
For each Power, per `references/buildability-assessment.md`, answer: can a well-resourced new entrant or roll-up platform build this Power within the horizon? Required conditions? Capital? Time?

This is the load-bearing output for the orchestrator's "roll-up archetype" questions.

### 5. Winner-archetype Power profile
Name the minimum Power combination the industry winner must hold. Be specific: not "scale + network" but "MES-scale in distribution + 2-sided network economies between buyer and seller". Reference Power Progression: which Powers are available at the current S-curve stage of the industry?

### 6. Cross-reference reconciliation
If `working/value-chain-profit-pools.md` exists:
1. Read the structural-protection statement for the highest-EBIT stage.
2. Compare to the dominant Power identified in step 5.
3. Write a `## Cross-reference reconciliation` section that explicitly:
   - Quotes the value-chain-profit-pools Power name.
   - States this skill's dominant Power name.
   - Concludes: `MATCH` / `MISMATCH — flag for Gate 2`.
4. If MISMATCH, do NOT silently override either skill. Surface the contradiction with the candidate resolution (which is more likely correct + why).

If `working/five-forces.md` exists, also cross-reference: the governing force should be consistent with the dominant Power (e.g., high buyer power is inconsistent with strong switching-costs Power on the seller side).

### 7. Named durability risks
List the top 3 risks that could erode the winner-archetype's Power combination within horizon. Each risk: trigger event + estimated probability band + estimated impact. AI as a force is explicitly considered per `references/seven-powers-canonical.md` "AI impact" section.

### 8. Validate + write output
Run `python scripts/validate_moat.py --output-path <path>`. Write to `working/moat-sources.md` (orchestrator) or `standalone/assess-moat-sources-YYYY-MM-DD.md` (standalone).

**HTML on request (standalone only):** markdown is the default and the only format the validator and the orchestrator consume. If the user explicitly asks for an HTML version of a standalone run, then after validation passes, also render the output via the `html-output` skill and review it per `../_shared/output-conventions.md` § "HTML deliverables and quality review". Never produce HTML automatically.

### 9. Append `next_skills:` YAML
At end of file. Example:

```
---
next_skills:
  - analyze-trajectory       # confirm Power Progression matches S-curve stage
  - map-competitive-arena    # identify which players hold which Powers
---
```

## Gotchas

- **Symptom:** Power named without benefit + barrier decomposition. **Cause:** writer asserted "scale economies" without specifying MES or the cost penalty for sub-scale players. **Fix:** validator rejects any present-Power assertion without both `benefit:` and `barrier:` lines.
- **Symptom:** "first-mover advantage" listed as a Power. **Cause:** position confused with structure. **Fix:** first-mover is durable only if it enabled a named Power (network economies, cornered resource). Validator rejects standalone.
- **Symptom:** "operational excellence" / "execution" labelled as Process Power. **Cause:** symptom confused with structure. **Fix:** Process Power requires multi-year compounding AND evidence that competitors who poached senior leaders could not replicate. Validator rejects "operational excellence" / "execution" alone.
- **Symptom:** only 3-4 Powers discussed; remainder silently omitted. **Cause:** writer focused on present Powers and skipped absent ones. **Fix:** validator counts explicit assessments for all 7 Powers (present OR absent OR nascent).
- **Symptom:** durability rated "long" with no erosion vector named. **Cause:** assumed permanence. **Fix:** validator requires an erosion vector phrase for every present Power, even if rated long.
- **Symptom:** value-chain-profit-pools.md says "branding" protects the highest pool, but moat-sources.md names "switching costs" as dominant. **Cause:** sub-skills written independently. **Fix:** step 6 reconciliation required; mismatch blocks Gate 2.
- **Symptom:** AI dismissed in one sentence. **Cause:** under-engagement with the strongest current erosion vector for 2026-era assessments. **Fix:** named-risks section must explicitly consider AI's effect on Switching Costs, Branding, and Scale Economies per `references/seven-powers-canonical.md`.

## Rules

- Never name a Power without explicit benefit + barrier.
- Never silently omit a Power — all 7 receive an explicit assessment.
- Never label "first-mover" / "differentiation" / "execution" / "expertise" / "relationships" / "quality" / "complexity" / "adds value" / "is critical" as a Power.
- Never declare a Power durable without naming the erosion vector being assessed against.
- Never override `value-chain-profit-pools.md` silently — mismatches surfaced explicitly.
- Every fact-claim carries a V/C/A/I tag.
- All file reads use `encoding='utf-8'`.

## Old patterns
v1.0 (2026-05-18) initial build. Canonical 7 Powers verified against Helmer (2016) + 2024-26 commentary including Strategy Capital posts and the Lenny's Newsletter interview on AI impact. Built as Phase 2 sub-skill of `analyze-industry` with explicit Gate 2 reconciliation against `map-value-chain-profit-pools.md`. Inherits `_shared/provenance-tagging.md` + `_shared/2026-terminology.md`.

---
<!-- Built with Agent Engineer Master — get your own production-ready skill: www.agentengineermaster.com/skill-engineer -->

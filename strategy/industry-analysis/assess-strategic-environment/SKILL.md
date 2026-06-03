---
name: assess-strategic-environment
description: "Diagnoses competitive environment for an industry using BCG's Strategy Palette (Reeves) — Classical / Adaptive / Visionary / Shaping / Renewal — via the three-question discipline (predictability, malleability, harshness). Output: strategic-environment.md classifying the environment, evidencing the 3 dimensions with V/C/A/I tags, flagging ambidexterity, emitting a sub-skill routing matrix that weights Phase 1+2 sub-skills heavy/light/skip. Sub-skill of analyze-industry, invocable standalone. Runs FIRST in orchestrator chain — wrong diagnosis = wrong toolkit. Triggers on 'diagnose strategic environment for [industry]', 'strategy palette for [industry]', 'is [industry] classical or adaptive', 'classify the [industry] environment', 'Reeves environment for [industry]'. Do NOT activate for industry-attractiveness (use map-five-forces), market sizing (use size-market), single-company moat work (use assess-moat-sources), or DTC category go/no-go (use assess-category)."
---

# Assess Strategic Environment

For a defined industry, diagnose the competitive environment type using BCG's Strategy Palette. Output: `strategic-environment.md` naming the environment in one causal sentence, evidencing the three diagnostic dimensions, flagging ambidexterity where present, and emitting a routing matrix that downstream sub-skills consume.

**The discipline:** Wrong environment diagnosis = wrong toolkit = useless output. A Classical analysis of an Adaptive industry produces a five-year plan that won't survive contact with reality. An Adaptive analysis of a Classical industry produces overcautious wait-and-see recommendations. This skill runs FIRST in the orchestrator chain.

**Iron rules:**
- Every dimension assessment carries V/C/A/I-tagged evidence — see `../_shared/provenance-tagging.md`.
- The classification named in one causal sentence ("Industrial robotics is Adaptive because trajectory is unforecastable beyond 18 months [C: ...], no single player can shape the standards landscape [C: ...], and demand is not in survival-mode [V: ...].").
- Three diagnostic dimensions independently assessed: predictability, malleability, harshness — none skipped, none collapsed.
- Routing matrix included — names Phase 1+2 sub-skills with heavy / light / skip designation per the diagnosed environment.
- 2026 terminology only — see `../_shared/2026-terminology.md`.
- Ambidexterity flagged when the industry genuinely spans two environments (different layers, geos, or customer segments).

## Process

### 1. Intake
Confirm: industry slug, geographic scope (if relevant — the same industry can sit in different environments in different geos), focal layer (optional but recommended for multi-layer industries — see Five Forces focal-layer discipline). Read `references/strategy-palette.md` for the framework refresher and `references/diagnostic-questions.md` for the three-question discipline with per-environment anchors.

### 2. Assess predictability
Can the trajectory be reliably forecast over a 3-5 year horizon? Rate **High / Medium / Low**. Evidence anchors (see `references/diagnostic-questions.md`):
- Demand volatility (5yr coefficient of variation)
- Technology stability vs disruption cadence
- Regulatory cliffs / known mandates
- Number of viable strategic scenarios on a 5yr view

Write 2-3 sentences with ≥1 V/C/A/I-tagged evidence claim. Never assert High predictability for a market with active AI-native disruption.

### 3. Assess malleability
Can a single player (or coalition) materially shape the industry's structure or rules? Rate **High / Medium / Low**. Evidence anchors:
- Existence of platform dynamics / network effects
- Concentration — is there an actor with >25% share or de-facto standards power?
- Regulatory openness — is the rulebook negotiable?
- Active shaping moves visible (consortia, standards bodies, ecosystem investments)

Write 2-3 sentences with ≥1 V/C/A/I-tagged evidence claim. Default to Low unless there is named evidence of shaping power — Visionary and Shaping classifications require positive evidence.

### 4. Assess harshness
Is the industry in a survival-mode constrained environment (capital scarcity, regulatory cliff, demand collapse, cost-curve collapse)? Rate **High / Medium / Low**. Evidence anchors:
- Sustained negative growth (-3pp or worse, 2+ years)
- Capital markets closed to the sector (no funding rounds, debt repricings, bankruptcy waves)
- Existential regulatory event (ban, mandated wind-down)
- Cost-base structurally above price (margins below cost-of-capital across the sector)

Write 2-3 sentences with ≥1 V/C/A/I-tagged evidence claim. Harshness is rare — Renewal should be called only with named evidence of at least one of these triggers.

### 5. Classify the environment
Apply the decision rule from `references/strategy-palette.md`:

| Predictable? | Malleable? | Harsh? | Environment |
|---|---|---|---|
| High | Low | Low | **Classical** |
| Low | Low | Low | **Adaptive** |
| High | High | Low | **Visionary** |
| Low | High | Low | **Shaping** |
| any | any | High | **Renewal** |

If the dimensions don't map cleanly, see `references/diagnostic-questions.md` "Edge cases" — typically the resolution is to declare ambidexterity (step 6) or restate the focal layer.

Write the classification in ONE causal sentence naming all three dimensions: "Industry X is [Environment] because [predictability evidence], [malleability evidence], and [harshness evidence]."

### 6. Ambidexterity check
Does the industry genuinely span TWO environments at different layers, geos, or customer segments? If yes, declare it: "Industry X exhibits ambidexterity — the regulated incumbent layer is Classical [evidence]; the agentic-commerce-native layer is Shaping [evidence]." Default is single-environment classification; only flag ambidexterity with named layer/segment evidence. See `references/diagnostic-questions.md` "Ambidexterity discipline."

**Orchestrator-mode signal:** when invoked by `analyze-industry`, ambidexterity in the output triggers the orchestrator's Ambidexterity Checkpoint (a hard stop where the user chooses single-focus / dual analysis / re-scope). Do NOT presume which choice the user wants — write the ambidexterity declaration clearly enough that the orchestrator's checkpoint prompt can render it directly. See `analyze-industry/references/gate-prompts.md` "Ambidexterity Checkpoint" for the prompt the orchestrator will use.

### 7. Direction of travel
Is the environment classification stable, or is the industry transitioning? Examples: Classical → Adaptive (AI disruption breaking long-run predictability); Adaptive → Renewal (capital tightening, demand collapse); Visionary → Shaping (first-mover advantage decaying as ecosystem opens). Write one sentence: "Stable" OR "Transitioning from [X] toward [Y] because [evidence]."

### 8. Emit routing matrix
Read `references/routing-matrix.md`. Produce a table mapping the diagnosed environment to weighting designations (heavy / light / skip) for each Phase 1+2 sub-skill: `size-market`, `map-five-forces`, `map-value-chain-profit-pools`, `map-competitive-arena`, `analyze-trajectory`, `assess-moat-sources`, `analyze-demand`. `map-five-forces` is never `skip` — Reeves's contention is that structural analysis is required in every environment.

### 9. Append structured `next_skills` YAML block
Because this skill runs FIRST, `next_skills:` names the Phase 1+2 sub-skills the orchestrator should dispatch next, ordered by weight (heavy-first):

```
---
next_skills:
  - size-market    # always next (calibrates dollar magnitudes)
  - map-five-forces    # always required (industry structure)
  - map-value-chain-profit-pools    # always required (profit location)
  - [heavy-weight Phase 2 skill per environment]
  - [heavy-weight Phase 2 skill per environment]
---
```

At minimum: the three Phase 1 skills plus the environment-specific heavy-weight skills from step 8.

### 10. Validate + write output
Run `python scripts/validate_environment.py --output-path <path>` — checks: classification = one of 5 named environments; 3 diagnostic dimensions each present with a tagged sentence; routing matrix present with all 7 sub-skills enumerated and weights assigned; tag coverage ≥3; `next_skills:` YAML block present with ≥3 entries; direction-of-travel statement present; ambidexterity declared OR explicitly noted as absent. Write to `working/strategic-environment.md` (orchestrator mode) or `standalone/assess-strategic-environment-YYYY-MM-DD.md` (standalone mode).

**HTML on request (standalone only):** markdown is the default and the only format the validator and the orchestrator consume. If the user explicitly asks for an HTML version of a standalone run, then after validation passes, also render the output via the `html-output` skill and review it per `../_shared/output-conventions.md` § "HTML deliverables and quality review". Never produce HTML automatically.

## Integrates with

- **`analyze-industry`** — orchestrator parent. This skill is step 2 of the orchestrator chain; its output routes all downstream sub-skill weighting.
- **`map-five-forces`** — always-run downstream. Five Forces consumes the focal-layer declaration from this skill's intake.
- **`assess-moat-sources`** *(Phase 2)* — gets heavy-weight in Visionary and Shaping environments.
- **`analyze-trajectory`** *(Phase 2)* — gets heavy-weight in Adaptive, Visionary, and (transitioning) Renewal environments.

## Gotchas

- **Symptom:** classifies every industry as Classical. **Cause:** analyst trained pre-2010, defaulting to the familiar. **Fix:** validator requires the classification be one of the five names; Classical must be supported by High-predictability AND Low-malleability AND Low-harshness with tagged evidence on each.
- **Symptom:** declares Visionary for any company with a charismatic founder pitching a big vision. **Cause:** confusing firm-level ambition with industry-level malleability. **Fix:** Visionary requires industry-level evidence that a single player has shaped (or could shape) the standards / rules — not founder rhetoric. Default malleability to Low unless evidence is named.
- **Symptom:** declares all three dimensions as "Medium" with no classification. **Cause:** drafter unwilling to take a position. **Fix:** the framework requires binary-ish calls on each dimension; "Medium" across the board fails validation. Resolve to a high/low side per dimension, or declare ambidexterity.
- **Symptom:** assesses predictability only by gut-feel ("seems uncertain"). **Cause:** skipped the evidence anchors. **Fix:** `references/diagnostic-questions.md` lists 4 anchors per dimension; each rating must cite at least one with a tag.
- **Symptom:** routing matrix absent or generic ("run all the sub-skills"). **Cause:** drafter treated the routing as decorative. **Fix:** validator requires the matrix to enumerate all 7 sub-skills with heavy/light/skip designations; `map-five-forces` must never be `skip`.
- **Symptom:** classifies a multi-layer industry (e.g., semis) as one environment. **Cause:** ignored focal-layer discipline. **Fix:** either declare focal layer at intake OR declare ambidexterity in step 6 with per-layer classifications.
- **Symptom:** calls a sector Renewal because growth slowed last quarter. **Cause:** confusing cyclical slowdown with structural harshness. **Fix:** Renewal requires sustained (2+ year) evidence of one of the named triggers — capital closed, regulatory cliff, demand collapse, cost > price.
- **Symptom:** every direction-of-travel says "Stable" across a portfolio of analyses. **Cause:** drafter treating step 7 as box-ticking. **Fix:** in 2026, AI is reshaping predictability and malleability across most industries; real industries usually have at least one dimension in motion.

## Rules

- Never default to Classical without testing all three dimensions against the named anchors.
- Never declare Visionary or Shaping without positive, tagged evidence of malleability.
- Never declare Renewal without tagged evidence of sustained harshness (one of the named triggers).
- Never produce an environment diagnosis without a routing matrix downstream sub-skills can consume.
- Every dimension assessment carries a V/C/A/I-tagged evidence claim.
- `map-five-forces` is never weighted "skip" in any environment.
- All file reads use `encoding='utf-8'`.

## Old patterns

None yet — v1 (split out from `analyze-industry/references/strategy-palette.md` on 2026-05-18 as a standalone Phase 2 sub-skill).

---
<!-- Built with Agent Engineer Master — get your own production-ready skill: www.agentengineermaster.com/skill-engineer -->

---
name: map-five-forces
description: "Produces a Porter Five Forces analysis extended with complementors (sixth force, Brandenburger/Nalebuff) and AI-as-named-force (cost-structure impact + new-entry vector + data-intermediary position) for a defined industry. Output: five-forces.md naming THE governing force that determines this industry's profit distribution in one causal sentence, plus per-force intensity assessment with V/C/A/I-tagged evidence and explicit profit-pool cross-reference. Sub-skill of analyze-industry but invocable standalone. Triggers on 'five forces analysis for [industry]', 'Porter analysis for [industry]', 'industry-structure analysis for [industry]', 'is [industry] structurally attractive'. Do NOT activate for single-company competitive positioning (use map-competitive-arena or build-company-model), market sizing (use size-market), or moat assessment of a specific company (use assess-moat-sources)."
---

# Map Five Forces

For a defined industry, produce a Porter Five Forces analysis extended with complementors (sixth force), AI-as-named-force, and an AI-reshape overlay on the classical five. Output: `five-forces.md` that names **THE governing force** that determines this industry's profit distribution.

**The discipline:** Five Forces is a hypothesis generator, not a conclusion. Every force assessment must be tested against profit pool data, carry a direction-of-travel arrow, and (in 2026) reckon with how AI reshapes it.

**Iron rules:**
- Every evidence claim carries a V/C/A/I tag — see `../_shared/provenance-tagging.md`.
- The governing force named in one causal sentence ("Buyer concentration governs this industry because three customers represent 60% of demand and have substituted on price every two years.").
- Complementors (sixth force) assessed as a named section.
- AI assessed as a named force AND inline per classical force (reshape commentary) AND summarized in the reshape matrix.
- Every force carries a direction-of-travel arrow (intensifying / stable / weakening) with velocity where non-stable.
- Focal value-chain layer specified explicitly; the same industry has different forces at different layers.
- At-a-glance heatmap mandatory near top of output.

## Process

### 1. Intake
Confirm: industry slug, geographic scope, **focal value-chain layer** (OEM / integrator / distributor / fab / fabless / IP / equipment — pick exactly one). Read `references/forces-rubric.md`. Apply the platform-industry test in `references/platform-extensions.md`; if positive, add a boundary note to the output.

### 2. Assess the five classical forces
For each force — Rivalry, Supplier Power, Buyer Power, Threat of New Entry, Threat of Substitutes — produce:
- (a) Intensity rating (Low / Moderate / High) with ≥2 supporting claims, each V/C/A/I-tagged
- (b) **Direction of travel** (intensifying ↑ / stable ↔ / weakening ↓) with velocity (slow / medium / fast) when non-stable, supported by a tagged evidence claim — see `references/dynamism.md`
- (c) One sentence on WHY this force is at this intensity (the structural reason, not the symptom)
- (d) **How AI is reshaping this force** — required inline subsection: intensifying / weakening / no material effect, with 1 tagged evidence claim when non-trivial. The word "AI" must appear within the force's section. This is primary; step 5's matrix summarizes these.
- For platform industries, apply the layer-specific adjustments in `references/platform-extensions.md` (e.g., rivalry assessed at both within-ecosystem and cross-ecosystem levels)

Read `references/forces-rubric.md` for per-force evidence anchors, "good vs bad output" exemplars, and when-it-breaks-down notes.

### 3. Assess complementors (sixth force)
Read `references/complementors.md`. Identify firms/platforms whose presence increases this industry's value. Rate complementor concentration + leverage + direction. Examples: app stores for mobile gaming, payment rails for e-commerce, certification bodies for medtech. For platform industries, complementors often co-govern — see `references/platform-extensions.md`.

### 4. Assess AI as named force
Read `references/ai-as-force.md`. Three sub-checks:
- **Cost-structure impact** — which value-chain activities does AI automate? % of cost base affected?
- **New-entry vector** — is there an AI-native competitor with no legacy cost structure? Funded? Active?
- **Data-intermediary position** — who owns the model-training data for this industry? Is that asymmetric?

If any signal is material, AI is a force; assess intensity and direction. If immaterial, state "AI not material because [reason]" — do not silently omit.

### 5. Produce the AI Reshape Matrix (summary)
Read `references/ai-as-force.md` "AI as transforming overlay" section. The per-force inline AI commentary written in step 2 is primary; this matrix is a one-table summary of what was already written, placed below the per-force assessments and the standalone AI section.

### 6. Render the heatmap (REQUIRED)
Heatmap is required — not optional. Read `assets/heatmap-template.md`. The at-a-glance heatmap (a markdown table with columns including "Force", "Intensity", "Direction", "Governs?") must appear near the top of `five-forces.md` (after the boundary note if present, before the per-force assessments). Validator fails if absent. Exactly one force flagged "yes" in the Governs? column; up to two "candidate".

### 7. Name the governing force
The single most important output. In one causal sentence, name THE force that explains why profits sit where they sit in this industry. Two forces are allowed only when they genuinely co-govern (rare); three or more = analysis failure. If the analysis cannot name one, return to step 2.

### 8. Cross-reference profit pool
If `working/value-chain-profit-pools.md` exists in the same industry folder (orchestrator mode), reconcile: does the governing force correctly predict where profits concentrate? If not, the force assessment OR the profit pool is wrong — flag for Gate 2. If the profit-pool file does not exist (standalone mode), add the explicit note "Profit-pool cross-reference deferred — value-chain-profit-pools.md not present."

### 9. Add the Helmer handoff note + structured next_skills block
Append to `five-forces.md`: "Five Forces answers where to compete (industry structure). For 'how to win in this industry' (firm-specific durable power), run `assess-moat-sources` next — Helmer's 7 Powers." This keeps the user from over-asking Five Forces to do moat work it cannot.

Also append a YAML `next_skills` block at the very end of the file (orchestrator Phase 2 reads this to automate the handoff):

```
---
next_skills:
  - assess-moat-sources    # firm-specific durable-power assessment (Helmer 7 Powers)
  - map-value-chain-profit-pools    # if profit-pool data not yet present
---
```

At least one skill is required. Omit `map-value-chain-profit-pools` if `working/value-chain-profit-pools.md` already exists.

### 10. Validate + write output
Run `python scripts/validate_forces.py --output-path <path>` — checks: all 6 forces present (5 classical + complementors), AI sub-checks present, AI reshape matrix present, inline AI-reshape commentary near each classical force, heatmap table present, governing force sentence present, focal-layer specified, direction-of-travel arrows on ≥5 forces, tag coverage ≥6, `next_skills:` YAML block at end with ≥1 skill, profit-pool cross-reference present (if file exists). Warns (non-failing) if every direction is "stable." Write to `working/five-forces.md` (orchestrator) or `standalone/map-five-forces-YYYY-MM-DD.md` (standalone).

**HTML on request (standalone only):** markdown is the default and the only format the validator and the orchestrator consume. If the user explicitly asks for an HTML version of a standalone run, then after validation passes, also render the output via the `html-output` skill and review it per `../_shared/output-conventions.md` § "HTML deliverables and quality review". Never produce HTML automatically.

## Gotchas

- **Symptom:** every force rated "Moderate" with no governing force named. **Cause:** ran as checklist; drafter unwilling to take a position. **Fix:** `validate_forces.py` requires the governing-force sentence and at least one force at High or Low intensity. Universal-Moderate outputs fail validation.
- **Symptom:** AI section says "AI will impact this industry" without specifics. **Cause:** AI-as-force treated as throwaway nod. **Fix:** AI section must answer all three sub-checks (cost-structure, new-entry, data-intermediary) with named examples and tagged evidence, OR explicitly conclude "AI not material because [reason]."
- **Symptom:** AI assessed only in its own section; the five classical forces written as if AI weren't reshaping them. **Cause:** AI treated as a sidecar instead of a cross-cutting transforming overlay. **Fix:** the AI Reshape Matrix (step 5) is mandatory; validator catches its absence. Senior reviewers in 2026 expect both the standalone AI section AND the per-force AI reshape commentary.
- **Symptom:** force intensity contradicts profit pool location (e.g., "buyer power high" but margins concentrate at the layer selling to those buyers). **Cause:** the force analysis is structurally wrong OR the profit pool is mis-mapped. **Fix:** step 8 requires explicit cross-reference and flagging at Gate 2 if contradictory.
- **Symptom:** complementors section absent or trivialized ("none material"). **Cause:** drafter unfamiliar with sixth-force framing. **Fix:** complementors required to be assessed; "none material" requires explicit justification (rare — typically only bulk commodities sold direct).
- **Symptom:** every direction-of-travel arrow says "stable." **Cause:** drafter treated trajectory as box-ticking. **Fix:** validator emits a warning; real industries always have at least one intensifying or weakening force. Re-engage the trajectory analysis per `references/dynamism.md`.
- **Symptom:** Five Forces applied to a platform industry (e.g., mobile gaming, ride-hail, cloud marketplaces) using classical boundaries; analysis reads incoherent because the same actor is supplier-and-competitor. **Cause:** missed the platform-industry detection at intake. **Fix:** apply the platform test in `references/platform-extensions.md` at intake; add a boundary note when positive.
- **Symptom:** "Semiconductors are structurally attractive because..." — analysis treats a multi-layer industry as one. **Cause:** focal-layer not specified. **Fix:** validator rejects outputs without a focal-layer declaration.

## Rules

- Never write a Five Forces analysis where every force is "Moderate."
- Never skip the governing-force sentence — it is the analytical conclusion.
- Never skip the AI-as-force assessment or the AI Reshape Matrix, even when the conclusion is "not material."
- Never omit direction-of-travel arrows; never default every arrow to "stable" without testing the alternative.
- Never produce a Five Forces output without specifying focal value-chain layer.
- Every evidence claim carries a V/C/A/I tag.
- Never answer firm-specific moat questions inside Five Forces — defer to `assess-moat-sources` (Helmer's 7 Powers).
- All file reads use `encoding='utf-8'`.

## Old patterns
None yet — v2 (refinement pass 2026-05-18). v1 → v2 added: `references/dynamism.md`, `references/platform-extensions.md`, AI reshape matrix in `references/ai-as-force.md`, `assets/heatmap-template.md`, focal-layer + direction + reshape validation, Helmer handoff note. v1 evals expanded from 3 to 9 cases.

---
<!-- Built with Agent Engineer Master — get your own production-ready skill: www.agentengineermaster.com/skill-engineer -->

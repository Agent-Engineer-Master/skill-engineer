# Sub-Skill Orchestration

How the orchestrator routes sub-skills based on mode + strategic environment diagnosis.

## Quick mode (Phase 1)

Always run, sequenced for dependency:

1. **`size-market`** — runs first (sizing calibrates profit-pool dollar magnitudes)
2. **`map-five-forces`** — runs in parallel with #3
3. **`map-value-chain-profit-pools`** — runs in parallel with #2, but reads `size-market` output

Parallelization: spawn #2 and #3 concurrently after #1 completes.

## Deep mode (Phase 1 + Phase 2 — full battery)

All Quick-mode sub-skills, plus all four Phase 2 sub-skills:

4. **`map-competitive-arena`** — dispatched in Deep mode; runs in parallel with #5 after Quick-mode 3 complete
5. **`analyze-trajectory`** — dispatched in Deep mode; runs in parallel with #4; reads `size-market` G3 output
6. **`assess-moat-sources`** — runs AFTER `map-five-forces` AND `map-value-chain-profit-pools` (needs both as inputs); produces cross-skill reconciliation that Gate 2 enforces
7. **`analyze-demand`** — conditional (see Conditional sub-skill rules below); when run, parallel with others

## Environment-based weighting (from strategic-environment.md)

| Environment | Heavy weight | Light weight | Skip |
|-------------|-------------|--------------|------|
| Classical | Five Forces, value chain | Trajectory, demand | — |
| Adaptive | Trajectory, demand, arena | Five Forces (still required) | — |
| Visionary | Trajectory, moat (7 Powers), demand | Five Forces (still required) | — |
| Shaping | Complementors (within Five Forces), arena, moat | Static value chain | — |
| Renewal | Profit pool (cash focus), demand | Trajectory | — |

"Heavy weight" = sub-skill gets more detailed treatment and more pages in the brief. "Light weight" = brief mentions; runs but its output gets a tight section. Five Forces is required in all environments (never skip).

## Parallel-execution contract

A sub-skill is safe to run in parallel with another iff:
- Their outputs do not reference each other in process steps
- Neither needs the other's output as input

Safe-parallel pairs:
- `map-five-forces` || `map-value-chain-profit-pools` (after `size-market`)
- `map-competitive-arena` || `analyze-trajectory` (after Quick-mode 3 complete)
- `analyze-demand` || any others (independent)
- `assess-moat-sources` must run AFTER `map-five-forces` AND `map-value-chain-profit-pools` (needs both as inputs)

## Conditional sub-skill rules

- **`analyze-demand`** — skip if all of: market is mature (>20 years), demand is stable (±2% volatility), no substitution threats flagged in Five Forces. Otherwise run.
- **`assess-strategic-environment`** — Phase 2 **BUILT** (2026-05-18). Orchestrator calls this as step 3 (AFTER Gate 1 confirms scope, BEFORE sub-skill battery). Output `working/strategic-environment.md` includes the routing matrix that drives downstream sub-skill weighting.

## Ambidexterity handling

When `working/strategic-environment.md` declares ambidexterity (industry genuinely spans two environments at different layers / geographies / customer segments), the orchestrator MUST stop at step 3a and present the Ambidexterity Checkpoint (per `references/gate-prompts.md`) to the user. The user chooses:

1. **Single-focus** — pick one layer/segment; sub-skills run once with that environment's routing
2. **Dual analysis** — sub-skills run twice (once per environment); brief produces two parallel WTP/HTW threads. ~2× time + tokens.
3. **Re-scope** — return to Gate 1 with a tighter framing

Do NOT auto-proceed. Do NOT auto-run sub-skills twice. The right choice depends on the user's actual decision question, which the orchestrator cannot infer.

## Output reconciliation

After all sub-skills complete and before Gate 2:
- Check Five Forces governing force vs profit pool location — should align
- Check sizing growth rates vs trajectory S-curve stage — should align
- Check arena classification (from sizing) vs strategic environment (from intake) — should align
- **Helmer power consistency (ACTIVE)** — the structural protection named in `value-chain-profit-pools.md` must match the dominant Power identified by `assess-moat-sources.md`. Mismatch BLOCKS Gate 2; orchestrator requires rework on the weaker sub-skill (lower V/C tag density on disputed claim) before proceeding. "Defer to next phase" is not acceptable.
- Any contradictions surface as flags in the Gate 2 prompt

## `next_skills` YAML consumption

Each sub-skill output ends with a `next_skills:` YAML block declaring recommended downstream skills (e.g., size-market emits `[map-five-forces, map-value-chain-profit-pools, analyze-trajectory]`).

After each sub-skill completes:
1. Parse the `next_skills:` block from the output file's trailing YAML
2. Add any not-yet-run, in-scope-for-current-mode skills to the orchestrator's run queue
3. Skip skills already run or out of scope (e.g., Phase 2 skills are skipped in Phase 1 with a placeholder note)

This enables dependency-driven sub-skill chaining without hardcoding the full sequence in the orchestrator. Sub-skills know who they hand off to.

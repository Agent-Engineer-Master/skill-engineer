# Lane Allocation — how much of each generation lane to run

The two generation lanes (incumbent-anchored Moves 1-7 vs first-principles Move 8 + Secrets) should not be split 50/50 by default. The right mix is a property of the industry: some industries are full of exploitable structure (fat trapped incumbents, rent-extracting intermediaries, aggregatable fragmentation), others are defined by a live capability frontier (a recent inflection, broad non-consumption, a wide-open window). The split should follow.

This file gives a **legible decision table**, not a weighted formula. A made-up scoring index would look rigorous and be arbitrary. Three structure reads + three frontier reads, each yes/no, tilt the allocation in steps. The human ratifies the proposal at Gate 2 and can override.

**This is a recommended default, not a law.** The hardcoded 50/50 it replaces was a debiasing crutch; this makes the split visible and arguable. A hard floor of ≥1 concept per lane always holds, so neither lane can silently go to zero — the original debiasing intent survives any allocation.

## When it runs

- **Computed at the start of Phase 4** (needs the Phase 1-3 dataset).
- Written to the `lane_allocation` block of `disruption-dataset.yaml` with its rationale.
- Used as the **generation budget** for Phase 4 signals and Phase 5 concepts (it replaces the old fixed ≤50% incumbent cap).
- **Ratified by the human at Gate 2.** If the human overrides, set `final_*` shares and rebalance — generate more signals/concepts for the underweighted lane (cheap) before Phase 5. If not overridden, `final_*` = `proposed_*`.

## The reads

Each is a yes/no judgment from the existing dataset. Cite the dataset path that justifies the call.

### Structure signals (favour the incumbent-anchored lane)

| # | Read | Yes when… | Dataset source |
|---|---|---|---|
| S1 | **Fat, trapped incumbent profit pools** | ≥1 incumbent has a load-bearing profit pool with named structural constraints that trap it | `incumbents[].business_model.profit_pool_source` + `structural_constraints` |
| S2 | **Rent-extracting structure** | a high-friction intermediary node OR aggregatable fragmentation (highly_fragmented / fragmented) | `value_chain.flows[].friction_level: high`, `market_structure.fragmentation` |
| S3 | **Pain concentrated in existing flows** | the top pains (score = intensity × frequency) sit *inside* an incumbent-served flow, not in non-consumption | `value_chain_pain.*.pain_points` top scores |

### Frontier signals (favour the first-principles lane)

| # | Read | Yes when… | Dataset source |
|---|---|---|---|
| F1 | **Broad non-consumption** | non-consumption spans multiple segments / exclusion types — jobs not done at all, not just done badly | `value_chain_pain.*.non_consumption` breadth |
| F2 | **Live capability frontier** | ≥2 capability seeds, OR a capability inflected in roughly the last 24 months | `enabling_conditions.capability_seeds`, `technology_unlocks[].when` |
| F3 | **Open window** | the load-bearing intersection is wide-open and in the access phase (capability newly accessible) | `enabling_conditions.intersections[].window_timing`, `.phase` |

`structure_score` = count of S1-S3 that are yes (0-3).
`frontier_score` = count of F1-F3 that are yes (0-3).

## The decision table

Map the two scores to a target **incumbent : capability** share of generated signals/concepts:

| Relationship | Incumbent : Capability | Read it as… |
|---|---|---|
| `structure_score ≥ frontier_score + 2` | **70 : 30** | structurally rich, frontier quiet — mine the existing chain, keep a capability probe |
| within 1 of each other | **50 : 50** | both live — balanced |
| `frontier_score ≥ structure_score + 2` | **30 : 70** | frontier-defined, little to attack — lead with capability-first |

Edge cases:
- **Both scores 0** (thin on both): default 50/50 and flag low confidence — the industry may be poorly characterised; consider deeper Phase 1-3 research before generating.
- **Both scores 3** (rich on both): 50/50, high confidence — genuinely a two-lane industry.

The `≥1-per-lane floor` overrides any allocation: a 70:30 or 30:70 split still ships at least one concept from the minority lane into the kept set.

## Gate 2 proposal prompt

Surface the proposal inside the Gate 2 review (HTML), and in the chat four-line prompt reference it:

> **Lane allocation (proposed):** [incumbent]% incumbent-anchored / [capability]% capability-first.
> Structure score [S/3] ([which reads fired]); frontier score [F/3] ([which reads fired]).
> Rationale: [one sentence — e.g. "Non-consumption is broad and a capability inflected in 2025, while incumbents are weak, so I'm proposing 30/70 toward capability-first."]
>
> Approve this mix, or override (e.g. "make it 50/50" / "lead incumbent"). The ≥1-per-lane floor holds either way.

## What to log

Write to `lane_allocation` in the dataset (see schema). Over many runs, tag every concept by `origin` (already required) and track per-lane hit-rate **normalised by concepts generated in that lane** (not raw count — fewer slots produce fewer winners, which would self-justify). That ledger is what eventually turns these defaults into a learned per-industry-archetype prior. Until then, this table is the prior.

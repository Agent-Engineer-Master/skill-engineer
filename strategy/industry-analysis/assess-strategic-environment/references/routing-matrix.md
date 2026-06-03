# Routing Matrix — Environment → Sub-Skill Weighting

The output of this skill drives orchestrator dispatch. Each Phase 1+2 sub-skill is assigned a weight per environment: **heavy** (deep treatment, full pages in the brief), **light** (brief mention, tight section), or **skip** (do not run — rare).

`map-five-forces` is NEVER assigned `skip` — Reeves's contention is that industry structure is always required, even where the analytical posture differs.

## The matrix

| Sub-skill | Classical | Adaptive | Visionary | Shaping | Renewal |
|-----------|-----------|----------|-----------|---------|---------|
| `size-market` (Phase 1) | heavy | heavy | heavy | heavy | heavy |
| `map-five-forces` (Phase 1) | heavy | light | light | light (complementors heavy) | light |
| `map-value-chain-profit-pools` (Phase 1) | heavy | light | light | light | heavy (cash focus) |
| `map-competitive-arena` (Phase 2) | light | heavy | light | heavy | light |
| `analyze-trajectory` (Phase 2) | light | heavy | heavy | light | light |
| `assess-moat-sources` (Phase 2) | light | light | heavy | heavy | light |
| `analyze-demand` (Phase 2) | light | heavy | heavy | light | heavy (survival demand) |

## Rationale per environment

**Classical** — predictable + non-malleable + non-harsh. Position-and-execute world. Heavy on structural analysis (Five Forces, value chain, market sizing). Trajectory and arena get light treatment because position dominates.

**Adaptive** — unpredictable + non-malleable + non-harsh. Sense-and-respond world. Heavy on trajectory, demand dynamics, and competitive arena (who is moving where). Five Forces still required but its predictive value is lower because structure shifts.

**Visionary** — predictable (the endpoint) + malleable. Envision-and-build world. Heavy on trajectory (the S-curve to ride), moat sources (the structural protection the visionary builds), and demand (the customer wave). Arena is light because the visionary is creating the arena, not navigating one.

**Shaping** — unpredictable + malleable. Orchestrate-the-ecosystem world. Heavy on competitive arena (who is shaping vs being shaped) and moat sources (platform power, network effects). Five Forces light overall BUT the complementors / sixth-force section gets heavy treatment because ecosystem partners co-govern the industry. Static value-chain less useful because the chain is being re-cut.

**Renewal** — harsh. Survive-then-grow world. Heavy on profit pools (where is the cash that funds survival?) and demand (is there a viable customer base left?). Trajectory and moat are light because they assume an indefinite future the firm may not have.

## Special directives by environment

- **Shaping** → in Five Forces, the complementors / sixth-force section is heavy-weight. Set a flag in the routing output: `complementors_emphasis: heavy`.
- **Renewal** → in profit pools, focus on cash and economic profit; revenue-only views are misleading. Set: `profit_pool_focus: cash`.
- **Visionary** → in trajectory, the S-curve stage assessment is the key output. Set: `trajectory_focus: s_curve_stage`.
- **Ambidexterity declared** → routing matrix is emitted TWICE, once per environment, scoped to the relevant layer/geo/segment.

## Output format expected by orchestrator

The routing matrix in `strategic-environment.md` must be a markdown table with rows for each sub-skill and a single column showing the weight for the diagnosed environment. The orchestrator parses this table to build its dispatch plan.

Example (for an Adaptive industry):

```markdown
## Sub-skill routing matrix (environment: Adaptive)

| Sub-skill | Weight | Notes |
|-----------|--------|-------|
| size-market | heavy | Phase 1, always required |
| map-five-forces | light | Phase 1, required but structure shifts fast |
| map-value-chain-profit-pools | light | Phase 1 |
| map-competitive-arena | heavy | Phase 2, who is moving where |
| analyze-trajectory | heavy | Phase 2, S-curve assessment central |
| assess-moat-sources | light | Phase 2 |
| analyze-demand | heavy | Phase 2, demand dynamics central |
```

All 7 sub-skills must be enumerated. Missing rows = validator failure.

# Strategic Group Map — Output Template

Include this strategic-group visualization in `competitive-arena.md`. Two acceptable formats: grid table or coordinate notation. Pick the format that best fits the axes; grid table is preferred for most cases.

## Format A — Grid table (preferred)

The grid table uses one axis as rows, the other as columns. Cells contain firm names. Cluster boundaries are indicated by the strategic-group label after the table.

```markdown
## Strategic Group Map

**Axes:** Scope (broad ↔ narrow) × Integration (full-stack ↔ specialist)
**Axis rationale:** Scope and integration are uncorrelated in this industry (broad-scope firms can be full-stack OR specialists). Both are strategic choices, not outcomes. They produce 4 discriminating clusters.

|                        | Full-stack             | Mid-integration        | Specialist           |
|------------------------|------------------------|------------------------|----------------------|
| **Broad scope**        | Firm A, Firm B         | Firm C                 | —                    |
| **Mid scope**          | Firm D                 | Firm E, Firm F         | Firm G               |
| **Narrow scope**       | —                      | Firm H                 | Firm I, Firm J, Firm K |

**Identified groups:**
- **Group 1 — Full-stack incumbents** (Firm A, Firm B): broad-scope full-stack. ~50% industry revenue.
- **Group 2 — Mid-tier integrators** (Firm C, Firm D, Firm E, Firm F): mixed posture. ~30% industry revenue.
- **Group 3 — Specialist disruptors** (Firm G, Firm I, Firm J, Firm K): narrow-scope specialists. ~15% industry revenue.
- **Group 4 — Generalist mid-tier** (Firm H): mid-scope mid-integration. ~5% industry revenue, single-firm group, watch for entry.
```

## Format B — Coordinate notation

Use when axes are continuous or when grid form would be too sparse.

```markdown
## Strategic Group Map

**Axes:** Price (premium ↔ value, X) × Service intensity (high-touch ↔ self-serve, Y)
**Axis rationale:** [why uncorrelated and discriminating]

```
Service intensity (high-touch ↑)
  │
  │ Group A: Premium concierge (Firm 1, Firm 2)        Group B: Enterprise high-touch (Firm 3)
  │     (premium price, high-touch)                        (value price, high-touch)
  │
  │ Group C: Premium self-serve (Firm 4)                Group D: Mass self-serve (Firm 5, 6, 7)
  │     (premium price, self-serve)                        (value price, self-serve)
  │
  └──────────────────────────────────────── → Price (premium ←→ value)
```
```

## Per-group profile block (required for each group)

```markdown
### Group [N] — [Strategic-posture name]

- **Members:** Firm A, Firm B, Firm C [V/C/A/I tag if needed]
- **Estimated size:** ~X% of industry revenue [C: source 2026]
- **Basis of competition:** [scale / brand / channel access / data depth / capability / etc.]
- **Typical profitability:** [high / moderate / low] — [reasoning] [C: source]
- **Trajectory:** [growing / stable / shrinking] as % of industry — [reasoning]
- **Winner archetype:** [consolidator / innovator-specialist / platform-orchestrator / vertically-integrated / asset-light / none-emerging]
- **Archetype reasoning:** [one sentence on why this archetype fits group leaders]
```

## Mobility-barrier matrix (required)

```markdown
## Mobility Barriers

| From \ To       | Group 1 | Group 2 | Group 3 |
|-----------------|---------|---------|---------|
| **Group 1**     | —       | scale + brand | data flywheel + ecosystem position |
| **Group 2**     | switching costs | — | cornered talent |
| **Group 3**     | channel access | capability stack | — |

### Adjacent-pair elaboration

**Group 1 → Group 2** (scale + brand): Group 1 incumbents would need to shed scale and re-brand as mid-tier — typically value-destructive. Failed attempt: [example firm and outcome, tagged]. Barrier direction: stable.

**Group 2 → Group 3** (cornered talent): Group 3 specialists hire from a narrow talent pool (e.g., domain PhDs); Group 2 mid-tier firms cannot hire at the depth required. Barrier direction: stable.

**Group 3 → Group 1** (channel access): Group 3 specialists lack the channel relationships Group 1 incumbents have locked in; reaching Group 1's customer base requires either acquisition (rare due to size mismatch) or 5+ years of channel-build.
```

## Arenas overlay block (when applicable)

```markdown
## Arenas Overlay

- **Market classification:** Arena [C: size-market output 2026-MM-DD]
- **Expected group-structure signature:** 4-7 groups, active mobility, multiple co-existing winner archetypes
- **Observed vs expected:** observed 4 groups, mobility active (2 recent repositioning attempts), multiple archetypes (consolidator + specialist + platform orchestrator co-exist). Matches signature.
- **"Redefining the arena" call:** Group 3 (specialists) is positioned to redefine the arena — Helmer Cornered Resource + Counter-Positioning combo against Group 1's scale moat.
- **Eroding mobility barriers:** channel access (D2C disintermediation, eroding fast); data flywheel (open-source training data, eroding medium).
- **McKinsey arena mapping:** AI software & services.
```

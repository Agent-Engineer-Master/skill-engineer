# BCG Strategy Palette — Environment Diagnosis

Source: Martin Reeves, *Your Strategy Needs a Strategy* (BCG / HBR Press).

Before running the analytical battery, diagnose the competitive environment. Wrong environment diagnosis = wrong toolkit = useless output. This is the orchestrator's first analytical call.

## The three diagnostic questions

For the target industry:

1. **Predictability** — can the trajectory be reliably forecast over a 3-5 year horizon?
2. **Malleability** — can a single player (or coalition) materially shape the industry's structure or rules?
3. **Harshness** — is the industry in a survival-mode constrained environment (capital scarcity, regulatory cliff, demand collapse)?

## The five environments

| Environment | Predictable? | Malleable? | Harsh? | Strategic posture | Analytical priority |
|------------|--------------|-----------|--------|------------------|---------------------|
| **Classical** | Yes | No | No | Plan and execute | Five Forces + value chain + market sizing (heavy) |
| **Adaptive** | No | No | No | Iterate fast, sense and respond | Trajectory + demand + arena (Five Forces secondary) |
| **Visionary** | Yes | Yes | No | Envision and build | Trajectory + moat (7 Powers heavy) + ecosystem |
| **Shaping** | No | Yes | No | Coordinate ecosystem | Complementors + platform analysis + arena |
| **Renewal** | — | — | Yes | Survive then grow | Profit pool (cash) + cost-curve + demand survival |

## Diagnosis output

Write to `working/strategic-environment.md`:

```markdown
---
industry: [slug]
environment: [Classical | Adaptive | Visionary | Shaping | Renewal]
date: YYYY-MM-DD
---

# Strategic Environment Diagnosis

## Predictability: [High | Medium | Low]
[2-3 sentence reasoning with V/C/A/I tags]

## Malleability: [High | Medium | Low]
[2-3 sentence reasoning with V/C/A/I tags]

## Harshness: [High | Medium | Low]
[2-3 sentence reasoning with V/C/A/I tags]

## Environment classification: [name]
[Single paragraph: why this classification, and what it implies for the sub-skill battery and weighting.]

## Sub-skill routing implications
- [skill]: [run / skip / de-emphasize / heavy-weight]
- ...
```

## Anti-patterns

- ❌ Skipping diagnosis and defaulting to Classical (the default of most analysts trained pre-2010)
- ❌ Classifying a digital platform industry as Classical (almost always Shaping or Adaptive)
- ❌ Classifying any industry as Renewal without explicit harshness evidence (rare classification)

## Why this matters

Industrial robotics in 2026 is Adaptive (uncertain trajectory, no single shaper) — running a Classical analysis produces a beautiful five-year plan that won't survive contact with reality. Industrial gases is Classical (stable, predictable, mature) — running an Adaptive analysis produces overcautious wait-and-see recommendations. Diagnosis routes the toolkit.

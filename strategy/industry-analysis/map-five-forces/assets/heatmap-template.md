# Five Forces Heatmap — Output Template

Include this heatmap inline near the top of `five-forces.md` (after the boundary note, before the per-force assessments). It gives a senior reviewer a 10-second read of where the analysis lands.

## Template

```markdown
## At-a-glance — Force Heatmap

| Force | Intensity | Direction | Velocity | AI reshape | Governs? |
|-------|-----------|-----------|----------|------------|----------|
| Rivalry | Low / Mod / **High** | ↑ / ↔ / ↓ | slow / med / fast | ↑ / ↔ / ↓ / n/a | yes / no |
| Supplier Power | Low / Mod / High | ↑ / ↔ / ↓ | slow / med / fast | ↑ / ↔ / ↓ / n/a | yes / no |
| Buyer Power | Low / Mod / High | ↑ / ↔ / ↓ | slow / med / fast | ↑ / ↔ / ↓ / n/a | yes / no |
| Threat of New Entry | Low / Mod / High | ↑ / ↔ / ↓ | slow / med / fast | ↑ / ↔ / ↓ / n/a | yes / no |
| Threat of Substitutes | Low / Mod / High | ↑ / ↔ / ↓ | slow / med / fast | ↑ / ↔ / ↓ / n/a | yes / no |
| Complementors (6th) | Low / Mod / High | ↑ / ↔ / ↓ | slow / med / fast | ↑ / ↔ / ↓ / n/a | yes / no |
| AI (named force) | Low / Mod / High | ↑ / ↔ / ↓ | slow / med / fast | — | yes / no |

**Governing force:** [name] — see causal sentence below.
```

## Filled exemplar — US ambient-scribe medtech (illustrative)

```markdown
## At-a-glance — Force Heatmap

| Force | Intensity | Direction | Velocity | AI reshape | Governs? |
|-------|-----------|-----------|----------|------------|----------|
| Rivalry | High | ↑ | fast | ↑ | no |
| Supplier Power | Low | ↔ | slow | ↓ | no |
| Buyer Power | High | ↑ | medium | ↑ | candidate |
| Threat of New Entry | High | ↑ | fast | ↑ | **yes** |
| Threat of Substitutes | Moderate | ↑ | medium | ↑ | no |
| Complementors (6th) | High | ↔ | slow | ↔ | candidate |
| AI (named force) | High | ↑ | fast | — | structurally cross-cutting |

**Governing force:** Threat of new entry — AI-native vendors with EHR-app-store distribution achieve clinical-grade product at 1/5 the per-encounter cost basis of legacy transcription incumbents.
```

## Rules for the heatmap

- One word per cell — no prose.
- "Governs?" column has exactly one **yes**; up to two "candidate"; rest "no". If two yes, the analysis hasn't resolved.
- "AI reshape" column for the AI named-force row is "—" (not applicable; covered in the cross-cutting Reshape Matrix lower in the document).
- Velocity column required for any force with direction ≠ stable. Optional but recommended for stable forces.
- The heatmap is a summary, not a substitute — every cell must be backed by the corresponding force section's detailed analysis.

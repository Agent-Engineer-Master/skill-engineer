# Strategic Groups — Methodology and 2-Axis Selection

Porter (1980) introduced strategic groups as clusters of firms within an industry that pursue similar strategies — i.e., make similar strategic-choice variables (scope, integration, channel, asset model). Competition is more intense within-group than across-group; profitability differences across groups can persist for decades.

## The 3-test rubric for axis selection

Before plotting, every candidate axis pair must pass:

1. **Discriminating** — placing the industry's known firms on the axes produces ≥3 visibly distinct clusters. If firms scatter randomly, or collapse onto one cell, the axes don't discriminate. Re-pick.
2. **Uncorrelated** — the two axes capture independent strategic dimensions. "Price" and "quality" usually move together (premium players are high-quality) — picking both gives you one dimension twice and yields a diagonal, not clusters.
3. **Choice-based, not outcome-based** — axes must be strategic decisions firms made: scope, integration, channel, asset model, geographic reach. Outcomes — market share, profitability, growth rate — are CONSEQUENCES of strategy, not the strategy itself. Using them as axes makes the analysis circular.

## Default candidate axes

Pick the pair that best discriminates THIS industry from this list:

| Axis | Range | When to use |
|------|-------|-------------|
| **Scope** | broad ↔ narrow | Most industries — strong discriminator |
| **Integration** | full-stack ↔ specialist | Tech, healthcare, manufacturing |
| **Price** | premium ↔ value | Consumer, retail, hospitality |
| **Service intensity** | high-touch ↔ self-serve | SaaS, services, B2B |
| **Channel** | direct ↔ indirect (partner) | B2B software, industrial |
| **Geographic reach** | global ↔ regional ↔ local | Logistics, retail, professional services |
| **Asset model** | asset-heavy ↔ asset-light | Hospitality, transport, infrastructure |
| **Customer segment** | enterprise ↔ SMB ↔ consumer | Software, financial services |
| **Data position** | data-rich ↔ data-poor | AI-reshaped industries (2024+ addition) |
| **Power profile** | Helmer-power-A ↔ Helmer-power-B | Tech / platform industries |

## Common axis pairings that work

- Scope × Integration — most general-purpose pair
- Price × Service intensity — services and SaaS
- Channel × Customer segment — B2B
- Asset model × Geographic reach — transport, hospitality
- Data position × Integration — AI-native industries
- Scope × Price — consumer retail (classic Porter pair)

## Common axis pairings that fail

- **Price × Quality** — correlated. Premium players are higher-quality. You get a diagonal.
- **Size × Profitability** — both are outcomes. Circular.
- **Innovation × Quality** — too abstract; not strategic choices.
- **Growth × Share** — outcomes; tells you what happened, not how firms compete.

## The 5-step process (Porter, with 2026 overlays)

1. **Define the industry** — boundary, geographic scope, focal value-chain layer.
2. **Identify strategic-choice variables that distinguish firms** — brainstorm 5-8 candidates; pick the most discriminating pair.
3. **Place named firms on the map** — ≥10 firms ideally; ≥6 minimum to discriminate.
4. **Draw cluster boundaries** — circles around firms that occupy similar coordinates. Cluster size on the visualization can encode group's share of industry revenue.
5. **Interpret the map** — per-group basis of competition, profitability, mobility barriers (covered in `mobility-barriers.md`), winner archetypes (covered in `winner-archetypes.md`).

## When the map "fails"

| Failure | Diagnosis | Fix |
|---------|-----------|-----|
| Firms scattered randomly | Axes don't discriminate | Re-pick axes |
| Diagonal (firms on a 45° line) | Axes correlated | Re-pick one axis to make it orthogonal |
| Single cluster | Axes don't discriminate OR industry is homogeneous | Re-axis first; if same result, flag as homogeneous (rare) |
| 2 clusters | Axes only capture one dimension | Add or swap to a second uncorrelated axis |
| ≥6 clusters | Industry is fragmented or axes too granular | Coarsen the axes (e.g., 3-level scale instead of 5-level) |

## Group naming convention

- Label groups by **strategic posture**, not by tier or ownership.
- ✅ "Full-stack premium enterprise vendors"
- ✅ "Asset-light SMB self-serve specialists"
- ✅ "Regional vertically-integrated commodity players"
- ❌ "The big guys"
- ❌ "Incumbents"
- ❌ "Tier 1"

The group name must convey strategic choice on the two axes plus the basis of competition.

## Industry-evolution note

Strategic groups are not permanent. Groups split, merge, or new ones emerge in response to:
- Technology shifts (AI, platform economics)
- Regulatory changes
- Consolidation waves (M&A reduces group count)
- Disruption (new entrants form new groups outside existing axes)

When analyzing an industry in active disruption, the map captures TODAY'S structure; flag the trajectory of group counts and mobility barriers in the output.

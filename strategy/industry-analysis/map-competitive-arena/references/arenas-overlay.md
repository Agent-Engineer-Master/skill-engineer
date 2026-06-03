# Arenas Overlay

When the upstream `size-market` arenas screen has classified the market, the strategic-group map gets richer if cross-referenced with the McKinsey Arenas-of-Competition framing. This reference is the integration layer.

## What size-market's arenas-screen produces

`size-market/references/arenas-screen.md` classifies the WHOLE market as one of:

| Classification | Criteria | Group-structure signature |
|---|---|---|
| **Arena** | >10% CAGR AND top-5 share movement >5pp / 5yr | 4-7 groups, active mobility, multiple co-existing winners |
| **Pre-arena** | High growth, low share movement (still early) | 2-3 groups, one likely dominant, group definition still forming |
| **Mature** | <10% CAGR, low share movement | 3-4 stable groups, high mobility barriers, dominant archetype per group |
| **Contested mature** | <10% CAGR, high share movement (>5pp) | 3-4 groups but barriers eroding, repositioning attempts active |
| **Declining** | Negative growth | 1-2 groups consolidating; M&A common; sole-survivor dynamics |

This skill (`map-competitive-arena`) goes one level deeper — it maps groups WITHIN the market and applies the classification's signature.

## Per-classification overlay actions

### Arena
- Expect 4-7 strategic groups (more than mature).
- Identify which group is positioned to "redefine the arena" — usually one with a Helmer Scale Economies + Cornered Resource combo, or a platform orchestrator that's still subsidizing one side.
- Flag mobility barriers that are eroding fastest (Arena dynamics specifically erode barriers).
- Name the McKinsey arena if the industry maps to one of the 12 current or 18 future arenas (AI software, autonomous mobility, cybersecurity, climate tech, batteries, biotech, etc.).
- Expect multiple winner archetypes co-existing — specialists AND platform orchestrators winning simultaneously in different groups.

### Pre-arena
- Expect 2-3 groups; one likely dominant by sheer first-mover share.
- Group definitions may still be forming — flag axis-selection sensitivity (different axes give different group structures, which is itself a signal).
- Winner archetype often "none emerging" yet — multiple firms trying multiple models.
- Note the trajectory: which group is likely to consolidate to Arena status (high growth materializing) vs Mature (growth caps).

### Mature
- Expect 3-4 stable groups with strong mobility barriers.
- Dominant archetype per group is usually entrenched (consolidator at low end, asset-light or vertically-integrated at premium).
- Group count rarely changes; M&A within groups (consolidation), not across.
- Skip the "redefining the arena" call; mature markets are not being redefined.

### Contested mature
- Expect 3-4 groups, same as mature — but mobility barriers eroding.
- Active repositioning attempts: name firms attempting to climb groups (success or failure tells you barrier strength).
- Often signals incoming disruption — note the disruption vector (tech, regulatory, channel).
- Winner archetypes may shift; consolidator may give way to platform orchestrator as data/network effects emerge.

### Declining
- Expect 1-2 groups, consolidating.
- M&A common; sole-survivor dynamics; "last firm standing" plays.
- Winner archetype usually consolidator OR asset-light operator (capital-efficient run-off).
- Mobility barriers may invert — barrier to ENTERING the declining industry becomes high (no one wants in); barrier to exiting low.

## The 12 current McKinsey arenas (as of 2024 publication)

If the industry maps to one of these, name it explicitly in output:

1. AI software & services
2. Cybersecurity
3. Climate & decarbonization tech
4. Electric vehicles
5. Batteries & energy storage
6. Semiconductors (frontier nodes)
7. Streaming & digital media
8. Modern logistics & supply chain
9. Cloud infrastructure & platforms
10. Future of mobility (autonomous, urban air)
11. Biotech (cell + gene therapy, AI-discovery)
12. Space economy

## 18 future arenas (forward-looking, 2030-2040)

Include if industry is plausibly an emergent McKinsey arena: synthetic biology, fusion energy, quantum computing, advanced materials, longevity medicine, etc. (See McKinsey "Arenas of Competition" 2024 source.)

## When to skip the overlay

If market is Mature or Declining AND there is no plausible Arena trajectory, the overlay adds little. State explicitly in output:

> "Arenas overlay not applicable — market classified Mature with no Arena-trajectory signal. Group structure stable, mobility barriers high, no McKinsey-arena mapping."

## Output integration

Add a section in `competitive-arena.md` titled "Arenas overlay" after the per-group profiles and winner archetypes. Structure:

1. Market classification (from upstream sizing or intake): [Arena / Pre-arena / etc.]
2. Expected group-structure signature for this classification: [from table above]
3. Observed vs expected: does this industry's structure match the expected signature?
4. "Redefining the arena" call: which group is positioned to do so (Arena/Pre-arena only)
5. Eroding mobility barriers (Arena/Contested mature only)
6. McKinsey arena mapping: [named arena, or "not on McKinsey's list"]

Tag observations V/C/A/I per usual.

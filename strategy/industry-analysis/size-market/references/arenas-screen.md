# Arenas Qualification Screen

Source: McKinsey Global Institute, *The Next Big Arenas of Competition*, October 2024 — relaunch of the 2008 "arenas" concept (Bryan/Joyce). MGI identified 12 current arenas (analysis window 2005-2020) and 18 future arenas (projection to 2040, estimated $29-48T revenue / $2-6T profit, rising from 4% to 10-16% of global GDP).

## McKinsey's qualitative definition

An arena is a market with **both**:

1. **Outsize growth** — captures a disproportionate share of the economy's expansion.
2. **Outsize dynamism** — high "shuffle rate": top-player market share changes hands materially over the window.

McKinsey does not publish operational thresholds. The below are **our operational interpretations** for PE-CDD speed, designed to match the empirical pattern in the 12 identified arenas.

## Operational screen (our interpretation)

A market qualifies as an **arena** if it satisfies BOTH:

1. **High growth** — sub-segment 5yr forward CAGR >10%.
2. **High dynamism** — sum of top-5 player share movements >5 percentage points over trailing 5yr window (the "shuffle rate" proxy).

Both metrics must be defended with the same V/C/A/I provenance discipline as the sizing.

## Classifications

| Classification | Growth (5yr fwd CAGR) | Dynamism (top-5 5yr Δ) | Strategic implication |
|---------------|----------------------|------------------------|----------------------|
| **Arena** | >10% | >5pp | Active land-grab; structural positions are being formed. High-stakes but high-reward. Map to Shaping or Adaptive environment in `_shared/`. |
| **Pre-arena** | >10% | <5pp (yet) | Growth attracting attention; dynamism may emerge as incumbents are displaced. Watch for AI-native entrants. |
| **Mature** | 2-10% | <5pp | Stable structure; advantage from operational excellence + adjacency expansion. Classical environment. |
| **Contested mature** | 2-10% | >5pp | Stable size but active disruption. Often signals upcoming arena status (incumbent restructuring) or terminal decline. |
| **Declining** | <2% or negative | varies | Profit pool shrinking. Consolidation or harvest plays only. |

## Reference: the 12 current arenas (McKinsey 2024)

Software, semiconductors, consumer internet, e-commerce, consumer electronics, biopharmaceuticals, industrial electronics, payments, video and audio entertainment, cloud services, electric vehicles, information-enabled business services.

## Reference: the 18 future arenas (McKinsey 2024, through 2040)

- **Continuing** (mature arenas with continued dynamism): e-commerce, electric vehicles, cloud services, semiconductors.
- **Spin-off** (sub-segments breaking out of existing arenas): AI software and services, digital ads, streaming.
- **Emergent** (new arena formation): shared autonomous vehicles, space, cybersecurity, batteries, video games, robotics, industrial and consumer biotechnology, modular construction, nuclear fission power plants, future air mobility, GLP-1 obesity drugs.

If the industry being sized maps to one of these, state it and inherit the McKinsey arena thesis as initial hypothesis (still validate with the two-axis test on your specific G3 cut).

## How to gather inputs

**For growth rate:** use the G3 decomposition output from the sizing exercise (must already exist). Use sub-segment-weighted CAGR, not aggregate.

**For top-5 share movement:** sources include:
- Trade-body market share data (often published annually — IFR for robotics, SEMI for semis).
- Analyst notes that publish share tables (Bernstein and Morgan Stanley do this for many sectors).
- Public company filings + private-company estimates triangulated.
- IBISWorld competitor profiles (lists top 4-5 with revenue estimates).

If primary share data is unavailable, compute share movement from listed-comparable revenue growth differential vs total market growth: |share_t1 - share_t0| summed across top 5. Tag as `[I: derived from comparable revenue analysis, 5yr window]`.

**Minimum acceptable evidence:** at least one named share data point with a year. Stating "share is shifting rapidly" without a number fails validation.

## Output

A single section in `market-sizing.md`:

```markdown
## Arenas Qualification

**Classification:** [Arena | Pre-arena | Mature | Contested mature | Declining]

**Growth rate (5yr forward CAGR):** X% [V/C/A/I: source-name + year + section]
**Top-5 share movement (trailing 5yr, sum of absolute Δ):** Y pp [V/C/A/I: source-name + year]
**Maps to McKinsey 2024 arena?** [Yes — name the arena | No | Adjacent to — name]

**Implication:** [one sentence on what this classification means for strategic posture — competitive intensity, expected ROI on share investment, time-window for positioning]
```

## Why this matters

The 2024 McKinsey arena revival exists because the standard "industry attractiveness" frame (Porter Five Forces snapshot) fails in markets where structure is actively shifting. A 2010 mobile gaming Five Forces analysis would have called it "moderate rivalry" — but the share dynamism was off the charts and incumbents (Zynga, EA) were being unseated. The arena screen catches that early.

Pair the classification with the strategic environment diagnosis (`strategy-palette.md` if available in orchestrator context): Arenas usually map to Adaptive or Shaping environments; Mature usually maps to Classical.

## Common failure modes

1. **Skipping the share-shift measurement** — asserting "Arena" because growth is high. Both conditions required.
2. **Aggregate share movement only** — using total market churn instead of top-5. Top-5 is the McKinsey definition.
3. **Single year share data** — needs a multi-year window (5yr is the convention; 3yr acceptable if data thin).
4. **Confusing fast growth with arena status** — high-growth mature markets exist (commodity expansion). The dynamism criterion is the discriminator.
5. **Ignoring McKinsey's published 18 future arenas** — if your industry is on the list, that's strong corroboration; not naming it is a missed signal.

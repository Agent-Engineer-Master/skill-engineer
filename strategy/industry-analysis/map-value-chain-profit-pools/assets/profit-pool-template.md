# Profit Pool Visualization Template

Copy this structure into `value-chain-profit-pools.md`. Default unit: 1 character per $0.5B EBIT — adjust scale to suit industry size (pick a unit and apply consistently).

## Profit pool by value-chain stage — DEFAULT (horizontal bar)

| Stage | Revenue ($B, range) | EBIT margin (3yr avg, %) | EBIT ($B, low–base–high) | Share of pool (%) | Profit-pool bar |
|-------|--------------------|--------------------------|--------------------------|-------------------|------------------|
| [Stage 1] | X.X–X.X | YY | Z.Z–Z.Z–Z.Z | A% | █████ |
| [Stage 2] | X.X–X.X | YY | Z.Z–Z.Z–Z.Z | A% | █ |
| [Stage 3] | X.X–X.X | YY | Z.Z–Z.Z–Z.Z | A% | ████████ |
| [Stage 4] | X.X–X.X | YY | Z.Z–Z.Z–Z.Z | A% | ██ |
| [Stage 5] | X.X–X.X | YY | Z.Z–Z.Z–Z.Z | A% | ▌ |
| **Total** | **X.X** | — | **Z.Z** | 100% | |

**Bar scale:** 1 character = $0.5B EBIT (base case)
**Profit metric used:** EBIT (or economic profit — see below if upgraded)
**Normalisation:** 3-year trailing average margin; cyclical industries 5-year. State the basis explicitly.
**Sources per row:** [V/C/A/I-tagged sources for each row's revenue and margin estimate]

## OPTIONAL — Economic profit version (when capital intensity varies materially)

Use when stage capital intensity varies >2× across the chain. See `references/economic-profit.md`.

| Stage | NOPAT ($B) | Capital employed ($B) | Stage WACC (%) | Economic profit ($B) | EP-pool bar |
|-------|-----------|----------------------|----------------|----------------------|-------------|
| [Stage 1] | Z.Z | X.X | YY | E.E | █████ |
| [Stage 2] | Z.Z | X.X | YY | E.E | █ |
| **Total** | Z.Z | X.X | — | E.E | |

**WACC source per stage:** [tag]
**Capital-employed source per stage:** [tag]

## OPTIONAL — Bain "river" chart (executive summary)

For executive presentations, a two-axis river chart makes the revenue-vs-profit inversion visceral:

- **X-axis:** cumulative revenue share across the value chain (0% → 100%)
- **Y-axis:** EBIT margin %
- **Area under each block = absolute EBIT** for that stage

A stage with 5% of revenue and 35% margin shows as a tall thin block; a stage with 40% of revenue and 4% margin shows as a wide flat block. Render in markdown as a stacked block diagram or hand off to the orchestrator for graphical render.

Example schematic (text approximation):

```
Margin (%)
 35 |             ▓▓
 25 |             ▓▓
 15 |   ▓▓        ▓▓
  8 |   ▓▓  ▓▓▓▓  ▓▓  ▓▓▓▓▓▓
  4 |   ▓▓  ▓▓▓▓  ▓▓  ▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓
    +---------------------------------------
        S1   S2    S3   S4         S5
       (5%) (20%) (5%) (30%)      (40%)   ← cum revenue share
```

---

## Structural protection — concentration stage

**Stage with highest profit concentration:** [name]
**Absolute EBIT (base case):** $X.XB ([Y]% of industry pool)
**Trend (3yr direction of travel):** [growing / stable / declining]

**Structural protection (Helmer 7 Powers — name one):**
[scale economies / network economies / counter-positioning / switching costs / branding / cornered resource / process power]

**Diagnostic answers (from `references/structural-protections.md`):**
- [Per-power diagnostic question 1 and your answer]
- [Per-power diagnostic question 2 and your answer]
- [Per-power diagnostic question 3 and your answer]

**Why this protection sustains the pool (2-3 sentences, naming the specific mechanism):**
[Must name the specific mechanism. Generic "adds value", "is critical", "differentiated", "first-mover", "expertise", "relationships" do NOT qualify and will fail validation.]

**If you cannot name a structural protection:** state explicitly: "Profit concentration at [stage] is not structurally protected — expect arbitrage by [named likely entrant] within [time horizon]." This is itself a valid finding.

---

## Cross-reference to Five Forces

[If `working/five-forces.md` exists:]
**Governing force from Five Forces:** [name]
**Predicts profit concentration at:** [stage name implied by governing force]
**Observed profit concentration at:** [actual stage from this analysis]
**Reconciliation:** [aligned / contradictory + reasoning]

[If contradictory, flag for orchestrator Gate 2 review.]

---

## Methodology disclosure (mandatory footnotes)

- **Profit metric:** EBIT (or economic profit + reason for upgrade)
- **Normalisation period:** [3-year / 5-year / 12m + cyclical justification]
- **Listed comparables used per stage:** [names, n per stage]
- **Margin definition:** GAAP EBIT including stock-based compensation, excluding restructuring / impairment
- **Allocated-cost share:** [%] of total stage EBIT (>30% = low-confidence flag)
- **Geographic scope:** [region(s)]
- **Estimate vintage:** [date]

---

## Next skills (orchestrator hand-off)

Append this YAML block as the **final lines** of the file. Listing >=1 entry is required; validator fails otherwise.

```
---
next_skills:
  - assess-moat-sources    # to assess durability of the structural protection identified
  - map-five-forces        # if Five Forces not yet present, for cross-reference reconciliation
---
```

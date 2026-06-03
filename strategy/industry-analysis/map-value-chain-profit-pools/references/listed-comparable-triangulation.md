# Listed-Comparable Triangulation

The core workhorse method for estimating stage-level EBIT when an industry has no clean segment reporting. Used as standard practice in MBB strategy work and PE CDD.

## The 5-step protocol

### 1. Identify pure-play listed comparables for the stage

For each value-chain stage, find 3-5 listed companies whose business is **substantially concentrated** in that stage. Pure-plays beat diversified players — a fabless semiconductor pure-play tells you about fabless economics; a vertically-integrated player conflates stages.

Acceptance bar:
- ≥70% of the comparable's revenue comes from the target stage
- Listed (so financials are audited and comparable)
- Operating in a roughly similar geography / regulatory regime
- ≥3 years of stable history (avoid one-off restructurings)

If pure-plays do not exist (common in fragmented / private-dominated stages), fall back to **segment data from diversified players** (Method 2 below).

### 2. Pull EBIT margins with consistent definition

Standardise the EBIT definition before comparing:
- **EBIT from continuing operations**, excluding restructuring / impairment / non-recurring items
- After **stock-based compensation** (SBC) — this is real economic cost, do not let tech filings hide it as "adjusted EBIT"
- Before financing items and tax

Pull 3-year average (or 5-year if cyclical) — single-year prints are noisy.

### 3. Compute the stage median margin

Median, not mean, to dampen outlier effects. Document the range (low / median / high) and disclose dispersion. A tight range (±200 bps) is high-confidence; a wide range (±800 bps) means the "stage" is not actually one stage and needs sub-segmentation.

### 4. Multiply by estimated stage revenue

Stage revenue = industry total revenue × stage's share of value capture.

Stage revenue itself is an estimate — sources:
- Industry trade-association reports
- Government statistics (BEA, Eurostat, ONS)
- Sell-side analyst sector primers (Bernstein, Jefferies, JPM)
- Triangulation from end-customer spend × stage's share

Express stage revenue as a **range** (low / base / high), not a point estimate.

### 5. Compute stage EBIT and disclose uncertainty

```
Stage EBIT (base) = Stage revenue (base) × Stage median margin
Stage EBIT (low)  = Stage revenue (low)  × Stage 25th-pct margin
Stage EBIT (high) = Stage revenue (high) × Stage 75th-pct margin
```

Tag: `[I: triangulated from {N} listed comparables — {names}; 3yr avg margin {x}%; stage revenue {C: source}]`

## Method 2 — Reported segment data

When pure-plays do not exist, mine the **segment reporting** in 10-Ks / 20-Fs of diversified players. IFRS 8 and ASC 280 require segment-level revenue, EBIT (or equivalent), and assets where the segment is reported to the CODM.

Quality gate:
- Segment definition matches the value-chain stage cleanly (often it does not — intercompany transfer pricing distorts)
- Disclosed margins are not "managed" (i.e., the player has no incentive to mask the segment)
- ≥2 comparable segment disclosures cross-check each other

## Method 3 — Sector analyst notes

Sell-side analysts at Bernstein, Morgan Stanley, JPM, Jefferies, Redburn often publish **value-chain profit maps** for major industries. Use these as triangulation, not primary source.

Confidence rank: own listed-comparable analysis > segment data > analyst-published profit maps > management assertions.

## Method 4 — Cost-build (last resort)

If no listed comparables and no segment data exist (typical for highly fragmented stages: e.g., independent dental practices, regional logistics specialists):

1. Estimate stage revenue from end-market triangulation
2. Build a representative cost stack from primary research (vendor pricing, labour, real estate) and trade interviews
3. Derive implied EBIT as the residual

Cost-build estimates carry an `[I: cost-build, primary-research-based]` tag and the widest confidence interval. Use for direction, not for valuation.

## Common errors

| Error | Symptom | Fix |
|---|---|---|
| Including diversified players as "pure-plays" | EBIT median converges to the diversified industry average regardless of stage | Tighten the ≥70% revenue threshold; document exclusions |
| Using single-year margin | Stage EBIT swings 30%+ year-to-year | Use 3-year average minimum; 5 years for cyclicals |
| Mixing GAAP and non-GAAP "adjusted" EBIT | Apparent margins inflated by 200-500 bps from add-backs | Standardise on GAAP EBIT including SBC |
| Geographic mismatch | EM comparables for a DM stage analysis | Match geography to within one tier (DM/EM, regulated/unregulated) |
| Ignoring scale differences | Treating a $50m player like a $5B player | Note that small comparables may have sub-scale margin; weight median toward stage-typical scale |

## When to commission primary research

If the listed-comparable median has a dispersion >600 bps, or if pure-plays cover <50% of stage revenue, commission **expert interviews** (2-4 ex-executives per stage). Use to validate the comparable-derived range, not to replace it.

## Output format for the stage row

```
Stage: Component manufacturing
Estimated revenue: $14-18B [C: SIA 2025 + 2 sell-side primers]
Median EBIT margin: 12% (3-yr avg, n=4 comparables: STM, Infineon, ON Semi, Renesas) [I: listed-comp triangulation]
Stage EBIT range: $1.7-2.2B (base $1.9B)
```

The validator looks for this level of disclosure on the methodology, not just the number.

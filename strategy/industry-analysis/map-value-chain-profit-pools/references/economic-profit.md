# Economic Profit — When EBIT Is Not Enough

EBIT is a fine first-pass profit metric for a profit pool. It breaks down when stages differ materially in **capital intensity**. A capital-heavy stage and a capital-light stage with the same EBIT have very different economics for an owner of capital — the heavy stage may be destroying value even while reporting accounting profit.

## The metric

```
Economic profit (EP) = NOPAT − (Capital employed × WACC)

where:
  NOPAT = EBIT × (1 − effective tax rate)
  Capital employed = Net working capital + Net PP&E + Capitalised intangibles (incl. capitalised R&D)
  WACC = weighted-average cost of capital for the stage
```

Equivalent forms used in CDD: **EVA®** (Stern Stewart), **economic value added**, **residual income**.

## When to upgrade from EBIT to economic profit

**HARD RULE — the >2× capital-intensity trigger:** if stage capital intensity is disclosed in the output and the max/min capital-intensity (or capital-employed-to-revenue) ratio across stages exceeds **2.0×**, you MUST use economic profit (EP / NOPAT minus capital charge), not EBIT. The validator enforces this as a hard fail. Rationale: at >2× variance, EBIT-only comparisons systematically misrank stages — the conclusion about where profit concentrates is wrong, not just imprecise.

Use EBIT (default, when the hard rule does not bind):
- Capital intensity is similar across stages (max/min ≤ 2×) — but disclose the intensity numbers so the reader can verify
- Capital-intensity data is not available at all (validator emits a soft warning suggesting disclosure)
- Analysis is directional / qualitative-bias and the audience accepts the limitation

Additional soft triggers to upgrade even when the hard rule does not bind:
- The audience is a PE buyer or CFO who underwrites to IRR
- One or more stages have heavy intangibles (capitalised R&D, customer-acquisition cost, content libraries)
- The profit-pool conclusion would change if a capital charge were applied

## WACC selection at the stage level

Stage WACC is typically not separately disclosed. Triangulate via:

1. **Pure-play listed comparables** — pull their published WACC (or estimate from beta + Rf + ERP). Use the median for the stage.
2. **Sector mid-point** — Damodaran's industry WACC tables (NYU Stern, updated annually) give cost-of-capital benchmarks by sector.
3. **Adjusted for stage risk** — a stage with high operating leverage (e.g., capital-intensive manufacturing) carries a higher WACC than the parent industry average; an asset-light services stage typically lower.

Document the stage WACC and basis as a separate row in the working file. Tag as `[I: Damodaran industry WACC 2025 + 3 listed comparables]`.

## Capital employed estimation

For each stage:
- **Net working capital** — DSO − DPO + inventory days, applied to stage revenue
- **Net PP&E** — from listed comparables' balance sheets, scaled to stage revenue
- **Capitalised intangibles** — for software/pharma, capitalise R&D over 3-5 years using a straight-line amortisation. For DTC, capitalise customer acquisition cost over expected customer life.

## Worked example — fabless vs. integrated semiconductor

| Stage | Revenue $B | EBIT % | EBIT $B | Capital $B | WACC | EP $B |
|---|---|---|---|---|---|---|
| Fabless design | 40 | 30% | 12.0 | 25 | 11% | 9.25 |
| Foundry (manufacturing) | 80 | 35% | 28.0 | 220 | 9% | 8.20 |
| Test & assembly | 12 | 12% | 1.4 | 8 | 10% | 0.60 |
| Distribution | 18 | 4% | 0.7 | 2 | 8% | 0.54 |

**EBIT view:** foundry captures 60% of pool — looks dominant.
**Economic-profit view:** fabless and foundry are tied (~$9B each) because foundry's $220B capital base soaks up most of its accounting profit at a 9% WACC.

The strategic implication flips: a capital-light fabless position is **as economically profitable** as a capital-heavy foundry, with far less capital risk. This is the kind of conclusion EBIT alone would obscure.

## Negative economic profit is a real finding

A stage with positive EBIT and negative EP is **destroying capital**. Common in:
- Asset-heavy distribution / logistics
- Mature commodity manufacturing
- Sub-scale infrastructure plays

Negative-EP stages are often where the **disruption** is coming from (asset-light entrants) or where the **roll-up consolidation** thesis lives (only scale can rescue returns).

## Output requirements

If you used economic profit (not EBIT):
- Label the table column `EP ($B)` explicitly
- Disclose WACC per stage in a footnote
- Disclose capital employed source per stage (V/C/A/I tag)
- The validator accepts either "EBIT" or "economic profit" but warns if both are mixed in the same pool

## Anti-patterns

- ❌ Mixing EBIT for some stages and EP for others without explanation
- ❌ Using a single industry-wide WACC for all stages when capital intensity varies materially
- ❌ Ignoring capitalised intangibles in software/pharma (understates capital, overstates EP)
- ❌ Quoting EP to 2 decimal places when the underlying WACC is ±200bps uncertain

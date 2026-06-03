# Sizing Methodology — McKinsey G3 / Granular Growth + Triangulation

The discipline: aggregate market growth rates are misleading. G3-level sub-segment portfolio choice explains ~65% of organic top-line growth (Viguerie/Smit/Baghai, *The Granularity of Growth*, McKinsey 2008; reaffirmed in McKinsey Insights 2023-2025). Always decompose before accepting any aggregate rate.

## The G3 hierarchy

| Level | Granularity | Example (specialty apparel) | Typical $ size |
|-------|------------|---------------------------|----------------|
| G0 | Sector | Consumer discretionary | $T-scale |
| G1 | Industry | Apparel | $100B+ |
| G2 | Sub-industry | Specialty apparel | $10-100B |
| **G3** | **Segment** | **Off-price specialty apparel × US × women's** | **$1-20B** |
| G4 | Micro-segment | Off-price specialty apparel × US × women's × athleisure × $25-$50 | $0.1-1B |
| G5 | Item-level | Above × specific SKU class | <$0.1B |

**G3 is the minimum decomposition for analytical credibility.** Aggregate growth at G2 typically hides 5-15pp variance across G3 segments. Without de-averaging, any growth-rate claim is structurally suspect.

**How many sub-segments?**

| Arenas classification | Minimum sub-segments |
|----------------------|----------------------|
| Quick mode (default) | ≥3 |
| Deep mode (default)  | ≥5 |
| **Arena** (any mode) | **≥7** — highest within-market dispersion, finer-grained decomposition required |

McKinsey's full granular-growth practice uses 10-30 to capture full variance; we cap as above for PE-CDD speed. State the cap in output.

## Intake — lock these before any research

1. **Industry slug** (`industrial-robotics-na`) — locked at G2 or G3.
2. **Geographic basis** (NA / EU / global) — single basis. Cross-region requires reconciliation.
3. **Base currency** (USD unless reason otherwise) — all figures converted to base.
4. **Reporting year** (current = 2026 unless specified) — sources >24mo old need explicit "still current" justification.
5. **Definition lock** — write the one-sentence inclusion/exclusion rule. *Example: "Industrial robotics = articulated + SCARA + collaborative robot arms sold for industrial use. Excludes AGVs, AMRs, software-only integration, and consumer robotics."*
6. **Depth mode** — Quick (TAM+SAM, ≥3 G3 sub-segments) or Deep (TAM+SAM+SOM, ≥5 G3 sub-segments + competitor share-shift data).

## Top-down sizing

**Method:** start from a published total market figure, validate the definition matches your locked definition.

Sources in declining order of preference (each with the V/C/A/I tag it should carry):

1. **Regulatory filings** (`[V]`) — FDA UDI, FERC, SEC, EU MDR Annex VIII. Strongest evidence.
2. **Industry trade-body data** (`[V]` or `[C]`) — IFR for robotics, RILA for retail, BIO for biotech, SEMI for semis, IATA for aviation. Often free, definition-stable.
3. **Government statistical agencies** (`[V]`) — Census, BLS, Eurostat, ONS. Slow but authoritative.
4. **Paid syndicated research** (`[C]`) — IBISWorld, Statista, Frost & Sullivan, Euromonitor, Gartner, IDC, Forrester. Standard PE input. Tag the report name + year + section, not "industry report".
5. **Sell-side analyst notes** (`[C]` if ≥2; `[A]` if single) — Bernstein, Morgan Stanley, JPM, Jefferies sector teams. Accessed via Tegus, AlphaSense, Sentieo. Note the aggregator but cite the underlying analyst.
6. **AI aggregators** (Perplexity, ChatGPT, etc.) — **NEVER cite as primary.** Use only to find underlying source, then cite the source directly. Citing the aggregator without source chain is a known 2026 failure mode (validator flags this).

**Always capture:** report name, year, geographic basis, definition used, currency. Tag every figure V/C/A/I.

**Definitional drift — the #1 top-down trap.** "Industrial robotics" varies wildly across reports (some include AGVs, some don't; some include software/integration, some are hardware-only; some include service revenue, some are equipment-only). Reconcile every source to your locked definition. State adjustments inline: *"IFR reports $X.XB but includes AGVs and service revenue; adjusted to hardware-only = $Y.YB [I: -15% AGV share + -8% service revenue per IFR methodology notes]."*

## Bottom-up sizing

**Method:** estimate from primary inputs.

Three formulas (use at least one; two for triangulation):

- **Volume × price:** units sold per year × average price per unit. Best when unit data is published (autos, smartphones, robots).
- **Customers × spend × penetration:** addressable customers × average annual spend × % currently spending. Best for services and SaaS.
- **Value-theory (optional generally; REQUIRED for software/SaaS):** customer benefit value × addressable customers × capture rate. Best when units are hard to count but value-per-customer is documented (e.g., AI productivity tools — "$X saved per knowledge worker × Y workers × Z% willing to pay"). Newer 2026-era third triangulation method (slgoodrich, wshobson, McKinsey internal). **For software/SaaS markets** — where the industry slug or locked definition contains any of `saas, software, cloud, platform, api, developer tools, observability, security software, fintech-software` — value-theory is a **required third leg**, not optional. Rationale: unit counts in software are noisy (seats vs sites vs API calls vs tenants) and value-per-customer is more defensible.

Document every assumption with V/C/A/I tag. Source assumptions from data **independent** of the top-down report (circular sourcing fails validation).

**The 10-customer test:** at the end of bottom-up, can you name 10 specific potential customers in the market you just sized? If not, the customer count is air. (Borrowed from slgoodrich/ai-pm-copilot.)

## Triangulation

Compare top-down vs bottom-up. Acceptance bands:

| Gap | Interpretation | Action |
|-----|---------------|--------|
| <5% | Suspicious — almost certainly circular sourcing. | Re-verify the bottom-up source is fully independent. Document independence proof. |
| 5-25% | Normal. | Pick whichever has the more defensible assumptions as primary; note the other as triangulation check. |
| >25% | Reconciliation required. | Trace to specific assumption(s) driving the gap. Common causes: time period, geographic scope, customer/product inclusion, FX rate, service vs hardware split. |

If value-theory was used as a third leg, all three should land within ±25% of the median; if not, the outlier method is flagged in output.

## G3 decomposition output

For each of ≥3 (Quick) or ≥5 (Deep) sub-segments, capture:

```
| Sub-segment | Current size ($B) | 5yr CAGR (%) | Source tag |
|-------------|-------------------|--------------|-----------|
| [name × geo × customer] | X.X | YY | [V/C/A/I: source-name + year + section] |
```

Sub-segments must sum to within ±10% of the top-down TAM (sanity check). If they don't sum, either the G3 cut is wrong or the TAM is wrong — fix before continuing.

Then write the **de-averaging statement** explicitly:

> "Aggregate growth is [X]%, but the [Y] sub-segment grows at [A]% while [Z] declines at [-B]%. The aggregate is misleading because [structural reason: e.g., commoditization in mature sub-segment masks rapid growth in premium]."

Even if all sub-segments grow at similar rates, state that explicitly: *"All five G3 sub-segments grow within ±2pp of the aggregate — de-averaging confirms aggregate is representative."*

## Scenario range (recommended)

For headline TAM and SAM, provide three figures:

- **Conservative** (Pn=70): tight definition, low penetration assumptions.
- **Base** (Pn=50): locked definition, central assumptions.
- **Aggressive** (Pn=30): broad definition, optimistic penetration.

Identify the 3-5 swing variables that move the result most. Document in a sensitivity table.

## SOM realism checks (when SOM is in scope)

- **New-entrant SOM Year 1:** typically 0.1-0.5% of SAM. >5% needs justification; >10% is rejected unless a contracted backlog supports it.
- **3-year SOM:** typically 1-5% of SAM for new entrants; 10-20% for incumbents extending core.
- **5-year SOM:** typically 5-15% for new entrants.
- **TAM > SAM > SOM** must hold strictly (validator auto-checks).

## Common failure modes

1. **Single-rate sizing** — quoting one aggregate growth rate. Always fails Gate.
2. **Circular sourcing** — top-down and bottom-up from the same report. Catch by source-name comparison.
3. **Definitional drift** — switching definitions mid-analysis. Lock at intake; document any reconciliation.
4. **Stale data** — >24mo old reports without adjustment. Validator flags pre-2024 sources for 2026 sizing.
5. **Currency confusion** — mixing USD and EUR figures without conversion. Lock base currency at intake.
6. **LLM-aggregator sourcing** — citing Perplexity/ChatGPT/Bard as the source. Always trace to the underlying report and cite that.
7. **Aspirational SOM** — Year-1 SOM at 10%+ of SAM with no backlog evidence.
8. **TAM/SAM/SOM ordering violation** — SAM > TAM or SOM > SAM. Catch by validator.
9. **Sub-segment non-summation** — G3 segments sum to >110% or <90% of TAM. Indicates definitional mismatch.
10. **Missing scenario range** — single point estimate without low/base/high (warning, not fail).

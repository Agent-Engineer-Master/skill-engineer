# Profit Pool Methodology

Source: Orit Gadiesh & James Gilbert, *Profit Pools: A Fresh Look at Strategy* (Bain / HBR, 1998). Now standard senior MBB / PE-CDD practice.

The discipline: map ABSOLUTE economic profit (not revenue, not margin %) by value-chain stage. Profit concentrates in structurally protected niches — often inverted from where revenue is highest.

## Why absolute $ matters

Two stages with the same 12% EBIT margin can represent radically different profit pools if their revenue scales differ. Final assembly might be 60% of industry revenue at 8% margin ($4.8B EBIT on $60B revenue); integration might be 15% of revenue at 25% margin ($3.75B EBIT on $15B revenue). The integration stage is nearly as large a profit pool despite being 1/4 the revenue — and it's structurally more attractive.

**Always express profit pool in absolute $ EBIT or economic profit. Never as margin % or revenue share.**

## Estimating EBIT per stage

**Method 1 — Listed comparable triangulation (most common):**

For each value-chain stage:
1. Identify 3-5 listed pure-play companies operating primarily in that stage
2. Pull their EBIT margins (consistent definition — typically EBIT/revenue from continuing operations)
3. Compute median EBIT margin for the stage
4. Multiply by estimated total industry revenue at that stage
5. Result: estimated absolute EBIT for the stage

Tag the median margin as `[I: derived from N listed comparables — list names]`.

**Method 2 — Reported segment data:**

For stages dominated by diversified players (e.g., an OEM that also runs integration services), use the players' segment-level reporting where available. Most public companies report segment EBIT in 10-K / 20-F filings.

**Method 3 — Sector analyst notes:**

Bernstein, Morgan Stanley, JPM, and Jefferies sector teams sometimes publish profit-pool maps for major industries. Use as triangulation, not primary source.

## Economic profit (preferred over EBIT for capital-intensive stages)

Economic profit = EBIT − (capital employed × cost of capital).

Use economic profit when stages differ materially in capital intensity. A pure-software integration stage and a capital-intensive component manufacturing stage with identical EBIT will have very different economic profit. For most consultative purposes, EBIT is sufficient; for PE due diligence on capital-intensive sectors, use economic profit.

## Profit-pool visualization

Use a horizontal-bar markdown table where bar width is proportional to absolute EBIT:

```
| Stage | EBIT ($B) | Margin (%) | Profit-pool bar |
|-------|-----------|-----------|------------------|
| Components | 2.1 | 11 | ███ |
| Manufacturing | 0.8 | 4 | █ |
| Integration | 4.3 | 25 | ██████ |
| Distribution | 1.2 | 8 | ██ |
| Service | 0.5 | 22 | ▌ |
```

Bar width scaling: pick a unit (e.g., 1 char = $0.7B) and apply consistently. Round to nearest character.

## Identifying structural profit concentration

Name the stage with highest absolute EBIT. Then answer the WHY question with a **named structural protection** from Helmer's 7 Powers:

- **Scale economies** — fixed costs amortised over large volume; minimum efficient scale unattainable for entrants
- **Network economies** — value increases with participants (two-sided marketplaces, payments, social)
- **Counter-positioning** — new entrant's business model is one the incumbent cannot copy without damaging existing economics
- **Switching costs** — customer's all-in switching cost (financial + procedural + relational) materially exceeds any price differential
- **Branding** — durable customer ascription of higher value to objectively-identical offering (trust, safety, status)
- **Cornered resource** — preferential access at attractive terms to a coveted asset (patent, licence, deposit, talent, dataset). **Regulatory barriers** sit inside this category.
- **Process power** — organisational capability evolved over years that competitors cannot replicate in reasonable time (Toyota, ASML, Amazon logistics)

These names map 1:1 to Helmer's 7 Powers (2016), which is how `assess-moat-sources` (Phase 2) will assess durability. See `references/structural-protections.md` for diagnostic questions per power and the list of non-structural anti-patterns the validator rejects.

**If you cannot name a structural protection, profit concentration is unstable** — and that itself is a finding. Document it explicitly.

## Cross-reference with Five Forces

If `working/five-forces.md` exists, reconcile:
- The named governing force should explain WHY profit concentrates where it does
- "Buyer power high" should NOT coexist with "customer-facing stage captures most profit"
- "Switching costs high" SHOULD coexist with "stage with switching cost lock-in captures most profit"

Document contradictions in the output and flag for orchestrator's Gate 2.

## Normalisation — 3-5 year average, not single year

Single-year EBIT prints are noisy. Cyclical industries (auto, semis, commodity chemicals, freight) can swing margins 1000+ bps year-to-year. Normalise:

- **Default:** 3-year trailing average margin per stage
- **Cyclical industries:** 5-year average to span at least one full cycle
- **Disruption phase:** explicitly flag and use most-recent-12-months, with rationale

The validator looks for a normalisation disclosure in the output footnotes. A profit pool built on a single-year print without justification is a failure mode.

## Ranges, not point estimates

Every stage EBIT estimate carries irreducible uncertainty. Express as:

```
Stage EBIT: $1.7-2.2B (base $1.9B)
```

Not:

```
Stage EBIT: $1.94B   ← false precision
```

Three-decimal precision implies sourcing rigor that does not exist in triangulated estimates. The validator warns on EBIT figures quoted to ≥2 decimals without an accompanying range.

## Shared cost allocation — ABC-lite

When stages share back-office, IT, or corporate overhead (common with vertically-integrated players in the comp set), allocate using activity-based costing drivers:

- Revenue share (simplest, weakest)
- Headcount share (better for support overhead)
- Direct cost share (better for shared procurement / IT)
- Transaction count / SKU count (for distribution and operations)

Disclose the driver used and the % of total EBIT that came from allocated (vs. directly observed) figures. >30% allocated = flag as low-confidence.

## Alternative visualisation — Bain "river" chart

The horizontal-bar table is the default deliverable. For executive presentation, the original Bain visualisation is a **two-axis river chart**:

- X-axis: cumulative revenue share across value chain (0% to 100%)
- Y-axis: EBIT margin %
- Area under curve = absolute profit pool

The river makes the **revenue-vs-profit inversion** visceral — a stage with 5% of revenue and 35% margin shows as a tall thin block; a stage with 40% of revenue and 4% margin shows as a wide flat block. Useful in the orchestrator's executive summary, optional for the working file.

See `assets/profit-pool-template.md` for both formats.

## Common failure modes

1. **Revenue-margin pool** — using % margin where absolute $ is required. Always fails validation.
2. **Flat profit pool** — every stage shows similar EBIT. Rare in real industries; usually an estimation error.
3. **Non-structural protection** — "stage X captures most profit because it adds the most value." Tautological. Must name a specific Helmer power.
4. **Missing cross-reference** — pool location contradicts Five Forces governing force without flagging.
5. **Single-year anomaly** — built on a one-off margin print. Always normalise to 3-5 year average.
6. **False precision** — point estimates without ranges. Triangulated estimates carry ±20-30% irreducible error; disclose.
7. **Ignoring capital intensity** — comparing EBIT across stages with materially different capital bases. Upgrade to economic profit (see `references/economic-profit.md`).
8. **Pure-play comparable inflation** — counting diversified players as pure-plays. Tighten to ≥70% revenue concentration.
9. **Mixing GAAP and adjusted EBIT** — non-GAAP "adjusted EBIT" inflates margins 200-500 bps from SBC and acquisition add-backs. Standardise on GAAP including SBC.
10. **Static-pool fallacy** — treating the profit pool as a fixed map. Pools migrate (Christensen) — always note 3-year direction of travel.

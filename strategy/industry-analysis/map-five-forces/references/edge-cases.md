# Edge Cases — map-five-forces

Factual exceptions and industry-specific quirks encountered in real use. Update via the closing feedback gate when a factual exception arises that the next run would otherwise miss. Distinct from `learnings.md` which holds behavioral patterns.

## Industries where complementors genuinely don't apply

- Bulk commodity chemicals sold direct to industrial buyers (no ecosystem; complementors section reads "none material — bulk commodity sold direct, no ecosystem dependencies").
- Primary metals, cement, basic petrochemicals.
- Most B2B IT staffing (no platform layer).

## Industries where AI is genuinely not yet material (May 2026)

- Heavy infrastructure construction — physical capital dominates, AI compresses <5% of cost base.
- Bulk shipping — fuel + ship capex dominate.
- Real estate ownership (not brokerage — brokerage IS AI-affected).

State "AI not material because [physical capital dominates / etc.]" — do not silently omit.

## Focal-layer ambiguity — semiconductor example

For "semiconductors," intake must force a focal-layer choice:
- IP (ARM, Synopsys) — extreme network economies, near-zero rivalry
- Fabless design (Nvidia, AMD) — high rivalry, brand power, talent constraints
- Foundry (TSMC, Samsung) — extreme supplier power as buyer; capital wall
- Equipment (ASML, Applied) — monopoly/oligopoly characteristics
- Packaging/test — fragmented, commodity-like

A single Five Forces analysis cannot cover all five layers — pick one or run separately.

## Two-sided platforms — buyer/supplier role flip

On platforms (Uber, App Store, Amazon Marketplace), the same actor can be supplier today and competitor tomorrow. Document the focal viewpoint in the boundary note — are we analyzing the platform-as-keystone, or the participant-as-seller? The force assessment differs sharply.

## Regulated industries — regulator as implicit force

In healthcare, finance, defense, telecoms, utilities, the regulator behaves as a quasi-force (sets entry barriers, caps margins, mandates standards). Include a "Regulator dynamics" sub-paragraph under Threat of New Entry; do not invent an eighth force.

## When the profit pool cannot be obtained

If `map-value-chain-profit-pools` has not been run in the same industry folder, step 6 (cross-reference) is skipped with an explicit note: "Profit-pool cross-reference deferred — value-chain-profit-pools.md not present." The analysis still ships but is flagged for re-validation when the profit-pool file lands.

## When two forces genuinely co-govern

Rare but real. State both in the governing-force sentence joined by "and," and explain the mechanism by which they interact:

> "Buyer concentration AND complementor density co-govern this industry because the top three buyers control 65% of demand and demand specific complementor integrations as table-stakes."

The validator accepts up to two governing forces. Three or more = analysis failure.

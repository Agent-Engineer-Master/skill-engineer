# Willingness-to-Pay Drivers — Per-Segment Analysis

## What we are doing here, and what we are NOT

At industry-analysis altitude, we are **not** pricing a single product. We are identifying which DRIVERS govern the price ceiling for each segment, so a downstream user (PE investor, strategist, product team) can predict how WTP will move under different scenarios.

A WTP "answer" of "$X per seat per month" is product-pricing work. A WTP DRIVER analysis answers: *why does this segment's price ceiling sit where it sits, and what would move it?*

## Why drivers, not numbers

Industry-level WTP shifts. Numbers don't generalize across segments or across time. Drivers — the underlying causal mechanisms — do generalize and do let a reader reason about scenarios.

Examples of WTP driver statements:

- "Regulated buyers in segment A will pay 3-5x premium for documented compliance proofs because non-compliance carries seven-figure fines per FDA 483 history [V: FDA 483 letters 2022-2024]. The driver is **regulatory penalty avoidance**; weakening enforcement would compress the premium."
- "Self-serve developer-tooling buyers in segment B will not pay until usage exceeds free tier by ~2x because procurement friction (expense reports, manager approval) exceeds rational threshold [C: PriceBeam B2B WTP study 2024 + Stripe Atlas developer pricing data]. The driver is **procurement friction**; a usage-based credit-card-bypass model would reset the ceiling."
- "Consumer segment C exhibits steep WTP cliff at $30 where category framing shifts from impulse to considered [A: vendor pricing test, single data point — confirm with conjoint]. The driver is **category framing anchored on the impulse threshold**; reframing as subscription or bundling shifts the anchor."

Each statement: segment → driver → mechanism → what would move it.

## B2B vs B2C — the structural split

### B2B WTP drivers (typical priority order)
1. **ROI defensibility** — can the buyer build a business case the CFO will sign?
2. **Risk reduction** — what does this protect against, and how big is the avoided cost?
3. **Procurement friction** — vendor-onboarding cost, terms, security review burden
4. **Switching cost lock-in** — incumbent advantage to existing supplier
5. **Career insurance** — what does buying THIS protect the buyer's career from?

Note: in procurement-driven B2B, tenders, incumbent bias, and terms drive realized price more than perception-based methods predict. Van Westendorp on enterprise software typically over-states the achievable price.

### B2C WTP drivers (typical priority order)
1. **Reference price** — what comparable thing costs
2. **Perceived value at point-of-purchase** — heuristic, anchoring-sensitive
3. **Category framing** — impulse vs considered; the framing sets the anchor
4. **Identity signaling** — what does buying THIS say about me
5. **Substitute price** — including do-nothing

## Methodology anchors (state when available)

When citing WTP, anchor to the methodology:

| Method | Best for | Limits |
|--------|----------|--------|
| Van Westendorp PSM | B2C / prosumer / single-attribute pricing | Hypothetical; weak when feature-price interactions matter; over-states B2B realized price |
| Choice-based conjoint / discrete choice | B2B feature bundles, multi-attribute trade-offs | 5-8 weeks; expensive; still hypothetical |
| Value-based pricing (ROI) | B2B with quantifiable economic outcome | Requires the buyer to believe the ROI claim |
| Expert elicitation | Pre-launch, new category | Anchored by expert's existing reference set |
| Revealed-preference (real transactions) | Mature markets | Lags by definition; censored by what's been offered |

In industry-analysis output, state which method's evidence base supports each driver claim.

## Common failure modes

- **Single number, no driver** — "ACV $50K." Tells the reader nothing about how WTP will move.
- **Demographic-anchored WTP** — "Enterprises pay more than SMBs." True but trivial; the structural driver is what matters.
- **Ignoring procurement friction in B2B** — it almost always dominates pure value-perception in regulated procurement environments.
- **Treating all B2C WTP as price-elastic** — identity-signaling and category-framing often dominate price-sensitivity in lifestyle categories.
- **No method anchor** — claiming a WTP without saying where the evidence comes from.

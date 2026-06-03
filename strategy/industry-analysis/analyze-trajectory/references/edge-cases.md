# Edge Cases — analyze-trajectory

Factual exceptions and special-handling protocols. Distinct from `learnings.md` (behavioral feedback).

## Very young industries (<3 years old)
- S-curve assessment is high-error. Default classification: Introduction with explicit note "stage classification has wide error bars; tech S-curve may matter more than market S-curve."
- Three Horizons collapses: there may be no H1 (everything is H2/H3). State this and recommend the analysis be re-run after the dominant design locks in.
- Power Progression: Counter-Positioning and Cornered Resource windows are wide open; Branding and Process Power not yet buildable.

## Declining industries
- Three Horizons partially collapses: H3 may be absent. State explicitly. Don't invent H3 sub-segments to fill the table.
- Power Progression: only defensive Powers remain (Scale defense, Process Power defense, Branding defense). Counter-Positioning and Network Economies windows are CLOSED.
- Scenarios: bull case is "decline arrested" not "growth resumed." Be honest.

## Platform / ecosystem industries
- Dual S-curve applied to both sides of the platform (e.g., for mobile gaming: market = consumer adoption; tech = device + content tooling).
- Three Horizons applied at the keystone level — sub-segments are use cases, not just product variants.
- Discontinuities often regulatory (app store fee rulings, antitrust) — scan that type deliberately.

## Heavily regulated industries (healthcare, finance, defense)
- Regulatory discontinuities dominate the catalog. Tech and behavioral still scanned but typically smaller mover.
- Timing windows often anchored to legislative or rulemaking calendars (e.g., "FDA Q4 2027 final rule").
- Power Progression: Cornered Resource (license) often dominates and is the binding constraint for new entrants.

## Multi-layer industries (e.g., semiconductors)
- Trajectory may differ per layer. Default: run trajectory at the SAME focal layer as the upstream Five Forces analysis (if present). Document the layer in the output header.
- S-curve at fabless vs OEM vs equipment will desynchronize; pick one.

## When size-market output is absent (standalone mode)
- Ask user for ≥3 named sub-segments at intake.
- If user can only name 1-2, run the analysis on the aggregate but flag in output: "Three Horizons applied at aggregate level due to insufficient G3 decomposition; recommend running size-market for finer overlay."

## When the industry slug spans multiple genuinely-different markets
- Reject. Three Horizons + scenarios cannot meaningfully be applied to "the AI industry" (too broad) or "the technology sector" (multi-industry). Narrow the slug and re-run.

## Hyper-cycle / sentiment-driven markets (e.g., crypto sub-segments)
- S-curve assessment is unreliable; sentiment cycles overlay underlying lifecycle. Default: classify the underlying technology S-curve only, note that market S-curve is sentiment-dominated, scenarios driven primarily by sentiment / regulatory swing variables.

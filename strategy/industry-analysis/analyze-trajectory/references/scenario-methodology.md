# Scenario Methodology — Base / Bear / Bull

PE-CDD speed scenario construction. Shell-style 2x2 driving-forces matrices are gold-standard for >10yr work; for 5yr industry trajectory, base / bear / bull with named swing variables is the operative method.

## The discipline

Each scenario is defined by **explicit, named, falsifiable swing variables** — NOT adjectives.

- ❌ "Bear: growth could be lower" (unfalsifiable)
- ✅ "Bear: GPU $/hour stays at $0.50 through 2028 (vs base assumption of $0.20)" (named, falsifiable, independent)

## Construction protocol

### 1. Identify swing variables (≥3 named)
Swing variables are factors that:
- Materially move the 5yr outcome (≥20% delta on TAM or profit pool)
- Are independent (not just three names for the same underlying force)
- Are falsifiable (you can name the data point that resolves them)
- Are exogenous to the industry firms' actions (mostly)

Typical sources: discontinuities (from `discontinuities-catalog.md`), macro variables (rates, FX, commodity), regulatory open questions, demand-side behavior shifts.

### 2. Build the base case
The modal trajectory under current discontinuities. Swing variables resolve in their most likely state. State the assumption explicitly for each swing variable.

### 3. Build the bear case
1-2 swing variables resolve AGAINST the industry. The other swing variables hold at base. (Don't flip all swings simultaneously — that's a worst-case, not a bear case.)

### 4. Build the bull case
1-2 swing variables resolve FOR the industry. Same discipline.

### 5. Quantify the spread
For each scenario, state the headline number (TAM, profit pool, share concentration, or growth rate) under that scenario. The spread between bear and bull is the analysis's measure of trajectory uncertainty.

| Scenario | Swing var 1 | Swing var 2 | Swing var 3 | Headline outcome (5yr) |
|----------|------------|------------|------------|------------------------|
| Bear | [resolution] | [resolution] | [resolution] | [number] |
| Base | [resolution] | [resolution] | [resolution] | [number] |
| Bull | [resolution] | [resolution] | [resolution] | [number] |

### 6. Identify the swing variable with highest leverage
One swing variable typically dominates the bear→bull spread. Name it. This becomes the focus of monitoring / option-value strategy.

## Examples of well-formed swing variables

- "EU AI Act enforcement intensity — light (warnings, low fines) vs strict (≥€20M fines per violation by 2027)"
- "GPU $/hour by 2028 — $0.50 (constrained supply) vs $0.20 (TSMC + Samsung capacity online)"
- "Ambient-scribe EHR-integration mandate — yes by 2027 (CMS reimbursement tied) vs no"
- "GLP-1 OTC availability — yes by 2028 vs Rx-only through 2030"
- "Battery $/kWh by 2028 — $80 (EV TCO parity) vs $110 (cobalt supply shock)"

## Quantitative rigor — conditional on `market-sizing.md`

The required level of scenario quantification depends on whether upstream sizing data is available:

- **Orchestrator mode** — the trajectory output sits inside `08-knowledge/world-model/industries/<slug>/working/` AND a sibling `market-sizing.md` exists. In this mode, scenarios MUST be quantitative. Across base/bear/bull combined, the output must contain at least 3 dollar figures (e.g., `$12B`, `$450M`, `$1.2bn`) AND at least 3 CAGR figures (e.g., `18% CAGR`). Validator regex: `\$[\d,.]+\s*(B|M|bn|mn)` and `\d+\s*%\s*CAGR`. The headline-outcome row of the scenario table is the natural home for the dollar figures; per-scenario growth-rate ranges are the natural home for the CAGRs.
- **Standalone mode** — the trajectory is run without `market-sizing.md` (either standalone path or orchestrator working folder with no sibling sizing file). Quantitative scenarios are NOT required. Validator emits a soft warning: "Scenario rigor limited without `market-sizing.md` data; consider running `size-market` first or use this analysis as directional only." The qualitative scenario discipline (named/independent/falsifiable swing variables) still applies.

The rationale: when sized data is upstream, scenarios become the deliverable that ties sizing to trajectory, so the cost of qualitative scenarios is high (the analyst silently discarded available rigor). When sized data is absent, forcing dollar figures invites fabrication.

## Anti-patterns

- ❌ Adjective scenarios ("things go well / poorly")
- ❌ Swing variables that aren't independent (3 names for "AI advances faster")
- ❌ Bear case = all swings flipped (that's worst-case theater, not a bear case)
- ❌ No headline outcome quantified — scenarios become atmospheric
- ❌ No identification of the highest-leverage swing variable

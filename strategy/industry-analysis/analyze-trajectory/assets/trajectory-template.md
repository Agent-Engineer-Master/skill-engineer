# Industry Trajectory — [industry slug]

**Geographic scope:** [region]
**Horizon:** 5-year (2026-2031)
**Focal layer:** [layer]
**G3 source:** working/market-sizing.md  |  user-supplied at intake
**Generated:** YYYY-MM-DD

---

## Headline

[One-sentence trajectory thesis: e.g., "Market is late-Growth and headed toward Maturity by 2028 driven by [discontinuity]; the binding constraint for new entrants is the closing Counter-Positioning window against the incumbent EHR vendors."]

---

## 1. Dual S-Curve Position

### Market-adoption S-curve
**Stage:** [Introduction / Growth / Maturity / Decline]
**Diagnostic signals:**
- [Signal 1 + value] [V/C/A/I: source]
- [Signal 2 + value] [V/C/A/I: source]

**Inflection-point indicator being tracked:** [named indicator + current reading]

### Technology S-curve
**Stage:** [Introduction / Growth / Maturity / Decline]
**Diagnostic signals:**
- [Signal 1 + value] [V/C/A/I: source]
- [Signal 2 + value] [V/C/A/I: source]

### Desynchronization assessment
[SYNC / DESYNC]. [One sentence on what desynchronization implies for trajectory.]

---

## 2. Three Horizons Portfolio Overlay

| Sub-segment (G3) | Horizon | Rationale (≥4 criteria) |
|------------------|---------|-------------------------|
| [sub-seg 1] | H1 / H2 / H3 | [why] |
| [sub-seg 2] | H1 / H2 / H3 | [why] |
| [sub-seg 3] | H1 / H2 / H3 | [why] |

**Implied portfolio allocation:** [e.g., "Conventional 70/20/10" or "Industry warrants 50/30/20 because [reason]"]

---

## 3. Discontinuities Catalog

| Type | Discontinuity | Likely window | Possible window | Leading indicator | Direction |
|------|--------------|---------------|-----------------|-------------------|-----------|
| Regulatory | [name] | YYYY-YYYY | YYYY-YYYY | [signal] | compress / expand / redistribute |
| Technology | [name] | YYYY-YYYY | YYYY-YYYY | [signal] | compress / expand / redistribute |
| Behavioral | [name] | YYYY-YYYY | YYYY-YYYY | [signal] | compress / expand / redistribute |

Per-discontinuity tagged evidence:
- [Regulatory discontinuity narrative] [V/C/A/I: source]
- [Technology discontinuity narrative] [V/C/A/I: source]
- [Behavioral discontinuity narrative, if any] [V/C/A/I: source]

---

## 4. Helmer Power Progression Assessment

Binding lifecycle stage: [the earlier of market or tech S-curve stage]

| Power | State | Rationale |
|-------|-------|-----------|
| Scale Economies | open now / open Year 3 / open Year 5+ / closed | [why] |
| Network Economies | open now / open Year 3 / open Year 5+ / closed | [why] |
| Counter-Positioning | open now / open Year 3 / open Year 5+ / closed | [why] |
| Switching Costs | open now / open Year 3 / open Year 5+ / closed | [why] |
| Branding | open now / open Year 3 / open Year 5+ / closed | [why] |
| Cornered Resource | open now / open Year 3 / open Year 5+ / closed | [why] |
| Process Power | open now / open Year 3 / open Year 5+ / closed | [why] |

**Handoff note:** This menu of Powers is consumed by `assess-moat-sources` to select which Powers a specific firm should pursue.

---

## 5. Scenarios (5-year)

### Swing variables
- **SV1:** [named variable + resolution range, e.g., "EU AI Act enforcement: light vs strict"]
- **SV2:** [named variable + resolution range]
- **SV3:** [named variable + resolution range]

### Scenario table

| Scenario | SV1 | SV2 | SV3 | Headline outcome (5yr) |
|----------|-----|-----|-----|------------------------|
| Bear | [resolution] | [resolution] | [resolution] | [number / outcome] |
| Base | [resolution] | [resolution] | [resolution] | [number / outcome] |
| Bull | [resolution] | [resolution] | [resolution] | [number / outcome] |

**Highest-leverage swing variable:** [name + why]

---

## 6. Reconciliation with size-market

[If market-sizing.md present: state whether sized growth rate is consistent with S-curve stage. Flag any contradictions for Gate 2.]
[If absent: "size-market reconciliation deferred — market-sizing.md not present."]

---

## Handoff

Trajectory answers WHERE the industry is going and WHICH Powers are available at WHICH timeframes. For firm-specific Power selection from this menu, run `assess-moat-sources` next.

---
next_skills:
  - assess-moat-sources
  - analyze-demand
---

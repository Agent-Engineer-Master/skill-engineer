# Dynamism — Direction of Travel

Five Forces is a snapshot tool. In dynamic environments (BCG Strategy Palette: Adaptive / Shaping / Renewal), a snapshot ages within months and misleads. Every force in `five-forces.md` MUST carry a direction-of-travel arrow over the next 3-5 years.

## Why this matters

A force that is "Low today, intensifying fast" is more strategically important than a force that is "High today, stable." Snapshot intensity tells you where profits sit *now*; trajectory tells you where they will sit when the decision plays out.

## Direction-of-travel categories

| Arrow | Meaning | Decision implication |
|-------|---------|----------------------|
| **Intensifying ↑** | Force will be materially stronger in 3-5yr | Discount future profit pool at this layer; expect margin compression |
| **Stable ↔** | Force structurally locked; no visible mechanism for change | Current profit pool persists |
| **Weakening ↓** | Force will be materially weaker in 3-5yr | Expansion opportunity; expect margin expansion |

## Evidence anchors for each direction

A direction claim, like an intensity claim, requires V/C/A/I-tagged evidence — not vibes.

**Intensifying signals:**
- New entrant funding accelerating (track Series A/B announcement velocity in industry)
- Buyer consolidation in motion (named M&A in last 24 months)
- Substitute price-performance crossing parity threshold
- Regulatory move telegraphed (e.g., FTC consent decree, EU Act proposal)
- AI-driven cost compression actively restructuring incumbents

**Stable signals:**
- HHI changes <5 points over 5 years
- No funded entrants with traction in 3+ years
- Substitute price-performance gap stable or widening in incumbents' favor
- Regulatory regime mature, no proposed changes

**Weakening signals:**
- Failed entrants outnumber funded ones 3:1 over 3 years
- Buyer fragmentation in motion (M&A breakups, new buyer cohorts)
- Substitute category losing share to industry
- Incumbents consolidating profitably (rivalry weakening)
- Regulatory loosening (license caps lifted, etc.)

## Velocity, not just direction

Where possible, qualify the trajectory with velocity:
- **Slow** — material change over 5+ years (regulatory cycles, infrastructure)
- **Medium** — material change in 2-5 years (entrant scale-up, buyer consolidation)
- **Fast** — material change in <2 years (AI cost compression, sudden substitute breakthrough, viral demand-side shift)

Fast trajectories override snapshot intensity in the governing-force decision. A "Moderate, intensifying fast" force often governs even when a "High, stable" force exists alongside it.

## Output requirement

Every force in `five-forces.md` carries a `**Direction:** ↑/↔/↓` line with at least one tagged evidence claim supporting the arrow. The validator (`validate_forces.py`) checks for direction arrows on all six forces (5 classical + complementors) and the AI section.

## Common failure mode

**Symptom:** every force tagged "stable" by default. **Cause:** drafter didn't engage with trajectory; treated direction as box-ticking. **Fix:** if all 7 force-direction arrows say "stable," the analyst hasn't engaged. Real industries always have at least one intensifying or weakening force. The validator warns when all-stable is detected.

## Cross-reference to Strategy Palette

The orchestrator's environment diagnosis (Classical / Adaptive / Visionary / Shaping / Renewal) sets the bar for trajectory rigor:
- **Classical** environment — snapshot dominant; direction is sanity check
- **Adaptive / Shaping / Renewal** — trajectory dominant; snapshot is starting point only
- **Visionary** — snapshot and trajectory both subordinate to the to-be-built future state

If the orchestrator's diagnosis is non-Classical and the Five Forces output has all-stable arrows, the analysis is structurally wrong for the environment. Flag at Gate 2.

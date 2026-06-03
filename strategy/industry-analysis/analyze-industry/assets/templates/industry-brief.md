---
industry: [industry-slug]
date: YYYY-MM-DD
mode: [quick | deep]
status: [draft | bar-tested | approved]
analyst: claude-analyze-industry
provenance_tag_coverage_pct: 100
---

# [Industry Name] — Industry Brief

## Situation
[1-2 sentences — what is currently true about this industry that the senior reader will agree with. Tagged claims.]

## Complication
[1-2 sentences — what has changed or is at risk that disrupts the situation. Tagged claims.]

## Question
[1 sentence — the strategic question this brief answers.]

## Answer
[1 paragraph — the governing observation and its top-line implication. This is the "if you read only one paragraph, read this" section.]

---

## Industry structure

**Governing force:** [the single causal sentence from map-five-forces output]

[2-3 paragraphs synthesizing five-forces.md output, structured Pyramid-style: main observation → MECE supporting reasons → tagged evidence. Reference the working file: `working/five-forces.md`.]

## Market size and growth

**Classification:** [Arena | Pre-arena | Mature | Declining]
**Aggregate market:** $[X]B (CAGR [Y]% [2024-2029])

[1-2 paragraphs synthesizing market-sizing.md with the de-averaging insight prominent. Reference the working file: `working/market-sizing.md`.]

## Where the dollars sit

**Profit concentration:** [stage name] captures $[X]B EBIT ([Y]% of industry pool), protected by [named structural protection].

[1-2 paragraphs synthesizing value-chain-profit-pools.md. Include the horizontal-bar profit-pool table. Reference the working file: `working/value-chain-profit-pools.md`.]

## [Additional sections when Deep mode — competitive arena, trajectory, moat sources, demand]

[Phase 2 — placeholder if sub-skill not yet built.]

---

## Where to Play / How to Win

**Where to play.** [The chosen segment/layer to focus, with explicit justification grounded in the structural analysis above.]

**How to win.** [The capability + structural-power combination that wins in the chosen WTP. Name the Helmer Power(s) the winning posture must hold.]

**What we are NOT recommending.** [Explicitly name the segment(s) or posture(s) considered and rejected, with reasoning. This is the discipline that separates a recommendation from a wishlist.]

**Go / No-Go triggers.** [REQUIRED. Specific, observable conditions that convert this conditional recommendation into a binding go or no-go decision. Format:]
- **GO if** all of: [condition 1 with measurable threshold], [condition 2 with measurable threshold], [condition 3 with measurable threshold]
- **NO-GO if** any of: [disqualifying condition 1 with measurable threshold], [disqualifying condition 2 with measurable threshold]
- **Re-evaluate if** [named external signal that would change the underlying structural analysis]

[Why required: a verdict of "conditionally attractive" without specific go/no-go triggers is not actionable. The conditions must be observable in target diligence (e.g., "≥3 candidates in food/bev with >40% recurring revenue") or in market signal (e.g., "AI-native entrants reach 15% combined integrator market share"), not in subjective judgment ("if the integration thesis still feels strong"). Bar test rejects soft conditions.]

---

## Risks to the recommendation

[3-5 named risks, each with: (a) what would have to be true for the risk to materialize, (b) what early-warning signal would surface it, (c) what mitigant or pivot is available.]

---

## Verdict

[attractive | conditionally attractive | unattractive]: [one-sentence verdict]

---

*Bar test:* see `bar-test.md`
*Structured data:* see `industry-brief.yaml`
*Catalysts log:* see `signals-log.md`
*Working sub-skill outputs:* see `working/`

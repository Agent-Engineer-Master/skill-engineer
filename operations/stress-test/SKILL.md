---
name: stress-test
description: >
  Three-phase strategic decision analysis combining verbalized sampling (Stanford arXiv 2510.01171),
  customizable analytical lenses, and a structured decision brief. Surfaces tail-distribution
  insights — the non-obvious, suppressed analyses that mode-collapsed prompting misses.
  Adapted from @alex_prompter's Model Council article (April 2026) for single-Claude use.
  Works on any high-stakes decision: founder pivots, DTC category selection, brand positioning,
  workstream prioritisation, pricing, hiring.
argument-hint: "[decision or choice to analyse]  — be specific, include relevant context"
---

# /stress-test — Strategic Decision Analysis

Runs a three-phase decision analysis using verbalized sampling to surface tail-distribution insights — the non-obvious analyses that standard prompting suppresses.

**Usage:**
- `/stress-test should I enter the home wellness category or stay narrower?`
- `/stress-test two content formats: long-form carousel vs short-form daily posts`
- `/stress-test hire a contractor now vs wait until revenue hits $10k/mo`

---

## Background

After alignment training (RLHF/DPO), LLMs suffer from mode collapse: they return the most *typical* analysis — safe, expected, rarely wrong but rarely surprising. The genuinely valuable insights live in the tails of the distribution.

**Verbalized sampling** (Zhang et al., Stanford 2025) fixes this: by asking the model to generate multiple candidate responses with probability estimates, it forces reasoning across the full distribution, including the suppressed tails. Diversity gains of 1.6–2.1x in creative tasks have been reported.

**Important caveat (from follow-up research, Jun 2025):** The probability *numbers* are unreliable — LLMs can describe a distribution accurately but don't faithfully sample from it. The mechanism that actually works is the *diversity forcing* (generate N, select from the non-obvious end), not the precision of the scores. Use the scores as a ranking device, not a measurement.

---

## Step 0 — Load Context

Before running the analysis, read the relevant context files for this project:

- Your personal/founder context file — profile, constraints, time/financial constraints
- Your constraints file — hard constraints on any decision
- Your anti-goals or strategic boundaries file
- If a product/store decision: your store or product context file
- If a brand/content decision: your brand summary file

Adjust these paths to match your project structure. The goal is grounding the analysis in real constraints before reasoning begins.

Reframe the question if needed after reading context (e.g. "build vs buy" might actually be "delegate vs own").

---

## Step 1 — Verbalized Sampling (Phase 1)

For each of the four analytical perspectives below, generate **3 candidate responses** with probability estimates (higher = more typical/expected). Then **use the lowest-probability response** as the perspective output.

The goal is not the probability number — it is the act of generating multiple candidates that forces the model past its default to the non-obvious analysis.

**Four required perspectives (single-model maximally-differentiated):**

1. **Quantitative** — what do the numbers say? Revenue, margin, time, probability of success. No narrative until the numbers are done.
2. **Strategic** — what does the system say? Where does this fit in the broader picture 12–24 months out? What does this signal, enable, or close off?
3. **Risk-first** — what's the specific failure mode? Not generic risk — the exact scenario where this goes wrong, how likely, how recoverable.
4. **Unconventional** — what would a smart person who disagrees with the framing say? What if the question itself is wrong? What's the adjacent move nobody is considering?

**For each perspective, output:**
- Recommendation (clear — not "it depends")
- Single strongest evidence
- What this perspective is NOT seeing
- `[Tail insight — probability: X%]` label on the final output to make explicit this was the non-obvious candidate

---

## Step 2 — Analytical Lenses (Phase 2)

Apply the preset lenses for the decision type, or use the custom lens block if the user provides one.

### Preset: `founder` (default for COO/strategic decisions)

| Lens | Question |
|------|----------|
| **Time ROI** | What is the hours-invested-to-value-returned ratio? Where does attention compound vs. drain? |
| **Cashflow impact** | What does this do to the financial runway in 90 days? In 12 months? |
| **Long-term optionality** | Does this open or close future options? Would a future version of you be grateful or boxed in? |
| **Constraint check** | Does this fit the actual constraints (time, money, energy, anti-goals)? Be honest — does it *actually* fit? |

### Preset: `dtc-store` (for product, category, supplier decisions)

| Lens | Question |
|------|----------|
| **Margin viability** | Can this hit ≥40% gross margin at a price the market will pay? |
| **Agent-readiness** | Will this product be findable and purchasable by an AI shopping agent in 2026? |
| **Competition density** | Is the category dominated, defensible, or open? Where exactly is the gap? |
| **Execution path** | What is the specific next physical action? Fastest test with real data? |

### Preset: `brand-content` (for content strategy, platform, format decisions)

| Lens | Question |
|------|----------|
| **Audience fit** | Does this serve the specific person the brand is talking to? Would they stop and engage? |
| **Credibility alignment** | Does this reinforce or dilute the brand's core positioning? |
| **Distribution leverage** | Does this work with how the algorithm actually distributes content in 2026? |
| **Longevity test** | Will this still be relevant in 6 months, or is it chasing a news cycle? |

### Custom lenses

If the user provides custom lenses (e.g. "lens: investor view / employee impact / technical feasibility"), use those instead. Format: same table structure, apply same depth of analysis.

---

## Step 3 — Decision Brief (Phase 3)

Output a structured brief under 500 words. No process explanation — results only.

```
THE QUESTION: [restate — reframe if the framing was wrong]

WHERE PERSPECTIVES AGREE: [2-3 genuine convergence points]

WHERE PERSPECTIVES DISAGREE: [key tensions — explicitly flag any tail-distribution insights
that challenge consensus from Step 1]

RISK: [single most important failure mode, one sentence]

BLIND SPOT: [assumption being made without stating — the thing that, if wrong, changes everything]

OPPORTUNITY: [unseen adjacent upside — what would a competitor do with this same information?]

VERDICT: [clear recommendation, 2-3 sentences — not "it depends"]

TEST IT THIS WEEK: [specific action + metric + success threshold]
```

Verdict must be real. If genuinely ambiguous, name the single deciding factor and what it would take to resolve it.

---

## Rules

1. Always run Step 0 before analysis — decisions without constraints are not decisions.
2. The probability numbers in Phase 1 are a diversity-forcing device, not measurements. Do not report them in the final brief.
3. Verdict must be directional. "It depends on X" is only acceptable if X is named, specific, and resolvable.
4. Flag reframing explicitly: if Step 0 reveals the question is wrong, say so before running the analysis.
5. Keep the final brief under 500 words. Depth in the analysis phases; brevity in the brief.
6. After completing, optionally write a recall to your memory system at `YYYY-MM-DD-stress-test-[slug].md`.

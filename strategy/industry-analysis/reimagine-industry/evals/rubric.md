# Reimagine-Industry Quality Rubric

Seven scoring dimensions, 1-3 scale. A mediocre output scores 1-2 on at least dimensions 3, 4, and 5 (most concepts skip these). This is by design — those are the dimensions that discriminate strong concepts from competent-but-generic ones.

## 1. Structural Grounding

Do concepts trace to specific Phase 1-3 dataset entries, or are they free-associated?

| Score | What it looks like |
|---|---|
| 1 | Concepts read as fresh ideas but no dataset citations; could have been generated without the dataset |
| 2 | Most concepts cite at least one Phase 1-3 entry but citations are vague ("from Phase 2") |
| 3 | Every concept cites specific dataset paths (e.g., `phase2.customers.gifting-shoppers.pain[evaluate]`) and the trace is verifiable |

## 2. Non-Obvious Insight

Do concepts surface moves incumbents haven't made, or do they restate existing market positions?

| Score | What it looks like |
|---|---|
| 1 | Concepts are obvious — existing market positions or "an X for Y" formulations |
| 2 | At least one concept feels fresh but others are predictable |
| 3 | ≥3 concepts strike a senior strategist as non-obvious; bar test sub-agent confirms |

## 3. Why-Now Sharpness

Does each why-now name a specific dated enabling condition, or handwave at trends?

| Score | What it looks like |
|---|---|
| 1 | Generic "AI is mature" or "consumer behavior shifted" with no dates |
| 2 | Dates present but only one axis (typically tech); no intersection thesis |
| 3 | 2-3-way intersection with month/year dates and specific cost crossings, behavioral shifts, or regulatory changes named |

## 4. Idea-Maze Depth

Does each concept's idea maze cite prior attempts with diagnosed failure causes, or claim novelty unexamined?

| Score | What it looks like |
|---|---|
| 1 | "We're the first to try this" with no prior-attempt research |
| 2 | 1-2 prior attempts named but failure causes generic ("ran out of money") |
| 3 | ≥3 prior attempts named with specific failure-cause diagnosis AND explicit articulation of which Phase 3 condition addresses each failure |

## 5. Counter-Positioning Clarity

Does each concept name the specific incumbent dependency that traps incumbents from copying?

| Score | What it looks like |
|---|---|
| 1 | No incumbent analysis; concepts read as "better than" existing products |
| 2 | Incumbent named but trap is vague ("they move slowly") |
| 3 | Specific revenue/cost/relationship dependency named with evidence; incumbent's worst-case response (e.g., separate brand) analyzed |

## 6. Moat Durability

Does each concept name which Helmer Power holds at scale, with mechanism?

| Score | What it looks like |
|---|---|
| 1 | "We'll move fast" or "first-mover advantage" — neither is a moat |
| 2 | Helmer Power named but as label, not mechanism ("network effects" without same-side/cross-side) |
| 3 | Entry power + wedge-to-platform mechanism + scale Power all named with specific causal chains; counter-positioning entry has explicit expiry plan |

## 7. AI-Washing Absence

Is AI/tech a mechanism in the concept, or is it the entire thesis?

| Score | What it looks like |
|---|---|
| 1 | Concepts are "an AI agent for X" — AI/tech is the thesis with no further specification |
| 2 | Mostly grounded but at least one concept's headline is tech-led rather than job-led |
| 3 | Every concept's headline is a customer job, structural move, or business model — AI/tech appears as a mechanism enabling the move, not as the move itself |

---

## Aggregate scoring

- **Overall score** = mean of 7 dimensions (1-3)
- **Pass threshold for shipping** = overall ≥2.5 AND no individual dimension <2
- **Strong output** = overall ≥2.7 AND ≥3 dimensions at 3

A concept set scoring 3 on dimensions 1, 2, 7 but 1 on dimensions 3, 4, 5 is competent but generic — strong groundedness, weak distinctiveness. The pass threshold catches this.

A concept set scoring 3 across all 7 is exceptional and should be saved to `assets/approved-examples/` as a reference output.

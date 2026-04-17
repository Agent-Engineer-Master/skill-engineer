# Eval Rubric — auto-research

Six dimensions for scoring a completed auto-research run. Used by `evals/judge.md`.

Scores: 1 (weak), 2 (adequate), 3 (strong). A mediocre run must score 1–2 on at least two dimensions.

---

## 1. Criteria Quality
Are all criteria binary (true/false), specific (exact number or named pattern), and single-variable?

- **3** — All criteria are binary with exact conditions; none require judgment to evaluate; none contain "and"
- **2** — Most criteria are binary; one is slightly vague or compound but still evaluable
- **1** — One or more criteria are gradient ("better", "more engaging"), compound, or underdefined

## 2. Hypothesis Substantiveness
Are the hypotheses meaningful changes that could plausibly affect the criteria?

- **3** — Every hypothesis targets a specific SKILL.md section with a clear stated mechanism; no whitespace or punctuation tweaks
- **2** — Most hypotheses are substantive; one is marginal but evaluable
- **1** — One or more hypotheses are trivial (whitespace, minor reordering, no stated mechanism)

## 3. Eval Integrity
Was the harness kept immutable, and were all criteria monitored for trade-offs every iteration?

- **3** — Dashboard shows all criteria scored every iteration; trade-offs flagged where present; no evidence of harness modification
- **2** — Most criteria tracked; one iteration may have omitted a criterion without explanation
- **1** — Only the active criterion tracked per iteration; no trade-off detection visible

## 4. Dashboard Clarity
Does the dashboard clearly show what changed, why, and the improvement delta per criterion?

- **3** — Every kept hypothesis has a diff description and mechanism; every reverted hypothesis has a reason; deltas are per-criterion not just overall
- **2** — Most hypotheses explained; one keep/revert decision lacks clear reasoning
- **1** — Dashboard shows results but not reasoning; reader cannot understand why changes were kept or reverted

## 5. Generalization
Did improvements hold on unseen inputs?

- **3** — Holdout pass rate is within 10% of training pass rate; generalization confirmed
- **2** — Holdout pass rate is 10–20% below training; partial generalization noted
- **1** — No holdout validation performed despite 10+ test inputs, OR holdout gap exceeds 20%

## 6. Trade-off Detection
Were regressions in non-active criteria caught and surfaced before keep/discard decisions?

- **3** — Dashboard explicitly notes any criterion that regressed; trade-offs influenced at least one keep/discard decision
- **2** — Trade-offs mentioned in summary but not tracked per-iteration
- **1** — No evidence of cross-criterion monitoring; only the active criterion scored per iteration

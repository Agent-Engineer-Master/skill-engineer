# Iteration Dashboard — [Skill Name]

**Date:** [YYYY-MM-DD]
**Target:** [path to skill file]
**Criteria:**
- [1. Criterion name — Level 1/2]
- [2. Criterion name — Level 1/2]
- [3. ...]

**Baseline pass rate:** [X/Y criteria = Z%] (training set, 5 runs)
**Target pass rate:** [100% or user-specified]
**Iteration cap:** [5 or 10]

---

## Iterations

| # | Hypothesis | Before | After | Decision | Trade-offs |
|---|-----------|--------|-------|----------|------------|
| 1 | [one-line description of change] | [score] | [score] | KEEP / REVERT | [any criterion that regressed] |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

---

## Final Result

**Final pass rate (training):** [X/Y = Z%]
**Final pass rate (holdout):** [X/Y = Z%] *(if holdout set was used)*
**Net improvement:** [+N% from baseline]
**Iterations used:** [N of cap]

### What changed (kept hypotheses only)

| Hypothesis | Mechanism | Lines changed |
|---|---|---|
| [kept hypothesis 1] | [why it worked] | [brief diff description] |
| [kept hypothesis 2] | | |

### What didn't work (reverted hypotheses)

| Hypothesis | Why reverted |
|---|---|
| [reverted hypothesis] | [score went down / trade-off detected] |

---

## Recommendations

- [Next variable to test in a follow-up run, if cap reached before goal]
- [Any criteria to refine based on what was observed]
- [Whether a holdout gap suggests overfitting to training inputs]

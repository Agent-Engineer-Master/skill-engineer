---
name: auto-research
description: Autonomously optimizes any Claude skill (SKILL.md) or CLAUDE.md file through a closed hypothesis→test→evaluate→keep/discard loop, producing an updated skill file and an iteration dashboard (baseline score, each hypothesis, keep/discard decision, improvement delta). Use when a user wants to improve a skill's output quality against measurable criteria, run autonomous evals on a skill, or set up a self-improving optimization loop for a content, writing, or routing skill. Do NOT use for building new skills from scratch, one-time debugging sessions, or tasks where evaluation criteria cannot be expressed as binary true/false conditions — use skill-engineer-master instead.
---

# Auto Research

Autonomously runs a hypothesis→test→evaluate→keep/discard optimization loop on a target skill or CLAUDE.md. Three isolated sub-agents handle testing and evaluation — the main agent orchestrates and decides.

## Output Contract

**Produces:** updated target skill file (SKILL.md or CLAUDE.md), iteration dashboard (markdown), entry appended to `results.md`.

**Does not produce:** new skills, research reports, publishing automation, or criteria for skills it has not been given.

## Startup

Read `references/learnings.md` and summarise the 3 most relevant bullets for this run. Read the target skill file in full. If `results.md` exists, read the last run entry for this target.

---

## Step 1: Criteria Design

Read `references/criteria-framework.md`.

Propose 3–5 candidate criteria for the target skill. For each criterion:
- State the exact binary condition (true/false only — no gradients)
- Classify: **Level 1** (deterministic, script-checkable) or **Level 2** (pattern/style, LLM judge required)
- Confirm it tests one variable only — split any criterion containing "and"
- Rank by expected impact

State the recommended iteration cap (5 for 1–2 criteria; 10 for 3+) and target pass rate (default 100%).

**Wait for human approval.** Human may approve, edit, or add criteria before the loop starts.

If any criterion cannot be expressed as a true/false binary, stop and ask the human to reformulate it before proceeding.

---

## Step 2: Eval Harness Setup

Generate a minimum of 5 diverse test inputs appropriate for the target skill. Write to `harness/test-inputs.md`.

**This file is read-only for the remainder of the run. The loop may never modify it.**

If 10 or more inputs are generated, designate the last 20% as the holdout validation set. Note the split at the top of `harness/test-inputs.md`.

Run the *current unmodified* target skill on the training inputs 5 times. Score every output against all approved criteria. Calculate baseline pass rate per criterion and overall.

Log to `results.md`:
```
## Run: [YYYY-MM-DD] — Target: [skill name or file path]
Criteria: [numbered list]
Baseline: [score per criterion] | Overall: [X/Y = Z%]
Iterations: [cap]
---
```

---

## Step 3: Optimization Loop

Repeat until overall pass rate reaches target OR iteration cap is reached.

### 3a. Hypothesize
Propose one substantive change to a working copy of the skill (one variable, one change). State the expected mechanism of improvement. Small tweaks (whitespace, punctuation, trivial reordering) are not valid hypotheses.

### 3b. Test
Read `agents/test-runner.md`. Spawn it as a sub-agent with:
- Path to the skill working copy
- Path to `harness/test-inputs.md` (training set only)

Do **not** pass: the hypothesis text, experiment log, baseline score, or prior iteration context. Receive: raw outputs array, one per input.

### 3c. Evaluate (run in parallel)
For each output:
- **Level 1 criteria** → Read `agents/eval-deterministic.md`. Spawn as sub-agent with: the raw output + criterion definition.
- **Level 2 criteria** → Read `agents/eval-judge.md`. Spawn as sub-agent with: the raw output + criterion definition + relevant reference files.

Receive from each: `{"criterion": "...", "result": "pass|fail", "evidence": "..."}`.

### 3d. Score and Decide
Calculate pass rate for **all** criteria — not just the active hypothesis. Compare every criterion to the previous iteration.

- If any criterion regresses more than 5% from its previous value: flag the trade-off explicitly before deciding.
- If overall score improved → **keep**: apply the hypothesis to the working copy permanently.
- If overall score did not improve → **revert**: restore working copy to previous version.

### 3e. Log
Append to `results.md`:
```
Iteration [N]: [hypothesis one-liner] | Before: [scores] | After: [scores] | KEEP/REVERT | [one-line reasoning]
```

---

## Step 4: Validation and Output

If a holdout set exists: run the final working copy on holdout inputs and score against all criteria. Note any gap between training and holdout pass rates.

Read `assets/dashboard-template.md`. Produce the iteration dashboard using it.

Present to human:
1. Iteration dashboard (table)
2. Final pass rate vs baseline + holdout result if applicable
3. Diff summary: what changed in the skill and why, per kept hypothesis

**Wait for human approval before writing to the original skill file.**

On approval: write the final working copy to the original file path.

---

## Step 5: Feedback Gate

Ask: "Any corrections or patterns from this run I should learn from?"

Route the response:
| User says | Destination |
|-----------|-------------|
| Behavioral correction ("don't do X", "I prefer Y") | `references/learnings.md` |
| Factual exception ("format is actually Z") | `references/edge-cases.md` |
| "Never do X again" | Add rule to Step 3 above |
| Approval / "perfect" | Save dashboard to `assets/approved-examples/` |
| No response / "looks good" | Do nothing |

Trim `references/learnings.md` at 80 lines (consolidate redundant entries); hard cap at 100. When a correction reveals a repeatable failure pattern, add a new case to `evals/evals.json` with a prompt that triggers it and an assertion that the corrected behaviour is present.

---

## Rules

1. `harness/test-inputs.md` is written once in Step 2 and never modified by the loop
2. Monitor **all** criteria every iteration — not just the active hypothesis (trade-off detection)
3. One hypothesis per iteration, one variable per hypothesis
4. Hypotheses must be substantive — trivial changes are not valid
5. Never write to the original target file without explicit human approval
6. Hard stop at iteration cap — report partial improvement and recommend a second run
7. Sub-agents receive only what they need — never pass hypothesis context to the test-runner

---
<!-- Built with Agent Engineer Master — get your own production-ready skill: www.agentengineermaster.com/skill-engineer -->

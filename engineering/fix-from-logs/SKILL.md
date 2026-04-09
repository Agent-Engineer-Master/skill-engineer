---
name: fix-from-logs
description: Diagnoses bugs from raw error logs, stack traces, or CI failure output — triages and clusters errors, localizes root cause (file → function → line), enters plan mode with a structured fix + test proposal for human approval, writes a typed pytest regression test using mocks first, then implements a targeted code fix and verifies the test turns green. Trigger when: user pastes logs and wants the underlying bug fixed with tests that prevent recurrence; user says "here are the logs, fix it"; CI output shows failures needing code changes and test coverage; stack traces are provided with a request to fix and test. Do NOT trigger for: general code review without logs, refactoring without a specific bug, performance work, test coverage requests with no associated failure.
---

## Output Contract

**Produces per bug cluster:** (1) one targeted code edit at the confirmed root cause location, (2) one named typed pytest function with mocks, (3) one-line root cause statement in the test comment.

**Does NOT produce:** architecture refactors, style fixes, unrelated test coverage, multiple competing fixes.

**Hands off to:** CI / `pytest` — the final action is confirming the full suite is green.

---

## Process

### Phase 1 — Ingest & Triage

1. Accept log input from paste, file path, or stdin reference.
2. Filter to FATAL/ERROR severity first; set INFO/DEBUG aside unless they precede the first error.
3. Cluster related errors: cascading failures share one root cause — group by error type, file, and timestamp proximity before analysing individual lines.
4. For each cluster, extract: error type, file path, line number, function name, request/correlation IDs, timestamp window.
5. Output a structured error inventory (1–3 clusters max; surface the highest-severity first).

Read `references/rca-framework.md` — Section 1 (triage sequence) and Section 2 (failure mode glossary).

---

### Phase 2 — Localize (file → function → line)

1. Read the flagged file(s) in the codebase using the paths extracted in Phase 1.
2. Trace the call chain **backward** from the error site — the logged error is almost always a symptom, not the cause.
3. Apply 5 Whys: for each "why did this fail?" step, read the upstream caller or dependency until reaching an actionable root cause (something changeable in this codebase, not a framework or stdlib).
4. Read 20–30 lines of surrounding context in the affected file to understand: naming conventions, type usage, existing mock patterns, and error handling style. The fix must be native to this style.
5. Form 2–3 ranked hypotheses per cluster. Each hypothesis must have: root cause statement, location (file:line), confidence level (high/medium/low), and supporting evidence from the log + code.

Read `references/rca-framework.md` — Section 3 (5 Whys walkthrough).

---

### Phase 3 — Plan Mode Gate *(human approval required before any edits)*

1. Call `EnterPlanMode`.
2. Present the following plan structure for each bug cluster:

   ```
   ## Bug [N]: [short description]
   Root cause: [one sentence, file:line]
   Evidence: [log excerpt + code snippet]
   Confidence: high / medium / low

   ### Proposed fix
   File: [path]
   Change: [one-sentence description of what changes and why]

   ### Test plan
   Test file: [path, e.g. tests/test_module.py]
   Test name: test_[exact_scenario_description]
   Mocks needed: [list of external dependencies to mock, e.g. payment gateway, DB call]
   Assertion: [what specific state the test will assert]
   ```

3. Wait for human to approve, edit, or redirect before proceeding.
4. Call `ExitPlanMode` only after the human confirms.

---

### Phase 4 — Write Failing Test First

*If you cannot write a test that fails on the bug, the root cause is wrong — return to Phase 2.*

1. Create or append to the appropriate test file (e.g. `tests/test_<module>.py`).
2. Write a typed pytest function following `references/test-writing-rules.md`.
3. Use `unittest.mock.patch` or `pytest-mock` to isolate external dependencies (DB, HTTP, filesystem, time).
4. Assert the **specific violated state** — not just `pytest.raises(Exception)`.
5. Run the test: `pytest <test_file>::<test_name> -v`.
6. Confirm it **fails for the right reason** (failure message matches the bug) before continuing.
7. If the test passes immediately: root cause was misidentified — return to Phase 2.

Read `references/test-writing-rules.md` before writing any test.

---

### Phase 5 — Fix & Verify

1. Implement the **minimum change** that makes the failing test pass. No opportunistic cleanup, refactoring, or unrelated improvements.
2. Match the surrounding code style exactly: type annotations, naming conventions, error handling patterns.
3. Run: `pytest <test_file>::<test_name> -v` → must be green.
4. Run the full test suite: `pytest` → confirm no regressions.
5. If any existing test breaks: investigate before reverting. The fix may have exposed a pre-existing wrong test — surface this to the human rather than silently reverting.
6. After 3 failed fix attempts: stop. Present a clear blocker statement and ask the human for direction.

---

## Rules

1. Never propose a fix before completing Phase 2 localization.
2. Never skip Phase 3 — `EnterPlanMode` before any file edit, every time.
3. Always write and run the failing test before writing the fix. Always.
4. If a freshly written test passes immediately: the root cause is wrong — back to Phase 2.
5. Fix scope = minimum change to make the failing test pass. No scope creep.
6. Test names must describe the exact failure scenario (`test_checkout_raises_when_payment_returns_none`, not `test_edge_case`).
7. All tests must use typed signatures: `def test_foo(mock_bar: MagicMock) -> None:`.
8. After 3 failed fix attempts: escalate to human with a clear blocker — never compound patches.
9. When the user flags something to never do again: update the relevant rule here or in the reference file immediately.
10. When a fix + test pair is approved: save it as an example in `assets/approved-examples/`.

---
<!-- Built with Agent Engineer Master — get your own production-ready skill: www.agentengineermaster.com/skill-engineer -->

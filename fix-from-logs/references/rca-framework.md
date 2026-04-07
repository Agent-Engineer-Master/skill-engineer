# RCA Framework Reference

## Table of Contents
1. [Log Triage Sequence](#1-log-triage-sequence)
2. [Failure Mode Glossary](#2-failure-mode-glossary)
3. [5 Whys Walkthrough](#3-5-whys-walkthrough)
4. [Cluster vs. Cascade Recognition](#4-cluster-vs-cascade-recognition)
5. [Escalation Criteria](#5-escalation-criteria)

---

## 1. Log Triage Sequence

Execute in this order — do not skip steps:

1. **Filter by severity** — FATAL first, then ERROR. Set INFO/DEBUG aside unless they appear in the 5 lines before the first ERROR.
2. **Identify the timestamp window** — narrow to the period immediately before the first failure. Correlate with: deploys, config changes, feature flags, cron jobs.
3. **Extract structured fields** — file path, line number, error type, function name, request/correlation/trace IDs, user ID if present.
4. **Read context around the error** — the 10–20 lines immediately before the first ERROR often contain the causal chain. Never read the error line in isolation.
5. **Cluster related errors** — group lines sharing the same: error type, file, request ID, or function chain. One cascading failure = one root cause, many symptoms.
6. **Identify the earliest error in the cluster** — this is the candidate root cause. Later errors are downstream effects.
7. **Reproduce before fixing** — confirm you can identify the code path that would produce this exact failure given the inputs visible in the log.

---

## 2. Failure Mode Glossary

| Failure Mode | What It Looks Like | What It Usually Means |
|---|---|---|
| **Unhandled None / null** | `AttributeError: 'NoneType' object has no attribute 'x'` | Missing guard before attribute access; upstream function returned None unexpectedly |
| **Index out of range** | `IndexError: list index out of range` | List shorter than assumed; empty result set not handled |
| **Key error** | `KeyError: 'field_name'` | Dict key assumed present but absent; schema mismatch between producer/consumer |
| **Type error** | `TypeError: unsupported operand type(s)` | Wrong type passed; usually a missing coerce or wrong return type |
| **Connection / timeout** | `ConnectionRefusedError`, `TimeoutError`, `requests.exceptions.Timeout` | External dependency unavailable; retry/fallback missing |
| **Import / module error** | `ModuleNotFoundError`, `ImportError` | Missing dependency, wrong venv, circular import |
| **Assertion error in test** | `AssertionError: assert X == Y` | Either the bug itself, or a test asserting wrong expected value |
| **Cascading failure** | Dozens of errors across multiple files within 1–2 seconds | One upstream failure (DB down, bad config) rippling downstream — find the first error, ignore the rest until root cause is fixed |
| **Intermittent failure** | Passes locally, fails in CI or on retry | Race condition, time-dependent logic, non-deterministic ordering, environment diff |

---

## 3. Five Whys Walkthrough

**The discipline:** ask "why did this fail?" recursively. Each answer must be supported by evidence in the log or code — not intuition. Stop when you reach something changeable in this codebase.

**Template:**

```
Error: [exact error message and location]

Why 1: Why did [error] occur?
→ Because [function X] received [value Y] instead of [expected type/value]
   Evidence: [log line or code line]

Why 2: Why did [function X] receive [value Y]?
→ Because [caller Z] calls X without checking the return value of [dependency W]
   Evidence: [code line in caller]

Why 3: Why does [dependency W] return [value Y]?
→ Because [dependency W] returns None when [condition C] is true, and that case is unhandled
   Evidence: [code line in dependency]

Root cause: [dependency W] can return None under [condition C], and no caller guards against it.
Fix location: [file:line] — add a guard / change the return contract / handle the None case.
```

**Stopping rule:** stop when the answer is: "because this code does X instead of Y, and we can change it." Do not stop at: "because the framework/OS/network did X" unless there is no code-level mitigation possible.

---

## 4. Cluster vs. Cascade Recognition

**Single-root cascade (most common):** Multiple errors across different files, all within a 1–3 second window, sharing a common request ID or service. Treat as one bug. Fix the earliest error; the downstream errors will disappear.

**Multiple independent bugs:** Errors separated by time, different users/requests, no shared ID. Treat as separate clusters. Fix and test independently.

**Intermittent bug:** Error appears in some runs but not others. Signals: time-dependent logic, threading, non-deterministic dict ordering, test pollution (shared state between tests). Requires a test that reliably reproduces — use `freezegun` for time, `random.seed()` for randomness, explicit teardown for shared state.

---

## 5. Escalation Criteria

Stop and surface to human when:

- **3+ fix attempts have failed** — do not attempt a 4th without new information
- **The failing test passes immediately after writing it** — root cause is wrong; restart Phase 2 before telling the human
- **The fix breaks more tests than it fixes** — the root cause statement was too narrow; escalate before expanding scope
- **The error originates in a third-party library or generated code** — the fix likely belongs in a wrapper, not the library itself; confirm with human before wrapping
- **Log lines reference an environment variable, secret, or infrastructure config** — do not guess at values; ask the human

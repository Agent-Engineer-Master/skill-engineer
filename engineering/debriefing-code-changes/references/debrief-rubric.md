# Code Change Debrief Rubric

Use this before writing the report.

## Strong debriefs

- Ground every claim in the diff, commit range, or file/function references.
- Prioritize the 3–7 files with the highest learning value instead of summarizing every touched file.
- Explain why code is shaped the way it is: boundaries, interfaces, state flow, data ownership, error handling, and tests.
- Separate observed code facts from inferred intent.
- Name concepts only when the code visibly demonstrates them.
- Include caveats that the developer can act on.
- End with a quiz that forces transfer, not memorization.

## Weak debriefs

- Recap the chat transcript instead of the diff.
- Say "this uses Strategy" or "this is dependency injection" without pointing to the actual call site/interface.
- List changed files without explaining design rationale.
- Generate generic quizzes like "what is polymorphism?"
- Ignore tests, edge cases, security, performance, or tech debt.
- Turn into a code review or refactor without permission.

## Report shape

1. One-paragraph top-line summary.
2. Files you should understand first.
3. Per-change learning blocks.
4. Caveats: edge cases, performance, security/privacy, tech debt.
5. Concepts map.
6. Quiz.
7. Optional notes/follow-up.

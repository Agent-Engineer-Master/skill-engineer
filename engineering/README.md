# Engineering

Skills for software engineers and technical teams who need AI agents to diagnose bugs, fix code, and enforce security standards during implementation.

## Skills

| Skill | Description | When to Use |
|---|---|---|
| [fix-from-logs](fix-from-logs/) | Diagnoses bugs from raw error logs, stack traces, or CI failure output — triages and clusters errors, localizes root cause, proposes a targeted fix and writes a typed pytest regression test | User pastes logs wanting the underlying bug fixed with tests that prevent recurrence; CI output shows failures needing code changes |
| [security-mindset-master](security-mindset-master/) | Gates implementation of API endpoints, auth logic, database queries, and user input handling with threat surface analysis, secure defaults verification, and attacker's eye pass before any code ships | Implementing or modifying any API endpoint, authentication or authorization logic, database queries, session/token management, file uploads, or any feature that stores or transmits user data |

## When to use this domain

Use engineering skills when you need an AI agent to act as a specialist during implementation — not as a general coding assistant. These skills enforce a structured process before code is written or merged, catching bugs and security issues at the right phase. They are not for code review on already-shipped code or architectural design without a concrete change in scope.

---

*Part of the [Skill Engineer](https://agentengineermaster.com) shared skills library.*

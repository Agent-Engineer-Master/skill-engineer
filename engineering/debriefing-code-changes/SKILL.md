---
name: debriefing-code-changes
description: Debriefs a developer after an AI-assisted coding session by inspecting git diffs or commits, explaining the actual architecture decisions, design patterns, tradeoffs, caveats, and learning concepts with file/function references, then generating a practical quiz and follow-up study notes. Use when the user says they shipped code with AI, vibe coded, wants to learn what changed, wants a post-session code debrief, or asks to review a diff/commit for learning. Do NOT use for generic code review, bug fixing, refactoring, or architecture planning when there is no concrete diff or commit range to inspect.
---

## Output Contract

**Produces:** a `Code Change Debrief` Markdown report grounded in a git diff or commit range, with: change summary, files-to-understand shortlist, per-change explanation, pattern/concept map, caveats, practical quiz, and optional durable notes.

**Does NOT produce:** generic CS lessons, ungrounded pattern spotting, code edits, refactors, or deploy approval.

**Hands off to:** the developer's learning loop — they read the debrief, answer the quiz, then decide whether to save notes, add tests, or request a separate code review/fix skill.

---

## Process

### Phase 1 — Collect the actual change set

1. Ask for or infer the target range: unstaged diff, staged diff, last commit, branch diff, or explicit commit range.
2. Prefer git facts over chat memory. Run `scripts/collect_diff.py` or equivalent git commands to capture: changed files, diff stats, commits, file excerpts, and touched functions/classes where available.
3. If the diff is too large, shortlist the 3–7 files with the highest learning value: core logic, new abstractions, boundary code, data model changes, tests, and security-sensitive paths.
4. If no diff or commit range exists, stop and ask for one. Do not debrief from the chat transcript alone.

**Why:** the lesson lives in code the developer now owns. Chat transcripts are noisy and often explain intentions that never landed in the repository.

Read `references/debrief-rubric.md` before writing the report.

---

### Phase 2 — Explain intent and structure per non-trivial change

For each selected change, produce this block:

```
### [File or subsystem]
What changed: [plain-English summary]
Why it was shaped this way: [architecture/design rationale inferred from the code]
Key code to read: [file:function or file:line when available]
Pattern or concept: [only if visibly present in the code]
Tradeoff accepted: [what this design makes easier vs harder]
One thing to watch: [edge case, coupling risk, missing test, performance/security caveat]
```

Rules:
- Cite actual files/functions for every claim.
- Say "no named pattern needed" when the code is straightforward.
- Separate observed facts from plausible intent. Use "the code appears to..." when intent is inferred.
- Prefer 3–5 high-signal explanations over exhaustive file-by-file commentary.

---

### Phase 3 — Surface caveats the developer should own

Cover the four caveat classes explicitly:

1. **Edge cases** — null/empty inputs, race conditions, boundary values, retries, partial failures.
2. **Performance** — loops over large collections, repeated I/O, N+1 queries, caching, render frequency.
3. **Security/privacy** — auth checks, secret handling, injection risk, unsafe deserialization, logging sensitive data.
4. **Tech debt** — duplicated abstractions, TODOs, unclear ownership, thin tests, temporary adapters.

If a class has no visible issue, write: `No obvious issue in the inspected diff.` Do not invent risk to fill the section.

Read `references/concept-map.md` for pattern terminology and guardrails.

---

### Phase 4 — Build a practical quiz loop

Generate 5–8 questions that test whether the developer can reason about the actual diff:

- **Explain:** "Why did this change need [adapter/interface/state split]?"
- **Debug variant:** "What breaks if [API returns null / event arrives twice / list is empty]?"
- **Tradeoff:** "What did this design make easier, and what did it make harder?"
- **Test placement:** "Where would you add a test for [specific branch]?"
- **Deployment judgment:** "Which part of this diff would you be nervous to deploy, and why?"

After the user answers, grade against the diff, correct misconceptions, and ask one follow-up question on the weakest area.

---

### Phase 5 — Save learning notes only when asked

Offer to save a concise note if the user wants the learning to compound. The note should include:

- commit/range reviewed
- concepts learned
- recurring personal blind spots
- tests or follow-up work identified
- links to files or PRs

Do not write notes, commit files, or publish anything without explicit approval.

---

## Rules

1. Start from `git diff`, `git show`, or a commit/PR diff — never from chat transcript alone.
2. Every architecture or pattern claim needs a file/function reference.
3. Do not label code with a design pattern unless the structural evidence is present.
4. Keep the tone educational, not performative: teach the code the user shipped, not a textbook chapter.
5. If the debrief exposes a bug or risky design, recommend a separate fix/review step rather than silently editing code.
6. Include caveats across edge cases, performance, security/privacy, and tech debt; explicitly say when no obvious issue is visible.
7. Quiz questions must be practical and diff-specific.
8. Ask before saving notes or making any repository changes.

---
<!-- Built with Agent Engineer Master — get your own production-ready skill: www.agentengineermaster.com/skill-engineer -->

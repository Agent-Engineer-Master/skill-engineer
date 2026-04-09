---
name: analyzing-feedback
description: Parses raw customer feedback (app reviews, support tickets, interview transcripts) into categorized severity-ranked themes, scans the codebase to identify affected files and components, and proposes 3 structural edit options per theme (minimal/refactor/architectural) with rationale tied directly to the original feedback. Trigger when: user provides raw customer feedback and wants to know what to change in the code; or an agent holds user complaints needing file-level engineering proposals. Do NOT trigger for: internal PR/code review comments (use receiving-code-review instead), stack-trace bug reports (use systematic-debugging instead), or PRD drafting.
---

# Analyzing Feedback

Translates raw customer language into ranked, file-level structural edit proposals.

## Reference files

- `references/feedback-taxonomy.md` — categories, severity tiers, intent tags, negative triggers
- `references/edit-proposal-template.md` — A/B/C option output format
- `references/context-augmentation.md` — codebase context packing guide

## Process

### Step 1 — Ingest and clarify

Receive raw feedback (pasted text, file path, or description). Check: is there at least one concrete user behaviour described (an action attempted, a screen visited, an outcome expected vs. received)?

If not — ask exactly one clarifying question: "What were users trying to do when they gave this feedback?"

If the feedback is multi-source (e.g. 50 reviews, a CSV), confirm the format before proceeding.

Do not scan the codebase until at least one concrete behaviour is confirmed.

*Principle: the FeedbackEval benchmark shows raw human language feedback achieves only 50.5% edit success; converting to structured form first is the single highest-leverage step.*

---

### Step 2 — Categorize and cluster *(human gate)*

Read `references/feedback-taxonomy.md`. For each distinct piece of feedback, assign:
- **Category** — UX / Performance / Bug / Feature / Content / Other
- **User intent** — the underlying job-to-be-done (not the literal request)
- **Severity** — Critical / Important / Minor
- **Pattern count** — number of independent users/sources who mentioned this

Apply the pattern threshold: only advance themes with **2+ independent mentions OR Critical severity**. Flag single-mention items explicitly — do not silently drop them.

Present the categorized table to the user:

> | Theme | Category | Severity | Pattern count | Advance? |
> |-------|----------|----------|---------------|---------|

**→ Human gate:** "Should I scan the codebase for these themes, or adjust any before I proceed?"

Do not continue to Step 3 until confirmed.

---

### Step 3 — Scan codebase

For each approved theme, use Glob and Grep to identify affected files:
- Search by component names, route paths, function names, and UI labels derived from the theme description
- Identify related test files
- Note any existing TODO / FIXME comments in the area

Read every identified file. Do not propose edits to any file that has not been read.

Read `references/context-augmentation.md` to pack context efficiently for large codebases.

After reading, record for each theme:
- Files confirmed relevant (with a 1-line reason each)
- Files skipped (not relevant after reading)
- Test coverage status (covered / partial / none)

---

### Step 4 — Propose edits *(human gate)*

For each theme (highest severity first), produce exactly 3 options. Read `references/edit-proposal-template.md` for the required format.

- **Option A — Minimal:** targeted patch, narrowest scope, lowest risk
- **Option B — Structural refactor:** addresses root cause, moderate scope
- **Option C — Architectural:** most comprehensive, highest scope

Each option must include:
1. File(s) affected (list every file)
2. Nature of change: add / modify / delete / extract / move
3. Two-sentence rationale quoting or directly referencing the original feedback words
4. Risk flag: "⚠ Touches shared code" or "⚠ No test coverage" where applicable

**→ Human gate:** Present all proposals. Ask: "Which options should I implement? (e.g. Theme 1: B, Theme 2: A)"

Do not implement anything until explicit option selections are received.

---

### Step 5 — Implement (only if approved)

Apply approved proposals atomically — one theme at a time, one file at a time.

Before editing any file with no test coverage: state the gap and recommend writing a test first. Proceed only if the user confirms.

After each theme is complete, note which feedback items from Step 2 it resolves.

---

## Rules

- Never scan the codebase before the Step 2 human gate confirms themes
- Never propose edits to files not read in Step 3
- Never implement without explicit Step 4 approval
- Always produce exactly 3 options (A/B/C) at Step 4 — never a single recommendation
- Single-mention feedback must be flagged, not dropped or silently advanced
- If changed code has no test coverage, flag before editing — do not skip this
- When the user flags something to never do again: update `references/feedback-taxonomy.md` immediately
- When the user approves a final proposal set: save it as an example in `assets/approved-proposals/`

---
<!-- Built with Agent Engineer Master — get your own production-ready skill: www.agentengineermaster.com/skill-engineer -->

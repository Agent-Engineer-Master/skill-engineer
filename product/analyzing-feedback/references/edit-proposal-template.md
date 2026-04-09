# Edit Proposal Template

Use this format exactly for Step 4 output. One block per theme.

---

## Template (repeat per theme)

```
## Theme: [Theme name] — [Severity] | [Pattern count] mentions

Original feedback: "[direct quote or paraphrase from user]"
User intent: [underlying job-to-be-done from taxonomy]

Files confirmed relevant:
- `path/to/file.ext` — [1-line reason]
- `path/to/other.ext` — [1-line reason]
Test coverage: [Covered / Partial / None ⚠]

---

### Option A — Minimal
**Change type:** [add / modify / delete / extract / move]
**Files:** `path/to/file.ext` (lines X–Y if known)
**What:** [1-sentence description of the change]
**Rationale:** [Sentence 1: tie to feedback words.] [Sentence 2: why this scope is sufficient.]
**Risk:** [None / ⚠ Touches shared code / ⚠ No test coverage]

### Option B — Structural refactor
**Change type:** [add / modify / delete / extract / move]
**Files:** `path/to/file.ext`, `path/to/new-file.ext`
**What:** [1-sentence description of the change]
**Rationale:** [Sentence 1: tie to feedback words.] [Sentence 2: why this addresses the root cause.]
**Risk:** [None / ⚠ Touches shared code / ⚠ No test coverage]

### Option C — Architectural
**Change type:** [add / modify / delete / extract / move]
**Files:** [list all affected files]
**What:** [1-sentence description of the change]
**Rationale:** [Sentence 1: tie to feedback words.] [Sentence 2: why this is the most durable fix.]
**Risk:** [None / ⚠ Touches shared code / ⚠ No test coverage / ⚠ Breaking change]
```

---

## Closing gate (after all themes)

End every Step 4 output with:

```
---
**Ready to implement.** Which options should I apply?

Format: "Theme 1: B, Theme 2: A, Theme 3: skip" — or list any adjustments.
```

---

## Implementation summary (Step 5, after each theme)

```
### Implemented: [Theme name] — Option [A/B/C]

- Modified: `path/to/file.ext`
- Added: `path/to/new-file.ext`
- Resolves feedback: [quote the original feedback items this closes]
- Test coverage note: [Existing tests cover this / ⚠ No tests — recommend adding before merging]
```

---

## Notes on rationale quality

Good rationale quotes or paraphrases the user's actual words:
> ✅ "Users said 'I can't find the settings' — this moves the settings link to the primary nav, eliminating the navigation step that caused confusion."

Weak rationale is generic:
> ❌ "This improves the user experience by making the UI more intuitive."

The rationale must make the connection between the feedback and the proposed change self-evident to anyone who reads it without context.

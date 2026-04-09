# Feedback Taxonomy

Reference for Step 2 categorization. Update this file — never SKILL.md — when rules need changing.

---

## Categories

| Category | Definition | Example feedback |
|----------|-----------|-----------------|
| **UX** | Interaction, navigation, layout, clarity, labelling | "I can't find the settings", "the button is confusing" |
| **Performance** | Speed, loading time, responsiveness, memory | "it takes forever to load", "the app freezes" |
| **Bug** | Broken functionality, incorrect output, crashes | "the submit button doesn't work", "I get an error" |
| **Feature** | Missing capability the user wants added | "I wish I could export to CSV", "add dark mode" |
| **Content** | Copy, error messages, labels, empty states, onboarding text | "the error message makes no sense", "I don't understand the instructions" |
| **Other** | Pricing, account, business model, support — not codebase-addressable | "it's too expensive", "support never replied" |

*Note: "Other" items should be flagged to the user but not advanced to codebase scanning.*

---

## Severity tiers

| Tier | Criteria | Response obligation |
|------|----------|-------------------|
| **Critical** | Blocks core user journey; data loss risk; affects majority of users | Advance regardless of pattern count; propose fix in current session |
| **Important** | Degrades core experience; workaround exists but is painful | Advance if 2+ independent mentions |
| **Minor** | Cosmetic, edge case, or preference | Advance only if 3+ independent mentions |

---

## Pattern threshold

- **2+ independent mentions** (different users/sources, not the same person twice): advance at Important or Minor
- **1 mention + Critical severity**: advance
- **1 mention only + Important or Minor**: flag as single-mention, do not advance without user override

Single-mention flag format:
> ⚠ Single mention: "[feedback]" — flagged but not advanced. Override? (y/n)

---

## User intent extraction (job-to-be-done)

Translate the literal request into the underlying job. This is the rationale anchor for proposals.

| Literal feedback | Underlying intent |
|-----------------|------------------|
| "make it faster" | Complete [task] without waiting |
| "I can't find X" | Navigate to [feature] without friction |
| "the error message is confusing" | Understand what went wrong and how to fix it |
| "add [feature]" | Accomplish [goal] without a workaround |
| "it crashes when I do X" | Complete [action] reliably |

Always restate feedback as intent before scanning the codebase.

---

## Negative triggers — do NOT activate this skill for

| Input type | Use instead |
|-----------|-------------|
| Internal PR comments / code review feedback from a developer | `receiving-code-review` |
| Bug reports with stack traces, error logs, or reproduction steps | `systematic-debugging` |
| Feature requests written as a formal spec or PRD | `prd` |
| Performance profiling data (flamegraphs, benchmarks) | `systematic-debugging` |
| Feedback about pricing, support, or business model | No skill — flag to human |

---

## Known anti-patterns (update when user flags issues)

*Empty — populate as the skill is used.*

Format: `YYYY-MM-DD: [what to never do] — [why]`

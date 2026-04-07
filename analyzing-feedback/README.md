# Analyzing Feedback

> Parse raw customer feedback (app reviews, support tickets, transcripts) into severity-ranked themes, scan the codebase to identify affected files, and propose 3 structural edit options per theme — minimal, refactor, or architectural

**Target user:** Developers and product engineers who have customer feedback and need to turn it into concrete, file-level code change proposals

## Install

```bash
cp SKILL.md ~/.claude/skills/
```

Reload Claude Code. Trigger phrase: `here's some customer feedback what should I change / I have app reviews help me prioritize what to fix / translate this user feedback into code changes`

## Example

**Input:**
```
"The checkout keeps freezing on mobile" (14 mentions)
"I can't figure out how to remove items from my cart" (8 mentions)
"App crashes when I try to upload a photo" (3 mentions)

```

**Output:**
```
Theme 1 — Checkout freeze (UX/Bug, Critical, 14 mentions)
Option A: Add loading state guard in CheckoutButton.tsx — targeted patch
Option B: Refactor cart submission flow to async with error boundary
Option C: Extract checkout into separate route with independent state tree

```

## Limitations

Requires a codebase to scan — output is file-level proposals, not abstract advice. Works best when feedback includes concrete user actions (what they tried to do), not just outcomes (it's broken).

---

*Built by [Agent Engineer Master](https://agentengineermaster.com) — production-ready Claude Code skills on demand.*
*Every skill is engineered to the AEM production bar: trigger logic, methodology, output contract, and edge case handling. All four. Every time.*

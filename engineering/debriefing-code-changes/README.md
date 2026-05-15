# Debriefing Code Changes

> Debrief an AI-assisted coding session from git diffs or commits, explaining architecture decisions, patterns, caveats, tradeoffs, and generating a practical quiz so the developer actually learns what changed.

**Target user:** Developers using Claude Code or other AI coding agents who ship code faster than they absorb it.

## Install

```bash
cp -r debriefing-code-changes ~/.claude/skills/
```

Reload Claude Code. Trigger phrase: `debrief what I just built / learn from this diff / explain my last commit / quiz me on this AI-coded change`

## Example

**Input:**
```
I just vibe coded a checkout refactor with Claude. Debrief me on the last commit and quiz me so I actually learn it.
```

**Output:**
```
Start with the diff, not the chat transcript. The report identifies the 3-7 files worth understanding, explains the design rationale and tradeoffs per file, calls out edge cases/performance/security/tech debt, maps only evidence-backed concepts, then quizzes you on the actual change.
```

## Limitations

Requires a concrete git diff, commit range, or PR. Does not replace security review, deploy approval, or bug fixing. Large diffs may need narrowing to the highest-learning-value files.

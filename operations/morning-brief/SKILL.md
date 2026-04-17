---
name: morning-brief
description: >
  Generates a structured morning brief and writes it to the daily review file.
  Pulls from: current priorities (goals summary), active task board, latest competitor
  digest, and content pipeline status. Fires automatically on weekdays. Output is
  the morning intention section of your daily review file.
argument-hint: "(no arguments needed — runs automatically)"
triggers:
  - "run morning brief"
  - "morning brief"
  - "generate morning brief"
  - "/morning-brief"
---

# /morning-brief — Daily Morning Brief

Generate a structured morning brief and write it to today's daily review file.

---

## Instructions

### Step 1 — Establish today's date

```bash
date +%Y-%m-%d
```

Use the output as `TODAY` (format: `YYYY-MM-DD`). Also derive:
- `DAY_NAME` — full weekday name (Monday, Tuesday, etc.)
- `MONTH_NAME` — full month name
- `DAY_NUM` — day of month

---

### Step 2 — Read context sources (run all reads in parallel)

1. **Goals summary** — your goals summary file (e.g. `goals/_summary.md`)
   Extract: This Month's Top Priorities list (the numbered items)

2. **Task board** — your task board index (e.g. `tasks/_index.md`)
   Extract: All Active Tasks where status is `active` or `in-progress`, priority is `critical` or `high`. Include agent and ID.

3. **Latest competitor digest** — find the most recent file in your competitor digests directory (e.g. `network/competitors/digests/`)
   Extract: Top 2–3 signals only. Look for "Key Signals", "Top Signals", or the first substantive section. Skip boilerplate.

4. **Content pipeline** — your content pipeline index (e.g. `content/posts/_posts-index.md`)
   Extract: All posts with stage READY or SCHEDULED. Note the next post due if any has a date.

---

### Step 3 — Compose the brief

Build a brief with exactly these sections, in this order:

```markdown
---
date: YYYY-MM-DD
day: DAY_NAME
type: daily-review
---

# Morning Brief — DAY_NAME, MONTH_NAME DAY_NUM, YEAR

## Top Priorities
[Numbered list pulled from monthly priorities in goals summary — max 5 items]

## Active Tasks (High/Critical)
[Table or bullet list: ID | Title | Agent — only critical and high priority active tasks]

## Competitor Signal
[2–3 bullet points from latest digest. Include digest date. If no digest from last 2 days, note it.]

## Content Pipeline
[READY posts: list with IDs and titles]
[SCHEDULED posts: list with IDs, titles, and scheduled dates if known]
[Note: if pipeline is empty or all posts are in IDEA/DRAFT, flag it]

## One Focus
[Single most important thing to do today, derived from priorities + task board. One sentence, direct.]
```

Keep the brief tight. No padding. The goal is to read it in under 2 minutes.

---

### Step 4 — Write to the daily review file

Target path: your daily review directory (e.g. `reviews/daily/YYYY-MM-DD.md`)

- **If the file does not exist:** write the full brief as the file content.
- **If the file already exists:** prepend the brief above any existing content, separated by `---`.

Do not overwrite existing evening reflection or other content.

---

### Step 5 — Confirm

Output to the chat:
- Confirmation that the brief was written, with the file path
- The "One Focus" line so it's visible without opening the file

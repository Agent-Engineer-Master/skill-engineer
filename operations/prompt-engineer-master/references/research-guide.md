# Research Guide — prompt-engineer-master

Reference for Step 2 of the prompt-engineer-master skill. Read this file when running the research phase.

---

## §1 — When to run research

**Run research** for: agent prompts, system prompts, multi-source workflows, prompts involving tools or irreversible actions — i.e., anything that would use layered XML architecture.

**Skip research** for: simple single-purpose task prompts (summarisation, classification, extraction) — i.e., anything that would use lightweight 5-section prose structure.

**Edge case — "improve this existing prompt" with no new domain context:** run Track A (prior art) only; skip Track B (domain research).

---

## §2 — Track A: Prior Art Research (run inline)

Run these WebSearch/WebFetch calls **in parallel**. Construct queries from the use-case domain extracted in Step 1 (e.g., "customer support AI", "code review agent", "HR policy Q&A").

**Source 1 — Anthropic resources:**
- `WebFetch https://docs.anthropic.com/en/resources/prompt-library` — scan for related use case
- `WebSearch site:github.com/anthropics "system prompt" "[use case]"` — Anthropic cookbook examples

**Source 2 — GitHub system prompt repos:**
- `WebSearch site:github.com "system prompt" "[use case domain]" filetype:md`
- High-signal repos to check: `f/awesome-chatgpt-prompts`, `mustvlad/ChatGPT-System-Prompts`, `LouisShark/ChatGPT_system_prompt`

**Source 3 — Community prompt repos:**
- `WebSearch promptbase.com "[use case]" system prompt`

**Source 4 — Community discussion:**
- `WebSearch site:reddit.com/r/PromptEngineering "[use case]" system prompt best practices`
- `WebSearch site:reddit.com/r/ClaudeAI "[use case]" system prompt`

**Synthesis format — hard cap: max 4 rows:**
```
| Source | Pattern | Signal | Worth adopting? |
|--------|---------|--------|----------------|
| [source name] | [structural pattern observed] | [official/N stars/N votes] | Yes/No — [one-line reason] |
```

Follow with:
- **Patterns to incorporate:** 2–3 bullets
- **Gaps (what none cover):** 1 bullet — this becomes the differentiator

---

## §3 — Track B: Domain Research (spawn librarian sub-agent)

**Full-complexity prompts** (tools, irreversible actions, multi-source): run all 3 modes below.

**Simpler agent prompts** (no tools, single domain): run Mode 2 only to keep sessions fast.

---

Spawn a sub-agent using the instructions in `agents/librarian.md`. Pass the following prompt, filling in `[domain]` and `[domain-slug]`:

> You are running domain research for the prompt-engineer-master skill. The use case is: **[domain — e.g., "customer support AI", "code review agent"]**
>
> Run the following modes and consolidate into a single report:
>
> **Mode 1 (Trending — full-complexity only):**
> Run WebSearch queries targeting the last 30 days for `[domain] AI prompting best practices` and `[domain] AI agent failures`. Use date filters where available. Surface what practitioners are actively discussing, debating, or discovering.
>
> **Mode 2 (Deep Web):**
> WebSearch + WebFetch for: what makes [domain] AI agents succeed, common failure modes in [domain] AI, expert opinions on prompting for [domain], established frameworks and vocabulary practitioners use.
>
> **Mode 3 (YouTube — full-complexity only):**
> Search for 3–4 recent practitioner videos on [domain] AI assistants or automation. Fetch and summarise transcripts. Prefer recent, high-view, practitioner content over explainers.
>
> **Output — produce a report with exactly these four sections:**
> 1. **Reliable approaches:** what practitioners consistently do well when building [domain] AI agents
> 2. **Failure modes:** the most common mistakes or failure patterns in [domain] AI systems
> 3. **Vocabulary and frameworks:** standard terminology a prompt for this domain should use
> 4. **Recent developments:** anything from the last 30 days worth baking into the prompt
>
> Save the full report to `research/YYYY-MM-DD-[domain-slug]-prompt-research.md`.
> Return the file path when done.

---

## §4 — Synthesis block format (present to user before Step 3)

Hard cap: max 4 rows in table, max 3 bullets per section.

```
Research synthesis — [prompt topic]

| Source | Key findings |
|--------|-------------|
| Prior art (Track A) | [structural patterns found, gaps] |
| Trending / community | [emerging techniques, vocabulary] |
| Deep web + YouTube | [best practices, failure modes] |

What to do: [2–3 bullets]
Failure modes to name in known_failure_patterns (Step 4): [2–3 bullets — feeds directly into quality rules step]
Differentiator (what none cover): [1 bullet]
```

The "Failure modes to name" line is a direct mechanical feed into Step 4. Do not omit it.

---

## §5 — Failure handling

- If Anthropic docs return 404 or are unavailable: skip and note in synthesis block.
- If librarian cannot complete all modes: use whatever it returned; note skipped modes in synthesis block.
- Never block prompt generation on research failure — degrade gracefully and proceed.

# prompt-engineer-master

Creates robust long-form task prompts and agent briefs using production prompt engineering patterns — layered XML architecture, trust boundaries, anti-rationalization rules, and numeric anchors.

## When to use

Invoke when you need to:
- Create an agent or system prompt
- Write a complex task prompt for a multi-source or tool-using workflow
- Design a multi-agent workflow prompt
- Produce prompts that are clearer, more reliable, and easier to debug

**Do NOT invoke for:** short single-turn prompts, simple rewrites, explaining prompt engineering concepts, or editing existing prose that is not a prompt.

## What it produces

A single copy-pasteable prompt block — either **Variant A (XML layered architecture)** or **Variant B (clean prose)** — plus optional usage notes. For agent/system prompts, both variants are delivered so you can choose.

## Structure

```
prompt-engineer-master/
  SKILL.md                         — skill instructions and step-by-step workflow
  agents/
    librarian.md                   — embedded research sub-agent definition
  references/
    prompt-engineer-master.txt     — canonical patterns: XML skeleton, real-world examples, production checklist
    research-guide.md              — query specs and librarian agent prompt for Step 2 research
    example-outputs.md             — concrete input → output pairs by agent type
    learnings.md                   — accumulated learnings (update as you use the skill)
    edge-cases.md                  — specific exceptions discovered during use
  assets/
    approved-examples/             — growing library of approved prompt outputs (add yours here)
  evals/
    evals.json                     — eval assertions for automated quality checking
```

## Sub-agent: Librarian

For complex agent prompts (Step 2), the skill spawns a **Librarian sub-agent** (`agents/librarian.md`) to run parallel domain research:
- **Trending:** surfaces what practitioners are discussing in the last 30 days
- **Deep web:** finds best practices, failure modes, and domain vocabulary
- **YouTube:** extracts practitioner insights from video transcripts (using NotebookLM or youtube_transcript_api)

For simple task prompts, the research step is skipped entirely.

## Quick start

1. Describe what you need ("Create a system prompt for a customer support agent that can look up orders and issue refunds")
2. The skill gathers context, runs research for complex prompts, selects structure, and delivers Variant A + Variant B
3. Choose your variant or merge elements from both
4. Optionally run the 10-point production checklist before shipping

---

*Part of the [Skill Engineer](https://agentengineermaster.com) shared skills library.*

# AI Agent Skills Library – Executable Workflows for LLMs

A curated, production-grade library of structured skills for AI agents. Drop any skill into your Claude Code project and invoke it immediately. Built and maintained by [Skill Engineer](https://agentengineermaster.com).

---

## What This Is

This repository contains structured, executable skills for AI agents — self-contained workflow definitions that any Claude Code instance can load and run. Each skill encodes a repeatable, expert-level process as a machine-readable SKILL.md file: triggers, inputs, step-by-step execution logic, outputs, and validation rules.

If you work with AI agents, LLM workflows, or prompt engineering, these skills save you from writing complex context from scratch. Instead of prompting from zero, you load a skill and invoke a proven workflow. Think of this library as reusable agent workflows — the equivalent of a shared component library, but for AI reasoning and execution patterns.

Keywords this library covers: AI agents, LLM workflows, prompt engineering, Claude skills, Copilot skills, reusable agent workflows, context engineering, autonomous agents, workflow automation.

---

## How Skills Work

Each skill lives in a subfolder inside its domain directory. The entry point is always `SKILL.md`.

### SKILL.md Structure

**Frontmatter (YAML):**

```yaml
---
name: skill-folder-name
description: One-sentence description of what the skill does and when to trigger it.
argument-hint: "[optional argument format]"
triggers:
  - "trigger phrase 1"
  - "/slash-command"
---
```

**Body sections:**

| Section | Purpose |
|---|---|
| When to use | Exact conditions that should trigger this skill (and explicit do-not-use cases) |
| Inputs | Required and optional parameters |
| Steps | Numbered execution phases — what the agent does, in order |
| Outputs | What gets produced: files, reports, structured data |
| Validation | How the agent self-checks its output before returning |
| Rules | Hard constraints the agent must not violate |

Each skill is self-contained and loadable by any Claude Code instance. No dependencies on external services unless explicitly documented in the skill.

---

## Skill Domains

### design/
Presentation and visual asset creation skills for designers and creative teams.

| Skill | Description | When to Use |
|---|---|---|
| [marp-slides](design/marp-slides/) | Creates MARP presentation decks (.md files rendered to PDF/HTML/PPTX via marp CLI) with custom CSS themes, SVG inline charts, dashboard components, and speaker notes | Creating slides, building a deck, making a presentation, generating MARP output, editing existing slides |

---

### engineering/
Code quality, security, and debugging skills for software engineers and technical teams.

| Skill | Description | When to Use |
|---|---|---|
| [fix-from-logs](engineering/fix-from-logs/) | Diagnoses bugs from raw error logs, stack traces, or CI failure output — triages and clusters errors, localizes root cause, proposes a fix + regression test | User pastes logs and wants the underlying bug fixed with tests |
| [security-mindset-master](engineering/security-mindset-master/) | Gates implementation of API endpoints, auth logic, database queries, and user input handling with threat surface analysis, secure defaults verification, and attacker's eye pass | Implementing or modifying any feature that stores or transmits user data |

---

### legal/
Compliance and regulatory assessment skills for legal and risk teams.

| Skill | Description | When to Use |
|---|---|---|
| [compliance-check](legal/compliance-check/) | Assesses US regulatory compliance likelihood for any consumer product before listing for US sale — classifies product, determines applicable standards, produces a structured verdict | Before listing any consumer product for US sale |

---

### marketing/
Go-to-market, brand, and competitive analysis skills for marketing teams.

| Skill | Description | When to Use |
|---|---|---|
| [analyzing-dtc-stores](marketing/analyzing-dtc-stores/) | Produces an investor-grade teardown of a DTC brand from its public URL, covering brand, market, unit economics, supply chain, channel mix, marketing, and agentic-commerce readiness | DTC teardown, brand teardown, competitor analysis, investor memo |
| [audit-brand](marketing/audit-brand/) | Audits and evolves brand positioning, voice consistency, and messaging for an existing brand — runs a structured audit and produces a scorecard with fix recommendations | Brand health checks, positioning refreshes, messaging framework development |
| [marketing-plan](marketing/marketing-plan/) | Develops a full go-to-market marketing plan covering ICP, competitive landscape, channel strategy, budget allocation, pricing, content strategy, and 90-day launch timeline | "Build a marketing plan", "create a GTM strategy", planning a product launch |

---

### operations/
Strategic analysis, planning, and research optimization skills for operations teams.

| Skill | Description | When to Use |
|---|---|---|
| [auto-research](operations/auto-research/) | Autonomously optimizes any Claude skill (SKILL.md) or CLAUDE.md file through a closed hypothesis→test→evaluate→keep/discard loop | Improving a skill's output quality against measurable criteria |
| [morning-brief](operations/morning-brief/) | Generates a structured morning brief from current priorities, active task board, competitor digest, and content pipeline status | Daily morning planning, intention setting |
| [stress-test](operations/stress-test/) | Three-phase strategic decision analysis combining verbalized sampling, customizable analytical lenses, and a structured decision brief — surfaces non-obvious tail-distribution insights | Any high-stakes decision: pivots, category selection, positioning, pricing, hiring |

---

### product/
User research, feedback analysis, and idea validation skills for product teams.

| Skill | Description | When to Use |
|---|---|---|
| [analyzing-feedback](product/analyzing-feedback/) | Parses raw customer feedback into categorized severity-ranked themes, scans the codebase to identify affected files, and proposes 3 structural edit options per theme | Translating customer complaints into file-level engineering proposals |
| [find-my-business](product/find-my-business/) | Guides a founder from "no idea" through idea generation, rapid validation, and commitment to a business — synthesizing PG, YC, Lean Startup, Mom Test, and JTBD methodology | Finding a business to start, exploring startup ideas, getting unstuck on what to build |

---

## Example Skill (Inline): `operations/stress-test`

**Trigger:** `/stress-test [decision or choice to analyse]`

**What it does:** Runs a three-phase strategic decision analysis. Phase 1 uses verbalized sampling across four analytical lenses (quantitative, strategic, risk-first, contrarian) to surface non-obvious insights that mode-collapsed prompting suppresses. Phase 2 synthesizes into a decision brief with a recommendation and confidence level. Phase 3 runs a critic pass to stress-test the brief.

**Example usage:**
```
/stress-test should I enter the home wellness category or stay narrower?
/stress-test hire a contractor now vs wait until revenue hits $10k/mo
/stress-test two content formats: long-form carousel vs short-form daily posts
```

**Output format:** Structured markdown decision brief — verbalized sampling outputs per perspective, synthesis narrative, ranked options with rationale, recommendation with confidence level, and critic objections addressed.

---

## How to Use

### 1. Developer: copy a skill into your project

Copy any skill folder into `.claude/skills/` in your project:

```bash
cp -r operations/stress-test /your-project/.claude/skills/stress-test
```

Then invoke it in Claude Code:

```
/stress-test should I build this feature in-house or use a third-party API?
```

Claude Code auto-discovers SKILL.md files in `.claude/skills/` and registers them as slash commands. No configuration required.

### 2. AI agent platform: load as a tool definition

Each SKILL.md is structured to load cleanly as a tool definition for any LLM-based agent platform:

- Parse the YAML frontmatter for `name`, `description`, `triggers`, and `argument-hint`
- Load the body as the tool's system prompt or instruction block
- Use `skills-index.json` at the repo root for programmatic discovery — it contains every skill's name, path, domain, description, and tags in a machine-readable array

```json
// skills-index.json entry example
{
  "name": "stress-test",
  "path": "operations/stress-test",
  "domain": "operations",
  "description": "Three-phase strategic decision analysis...",
  "tags": ["decision-analysis", "strategy", "verbalized-sampling", "founder", "risk-assessment"]
}
```

---

## Get a Custom Skill Built

Need a skill that isn't in this library? [Skill Engineer](https://agentengineermaster.com) builds custom skills to the same production standard — structured, tested, and ready to drop into any Claude Code project.

Commission a custom skill at **https://agentengineermaster.com**

---

## Keywords

This library covers AI agent skills, LLM workflows, prompt engineering framework, reusable agent workflows, and context engineering patterns for production use. It includes Claude Code skills structured for immediate slash-command invocation, GitHub Copilot skills loadable via tool definitions, and autonomous AI agents workflows spanning marketing, engineering, product, legal, design, and operations. Use this library to accelerate workflow automation with proven, expert-encoded skill definitions — a structured skill library built for any team deploying AI agents at scale.

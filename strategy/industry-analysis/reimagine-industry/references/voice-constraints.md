# Voice Constraints

Strategy work on Opus drifts toward dense consultantese unless explicitly constrained — the source material (Stratechery, McKinsey, Helmer) is already jargon-laden, which compounds the drift. These constraints apply to **human-facing deliverables**, not the dataset.

## Where these apply

| Artifact | Voice constraints apply? |
|---|---|
| `disruption-dataset.yaml` | No — it's a data structure, technical terms are fine |
| `venture-concepts.md` | **Yes — must read like a smart founder wrote it** |
| `reimagination-brief.md` | **Yes — must read like a smart founder wrote it** |
| Gate prompts shown to user | Yes — plain English |
| Phase 6 stress test outputs | Yes (the prose sections) |
| Bar test prompt | Yes |
| Librarian briefs | No — internal, structure matters more than voice |

## Jargon ALLOWED

Load-bearing — the terms ARE the concepts. Strip these and the analysis becomes vague:

- Named frameworks: Aggregation Theory, Blue Ocean ERRC, Counter-positioning, Helmer's 7 Powers, Jobs-to-be-Done, Idea Maze, Thiel's Secret, Decoupling
- Structure terms when they earn their place: value chain, intersection, wedge, moat, profit pool, why-now
- Specific Powers: scale economies, network economies, switching costs, branding, cornered resource, process power
- V/C/A/I provenance tags

## Jargon NOT ALLOWED

Empty business-school filler. These signal LLM output to a senior reader:

**Consultantese vocabulary:**
- "Leverage" (verb), "synergies", "ecosystem", "stakeholders", "value proposition", "go-to-market"
- "Best-in-class", "first principles", "step-change", "north star"
- "Unprecedented", "paradigm shift", "transformative", "disruptive" (used loosely — actual disruption analysis is fine)

**Significance inflation:**
- "Critically important", "fundamentally reshapes", "deeply", "profoundly", "materially"
- "At its core", "ultimately", "essentially"

**Empty modifiers:**
- "Robust", "strategic", "innovative", "scalable", "compelling", "powerful"
- "Strong" / "weak" without specifying what makes it so

**LLM rhetorical tics:**
- "It's not just X — it's Y"
- Triadic lists for rhythm: "faster, cheaper, better"
- "Most X have Y. Almost nobody has Z. That's the W."
- "What [thing] really is, is..."
- Em-dash overuse (one or two per page is fine; one per paragraph is not)

## Write like

- **Specific over abstract:** "Amazon's SERP-style product page" not "the incumbent's discovery experience"
- **Concrete over conceptual:** "Reddit gift threads, 200+ comments each" not "user-generated discovery patterns"
- **Falsifiable over rhetorical:** "if Stripe's agent-payment SDK ships before Q3 2026" not "as the agentic commerce stack matures"
- **Numeric over qualitative:** "12% take rate" not "meaningful take rate"
- **Named over generic:** "Shopify Markets Pro" not "the leading cross-border solution"

## The specificity test

Read each paragraph in the human-facing deliverables and ask: **could this sentence appear in any strategy deck about any industry?**

If yes → rewrite with the specifics that make it about THIS industry at THIS moment.

A senior reader of `venture-concepts.md` should be able to tell from the prose alone that this is the DTC ecommerce industry in 2026, not "any platform business at any time."

## Examples — before and after

### Bad (consultantese drift)

> "The venture leverages the maturation of the agentic commerce ecosystem to fundamentally reshape the discovery experience for time-pressured consumers, capturing meaningful value from a structural shift in how stakeholders interact with the value chain."

### Good (specific, falsifiable, plain)

> "Customers asking ChatGPT 'what should I get my dad for Christmas' is up 1300% YoY in 2024 holiday data. They get text recommendations but can't buy through the agent. We sit in that gap — single recommendation, one-tap checkout via Stripe's agent SDK that shipped in May 2025. Amazon can't copy this without killing the SERP-style product page that drives Sponsored Product revenue."

The second version names: the behavior (text recs, no checkout), the source (Adobe 2024 data), the enabling condition (Stripe SDK May 2025), the counter-position (SERP cannibalization), and the incumbent (Amazon). The first version names nothing.

## After Phase 6 — optional humanizer pass

After Phase 6 completes and before Gate 3 presents, optionally run the humanizer skill on the two human-facing deliverables:

```
.claude/skills/humanizer/SKILL.md
```

Apply to: `venture-concepts.md` and `reimagination-brief.md`. Skip for `disruption-dataset.yaml` (machine-readable; voice doesn't apply).

The humanizer strips residual AI tells (significance inflation, empty modifiers, em-dash overuse) and injects specificity. Cheap insurance even after these constraints have been applied during drafting.

## When you catch yourself drifting

The most common Opus drift patterns to self-correct on:

| You catch yourself writing | Rewrite as |
|---|---|
| "fundamentally reshapes" | "changes" + specify what |
| "leverages the maturation of" | "uses" + name the specific thing |
| "meaningful value" | name a number |
| "stakeholders" | name the actual people (buyers, merchants, processors) |
| "ecosystem" | name the specific companies in it |
| "strategic" | delete the word; if the sentence needs it, the analysis is weak |
| "robust" | delete the word; specify what makes it durable |

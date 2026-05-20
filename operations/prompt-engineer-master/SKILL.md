---
name: prompt-engineer-master
description: Creates robust long-form task prompts and agent briefs using production prompt engineering patterns (layered XML architecture, trust boundaries, anti-rationalization rules, numeric anchors). Invoke when the user needs to create an agent system prompt, write a complex task prompt, design a multi-agent workflow prompt, or produce prompts that are clearer, more reliable, and easier to debug. Does NOT activate for: short single-turn prompts, simple rewrites, asking Claude to explain prompt engineering concepts, or editing existing prose that is not a prompt.
---

# Prompt Engineer Master

## Output contract
- **Produces:** a single copy-pasteable prompt block in XML or 5-section prose format, plus optional usage notes
- **Does NOT produce:** implementation code, prompt evaluation reports, prompt explanations, or multi-turn dialogue scaffolds
- **Enables:** the user or calling agent to paste the output directly into a system prompt, agent config, or project instruction file
- **Consumed by:** the user directly, or an agent pipeline that needs a system prompt as input

## Canonical source
Read `references/prompt-engineer-master.txt` before generating any prompt — it contains the production patterns, XML skeleton, real-world examples, and the 10-point production checklist to adapt from.

## Step 1 — Gather context (skip if sufficient detail already given)
Ask at most 3 clarifying questions. Only ask if the answer would materially change the prompt:
- What is the *task* and the *deliverable*?
- What is the *audience* and *success criteria*?
- Any *constraints* — tools available, tone, forbidden items, or trust level of inputs (user-typed vs server-injected vs retrieved from docs)?

If the user has given enough detail, proceed immediately to Step 2.

## Step 2 — Research prior art and domain context

**Skip this step** if the request is for a simple single-purpose task prompt (single-source, no tools, no irreversible actions — i.e., anything that would use lightweight 5-section prose structure). Go directly to Step 3.

Read `references/research-guide.md` for full query specs, librarian sub-agent prompt, and synthesis format.

Run two tracks in parallel:

**Track A — Prior art (inline):** Search for existing prompts in this domain. Sources: Anthropic prompt library, GitHub system prompt repos, community repos, r/PromptEngineering. See research-guide.md §2 for queries.

**Track B — Domain research (spawn librarian sub-agent):** Read `agents/librarian.md` and spawn a sub-agent using those instructions. Research what makes this task domain work well — best practices, failure modes, practitioner vocabulary. Use the librarian agent prompt in research-guide.md §3.

Wait for both tracks. Present the synthesis block (format in research-guide.md §4) before proceeding. Save results to `research/YYYY-MM-DD-[domain-slug]-prompt-research.md`.

## Step 3 — Select structure
**Sub-check: classify each input before selecting structure.**
Separate inputs into:
- **Static** (system prompt / cache candidate) — domain knowledge, schema definitions, policy, background context that never changes between calls
- **Dynamic** (user turn / per-call payload) — user requests, images, retrieved documents, per-request data

Static inputs belong in the system prompt; dynamic inputs belong in the user turn. Conflating them wastes tokens and degrades performance. A stable static prefix is the natural prompt caching target.

Choose based on complexity:

**Use layered XML architecture** (from canonical reference) when:
- The prompt is for an agent or system prompt
- It will receive multi-source inputs (user input + retrieved docs + server context)
- It involves irreversible or externally visible actions
- It needs explicit tool policy or trust boundaries

Required XML sections: `<role>`, `<operating_policy>`, `<tool_policy>`, `<retrieved_context_policy>`, `<risk_policy>`, `<output_contract>`, `<known_failure_patterns>`

**Use lightweight 5-section prose** (Role, Objective, Steps, Output Format, Rules) when:
- The prompt is a simple single-purpose task (summarisation, classification, extraction)
- There is one input source with no trust boundary concerns
- No tools or irreversible actions involved

Do not over-engineer a prompt that does not need layering. If Step 2 prior art found a dominant structural pattern for this use case, weight that pattern in this decision.

## Step 4 — Apply mandatory quality rules
Apply these to every generated prompt regardless of structure:

**Failure patterns section is required.**
Name specific shortcuts the model is likely to take — not just desired behaviour.
Wrong: "Verify your work." Right: "Do not claim success from reading code alone — run the check."
Seed this section with the failure modes surfaced in Step 2 domain research, not just the generic patterns below.

**Use numeric anchors, not vague style.**
Wrong: "Be concise." Right: "At most one sentence before tool calls; at most three sentences after."
Wrong: "Return structured output." Right: exact ordered section list.

**Motivate non-obvious rules.**
State the rule, then add a Why: line (the tradeoff or reason) and a How to apply: line (when it fires).
This lets the model judge edge cases rather than follow blindly.

**Separate trust levels when inputs come from multiple sources.**
Use distinct XML blocks for: system policy, trusted runtime context, untrusted retrieved context, user request.
Never mix them in one block.

**Instruction order encodes epistemics, not style.**
When the prompt involves multiple input sources, state the processing order explicitly — the order determines what context is available at each inference step.
Wrong: "Analyze the document and the sketch." Right: "First examine the document and list what you find. Then analyze the sketch in light of what you learned from the document."
This matters especially for image analysis, multi-document reasoning, and any task where one source provides context for interpreting another.

**For production prompts, the approved-examples set is the compounding asset.**
`assets/approved-examples/` is not just initial build material — it is the long-tail edge-case library. For hard cases or gray areas, add a labeled few-shot example rather than editing prose rules. Prose rules are ignored under pressure; examples are always referenced.

**Use prefilled responses for machine-consumed structured outputs.**
For outputs consumed by applications (not humans), prefix the assistant turn with the opening tag or bracket to eliminate preamble and guarantee format compliance.
Pattern: if the output should be wrapped in `<verdict>`, start the assistant turn with `<verdict>` — Claude completes it without prose prefix.
Note: prefilling bypasses reasoning narration — only use it when output is parsed programmatically. For human-readable outputs, specify format in the output contract instead.

**For agent prompts: treat every tool definition as a colleague API.**
The model reads tool definitions the same way it reads instructions — vague definitions produce inconsistent calls. When generating a `<tool_policy>` section, every tool must have:
- A one-sentence purpose description stating what it does, what it returns, and when to use it
- Descriptive parameter names (not `a`, `b`, `x`, `data`) that make the parameter's role self-evident
- A per-parameter description and, where non-obvious, an example value
- A usage constraint if relevant: when NOT to call it, rate limits, caching behaviour

Wrong: `fetch_data(a, b)` — "Gets data"
Right: `fetch_product_page(supplier_id: str, sku: str)` — "Fetches a live listing from the supplier API for a specific SKU. Returns price, stock, and shipping options. Call once per SKU per session — results are cached for 24h. Do not call during price validation; use the cached snapshot instead."

## Step 5 — Select agent-type template (if applicable)
For known agent types, adapt from the corresponding real-world example in the canonical reference:
- **Coding agent** — rules of engagement + failure patterns + numeric response style
- **RAG / document analyst** — trust boundaries + evidence-only answers + exact output sections
- **Support action agent** — permission verification + risk policy + action confirmation
- **Multi-agent orchestrator** — decomposition + delegation policy + worker prompt pattern

For high-stakes work, recommend the Verifier Pattern (Planner / Executor / Verifier split) from the canonical reference.

## Step 6 — Deliver variants for agent/system prompts
For simple task prompts: deliver one output.

For agent or system prompts, deliver **two structural variants** so the user can choose:
- **Variant A — XML architecture:** full layered structure with explicit section tags
- **Variant B — Clean prose:** same semantic content rendered as readable prose sections (for teams that find XML heavy in their toolchain)

Present both variants, then ask the user which to keep or whether to merge elements from both.

See `references/example-outputs.md` for sample inputs and their expected variant outputs by agent type.

## Step 7 — Offer production checklist
For prompts destined for production systems, offer to run the 10-point production checklist from the canonical reference as a self-audit step. Do not run it unsolicited for quick or exploratory prompts.

For complex reasoning tasks, also offer the extended thinking diagnostic: enable extended thinking once, read the scratchpad to surface Claude's implicit reasoning steps, then encode those steps as explicit instructions in the prompt. Disable extended thinking in production — the goal is to extract its reasoning into the prompt itself, not to ship with it on.

## Self-improvement
- When the user flags a generated pattern as wrong or suboptimal, update the relevant rule in this SKILL.md or `references/prompt-engineer-master.txt` immediately.
- When the user approves a final generated prompt, save it to `assets/approved-examples/` with the input context noted as a comment at the top.

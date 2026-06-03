# Worked Examples — Pass / Fail by Dimension

Concrete examples for each rubric dimension, both passes. Each example shows the failing pattern and the corrected version. Reviewers use these when interpretation is ambiguous; the calling skill uses them (alongside `fix-patterns.md`) when uncertain how a fix should look.

---

## Full four-stage flow — `reimagine-industry` calling all modes

The canonical end-to-end demonstration. The upstream skill is `reimagine-industry`; the document being produced is the executive brief for a DTC ecommerce reimagination. Strictness is `standard`.

### Stage 0 — Pick the structural framework

`reimagine-industry` produces a recommendation-driven brief. Per `references/framework-selection-guide.md`, the default framework for `doc_type: brief` is `minto-pyramid`. The reimagine brief recommends an action (which venture concepts to ship) but is not itself a strategy document with a Rumelt kernel — `minto-pyramid` is the right choice. No override needed.

### Stage 1 — `mode: spec`

```text
Task(subagent_type="claude-orchestrator", prompt=f"""
Read .claude/skills/analysis-quality-review/SKILL.md and run with:

mode: spec
doc_type: brief
structural_framework: minto-pyramid
strictness: standard
caller_skill: reimagine-industry
""")

# Response:
#   TEMPLATE_PATH: .claude/skills/analysis-quality-review/references/authoring-templates/minto-pyramid.md
```

The caller reads the framework-matched template, fills in D1 (governing observation), D2 (3-5 MECE axes), D3 (SCQA opening), D5 evidence inventory and handles — using its subject context (the dataset, supporting working files, scope question). It writes the filled-in spec to `tasks/reimagine-industry/dtc-ecommerce-us/working/authoring-spec.md`.

(If `reimagine-industry` were producing a strategy document — e.g., the AEM go-to-market strategy — it would pick `structural_framework: rumelt-kernel` instead, and the template would be the kernel-shaped one with diagnosis + guiding policy + coherent actions sections.)

### Stage 2 — `mode: spec-judge` (loop)

**First iteration:**

```text
Task(subagent_type="claude-orchestrator", prompt=f"""
Read .claude/skills/analysis-quality-review/SKILL.md and run with:

mode: spec-judge
doc_type: brief
structural_framework: minto-pyramid
strictness: standard
iteration: 1
spec_path: tasks/reimagine-industry/dtc-ecommerce-us/working/authoring-spec.md
template_path: .claude/skills/analysis-quality-review/references/authoring-templates/minto-pyramid.md
caller_skill: reimagine-industry

supporting_artifacts:
  - path: 08-knowledge/world-model/industries/dtc-ecommerce-us/disruption-dataset.yaml
    role: source-of-truth
    description: Disruption dataset with 39 framework signals, 6 endorsed Thiel Secrets

intent_summary: |
  Executive brief for DTC ecommerce reimagination in an agentic-commerce world.
  Reader is the founder-COO deciding next-90-days operating priorities.
""")

# Response:
#   PASS: spec-judge
#   VERDICT: FAIL
#   VIOLATION_REPORT_PATH: tasks/analysis-quality-review/dtc-ecommerce-us-20260520/spec-iter1-report.md
#   FIX_PATTERNS_PATH: .claude/skills/analysis-quality-review/references/fix-patterns.md
#   AUDIT_DIR: tasks/analysis-quality-review/dtc-ecommerce-us-20260520/
```

The caller reads the spec-iter1 report. Sees three violations:
- **D1:** Governing observation reads as a question ("how does DTC restructure under agentic commerce?") rather than a claim.
- **D2:** Two axes overlap — "attribution layer" and "measurement infrastructure" are the same axis under different names.
- **D7:** Rumelt diagnosis is missing — guiding policy stated without naming what it answers.

The caller revises the spec. It has the context to stake a specific claim ("Citation surfaces, attribution layers, and vertical supply spines redistribute margin away from horizontal aggregators"), merge the two overlapping axes into one, and write a 2-sentence diagnosis block.

**Second iteration:**

```text
Task(subagent_type="claude-orchestrator", prompt=f"""
Read .claude/skills/analysis-quality-review/SKILL.md and run with:

mode: spec-judge
doc_type: brief
strictness: standard
iteration: 2
spec_path: tasks/reimagine-industry/dtc-ecommerce-us/working/authoring-spec.md
template_path: .claude/skills/analysis-quality-review/references/authoring-templates/brief.md
audit_dir: tasks/analysis-quality-review/dtc-ecommerce-us-20260520/
previous_violations: tasks/analysis-quality-review/dtc-ecommerce-us-20260520/spec-iter1-report.md
caller_skill: reimagine-industry

# manifest unchanged
""")

# Response:
#   PASS: spec-judge
#   VERDICT: PASS
#   VIOLATION_REPORT_PATH: tasks/analysis-quality-review/dtc-ecommerce-us-20260520/spec-iter2-report.md
#   FIX_PATTERNS_PATH: .claude/skills/analysis-quality-review/references/fix-patterns.md
#   AUDIT_DIR: tasks/analysis-quality-review/dtc-ecommerce-us-20260520/
```

Spec is approved. Caller proceeds to writing.

### Stage 3 — Caller writes the document

No invocation of this skill. The calling skill uses the approved spec as scaffolding and generates the executive brief. The brief lives at `08-knowledge/world-model/industries/dtc-ecommerce-us/venture-concepts.md`.

### Stage 4 — `mode: review, pass: 1`

The caller invokes Pass 1 review with the same manifest as Stage 2 (plus the document path). The review pass creates its own audit_dir (separate from the spec-judge audit_dir, both retained for traceability). Loop until PASS, applying fixes from `fix-patterns.md`. Because the spec-judge already caught the structural failures, Pass 1 typically clears in 1-2 iterations rather than 3-5.

### Stage 5 — `mode: review, pass: 2`

Gated on Pass 1 PASS. Same loop pattern for readability dimensions (action titles, so-what, specificity, code/jargon discipline, active voice). The caller applies fixes; reviewer re-grades.

**Token comparison (illustrative, not measured):**

| Without spec stages | With spec stages |
|---|---|
| Write 80K-token document | Write 3K-token spec + judge it (5K) ×2 iterations |
| Pass 1 catches D1/D2/D7 → rewrite large sections (40K) | Spec revised in 3K-token edits |
| Pass 1 re-review (15K) | Spec re-judged (5K) → PASS |
| Pass 1 still failing → another rewrite | Caller writes 80K-token document on approved scaffold |
| ...3-5 iterations | Pass 1 catches residual (10K to fix), 1-2 iterations |
| **Roughly 250-400K tokens** | **Roughly 110-150K tokens** |

The ghost-deck stages move structural failures from the most expensive layer (full-document rewrites) to the cheapest layer (spec edits). This is the dot-dash review discipline operationalized.

---

## Pass 1 — Argument Structure

### D1 — Single Governing Observation

**FAIL pattern (two competing apex claims):**

> # Industrial Robotics — North America Brief
>
> The integrator layer is the most attractive part of the value chain over a 5-year hold.
>
> Software-led entrants will reshape the OEM layer's competitive dynamics.

The reader gets two thesis statements. Which is the brief about? D1 fails.

**PASS pattern:**

> # Industrial Robotics — North America Brief
>
> A roll-up of regional integrators captures the migrating profit pool created by software-led unbundling at the OEM layer.

One sentence, one falsifiable claim, both observations subordinated to a single thesis. D1 passes.

---

### D2 — MECE Supporting Reasons

**FAIL pattern (overlap):**

> ## 1. Market growth
> ## 2. Competitor dynamics
> ## 3. Customer demand
> ## 4. Demand-side trends

Sections 3 and 4 overlap by ~60%. Not mutually exclusive.

**PASS pattern:**

> ## 1. Market is growing (12% CAGR)
> ## 2. Profit is migrating from OEM to integration
> ## 3. Integrator layer is fragmented
> ## 4. Three risks could erode the thesis

Each section addresses a distinct question. ME satisfied. Collectively they answer "is this attractive?" CE satisfied.

---

### D3 — SCQA Opening

**FAIL pattern (no SCQA):**

> # Industrial Robotics Brief
>
> This brief examines the industrial robotics market in North America. It covers market sizing, competitive dynamics, and recommendations.

This is a table-of-contents preamble, not SCQA. No Situation, no Complication, no Question, no Answer.

**PASS pattern:**

> **Situation.** Industrial robotics is a $52B market growing at 12% CAGR, with four global incumbents holding ~60% share.
>
> **Complication.** Software-led entrants are unbundling the controller layer from the hardware, eroding the OEM profit pool.
>
> **Question.** For a sponsor evaluating a roll-up of mid-tier integrators, is industrial robotics structurally attractive over a 5-year hold?
>
> **Answer.** Attractive at the integrator layer, not the OEM layer. Profit is migrating to integration + software, where the industry remains fragmented.

All four SCQA elements present.

---

### D4 — Dot-Dash Narrative

**FAIL pattern (noun-label titles):**

> ## Market
> ## Competitors
> ## Risks
> ## Conclusion

Read alone, these tell no story. D4 fails.

**PASS pattern:**

> ## The market is growing at 12% but the OEM profit pool is shrinking
> ## Three integrators are positioned to consolidate the fragmented mid-tier
> ## The thesis is exposed to regulatory tightening and currency volatility
> ## Acquire two integrators in 2026 to capture the migration

Read alone, the titles deliver the argument. D4 passes.

---

### D5 — Evidence Carries

**FAIL pattern (orphan evidence):**

> ## The integrator layer is fragmented
>
> - Fanuc reported $4B in robotic systems revenue in 2025.
> - The North American market grew 12% in 2025.

Both evidence items relate to robotics but neither establishes integrator-layer fragmentation. D5 fails.

**PASS pattern:**

> ## The integrator layer is fragmented
>
> - Top-5 integrator share is <15% (LEK 2024).
> - 1,200+ regional integrators identified in the NA market (IFR 2025).
> - No integrator above $200M annual revenue in NA.

Each item establishes fragmentation. D5 passes.

---

### D7 — Rumelt Strategy Kernel

**FAIL pattern (goals masquerading as strategy):**

> ## Recommendations
> 1. Become the leading agentic-commerce platform
> 2. Capture 20% market share in 3 years
> 3. Build a world-class team

No diagnosis. No guiding policy. Three goals.

**PASS pattern:**

> **Diagnosis.** The agentic-commerce category is forming around protocols (MCP, A2A) but no standardisation has emerged. The obstacle to a defensible position is that early winners will be selected by the protocol that becomes canonical, not by product quality.
>
> **Guiding policy.** Anchor on a protocol that has Anthropic adoption and align our DTC architecture to it. Concede on protocol neutrality; bet on Anthropic's gravity.
>
> **Coherent actions.**
> 1. Implement MCP-first agent endpoints by Q3.
> 2. Submit our schema as an MCP extension proposal.
> 3. Publish a public reference implementation under MIT license to seed adoption.

Diagnosis identifies the obstacle. Guiding policy is directional and rules out alternatives. Actions implement the policy.

---

## Pass 2 — Readability

### D1 — Action Titles

**FAIL:** `## Recommendations`
**PASS:** `## Acquire two mid-tier integrators in 2026 to capture the integration profit pool.`

**FAIL:** `## Market Overview`
**PASS:** `## The market is consolidating around three integrators.`

**FAIL:** `## Findings and Implications`  (the "and" test)
**PASS:** Split into two sections, one per finding, one per implication.

---

### D2 — So-What Completion

**FAIL:**
> Three of the top 5 incumbents raised capital in Q1 2026.

So what? The reader does not know what to do with this.

**PASS:**
> Three of the top 5 incumbents raised capital in Q1 2026 — meaning the integrator-layer roll-up must move before incumbent capital re-shapes the M&A market.

The implication is explicit.

---

### D3 — Specificity over Abstraction

**FAIL:**
> Various stakeholders have expressed concerns about the new architecture.

**PASS:**
> The procurement team and the CFO flagged concerns about the new architecture, citing the 3-month migration window and the $480K licensing delta.

Named groups, specific concerns, specific numbers.

---

### D4 — Active Voice

**FAIL:** "It is recommended that we acquire two integrators."
**PASS:** "We recommend acquiring two integrators."

**FAIL:** "It has been observed that customers prefer modular pricing."
**PASS:** "Our buyer interviews showed customers prefer modular pricing (8 of 12)."

---

### D5 — Code/Jargon Discipline (load-bearing-aware)

**FAIL pattern (raw codes in narrative prose):**

> SECRET-02 shows that retailers will gain dominance because CP-4 creates switching costs, which means M1-DTC is the strongest concept.

Five internal codes in one sentence. Cognitive overhead for the senior reader.

**PASS pattern (canonical safe fix — handle first, code preserved):**

> The retailer-AI dominance signal (`SECRET-02`) shows that retailers will consolidate market power, because the switching-cost layer (`CP-4`) makes vendor-side moves expensive. The strongest derived concept is the APAC integrator roll-up (`M1-DTC`).

The descriptive handles do the cognitive work; the codes are preserved in parentheses for cross-reference traceability. In subsequent paragraphs, the handles alone are used.

**FAIL pattern (jargon hits):**

> We need to leverage our ecosystem of stakeholders to provide color on the key opportunities.

Five jargon hits in 16 words: "leverage" (verb), "ecosystem" (unspecified actors), "stakeholders" (unspecified groups), "provide color" (signals thin analysis), "key" (meaningless modifier).

**PASS pattern:**

> We need our supplier network (Fanuc, ABB, KUKA) and the procurement team to validate the three integrator targets identified in section 2.

Named actors, named groups, specific scope.

---

### D7 — One-Message Discipline

**FAIL pattern ("and" joining two distinct so-whats in a heading):**

> ## The market is consolidating and the regulatory environment is tightening

Two distinct so-whats. Two distinct fixes. Two distinct sections.

**PASS pattern:**

> ## The market is consolidating around three integrators
>
> [section about consolidation]
>
> ## Regulatory tightening could erode integrator margins by 200-300bps
>
> [section about regulatory risk]

One message per section.

---

## Cross-pass interaction: D1 (structure) and D1 (readability) are not the same

- Structure D1 = "is there ONE governing observation that all sections support?" (apex existence)
- Readability D1 = "are the section TITLES complete-sentence conclusions, not noun labels?" (title form)

A document can pass structure D1 (it has a clear apex) and fail readability D1 (its section titles are still "Market", "Risks", "Recommendations"). It can also pass readability D1 (every title is a complete sentence claim) and fail structure D1 (the titles are claims but they're competing apex claims with no clear governing observation).

---

## Load-bearing element protocol — worked example (call-and-return)

### Scenario: D5 violation touching `concept_ids` at strictness=high, with `reimagine-industry` as the calling skill

**Document line 47 (under review):**

> SECRET-02 (retailer-AI wins) is the strongest signal in this market, and combined with M1-DTC creates a defensible moat.

**Reviewer's violation entry (high strictness, with preservation note):**

```yaml
violation:
  id: V-12
  dimension: D5
  evidence: "venture-concepts.md:47 — SECRET-02 (retailer-AI wins)..."
  why_it_fails: "Internal codes SECRET-02 and M1-DTC in narrative prose; senior reader cannot resolve without the cross-reference table."
  touches_load_bearing_element: "concept_ids"
  preservation_note: |
    SECRET-02 maps to disruption-dataset.yaml#framework_signals[6]; the underlying claim
    (retailer-captured AI captures more GMV than cross-retailer agents by 2028) must
    remain intact. M1-DTC maps to working/venture-options.md#M1. Code labels may be
    replaced with plain-English handles BUT the cross-reference path must update
    everywhere they appear (here, in the reference table at line 130, and in any
    dataset comments) — search-and-replace, not local edit.
  suggested_fix_shape: |
    Introduce a plain-English handle on first mention with the code in parentheses,
    then use the handle in subsequent narrative. Preserve the code verbatim in
    cross-reference tables.
```

### What the calling skill does next

`reimagine-industry` receives the five-line response, reads the violation report and `fix-patterns.md`, and applies the D5 canonical fix pattern using its own context:

1. Reads `disruption-dataset.yaml#framework_signals[6]` — confirms the canonical handle for `SECRET-02` is "the retailer-AI dominance signal" (the calling skill's working artifact already named it).
2. Reads `working/venture-options.md#M1` — confirms `M1-DTC` is named "the APAC integrator roll-up option".
3. Greps the document for all occurrences of `SECRET-02` (lines 47, 89, 130) and `M1-DTC` (lines 47, 102, 130).
4. Applies the Edit:

   Before (line 47):
   > SECRET-02 (retailer-AI wins) is the strongest signal in this market, and combined with M1-DTC creates a defensible moat.

   After:
   > The retailer-AI dominance signal (`SECRET-02`) is the strongest in this market, and combined with the APAC integrator roll-up option (`M1-DTC`) creates a defensible moat.

5. For subsequent narrative mentions (lines 89, 102), replaces the codes with the handles alone. Preserves codes in the reference table at line 130. Edit pass keeps brief and dataset coherent (in this case the dataset didn't need updates since the canonical handles already matched).
6. Re-invokes `analysis-quality-review` with the same `audit_dir` and `previous_violations` pointing at the prior report. The reviewer grades the new state. V-12 marked RESOLVED.

### Defer scenario — same violation, but the calling skill can't safely fix it

If the calling skill reads `disruption-dataset.yaml` and finds that `SECRET-02` is defined but `M1-DTC` is NOT (manifest declared the pattern but the artifact is silent on that token), then:

1. The calling skill applies the partial fix it can do safely (renames `SECRET-02` to the canonical handle).
2. For `M1-DTC`, it does NOT guess a handle. It marks the V-12 partial as `disposition: deferred` in its next invocation's `previous_violations`, with a short reason: "M1-DTC has no canonical definition in declared artifacts; calling skill cannot infer the handle safely."
3. The reviewer re-grades. It either:
   - Re-issues the violation with a richer preservation_note (if higher strictness would help locate the definition), or
   - Marks ACCEPTED-WITH-KNOWN-DEFER, excludes from FAIL count, and surfaces in the report so the calling skill can escalate to a human author.

The calling skill never guesses what `M1-DTC` means. This is the load-bearing safety pattern — preservation is the calling skill's accountability, not a guessing game.

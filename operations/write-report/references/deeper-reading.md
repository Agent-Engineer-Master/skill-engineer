# Deeper Reading — Operational Mechanics

This file extracts the operational mechanics from the foundational texts behind each rubric dimension. The librarian's MBB-readability research (`08-knowledge/resources/2026-05-19-consultant-readability-training-research.md`) covered the readability layer (Pass 2) thoroughly. This file goes deeper on the structural layer (Pass 1) by pulling the operational checklists from Minto, Rumelt, Conn & McLean, and Meadows.

---

## Barbara Minto — *The Pyramid Principle*

**Operational checklist for the pyramid (what the structure reviewer is actually testing):**

1. **The Single Governing Thought rule.** Every document has one apex. Every section under the apex summarises the ideas grouped beneath it. If a section does not summarise its children, the pyramid is broken — fix the section or fix the children.

2. **The three grouping rules (binding, not advisory):**
   - Every idea must SUMMARISE the ideas grouped below it.
   - Ideas in each grouping must be LOGICALLY ALIKE (same kind of statement — reasons, steps, problems).
   - Ideas within each group must be in a LOGICAL ORDER (time, structure, or degree).

3. **Horizontal vs vertical logic.** Vertical logic = the question-answer dialogue down the pyramid (the apex provokes the question "why?" → the level-2 reasons answer it). Horizontal logic = the relationship across siblings at one level, which must be either **deductive** (premise → premise → therefore conclusion; connected by "therefore") or **inductive** (several things similar in some way; connected by a plural noun like "reasons", "steps", "problems"). Mixing modes at the same level is a Pyramid violation — D2 in our rubric catches this as a MECE failure.

4. **SCQA opening sequence.** Situation (a stable fact the reader accepts) → Complication (the change that disrupts the stable fact) → Question (the resulting question this document answers) → Answer (the governing observation). Minto's specific test: if you cannot write all four in a paragraph, you do not yet know what the document is for.

**What our rubric inherits:** D1 (single governing observation), D2 (MECE supporting reasons including the inductive/deductive consistency check), D3 (SCQA opening), D5 (evidence under each reason actually establishes it, not merely relates to it — Minto's "summarise the ideas below" rule).

---

## Richard Rumelt — *Good Strategy / Bad Strategy*

**Operational mechanics of the strategy kernel:**

1. **Diagnosis.** A strategy must explicitly state the situation AND identify the obstacle to forward progress. Most "strategy" documents skip this — they list goals or activities. The diagnostic test is one sentence: "What is the situation and what is in the way of progress?" If that sentence is missing, there is no strategy.

2. **Guiding policy.** The overall approach to overcoming the obstacle. Not a goal. Not a list of values. A directional choice that constrains what the organisation will and will not do, and channels resources accordingly. Rumelt's test: does it rule out other approaches?

3. **Coherent actions.** Specific moves that implement the guiding policy. Each action must be feasible, coordinated with the others, and tied to the policy. Lists of disconnected initiatives (Rumelt's "garbage can of strategy") fail this test.

**The four hallmarks of BAD strategy (use as a failure taxonomy in the structure reviewer):**

- **Fluff** — abstract, jargon-laden language masquerading as deep thought ("synergistic leverage of core competencies")
- **Failure to face the challenge** — the document never states what is hard or what is in the way
- **Mistaking goals for strategy** — "increase revenue 20%" is a goal, not a strategy
- **Bad objectives** — objectives that are not coherent with each other or with the diagnosis (e.g., "improve quality" + "cut costs 30%" + "expand into 5 new markets" simultaneously, with no theory of how)

**What our rubric inherits:** D7 (Rumelt kernel: diagnosis + guiding policy + coherent actions). The Bad Strategy hallmarks are the FAIL taxonomy for D7. D1 (governing observation) cross-cuts here — for a strategy document, the governing observation must BE the kernel.

**Why this exists separately from D1:** A document can have a clear single thesis (D1 PASS) that is nevertheless a goal masquerading as strategy (D7 FAIL). Example: "We will become the leading agentic-commerce platform" is a clear thesis (D1 passes) but has no diagnosis, no guiding policy, no coherent actions (D7 fails).

---

## Charles Conn and Robert McLean — *Bulletproof Problem Solving*

**The McKinsey 7-step process (relevant operational mechanics):**

1. Define the problem (one precise question)
2. Structure the problem (issue tree or hypothesis tree — MECE branches)
3. Prioritise (most important branches first)
4. Develop work plan
5. Conduct analyses
6. Synthesise findings (which means rolling them up to the original question)
7. Communicate (which is where Minto's pyramid comes in)

**What our rubric inherits:**

- D2 (MECE supporting reasons) — Conn & McLean's issue-tree MECE discipline is the structural foundation. A document that fails MECE at the level-2 layer has skipped step 2 of the problem-solving process.
- D5 (evidence carries under each reason) — step 6 (synthesise) fails when evidence is collected but not actually rolled up to the parent claim. Our D5 catches this.
- The hypothesis-driven approach: every reason should be a falsifiable claim, not a topic label. Reviewer flags topic-label level-2 sections as D2 OR D4 failures depending on whether the structural error is at the grouping level or the title level.

**Issue-tree depth test:** If a level-2 reason cannot be decomposed into 2-4 sub-reasons that explain WHY the level-2 reason is true, the level-2 reason is probably itself an evidence item, not a reason. Promote it up or demote it down.

---

## Donella Meadows — *Thinking in Systems*

**Operational mechanics for systems analysis (relevant at high strictness for recommendation documents):**

1. **Stocks and flows literacy.** When a brief recommends "increasing X", check: is X a stock (accumulates over time, has delay) or a flow (rate, immediate)? Confusing them is a common diagnostic error.

2. **Feedback loop identification.** Recommendations should engage with the dominant feedback loops in the system. A recommendation that ignores a balancing loop (the system has a homeostat that will resist the change) will fail. A recommendation that strengthens a reinforcing loop without bounds will overshoot.

3. **The 12 leverage points (ranked from shallow to deep):**
   - Shallow (the brief flags these as low-impact): tweaking parameters (12), buffer sizes (11), stock/flow structure (10), delays (9)
   - Middle: negative feedback loop strength (8), positive feedback loop gain (7), information flow structure (6), rules of the system (5)
   - Deep (highest leverage): self-organisation capacity (4), goals of the system (3), paradigm the system arises from (2), power to transcend paradigms (1)

**What our rubric inherits (at strictness: high only):**

- A systems-literacy check on recommendation documents: does the brief identify the dominant feedback loop in the situation? Does its guiding policy engage with that loop or merely tweak parameters?
- This is a soft check, judged by the reviewer at high strictness — not a hard pass/fail at standard. Recorded as a sub-test under D7 (Rumelt kernel) for strategy documents: a kernel that recommends parameter tweaks for a problem rooted in feedback loop structure has failed Meadows' test.

**Operational test (for strategy briefs at high strictness):** What's the dominant feedback loop in the diagnosis? Which leverage point does the guiding policy target? If the policy targets parameters (leverage point 12) but the diagnosis describes a paradigm problem (leverage point 2), the policy is under-powered.

---

## Cole Nussbaumer Knaflic — *Storytelling with Data* (Pass 2 supplement)

**Relevant operational mechanic for Pass 2 D2 (so-what):** Knaflic's "so what?" applied to charts: every chart in the brief must have a one-sentence takeaway as its title — the chart's job is to support that sentence, not to display data. Reviewer flags charts (or table summaries in markdown) whose titles are noun labels ("Q3 revenue by region") rather than findings ("Q3 revenue grew 14% driven by APAC"). This is consistent with D1 (action titles) but applied to chart-equivalents.

---

## Gene Zelazny — *Say It with Charts*

**Relevant operational mechanic for Pass 2 D3 (specificity):** Zelazny's chart-selection discipline turns abstract claims into specific comparisons. Reviewer applies this principle to prose: any abstract claim ("growth was strong") should be replaceable with a specific comparison ("growth was 14%, vs. 8% segment average"). When the document cites a number, the comparison is the so-what.

---

## How these texts interact in the rubric

| Dimension | Primary source | Secondary sources |
|---|---|---|
| D1 — Single governing observation | Minto | — |
| D2 — MECE | Minto + Conn/McLean | — |
| D3 — SCQA | Minto | — |
| D4 — Dot-dash narrative | McKinsey practitioner literature (storyline) | Minto (vertical logic) |
| D5 — Evidence carries | Minto + Conn/McLean (synthesise step) | — |
| D6 — Frankenstein | McKinsey practitioner literature | — |
| D7 — Rumelt kernel | Rumelt | Meadows (high strictness) |

Readability rubric (Pass 2) sources are fully covered in the librarian's research file.

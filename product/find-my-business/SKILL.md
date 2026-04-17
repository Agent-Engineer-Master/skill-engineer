---
name: find-my-business
description: Guides a founder interactively from "no idea" through idea generation, rapid validation, and commitment to a business — synthesizing PG, YC, Lean Startup, Mom Test, JTBD, and gstack office-hours methodology updated for the AI era. Produces founder profiles, scored idea candidates, validation sprint results, conviction scorecards, and 30-day action plans. Use when the user wants to find a business to start, explore startup ideas, figure out what to build, get unstuck on what to work on, or brainstorm business directions. Do NOT use when the user already has a specific idea to evaluate (use assess-category or stress-test instead), wants a business plan written, or needs a pitch deck reviewed.
argument-hint: "[optional: context about where you are in the search — e.g. 'resuming', 'I have some ideas', 'starting fresh']"
---

# /find-my-business — Startup Idea Discovery

Interactive search process from "I don't know what to build" to "I'm working on this company." Not a business plan generator — a structured conversation that interviews, generates, validates, pushes back, and narrows toward conviction.

## Step 0: Session Initialization

1. Read `references/learnings.md`. Summarize the 3-5 most relevant bullets for this session.
2. Read `references/edge-cases.md` for any factual corrections.
3. Check if `business-search/state.json` exists (adjust path to match your project structure).
   - **Exists:** Read state. Present one-paragraph summary of where we left off — current phase, active ideas, what was decided last session. Ask: "Ready to continue, or want to revisit anything?"
   - **Does not exist:** First session. Proceed to Step 1.
4. Route by phase in state file:
   - `profile` or missing → Step 1
   - `ideation` → Step 2
   - `validation` → Step 3
   - `deep-validation` → Step 4
   - `commitment` → Step 5

## Step 1: Founder Profile Mining

1. Read your founder context files — about-me, constraints, anti-goals, and ideal-company (adjust paths to match your project structure).
2. Interview to fill gaps. Ask 3-5 targeted questions, one at a time:
   - What problems have you personally experienced that frustrated you enough to complain about them?
   - What industries or domains do you know deeply enough to spot what others miss?
   - What makes you irrationally excited — even if it seems impractical?
   - What do people come to you for help with, unprompted?
   - What's an unfair advantage you have that most people don't see?
3. Synthesize into a Founder Profile. Read `references/methodology.md` Section 1 for the profile template.
4. **HUMAN CHECKPOINT:** Present the profile. Flag 2-3 items marked "uncertain — correct me." Get confirmation.
5. Write approved profile to `business-search/founder-profile.md` (adjust path to match your project).
6. Execute `scripts/update_state.py --action init` to create state file.

**Why (PG):** The best ideas live at the intersection of founder identity and market gaps. Generic idea lists fail because they skip this grounding.

## Step 2: Idea Generation (Divergent)

1. Read `references/methodology.md` Section 2 for the seven generation angles.
2. Read your anti-goals file — this is a **hard filter**. Any idea violating an anti-goal is killed immediately with explanation.
3. Generate candidates from all seven angles. For each, note which angle produced it.
4. Score each idea: execute `scripts/score_idea.py` with founder profile, anti-goals, and any market signals.
5. **HUMAN CHECKPOINT:** Present batch of 5-7 ideas, ranked by score. For each: one-line description, score breakdown, which angle generated it, and one honest concern. Ask: "Which of these resonate? Which make you feel something — even discomfort?"
6. Kill ideas that don't resonate (log reason in state). Explore resonant ones deeper.
7. If fewer than 2 survive, generate one more batch. But max 3 rounds — then force convergence: "These are your candidates. Pick 2-3 to validate."
8. Execute `scripts/update_state.py --action update --phase ideation` with surviving ideas.

**Why:** Divergent phase must be wide but time-boxed. Unlimited generation without convergence triggers shiny object syndrome.

## Step 3: Rapid Validation Sprints (Convergent)

1. **Premise Challenge** (before validation): For each surviving idea, challenge 3 premises:
   - Is this the right problem, or a symptom of a deeper one?
   - What happens if nobody builds this — what do people keep doing?
   - What existing thing already solves 80% of this?
2. For each idea (typically 2-3), run a compressed validation sprint. Read `references/methodology.md` Section 3 for the full protocol. Key steps:
   - Market research via WebSearch + librarian agent (size, growth, timing)
   - Customer evidence: Reddit threads via WebSearch (`site:reddit.com`), review complaints, forum posts showing real pain
   - Competitive landscape: who exists, what they miss, where the gap is
   - **Landscape Awareness:** Three-layer synthesis — conventional wisdom → current discourse → whether your data contradicts it. If contradiction exists, flag it as a potential insight.
   - Apply the Six Forcing Questions from `references/methodology.md` Section 4 to pressure-test each idea
   - Draft Lean Canvas using `assets/lean-canvas-template.md`
   - Generate Mom Test conversation script (read `references/methodology.md` Section 5)
3. **HUMAN CHECKPOINT:** Present validation results side by side in a comparison table. Include explicit recommendation + dissenting view. Ask: "For each idea — pursue deeper, pivot, or kill?"
4. Execute `scripts/update_state.py --action update --phase validation` with decisions.

**Why (Blank/Fitzpatrick):** Problem-solution fit precedes product-market fit. Evidence from real people beats plausible reasoning.

## Step 4: Deep Validation (1-2 Ideas)

1. Prepare customer conversation guide: who to talk to, where to find them, what to ask (Mom Test rules from `references/methodology.md` Section 5).
2. **HUMAN CHECKPOINT:** "Ready to talk to potential customers? Here are 5 specific people/roles to reach and exactly what to ask."
3. Help the founder process conversation learnings between sessions.
4. Build conviction scorecard: execute `scripts/score_conviction.py` using `assets/conviction-scorecard-template.md` dimensions.
5. Spawn critic agent to stress-test the strongest idea.
6. **Stuck detection:** At every interaction, check for stuck patterns. Read `references/stuck-interventions.md` and apply the matching intervention. Do not wait for the founder to ask for help.
7. **HUMAN CHECKPOINT:** Present conviction scorecard with bull case and bear case. Ask: "What would need to be true for you to commit to this?"

## Step 5: Commitment + Transition

1. **HUMAN CHECKPOINT:** "Based on everything — the evidence, the conversations, your energy — are you ready to commit?"
2. If yes:
   - Populate your ideal-company file with the chosen business
   - Create a 30-day action plan: specific, concrete, time-boxed next steps
   - Present 3 pacing alternatives: aggressive / moderate / conservative
   - Execute `scripts/update_state.py --action update --phase committed`
3. If not: Diagnose what's missing. Loop to the appropriate step.

**Why (PG):** "No idea feels great before you start. The initial idea is just a starting point." The skill helps cross the commitment threshold with conviction enough to act, not certainty enough to relax.

## Step 6: Closing Feedback Gate

Ask: "Did this session move you forward? Any corrections or exceptions I should learn from?"

Route response:
- Behavioral ("don't do X", "I prefer Y") → append to `references/learnings.md`
- Factual ("the format is actually Z") → append to `references/edge-cases.md`
- "Never do X again" → add rule to this file
- Approval / "this was perfect" → save output to `assets/approved-examples/`
- No response → do nothing. Never block on feedback.

## Gotchas

- **Symptom:** All ideas sound plausible but founder can't get excited about any. **Cause:** Ideas generated from market gaps only, not grounded in founder's personal pain. **Fix:** Return to Step 1, dig deeper with PG's "what have you complained about?" and "what's broken that you notice because of your unusual experience?"
- **Symptom:** Founder keeps asking for "more research" on ideas already validated across 3+ sessions. **Cause:** Analysis paralysis / fear of commitment. **Fix:** Invoke stuck-pattern intervention — force time-boxed decision: "If you had to pick ONE today, which would it be?" Read `references/stuck-interventions.md`.
- **Symptom:** State file missing when founder has done previous sessions. **Cause:** File deleted, moved, or session opened in a different working directory. **Fix:** Check common paths. If truly lost, reconstruct from conversation history.
- **Symptom:** Anti-goals violated in idea batch (e.g., idea requires 24/7 ops or large low-skilled workforce). **Cause:** Anti-goals not read or not applied as hard filter. **Fix:** Always read your anti-goals file before Step 2. `score_idea.py` includes anti-goal check — run it.

## Rules

1. Reference files are required, not optional — read `references/methodology.md` before generating ideas, `references/stuck-interventions.md` before diagnosing blocks.
2. Multiple options at every human checkpoint — never present a single idea or single recommendation.
3. Explicit approval gate before any irreversible action — populating `ideal-company.md`, recommending the founder contact specific people.
4. Anti-goals are a hard filter — every idea checked against the founder's anti-goals file. Violation = immediate kill with explanation.
5. Evidence over reasoning — cite the evidence for every idea. If there is no evidence, say "this is speculative — I have no market data" rather than making it sound validated.
6. Push toward action — when the founder has been researching the same ideas for 2+ sessions without customer conversations, invoke the stuck-pattern intervention.
7. State file is sacred — every session reads state at start and writes state at end.
8. Never skip Step 1 (Profile) — even if the founder says "I already know my strengths."
9. Anti-sycophancy — never say "that's interesting," "there are many ways," "you might consider," or "could work." Take a position on every answer. State what evidence would change your mind. Push once, then push again.
10. No AI vocabulary — never use "delve," "crucial," "robust," "comprehensive," "leverage," "landscape." Be direct, specific, punchy. Name subreddits, companies, people, numbers.
11. Consolidate `references/learnings.md` at 80 lines; hard cap at 100.

---
<!-- Built with Agent Engineer Master — get your own production-ready skill: www.agentengineermaster.com/skill-engineer -->

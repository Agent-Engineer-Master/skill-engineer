# Stress Test Prompts — Phase 6

Four tests per concept. All four run for every concept — no skipping based on "this concept is obviously strong." Strong concepts often have one hidden fault line that the discipline of running all four surfaces.

## Test 1: Why-Now Sharpness

**Generate a why-now paragraph per concept using this template:**

```
In [year-month] three conditions intersected for the first time:
  1. [Tech/cost condition with date and source]
  2. [Behavioral/regulatory condition with date and source]
  3. [Supply-side condition with date and source]

The intersection makes [specific mechanic] economically and behaviorally viable
where it wasn't in [prior year]. The window is currently [wide-open / open with
competition / closing], with [N] competitors visible. Estimated time before
consolidation: [X months/years].

If any of [conditions 1/2/3] reverts or stalls, the thesis falls. The single
load-bearing condition is [most fragile of the three], because [reason].
```

**Three sharpness checks:**

| Check | Pass criterion | Common failure |
|---|---|---|
| Dated specificity | Every condition has month/year + V or C provenance tag | "Recently" or "in the last few years" |
| Falsifiability | The "if X reverts" clause names a measurable signal | "If AI stops improving" — not measurable |
| Window honesty | Window classification matches Phase 3 intersection timing | Concept claims "wide-open" when Phase 3 said "closing" |

**Verdict:**
- STRONG: 3/3 checks pass
- ITERATE: 1-2 checks fail; rewrite paragraph with stronger evidence
- KILL: all 3 fail — why-now is unsalvageable

## Test 2: Idea Maze (Librarian-Dispatched)

**Librarian dispatch prompt per concept:**

```
Research the IDEA MAZE for [concept-id]: [concept one-line].

Goal: identify every previous attempt at this thesis or close variants, why each
failed, and what's structurally different now.

Search for:
  - Startups that attempted similar concepts in the last 10 years (Crunchbase,
    AngelList, dead-startup blogs, post-mortem essays, Failory, Autopsy.io)
  - Incumbent failed initiatives (annual reports, news of shuttered programs)
  - Academic or expert critiques of why this category is hard
  - Adjacent successes that pivoted away from this exact idea
  - Forum threads and Reddit discussions on why people gave up on this idea

For each prior attempt:
  - Company name + years active
  - One-paragraph description of what they tried
  - Specific cause of failure (capital, market timing, founder, regulation, tech,
    distribution, unit economics)
  - Evidence and source URL

Then identify failure patterns: are failures clustered around one cause? Two?

Save to 08-knowledge/world-model/industries/[slug]/working/idea-maze-[concept-id].md
```

**Per-concept output structure:**

```yaml
idea_maze:
  prior_attempts:
    - company: string
      year: string
      attempted: string
      failure_cause: string
      lesson: string
      tag: string

  failure_cluster_analysis: |
    Of N prior attempts found, M failed due to [primary cause]; K failed due to
    [secondary cause]. The dominant historical kill mechanism is [primary failure].

  whats_different_now:
    - condition: string                   # Phase 3 enabling condition
      addresses_failure: string           # which historical failure mode it addresses
      tag: string

  unaddressed_historical_failure_modes:
    - string                              # failures NOT addressed by current thesis

  verdict: PASS | ITERATE | KILL
  verdict_reasoning: string
```

**Verdict logic:**
- **PASS** — every historical failure mode is addressed by a Phase 3 condition OR has a credible mitigation
- **ITERATE** — 1-2 failure modes unaddressed; concept needs sharpening
- **KILL** — multiple failure modes unaddressed AND no plausible mitigation; "this idea is broken"

**Pass requires ≥3 prior attempts surfaced OR explicit "novel category" justification with evidence.** Lazy idea-maze (1-2 attempts → "novel") is the most common stress-test failure mode.

## Test 3: Incumbent War-Game

**For each incumbent named in `who_it_displaces`, run three-year war-game:**

```
INCUMBENT WAR-GAME for [concept] vs [incumbent]:

Year 0 (now):
  - Incumbent's current state: revenue, profit pool, strategic priorities
  - Their visible activity in this space: products, partnerships, hiring
  - Their probable initial response to noticing us: ignore | monitor | acquire-talk
    | build-competitor | lobby | acquire-us

Year 1 (10k-100k users, year-1 metric met):
  - What we've proven: thesis validated; year_one_metric exceeded
  - What incumbent observes: our traction visible publicly
  - Their likely response: [specific action]
  - Structural constraint to acting (from Phase 4.4): why they can't easily copy
  - Estimated time to response: [months]

Year 2 (1M users):
  - Our position: GMV, retention, market share
  - Incumbent's response now: [specific competitive product or M&A play]
  - Probability we hold the position: [%, reasoning]
  - What we need to have built by now to survive: [specific moat layer]

Year 3 (steady state):
  - Equilibrium outcome: we win | we get acquired | we coexist in segment | we lose
  - Structural force determining outcome: [Phase 4.5 scale power]
  - Probability of each outcome: [%]
```

**Three war-game checks per incumbent:**

| Check | Pass criterion | Common failure |
|---|---|---|
| Constraint-grounded response | Each year's response constrained by Phase 4.4 counter-pos analysis | "They won't respond because they're slow" — passivity without trap |
| Realistic timeline | Response timeline matches incumbent's actual decision cadence | "Amazon takes 5 years" — Amazon launches features in months |
| Survival mechanism named | Year 2 names specific moat layer needed | "We'll have network effects" without naming the type |

**Verdict:**
- STRONG: credible "we win" or "we get acquired" outcome with grounded reasoning
- ITERATE: war-game requires some incumbent passivity but core trap is real
- KILL: every plausible response kills the concept

## Test 4: Moat Durability

**Three-stage moat trajectory per concept:**

| Stage | Question | Pass criterion |
|---|---|---|
| Entry (Y0-1) | What stops a well-funded competitor copying us in 12 months? | Named entry power: counter-positioning OR cornered resource. Generic "speed" or "execution" fails. |
| Wedge-to-platform (Y1-3) | What converts our wedge into a platform with compounding advantage? | Named mechanism: transaction data → improved recommendations → more transactions = network effect (specific causal chain) |
| Scale moat (Y3+) | Which Helmer Power holds at $100M revenue? | One of: scale economies, network economies, switching costs, branding, cornered resource, process power. Counter-positioning typically **expires** at scale. |

**Three moat checks:**

| Check | Pass criterion | Common failure |
|---|---|---|
| Power-to-mechanism specificity | Each power named with mechanism, not just label | "Network effects" without specifying same-side or cross-side |
| Counter-positioning expiry plan | If entry_power is counter-positioning, scale stage names what replaces it | "Counter-position now, network effects later" without explaining when/how |
| Inversion test | What happens if the dominant Phase 3 enabling condition stalls? | "It still holds because of X" — if X doesn't exist, no moat |

**Verdict:**
- STRONG: all three stages have specific mechanisms named
- ITERATE: stages exist but mechanisms vague
- KILL: depends entirely on first-mover advantage (first-mover isn't a moat)

## Test 5: Bet-Validity Gate (forward test design)

Tests 1-4 grade the *thesis*. This gate grades the *bet* — the forward experiment that resolves it. It runs on every concept and is **load-bearing for capability-first / Secret-derived concepts**, where the backward-looking idea-maze (Test 2) often returns thin ("novel category") and the only honest validation is a forward test.

This is where the skill's existing forward machinery points the right way: the `load_bearing_hypothesis` is the secret restated as a falsifiable claim, and the `validation_test` is the cheapest experiment that resolves it — not a historical post-mortem.

**Three bet checks per concept:**

| Check | Pass criterion | Common failure |
|---|---|---|
| Hypothesis is the kill-switch | `load_bearing_hypothesis` names the single claim that, if false, kills the concept | A restated value-prop, not a falsifiable bet ("customers will love this") |
| Test resolves the hypothesis | `validation_test` would actually move belief on that exact claim, with named pass/fail thresholds | A vanity metric that passes regardless of whether the hypothesis holds |
| Test is fundable | Cost + time-to-signal are small enough that a founder would actually run it before committing | A "test" that requires building the whole company first |

**Verdict:**
- STRONG: all three pass — a cheap forward experiment resolves the load-bearing claim
- ITERATE: hypothesis or test is vague; redesign the `validation_test` with sharper thresholds
- KILL: no feasible cheap test exists — the bet is unfalsifiable until it's too late to matter

For `origin: capability-first` concepts, a KILL here is decisive: a first-principles idea with no cheap forward test is a daydream, regardless of how compelling the thesis reads.

## Aggregate Verdict Matrix

Per concept, combine the four thesis-test verdicts. **Test 5 (Bet-Validity) is a separate gate: a KILL there kills the concept regardless of the matrix below.**

| Pattern | Overall verdict |
|---|---|
| 4 STRONG | SHIP — top of shortlist |
| 3 STRONG + 1 ITERATE | PROCEED — iterate the failed test, then ship |
| 2 STRONG + 2 ITERATE | RECONSIDER — concept may need re-framing |
| 1+ KILL | KILL — log as considered-and-rejected in `signals-log.md` |

## Bar Test (Set-Level)

After per-concept stress tests, the **reimagination-specific bar test** runs from a fresh-context sub-agent. See `bar-test-criteria.md` for the prompt and pass criteria. The bar test grades the **set of concepts as a whole**, not individual concepts — a brief with three "PROCEED" concepts can still fail bar test if they're structurally similar or none is genuinely non-obvious.

If bar test returns ITERATE: loop back to the specific phase that failed (usually Phase 4 framework generation or Phase 5 filter). No "log and defer" path.

# Structural Moves — Phase 5 Templates

Phase 5 runs **two lanes** of generation in parallel against `framework-signals.yaml` — one concept per move.

- **Moves 1-7 — the incumbent-anchored lane.** These are the seven structural patterns observed across every major technology-enabled disruption (Airbnb, Uber, Netflix, Spotify, Stripe, Shopify, Amazon). Each starts from an *existing* actor — a middleman, aggregator, incumbent profit model, supplier, or pain. Powerful, but by construction they triangulate from what already exists.
- **Move 8 — the first-principles lane.** Starts from a Phase 3 `capability_seed`, not an incumbent. Asks what job becomes *possible* (not just cheaper) that nobody serves because it could not exist before. This is the lane that produces net-new ventures rather than "this industry's Uber." The Thiel Secrets (4.6) also emit concepts into this lane.

A move that genuinely cannot be executed against this industry returns `"not viable because [specific reason citing dataset]"`. That's a valid output. Forcing a concept onto an unfit move produces weak signals.

**Every concept ships as a bet (both lanes).** See the [Bet enrichment](#bet-enrichment-every-concept) section below — `load_bearing_hypothesis` + `validation_test` + `value_if_true` are required on every concept, with `why_unknown` + `origin: capability-first` on Move 8 and Secret-derived concepts.

## Move 1: Remove the middleman

**Pattern:** Drive transaction costs to near-zero so a previously necessary intermediary becomes redundant.

**Examples:** Airbnb (hotel chains as accommodation intermediary), Uber (taxi dispatchers), Robinhood (per-trade brokers)

**Trigger conditions to look for:**
- Phase 1 has an intermediary node with high friction in its outgoing flows
- Phase 3 has a tech unlock that makes the intermediary's function programmable
- Phase 2 shows customer pain at the intermediary handoff

**Concept generation prompt:**
> Which intermediary node in the value chain creates more cost than value? What tech unlock from Phase 3 makes their function programmable? Design a direct customer-supplier connection that eliminates them. Cite the Phase 1 node being removed and the Phase 3 condition enabling removal.

## Move 2: Aggregate fragmented supply

**Pattern:** Organize supply that incumbents couldn't or wouldn't aggregate; let suppliers compete to reach your users.

**Examples:** Uber (drivers), Airbnb (spare rooms), Spotify (tracks), DoorDash (restaurants)

**Trigger conditions to look for:**
- Phase 1 fragmentation = highly_fragmented OR fragmented
- Phase 3 supply_side condition shows newly organizable supply
- Aggregation Theory diagnostic from Phase 4.2 passed

**Concept generation prompt:**
> What supply in this industry is fragmented enough that no one has organized it? What's the supply-side condition (Phase 3) that just made organization viable? How would suppliers compete on our platform? Cite the Phase 1 fragmentation and Phase 3 supply condition.

## Move 3: Transfer the customer relationship

**Pattern:** Move ownership of the customer relationship from supplier to platform; suppliers become channel partners.

**Examples:** Netflix (studios → channel partners), Amazon (brands → channel partners), DoorDash (restaurants → channel partners)

**Trigger conditions to look for:**
- Phase 1 shows suppliers currently own the customer relationship
- Phase 2 shows customer pain in the supplier-mediated experience
- Phase 4 Aggregation Theory diagnostic passed

**Concept generation prompt:**
> Who currently owns the customer relationship in Phase 1? What's the supplier-mediated friction in Phase 2 that we'd remove by owning the relationship ourselves? What pulls users to us instead of going direct? Cite the relationship-owner node and the friction.

## Move 4: Attack one value-eroding activity

**Pattern:** Find one specific activity customers (or suppliers) hate; make its elimination the headline product. Teixeira decoupling.

**Examples:** Netflix (late fees), Stripe (developer onboarding friction), Robinhood (trading fees)

**Trigger conditions to look for:**
- Phase 2 has a top-pain activity with intensity × frequency ≥60
- Phase 4.3 decoupling test surfaced this pain
- Phase 4.4 counter-positioning analysis showed the incumbent depends on the activity

**Concept generation prompt:**
> What's the single highest-scoring pain activity in Phase 2? Why does the incumbent need it to be inside their flow? Design a product whose headline value is the elimination of that activity. Cite the Phase 2 pain and Phase 4.4 incumbent dependency.

## Move 5: Start narrow, expand laterally

**Pattern:** Win one segment completely before expanding. Often paired with Move 4 — narrow segment + attack their specific pain.

**Examples:** Facebook (Harvard → other universities → everyone), Amazon (books → everything), Tesla (Roadster → Model S → Model 3), Stripe (developers → SMB → enterprise)

**Trigger conditions to look for:**
- Phase 2 has a small segment with disproportionately high pain
- That segment has a credible expansion path to adjacent segments
- Phase 3 enabling conditions exist for the narrow segment, may not yet for adjacent ones

**Concept generation prompt:**
> What's the smallest segment in Phase 2 that would care most about our wedge? What's the credible expansion path from there to adjacent segments? Why does starting narrow give us a defensible position from which to expand? Cite the Phase 2 segment and expansion logic.

## Move 6: Counter-position against the incumbent's profit model

**Pattern:** Adopt a business model that forces incumbents to choose between hurting their existing profit pool OR letting you win. Helmer counter-positioning.

**Examples:** Netflix subscription vs Blockbuster late fees, Robinhood free vs E*TRADE per-trade, Vanguard low-fee index funds vs active managers

**Trigger conditions to look for:**
- Phase 1 incumbent has a load-bearing profit pool that's vulnerable
- Phase 4.4 counter-positioning analysis returned a signal with named structural trap
- Phase 4.5 entry_power = counter-positioning

**Concept generation prompt:**
> Which Phase 1 incumbent has a profit pool we can attack? What business model would force them into the dilemma (hurt their profit pool OR lose to us)? Why can't they copy without self-harm? Cite the incumbent, the profit pool, and the trap from Phase 4.4.

## Move 7: Arm the supply side (rather than commoditize it)

**Pattern:** Instead of aggregating supply (Move 2), give suppliers tools that let them compete directly with the existing aggregator. Inverts Move 2.

**Examples:** Shopify (vs Amazon — armed merchants), Substack (vs Medium — armed writers), Stripe (vs PayPal — armed developers), Twilio (vs incumbent telco — armed builders)

**Trigger conditions to look for:**
- Phase 1 shows suppliers being commoditized by an existing aggregator
- Phase 2 shows supplier pain (not just customer pain) — pain audit must have covered suppliers
- Suppliers have latent customer relationships they want to reclaim

**Concept generation prompt:**
> What aggregator is currently commoditizing suppliers in this industry? What tools would let suppliers reclaim direct customer relationships and compete with the aggregator? Why would suppliers pay for these tools? Cite the aggregator being attacked and the supplier pain from Phase 2.

## Move 8: Capability-first / new-to-the-world

**Pattern:** Start from a capability that did not exist before, not from an incumbent. Ask what job becomes *possible* — not merely cheaper or faster — that no one serves because the capability to serve it didn't exist. The venture is derived from the new capability; there may be no incumbent to displace at all, because the job is new.

This is the lane that breaks the triangulation bias. Moves 1-7 ask "who do I attack?" Move 8 asks "what is now possible?"

**Examples (capability → previously-impossible job):**
- Smartphone GPS + ubiquitous data → real-time turn-by-turn for everyone (not a cheaper Garmin — a job no consumer device could do)
- Cheap genome sequencing → consumer ancestry + health reports (no incumbent was "sequencing for consumers" — the job didn't exist)
- Sub-cent LLM inference + agent tool-use → an agent that continuously arbitrates price/spec across thousands of SKUs on a buyer's behalf (no human shopper or retailer could perform this at any price before)

**Trigger conditions to look for:**
- Phase 3 has ≥1 `capability_seed` describing a job that is newly *possible* (not just cheaper)
- The job has no clear incumbent owner — or the "incumbent" is non-consumption (the job simply wasn't done)
- The capability is the load-bearing dependency; remove it and the venture is impossible, not just worse

**Concept generation prompt:**
> Take one Phase 3 `capability_seed`. State the job it makes possible that could not exist before — be specific about what was *impossible*, not just expensive. Design the venture that does that job. Cite the `capability_seed` ID and the underlying capability. Do NOT cite an incumbent — if you find yourself naming one to attack, you're in Moves 1-7, not Move 8. Then state the one assumption that must be true for buyers to want this (the `load_bearing_hypothesis`) and the cheapest test that would resolve it.

**Anti-pattern:** "An AI that does [existing job] but better/cheaper." That's a Move 1-4 efficiency play wearing first-principles clothing. Move 8 requires a job that was *impossible*, not an existing job made cheaper. If the job already exists and someone serves it, you're in the incumbent-anchored lane.

## Memorable handle requirement (RULE-1)

Every concept generated MUST carry a **memorable 3-5 word handle** alongside its `concept_id`. The handle captures the core idea well enough that a senior reader recognizes what the concept IS without reading the one-liner.

### Handle generation prompt

After generating each concept, before writing it to `framework-signals.yaml`:

> Generate a 3-5 word memorable handle for this concept. It should:
> - Capture the core idea (not the framework or move)
> - Be self-descriptive — recognizable on its own
> - Use specific, evocative words (preferably with a known analog like "Wirecutter-for" or "Stripe-for")
> - Avoid generic words: "platform", "marketplace", "agent", "AI"
>
> Examples:
> - ✅ "Wirecutter-for-niche, AI-citation-first"
> - ✅ "Stripe-for-merchant-agent-protocols"
> - ✅ "Substack for niche product authority"
> - ❌ "AI shopping platform" (generic)
> - ❌ "AUTH-DTC" (code only)
> - ❌ "M4 concept" (no semantic content)

The handle becomes the H3/card title in HTML gate reviews. The `concept_id` appears as a small monospace tag beneath it.

## Secret-derived concepts (RULE-2)

Thiel Secrets are not endorsed for truth — they are converted to bets (see `frameworks-cheatsheet.md` §4.6). A Secret emits a venture concept into the first-principles lane; that concept carries the secret restated as its `load_bearing_hypothesis`, plus a `validation_test` and `value_if_true`, exactly like any other concept (see [Bet enrichment](#bet-enrichment-every-concept)).

There is **no** `depends-on / survives-falsification / counter-bet` tagging and **no** truth- or conviction-endorsement step — both are obsolete. The human never decides whether a Secret is true; at the Phase 5 gate the human decides which bets are worth *testing*. Conviction is the output of running the test, not an input.

## Y1 metric bottoms-up requirement (RULE-3)

When enriching each kept concept with `year_one_metric`:

- If the metric implies outperforming an industry-wide projection cited in Phase 3, include `bottoms_up_justification`:
  - Conversion delta vs industry average (with source)
  - Competing-merchant count in the addressable SKU set
  - Precedent operators who achieved comparable concentration and timeline
- If the metric still reads as goal-seeked after justification, either lower the Y1 floor or add a Y2 ramp

Bar-test reviewers reading the brief cold will flag any metric that contradicts the brief's own data. This is the most common avoidable bar-test ITERATE trigger.

## After all 8 moves: diversity check

After generation, the skill runs an automated diversity check across the concepts:

- **Customer segments:** ≥2 distinct
- **Entity types attacked:** ≥2 distinct (customer pain vs supplier pain vs intermediary pain)
- **Revenue models:** ≥2 distinct (subscription, take-rate, referral, transaction, freemium, SaaS)
- **Incumbents displaced:** ≥2 distinct
- **Origin:** ≥1 concept tagged `origin: capability-first` (Move 8 or a Secret-derived concept) — the first-principles lane must survive into the candidate set, not just be generated and dropped

If diversity is thin or the capability-first floor is unmet, the skill re-runs the underweighted moves with an explicit constraint: "produce a concept that is **structurally different** from the others," and generates from any un-used `capability_seeds`.

## Filter step (human-led) — test-worthiness, not conviction

After generation + diversity check, the human filters from the candidate set (some "not viable") to **3-5 concepts**. The gate is **test-worthiness, not truth or conviction** — the human cannot know whether a secret is true (that's why it's a secret), but can decide whether finding out is worth it. For each bet weigh:

1. **Prize if true** (`value_if_true`) — is the upside big enough to bother testing?
2. **Cost + speed to test** (`validation_test`) — is the experiment cheap and fast enough to run?
3. **Strategic fit** — founder bandwidth, capital, time horizon.
4. **Non-obviousness** — would a senior strategist recognize this as fresh?

The question is "which of these tests are worth funding?" Conviction is the *output* of running the test, not an input to this gate. The AI does not pre-filter; the human selects which experiments to run.

## Bet enrichment (every concept)

Every kept concept ships as a **bet**, regardless of lane:

1. **`load_bearing_hypothesis`** — the single claim that, if false, kills the concept. For Secret-derived concepts this is the secret restated as a falsifiable proposition specific to this venture.
2. **`why_unknown`** — why this can't be desk-researched away (required for `origin: capability-first`; it's usually a behavioural fact that doesn't exist in the data yet). Incumbent-first concepts may mark this `desk-researchable`.
3. **`validation_test`** — the cheapest experiment that moves your belief on the hypothesis: `{experiment, cost, time_to_signal, pass_threshold, fail_threshold}`.
4. **`value_if_true`** — the prize if the hypothesis holds.
5. **`origin`** — `capability-first` (Move 8 / Secret-derived) or `incumbent-first` (Moves 1-7).

## Enrichment step

Each kept concept also gets three Phase-6 enrichment fields:

1. **`market_size_hypothesis`** — TAM/SAM for this specific concept (not the whole industry)
2. **`wedge_product`** — the MVP, what early customers pay for
3. **`year_one_metric`** — the one KPI that validates the thesis (with success and failure thresholds)

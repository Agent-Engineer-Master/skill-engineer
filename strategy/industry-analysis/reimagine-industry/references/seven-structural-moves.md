# Seven Structural Moves — Phase 5 Templates

These are the seven structural patterns observed across every major technology-enabled disruption (Airbnb, Uber, Netflix, Spotify, Stripe, Shopify, Amazon). Phase 5 applies each as a template against `framework-signals.yaml` — one concept per move, in parallel.

A move that genuinely cannot be executed against this industry returns `"not viable because [specific reason citing dataset]"`. That's a valid output. Forcing a concept onto an unfit move produces weak signals.

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

## Endorsed Secret dependency tagging (RULE-2)

For each generated concept, record its relationship to each endorsed Thiel Secret:

```yaml
endorsed_secrets_dependency:
  - secret_id: secret-1-handle
    relationship: depends-on | survives-falsification | counter-bet
    rationale: "One sentence on what the concept assumes about this Secret."
```

- **`depends-on`**: this concept is the one that wins if Secret is true
- **`survives-falsification`**: this concept works whether Secret is true or false (robust to the bet)
- **`counter-bet`**: this concept is the one that wins if Secret turns out false

Phase 5 filter aims for a portfolio that spans the hypothesis space — at least one `depends-on` and one `counter-bet` for each high-stakes Secret, plus `survives-falsification` concepts that don't take a side.

## Y1 metric bottoms-up requirement (RULE-3)

When enriching each kept concept with `year_one_metric`:

- If the metric implies outperforming an industry-wide projection cited in Phase 3, include `bottoms_up_justification`:
  - Conversion delta vs industry average (with source)
  - Competing-merchant count in the addressable SKU set
  - Precedent operators who achieved comparable concentration and timeline
- If the metric still reads as goal-seeked after justification, either lower the Y1 floor or add a Y2 ramp

Bar-test reviewers reading the brief cold will flag any metric that contradicts the brief's own data. This is the most common avoidable bar-test ITERATE trigger.

## After all 7 moves: diversity check

After generation, the skill runs an automated diversity check across the 7 concepts:

- **Customer segments:** ≥2 distinct
- **Entity types attacked:** ≥2 distinct (customer pain vs supplier pain vs intermediary pain)
- **Revenue models:** ≥2 distinct (subscription, take-rate, referral, transaction, freemium, SaaS)
- **Incumbents displaced:** ≥2 distinct

If diversity is thin, the skill re-runs the underweighted moves with an explicit constraint: "produce a concept that is **structurally different** from the others."

## Filter step (human-led)

After generation + diversity check, the human filters from 7 (some "not viable") to **3-5 concepts** using three questions:

1. **Conviction:** do I actually believe this thesis?
2. **Strategic fit:** does this fit our context (founder bandwidth, capital, time horizon)?
3. **Non-obviousness:** would a senior strategist recognize this as fresh?

The AI cannot supply conviction. This filter is the human's contribution.

## Enrichment step

Each kept concept gets three enrichment fields needed for Phase 6:

1. **`market_size_hypothesis`** — TAM/SAM for this specific concept (not the whole industry)
2. **`wedge_product`** — the MVP, what early customers pay for
3. **`year_one_metric`** — the one KPI that validates the thesis (with success and failure thresholds)

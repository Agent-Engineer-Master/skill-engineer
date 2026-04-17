---
name: marketing-plan
description: Develops a full go-to-market marketing plan for a new online business, product, or idea — covering beachhead market, ICP, competitive landscape, Dunford positioning with messaging, channel strategy with buyer journey mapping, budget allocation, pricing, content strategy with retention, 90-day launch timeline, PMF definition, first customer motion, and AARRR + GEV KPI framework with measurement setup. Produces a structured markdown plan saved locally. Activate when: "build a marketing plan", "create a GTM strategy", "how should I market my new product/brand/startup", "plan the launch for", "what channels should I use to launch", "write a marketing plan for". Do NOT activate for: auditing existing marketing performance, writing individual content pieces, running specific campaigns, or competitive analysis without a launch goal.
---

# Marketing Plan

Produces a full go-to-market marketing plan for a new online business.

## Process

### Phase 1: Context Intake

Before asking questions, check if a shared context file exists (e.g. `product-marketing-context.md`, `_store-state.md`, or similar product brief in the working directory). If found, read it and pre-fill answers. Only ask questions whose answers are not already available.

Ask these 7 questions (all required before proceeding):

1. **Product/service** — What are you selling and how is it delivered? (1-2 sentences)
2. **Business model** — SaaS / DTC ecommerce / service / marketplace / other?
3. **Stage** — Pre-launch (no customers), early (1-50 customers), or growing (50+)?
4. **Geography** — Primary target market (country/region)?
5. **Budget** — Bootstrapped (no ads), low (<$1k/mo), medium ($1k-$10k/mo), or well-funded?
6. **Key constraint or unfair advantage** — One thing that limits or enables this launch.
7. **Existing audience** — Do you have a personal brand, newsletter, social following, or community presence? If yes: where and approximate size.

Store answers as a context card. Load `references/business-type-guide.md` to apply business-type rules. If Q7 reveals an existing audience, check the Personal Brand Flywheel section of that file and apply the modifier before generating channel options.

---

### Phase 2: Beachhead Market + ICP

*Principle: The most common GTM failure is targeting everyone. Define the smallest winnable segment first.*

Using context card and `references/frameworks.md` (JTBD + beachhead sections):

1. Size the market: TAM -> SAM -> beachhead
2. Generate **3 ICP options** as JTBD statements: "When [trigger], [persona] wants to [outcome], so they can [deeper goal]."
3. For each option, rate: market size (S/M/L), competition (low/med/high), reachability (hard/med/easy)

**GATE A — present 3 ICP options. Wait for user to choose one. If none fit, ask which element to change (trigger, persona, or outcome) and generate 3 new options.**

**GATE A constraint check — before accepting the user's choice, cross-reference it against the context card:**
- If chosen ICP is Teams or Enterprise AND constraints include bootstrapped + pre-launch + no distribution: surface the tension explicitly. State the typical sales cycle length (3-8 weeks), the trust-building required, and the opportunity cost. Ask the user to confirm or reconsider. Do not block the choice — but do not silently accept it either.
- If chosen ICP has high friction AND the founder has an existing audience in a different segment: flag that the audience already in hand may be a faster beachhead. Offer to generate an alternative ICP option centred on that segment before proceeding.

---

### Phase 3: Competitive Landscape

*Principle: Positioning without competitive context is guesswork. Map the terrain before choosing your position.*

Using chosen ICP and `references/execution-playbooks.md` (competitive mapping section):

1. Identify **3-5 direct competitors** and **2-3 indirect alternatives** (including "do nothing" and manual workarounds)
2. For each competitor, assess: positioning claim, primary channel, pricing model, and one vulnerability the ICP would notice
3. Map where competitors cluster and where **open ground** exists — this is the white space the positioning step will target
4. Flag any competitor whose positioning directly overlaps with the user's product — this is the displacement target

Present the competitive terrain map as a table. No gate — output feeds directly into Phase 4 (positioning uses the white space and displacement targets).

---

### Phase 4: Positioning + Messaging

*Principle: Weak positioning makes every channel expensive. Nail this before choosing channels.*

Using chosen ICP, competitive terrain map from Phase 3, and `references/frameworks.md` (Dunford 5-component section):

1. Map competitive alternatives (from Phase 3 terrain map — already done, refine if needed)
2. Identify unique attributes competitors lack
3. Translate attributes into differentiated value for the ICP
4. Generate **3 positioning directions** — one per distinct value theme, each targeting identified white space

**GATE B — present 3 positioning directions. Wait for user to choose one. If none fit, ask which component to challenge (alternatives, value theme, or category) and generate 3 new directions.**

Extract one-liner: "[Product] is the [category] for [ICP] who [trigger/context], unlike [alternative]."

**Messaging derivation** — from the chosen positioning, generate:
- **Primary message** (1 sentence) — the outcome the ICP gets, in their language
- **Supporting messages** (2-3 bullets) — proof points that back up the primary message
- **Channel-specific hooks** — a one-line adaptation for each likely channel (social, email, landing page)

---

### Phase 5: Channel Strategy + Journey Map

*Principle: Channel selection must follow ICP behaviour, not trend. One primary + one support + one retention lever.*

Using chosen ICP, positioning, and `references/business-type-guide.md`:

**Step 1: Buyer journey map.** Using `references/execution-playbooks.md` (journey mapping section), map the 5-stage ACCRL journey (Awareness -> Consideration -> Conversion -> Retention -> Loyalty) for the chosen ICP. For each stage: what the buyer does, what they need, and which channel type serves it. Build from JTBD data, not internal funnel stages.

**Step 2: Channel selection.** Using the journey map:
1. Map how the ICP discovers and evaluates solutions (Capture / Create / Convert)
2. Filter channels by business model, stage, and budget
3. Generate **3 channel mixes** — each with primary, support, retention lever, and 1-sentence rationale
4. Include a GEV tactic in every mix — see `references/frameworks.md` (GEV section)

**GATE C — present 3 channel mixes. Wait for user to choose one. If none fit, ask what constraint changed (budget, stage, or ICP behaviour) and generate 3 revised mixes.**

---

### Phase 6: Budget Allocation

*Principle: A plan without resource allocation is a wish list. Budget forces prioritisation.*

Using chosen channel mix, stage, and budget tier from Phase 1. Load `references/execution-playbooks.md` (budget allocation section).

1. Apply the **70/20/10 rule**: 70% proven channels (primary + support), 20% experimental, 10% tools and infrastructure
2. Recommend **monthly spend allocation** by channel using the stage-appropriate tier defaults from the reference file
3. Flag the **ROI hierarchy** — which channels have the best CPL at this budget level (SEO and email first for constrained budgets; paid search last)
4. State the **one hire/investment NOT to make** at this stage — and why (reference the common failure mode of premature hiring consuming channel budget)

No gate — feeds into Phase 7.

---

### Phase 7: Pricing Strategy

*Principle: Price is a positioning signal, not just a revenue mechanism. Launch price must be low enough to remove first-purchase friction and generate validation data, not to maximise margin.*

1. Recommend a **launch price** with rationale tied to ICP willingness to pay and the validation goal
2. Define a **price ladder** — 2-4 tiers with names, prices, and the scope/outcome that justifies each step up
3. Define **raise triggers** — the specific, measurable conditions that must be true before moving to the next tier (e.g. repeat rate >= X%, N unprompted outcome descriptions). Never recommend raising price based on volume alone.
4. Flag any **pricing experiments** worth running in the first 90 days (A/B framing, decoy pricing, free sample conversion test)

No gate — feeds into Phase 8.

---

### Phase 8: Content Strategy

*Principle: Content drives every channel — map what to produce, where, and at what cadence.*

Using chosen channel mix and buyer journey map:

1. Assign content types per channel and journey stage:
   - **Awareness**: founder POV content, educational posts, problem-space articles
   - **Consideration**: comparison content, case studies, proof points
   - **Conversion**: landing pages, onboarding sequences, social proof
   - **Retention**: welcome series, activation nudges, milestone celebrations
   - **Loyalty**: referral prompts, community content, exclusive updates
2. Recommend weekly production volume at current stage and budget
3. Name the one content format that reaches the ICP at lowest cost
4. Specify **retention content** — the 3 non-negotiable email campaigns: welcome series (days 0/3/7), activation nudge (day 3-5 for stalled users), win-back (30-day inactive). See `references/execution-playbooks.md` (retention campaigns section).

No gate — output feeds into Phase 9.

---

### Phase 9: 90-Day Launch Timeline

*Principle: Phases must have activation conditions, not just dates. A plan without a sequence is a wish list.*

Using `references/frameworks.md` (launch phases section):

- **Phase 0 (Weeks 1-4): Pre-launch validation** — waitlist, 5+ customer conversations, 3 testimonials minimum
- **Phase 1 (Weeks 5-8): Controlled launch** — activate primary channel, measure activation metric
- **Phase 2 (Weeks 9-12): Scale or pivot** — if activation metric hit, open secondary channel; if not, revisit ICP

Each phase: 3-5 specific weekly actions + the activation condition that must be met before advancing.

---

### Phase 10: PMF Definition

*Principle: PMF is not a feeling. Define it as a specific combination of measurable signals before launch, so you know whether to scale or pivot at Day 90.*

1. Define **3-5 PMF signals** specific to this business model and ICP — at least one must be a repeat behaviour signal (repeat purchase, renewal, referral). Avoid vanity signals (traffic spikes, social likes).
2. Define the **PMF threshold** — the minimum combination of signals that, together, confirm go/no-go for moving from validation to growth. Not all signals need to be met — specify which are required vs supporting.
3. Define **what PMF does NOT look like** — name the false positives specific to this product (e.g. one enthusiastic customer, a viral post with no conversions).

No gate — feeds into Phase 11.

---

### Phase 11: First Customer Motion

*Principle: The first 10 customers do not come from SEO, ads, or passive inbound. They come from the founder finding them and making direct contact. A plan without a Week 1 action list is not operational.*

Produce a **Day-by-Day Week 1 playbook** with:
- Day 1-2: what to publish or ship (free asset, listing, landing page)
- Day 3-4: where to seed it (specific communities, subreddits, Discord servers relevant to ICP)
- Day 5-6: direct outreach — how many contacts, where to find them, what 3-sentence message to send
- Day 7: review and follow-up actions

Be specific: name the subreddits, the listing platforms, the DM format. Generic advice ("post on social") is not acceptable here.

Also specify: **where NOT to look in Week 1** — channels that require more setup than Week 1 allows (Product Hunt, paid ads, newsletter swaps).

No gate — feeds into Phase 12.

---

### Phase 12: KPI Framework + Measurement Setup

*Principle: Metrics that don't connect to unit economics can't tell you if GTM is working. Metrics without instrumentation are fiction.*

**Part A: KPI Framework.** Using `references/frameworks.md` (AARRR + GEV sections):

1. Assign metrics to each AARRR stage with 30/60/90-day targets
2. Add GEV score — measure brand mentions in AI search responses
3. Present **3 North Star Metric candidates** — recommend one based on business model and stage

**Part B: Measurement Setup.** Using `references/execution-playbooks.md` (measurement setup section):

1. Define the **measurement chain**: Budget -> CPM -> CTR -> CPC -> Conversion rate -> CAC -> LTV:CAC
2. Specify the **pre-launch instrumentation checklist**: GA4 conversion events, UTM naming convention, CRM tracking fields
3. State the **UTM naming standard**: `utm_source` (platform) / `utm_medium` (channel type) / `utm_campaign` (stable campaign name). One owner, one naming sheet, consistent lowercase.
4. Recommend a **14-day setup timeline** for analytics before first campaign

---

### Phase 13: Assemble and Save

Compile all sections using `assets/plan-template.md`.

Save output to: `marketing-plan-[brand-slug]-[YYYY-MM-DD].md` in the working directory.

Confirm file path to user.

---

## Rules

1. Never recommend channels without presenting 3 options with tradeoffs (Gate C)
2. Never skip Phase 4 (positioning) — jumping to channels without positioning is a hard failure mode
3. Never skip Phase 3 (competitive landscape) — positioning without competitive context is guesswork
4. Every channel mix must include a GEV tactic
5. Every channel mix must include at least one owned channel (email, SEO, or community)
6. Phase 1 context intake must be complete before any recommendations
7. Never post or publish output — save locally only
8. Budget allocation must respect the budget tier from Phase 1 — never recommend paid ads for bootstrapped businesses without flagging the tradeoff
9. Retention content (welcome series, activation nudge, win-back) must appear in every plan regardless of business model
10. When user flags a bad recommendation: update the relevant reference file immediately
11. When user approves a final plan: save it to `assets/approved-examples/` as a reference

---

<!-- Built with Agent Engineer Master — get your own production-ready skill: www.agentengineermaster.com/skill-engineer -->

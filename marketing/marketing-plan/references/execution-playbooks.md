# Execution Playbooks

Tactical frameworks for competitive mapping, budget allocation, buyer journey mapping, measurement setup, and retention campaigns. Loaded on demand by SKILL.md phases.

## Table of Contents
1. [Competitive Mapping](#competitive-mapping)
2. [Budget Allocation](#budget-allocation)
3. [Buyer Journey Mapping](#buyer-journey-mapping)
4. [Measurement Setup](#measurement-setup)
5. [Retention Campaigns](#retention-campaigns)

---

## Competitive Mapping

### Purpose
Produce a competitive terrain map — not a 50-page report. The output is a visual of where rivals cluster and where open ground exists. Should take under 2 hours using existing customer research and public information.

### Framework: Lightweight Competitive Terrain Map

**Step 1: Identify competitors (10 minutes)**
- 3-5 direct competitors (same category, same buyer)
- 2-3 indirect alternatives (different category, same outcome — include "do nothing" and spreadsheets/manual workarounds)

**Step 2: Assess each competitor on 4 dimensions**

| Competitor | Positioning claim | Primary channel | Pricing model | One vulnerability |
|------------|------------------|-----------------|---------------|-------------------|
| [Name] | [Their one-liner] | [Where they acquire] | [How they charge] | [What their ICP complains about] |

**Step 3: Map the terrain**
- Where do competitors cluster? (e.g. all targeting enterprise, all on LinkedIn, all subscription-priced)
- Where is the **open ground**? (e.g. no one serves the solo practitioner, no one offers one-time pricing, no one has a personal brand presence)
- Which competitor is the **displacement target**? (the one whose customers are most likely to switch)

**Step 4: Extract positioning inputs**
- White space: the unclaimed territory to position into
- Displacement weakness: the specific pain point the displacement target creates for the ICP
- Counter-messages: for each competitor's positioning claim, what is the truthful counter that highlights your advantage?

### What NOT to do
- Do not analyse features exhaustively — focus on positioning and perception
- Do not research more than 8 total competitors — diminishing returns
- Do not treat this as a one-time exercise — revisit quarterly
- Do not copy competitor tactics without accounting for their stage and resources

### Sources for competitive research
- Customer interviews ("who else did you consider?")
- G2/Capterra/Product Hunt reviews (filter for 2-3 star reviews — these reveal vulnerabilities)
- Competitor pricing pages, landing pages, and LinkedIn company pages
- AI search queries ("best [category] for [ICP use case]")

---

## Budget Allocation

### The 70/20/10 Rule
The practitioner standard for marketing budget allocation:
- **70%** — Proven channels (primary + support channels from the channel strategy)
- **20%** — Experimental channels (testing new acquisition or content formats)
- **10%** — Tools and infrastructure (analytics, email platform, design tools)

### Stage-Based Budget Tiers

| Stage | Typical monthly budget | Content + SEO | Paid acquisition | Email/CRM | Tools | Experimental |
|-------|----------------------|---------------|-----------------|-----------|-------|-------------|
| **Bootstrapped** | $0-500 | 60% (founder time) | 0% | 20% (free tier tools) | 10% | 10% |
| **Low budget** | $500-1K | 50% | 15% | 15% | 10% | 10% |
| **Medium budget** | $1K-10K | 40% | 25% | 15% | 10% | 10% |
| **Well-funded** | $10K+ | 32% | 30% | 15% | 8% | 15% |

### Channel ROI Hierarchy (invest in this order at constrained budgets)

| Channel | Typical ROI | Typical CPL | When to add |
|---------|------------|------------|-------------|
| SEO / content marketing | 748% | $31 | Always — invest from day one, compounds over 3-6 months |
| Email marketing | 3,600-4,200% | $36-42 per $1 | Always — build list from day one |
| Webinars / events | 364% | $72 | At $5K+/month budget |
| Social media (organic) | Variable | $0 (time cost) | Always — founder time, not budget |
| LinkedIn ads (B2B) | 200-400% | $75-150 | At $5K+/month, B2B only |
| Google Search ads | 36% | $181 | At $10K+/month, only on validated keywords |
| Meta/TikTok ads (DTC) | Variable | $15-50 | At $5K+/month, only with validated creatives |

### Revenue Benchmark
- Industry average: 9.4% of revenue allocated to marketing
- B2B SaaS standard: 8-10% of ARR
- Seed-stage: 10-20% of funding round
- Venture-backed companies spend 58% more than bootstrapped peers

### Common Budget Failure Modes
1. **Premature hiring**: A marketing manager at $83K/year consumes the entire budget of a bootstrapped business. At <$5K/month, use freelancers and tools, not full-time hires.
2. **Paid ads before organic signal**: If 10 customers can't be acquired organically, paid won't fix the problem — it will amplify the waste.
3. **Tool bloat**: Subscribing to 5+ marketing tools before any channel is validated. Start with free tiers (GA4, Mailchimp/Brevo free, Canva free).
4. **No experimental budget**: Spending 100% on "what works" means never discovering what works better. Reserve 10-20%.

---

## Buyer Journey Mapping

### The ACCRL Model (Lightweight GTM Version)

Map the buyer's journey in 5 stages. Build from JTBD interview data, not internal funnel stages. The buyer journey is not the same as your funnel — funnels are company-centric; journey maps are buyer-centric.

| Stage | Buyer's question | What they do | What they need | Channel type |
|-------|-----------------|-------------|---------------|--------------|
| **Awareness** | "I have a problem" | Search, scroll, ask peers | Education, validation that the problem is solvable | Create channels |
| **Consideration** | "What are my options?" | Compare, read reviews, ask AI | Comparisons, social proof, trust signals | Capture channels |
| **Conversion** | "Is this the right one?" | Try, evaluate, hesitate | Low friction, risk reversal, clear next step | Convert channels |
| **Retention** | "Did I make the right choice?" | Use, evaluate satisfaction | Onboarding, quick wins, milestone recognition | Retention channels |
| **Loyalty** | "Should I recommend this?" | Refer, advocate, expand | Community, recognition, exclusive value | Referral channels |

### How to build the journey map
1. Start with the JTBD statement from Phase 2 — the trigger event is the entry point
2. For each stage, ask: "Where does the ICP go? What do they search? Who do they ask?"
3. Map the channel that serves each stage (this feeds directly into channel strategy)
4. Identify the **biggest drop-off risk** between stages — this is where to invest first

### B2B Modifier (SiriusDecisions 6-Stage)
For B2B products with longer sales cycles, use the more granular framework:
1. Loosen Status Quo — buyer acknowledges current approach isn't working
2. Commit to Change — buyer decides to actively seek alternatives
3. Explore Solutions — buyer creates a shortlist
4. Commit to Solution — buyer selects preferred option
5. Justify Decision — buyer builds internal case (ROI, stakeholder buy-in)
6. Make Selection — buyer signs/purchases

Map competitive counter-messages to stages 3-5 (where competitors are most visible).

---

## Measurement Setup

### The Measurement Chain
Every marketing plan should model this chain end-to-end before launching any campaign:

```
Budget -> CPM -> CTR -> CPC -> Conversion rate -> CAC -> LTV:CAC
```

If any link is unknown, the plan cannot predict whether spending is profitable. Define assumptions for each link at launch; replace with actuals weekly.

### Pre-Launch Instrumentation Checklist (14-Day Setup)

**Days 1-3: Define**
- [ ] Lock UTM naming convention (see standard below)
- [ ] Define GA4 conversion events (at minimum: page view, signup/purchase, activation milestone)
- [ ] Specify CRM tracking fields (lead source, first-touch UTM, last-touch UTM)
- [ ] Define activation moment (the specific action that predicts retention)

**Days 4-7: Implement**
- [ ] Install GA4 on all pages
- [ ] Configure conversion events in GA4
- [ ] Add UTM parameters to all campaign links
- [ ] Add hidden form fields for UTM capture (pass UTMs from URL into CRM)
- [ ] Install ad platform pixels if using paid channels (Meta, Google, TikTok)

**Days 8-14: Validate**
- [ ] Run end-to-end journey test: click campaign link -> land on page -> convert -> verify UTMs appear in CRM
- [ ] Verify GA4 events fire correctly (use GA4 DebugView)
- [ ] Create a simple attribution dashboard (even a spreadsheet) showing: source -> leads -> conversions -> revenue
- [ ] Document who owns analytics (one person, not "everyone")

### UTM Naming Standard
Consistent, lowercase, no spaces:
- `utm_source`: Platform name (e.g. `linkedin`, `google`, `newsletter`)
- `utm_medium`: Channel type (e.g. `organic`, `paid`, `email`, `referral`)
- `utm_campaign`: Stable campaign name (e.g. `launch-week`, `comparison-post-q2`)
- `utm_content`: Creative variant (optional, for A/B testing)

**Critical rule**: GA4 treats `Email` and `email` as different sources. Use lowercase consistently. Missing UTMs cause 25-30% of traffic to appear as "Direct" — this is the single most common attribution failure.

### What NOT to measure early
- Marketing Mix Modelling (requires 6+ months of data)
- Multi-touch attribution models (requires volume; use first-touch until 1K+ leads)
- Brand lift studies (requires budget and statistical significance)
- Sentiment analysis (useful later, not before PMF)

---

## Retention Campaigns

### The 3 Non-Negotiable Campaigns (First 90 Days)

Every new business needs these three email/notification campaigns before investing in acquisition at scale. 70% of churn is concentrated in users who never completed a specific setup step in week one.

#### 1. Welcome Series (Days 0, 3, 7)

| Email | Timing | Goal | Content |
|-------|--------|------|---------|
| Welcome | Immediately after signup/purchase | Set expectations, deliver first value | Thank you + one clear next action (not a feature tour) |
| Quick win | Day 3 | Drive toward activation milestone | Show the fastest path to the core value moment |
| Social proof | Day 7 | Reinforce decision, reduce buyer's remorse | Customer story or outcome data + second call-to-action |

#### 2. Activation Nudge (Day 3-5, triggered)

Fires only for users who have NOT completed the activation milestone by day 3-5.
- Tone: helpful and diagnostic, not pushy ("We noticed you haven't [action] yet — here's how most people get started")
- Include: a direct link to the activation step, a short video or GIF showing how, and a reply-to address for questions
- Goal: recover 15-25% of stalled users

#### 3. Win-Back Sequence (30-Day Inactive)

Two emails for users/customers who haven't engaged in 30 days:
- Email 1 (Day 30): "We miss you" — highlight what's new or what they're missing. Include a re-engagement incentive if applicable.
- Email 2 (Day 37): "Last chance" — if no response, ask for feedback ("What would make this useful for you?"). Use responses to improve onboarding.
- Expected recovery: 10-15% of dormant users

### 90-Day Retention Roadmap

| Period | Focus | Actions |
|--------|-------|---------|
| Days 1-30 | Foundation | Deploy welcome series, identify activation milestone, segment users (active / stalled / at-risk) |
| Days 31-60 | Activation | Build activation nudge, add milestone celebration emails, run first cohort analysis |
| Days 61-90 | Recovery | Deploy win-back sequence, analyse cohort retention curves, identify the #1 onboarding gap |

### Key Retention Metrics
- **TTFV** (Time to First Value): How quickly does the customer experience the core value? Target: <24 hours for SaaS, <7 days for DTC.
- **7-day activation rate**: % of signups who complete the activation milestone within 7 days
- **30-day retention rate**: % of customers still active at day 30
- **Monthly churn rate**: % of customers lost per month. Benchmark: <5% for SaaS, <8% for DTC
- **Revenue per subscriber**: For email/notification channels — are retention campaigns generating repeat revenue?

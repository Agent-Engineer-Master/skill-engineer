# Methodology Reference — find-my-business

Consolidated frameworks for startup idea discovery and validation. Load during Steps 1-4.

## Table of Contents

1. [Founder Profile Template](#1-founder-profile-template)
2. [Seven Generation Angles](#2-seven-generation-angles)
3. [Validation Sprint Protocol](#3-validation-sprint-protocol)
4. [Six Forcing Questions](#4-six-forcing-questions)
5. [Mom Test Conversation Design](#5-mom-test-conversation-design)
6. [JTBD Analysis Framework](#6-jtbd-analysis-framework)
7. [AI-Era Opportunity Categories](#7-ai-era-opportunity-categories)

---

## 1. Founder Profile Template

Synthesize from context files + interview into these sections:

### Skills & Expertise
- Professional domains (list with depth level: surface / working / deep / expert)
- Technical capabilities
- Operational experience (team size managed, revenue scale, fundraising)

### Unfair Advantages
- Domain intersections others don't have (e.g., "math + biotech + YC network")
- Network access (specific communities, alumni groups, industry contacts)
- Credibility signals (degrees, companies, exits, publications)
- Unusual experiences that give non-obvious insight

### Energy Patterns
- What makes them irrationally excited (even if impractical)
- What drains them (these become anti-goal reinforcements)
- Work style preferences (deep focus vs variety, solo vs collaborative)
- MBTI/personality insights relevant to founder-market fit

### Constraints (Hard Boundaries)
- Time: hours available per week, protected commitments
- Financial: runway, investment capacity, income needs
- Geographic: location, willingness to relocate, timezone
- Personal: family obligations, health considerations

### Anti-Goals (Hard Filters)
- Copied verbatim from `02-vision/anti-goals.md`
- Every idea must pass every anti-goal or be killed immediately

### Networks
- Professional communities with access (YC, INSEAD, consulting alumni, etc.)
- Industry contacts who could be early customers or advisors
- Geographic network strength by region

---

## 2. Seven Generation Angles

Generate candidate ideas from each angle. Note which angle produced each idea — this helps diagnose when the idea pool is too narrow (all from one angle) or too disconnected (none from personal pain).

### Angle 1: Personal Pain (PG — "Notice, Don't Invent")
> "The way to get startup ideas is not to try to think of startup ideas. It's to look for problems, preferably problems you have yourself."

- What has the founder complained about in their professional life?
- What workarounds have they built for themselves?
- What tools do they wish existed?
- What processes at previous jobs were embarrassingly broken?

**Quality test:** "Who wants this so much they'll use it even when it's a crappy version one made by a two-person startup they've never heard of?"

### Angle 2: Unfair Advantage Matching
Cross the founder's skills/networks with known market gaps:
- Where does their expertise intersect with an underserved market?
- What can they build that competitors can't because of unique domain knowledge?
- Which of their networks gives them distribution others lack?

### Angle 3: AI-Era Opportunities
> "What was previously impossible that is now possible with AI?"

- See Section 7 for current AI-native categories
- Filter through founder's domain expertise — which AI opportunities can they credibly pursue?
- Avoid thin wrappers: what proprietary asset (data, workflow, compliance, network effect) would they build on top of the AI capability?

### Angle 4: YC RFS Filtered Through Founder Profile
Current YC Requests for Startups (Spring 2026):
- AI for product management ("Cursor for PMs")
- AI-native agencies (agency output at software margins)
- AI guidance for physical work (multimodal + wearables)
- AI-native hedge funds
- Government AI
- Stablecoins / new financial primitives
- Metal mill modernization
- AI dev tools

**Filter:** Only present RFS categories where the founder has genuine domain knowledge or network access. Generic matches are noise.

### Angle 5: Reddit/HN Pain Mining
Systematic extraction of recurring complaints from community platforms:
1. Identify 3-5 subreddits in the founder's domain
2. Use WebSearch with `site:reddit.com` queries to surface pain signals — no API credentials needed
3. Rank complaints by frequency and lack of existing solution
4. Cross-reference with founder's ability to build a solution

Search query pattern: `site:reddit.com "[subreddit]" "I wish" OR "I hate" OR "why doesn't" OR "is there a tool" OR "frustrated with"`

Run multiple searches varying the subreddits and pain terms. Synthesize into a ranked list of recurring complaints.

### Angle 6: JTBD Analysis
See Section 6. For each domain the founder knows:
- What job are people hiring existing (bad) solutions to do?
- Which outcomes are underserved?
- Where do existing solutions leave the job 80% done?

### Angle 7: Attention Arbitrage (Gary V)
> "Business opportunities emerge from attention arbitrage — platforms where organic reach significantly exceeds production cost."

- Where is attention underpriced in markets the founder understands?
- Which distribution channels does the founder already have credibility on?
- What content could serve as both research and distribution?
- "Document, don't create" — can the search process itself become content?

---

## 3. Validation Sprint Protocol

For each surviving idea, run this compressed sprint. Target: 2-4 hours per idea, not days.

### 3a. Market Research
- Market size (TAM/SAM/SOM) — use WebSearch, be specific about sources
- Growth rate and trajectory
- Timing signal: why now? What changed in the last 2 years?
- Regulatory environment (blockers or tailwinds?)

### 3b. Customer Evidence
Search for real pain signals — not market reports, but actual humans complaining:
- Reddit threads in relevant subreddits
- Product review complaints (App Store, G2, Capterra, Amazon)
- Forum posts, Quora questions, Stack Overflow pain
- Twitter/X complaints about existing solutions

**Evidence quality ladder:**
1. Someone paid for a workaround (strongest)
2. Someone built their own workaround
3. Someone complained publicly and others agreed
4. Someone asked "is there a tool that does X?"
5. Market report says the segment exists (weakest)

### 3c. Competitive Landscape
- Who exists? List by name with pricing and positioning
- What do they miss? (Read real user reviews for complaints)
- Where is the gap? (Underserved segment, missing feature, wrong business model)
- Crowded market = good sign (proves demand). Empty market = question demand.

### 3d. Landscape Awareness (Three-Layer Synthesis)
Adapted from gstack office-hours:
1. **Conventional wisdom:** What does everyone in this space believe?
2. **Current discourse:** What are practitioners actually saying right now? (Reddit, X, HN — last 30 days)
3. **Contradiction check:** Does your evidence contradict the conventional wisdom?

If contradiction exists → flag as potential insight. These are where the biggest opportunities hide.

### 3e. Lean Canvas Draft
Use `assets/lean-canvas-template.md`. Fill in all 9 blocks. Mark uncertain blocks explicitly.

### 3f. Mom Test Script
Generate 5-7 specific conversation questions following Section 5 rules. Include: who to talk to, where to find them, how to open the conversation.

---

## 4. Six Forcing Questions (Validation Battery)

Adapted from Garry Tan's gstack office-hours protocol. Apply during Steps 3-4 to pressure-test each idea. Push until answers are specific and evidence-based.

### Q1: Demand Reality
"What's the strongest evidence someone would be upset if this disappeared tomorrow?"
- Not interest, not waitlists, not "everyone agrees" — actual behavioral demand
- If pre-product: "What's the strongest evidence this problem is real and urgent?"
- Acceptable answers: someone is paying for a bad workaround, someone built their own solution, someone's job depends on solving this

### Q2: Status Quo
"What are people doing right now, badly, to solve this? What does that workaround cost them?"
- The real competitor is never another startup — it's the spreadsheet, the manual process, the intern, the "we just live with it"
- If nobody is doing anything → question whether the problem is real enough

### Q3: Desperate Specificity
"Name the actual human who needs this. What's their title? What gets them promoted or fired? What keeps them awake?"
- "Everyone needs this" = nobody needs this
- "SMBs" is not a customer. "The ops manager at a 20-person logistics company who manually reconciles shipments every Friday afternoon" is a customer

### Q4: Narrowest Wedge
"What's the smallest version someone pays for this week?"
- Not the full platform — the wedge
- Brex launched without user account creation. Users emailed in their password.
- If you can't describe a version someone pays for this week, the idea is too abstract

### Q5: Observation & Surprise
"Have you watched someone struggle with this problem? What surprised you about their behavior?"
- Observation beats interview — what people do differs from what they say
- If you haven't observed → this becomes the validation assignment

### Q6: Future-Fit
"In 3 years, does this product become more essential or less? Why?"
- AI tailwind: does AI make this more valuable (new capabilities) or less (commoditizes it)?
- Market trajectory: growing, stable, or shrinking?
- Regulatory trajectory: more restrictive (moat) or more open (competition)?

---

## 5. Mom Test Conversation Design

From Rob Fitzpatrick's "The Mom Test." These rules are non-negotiable for customer conversations.

### The Three Rules
1. **Talk about their life, not your idea.** Never pitch. Never describe what you're building. Ask about their problems.
2. **Ask about specifics in the past, not opinions about the future.** "Tell me about the last time you had to do X" — not "Would you use a tool that did X?"
3. **Seek commitments and concrete actions, not compliments.** A commitment = deposit, letter of intent, introduction to decision-maker, time booked. A compliment = "Sounds great!" (worthless)

### Three Types of Bad Data (Filter Ruthlessly)
- **Compliments:** "This sounds great!" "I'd definitely use that!" → ignore
- **Hypothetical fluff:** "I would pay $50/month for that" → ignore unless they hand you $50
- **Wishlists:** "It would be cool if it also did X" → note but don't act on

### Good Questions Template
- "Tell me about the last time you had to [do the job this idea addresses]."
- "What was the hardest part about that?"
- "How are you solving that problem today?"
- "What have you tried that didn't work?"
- "How much time/money does this problem cost you per [week/month]?"
- "If you could wave a magic wand and fix one thing about [domain], what would it be?"

### Bad Questions (Never Ask)
- "Would you use a product that does X?" (hypothetical)
- "How much would you pay for this?" (fantasy pricing)
- "Do you think this is a good idea?" (fishing for compliments)
- "What features would you want?" (designing by committee)

### Opening the Conversation
Don't pitch. Frame as learning:
- "I'm researching how [people in role X] handle [problem Y]. Could I ask you a few questions about your experience?"
- "I'm trying to understand [domain]. You seem like someone who deals with this — would you be open to a 15-minute chat?"

### The Only Real Validation Signals
1. They put down a deposit or sign a letter of intent
2. They introduce you to their decision-maker
3. They book a follow-up on their calendar (not "let's stay in touch")
4. They share proprietary information about their workflow
5. They ask when they can start using it

Everything else is noise.

---

## 6. JTBD Analysis Framework

From Clayton Christensen and Tony Ulwick. People don't buy products — they hire them to get a job done.

### How to Apply
1. **Identify the job:** What is the customer trying to accomplish? State at a level of abstraction that makes it an attractive market (not too narrow, not too broad).
2. **Map the current hire:** What are people currently "hiring" to do this job? (May be a competitor, a workaround, or nothing — they just suffer.)
3. **Find underserved outcomes:** What results do customers want from this job that current solutions don't deliver?
4. **Locate the 80% gap:** Where do existing solutions leave the job 80% done? The remaining 20% is the opportunity.

### Quality Test
Ulwick's outcome-driven innovation achieved 86% success rate across 400+ companies — but only when applied rigorously. "Rigorous" means:
- The job is defined at the right abstraction level
- Outcomes are measurable (not "make it better")
- Current solutions are mapped with real usage data
- Underserved outcomes are identified from customer evidence, not assumption

---

## 7. AI-Era Opportunity Categories (2025-2026)

From YC Spring 2026 RFS, a16z Big Ideas 2026, and practitioner research.

### Categories Where AI Creates New Business Types
- **Agent-native infrastructure:** Databases, rate-limiters, coordination layers redesigned for bursty agent workloads
- **AI-native agencies:** Agency output (design, ads, legal, copy) at software margins
- **AI-guided physical work:** Multimodal models + wearables coaching physical tasks in real time
- **Vertical AI going multiplayer:** Domain software evolving from retrieval to multi-stakeholder collaboration
- **Personalization at scale:** Products moving from mass-market to individual-level customization
- **AI for product management:** Synthesizing feedback, proposing features, generating PRDs

### The Moat Question
The most defensible AI businesses are NOT thin wrappers around foundation models. They build proprietary assets:
- Domain-specific training data or fine-tuning
- Workflow integrations that create switching costs
- Regulatory compliance certifications
- Network effects (more users → better product)
- Proprietary data loops (usage data improves the product)

**Filter:** For any AI-era idea, ask: "If OpenAI/Anthropic/Google adds this feature to their base model next quarter, does this business survive?" If the answer is no, the moat is insufficient.

### The Speed Advantage
AI compresses the Build-Measure-Learn loop:
- MVP build time: weeks → days (AI coding assistants)
- Market sizing: days → minutes (AI research tools)
- Interview synthesis: hours → seconds (AI pattern recognition)

Implication: the cost of being wrong drops. More ideas can be tested per unit time. This favors breadth-first search with rapid kill decisions over deep analysis of a single idea.

**But:** AI does NOT replace talking to customers. Founders who use AI to skip customer conversations build better-engineered solutions to problems nobody has.

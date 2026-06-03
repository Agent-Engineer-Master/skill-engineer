# Demand Signals — Leading Indicators of Demand Shifts

## Leading vs lagging — the discriminator

A leading indicator is something you could observe BEFORE the shift hits financial results. Revenue, share, NPS — these are lagging. By the time they move, the market has already noticed and competitive response is underway.

Leading indicators are how analysts get ahead of share-data movement. A demand-side analysis without ≥1 leading signal is not doing the early-warning job it exists to do.

## Required signal format

For each signal:

1. **Signal name** — what to watch (one phrase)
2. **Measurement source** — where the indicator lives (Google Trends, app-store rank, GitHub stars, distributor reorder cadence, regulatory filing keyword frequency, expert-interview language shift, job-posting taxonomy)
3. **Threshold** — what level of change constitutes a meaningful shift (numeric where possible)
4. **What it would mean** — the structural shift the signal would imply

Example (well-formed):
- **Signal:** Job-posting language shift from "Salesforce admin" to "RevOps automation engineer"
- **Measurement source:** LinkedIn job-postings index, keyword frequency by quarter
- **Threshold:** "RevOps automation engineer" exceeding "Salesforce admin" mentions in jobs requiring 5+ years experience
- **What it would mean:** the buying-committee end-user JTBD has shifted from "configure a CRM" to "orchestrate revenue automation across systems" — Salesforce's CRM-centric product becomes the lower-leverage layer

Example (anti-pattern — REJECTED):
- "Watch revenue growth" — lagging
- "Monitor market share" — lagging
- "Track NPS" — lagging and a feeling-state, not a structural shift indicator
- "Customer churn rate" — lagging by the time it moves

## Signal-source catalog

Useful leading-indicator sources by industry type:

### Consumer / B2C
- Google Trends — search-term frequency for the JOB language
- App-store rank velocity, especially for substitute apps
- Reddit / subreddit sentiment + volume on the JOB
- TikTok / short-form content volume around the JOB
- Walmart / Costco SKU rotation cadence (CPG)

### B2B software
- GitHub star velocity for OSS substitutes
- HackerNews / dev-forum mention volume
- Hiring-page job-title taxonomy shifts (large-employer aggregate)
- Procurement RFP keyword shifts (where visible)
- Expert-network interview language shifts ("we used to ask about X, now they ask about Y")

### Healthcare / regulated
- FDA / EMA filing keyword frequency
- ClinicalTrials.gov enrollment velocity for substitute mechanisms
- Payer policy-language shifts (coverage decisions are leading-vs-lagging on adoption)
- Specialty-society guideline updates

### Industrial / B2B physical
- Distributor reorder cadence (the most accurate near-term demand signal in physical industries)
- Trade-show booth count and floor share by category
- Customs / import data on substitute inputs
- Equipment-as-a-service contract terms — shift from purchase to subscription is a substitution signal

### Cross-cutting
- LinkedIn job-posting taxonomy
- Patent filing velocity in adjacent categories
- Capex announcements from large buyers in the segment
- Earnings-call language shifts (Q&A keyword frequency over time across the industry)

## "What would I need to see to change my mind?" — the disciplined version

The best demand signal is the one that would falsify your current view. Frame at least one signal as: *"If [observable measurable thing] crossed [threshold], I would re-rate substitution risk from Low to High."* This is the test that distinguishes a thoughtful demand analysis from a passive one.

## Failure modes

- **Lagging indicator framed as leading** — revenue, share, NPS. Rejected.
- **Signal without a measurement source** — "watch the market." Not actionable.
- **Signal without a threshold** — "watch search trends." Search trends for WHAT, crossing WHAT level?
- **Signal without an interpretation** — what would it MEAN if this signal moved? Without that, it is data without analysis.
- **Listing every conceivable signal** — pick the 1-3 that would actually change the decision. More signals = less signal.

# Customer Segmentation — JTBD-Based, Not Demographic

## The core principle

Demographic and firmographic segmentation describe WHO the buyer IS. JTBD-based segmentation describes WHAT THE BUYER IS TRYING TO ACCOMPLISH. For industry analysis, only the second is predictive.

The reason: demographic attributes do not predict willingness to switch. Two "mid-market US manufacturers with 200-500 employees" can be hiring the product to do entirely different jobs, and their substitution behavior will diverge accordingly. Conversely, a Fortune-500 buyer and a 20-person startup hiring the product for the same JOB (e.g., "produce an SBOM that survives a customer audit") will behave structurally similarly when a substitute appears.

## Anti-patterns (REJECTED by validator)

These segment names fail because they are pure demographic/firmographic boxes:

- "Young urban professionals, 25-34"
- "Mid-market enterprises in financial services"
- "SMB customers, <50 employees"
- "Manufacturers with >$500M revenue"
- "Gen-Z consumers"
- "Enterprise IT buyers"
- "DACH-region customers"
- "Tier-1 OEMs"

If your segment can be expressed entirely as a filter on a CRM — it is not a JTBD segment.

## Correct patterns (ACCEPTED)

These segment names describe the JOB the buyer is hiring the product to do:

- "Buyers hiring the product to compress a 6-week manual reconciliation cycle into a single audit-ready report"
- "Buyers hiring the product as career insurance against a known regulator escalation pattern"
- "Buyers hiring the product to enable a single specialist to do the work that previously required a team of four"
- "Buyers hiring the product to remove the dependency on a single retiring expert"
- "Buyers hiring the product to demonstrate ESG compliance to a downstream customer who is being audited"
- "Buyers hiring the product to convert a capex purchase into an opex subscription for cash-flow reasons"

The leading clause is "Buyers hiring the product to [verb] [object] [contextual qualifier]." If the leading clause can be written this way, the segment is JTBD-based.

## Hybrid (acceptable with care)

Sometimes a segment is GENUINELY clustered by both job AND a firmographic attribute (e.g., "Regulated EU pharma buyers hiring the product to maintain Annex 11 audit trail readiness"). This is acceptable provided:

1. The JTBD clause leads the segment name (not the firmographic clause)
2. The firmographic attribute is causally tied to the job, not decorative
3. Removing the firmographic would meaningfully change the segment's JTBD or WTP profile

If the firmographic could be stripped without changing the analysis, strip it.

## How many segments?

Minimum 2. The point is to show the market is NOT a single homogenous demand pool. Three to six is typical for industry-analysis altitude. More than seven and the segmentation is probably operating at product-design altitude, not industry altitude.

## Distinguishing axes (cluster by these, not demographics)

When defining segments, the useful axes are:

- **Job priority** — what the buyer is primarily hiring the product to do
- **Outcome importance/satisfaction pattern** — where they are under-served (Ulwick)
- **Substitution proximity** — how close a cross-category substitute already is
- **Switching cost profile** — what would have to be true for them to switch
- **WTP driver** — what determines the price ceiling

Two segments are genuinely distinct when their substitution behavior or WTP profile would diverge meaningfully under the same external shock.

## Common segmentation failure mode in PE-CDD work

In private-equity commercial due diligence under time pressure, the drafter often inherits demographic segmentation from the target's marketing materials. This is the path of least resistance and is almost always wrong for assessing structural demand risk. The CDD reader is making a structural-risk decision; demographic segmentation hides the risk. Insist on JTBD restatement even when the target's own materials are demographic.

# Learnings — reimagine-industry

Behavioral preferences and patterns learned during use. Updated at the closing feedback gate after each run.

## What Has Worked

- **Synthesizing Phase 1 from existing research instead of dispatching librarian** when the industry has substantial prior research in `08-knowledge/resources/` and `03-exploration/`. Phase 1 is structural deconstruction — it doesn't need fresh research if structured material already exists. Run `dtc-ecommerce-us` 2026-05-19 collapsed from 3 planned librarian dispatches to 1.
- **Hard-excluding a specific prior concept from Phase 5 inputs** when the user has explicitly moved away from it. Prevents anchoring. Done at Gate 1 in `dtc-ecommerce-us` against the AI-native-founder-platform concept; effective.
- **De-duplicating overlapping Move outputs at the Phase 5 filter** (M3 + M5 collapsed into single AUTH concept). Diversity check passed cleanly afterward.
- **Running the bar test twice when the first pass returns ITERATE** — fix the specific flagged issues inline, then re-dispatch with a different sub-agent role framing. `dtc-ecommerce-us` 2026-05-19 went ITERATE → PASS on second pass.

## What Has Failed

- **Presenting Thiel Secrets as "endorsement filters" without sufficient framing.** In the `dtc-ecommerce-us` run, the user endorsed 6 of 10 Secrets but clarified afterward: "this is not high conviction, I just think these are positions where the data is inconclusive either way." The skill's framing implies Secrets are load-bearing convictions that filter out concepts — but at the contrarian-question stage, most are open empirical bets, not high-conviction beliefs. Presenting them as conviction filters created cognitive overhead and risked over-filtering Phase 5 concepts on the basis of bets the user did not actually hold.
- **Jargon-heavy concept descriptions in Gate 2 and Gate 3 reviews.** Business model framings and Thiel Secret summaries read like code rather than plain English. User had to explicitly ask for plain-English re-explanation at both gates. The core idea of each concept (and each Secret) needs to be distilled to its essence and given a memorable name/handle before being presented for review.

## Patterns and Preferences

- **Thiel Secrets as lenses, not filters.** Re-frame Phase 4.6 Secrets as "strategic lenses that suggest experiments to run" rather than "high-conviction filters that eliminate concepts." A Secret is a great pivot point that defines what the strategy could become if it turned out true — but at the brief-writing stage it's an open question, not a decided bet. Phase 5 should generate concepts that span the Secret's hypothesis space rather than pre-filter on the Secret being true.
- **Always provide a plain-English layer at each gate.** Every concept, Secret, and framework signal that surfaces in a human-gate review needs a one-sentence plain-English distillation alongside its structured form. The structured form is for the dataset; the plain-English distillation is for the human gate. Don't make the human ask twice.
- **Name concepts memorably.** Each Phase 5 concept needs a short handle (3-5 words) that captures the core idea, not just a `concept_id`. "Wirecutter-for-niche, AI-citation-first" works; "AUTH-DTC" does not on its own. The handle should be self-descriptive enough that a senior reader knows what the concept IS without needing to read the one-liner.
- **Explain new concepts and competitive color in Gate 2 why-now zones.** When Gate 2 introduces new opportunity-zone concepts, give each one a fuller plain-English explanation before asking for approval: what it means, why the window is open, and how it maps to the framework signals. If a window is "open with competition," include a short competitor overlay inside the original HTML, mapped to each zone and related signals. The user found it useful to understand both the new concept itself and which players already pressure each zone, e.g. AI-native advisory firms for the supervised agentic bank idea, VDR/CRM/deal-management platforms for the process-control layer, and sourcing/matching networks for buyer-network quality.
- **Gate 3 concepts must be product-crystal-clear, not just strategically interesting.** For every shortlisted idea, include an explicit plain-English block covering: exact customer, customer pain, proposed day-one product, core workflow/artifacts, value proposition, first paid version, and why someone would buy now. Do this inside the original Gate 3 HTML and `venture-concepts.md`, not only in follow-up chat. The user should not have to infer the product from phrases like "control point," "wedge," or "compounding asset."
- **Diagram-light at present.** User is planning to upgrade gate reports from markdown to HTML to support diagrams. Until then, keep gate-review prose tight and use tables aggressively for any multi-concept comparison.

## Open Questions

- How should Phase 4.6 distinguish between "Thiel Secret as conviction filter" (the literal Thiel framing) and "Thiel Secret as scenario lens" (the more useful framing for early-stage exploration)? Both are valid in different contexts. Consider adding a Gate-2 sub-prompt that asks the user which framing they're operating in.
- Should the skill auto-generate plain-English concept handles in Phase 5 alongside the `concept_id`, or surface this as a Gate-3 final-naming step?

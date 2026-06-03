# Senior-Analyst Bar Test

Protocol for grading an industry brief (or sub-skill output) against the standard of a senior sub-sector analyst.

## The bar

A senior analyst in this industry, reading the brief in their own sub-sector, should:
- Find at least 3 non-obvious observations they had not articulated
- Not find any obvious observations missing
- Recognize the framing and vocabulary as current (2026), not legacy (2005)

## How to invoke

The bar test is run by a **fresh-context sub-agent** that does NOT have the drafting context. This prevents motivated reasoning by the drafter.

```
python scripts/bar_test.py --brief-path <path-to-brief.md> --industry "<industry-slug>"
```

The script spawns a sub-agent with the brief file but not the drafting transcript, prompted to:

> "You are a senior sub-sector analyst with 15 years of experience in [industry]. Read this brief. You are being paid to find what is missing or weak. Return:
> 1. At least 3 non-obvious observations the brief surfaces that you had not previously articulated.
> 2. At least 5 obvious observations the brief correctly captures.
> 3. Any obvious observations that are MISSING — this list must be empty before the brief ships.
> 4. Any factual claims that read as overconfident given the cited evidence.
> 5. Any 2005-era framing that should be modernized (e.g., raw SWOT, BCG matrix, value chain without profit pool overlay).
> 6. **Internal-consistency check** — any place where the WTP/HTW recommendation (or any conclusion section) contradicts a structural finding earlier in the brief. Examples: the analysis argues the data moat is sub-segment-specific but the recommendation acquires across distinct sub-markets; the analysis flags rivalry as governing but the recommendation depends on premium pricing; the profit-pool inversion is identified but the WTP targets the high-revenue / low-profit layer. The list must be empty — 'defer to Phase 2' is NOT a valid resolution; the brief must either resolve the contradiction in-text or change the recommendation to be consistent with the structural analysis."

## Pass criteria

A brief passes bar test when:
- Non-obvious observations: ≥3
- Obvious-captured observations: ≥5
- Obvious-missing list: empty
- Overconfidence flags: zero (or all resolved)
- Modernization flags: zero (or all resolved)
- **Internal-consistency contradictions: zero (or all resolved in-text — not deferred)**

If any criterion fails, the orchestrator iterates the relevant sub-skill output(s) and/or the synthesis section, and re-runs the bar test before Gate 3 approval. Iteration is mandatory; "log and defer" is not a valid resolution path for any failed criterion.

## Anti-patterns

- ❌ Running the bar test from the same context that wrote the brief (motivated reasoning)
- ❌ Accepting "no obvious observations missing" on first pass without surfacing the prompt: always require the sub-agent to actively look for gaps
- ❌ Treating the bar test as a polish step (it is the structural quality gate before final delivery)

## Modernization watchlist (2026)

Flag these as legacy framing:
- Raw SWOT without supporting structural analysis
- BCG Growth-Share Matrix as primary tool (absorbed into Three Horizons portfolio logic)
- Five Forces without complementors / sixth force / AI-as-force consideration
- Value chain without profit pool overlay
- Strategic groups without arenas qualification
- "Competitive advantage" without naming which of Helmer's 7 Powers
- "Moat" without specifying benefit + barrier
- TAM/SAM/SOM without G3 granular decomposition
- "Where to compete" instead of "where to play / how to win"

Inherited from `build-company-model`; modernized for industry-level analysis.

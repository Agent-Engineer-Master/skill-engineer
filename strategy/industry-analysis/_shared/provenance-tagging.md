# V/C/A/I Provenance Tagging

Every fact-claim about an industry, market, or competitor in any industry-analysis sub-skill output carries an inline provenance tag in the form `[X: source]`, where X is one of:

| Tag | Meaning | When to use | Example source |
|-----|---------|------------|----------------|
| **V** | **Validated** | Claim sourced directly from a primary document, regulatory filing, or audited financial. The strongest tag. | `[V: Acme 10-K 2024]`, `[V: EU MDR Annex VIII]` |
| **C** | **Corroborated** | Claim independently reported by ≥2 credible third-party sources (analyst notes, trade press, expert interviews). Cite at least one. | `[C: McKinsey Industrial Report 2024 + IBISWorld 2025]` |
| **A** | **Asserted** | Claim from a single source — typically management, a vendor, or a single analyst. Treat with skepticism. | `[A: management presentation]`, `[A: vendor pitch deck]` |
| **I** | **Inferred** | Claim derived by analysis (gap inference, peer benchmark, triangulation). Cite the inference basis. | `[I: peer-benchmark — top quartile achieves 18%; target reports 11%]` |

## Rules

- **Every fact-claim about external state carries a tag.** Statements about analytical framework choice or methodology do not require tags.
- **No untagged numeric claim is allowed in any final output.** A revenue number, growth rate, market share, or margin figure without a tag fails validation.
- **One tag per claim, inline.** Place the tag at the end of the sentence or after the specific datum it qualifies.
- **Asserted claims must be flagged in synthesis.** If a load-bearing conclusion rests on an `[A]`-tagged claim, the orchestrator's bar-test surfaces it as a risk.
- **Inferred claims must be explainable.** The inference basis is part of the tag — `[I]` alone is invalid.

## Anti-patterns

- ❌ "The market is growing at 12% per year." (no tag)
- ❌ "The market is growing at 12% per year. [Source: industry report]" (vague source, wrong format)
- ❌ "Management says margins are improving. [A]" (no specificity on inference basis)
- ✅ "The market is growing at 12% per year [C: IBISWorld 2025 + Statista 2024]."
- ✅ "Top-quartile players achieve 18% EBIT margin [I: peer benchmark across 5 listed comparables]."

## Why this exists

A claim's strength is invisible without provenance. Two analysts can write identical-looking briefs where one is solid and one is air. The tag is the contract that forces the writer to know — and the reader to see — where every fact comes from. This is the discipline that separates a McKinsey-grade brief from a polished hallucination.

Inherited from `build-company-model` for consistency across the analysis stack.

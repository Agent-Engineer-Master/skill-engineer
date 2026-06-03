# industry-analysis

A collection of MBB-style industry-structure analysis skills. One orchestrator (`analyze-industry`) plus 7-8 peer sub-skills, each runnable standalone or composed by the orchestrator.

## When to use

- Industry attractiveness assessment (PE due diligence, market entry, capital allocation)
- Competitive structure analysis ("is this industry structurally attractive?")
- Where-to-play / how-to-win strategic choice work
- Pre-deal industry brief at PE-grade CDD speed and quality

Do **not** use for:
- Single-company analysis → use `build-company-model`
- DTC category go/no-go verdict → use `assess-category`
- Decision pressure-testing → use `stress-test`
- Buyer/investor universe building → use `building-buyer-shortlists`

## Skills in this collection

**Tier 1 — Structural analysis** (orchestrator + sub-skills):

| Skill | Standalone use | Role in orchestrator |
|-------|---------------|---------------------|
| `analyze-industry` | Synthesizes industry brief | Orchestrator |
| `assess-strategic-environment` *(Phase 2)* | Diagnose competitive environment type | Run first — routes other sub-skills |
| `size-market` | Granular market sizing | Always run |
| `map-five-forces` | Industry structure analysis | Always run |
| `map-value-chain-profit-pools` | Value capture analysis | Always run |
| `map-competitive-arena` *(Phase 2)* | Strategic groups + arenas overlay | Run for active markets |
| `analyze-trajectory` *(Phase 2)* | S-curve + Three Horizons + discontinuities | Run when direction matters |
| `assess-moat-sources` *(Phase 2)* | Helmer's 7 Powers durability judgment | Run last — converts to "so what" |
| `analyze-demand` *(Phase 2, optional)* | JTBD + substitution risk | Skip for stable-demand mature industries |

**Tier 2 — Creative ideation** (runs AFTER tier 1):

| Skill | Standalone use | Role |
|-------|---------------|------|
| `reimagine-industry` | Generates ranked venture concept shortlist via 6-phase workflow | Creative "so what" layer that follows structural diagnosis — applies Blue Ocean ERRC, Aggregation Theory, Decoupling, Counter-positioning, 7 Powers, Thiel's Secret against a structured disruption-dataset.yaml |

## Invoke directly

Library-tier: not auto-routed. Invoke explicitly:

- Orchestrator: `run the analyze-industry skill on [industry] with [scope question]`
- Sub-skill: `run the map-five-forces skill on [industry]`
- Reimagination: `run the reimagine-industry skill on [industry]` (most useful after `analyze-industry`)

## Shared assets

Files in `_shared/` are referenced by every skill in this collection:

- `provenance-tagging.md` — V/C/A/I claim attribution (Validated / Corroborated / Asserted / Inferred)
- `bar-test.md` — fresh-context senior-analyst grading protocol
- `pyramid-scqa.md` — synthesis discipline for the orchestrator output
- `2026-terminology.md` — current MBB vocabulary (drives skill descriptions and output language)
- `output-conventions.md` — file naming, output locations under `08-knowledge/world-model/industries/`

## Output destination

All industry briefs land in `08-knowledge/world-model/industries/[industry-slug]/`. Sub-skill outputs land in that folder's `working/` subdirectory when called by the orchestrator, or one-off paths when called standalone.

## Design provenance

Built 2026-05-18 informed by:
- Librarian deep research on current MBB practice (McKinsey/BCG/Bain/Deloitte/LEK/OC&C): `08-knowledge/resources/2026-05-18-mbb-industry-analysis-skill-research.md`
- Pattern reference: `build-company-model` (V/C/A/I, gates, bar-test); `building-buyer-shortlists` (orchestrator + sub-agent pattern)
- Prior art surveyed: `gcamilo/management-consulting`, `yennanliu/InvestSkill`, `phuryn/pm-skills`

# Strategy

Skills for founders, operators, investors, and strategists who need AI agents to run MBB-grade industry and competitive analysis — structural diagnosis, market sizing, moat assessment, and venture ideation.

## Skills

This domain contains the **[industry-analysis](industry-analysis/)** family — a coordinated set of strategy skills built on the BCG Strategy Palette, McKinsey G3 / Arenas, Porter Five Forces and value chain, Bain profit pools, Helmer 7 Powers, and Christensen JTBD. `analyze-industry` orchestrates the sub-skills into a single quality-reviewed brief; every sub-skill is also invocable standalone. Shared methodology (provenance tagging, Pyramid/SCQA, the senior-analyst bar test) lives in `industry-analysis/_shared/`.

| Skill | Description | When to Use |
|---|---|---|
| [analyze-industry](industry-analysis/analyze-industry/) | Orchestrates the sub-skills below into a senior-analyst industry-structure brief — Strategy Palette, G3 sizing, Five Forces, profit pools, arenas, S-curve, 7 Powers, JTBD — shipped as a quality-reviewed HTML report ending in where-to-play / how-to-win | Industry attractiveness, market entry, PE deal screening, or roll-up thesis |
| [reimagine-industry](industry-analysis/reimagine-industry/) | Produces a ranked shortlist of venture concepts to disrupt an industry via a 6-phase workflow applying Blue Ocean ERRC, Aggregation Theory, Decoupling, Counter-positioning, 7 Powers, and Thiel's Secret | Finding disruption angles or venture concepts in an industry |
| [assess-strategic-environment](industry-analysis/assess-strategic-environment/) | Diagnoses the competitive environment (BCG Strategy Palette — Classical / Adaptive / Visionary / Shaping / Renewal) via the predictability / malleability / harshness discipline and emits a sub-skill routing matrix | Classifying an industry's strategic environment before choosing analytical tools |
| [size-market](industry-analysis/size-market/) | Granular market sizing (McKinsey G3 decomposition + arenas screen) with top-down / bottom-up triangulation, TAM/SAM/SOM, and sub-segment growth rates | Sizing an industry or sub-segment; TAM SAM SOM |
| [map-five-forces](industry-analysis/map-five-forces/) | Porter Five Forces extended with complementors (sixth force) and AI-as-named-force; names the governing force that determines profit distribution | Assessing industry structural attractiveness |
| [map-value-chain-profit-pools](industry-analysis/map-value-chain-profit-pools/) | Paired Porter value-chain decomposition + Bain profit-pool overlay showing absolute EBIT / economic profit per stage and where profit concentrates | Finding where the money sits in an industry |
| [map-competitive-arena](industry-analysis/map-competitive-arena/) | Porter strategic-group map with McKinsey Arenas overlay — ≥3 groups, winner archetypes, and a mobility-barrier matrix | Mapping the competitive landscape and who competes with whom |
| [analyze-trajectory](industry-analysis/analyze-trajectory/) | Forward-looking trajectory — dual S-curve, Three Horizons, discontinuities catalog, Helmer Power Progression, and base/bear/bull scenarios over a 5-year horizon | Understanding where an industry is heading; scenario analysis |
| [assess-moat-sources](industry-analysis/assess-moat-sources/) | Assesses which of Helmer's 7 Powers protect incumbents, how durable each is, and which Power combination the winning archetype must hold | Judging moat durability in an industry |
| [analyze-demand](industry-analysis/analyze-demand/) | Structural demand-side analysis — JTBD, JTBD-based segmentation, substitution risk per segment, WTP drivers, and leading demand signals | Understanding demand structure and substitution risk for an industry |

## When to use this domain

Use strategy skills when a decision turns on industry *structure* rather than a single company or a quick take — market entry, capital allocation, a roll-up thesis, or where to aim a new venture. `analyze-industry` is the front door: it diagnoses the environment first, then weights and runs the right sub-skills, reconciles their outputs, and ships a brief that clears a senior-analyst bar test. Reach for individual sub-skills when you need just one lens (a sizing, a Five Forces, a moat read), and `reimagine-industry` when the goal is to disrupt rather than to evaluate.

**Dependencies:** the brief deliverables render via [`design/html-output`](../design/html-output/) and are graded by [`operations/analysis-quality-review`](../operations/analysis-quality-review/). Install those two alongside this domain for the full pipeline.

---

*Part of the [Skill Engineer](https://agentengineermaster.com) shared skills library.*

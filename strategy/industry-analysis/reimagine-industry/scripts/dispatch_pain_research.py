"""Generate a structured librarian brief for Phase 2 or Phase 3 research.

Reads the partially-populated disruption-dataset.yaml, extracts the value chain
(or the industry definition for Phase 3), and writes a librarian brief file
that the orchestrator's host agent will pass to the librarian via the Task tool.

This script does NOT spawn the librarian itself — that's the orchestrator's job.
It generates the brief so the dispatch is structured and consistent.

Usage:
    python dispatch_pain_research.py --slug <slug> [--mode pain|enabling-conditions]

Default mode: pain (Phase 2 value chain pain audit).

Output:
    Writes <industry-dir>/working/librarian-brief-<mode>.md
    Prints the brief path to stdout.
"""

import argparse
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[5]
INDUSTRIES_DIR = REPO_ROOT / "08-knowledge" / "world-model" / "industries"


PAIN_BRIEF_TEMPLATE = """# Librarian Brief — Phase 2 Value Chain Pain Audit

Industry: {slug}
Dataset path: {dataset_path}

## Goal

Research pain points across EVERY entity in the {slug} value chain — not just
end-customers. This widens the disruption surface to include supplier pain
(Shopify pattern), intermediary pain (Stripe pattern), and non-consumer pain
(Christensen new-market footholds).

## Value chain entities to research

Read the value_chain block in {dataset_path} for the specific nodes.
Default entity types:

  - Customers / end users (segment by behavior or situation, not demographic)
  - Suppliers / producers / manufacturers
  - Intermediaries / distributors / platforms
  - Adjacent players (complementors, regulators)
  - Non-consumers (people excluded from the market today)

## For each entity, return

  - Top 3-5 pain points with intensity signals
  - Source of evidence: Reddit threads, forum complaints, review sites
    (G2/Capterra for B2B), trade press, earnings calls mentioning friction,
    regulatory filings, expert interview write-ups
  - Workarounds people use today (this is GOLD for disruption ideation)
  - V/C/A/I provenance tag per pain point

## Output format

Structured Markdown sections per entity type. Within each entity:

  ### [Entity name]
  #### Pain points
  - **Pain:** [description]
    - Intensity: [1-10] | Frequency: [1-10]
    - Workaround: [specific workaround, or "no workaround named"]
    - Evidence: [source URL or citation]
    - Tag: [V/C/A/I]

## Output file

Save to: 08-knowledge/world-model/industries/{slug}/working/value-chain-pain-audit.md

## Iron rules

- Every pain claim has a V/C/A/I tag
- Behavioral or situational segments only (not "women 25-34")
- Workarounds are load-bearing — if a customer doesn't have one, flag the pain
  as potentially hypothetical
- Include functional, emotional, AND social jobs where relevant (not just functional)
"""


ENABLING_CONDITIONS_BRIEF_TEMPLATE = """# Librarian Brief — Phase 3 Enabling Conditions Scan

Industry: {slug}
Dataset path: {dataset_path}

## Goal

Research enabling conditions that make disruption of {slug} viable TODAY that
weren't true 3-5 years ago. The goal is dated, evidence-backed conditions —
not "AI is hot" handwaves.

For each of the 5 unlock types, return 2-4 specific candidate conditions.

## AXIS 1 — TECHNOLOGY UNLOCKS

What capabilities are newly available? Search for:
  - Cost crossings (LLM token cost, compute, bandwidth, sensor cost)
  - Capability emergence (multimodal AI, real-time translation, vector search)
  - Platform availability (new APIs, SDKs, infrastructure primitives)
  - Run last30days skill on "{slug} AI", "{slug} technology" if available

## AXIS 2 — COST CURVE CROSSINGS

What input cost just made a previously-uneconomic model viable? Search for:
  - Wright's law curves
  - Moore's law adjacencies
  - Logistics, labor, energy cost trends
  - Customer acquisition costs

## AXIS 3 — BEHAVIORAL SHIFTS

What did customers, workers, or partners just start doing differently?
  - Adoption-curve crossings
  - Generational handoffs
  - Post-COVID normalizations
  - New platform behaviors
  - Trust thresholds

## AXIS 4 — REGULATORY CHANGES

What's newly permitted or newly restricted?
  - Recent legislation
  - Agency rule changes
  - Court rulings
  - International harmonization
  - Sandbox programs

## AXIS 5 — SUPPLY-SIDE AVAILABILITY

What supply exists now that couldn't be aggregated before?
  - Fragmentation that's been organized (gig labor, spare capacity, latent inventory)
  - Formalization of informal supply
  - New standardization (APIs, schemas, protocols)

## For each condition, return

  - id: short slug
  - axis: tech | cost | behavioral | regulatory | supply
  - what_changed: one sentence, specific
  - when: year and quarter
  - maturity: emerging | available | commoditized (for tech and supply axes)
  - relevance: why this removes a constraint in {slug}
  - tag: V/C/A/I with source

## Output file

Save to: 08-knowledge/world-model/industries/{slug}/working/enabling-conditions-scan.md

## Iron rules

- Every condition has a year (quarter where possible)
- Every condition has a V/C/A/I tag with source
- Maturity is required for tech and supply conditions
- "Recently" or "in the last few years" is not acceptable — name the date
- If a condition is genuinely N/A for this industry, write that explicitly
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--slug", required=True)
    parser.add_argument("--mode", choices=["pain", "enabling-conditions"], default="pain")
    args = parser.parse_args()

    industry_dir = INDUSTRIES_DIR / args.slug
    if not industry_dir.exists():
        print(f"ERROR IndustryDirMissing: {industry_dir} not found.", file=sys.stderr)
        print("Fix: run init_reimagination.py first.", file=sys.stderr)
        return 2

    dataset_path = industry_dir / "disruption-dataset.yaml"
    if not dataset_path.exists():
        print(f"ERROR DatasetMissing: {dataset_path} not found.", file=sys.stderr)
        print("Fix: run init_reimagination.py first.", file=sys.stderr)
        return 2

    template = PAIN_BRIEF_TEMPLATE if args.mode == "pain" else ENABLING_CONDITIONS_BRIEF_TEMPLATE
    brief_content = template.format(slug=args.slug, dataset_path=dataset_path.as_posix())

    brief_path = industry_dir / "working" / f"librarian-brief-{args.mode}.md"
    brief_path.parent.mkdir(parents=True, exist_ok=True)
    brief_path.write_text(brief_content, encoding="utf-8")

    print(str(brief_path))
    print(
        "Next: orchestrator spawns librarian agent with this brief; librarian writes "
        f"output to working/{'value-chain-pain-audit.md' if args.mode == 'pain' else 'enabling-conditions-scan.md'}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

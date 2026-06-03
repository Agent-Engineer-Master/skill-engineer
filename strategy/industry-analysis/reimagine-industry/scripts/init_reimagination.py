"""Initialize a reimagine-industry run.

Creates or extends the industry folder under 08-knowledge/world-model/industries/[slug]/
with a skeleton disruption-dataset.yaml. Detects existing analyze-industry outputs
to inherit (industry-brief.yaml, working/value-chain-profit-pools.md, etc.).

Usage:
    python init_reimagination.py --slug <industry-slug> --question "<scope-question>"

Expected stdout:
    Path to the disruption-dataset.yaml created.
    List of inherited inputs detected (for Gate 1 display).

Error taxonomy:
    - InvalidSlug: slug fails lowercase-hyphen validation
    - SchemaMissing: dataset-schema.yaml template not found
"""

import argparse
import datetime
import json
import re
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
REPO_ROOT = Path(__file__).resolve().parents[5]
INDUSTRIES_DIR = REPO_ROOT / "08-knowledge" / "world-model" / "industries"
TEMPLATE = SKILL_DIR / "assets" / "templates" / "disruption-dataset.yaml"


# Files written by analyze-industry sub-skills that we can inherit from.
# Maps inherited file -> which Phase it informs.
INHERITED_INPUTS = {
    "industry-brief.yaml": "all phases (industry definition + structural priors)",
    "industry-brief.html": "all phases (narrative context)",
    "working/value-chain-profit-pools.md": "Phase 1 (industry deconstruction)",
    "working/market-sizing.md": "Phase 1 (industry size + segments)",
    "working/five-forces.md": "Phase 4.4 (counter-positioning incumbent analysis)",
    "working/demand.md": "Phase 2 (value chain pain audit — customer side)",
    "working/trajectory.md": "Phase 3 (enabling conditions — discontinuities)",
    "working/moat-sources.md": "Phase 4.5 (7 Powers mapping)",
    "working/competitive-arena.md": "Phase 4 (strategic groups context)",
    "working/strategic-environment.md": "Phase 4 (environment-routed framework weighting)",
    "signals-log.md": "Phase 5 (rejected concepts from prior runs)",
}


def validate_slug(slug: str) -> bool:
    return bool(re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", slug))


def detect_inherited(industry_dir: Path) -> list[dict]:
    """Return list of inherited files actually present."""
    found = []
    for rel_path, informs in INHERITED_INPUTS.items():
        full_path = industry_dir / rel_path
        if full_path.exists():
            found.append({
                "path": rel_path,
                "informs": informs,
                "size_bytes": full_path.stat().st_size,
            })
    return found


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize reimagine-industry run.")
    parser.add_argument("--slug", required=True)
    parser.add_argument("--question", required=True)
    args = parser.parse_args()

    if not validate_slug(args.slug):
        print(f"ERROR InvalidSlug: '{args.slug}' must be lowercase with hyphens only.", file=sys.stderr)
        print("Fix: use only [a-z0-9-], e.g. 'dtc-ecommerce-us'.", file=sys.stderr)
        return 2

    if not TEMPLATE.exists():
        print(f"ERROR SchemaMissing: {TEMPLATE} not found.", file=sys.stderr)
        print("Fix: ensure assets/templates/disruption-dataset.yaml exists in skill folder.", file=sys.stderr)
        return 2

    industry_dir = INDUSTRIES_DIR / args.slug
    (industry_dir / "working").mkdir(parents=True, exist_ok=True)

    # Inherit or create dataset
    dataset_path = industry_dir / "disruption-dataset.yaml"
    if not dataset_path.exists():
        template_content = TEMPLATE.read_text(encoding="utf-8")
        dataset_path.write_text(template_content, encoding="utf-8")

    # Create signals-log if missing (shared with analyze-industry; do not overwrite)
    signals_log = industry_dir / "signals-log.md"
    if not signals_log.exists():
        signals_log.write_text(
            f"# Signals Log — {args.slug}\n\nAppend-only catalysts, discontinuities, "
            "and rejected concepts with rationale.\n",
            encoding="utf-8",
        )

    # Update or create run-log
    run_log = industry_dir / "run-log.json"
    if run_log.exists():
        metadata = json.loads(run_log.read_text(encoding="utf-8"))
    else:
        metadata = {"industry_slug": args.slug, "events": []}
    metadata.setdefault("events", []).append({
        "event": "reimagine-initialized",
        "ts": datetime.datetime.utcnow().isoformat() + "Z",
        "scope_question": args.question,
    })
    run_log.write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    inherited = detect_inherited(industry_dir)

    # Output
    print(str(dataset_path))
    print("---INHERITED-INPUTS---")
    if inherited:
        for item in inherited:
            print(f"  {item['path']} — informs {item['informs']} ({item['size_bytes']} bytes)")
    else:
        print("  (none — librarian dispatch required for Phases 1-3)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

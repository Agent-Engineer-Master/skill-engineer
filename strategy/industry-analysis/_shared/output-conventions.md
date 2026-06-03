# Output Conventions

Where industry-analysis outputs land and how they are named.

## Industry slug

A short, lowercase, hyphenated identifier for the industry being analyzed. Specific enough to disambiguate.

- ✅ `industrial-robotics-na`
- ✅ `off-price-specialty-apparel-us`
- ✅ `medtech-cardiology-eu`
- ❌ `retail` (too broad)
- ❌ `IndustrialRobotics` (wrong case)

## Output location — orchestrator-driven analysis

When the orchestrator (`analyze-industry`) runs, all outputs land in:

```
08-knowledge/world-model/industries/[industry-slug]/
├── industry-brief.html         # Final synthesis — reader-facing HTML report (rendered via html-output)
├── industry-brief.yaml         # Structured filters for downstream skill consumption (machine artifact)
├── signals-log.md              # Append-only catalysts, discontinuities, dated entries (machine/log artifact)
├── bar-test.md                 # Senior-analyst grading output (audit substrate)
├── bar-test-prompt.md          # Fresh-context sub-agent prompt for the bar test (audit substrate)
└── working/                    # Audit substrate — not reader-facing, stays markdown
    ├── authoring-spec.md        # Filled-in analysis-quality-review authoring spec (ghost-deck, step 6a)
    ├── industry-brief-draft.md  # Markdown synthesis draft — source for the HTML render
    ├── strategic-environment.md
    ├── market-sizing.md
    ├── five-forces.md
    ├── value-chain-profit-pools.md
    ├── competitive-arena.md
    ├── trajectory.md
    ├── moat-sources.md
    └── demand.md               # (only if analyze-demand was run)
```

The `analysis-quality-review` audit directory for an orchestrator run lands outside the industry folder, at `tasks/analysis-quality-review/<doc-slug>-<YYYYMMDD-HHMM>/` — it holds the per-iteration violation reports and the load-bearing index. Surface its path to the user at Gate 3 for traceability.

## Output location — standalone sub-skill invocation

When a sub-skill is run directly (not via orchestrator), it writes to:

```
08-knowledge/world-model/industries/[industry-slug]/standalone/[skill-name]-YYYY-MM-DD.md
```

Standalone outputs do not overwrite orchestrator-managed `working/` files.

## HTML deliverables and quality review

The rule of thumb: **if a human is expected to read it as a finished deliverable, it ships as HTML and goes through `analysis-quality-review`. If it is machine input, an append-only log, or audit substrate, it stays markdown/YAML.**

### Orchestrator (`analyze-industry`) — HTML by default

The reader-facing brief is always a self-contained HTML report (`industry-brief.html`), rendered via the `html-output` skill (`report` archetype) from the markdown draft in `working/`. The orchestrator runs the full quality flow:

1. **Ghost-deck** — `analysis-quality-review` `mode: spec` → fill template → `mode: spec-judge` loop, before drafting (step 6a).
2. **Render** — `html-output` turns `working/industry-brief-draft.md` into `industry-brief.html` (step 8).
3. **Review** — `analysis-quality-review` `mode: review pass: 1` (structure) then `pass: 2` (readability) against the HTML, looping until PASS (step 9).

Use `doc_type: brief`, `structural_framework: minto-pyramid`. Machine/audit artifacts — `industry-brief.yaml`, `signals-log.md`, `bar-test.md`, and everything in `working/` — stay markdown/YAML and are NOT reviewed.

### Sub-skills — markdown by default, HTML only on explicit request

A sub-skill's default output is markdown: the Python validator parses markdown structure, and the orchestrator consumes `working/[file].md` directly. **Do not render HTML automatically.**

If — and only if — the user explicitly asks for an HTML version of a standalone sub-skill run, then after the `validate_*.py` check passes:

1. Render the validated markdown as an HTML report via the `html-output` skill, saved alongside the markdown at `standalone/[skill-name]-YYYY-MM-DD.html`.
2. Run it through `analysis-quality-review` (`doc_type: brief`, `structural_framework: descriptive` — a single-lens analysis is diagnostic, not recommendation-driven), looping `review pass: 1` then `pass: 2` until PASS.

The markdown file is still produced and still the validator's and orchestrator's source of truth — the HTML is an additional reader-facing view, never a replacement.

## YAML frontmatter (every output)

```yaml
---
industry: [industry-slug]
sub_skill: [skill-name]               # or "orchestrator"
date: YYYY-MM-DD
mode: quick | deep
status: draft | bar-tested | approved
provenance_tags_complete: true | false
---
```

## Recall log (for orchestrator runs)

After Gate 3 approval, write a recall to:

```
14-memory/recalls/analyze-industry/YYYY-MM-DD-[industry-slug].md
```

With fields: industry, scope question, mode, key finding (one sentence), brief path, bar-test pass/fail, sub-skills run.

## Brief versioning

If an industry brief is re-run (industry refresh, scope change), the old brief is moved to `working/archive/industry-brief-YYYY-MM-DD.md` before the new one is written. Signals log is append-only across versions.

# Pyramid Principle + SCQA Synthesis Discipline

The orchestrator's final industry brief is structured using **Minto Pyramid Principle** for hierarchical recommendation and **SCQA** (Situation / Complication / Question / Answer) for narrative coherence. Sub-skill outputs are inputs, not deliverables — the orchestrator synthesizes them into a single brief that reads top-down.

## Pyramid Principle — structure of the brief

Every section follows the same hierarchy:

```
Main answer (one sentence — the governing observation)
├── Supporting reason 1
│   ├── Evidence
│   ├── Evidence
│   └── Evidence
├── Supporting reason 2
│   ├── Evidence
│   └── Evidence
└── Supporting reason 3
    └── ...
```

**Rules:**
- The main answer comes first, not last. Senior readers stop after the top of each section if it answers the question.
- Supporting reasons are **MECE** (mutually exclusive, collectively exhaustive). If two reasons can be merged, merge them.
- Each supporting reason is itself a complete sentence claim, not a label. Not "Profitability" but "Profit concentrates in distribution despite manufacturing capturing the most revenue."
- Evidence under each reason carries provenance tags per `_shared/provenance-tagging.md`.

## SCQA — narrative opening

The brief opens with a SCQA frame, not "Executive Summary":

- **Situation** (1-2 sentences) — what is currently true about this industry that the reader will agree with
- **Complication** (1-2 sentences) — what has changed or is at risk that disrupts the situation
- **Question** (1 sentence) — the strategic question this brief answers
- **Answer** (1 paragraph) — the governing observation and its top-line implication

SCQA is the contract that tells the reader why they should keep reading. Skip it = the brief reads as a dump.

## Worked example — SCQA opening for a fictional industrial robotics brief

> **Situation.** Industrial robotics is a $52B market growing at 12% CAGR [C: IFR 2025 + IBISWorld 2025], with four global incumbents (Fanuc, ABB, KUKA, Yaskawa) holding ~60% share [C: company filings + LEK 2024].
>
> **Complication.** Software-led entrants (Symbotic, Berkshire Grey, Veo Robotics) are unbundling the controller/perception layer from the hardware, eroding the OEM's profit pool in motion control [I: peer benchmark — software-attach margin at entrants 38% vs incumbents 12%].
>
> **Question.** For a sponsor evaluating a roll-up of mid-tier integrators, is industrial robotics structurally attractive over a 5-year hold?
>
> **Answer.** Attractive but only at the integrator layer, not the OEM layer. Profit is migrating away from hardware and into integration + software, where the industry remains fragmented (top-5 integrator share <15%) [C: LEK 2024]. Recommend a roll-up of regional integrators with a software-attach thesis; avoid the OEM layer where 7 Powers (scale economies + switching costs) protect incumbents from new entrants but not from value-chain disintermediation.

## Where SCQA goes in the orchestrator output

Top of the markdown synthesis draft (`working/industry-brief-draft.md`), immediately after the title and frontmatter — and carried through into the rendered `industry-brief.html`. Followed by sections drawn from sub-skill outputs, each itself structured Pyramid-style.

## Why this exists

Sub-skills produce diagnostic analysis. The orchestrator's job is to convert diagnosis into a recommendation a senior reader can act on. Pyramid + SCQA is the field-standard MBB discipline for that conversion. Adopted from prior-art (`gcamilo/management-consulting`) where it scored 7.8/10 vs 6.3 baseline on rubric testing.

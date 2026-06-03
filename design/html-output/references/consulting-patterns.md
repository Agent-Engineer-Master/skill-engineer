# Consulting slide patterns (McKinsey / BCG / Bain style)

The patterns that make a consulting deck feel like a consulting deck. Apply these to `slide-deck.html`.

## 1. Action titles — the most important rule

Every slide title is a complete sentence stating the **takeaway**, not the topic.

| Topic title (weak) | Action title (strong) |
|---|---|
| "Revenue by segment" | "Enterprise drives 78% of revenue but only 30% of growth" |
| "Competitive landscape" | "Three competitors control 60% of share; entry window closes Q4" |
| "Customer satisfaction" | "NPS gains are concentrated in onboarding — retention metrics are unchanged" |

Rule: if you stripped every chart and kept only the titles, the deck should still tell the story. Read the titles in order — they should form an argument.

## 2. Pyramid principle structure

Each slide answers ONE question. The slide title states the answer. The body provides 2–4 pieces of supporting evidence (MECE — mutually exclusive, collectively exhaustive). The bottom right has a "so what" box if the implication isn't obvious from the chart.

```
┌─────────────────────────────────────────────┐
│ ACTION TITLE — the takeaway as a sentence   │
├─────────────────────────────────────────────┤
│                                  ┌────────┐ │
│   [Main exhibit / chart]         │ So     │ │
│                                  │ what   │ │
│                                  │ box    │ │
│                                  └────────┘ │
├─────────────────────────────────────────────┤
│ Exhibit 3 of 8     Source: ...   Footnote.. │
└─────────────────────────────────────────────┘
```

## 3. Slide archetypes and when to use them

| Archetype | When | Visual element |
|-----------|------|---------------|
| **Cover** | Deck opening | Big title, subtitle, date, author |
| **Executive summary** | Slide 2 | 3–5 bullets, each = one downstream slide's action title |
| **Single chart** | Most slides | One exhibit + action title + so-what |
| **2×2 matrix** | Strategic positioning | Quadrant labels, dots positioned by attribute |
| **Marimekko** | Market share × segment size | Variable-width stacked bars |
| **Waterfall** | Decomposition (e.g. revenue bridge) | Sequential +/– bars |
| **Comparison table** | Option evaluation | Criteria × options, scored cells |
| **Three-column** | MECE breakdown ("there are three reasons…") | Equal columns with header → body → synthesis |
| **Process / timeline** | Sequencing | Numbered steps, arrow flow |
| **Synthesis** | Closing | Recommendation, next steps, decision required |

## 4. Visual rules

- **One typeface hierarchy:** Space Grotesk for titles + labels, Inter for body. No other fonts.
- **Three colors per slide max:** primary forest green, one accent (amber for highlight, slate for secondary data), one neutral.
- **No chartjunk:** Strip default Chart.js legends if the data is labelled inline. Kill gridlines on bar charts.
- **Label directly:** Put data labels on bars/lines, not in a separate legend.
- **Highlight the point:** The one bar / line / cell that proves the action title should be the accent color. Everything else is muted.
- **Footnote everything:** Sources, methodology, caveats go at the bottom in 9pt. Use superscript numbers in the chart, footnotes below.

## 5. Specific chart archetypes

### 2×2 matrix
- Two axes labelled with continuous variables ("Market growth ↑" and "Competitive intensity →")
- Quadrants labelled ("Invest", "Hold", "Harvest", "Exit")
- Items as labelled dots, sized by a third variable (revenue, headcount)

### Waterfall
- Start bar (e.g. "2024 revenue: $100M")
- Sequence of positive (green) and negative (red/amber) deltas
- End bar (e.g. "2025 revenue: $112M")
- Connecting dotted lines between bar tops

### Marimekko
- X-axis width = segment size (% of total market)
- Within each column, vertical bands = share by player
- Total area = revenue / volume / share

### Three-column MECE
- Header row: three categories that together cover the answer space
- Body rows: evidence under each
- Footer synthesis row spanning all three: "Therefore…"

## 6. Action title checklist

Before shipping a slide:
- [ ] Title is a complete sentence with a verb
- [ ] Title states a finding, not a topic
- [ ] The chart visually proves what the title claims (one element highlighted)
- [ ] Exhibit number + source + footnote present
- [ ] No more than 3 colors used
- [ ] No chartjunk (gridlines off, legends merged into labels)

## 7. The deck-level test

Read just the action titles, in order. Does the deck:
- Open with the answer (executive summary)?
- Build the argument MECE (no logical gaps, no overlaps)?
- Close with a recommendation and next steps?

If a title is "Background" or "Approach" or "Methodology" — that's a working-paper section, not a slide title. Put it in the appendix.

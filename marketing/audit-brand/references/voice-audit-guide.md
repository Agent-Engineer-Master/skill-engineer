# Voice Audit Guide

Reference for Module 2 of /audit-brand.

## Table of Contents
- [Voice Drift Detection](#voice-drift-detection)
- [AI Tell Detection](#ai-tell-detection)
- [Platform Voice Comparison](#platform-voice-comparison)
- [Voice Fix Templates](#voice-fix-templates)
- [Common Voice Decay Patterns](#common-voice-decay-patterns)

---

## Voice Drift Detection

Voice drift is when content gradually moves away from the defined voice guidelines. It's insidious because each individual piece seems fine — drift only becomes visible across multiple pieces.

### How to detect

1. Extract the 3-5 voice adjectives from guidelines
2. Read 5 recent pieces of content
3. For each piece, rate how strongly each adjective is present (1-5)
4. Look for patterns: which adjectives are consistently low?

### Drift types

| Type | What Happens | Detection Signal |
|------|-------------|-----------------|
| **Tonal drift** | Voice becomes more formal or casual than intended | Compare first post to most recent — noticeable tone shift? |
| **Vocabulary drift** | Banned words creep in, approved words fade out | Grep recent content for banned word list |
| **Energy drift** | Voice becomes more cautious/hedging over time | Count qualifying words ("maybe", "potentially", "somewhat") |
| **Personality fade** | Voice becomes generic, loses distinctive character | Could this content belong to any brand in the category? |
| **Platform bleed** | LinkedIn voice on X, or vice versa | Compare same-day posts across platforms — should feel different |

### Scoring voice adjective fidelity

For each defined voice adjective:

| Score | Criteria |
|-------|----------|
| 5 | Every piece of content unmistakably embodies this adjective |
| 4 | Most content embodies it; rare lapses |
| 3 | Sometimes present, sometimes not — inconsistent |
| 2 | Rarely present — content mostly doesn't feel this way |
| 1 | Never present — this adjective is aspirational, not actual |

---

## AI Tell Detection

Content created or edited with AI assistance often contains telltale patterns. These undermine brand voice because they make the brand sound like "AI" rather than a specific person/brand.

### High-confidence AI vocabulary (ban these)

| Word/Phrase | Why It's a Tell | Better Alternative |
|------------|----------------|-------------------|
| "Delve" | Almost never used in natural speech | "Dig into", "explore", "look at" |
| "Tapestry" | Overused AI metaphor | Remove or use specific metaphor |
| "Testament" | AI formalism | "Proof", "evidence", "shows" |
| "Nuanced" | AI favorite hedge | Be specific about what the nuance IS |
| "Landscape" (as metaphor) | AI overuses for "field/space" | "Space", "market", "world" |
| "Leverage" (as verb) | Corporate AI-speak | "Use", "apply", "build on" |
| "Navigate" (metaphorical) | AI loves navigation metaphors | "Handle", "deal with", "figure out" |
| "Realm" | AI overuses for "area" | "Area", "space", "field" |
| "Multifaceted" | AI complexity word | Describe the specific facets instead |
| "Pivotal" | AI drama word | "Important", "key", or just state why |
| "Seamless(ly)" | AI smoothness word | Describe what makes it smooth specifically |
| "Robust" | AI quality word | State what makes it strong specifically |
| "Ecosystem" | AI systems word (unless actually about ecosystems) | "System", "network", "stack" |
| "It's worth noting" | AI preamble | Just state the thing |
| "In today's [X]" | AI intro crutch | Cut entirely — start with the point |

### Structural AI tells

| Pattern | What It Looks Like | Fix |
|---------|-------------------|-----|
| **List-then-summary** | 3-5 points followed by "In summary..." | Cut the summary — reader just read the points |
| **Hedging chains** | "While X is important, it's worth noting that Y, and we should also consider Z..." | Take a position. "X matters because..." |
| **False balance** | "On one hand... on the other hand..." | Pick a side. The brand has a point of view. |
| **Throat-clearing** | First paragraph restates the topic before saying anything | Delete first paragraph. Start with the insight. |
| **Em-dash abuse** | Multiple em-dashes per paragraph | Use one per paragraph max. Prefer periods. |

---

## Platform Voice Comparison

The same brand voice should feel different across platforms while remaining recognizably the same person/brand.

### LinkedIn vs X comparison

| Dimension | LinkedIn | X |
|-----------|----------|---|
| **Length** | 150-300 words typical | 280 chars max per tweet |
| **Formality** | Slightly more professional | More casual, punchier |
| **Setup** | Brief context/story OK | Zero setup — lead with insight |
| **Qualification** | Some nuance acceptable | No hedging — takes a position |
| **CTA** | Explicit engagement ask OK | Implicit or none |
| **Hashtags** | 3-5 relevant | 0-2 (or none) |

### What should be the SAME across platforms

- Core personality (the "who")
- Domain expertise (the "what about")
- Point of view (the "stance")
- Banned words (never platform-dependent)

### What should DIFFER

- Length and density
- Formality level
- Setup and context
- CTA style

---

## Voice Fix Templates

When a voice violation is found, provide the original AND a rewritten version.

### Template

```
**Violation:** [which voice adjective or rule was violated]
**Original:** "[the actual sentence from content]"
**Issue:** [what's wrong and why]
**Rewrite:** "[the fixed version]"
```

### Example fixes

**Violation:** Banned word "delve"
**Original:** "Let's delve into why agentic commerce is reshaping DTC."
**Issue:** AI vocabulary — "delve" is a high-confidence AI tell
**Rewrite:** "Here's why agentic commerce is reshaping DTC."

**Violation:** Throat-clearing (voice adjective: "direct" not met)
**Original:** "In today's rapidly evolving DTC landscape, it's worth noting that AI agents are fundamentally changing how consumers discover and purchase products."
**Issue:** 3 AI tells in one sentence (landscape, worth noting, in today's). Also hedging instead of claiming.
**Rewrite:** "AI agents are changing how people buy things. Here's what that means for DTC brands."

**Violation:** Platform bleed (LinkedIn tone on X)
**Original tweet:** "I've been thinking about the implications of agentic commerce for DTC operators, and here are three observations that I believe are worth sharing with this community."
**Issue:** 40 words of setup for what should be a punch. LinkedIn voice on X.
**Rewrite tweet:** "Three things agentic commerce is about to do to DTC:"

---

## Common Voice Decay Patterns

| Pattern | Symptom | Root Cause | Fix |
|---------|---------|-----------|-----|
| **AI contamination** | Content sounds increasingly generic/polished | Over-reliance on AI drafting without human voice editing | Run /humanizer on all AI-drafted content; strengthen banned word list |
| **Formality creep** | Voice becomes stiff, corporate-sounding | New audience anxiety ("what if serious people are reading?") | Reread earliest posts for original energy; voice adjectives don't change with audience size |
| **Expertise signaling** | Content becomes lecturing/condescending | Success in the domain → unconscious shift to "teacher" mode | Add "accessible" or "conversational" to voice adjectives; ban "you should" |
| **Controversy avoidance** | Content becomes bland, avoids taking positions | Fear of backlash or unsubscribes | The brand has a point of view. Bland = invisible. Revisit "stands for / stands against" |
| **Copycat drift** | Voice starts mimicking a successful peer | Unconscious imitation of what seems to work | Return to own voice guidelines. What makes THIS voice distinctive? |

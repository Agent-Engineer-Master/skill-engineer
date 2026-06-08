# Tone of Voice — Analytical Report Register

The positive target for reader-facing analytical deliverables (briefs, memos, decks, decision records, descriptive reports). `fix-patterns.md` says what to *strip*; this file says what to *aim at*. The readability rubric (Pass 2, dimensions D8 and D9) grades prose against this file.

**Scope boundary — read first.** This register governs analytical deliverables only. It is **not** the personal-brand voice (`content` skill, `voice-personal.md`) and **not** the True Norma store voice. Those are punchier, more conversational, and tuned for a feed. A strategy report should never inherit them, and personal-brand copy should never inherit this. If a skill is producing a LinkedIn post or a product description, it does not read this file.

---

## The register in one paragraph

Write like an intelligent person explaining something they understand deeply to a peer who is sharp but not in the weeds. Conversational, but educated. Formal enough to be taken seriously, never so formal it sounds like a contract or a McKinsey deck. The reader should feel they are being *let in on the reasoning*, not made to decode it. The target sits between two failure modes: academic density on one side (every clause doing analytical work, nothing skimmable) and consumer-app plainness on the other (so simple it loses the nuance a sophisticated reader came for). Aim for the middle — clear, energetic, substantial.

This is calibrated to the midpoint Brigitte Small described: "conversational language that feels educated, a bit formalised but not stuffy." Monzo's public tone-of-voice guide is the closest published reference, but Monzo is a consumer bank writing to retail customers — for B2B strategic analysis we keep more intellectual weight than Monzo would, while borrowing its discipline on plain words and active voice.

---

## The five rules

### 1. One claim per sentence (concept density — graded by D8)

The single most common failure in our reports: too much reasoning laid bare in the conclusion. A sentence that stacks the headline number, two citations, a ranking claim, and two separate mechanisms forces the reader to fully decode the argument before they can grasp the point. There is no skim layer.

**Rule:** each sentence advances one idea. When a sentence carries a finding *and* its mechanism *and* its evidence, split it. Put the claim first, in its own short sentence. Give each supporting mechanism its own sentence. Move evidence to footnotes (see rule 2).

**Worked example.** This is one real sentence from a property-market report:

> Commercial valuation firms (Savills, CBRE, JLL, Knight Frank) capture approximately £79M EBIT at 13–17% margins [C: Savills Annual Report 2024; CBRE UK segment 2024] — the largest single profit pool — protected by switching costs (institutional clients face 6–18 months of onboarding friction to switch valuer [I: estimated from framework agreement structures]) and a regulatory cornered resource (RICS Red Book methodology + MRICS credential, legally required for lender-accepted valuations).

Roughly five concepts and two evidence tags in one breath. Rewritten:

> **Commercial valuation is the market's largest profit pool.** Four firms — Savills, CBRE, JLL and Knight Frank — earn about £79M EBIT on it, at margins of 13–17%.¹
>
> Two things protect that pool. Switching is slow: an institutional client needs six to eighteen months to onboard a new valuer.² And regulation gates the work — only an MRICS-credentialled valuer using the RICS Red Book can sign a valuation a lender will accept.³

Same information. The claim leads. Each mechanism gets its own sentence. Evidence drops to footnotes. The result reads at three depths (see rule 5).

### 2. Evidence belongs in footnotes, not mid-sentence (graded by D8)

Inline evidence tags — `[C: ...]`, `[I: ...]`, `[V: ...]`, `[A: ...]` — are load-bearing (they chain to source datasets) but they shatter reading rhythm when they sit inside a sentence. Move them to numbered footnotes or endnotes. The claim stays clean and skimmable in the body; the citation survives, intact, at the bottom.

This is a *rendering* move, not a deletion. The evidence chain must remain whole — never strip a tag, only relocate it. In HTML, render as a superscript footnote ref. In markdown, a `[^n]` footnote. Preserve the tag's full content (`[C: Savills Annual Report 2024]`) in the footnote body. See `fix-patterns.md` D5/D8 and the load-bearing protocol — relocate as a unit, never local-edit.

### 3. Active voice (graded by D5)

Active voice gives prose energy and feels modern — it reads like a person thinking, not a process being described. It is also more honest: it names who does what. "We recommend a pilot" beats "a pilot is recommended." "The data shows X" beats "it was found that X." Passive is acceptable only where the actor genuinely doesn't matter (describing a measurement process) — and even there, prefer active if you can name the actor without strain.

### 4. Anglo-Saxon backbone, Latinate for nuance (register — graded by D9)

Default to the plain, short, Anglo-Saxon word. *Use*, not *utilise*. *Buy*, not *procure*. *Start*, not *commence*. *Show*, not *demonstrate*. These are the words we actually say out loud; written down they read warm and direct rather than cold and distant.

But this is **not** a blanket "always use the simple word" rule — that is where Monzo goes too far for our audience. Reach for the Latinate or technical word **when its nuance genuinely refines the point**. *Institutional* client says something *big* client does not. *Credentialled* carries the regulatory weight that *qualified* misses. *Marginal* cost means something precise that *extra* cost does not. The test: does the longer word add a distinction the reader needs, or is it there to sound clever? If it adds a distinction, keep it. If it is decoration, cut it.

The same applies to jargon and professional terms. Use them **where they add clarity for this reader** — a domain term that names a real thing precisely is a gift, not a sin. Strip jargon only when it obscures rather than sharpens, or when the reader won't know it (see rule below on acronyms).

**Calibration — where the midpoint keeps a word Monzo would cut.** "Incumbent" is not stuffy decoration; it names the existing market-holder with a precision that "the old model" or "established players" loses. Keep it. Same for "marginal," "institutional," "counterparty," "underwrite." The midpoint is *not* "always pick the plainer word" — it is "pick the plainer word unless the harder one carries a distinction the reader needs." When Monzo flattens these, that is Monzo writing for retail consumers, not for a strategic reader. Don't follow it there.

**Cut empty qualifiers (the Anglo-Saxon flip-side).** The same decoration test applies to plain words. "Structurally accessible" → "accessible" — the modifier added nothing. Drop adverbs and modifiers that don't sharpen the claim: "fundamentally," "essentially," "structurally," "effectively," "broadly." If removing the word changes no meaning, remove it.

**Word-swap reference** (default → keep the right column only when nuance demands):

| Stuffy / Latinate default | Plain Anglo-Saxon | Keep the formal word when… |
|---|---|---|
| utilise / leverage (verb) | use, draw on | — (almost never) |
| commence | start, begin | — |
| terminate | end, stop | "terminate a contract" (legal precision) |
| endeavour | try | — |
| facilitate | help, ease | — |
| ascertain | find out, check | — |
| procure | buy, get | "procurement" as a named function |
| in order to | to | — |
| prior to / subsequent to | before / after | — |
| in the event that | if | — |
| a number of | several, some, or the actual count | — |
| the majority of | most | "majority stake" (ownership precision) |
| aforementioned | this, that, the | — |

### 5. Write for three depths (multi-depth reading — supports D8)

A good report rewards a skim *and* a deep read. Structure every report so three layers exist:

1. **Skim layer** — section action titles + the first sentence of each paragraph. A reader who reads only this should get the whole argument. (This is why rule 1 matters: if the claim leads each sentence, the skim layer is automatically coherent.)
2. **Argument layer** — the full paragraphs: claims plus their mechanisms and reasoning.
3. **Evidence layer** — footnotes, citations, appendices. There for the reader who wants to check the work; out of the way for the reader who doesn't.

The single dense sentence fails because it collapses all three layers into one — you cannot skim it, and the evidence is jammed into the argument. Unstacking the sentence (rule 1) and footnoting the evidence (rule 2) reconstructs the three layers.

---

## Section headers: claims with narrative tension (high strictness — extends D1)

Headers are already required to be action titles — claims, not noun labels ("Market is consolidating around three players," not "Market"). At high strictness, push one step further: a header may carry **narrative tension** to pull the reader forward. "Three firms own the profit pool — and one regulation keeps it that way" earns its drama from the analysis.

**Guardrail.** Tension, not melodrama. The header must still state a real claim the section proves. Clickbait that the body doesn't deliver ("You won't believe which firm is exposed") undercuts analytical credibility and fails D1. Drama is allowed *because* the finding is genuinely dramatic — never as a substitute for one.

---

## Frameworks stay backstage (extends D5)

The analytical frameworks that shaped the report — SCQA, MECE, JTBD, Rumelt's kernel, 7-Powers / Helmer, "governing observation" — do their work in the *structure*. They must not show their face in the reader-facing text. No heading reads "Situation" / "Complication" or "Governing force"; no sentence says "using 7-Powers we find…" or "the JTBD here is…". The framework is scaffolding. The reader sees the building, never the scaffolding.

**The move:** replace the framework label with the insight it produced. "The governing force explains why…" → "Why 78% of homebuyers get nothing." "JTBD: homebuyer regret avoidance" → the buyer's actual want: "Tell me what's wrong with this house before I commit." (See the next technique.)

## Say it in the reader's own words (technique)

The fastest way out of jargon is to write the concept as the person you're describing would actually say it. A "job to be done" stated in the customer's voice lands harder and reads cleaner than the abstraction. "Homebuyer regret-avoidance need" is a label; "Tell me what's wrong with this house before I commit" is the same idea the reader can feel. Lead with the human voice or the concrete number, not the construct that generated it.

## Acronyms and unfamiliar terms (extends D5)

Spell out an acronym on first use, with the acronym in parentheses: "Royal Institution of Chartered Surveyors (RICS)." After that, use the acronym freely. The exception is acronyms so universal to the reader that expansion would be patronising (e.g. *CEO*, *GDP*, *API* for a technical reader) — judge by `intent_summary`. When in doubt, expand once; it costs four words and removes all doubt.

---

## What "not stuffy" sounds like in practice

- It is fine to start a sentence with *But*, *And*, *So*, or *Because*. We do it when we talk; it reads natural on the page.
- Contractions are fine in a memo or brief ("doesn't," "won't"). They warm the prose. Use sparingly in a formal decision record.
- Short sentences are allowed to be very short. "Switching is slow." is a complete, strong sentence.
- Read it aloud. If you would never say it to the reader's face, rewrite it.

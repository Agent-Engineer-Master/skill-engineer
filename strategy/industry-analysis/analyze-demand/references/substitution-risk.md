# Substitution Risk — Named Candidates, Switching Cost, Likelihood

## Heading-naming rule (READ FIRST)

The substitution analysis section in the `demand.md` output MUST use the exact heading `## Substitution Risk` (level-2 markdown heading, verbatim wording).

Downstream consumers — the Five Forces "Threat of Substitutes" reconciliation, the analyze-trajectory cross-category-substitute scan, and the orchestrator gate-checks — parse this section by exact heading match. Variants like `## Threat from Adjacent Categories`, `## Substitutes`, `## Cross-Category Risk`, or `### Substitution` all break the downstream parse and fail validation with: "Missing `## Substitution Risk` section. The validator requires the exact heading 'Substitution Risk' for downstream consumer consistency. Rename your section."

This rule overrides any house-style heading preference. If the drafter prefers a more descriptive title, put it in the body line under the heading, not in the heading itself.

## Why "Threat of Substitutes" in Five Forces is usually under-specified

The classical Porter "threat of substitutes" force is typically scored as a single Low/Moderate/High rating with one or two examples. That treatment misses the structural-disruption case, which is almost always **cross-category** — a substitute appearing from outside the SIC code, attached to the same JOB.

This analysis exists to do that job properly. For each segment, name the substitutes, quantify switching cost, and state likelihood with a trigger event.

## Categories of substitute

For each segment, scan all four categories:

### 1. In-category competitors
Other firms doing the same thing. Usually already covered in Five Forces rivalry. List only if substitution dynamics differ from rivalry dynamics (e.g., a low-end disruptor inside the category attacking up-market).

### 2. Cross-category substitutes (THE PRIORITY)
Solutions from another SIC code attached to the same JOB. Modern examples:

| JOB | Incumbent category | Cross-category substitute | Year of visible substitution |
|-----|--------------------|-----------------------------|-----------------------------|
| "Meet a colleague in another city" | Business travel | Zoom / video conferencing | 2020-2023 partial |
| "Find lodging on a trip" | Hotels | Airbnb / short-term rental | 2015 onward, strongest mid-range |
| "Manage weight + appetite" | Snack food, diet programs, bariatric surgery | GLP-1 drugs (Ozempic, Wegovy) | 2023-2025 |
| "Answer a question quickly" | Google search, Stack Overflow, entry-level analyst | ChatGPT and successors | 2023-2026 |
| "Write production code for a known pattern" | Offshore dev labor, in-house junior eng | AI coding assistants (Copilot, Claude Code) | 2024-2026 |
| "Get a quick caloric breakfast on commute" | Bagel shop, donut shop, fast-food | Milkshake (Christensen's original) | continuous |
| "Track personal cardio metrics" | Medical equipment, gym tests | Apple Watch / Whoop / Garmin | 2015 onward |
| "Listen to recorded music" | CDs, MP3 downloads | Streaming | 2008 onward |

The pattern is consistent: the substitute is attached to the JOB, not the product category. If you are listing only within-category competitors, you have missed the structural threat.

### 3. DIY / in-house build
Particularly in B2B software, "build it ourselves" is a substitute that becomes more attractive as commoditization or AI-assist lowers the cost of internal build. Often under-rated. Trigger event: a credible internal AI-assist platform makes the in-house build path cheaper than the buy path.

### 4. Do-nothing
The most common substitute and the most often omitted. "The buyer continues to live with the problem because no available solution is worth the switching cost." Critical for nascent markets where the question is not "us vs them" but "us vs status quo."

Always state do-nothing explicitly even when the conclusion is "low risk — pain is acute enough that do-nothing is not viable for >X% of segment."

## Switching cost — the four dimensions

For each named substitute, decompose switching cost across:

1. **Financial** — contract penalties, sunk infrastructure, parallel-run cost
2. **Workflow** — process change, integration rework, retraining cycles
3. **Skill** — internal team capability gaps, certification requirements, hiring delays
4. **Psychological** — career risk of being the person who switched, change fatigue, vendor relationship loss

A switching cost of "high" with no decomposition is non-informative. The decomposition reveals where intervention or trigger events would unblock substitution. (Often workflow and psychological dominate financial.)

## Likelihood — anchored, not guessed

State likelihood on a 3-year horizon as Low / Moderate / High, anchored by:

- Adoption curve evidence (early-adopter share already migrated)
- Capability gap remaining (does the substitute actually do the job today, or only adjacent jobs)
- Triggering events that would accelerate (regulation, pricing change, capability release, recession)
- Reference cases from analogous industries

Always state the **trigger event that would re-rate the likelihood up** — e.g., "Low today; would re-rate to High if [a comparable workflow product] launches an AI-native equivalent priced 5x below incumbent."

## Failure modes

- **"General competition"** — not a substitute. Name candidates.
- **Only listing direct competitors** — that is rivalry, not substitution. Cross-category is the point.
- **Switching cost stated as "high" with no decomposition** — non-informative.
- **Likelihood stated without horizon** — "high" over what timeframe? Always anchor to 3 years (or state the horizon explicitly).
- **Missing do-nothing** — the most-overlooked substitute.

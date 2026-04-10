# Prompt — Digest — Sectors

## Role
You are an expert financial analyst. Your task is to synthesize sector and industry news from the Sectors Digest into actionable TAILWIND candidates.

## Step 1: Gather Context

### Required Context
Read the following before doing anything else:

*   `GEMINI.md` — The foundational Analysis Philosophy & Guidelines. This is the primary lens through which all analysis must be filtered.
*   `context_sectors.md` — Sector context, structural dynamics, and companies of interest. Read to understand the current state of each sector before analyzing today's digest.
*   `Peter's Digest/Sectors Digest/Sectors_Digest_{DATE}.md` — Your raw material. Read it in full; ensure no data point is skipped or overlooked.

**STOP. Do not proceed until all files have been read.**

---

## Step 2: Analyze & Identify Candidates

### Analysis Guidelines
*   Apply the `GEMINI.md` Analysis Philosophy to all analysis — it is the primary lens for candidate selection and framing.
*   Categorize AI developments using the sector framework and overarching context in `context_sectors.md`.
*   Maintain healthy skepticism — note the prevailing market narrative, but highlight claims that should be empirically validated or may be disputed before being accepted as fact. Market narratives often rationalize price movements after the fact.
*   This prompt does not perform LOSER analysis. Focus exclusively on structural multi-year signals that support a `[TAILWIND]` thesis per `GEMINI.md`.

---

## Step 3: Research & Verify Public Status

For any company identified in Step 2 as a candidate, you must verify its public trading status and ticker.

**Action:** Use the FMP Name Search API (`search-name`) via `run_shell_command` to verify the company.
*   **Command:** `curl -s "https://financialmodelingprep.com/stable/search-name?query=[COMPANY_NAME]&apikey=[FMP_API_KEY]"`
*   Identify the correct ticker and exchange (prefer major US exchanges: NYSE, NASDAQ).
*   If the company is private or the status is unclear, flag it as "Public status unconfirmed."

---

## Step 4: Generate Report

### Writing Guidelines
*   **Source Fidelity:** All insights must be sourced directly from the digest. Explicitly cite sources using the format `(Source: [Headline/Outlet])`. Do not introduce outside opinions or judgments.
*   **Context Fidelity:** Capture the full context, logic, and figures behind each item. Do not summarize — a "$6B market cap loss" must not become "significant losses."
*   **Synthesize, Don't Copy-Paste:** Quoting a source is acceptable for key phrases, but do not reproduce entire paragraphs verbatim. Extract the thesis, the evidence, and the implications.

### Deliverable

**Questions:**
1.  **Source Check:** Has every item been sourced directly from the digest — no outside data or opinions introduced?
2.  **Context Check:** Has the full context been preserved — no figures, narratives, or causal links compressed or summarized away?
3.  **Philosophy Check:** Do the signals genuinely reflect the `[TAILWIND]` framework in `GEMINI.md` — structural improvement, external catalyst, not yet fully priced in?
4.  **Sector Check:** Have developments been analyzed through the relevant sector context and dynamics in `context_sectors.md`?
5.  **Coverage Check:** Have all tickers/companies that plausibly fit a `[TAILWIND]` thesis per `GEMINI.md` been included?
6.  **Reflexivity Check:** Have reflexive dynamics or circular revenue patterns (per the AI Overarching Context in `context_sectors.md`) been flagged where evident?
7.  **Ticker Verification:** Have you used the FMP `search-name` API to confirm the public status and ticker for candidates?

**Output Format:**

## Sectors Analysis

### 1. Sectors
[Include ALL sectors listed below. For each relevant development, provide the signal analysis. If no news exists for a sector, state "No news today."]

#### AI — Compute & Chips
[For each relevant development:]
*   **Signal:** [What the digest says and why it may matter, tied to the `[TAILWIND]` framework in `GEMINI.md`. Include all figures and context. Include tickers/companies mentioned.]
*   **Risks:** [Apply the two TAILWIND hazards from `GEMINI.md`: (1) is the thesis likely correct, or could the forecast simply be wrong? (2) is the improvement already priced in? Flag either if unclear.]
*   **Tickers/Companies mentioned:** [all tickers/companies cited in this context. Use verified tickers where found in Step 3.]
*   **Source:** [Exact headline and outlet, formatted for CTRL+F]
[If no news: "No news today."]

#### AI — Networking & Optical
[Same format as above or "No news today."]

#### AI — Infrastructure & Power
[Same format as above or "No news today."]

#### AI — Nuclear & Energy
[Same format as above or "No news today."]

#### AI — Software & Disruption
[Same format as above or "No news today."]

#### Critical Minerals & Rare Earths
[Same format as above or "No news today."]

#### Defense & Aerospace
[Same format as above or "No news today."]

### 2. Stocks: Tailwinds
[All tickers/companies appearing in a positive or momentum context in the digest that plausibly fit a `[TAILWIND]` thesis per `GEMINI.md`. For each:]
*   **Signal:** [What the digest says and why it may matter, tied to the `[TAILWIND]` framework in `GEMINI.md`. Include all figures and context from the digest.]
*   **Risks:** [Apply the two TAILWIND hazards from `GEMINI.md`: (1) is the thesis likely correct, or could the forecast simply be wrong? (2) is the improvement already priced in? Flag either if unclear.]
*   **Tickers/Companies mentioned:** [all tickers/companies cited in this context. Use verified tickers where found in Step 3.]
*   **Source:** [Exact headline and outlet, formatted for CTRL+F]

---

**Action:** Ask: "Do you approve this analysis? Should I prepend this analysis to the Sectors Digest file?"

**STOP. Wait for user approval before proceeding to Step 5.**

---

## Step 5: Commit Analysis

Upon explicit user approval (e.g., "yes", "go ahead"), prepend the full analysis report (from the "Sectors Analysis" header onwards) to the top of `Peter's Digest/Sectors Digest/Sectors_Digest_{DATE}.md`, immediately below the main "Peter's Digest: Sectors" header.

**STOP. Wait for user approval before committing.**

---

## Step 6: Propose Context Update

Re-read `context_sectors.md`. For each sector that had developments in today's digest, assess whether an update to the context file is warranted. Apply the following principles:

*   **Do not force updates.** The context file captures structural, medium-term perspectives. The bar for an update is: "Does this represent a meaningful development, or is it daily noise?"
*   **Recent Signals & Developments** is the appropriate field for new additions. Add an entry when a development represents a genuine signal — a new contract, a policy shift, a technology milestone, or a significant headline worth tracking. Do not add routine price moves or minor one-off mentions.
*   **Context and Risks sections** are relatively evergreen. Update them only if a fundamental dynamic has materially shifted — a new technology, a confirmed structural break, a significant policy change.
*   **Companies of Interest** may be added when a company appears in a context that warrants further investigation — a major contract, structural relevance to a sector thesis, or a significant development. Significance is the test, not frequency of mention.
*   **If nothing warrants an update, state "No context updates warranted today."** This is the expected outcome on many days.

For each proposed change, briefly state why it clears the bar for a meaningful update.

**Action:** Ask: "Do you approve these context updates? Should I apply them to context_sectors.md?"

**STOP. Wait for user approval before proceeding to Step 7.**

---

## Step 7: Commit Context Update

Upon explicit user approval, apply the approved updates to `context_sectors.md` — updating sections in place — and update the `*Last updated*` date at the top of the file.

**STOP. Wait for user approval before committing.**

---

### Appendix: Keyword Filter (Internal Use Only)
Keep these keywords in mind when identifying relevant signals (do not output this list):
*   **AI — Compute & Chips:** GPU rental, H100, Blackwell, Vera Rubin, Groq, inference, inference inflection, agentic AI, ASML, DUV, MATCH Act, export controls, DRAM, NAND, HBM, HBM3, DDR4, DDR5, memory constraints, TurboQuant, Jevons Paradox, custom silicon, TPU, Trainium, depreciation risk, foundry leverage, capacity overbuild, customer defection, China chip scaling, spot pricing, co-packaged optics, supplier lock-in, contract minimums.
*   **AI — Networking & Optical:** 800G, 1.6T, transceivers, optical interconnects, co-packaged optics, copper interconnect debate, EML lasers, optical circuit switches, hyperscaler interconnect, backplane, fiber.
*   **AI — Infrastructure & Power:** data center construction, co-located power, liquid cooling, liquid-cooled AI factory, immersion cooling, direct-to-chip, rear-door heat exchanger, warm-water cooling, grid strain, moratorium, 20 megawatt, neocloud, gigawatt campus, execution risk, redesign risk, cascading delays, demand shock, data center REIT, hyperscaler CapEx, crowding out, human logistics constraint, construction housing.
*   **AI — Nuclear & Energy:** nuclear renaissance, SMR, uranium, reactor components, AI power demand, positive estimate revisions, criticality, reactor pilot, OTA, Other Transaction Authority, Reactor Pilot Program, mine-to-megawatt, molten salt, AP1000, NRC design certification, capacity factor.
*   **AI — Software & Disruption:** AI displacement, seat reduction, enterprise AI adoption, software pricing pressure, low switching costs, moat durability, vibe-coding, debt refinancing risk, orchestration, agent framework, data services, revenue test, network effects, embedded workflows, Claude, Codex, OpenAI, Anthropic, Gemini, Copilot, ChatGPT, foundation model, frontier model.
*   **Critical Minerals & Rare Earths:** rare earth, NdPr, neodymium-praseodymium, NdFeB magnets, dysprosium, terbium, gallium, beryllium, niobium, scandium, heavy rare earths, light rare earths, rare earth separation, Chinese rare earth processing, domestic supply chain, CHIPS Act, DoD funding, mine-to-magnet, onshoring, critical minerals, Project Vault, Western supply chain, vertically integrated, strategic reserve.
*   **Defense & Aerospace:** autonomous warfare, drone autonomy, hypersonic, hypersonic test flights, space infrastructure, satellite-to-cellular, defense contracts, SMR for defense, dual-use, Neutron rocket, Space Development Agency, eVTOL, edge AI, geospatial intelligence.

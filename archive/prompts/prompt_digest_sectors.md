# Prompt — Digest — Sectors

## Role
You are an expert analyst. Your task is to read the Sectors Digest and record structural developments across key sectors — capturing the signals, figures, and companies that inform `context_sectors.md`.

## Step 1: Gather Context

### Required Context
Read the following before doing anything else:

*   `GEMINI.md` — The foundational Analysis Philosophy & Guidelines.
*   `context_sectors.md` — Sector context, structural dynamics, and companies of interest. Read to understand the current state of each sector before analyzing today's digest.
*   `Peter's Digest/Sectors Digest/Sectors_Digest_{DATE}.md` — Your raw material. Read it in full; ensure no data point is skipped or overlooked.

**STOP. Do not proceed until all files have been read.**

---

## Step 2: Analyze & Synthesize

### Analysis Guidelines
*   Focus on structural, multi-year developments. Filter out routine announcements, single-datapoint snapshots, and daily price moves.
*   Do not weight narratives by volume of headlines. A single brief item from one source may be more significant than five mainstream headlines if the underlying signal is large.
*   Categorize AI developments using the sector framework and overarching context in `context_sectors.md`. When a development is ambiguous across sectors, assign it to the sector that best matches the company's primary business activity. Use the following as guiding examples: a space company pursuing orbital compute belongs in **Defense & Aerospace**, not AI — Software & Disruption; an energy company building nuclear capacity for data centers belongs in **AI — Nuclear & Energy**, not AI — Power & Grid; a story about data center construction or REITs belongs in **AI — Data Centers & Cloud**, not AI — Power & Grid; a story about grid strain or utility-scale power delivery belongs in **AI — Power & Grid**, not AI — Data Centers & Cloud.
*   Maintain healthy skepticism — note the prevailing market narrative, but highlight claims that should be empirically validated or may be disputed before being accepted as fact.
*   Flag reflexive dynamics or circular revenue patterns (per the AI Overarching Context in `context_sectors.md`) where evident.

---

## Step 3: Research & Verify Public Status

For any company identified in Step 2, verify its public trading status and ticker for reference.

**Action:** Use the FMP Name Search API (`search-name`) via `run_shell_command` to verify the company.
*   **Command:** `curl -s "https://financialmodelingprep.com/stable/search-name?query=[COMPANY_NAME]&apikey=[FMP_API_KEY]"`
*   Identify the correct ticker and exchange (prefer major US exchanges: NYSE, NASDAQ).
*   If the company is private or the status is unclear, flag it as "Public status unconfirmed."

---

## Step 4: Generate Report

### Writing Guidelines
*   **Source Fidelity:** All insights must be sourced directly from the digest. Explicitly cite sources using the format `(Source: [Headline/Outlet])`. Do not introduce outside opinions or judgments.
*   **Context Fidelity:** Capture the full context, logic, and figures behind each item. Do not summarize — a "$6B market cap loss" must not become "significant losses." For technical articles, include the full technical argument: if an article defines a technology hierarchy or architecture, list it; if it explains the causal logic behind a market shift, reproduce that logic; if it contains specific figures (deal sizes, percentages, voltages, capacity numbers), include them. A condensed sentence is not a substitute for an article whose analytical value lies in its technical specificity.
*   **Synthesize, Don't Copy-Paste:** Quoting a source is acceptable for key phrases, but do not reproduce entire paragraphs verbatim. Extract the thesis, the evidence, and the implications.

### Deliverable

**Questions:**
1.  **Source Check:** Has every item been sourced directly from the digest — no outside data or opinions introduced?
2.  **Context Check:** Has the full context been preserved — no figures, narratives, or causal links compressed or summarized away?
3.  **Coverage Check:** Have all structurally significant developments been captured? Have they been weighted by signal significance, not by volume or length of coverage?
4.  **Sector Check:** Have developments been analyzed through the relevant sector context and dynamics in `context_sectors.md`?
5.  **Structural Filter Check:** Does each entry represent a structural, multi-year development rather than daily noise?
6.  **Reflexivity Check:** Have reflexive dynamics or circular revenue patterns (per the AI Overarching Context in `context_sectors.md`) been flagged where evident?
7.  **Ticker Verification:** Have you used the FMP `search-name` API to confirm the public status and ticker for all companies?

**Output Format:**

## Sectors Analysis

### 1. Sectors
[Include ALL sectors listed below. For each relevant development, provide the analysis. If no news exists for a sector, state "No news today."]

#### AI — Compute & Chips
[For each relevant development:]
*   **Analysis:** [What the digest says, why it matters structurally, the full causal logic and figures, and which companies are involved. Apply skepticism where claims should be validated.]
*   **Tickers/Companies mentioned:** [All tickers/companies cited in this context. Use verified tickers where found in Step 3.]
*   **Source:** [Exact headline and outlet, formatted for CTRL+F]
[If no news: "No news today."]

#### AI — Networking & Optical
[Same format as above or "No news today."]

#### AI — Data Centers & Cloud
[Same format as above or "No news today."]

#### AI — Power & Grid
[Same format as above or "No news today."]

#### AI — Nuclear & Energy
[Same format as above or "No news today."]

#### AI — Software & Disruption
[Same format as above or "No news today."]

#### Critical Minerals & Rare Earths
[Same format as above or "No news today."]

#### Defense & Aerospace
[Same format as above or "No news today."]

### 2. Public Companies Referenced
[Consolidated quick-reference list of all publicly traded companies mentioned across today's analysis. For each:]
*   **[Company] ([TICKER], [Exchange])** — [one-line context: what they did or why they were mentioned today]

### 3. Screening Candidates
[From the companies above, flag those with a specific, notable development today — a major contract, a structural catalyst, a technology milestone, a significant competitive shift. Omit companies that were merely mentioned in passing. For each:]
*   **[TICKER]** — [one-line reason it warrants screening]

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

*   **Do not force updates.** The context file captures structural, medium-term perspectives. Before proposing any update, apply the following self-check:
    1.  **Does it add value?** Does it introduce genuinely new information, or meaningfully deepen existing context with updated data, figures, or developments? A new concept clearly passes. An existing concept can also warrant an update if new data materially anchors or extends it — a major deal figure, a policy milestone, a confirmed structural break. What does not pass: restating an existing concept in different words, or adding a snapshot statistic from a single report that doesn't change the underlying picture.
    2.  **Is it structural?** Is this a multi-month/multi-year trend backed by multiple data points, or a single-day observation? A snapshot statistic from one article is not a structural shift.
    3.  **Is it evergreen?** Would this context still be meaningful and accurate 3–6 months from now? If not, it belongs in the digest analysis, not the context file.
    4.  **Does it clear the section bar?** (See section-specific rules below.)
*   **Recent Signals & Developments** is the appropriate field for new additions. Add an entry when a development represents a genuine signal — a new contract, a policy shift, a technology milestone, or a significant headline worth tracking. Do not add routine price moves or minor one-off mentions.
*   **Context and Risks sections** are relatively evergreen. Update them only if a fundamental dynamic has materially shifted — a new technology, a confirmed structural break, a significant policy change.
*   **Companies of Interest** may be added when a company appears in a context that warrants further investigation — a major contract, structural relevance to a sector thesis, or a significant development. Significance is the test, not frequency of mention.
*   **If nothing warrants an update, state "No context updates warranted today."** This is the expected outcome on many days.

**Proposal format:** For each proposed update, provide:
*   **Proposed change:** What you are adding and where.
*   **Structural value:** Why it clears the evergreen bar — specifically, whether it is genuinely new context vs. already covered, and why it is structural vs. daily noise.
*   **What you are NOT proposing, and why:** For any developments in the digest you considered but filtered out, briefly note the reason (e.g., "single-day datapoint," "already covered under X"). This shows the filtering process, not just the accepted items.

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
*   **AI — Networking & Optical:** 800G, 1.6T, transceivers, optical interconnects, co-packaged optics, copper interconnect debate, EML lasers, optical circuit switches, hyperscaler interconnect, backplane, fiber, dark fiber, wavelength.
*   **AI — Data Centers & Cloud:** data center construction, co-location, hyperscaler CapEx, liquid cooling, liquid-cooled AI factory, immersion cooling, direct-to-chip, rear-door heat exchanger, warm-water cooling, neocloud, gigawatt campus, execution risk, redesign risk, cascading delays, demand shock, data center REIT, crowding out, human logistics constraint, construction housing, campus development, data center moratorium.
*   **AI — Power & Grid:** grid strain, co-located power, power purchase agreement, PPA, utility-scale power, transmission, load growth, interconnection queue, behind-the-meter, grid interconnection, power delivery, stranded power, curtailment, baseload.
*   **AI — Nuclear & Energy:** nuclear renaissance, SMR, uranium, reactor components, AI power demand, positive estimate revisions, criticality, reactor pilot, OTA, Other Transaction Authority, Reactor Pilot Program, mine-to-megawatt, molten salt, AP1000, NRC design certification, capacity factor.
*   **AI — Software & Disruption:** AI displacement, seat reduction, enterprise AI adoption, software pricing pressure, low switching costs, moat durability, vibe-coding, debt refinancing risk, orchestration, agent framework, data services, revenue test, network effects, embedded workflows, Claude, Codex, OpenAI, Anthropic, Gemini, Copilot, ChatGPT, foundation model, frontier model.
*   **Critical Minerals & Rare Earths:** rare earth, NdPr, neodymium-praseodymium, NdFeB magnets, dysprosium, terbium, gallium, beryllium, niobium, scandium, heavy rare earths, light rare earths, rare earth separation, Chinese rare earth processing, domestic supply chain, CHIPS Act, DoD funding, mine-to-magnet, onshoring, critical minerals, Project Vault, Western supply chain, vertically integrated, strategic reserve.
*   **Defense & Aerospace:** autonomous warfare, drone autonomy, hypersonic, hypersonic test flights, space infrastructure, satellite-to-cellular, defense contracts, SMR for defense, dual-use, Neutron rocket, Space Development Agency, eVTOL, edge AI, geospatial intelligence, orbital compute, launch infrastructure, constellation funding, reaction wheel, LEO broadband.

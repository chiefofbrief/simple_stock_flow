# Workflow Overview
This document summarizes the end-to-end investment research workflow, including phases, steps, file structure, and key dependencies. See `index.md` for a complete map of repository files, folders, scripts, prompts, and source material, which you should consult to understand available tools and context.

## Design Philosophy
The repository is modular by design. Scripts, prompts, data, and source material are organized as independent components that can be run individually or as part of the default workflow. **You must heavily consult `index.md` as the central map for all these modular components, their purposes, and when to use them.** The default workflow is a starting point, not a rigid pipeline — steps can be reordered, skipped, or repeated as the situation demands.

The system follows the default workflow but is expected to suggest deviations — additional scripts, API calls, source material consultation, or new analyses — when the data warrants it. All deviations require user notification and written approval before execution. Written approval means an explicit confirmation in chat (e.g., "yes", "go ahead") before proceeding.

---

## Analysis Philosophy & Guidelines

### Analytical Conduct

Only proceed when sufficient data is available. If data is insufficient to address a query, say so explicitly and develop a plan for gathering the necessary context using the Source Material and/or APIs (see the Index for additional details).

Limit analysis depth to match importance — accept information gaps when additional data requires disproportionate effort. Separately, acknowledge the limitations of the analysis itself: for businesses with limited data, wide variations in financials, or heavy reliance on growth forecasts, conclusions carry less weight. Projections have a significant impact on sentiment and market price, but a margin of safety cannot be based solely on future growth.

**Metric Discipline:** Only apply financial metrics, ratios, and analytical frameworks explicitly established in the project files or source material. Do not introduce outside metrics (e.g., PEG ratio, EV/EBITDA) unless sourced from `index.md` resources. If an additional metric appears relevant, flag it and ask before applying it.

**Source Citation Requirement:** Every factual claim in every analysis must cite its source — the specific file, section, table, or speaker. General references ("per the financial data," "as noted in the Thesis") are not acceptable. Uncited claims must be removed or tagged as inferences.

**Epistemic Tagging:** Every factual claim must be tagged with one of three markers:
- `[CONFIRMED: source]` — figure or fact appears verbatim in a primary source (10-K, 10-Q, earnings transcript)
- `[ESTIMATED: source, method]` — figure is analytically derived from confirmed inputs; show the derivation
- `[INFERRED: source, logic]` — claim is a logical inference from confirmed facts, not a directly disclosed figure

Do not use `[CONFIRMED]` for analytically-derived figures, even if the derivation is airtight. If a claim cannot be tagged, remove it.

**Forward vs. Backward Labeling:** Historical metrics and forward-looking projections must be explicitly labeled as such. A historical CAGR is not a forward growth rate. Where growth is decelerating, the historical CAGR overstates the forward trajectory — flag this explicitly. Do not blend historical figures with forward guidance in the same valuation argument without clearly distinguishing them.

**Adjusted vs. GAAP Labeling:** Every P/E multiple, EPS figure, margin, and earnings-derived metric must be explicitly labeled as GAAP or adjusted (non-GAAP). Do not write "P/E of 12x" — write "adjusted P/E of ~12x (~16.5x GAAP)" and cite the source of both. Where GAAP and adjusted figures diverge materially (>15%), flag the gap and investigate the drivers before drawing valuation conclusions.

**Cross-Section Consistency:** After all steps are complete and before Synthesis, verify that the same figures are described consistently across all Thesis sections. A figure that appears with different values in different sections (e.g., "$150M" in one place and "$255M" in another for the same event) is an error — resolve it before Synthesis. New sections that revise a prior section's conclusion must do so explicitly.

**Devil's Advocate at Synthesis:** Before writing the Bull Case or recommendation, write the strongest possible Bear Case using only facts from the prior analyses. A Bear Case that relies on vague language or doesn't engage with specific data is insufficient. Test every Bull Case point against the Bear Case before finalizing the recommendation.

---

### Investment Types

Two investment types are in scope. Classification is the first step — it determines the analytical burden for everything that follows.

**LOSER — Temporary Price Dislocation**
High-quality businesses with large but solvable one-time problems produce temporary mispricings when the market overreacts to bad news. The resulting divergence between fundamentals and price is the opportunity. The primary analytical question is: *do the fundamentals tell a different story than market sentiment/price, and at what point may the two converge (if ever)?*

Mispricings concentrate in out-of-favor situations: litigation, scandal, distress, disappointment, management upheaval, downgrades. Brand name stocks are particularly attractive candidates — market participants are more likely to hear news of improvement, so these stocks recover faster than secondary stocks when sentiment normalizes.

**TAILWIND — Improvement Due to External Factors**
Businesses of solid quality where external tailwinds — new technology, market cycles, wars, politics — are likely to improve financials and/or sentiment. The primary analytical question is: *is a fundamental improvement likely, when will it occur, and is that improvement already priced in?*

The analytical edge in TAILWIND investing comes from identifying the flaws in the thesis before the market does. If the flaws are found, losses can be limited when reality arrives. It is when we are unaware of what could go wrong that we have to worry. Two specific hazards apply: (1) the forecast may simply be wrong; (2) even if correct, the improvement may already be priced in — accurate forecasts provide no edge if the market already discounts them.

**Signal tiers within each type:** Both LOSER and TAILWIND candidates are sub-classified by signal strength to drive prioritization. For LOSERs, the strongest signal is **LOSER—EPS+** (auto-tagged when EPS YoY > 0 AND vs_1Y < 0) — earnings are intact while price is down, a direct dislocation. Plain LOSERs with flat or temporarily declining earnings rank below. For TAILWINDs, signal strength is measured by Spread (vs_1Y minus EPS YoY): Tier 1 (≤ 0%, earnings outpacing price), Tier 2 (0–30%), Tier 3 (30–150%), Tier 4 (>150% or EPS YoY < −10%). Tier 1 candidates across both types go directly to PIPELINE. Tiers 2–3 remain in WATCHLIST until data improves.

---

### Financials & Margin of Safety

**Start with economic reality, not reported numbers**
Focus on cash generation and economic substance, not accounting presentation. GAAP profits ≠ bona fide profits — true profit means owners are wealthier afterward. The purpose of financial reporting is often to obtain cheap capital, not to present economic reality.

This skepticism extends to the metrics that drive price. Revenue growth gets headlines, but sales growth alone does not grow EPS. A stock rising on top-line growth that doesn't translate to earnings improvement is a mispricing candidate when sentiment corrects. The question is always whether reported improvement reflects genuine cash generation or accounting presentation.

**Margin of Safety**
The goal is safety of principal and adequate return — anything failing either test is speculation. The mechanism is the Margin of Safety: buying below intrinsic value protects against analytical errors, business deterioration, and adverse conditions. Precision is unnecessary — establish whether value is adequate, considerably higher, or lower than price. At sufficiently low prices, even troubled businesses can become investments — downside is limited by the discount to value.

The required MOS is not fixed — it moves with market conditions. When the market is overly optimistic, raise the bar: cheap stocks can still be found, but avoid being too aggressive when prices are elevated. Sentiment is not separate from this calculus. Deeply negative sentiment may produce a wide MOS; strongly positive sentiment may compress it to zero or below. Financials and sentiment must be evaluated together.

---

### Sentiment

Sentiment drives prices, creating opportunities when popularity diverges from value. Prices reflect sentiment, not mathematical risk: public attitude → bids/offers → price.

**Narrative as rationalization:** Price moves often precede their stated explanations. Financial media assigns causes after the fact — large moves occur on no news; significant news produces small moves. Treat reported catalysts as hypotheses, not causes. When news and a price move coincide, the analytical question is always: which came first, and would the price have moved anyway? Institutional flows, technical levels, and positioning can drive moves entirely independent of any fundamental development. The narrative is what gets sold to latecomers.

That a thesis is flawed does not mean we should not invest — as long as other people believe in it and there is a large group left to be convinced. The edge is in looking for the flaws: if found, losses can be limited when the market discovers what we already know. Recognizing flaws that are likely to appear when a hypothesis becomes reality puts you ahead of the game.

**Reflexivity**
In certain conditions, sentiment doesn't just reflect fundamentals — it creates them. Inflated stock prices can accelerate an underlying trend, enhancing expectations and inflating prices further, until outcomes fail to sustain expectations. Two conditions are required for this dynamic to emerge at the stock level: (1) stock prices must be capable of affecting fundamentals through acquisitions, financing, or incentives; and (2) there must be a flaw in perception that allows the bias to emerge.

A misconception is always involved. What makes it durable is that it is reinforced by genuinely improving fundamentals — this is the fertile fallacy. Eventually a turning point is reached, and once the loop reverses it becomes self-reinforcing in the opposite direction. Reflexivity is not an everyday market occurrence, but when present — as with AI today — it can dominate sentiment entirely. It is worth monitoring, not assuming.

---

## Architecture

### Workflow
`Discovery → Price → Earnings → [Initial Position?] → Financials → Footnotes → [Scale/Exit?] → Earnings Calls → Research → Synthesis → [Full Position?]`

- **Consider initial position** — passed Earnings, low-risk profile, no position yet
- **Scale/Exit decision** — passed Financials and Footnotes, quantitative case built and validated
- **Prioritize for deep analysis** — high conviction or complexity warrants Earnings Calls and Research before full sizing
- **Full position** — completed Synthesis, thesis fully validated, conviction warrants full sizing

### Workflow Steps

**How to use this table:** For steps with a script, run the script first to fetch and save data, then load the prompt in a new chat session — the prompt instructs the LLM to read the output files and produce an analysis. For steps with no script, load the prompt directly. All prompts follow a Step 1 (gather context) → Step 2 (analyze) → Step 3 (commit) structure with explicit user approval gates between steps.

| Step | Phase | Script | Prompt | Reads | Writes | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **0. Tracker Update** | Maintenance | `tracker_update.py` | — | `Stock_Tracker.md` | `Stock_Tracker.md`, `{TICKER}_price.json`, `{TICKER}_earnings.json` | Run weekly. Populates market data columns (price, P/E, EPS CAGR, beats, etc.) for all PIPELINE and WATCHLIST tickers via FMP. |
| **1a. Markets Digest** | Screening | `Digest Scripts/markets_digest.py` | `prompt_digest_markets.md` | News APIs | `Markets_Digest_{DATE}.md` | Run daily. Updates `context_markets.md`. |
| **1b. Sectors Digest** | Screening | `Digest Scripts/sectors_digest.py` | `prompt_ai_supply_chain_update.md` | News APIs | `Sectors_Digest_{DATE}.md` | Run when sector developments warrant. Updates `context_ai_supply_chain.md`. |
| **2. Daily Screening** | Screening | — | `prompt_daily_screening.md` | Digests, User Input | `Screening_{DATE}.md` | Reads digest outputs from steps 1a/1b. Produces candidate list. |
| **3. Price & Earnings** | Screening | `price.py` + `earnings.py` | `prompt_price_earnings.md` | `Screening_{DATE}.md` | `Price_Data_{DATE}.txt`, `Earnings_{DATE}.txt`, `Screening_{DATE}.md` | Run sequentially: `price.py` first, then `earnings.py` — earnings depends on price JSON output. Writes analysis directly to the screening file. Can run standalone without a screening file. |
| **4. Screening Completion** | Screening | — | `prompt_screening_completion.md` | `Screening_{DATE}.md` | Thesis, Tracker | Initializes the Thesis file and adds the ticker to the Tracker. |
| **6. Financials** | Deep Dive | `financials.py` | `prompt_financials.md` | Thesis | Thesis, Tracker | |
| **7. Footnotes** | Deep Dive | `footnotes.py` | `prompt_footnotes.md` | Thesis | Thesis, Tracker | *[Scale/Exit decision point]* |
| **8. Earnings Calls** | Deep Dive | `earnings_calls.py` | `prompt_earnings_calls.md` | Thesis | Thesis, Tracker | |
| **9. Research** | Deep Dive | `research.py` | `prompt_research.md` | Thesis | Thesis, Tracker | Investigates open questions from all prior analyses using news data. |
| **10. Synthesis** | Deep Dive | — | `prompt_synthesis.md` | Thesis | Thesis, Tracker | *[Full position decision point]* Final integration of all analyses into an investment verdict. |

---

## Core Tracking
For a complete breakdown of all files, **always consult `index.md`**. Key tracking files include:
- **`Stock_Tracker.md`**: Central tracker with three sections — PIPELINE (active analysis, both LOSERs and TAILWINDs), WATCHLIST (continuous monitoring, awaiting entry signal), and Trade Tracker (open positions). Market data columns are refreshed weekly by `tracker_update.py`.
- **`Screening_{DATE}.md`**: The daily screening file. Captures candidates, enriched context, and price/earnings screening results.
- **`context_markets.md`**: Rolling market context — macro conditions, prevailing narratives, recurring signals. Updated daily via the Markets Digest flow.
- **`context_ai_supply_chain.md`**: AI supply chain context — layer-by-layer dynamics, constraint map, and companies of interest. Updated when meaningful developments warrant it.
- **Thesis Files**: Located in `Data/tickers/{TICKER}/`, built sequentially during Phase 2.

---

## Resources for Additional Context
When data or knowledge gaps arise, consult the available resources detailed in our indexes:

1. **`index.md` (Source Material)**: Maps topics to specific investment literature (e.g., Graham & Dodd, Soros) found in `Source Material/`. When deeper context is needed, search the summaries first. Consult raw chapters only if summaries are insufficient.
   **CRITICAL:** Before reading any large raw source files (`Source Material/raw/`), you must explicitly state your plan and ask the user for permission to avoid burning compute.
2. **`api_index.md`**: Maps available APIs and external data endpoints for fetching live prices, news, and financials. Use this when local data is outdated or missing.

**Quick reference — source strengths:**

- **Security Analysis (Graham & Dodd)** — investment principles, fundamental analysis philosophy, valuation
- **Financial Statement Analysis (Fridson & Alvarez)** — accounting mechanics, financial statement specifics, earnings quality
- **The Alchemy of Finance (Soros)** — reflexivity, market psychology, boom/bust cycles
- **Options: Beginner to Beyond** — options strategies
- **`context_ai_supply_chain.md`** — AI supply chain context across all 13 layers. Includes structural dynamics, constraint map, company-level theses, and reflexivity context.

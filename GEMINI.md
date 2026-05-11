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

**Cross-Section Consistency:** The same figures must be described consistently across all Thesis sections. A figure that appears with different values in different sections is an error — resolve it before Synthesis. New sections that revise a prior section's conclusion must do so explicitly.

**Analytical balance:** Both sides of any investment case must receive equal rigor. A bear case that relies on vague language, fails to cite specific data, or exists only as a formality is insufficient. The same standard applies to the bull case. Neither optimism nor pessimism is the goal — honesty is.

---

### Investment Types

Two investment types are in scope. Classification is the first step — it determines the analytical burden for everything that follows.

**LOSER — Temporary Price Dislocation**
High-quality businesses with large but solvable one-time problems produce temporary mispricings when the market overreacts to bad news. The resulting divergence between fundamentals and price is the opportunity. The primary analytical question is: *do the fundamentals tell a different story than market sentiment/price, and at what point may the two converge (if ever)?*

Mispricings concentrate in out-of-favor situations: litigation, scandal, distress, disappointment, management upheaval, downgrades. Brand name stocks are particularly attractive candidates — market participants are more likely to hear news of improvement, so these stocks recover faster than secondary stocks when sentiment normalizes.

**TAILWIND — Improvement Due to External Factors**
Businesses of solid quality where external tailwinds — new technology, market cycles, wars, politics — are likely to improve financials and/or sentiment. The primary analytical question is: *is a fundamental improvement likely, when will it occur, and is that improvement already priced in?*

The analytical edge in TAILWIND investing comes from identifying the flaws in the thesis before the market does. If the flaws are found, losses can be limited when reality arrives. It is when we are unaware of what could go wrong that we have to worry. Two specific hazards apply: (1) the forecast may simply be wrong; (2) even if correct, the improvement may already be priced in — accurate forecasts provide no edge if the market already discounts them.

**AI SC TAILWIND candidates** may carry speculative characteristics beyond typical TAILWINDs — pre-profitability, wide uncertainty in business model outcomes, valuation dependent on adoption scenarios not yet proven. The analytical burden is higher, not lower, than for standard TAILWINDs. These require the AI-specific prompts (see workflow table).

**Signal tiers within each type:** Both LOSER and TAILWIND candidates are sub-classified by signal strength to drive prioritization. For LOSERs, the strongest signal is **LOSER—EPS+** (auto-tagged when EPS YoY > 0 AND vs_1Y < 0) — earnings are intact while price is down, a direct dislocation. Plain LOSERs with flat or temporarily declining earnings rank below. For TAILWINDs, signal strength is measured by Spread (vs_1Y minus EPS YoY): Tier 1 (≤ 0%, earnings outpacing price), Tier 2 (0–30%), Tier 3 (30–150%), Tier 4 (>150% or EPS YoY < −10%). Tier 1 candidates across both types go directly to PIPELINE. Tiers 2–3 remain in WATCHLIST until data improves.

---

### Financials & Margin of Safety

**Start with economic reality, not reported numbers**
Focus on cash generation and economic substance, not accounting presentation. GAAP profits ≠ bona fide profits — true profit means owners are wealthier afterward. The purpose of financial reporting is often to obtain cheap capital, not to present economic reality.

This skepticism extends to the metrics that drive price. Revenue growth gets headlines, but sales growth alone does not grow EPS. A stock rising on top-line growth that doesn't translate to earnings improvement is a mispricing candidate when sentiment corrects. The question is always whether reported improvement reflects genuine cash generation or accounting presentation.

**P/E discipline applies regardless of growth narrative** — unprofitable companies must be explicitly flagged, and high multiples require scrutiny. For businesses with demonstrated, rapid earnings growth, trailing P/E alone may understate earning power; apply forward P/E alongside trailing and state both. Growth does not excuse valuation — it adjusts it. The central question is always: does the price, given the demonstrated growth rate, produce an adequate expected return?

**Margin of Safety**
The goal is safety of principal and adequate return — anything failing either test is speculation. The mechanism is the Margin of Safety: buying below intrinsic value protects against analytical errors, business deterioration, and adverse conditions. Precision is unnecessary — establish whether value is adequate, considerably higher, or lower than price. At sufficiently low prices, even troubled businesses can become investments — downside is limited by the discount to value.

A margin of safety cannot be based solely on future growth. That said, *demonstrated* earnings growth is a real component of intrinsic value. A business compounding earnings at a durable rate may offer genuine margin of safety at a price that appears expensive on current-year multiples — the safety is embedded in the growth, not the discount. The distinction is between *demonstrated* growth (historical, confirmed, mechanism still intact) and *projected* growth (a story about the future). Only the former contributes to intrinsic value with confidence.

The required MOS is not fixed — it moves with market conditions. When the market is overly optimistic, raise the bar: cheap stocks can still be found, but avoid being too aggressive when prices are elevated. Sentiment is not separate from this calculus. Deeply negative sentiment may produce a wide MOS; strongly positive sentiment may compress it to zero or below. Financials and sentiment must be evaluated together.

**Expected Value:** The expected value of an investment is the probability-weighted sum of its potential outcomes. Precision is not required and is often dishonest — the goal is a clear-eyed assessment of whether the price offers more or less than a dollar's worth of value. Express it as a narrative: *dollar for 70 cents, dollar for a dollar, dollar for 120 cents*. Support the narrative with figures, but the conclusion is qualitative. If the honest answer is "we have no idea," that is acceptable — state it explicitly and name the specific reasons why.

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

`Discovery → Setup (Step 0) → Context (Step 1) → The Numbers (Pass 1) → The Projection (Pass 2) → [Assessment]`

**Assessment** (Expected Value) is written once, at end of Pass 2. It concludes the analysis. No intermediate gates.

**Model division of labor:** Gemini handles Step 0 only — runs fetch scripts, extracts MD&A excerpts verbatim, verifies file checklist. No open-ended analysis. Claude handles all analysis (Step 1, Pass 1, Pass 2).

### Workflow Steps

**How to use:** All prompts follow a Step 1 (gather) → Step 2 (analyze) → Step 3 (commit) structure with explicit user approval gates. For steps with scripts, run the script first; the prompt reads the output files. **Before executing each step, read the corresponding prompt file from `Prompts/`. The table below describes what each prompt does — it does not replace it.**

| Step | Phase | Script | Prompt | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Tracker Update** | Maintenance | `tracker_update.py` | — | Run weekly. Refreshes all market data columns (P/E, ROIC, EPS YoY, FCF, etc.) for PIPELINE and WATCHLIST via FMP. |
| **Tracker Review** | Maintenance | — | `prompt_tracker_review.md` | Run after Tracker Update. Identifies top 3 analysis candidates, add-to-position signals, removal flags. Updates SC Layer Coverage. |
| **Markets Digest** | Screening | `Digest Scripts/markets_digest.py` | `prompt_digest_markets.md` | Run daily. Updates `context_markets.md`. |
| **Sectors Digest** | Screening | `Digest Scripts/sectors_digest.py` | `prompt_ai_supply_chain_update.md` | Run when sector developments warrant. Updates `context_ai_supply_chain.md`. |
| **Price & Earnings** | Screening | `price_earnings.py` | — | Screens candidates on price and earnings. Can run standalone. |
| **Step 0: Setup** | Deep Dive | Multiple — see prompt | `prompt_setup.md` | Gemini-led. Fetches all ticker data, extracts MD&A excerpts, verifies file checklist. No analysis. |
| **Step 1: Context** | Deep Dive | — | `prompt_the_context.md` | Claude. Sentiment, analyst consensus, price/earnings framing, MD&A, preliminary hypothesis. AI SC stocks: use `prompt_the_context_ai.md`. |
| **Pass 1: The Numbers** | Deep Dive | — | `prompt_the_numbers.md` | Claude. 10 financial metrics (incl. ROIC) + 5-category accounting checklist via targeted grep. Updated hypothesis. AI SC stocks: use `prompt_the_numbers_ai.md`. |
| **Pass 2: The Projection** | Deep Dive | — | `prompt_the_projection.md` | Claude. Earnings call analysis, catalyst check, final synthesis + assessment. AI SC stocks: use `prompt_the_projection_ai.md`. |

---

## Core Tracking
For a complete breakdown of all files and scripts, **always consult `index.md`**. Key tracking files:
- **`Stock_Tracker.md`**: Central tracker — PIPELINE (active analysis), WATCHLIST (monitoring, awaiting entry signal), SC Layer Coverage (pipeline count by AI layer), Trade Tracker (open positions). Market data columns refreshed weekly by `tracker_update.py`.
- **`context_markets.md`**: Rolling market context — macro conditions, prevailing narratives, recurring signals. Updated via the Markets Digest flow.
- **`context_ai_supply_chain.md`**: AI supply chain context — layer-by-layer dynamics, constraint map, and company-level theses. Updated when sector developments warrant.
- **Thesis Files**: Located in `Data/tickers/{TICKER}/{TICKER}_Thesis.md`. Four sections built sequentially: `### Context` → `### The Numbers` → `### The Projection` → `### Synthesis`. Assessment (Expected Value) written only at Synthesis.

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

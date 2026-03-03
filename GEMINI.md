# Workflow Overview
This document summarizes the end-to-end investment research workflow, including phases, steps, file structure, and key dependencies. See `Index.md` for a complete map of repository files, folders, scripts, prompts, and source material, which you should consult to understand available tools and context.

## Design Philosophy
The repository is modular by design. Scripts, prompts, data, and source material are organized as independent components that can be run individually or as part of the default workflow. **You must heavily consult `Index.md` as the central map for all these modular components, their purposes, and when to use them.** The default workflow is a starting point, not a rigid pipeline — steps can be reordered, skipped, or repeated as the situation demands.

The system follows the default workflow but is expected to suggest deviations — additional scripts, API calls, source material consultation, or new analyses — when the data warrants it. All deviations require user notification and written approval before execution. Written approval means an explicit confirmation in chat (e.g., "yes", "go ahead") before proceeding.

# Analysis Philosophy & Guidelines

## Analytical Conduct

Only proceed when sufficient data is available. If data is insufficient to address a query, say so explicitly and develop a plan for gathering the necessary context using the Source Material and/or APIs (see the Index for additional details).

Limit analysis depth to match importance — accept information gaps when additional data requires disproportionate effort. Separately, acknowledge the limitations of the analysis itself: for businesses with limited data, wide variations in financials, or heavy reliance on growth forecasts, conclusions carry less weight. Projections have a significant impact on sentiment and market price, but a margin of safety cannot be based solely on future growth.

---

## Investment Types

Two investment types are in scope. Classification is the first step — it determines the analytical burden for everything that follows.

**LOSER — Temporary Price Dislocation**
High-quality businesses with large but solvable one-time problems produce temporary mispricings when the market overreacts to bad news. The resulting divergence between fundamentals and price is the opportunity. The primary analytical question is: *do the fundamentals tell a different story than market sentiment/price, and at what point may the two converge (if ever)?*

Mispricings concentrate in out-of-favor situations: litigation, scandal, distress, disappointment, management upheaval, downgrades. Brand name stocks are particularly attractive candidates — market participants are more likely to hear news of improvement, so these stocks recover faster than secondary stocks when sentiment normalizes.

**TAILWIND — Improvement Due to External Factors**
Businesses of solid quality where external tailwinds — new technology, market cycles, wars, politics — are likely to improve financials and/or sentiment. The primary analytical question is: *is a fundamental improvement likely, when will it occur, and is that improvement already priced in?*

The analytical edge in TAILWIND investing comes from identifying the flaws in the thesis before the market does. If the flaws are found, losses can be limited when reality arrives. It is when we are unaware of what could go wrong that we have to worry. Two specific hazards apply: (1) the forecast may simply be wrong; (2) even if correct, the improvement may already be priced in — accurate forecasts provide no edge if the market already discounts them.

---

## Financials & Margin of Safety

**Start with economic reality, not reported numbers**
Focus on cash generation and economic substance, not accounting presentation. GAAP profits ≠ bona fide profits — true profit means owners are wealthier afterward. The purpose of financial reporting is often to obtain cheap capital, not to present economic reality.

This skepticism extends to the metrics that drive price. Revenue growth gets headlines, but sales growth alone does not grow EPS. A stock rising on top-line growth that doesn't translate to earnings improvement is a mispricing candidate when sentiment corrects. The question is always whether reported improvement reflects genuine cash generation or accounting presentation.

**Margin of Safety**
The goal is safety of principal and adequate return — anything failing either test is speculation. The mechanism is the Margin of Safety: buying below intrinsic value protects against analytical errors, business deterioration, and adverse conditions. Precision is unnecessary — establish whether value is adequate, considerably higher, or lower than price. At sufficiently low prices, even troubled businesses can become investments — downside is limited by the discount to value.

The required MOS is not fixed — it moves with market conditions. When the market is overly optimistic, raise the bar: cheap stocks can still be found, but avoid being too aggressive when prices are elevated. Sentiment is not separate from this calculus. Deeply negative sentiment may produce a wide MOS; strongly positive sentiment may compress it to zero or below. Financials and sentiment must be evaluated together.

---

## Sentiment

Sentiment drives prices, creating opportunities when popularity diverges from value. Prices reflect sentiment, not mathematical risk: public attitude → bids/offers → price.

That a thesis is flawed does not mean we should not invest — as long as other people believe in it and there is a large group left to be convinced. The edge is in looking for the flaws: if found, losses can be limited when the market discovers what we already know. Recognizing flaws that are likely to appear when a hypothesis becomes reality puts you ahead of the game.

**Reflexivity**
In certain conditions, sentiment doesn't just reflect fundamentals — it creates them. Inflated stock prices can accelerate an underlying trend, enhancing expectations and inflating prices further, until outcomes fail to sustain expectations. Two conditions are required for this dynamic to emerge at the stock level: (1) stock prices must be capable of affecting fundamentals through acquisitions, financing, or incentives; and (2) there must be a flaw in perception that allows the bias to emerge.

A misconception is always involved. What makes it durable is that it is reinforced by genuinely improving fundamentals — this is the fertile fallacy. Eventually a turning point is reached, and once the loop reverses it becomes self-reinforcing in the opposite direction. Reflexivity is not an everyday market occurrence, but when present — as with AI today — it can dominate sentiment entirely. It is worth monitoring, not assuming.

## Two-Phase Architecture
### Phase 1: Screening
Rapidly filter tickers to identify candidates worth a deep dive. All output is tracked in the Tracker — no per-ticker files are created at this stage.

### Phase 2: Deep Dive
Build a comprehensive investment thesis for promoted candidates. A dedicated thesis file is created per ticker and populated sequentially as each analysis step completes. On promotion, the thesis file is seeded with the ticker's screening summaries from the Tracker.

## Workflow Steps
| Step | Phase | Script | Prompt | Reads | Writes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Digest** | Screening | `peters_digest.py` | `prompt_digest.md` | News APIs, Digest | Digest |
| **2. Discovery** | Screening | — | `prompt_discovery.md` | Digest, User Text | Tracker, Context |
| **3. Price** | Screening | `price.py` | `prompt_price.md` | Tracker, Context | Tracker |
| **4. Earnings** | Screening | `earnings.py` | `prompt_earnings.md` | Tracker, Context | Tracker |
| **5. Prep** | Deep Dive | — | `prompt_deep_dive_prep.md` | Tracker, Context | Thesis |
| **6. Financials** | Deep Dive | `financials.py` | `prompt_financials.md` | Thesis | Thesis, Tracker |
| **7. Sentiment** | Deep Dive | `sentiment.py` | `prompt_sentiment.md` | Thesis, Context | Thesis, Tracker |
| **8. Footnotes** | Deep Dive | `footnotes.py` | `prompt_footnotes.md` | Thesis | Thesis, Tracker |
| **9. Earnings Calls** | Deep Dive | `earnings_calls.py` | `prompt_earnings_calls.md` | Thesis | Thesis, Tracker |
| **10. Synthesis** | Deep Dive | — | `prompt_thesis_synthesis.md` | Thesis | Thesis, Tracker |

## Core Tracking
For a complete breakdown of all files, **always consult `Index.md`**. Key tracking files include:
- **`Stock_Tracker.md`**: The single source of truth for tracking ticker progress and tags across all phases. (See the tracker itself for detailed formatting and status instructions).
- **Thesis Files**: Located in `Data/tickers/{TICKER}/`, built sequentially during Phase 2.

## Resources for Additional Context
When data or knowledge gaps arise, consult the available resources detailed in our indexes:

1. **`Index.md` (Source Material)**: Maps topics to specific investment literature (e.g., Graham & Dodd, Soros) found in `Source Material/`. When deeper context is needed, search the summaries first. Consult raw chapters only if summaries are insufficient. 
   **CRITICAL:** Before reading any large raw source files (`Source Material/raw/`), you must explicitly state your plan and ask the user for permission to avoid burning compute.
2. **`API_Index.md`**: Maps available APIs and external data endpoints for fetching live prices, news, and financials. Use this when local data is outdated or missing.

**Quick reference — source strengths:**

*   **Security Analysis (Graham & Dodd)** — investment principles, fundamental analysis philosophy, valuation
*   **Financial Statement Analysis (Fridson & Alvarez)** — accounting mechanics, financial statement specifics, earnings quality
*   **The Alchemy of Finance (Soros)** — reflexivity, market psychology, boom/bust cycles
*   **Options: Beginner to Beyond** — options strategies
*   **AI_Guidelines.md** (`AI_Guidelines.md`) — AI ecosystem framework, circular revenue dynamics, sector-specific signals, and key tickers by layer. Applied automatically in all Deep Dive prompts for AI-tagged tickers.

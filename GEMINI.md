# Workflow Overview
This document summarizes the end-to-end investment research workflow, including phases, steps, file structure, and key dependencies. See `INDEX.md` for a complete map of repository files, folders, scripts, prompts, and source material, which you should consult to understand available tools and context.

## Design Philosophy
The repository is modular by design. Scripts, prompts, data, and source material are organized as independent components that can be run individually or as part of the default workflow. The default workflow is a starting point, not a rigid pipeline — steps can be reordered, skipped, or repeated as the situation demands.

The system follows the default workflow but is expected to suggest deviations — additional scripts, API calls, source material consultation, or new analyses — when the data warrants it. All deviations require user notification and written approval before execution.

## Analysis Philosophy & Guidelines
These principles must govern all analysis, interpretation, and thesis generation:

*   **Ground All Interpretations:** Only answer when you have data. If data doesn't exist, say so explicitly—never fill gaps with estimates or assumptions. Ground all interpretations in glossaries or explicitly stated general financial knowledge—never fabricate explanations.
*   **GAAP vs. Economic Reality:** Focus on cash generation and economic substance, not accounting presentation. GAAP profits ≠ bona fide profits—true profit means owners are wealthier afterward. GAAP systematically understates value for intangible-heavy businesses (R&D, IT, brands) by expensing rather than capitalizing. Book value has fallen from 95% (1978) to ~10% (modern FAANG) of market value. Non-GAAP adjustments often exceed GAAP income by 2x. Remember: the purpose of financial reporting is often to obtain cheap capital, not to present economic reality.
*   **Investment vs. Speculation:** True investment requires both thorough analysis and safety of principal. Operations failing either test are speculative. True investment occupies middle ground between two speculative extremes: Low-quality at low prices (speculative due to doubtful quality) and High-quality at high prices (speculative due to excessive valuation). At sufficiently low prices, even troubled businesses can become safe investments—downside is limited by substantial discount to value.
*   **Margin of Safety:** Buy at a discount to intrinsic value — precision isn't required, a range suffices. Intrinsic Value: Value justified by assets, earnings, and definite prospects (approximates present value of future cash flows). Precision is unnecessary—establish whether value is adequate, considerably higher, or lower than price. A range suffices, widening with business uncertainty. Historical performance establishes credibility—consistent returns suggest continuation and provide confidence for buying temporary discounts. Price vs. Value: Buy at bargain prices relative to intrinsic value. This margin protects against analytical errors, business deterioration, and adverse conditions. Require returns exceeding market alternatives (e.g., 15% when market offers high-single-digits)—this gap absorbs mistakes and shortfalls.
*   **Market Pricing:** Sentiment drives prices, creating opportunities when popularity diverges from value. Prices reflect sentiment, not mathematical risk: public attitude → bids/offers → price. Sentiment-driven pricing creates opportunities when popularity diverges from value. Returns aren't inherent to asset classes—they result from fundamentals and prices paid.
*   **Analysis Limitations:** Analysis works best for stable businesses, not those with wide variations. Valuing future growth is hazardous—"little of definite value can be said" about determining prospects. Limit analysis depth to match investment importance; accept information gaps when additional data requires disproportionate effort.
*   **Opportunity Sources:** Best opportunities combine high-quality businesses with large but solvable one-time problems. Mispricings concentrate in out-of-favor situations: litigation, scandal, distress, disappointment, management upheaval, downgrades. Best opportunities combine high-quality businesses with large but solvable one-time problems—quality limits downside, pessimism creates bargain prices. Distinguish temporary problems (depress prices) from permanent impairments (justify low valuations).
*   **The Two Hazards of Forecasting:** (1) Forecast may be wrong. (2) Even if correct, may already be priced in. Current market price already reflects consensus future prospects—accurate forecasts provide no edge if market already discounts them.
*   **All Theses Are Flawed:** That a thesis is flawed does not mean we should not invest—as long as other people believe in it and there is a large group left to be convinced. The edge is in looking for the flaws: if we find them, we can limit losses when the market discovers what we already know. Recognizing flaws that are likely to appear when a hypothesis becomes reality puts you ahead of the game. It is when we are unaware of what could go wrong that we have to worry.
*   **Glamour Metrics Trap:** Be skeptical of "glamour" metrics driving price increases. Revenue growth gets headlines, but sales growth alone does not grow EPS. A stock rising on top-line growth that doesn't translate to earnings improvement is a mispricing candidate when sentiment corrects.
*   **Brand Name Dynamics:** Brand name stocks deserve special attention. Because market participants are more likely to hear news about popular companies, these stocks benefit from good news quickly and recover faster than secondary stocks—making them better mispricing candidates when quality remains intact.
*   **Reflexivity at Stock Level:** A prevailing bias can validate itself by altering a company's operational reality—lowering its cost of capital or inflating the value of its collateral. What appears to be improving "fundamentals" may be an artifact of market sentiment rather than genuine business improvement. Two necessary conditions for a reflexive boom/bust at the stock level: (1) Stock prices must be capable of affecting fundamentals (through acquisitions, financing, incentives), and (2) There must be a flaw in perception that allows the bias to emerge.
*   **Boom/Bust Anatomy:** Watch for reflexive feedback loops where inflated stock prices accelerate an underlying trend, which enhances expectations and inflates prices further—until outcomes fail to sustain expectations. A misconception is always involved (e.g., Conglomerate boom valuing per-share earnings identically; Tech boom valuing revenue multiples). In each case the misconception was reinforced by genuinely improving fundamentals—this is the fertile fallacy. Eventually a turning point is reached, and once stocks decline the trend becomes self-reinforcing in the opposite direction. Reflexivity may or may not give rise to a full boom/bust sequence.
*   **Cautionary Posture:** When the market is overly optimistic, be more selective. Cheap stocks can still be found, but raise the bar and avoid being too aggressive when prices are elevated.

## Two-Phase Architecture
### Phase 1: Screening
Rapidly filter tickers to identify candidates worth a deep dive. All output is tracked in the Tracker — no per-ticker files are created at this stage.

### Phase 2: Deep Dive
Build a comprehensive investment thesis for promoted candidates. A dedicated thesis file is created per ticker and populated sequentially as each analysis step completes.

## Workflow Steps
| Step | Phase | Script | Prompt | Reads | Writes |
|------|-------|--------|--------|-------|--------|
| 1. Price | Screening | price.py | prompt_price.md | Nothing | Tracker |
| 2. Earnings | Screening | earnings.py | prompt_earnings.md | Nothing | Tracker |
| 3. Financials | Deep Dive | financials.py | prompt_financials.md | Nothing | Thesis, Tracker |
| 4. Sentiment | Deep Dive | sentiment.py | prompt_sentiment.md | Financials | Thesis, Tracker |
| 5. Footnotes | Deep Dive | sec_filings.py | prompt_footnotes.md | Financials, Sentiment | Thesis, Tracker |
| 6. Earnings Calls | Deep Dive | earnings_calls.py | prompt_earnings_calls.md | Financials, Sentiment, Footnotes | Thesis, Tracker |

## Key Files
### Tracker
`data/screening/Tracker.md` Single source of truth for all tickers across all phases. Contains a status dashboard table and a concise LLM-generated summary for each completed analysis step per ticker. Updated automatically after each step.

```markdown
# Ticker Tracker

| Ticker | Last Run   | Current Phase | Status   | Thesis File             |
|--------|------------|---------------|----------|-------------------------|
| AAPL   | 2026-02-22 | Earnings      | PASS     | —                       |
| MSFT   | 2026-02-22 | Price         | FILTERED | —                       |
| NVDA   | 2026-02-20 | Earnings Calls| ACTIVE   | NVDA_Research_Thesis.md |

---

### AAPL
**Price** | 2026-02-22 | PASS
{LLM-generated summary}

**Earnings** | 2026-02-22 | PASS
{LLM-generated summary}

---

### NVDA
**Price** | 2026-02-20 | PASS
{LLM-generated summary}

...
```

### Research Thesis (per ticker)
`data/tickers/{TICKER}/{TICKER}_Research_Thesis.md` Created when a ticker is promoted to Deep Dive. Seeded with the ticker's screening summaries from the Tracker. Each subsequent analysis step appends its full findings under a dedicated section header.

## Source Material
Source material is organized into summaries and raw chapters under `sources/`. When deeper context is needed, search summaries first. Consult raw chapters only if summaries are insufficient. See `INDEX.md` for the full Insights Index mapping topics to specific source files.

**Quick reference — source strengths:**

*   **Security Analysis (Graham & Dodd)** — investment principles, fundamental analysis philosophy, valuation
*   **Financial Statement Analysis (Fridson & Alvarez)** — accounting mechanics, financial statement specifics, earnings quality
*   **The Alchemy of Finance (Soros)** — reflexivity, market psychology, boom/bust cycles
*   **Options: Beginner to Beyond** — options strategies

## Filtering
Candidates may be filtered out between any step. Status is updated in the Tracker at each decision point:

*   **PASS** — completed step, proceeding
*   **FILTERED** — eliminated, no further analysis
*   **PROMOTED** — advancing from Screening to Deep Dive
*   **ACTIVE** — Deep Dive in progress

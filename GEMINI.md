# Workflow Overview
This document summarizes the end-to-end investment research workflow, including phases, steps, file structure, and key dependencies. See `Index.md` for a complete map of repository files, folders, scripts, prompts, and source material, which you should consult to understand available tools and context.

## Design Philosophy
The repository is modular by design. Scripts, prompts, data, and source material are organized as independent components that can be run individually or as part of the default workflow. The default workflow is a starting point, not a rigid pipeline — steps can be reordered, skipped, or repeated as the situation demands.

The system follows the default workflow but is expected to suggest deviations — additional scripts, API calls, source material consultation, or new analyses — when the data warrants it. All deviations require user notification and written approval before execution. Written approval means an explicit confirmation in chat (e.g., "yes", "go ahead") before proceeding.

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

## Key Files

### Tracker
`Stock_Tracker.md` — Single source of truth for all tickers across all phases. Contains a status dashboard table and a concise LLM-generated summary for each completed analysis step per ticker. Updated automatically after each step. The tracker includes a Tags column per ticker (e.g., [AI], [LOSER]) used to determine which guidance files or specific prompt instructions apply during analysis.
```markdown
# Ticker Tracker

| Ticker | Last Run   | Current Phase | Status   | Tags           | Thesis File    |
|--------|------------|---------------|----------|----------------|----------------|
| AAPL   | 2026-02-22 | Earnings      | PASS     | [TECH]         | —              |
| MSFT   | 2026-02-22 | Price         | FILTERED | [LOSER] [AI]   | —              |
| NVDA   | 2026-02-20 | Earnings Calls| ACTIVE   | [AI]           | NVDA_Thesis.md |

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

**Earnings** | 2026-02-20 | PASS
{LLM-generated summary}

**Financials** | 2026-02-20 | PASS
{LLM-generated summary}

**Sentiment** | 2026-02-20 | PASS
{LLM-generated summary}

**Footnotes** | 2026-02-20 | PASS
{LLM-generated summary}

**Earnings Calls** | 2026-02-20 | ACTIVE
{LLM-generated summary}
```

### Thesis (per ticker)
`Data/tickers/{TICKER}/{TICKER}_Thesis.md` — Created when a ticker is promoted to Deep Dive. Seeded with the ticker's screening summaries from the Tracker. Each subsequent analysis step appends its full findings under a dedicated section header.

## Source Material
Source material is organized into summaries and raw chapters under `Source Material/`. When deeper context is needed, search summaries first. Consult raw chapters only if summaries are insufficient. **CRITICAL:** Before reading any large raw source files (`Source Material/raw/`), you must explicitly state your plan and ask the user for permission to avoid burning compute. See `Index.md` for the full Insights Index mapping topics to specific source files.

**Quick reference — source strengths:**

*   **Security Analysis (Graham & Dodd)** — investment principles, fundamental analysis philosophy, valuation
*   **Financial Statement Analysis (Fridson & Alvarez)** — accounting mechanics, financial statement specifics, earnings quality
*   **The Alchemy of Finance (Soros)** — reflexivity, market psychology, boom/bust cycles
*   **Options: Beginner to Beyond** — options strategies
*   **AI_Guidelines.md** (`AI_Guidelines.md`) — AI ecosystem framework, circular revenue dynamics, sector-specific signals, and key tickers by layer. Applied automatically in all Deep Dive prompts for AI-tagged tickers.

## Filtering
Candidates may be filtered out between any step. Status is updated in the Tracker at each decision point:

*   **PASS** — completed step, proceeding
*   **FILTERED** — eliminated, no further analysis
*   **PROMOTED** — advancing from Screening to Deep Dive
*   **ACTIVE** — Deep Dive in progress

## Analysis Philosophy & Guidelines
These principles must govern all analysis, interpretation, and thesis generation:

*   **Ground All Interpretations:** Only answer when you have data. If data doesn't exist, say so explicitly—never fill gaps with estimates or assumptions. To fill data or knowledge gaps, you are permitted to leverage the Source Material in addition to the context in the prompts. While you are permitted to use your financial knowledge, we much prefer to rely on the Source Material; if you do use your knowledge, please state that explicitly in your response.

*   **GAAP vs. Economic Reality:** Focus on cash generation and economic substance, not accounting presentation. GAAP profits ≠ bona fide profits—true profit means owners are wealthier afterward. GAAP systematically understates value for intangible-heavy businesses (R&D, IT, brands) by expensing rather than capitalizing. Book value has fallen from 95% (1978) to ~10% (modern FAANG) of market value. Non-GAAP adjustments often exceed GAAP income by 2x. Remember: the purpose of financial reporting is often to obtain cheap capital, not to present economic reality.

*   **Analysis Limitations:** Analysis works best for stable businesses, not those with wide variations. Valuing future growth is hazardous—"little of definite value can be said" about determining prospects. Limit analysis depth to match investment importance; accept information gaps when additional data requires disproportionate effort.

*   **Investment vs. Speculation + Margin of Safety:** True investment requires safety of principal and adequate return — anything failing either test is speculation. The mechanism is the Margin of Safety: buy below intrinsic value. Precision is unnecessary — establish whether value is adequate, considerably higher, or lower than price. This margin protects against analytical errors, business deterioration, and adverse conditions. At sufficiently low prices, even troubled businesses can become investments — downside is limited by the discount to value.

*   **Market Pricing:** Sentiment drives prices, creating opportunities when popularity diverges from value. Prices reflect sentiment, not mathematical risk: public attitude → bids/offers → price. Returns aren't inherent to asset classes—they result from fundamentals and prices paid.

*   **The Two Hazards of Forecasting:** (1) Forecast may be wrong. (2) Even if correct, may already be priced in. Current market price already reflects consensus future prospects—accurate forecasts provide no edge if the market already discounts them.

*   **Opportunity Sources + Brand Name Dynamics:** Best opportunities combine high-quality businesses with large but solvable one-time problems. Mispricings concentrate in out-of-favor situations: litigation, scandal, distress, disappointment, management upheaval, downgrades. Quality limits downside, pessimism creates bargain prices — distinguish temporary problems (depress prices) from permanent impairments (justify low valuations). Brand name stocks are particularly attractive candidates because market participants are more likely to hear news of improvement, so these stocks recover faster than secondary stocks when sentiment normalizes.

*   **Glamour Metrics Trap:** Be skeptical of "glamour" metrics driving price increases. Revenue growth gets headlines, but sales growth alone does not grow EPS. A stock rising on top-line growth that doesn't translate to earnings improvement is a mispricing candidate when sentiment corrects.

*   **All Theses Are Flawed:** That a thesis is flawed does not mean we should not invest—as long as other people believe in it and there is a large group left to be convinced. The edge is in looking for the flaws: if we find them, we can limit losses when the market discovers what we already know. Recognizing flaws that are likely to appear when a hypothesis becomes reality puts you ahead of the game. It is when we are unaware of what could go wrong that we have to worry.

*   **Reflexivity at Stock Level:** A prevailing bias can validate itself by altering a company's operational reality—lowering its cost of capital or inflating the value of its collateral. What appears to be improving "fundamentals" may be an artifact of market sentiment rather than genuine business improvement. Two necessary conditions for a reflexive boom/bust at the stock level: (1) Stock prices must be capable of affecting fundamentals (through acquisitions, financing, incentives), and (2) There must be a flaw in perception that allows the bias to emerge.

*   **Boom/Bust Anatomy:** Watch for reflexive feedback loops where inflated stock prices accelerate an underlying trend, which enhances expectations and inflates prices further—until outcomes fail to sustain expectations. A misconception is always involved (e.g., Conglomerate boom valuing per-share earnings identically; Tech boom valuing revenue multiples). In each case the misconception was reinforced by genuinely improving fundamentals—this is the fertile fallacy. Eventually a turning point is reached, and once stocks decline the trend becomes self-reinforcing in the opposite direction. Reflexivity may or may not give rise to a full boom/bust sequence.

*   **Cautionary Posture:** When the market is overly optimistic, be more selective. Cheap stocks can still be found, but raise the bar and avoid being too aggressive when prices are elevated.
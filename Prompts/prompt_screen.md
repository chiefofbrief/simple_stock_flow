# Prompt — Screen

## Role

You are screening a list of tickers to determine which warrant further investigation and potential addition to the tracker. This is triage, not analysis. The output is a structured comparison table and a brief per-ticker narrative — sufficient to surface the strongest candidates and dismiss the rest.

---

## Step 1: Gather Context

**Guidelines**
- `GEMINI.md` — Read the **Investment Types** and **Financials & Margin of Safety** sections. These define the analytical lens applied throughout — what constitutes a compelling signal, what quality means, and what the framework is trying to find.

**Data**

Run the following with the tickers to screen:

```
python Scripts/screen.py TICKER1 TICKER2 ...
```

Read the output file produced at:

```
Data/screening/Screen_{DATE}.txt
```

The script outputs the following metrics for each ticker:
- **Mkt Cap** — market capitalization
- **Spread** — Price vs_1Y minus EPS vs_1Y (≤0 = earnings outpacing price)
- **P/E Corr** — Pearson correlation of monthly price vs. TTM EPS over 12 months
- **Price** — current price
- **Price vs_1Y** — price change vs. 1 year ago
- **Price vs_2Y** — price change vs. 2 years ago
- **EPS TTM** — trailing twelve months EPS (diluted)
- **EPS vs_1Y** — most recent quarter EPS vs. same quarter prior year
- **EPS vs_2Y** — EPS vs. same quarter two years ago
- **Avg EPS QoQ (4Q)** — average of last 4 quarterly EPS changes (smoothed momentum)
- **P/E** — GAAP trailing P/E (TTM)
- **P/OE** — price to owner earnings (Market Cap / (FCF TTM − SBC TTM))
- **ROIC** — TTM return on invested capital (NOPAT / Invested Capital)
- **ROIC vs_1Y (pp)** — ROIC change vs. 1 year ago (percentage points)
- **ROIC vs_2Y (pp)** — ROIC change vs. 2 years ago (percentage points)
- **OCF/NI** — operating cash flow / net income (accrual quality)
- **FCF TTM** — trailing twelve months free cash flow
- **FCF vs_1Y** — FCF change vs. prior year
- **FCF vs_2Y** — FCF change vs. 2 years ago
- **Rev TTM** — trailing twelve months revenue
- **Rev vs_1Y** — revenue change vs. prior year
- **Rev vs_2Y** — revenue change vs. 2 years ago
- **Debt/OCF** — total debt / TTM operating cash flow

Do not proceed until the script completes successfully. If the script fails or returns missing data for any ticker, note the gap explicitly and proceed with available data — do not silently omit a ticker.

**STOP. Do not proceed until GEMINI.md sections and the script output have both been read.**

---

## Step 2: Analyze

> **Output mode — read before starting.**
> Write the table and per-ticker narratives directly in chat. No file writes during this step. This keeps the output reviewable before any commitment is made.

Work through the Output Format in order. The Metric Interpretations section at the bottom of this prompt is your primary interpretive reference — read it before beginning and apply it metric by metric.

---

### Analysis Guidelines

**Primary question first**
Spread is the primary signal: is earnings growth outpacing price growth? ROIC is the second-order signal: is the business behind that spread creating durable value? All other metrics contribute to conviction holistically — this is a holistic read, not a sort. For example, a weak spread with exceptional ROIC and broad quality support can outrank a strong spread with deteriorating fundamentals. Establish the spread first, then assess the full picture.

**Comparison frame**
This is a side-by-side screening, not a series of individual analyses. Read tickers against each other. A spread that looks strong in isolation may look less compelling against a peer with a stronger spread and higher ROIC. The contrast between candidates is as informative as any individual reading.

**Quarterly weighting**
For cyclical and growth businesses where an industry inflection may be underway, weight Avg EPS QoQ (4Q) appropriately alongside the annual figures. Do not allow a lagging annual comparison to dismiss a live earnings recovery visible in the quarterly trend.

**GAAP vs. adjusted**
Every P/E and EPS figure must be read as GAAP. Where GAAP and adjusted figures diverge materially (>15%), flag the gap and note the drivers — the adjusted figure may exclude real recurring costs such as SBC.

**Source discipline**
This analysis must be grounded in the script output and the Metric Interpretations below. Outside knowledge — industry norms, general financial theory — may inform interpretation but must never substitute for data. When you draw on outside knowledge, say so explicitly. When data needed for a conclusion is unavailable, flag the gap — do not fill it with assumptions.

---

### Output Format

All sections below constitute the full screening output.

---

#### Screening Table

Present the full comparison table. All tickers appear as columns. Every row must be populated — use `—` only when the data is genuinely unavailable from the script. Do not omit rows.

```
                         | TICKER A | TICKER B | TICKER C |
─── SIGNAL ──────────────┤
Spread (Price−EPS 1Y)    |          |          |          |
P/E Correlation 1Y       |          |          |          |
Mkt Cap                  |          |          |          |

─── PRICE ───────────────┤
Price                    |          |          |          |
vs_1Y                    |          |          |          |
vs_2Y                    |          |          |          |

─── EARNINGS ────────────┤
EPS (TTM)                |          |          |          |
EPS vs_1Y                |          |          |          |
EPS vs_2Y                |          |          |          |
Avg EPS QoQ (4Q)         |          |          |          |

─── VALUATION ───────────┤
P/E (GAAP TTM)           |          |          |          |
P/Owner Earnings         |          |          |          |

─── QUALITY ─────────────┤
ROIC                     |          |          |          |
ROIC vs_1Y (pp)          |          |          |          |
ROIC vs_2Y (pp)          |          |          |          |
OCF/NI                   |          |          |          |
FCF (TTM)                |          |          |          |
FCF vs_1Y                |          |          |          |
FCF vs_2Y                |          |          |          |
Revenue (TTM)            |          |          |          |
Rev vs_1Y                |          |          |          |
Rev vs_2Y                |          |          |          |
Debt/OCF                 |          |          |          |
```

---

#### Priority Ranking

Below the table, write a ranked priority list before the full narratives. Group tickers into three buckets:

- **Add to Tracker** — signal clear enough to warrant ongoing monitoring; quality supports it, or a specific blocker is identified and named
- **Skip** — no signal, inverted signal, or quality disqualifies it

Format: one line per ticker, in order within each bucket. Each line states the one-sentence reason. Answer three things implicitly in that sentence: is earnings outpacing price, are earnings reliable, and what is the key flag.

---

#### Per-Ticker Narratives

Below the priority ranking, write one focused paragraph per ticker. Each paragraph must address:

1. What does the spread and P/E correlation say about the primary signal?
2. What do the quality metrics say about the durability of that signal?
3. What is the single most important open question if this ticker proceeds to the tracker?

Do not restate the numbers — interpret them. The table already contains the data; the narrative is the read.

---

## Self-Check

Answer the following internally before presenting output. Do not include these answers in your output — they are for your own verification only. If any answer is no, revise before proceeding.

- Has the Metric Interpretations been read before beginning?
- Has quarterly weighting been applied where an industry inflection appears underway?
- Has the ranking been holistic — not just a Spread sort?
- Does the narrative interpret rather than restate the numbers?
- Have the strongest and weakest candidates been distinguished — is the comparison frame present?
- Are GAAP vs. adjusted gaps flagged where they diverge materially (>15%)?

---

## Step 3: Commit

Present the table and narratives in chat for review.

Once the user has reviewed, append the full analysis (table + per-ticker narratives) to the existing screening file at:

```
Data/screening/Screen_{DATE}.txt
```

The script already wrote the raw data to this file. Append a clearly marked section break followed by the analysis:

```
════════════════════════════════════════════════
ANALYSIS — {DATE}
════════════════════════════════════════════════

[table]

[per-ticker narratives]
```

**Action:** Ask: *"Which of these tickers would you like to add to the tracker, and to which section?"*

**STOP. Do not write to any file without explicit user instruction.**

---

## Metric Interpretations

---

### SPREAD — Price vs_1Y minus EPS vs_1Y

The spread is the primary signal. It answers the core question: **is earnings growth outpacing price growth?**

A spread at or below zero — earnings growing as fast or faster than price — is the compelling signal. A modestly positive spread means price has moved ahead of earnings but the gap is not alarming; earnings growth still exists and the relationship warrants monitoring. A highly positive spread, or one where EPS YoY is negative, means price is significantly ahead of earnings or earnings are declining — the burden of proof is high before proceeding further.

Also compute the 2-year spread: EPS vs_2Y minus Price vs_2Y. A strong 1Y spread alongside a weak or negative 2Y price delta is the better signal — it suggests the dislocation is recent and acute, consistent with an overreaction to a specific event. That is what the framework targets. A strong spread on both 1Y and 2Y warrants more scrutiny — the dislocation may have been building for longer, which raises the question of whether it is temporary or structural.

---

### P/E CORRELATION — 1Y

Complements the spread by measuring consistency rather than magnitude. A correlation near +1.0 means price and earnings have been moving in sync throughout the period. A correlation near 0 or negative means they have been diverging systematically — the lower the correlation alongside a positive spread, the more persistent the dislocation. A strong spread alongside a low or negative correlation is a stronger combined signal than spread alone.

---

### PRICE — Current, vs_1Y, vs_2Y

The price rows establish the starting point for the spread calculation. vs_1Y and vs_2Y must be read together — vs_1Y alone can be misleading when the reference point one year ago was itself an anomalous high or low.

Read the two deltas in combination to understand the nature of the dislocation. As illustrations of the reasoning: a stock down sharply on vs_1Y but roughly flat on vs_2Y suggests an acute recent event; a stock down similarly on both suggests a gradual multi-year decline that deserves more scrutiny before treating it as a temporary opportunity. The principle is to assess whether the dislocation is recent or chronic — the former is what the framework targets.

Price has no inherent signal on its own. The signal emerges in combination with earnings.

---

### EARNINGS — EPS TTM, vs_1Y, vs_2Y, Avg EPS QoQ (4Q)

EPS YoY is the primary annual signal. Avg EPS QoQ (4Q) shows whether earnings momentum is building or fading in real time — and for cyclical and growth businesses where an industry inflection is underway, the quarterly trend can be the leading indicator before annual comparisons have had time to reflect the turn. A stock with still-negative EPS YoY but several consecutive quarters of positive and accelerating QoQ growth may be at the early stage of an inflection the annual number has not yet captured. Weight the quarterly trend accordingly — do not let a lagging annual figure dismiss a live earnings recovery.

vs_1Y and vs_2Y read together reveal whether growth is accelerating, decelerating, or a single-year anomaly. A meaningful divergence between the two — in either direction — is worth explaining before drawing a conclusion.

---

### VALUATION — P/E (GAAP TTM)

Below 20x cheap; 20–30x reasonable; above 30x requires strong growth justification. Above 50x needs exceptional and accelerating growth.

P/E must always be read as GAAP. Where GAAP and adjusted figures diverge materially (>15%), note the gap — the adjusted figure may exclude real recurring costs such as SBC. See P/Owner Earnings.

---

### VALUATION — P/Owner Earnings

Owner Earnings = FCF − SBC. P/Owner Earnings = Market Cap ÷ Owner Earnings.

> The appropriate owner-earnings figure is FCF minus SBC, not gross FCF. SBC is a recurring economic cost that dilutes shareholders; it inflates OCF relative to NI but does not improve earnings quality.

P/Owner Earnings is the correct economic multiple — it prices the business as a buyer of the whole enterprise would, after accounting for the true cost of equity compensation.

Read P/OE alongside P/E. When they are close, SBC is a small fraction of FCF and the gross multiple is a reasonable approximation. When P/OE is materially above P/E, SBC is a significant drag on owner earnings — assess whether it is stable, growing, or declining as a percentage of revenue, since a declining trend narrows the gap over time. When P/OE is undefined or negative, FCF is negative or SBC exceeds FCF — any valuation argument is entirely forward-looking.

---

### QUALITY — ROIC, ROIC vs_1Y (pp), ROIC vs_2Y (pp)

> Measures how efficiently a business converts its total capital base — debt and equity combined — into after-tax operating profit. Unlike EPS, ROIC is unaffected by capital structure choices such as debt-funded buybacks or acquisitions. It answers the question EPS cannot: for every dollar deployed in the business, how many cents of operating profit does it generate?

> **Above 20%:** Strong capital efficiency — indicative of durable competitive advantage. A business sustaining 20%+ ROIC across a full economic cycle is generating a meaningful spread over its cost of capital.
> **10–20%:** Moderate — acceptable but not exceptional. The spread over cost of capital is narrow; growth does not automatically create value.
> **Below 10%:** Weak — the business may be destroying value with every dollar it reinvests. Growth actively makes this worse.

> The ROIC trend is as informative as the absolute level. A business at 22% and rising tells a different story from one at 28% and declining. A narrowing ROIC trend is an early warning of moat erosion — it tends to precede margin compression and multiple contraction by two to three reporting periods.

vs_1Y and vs_2Y express the trend in percentage points. Read them directionally: sustained improvement over two years is a moat-strengthening signal; sustained deterioration is a structural warning regardless of the absolute level. A single-year dip warrants less weight than a consistent multi-year trend.

> **Intangible-heavy businesses:** Book value understates economic capital for companies whose competitive advantages rest on R&D, brand, or software. ROIC will appear elevated relative to asset-heavy peers — this is appropriate, not a distortion, if genuine intangible value creation underlies it.
> **Asset age limitation:** A business can mechanically boost ROIC by underinvesting — fully depreciated assets reduce the denominator without reflecting economic reality. Cross-reference FCF trend when ROIC appears unusually high.
> **Negative invested capital:** Asset-light businesses with large deferred revenue or negative working capital can have ROIC that is mathematically undefined or misleading. Flag this when it occurs; use FCF as the primary quality metric instead.

---

### QUALITY — OCF/NI

> Measures earnings quality by comparing reported profits to actual cash collection.

> **> 1.1:** Conservative accounting or efficient working capital management — high quality earnings.
> **0.8–1.1:** Reasonable earnings quality.
> **< 0.8** (especially if deteriorating): Earnings significantly exceed cash generation, suggesting potential revenue recognition issues, working capital consumption, or reserve inadequacy.

> A ratio above 1.1 does not automatically indicate conservative accounting — identify the specific non-cash drivers first. SBC is a recurring economic cost that dilutes shareholders; it inflates OCF relative to NI but does not improve earnings quality. Amortization of acquired intangibles is a wasting charge that declines as acquisitions age — more benign, but requires verification. The appropriate owner-earnings figure is FCF minus SBC, not gross FCF.

---

### QUALITY — FCF TTM, vs_1Y, vs_2Y

> Free cash flow represents the cash an owner can pocket after paying all expenses and making necessary maintenance investments — "the well from which all returns are drawn." It is the ultimate measure of value creation regardless of how that value is deployed.

> Consistent FCF generation indicates a self-funding business not dependent on external capital. Strong current FCF generation means nothing if the business model is deteriorating or if the company benefited from unsustainable temporary factors.

Positive/improving FCF = earnings are real. Declining FCF + positive EPS = yellow flag.

vs_1Y and vs_2Y read together: FCF growing on both is the most durable cash generation signal. FCF vs_1Y positive but vs_2Y flat or negative warrants assessment of whether the improvement is operational or transient. FCF declining on both alongside growing EPS is the most serious earnings quality flag at screening level — earnings are not converting to cash across multiple periods.

---

### QUALITY — Revenue TTM, vs_1Y, vs_2Y

> Revenue growth substantially above industry with maintained margins indicates strengthening position; growth above industry with compressing margins suggests buying share through price cuts.

> Revenue growth without margin improvement creates no shareholder value — acceleration alone is meaningless if profit per dollar of sales remains constant or declines.

> Red flag: Growth substantially outpacing competitors without operational explanation warrants investigation and could signal aggressive accounting.

Declining EPS alone is not sufficient — a company with deteriorating EPS but growing revenue may have a timing or accounting distortion, not a broken thesis. Only flag when deterioration is broad-based.

vs_1Y and vs_2Y read together: revenue growing on both is the baseline healthy signal. Revenue vs_2Y strong but vs_1Y decelerating — assess whether the deceleration is cyclical, competitive, or structural. Revenue growing while EPS and FCF are flat or declining across both periods means growth is not reaching the bottom line; investigate before treating revenue growth as a positive signal.

---

### SIGNAL — Mkt Cap

Context for normalization, not a signal in itself. Below $10B warrants additional scrutiny before proceeding further.

---

### QUALITY — Debt/OCF

Measures the time required to eliminate all debt if 100% of operating cash flow were dedicated to debt repayment.

**Below 3x:** Strong debt service capacity.
**3x–5x:** Manageable with stable cash generation.
**Above 5x:** Distress risk rises meaningfully if OCF declines.
**Above 7x:** Serious scrutiny required regardless of spread.

Ratio rising due to OCF decline rather than debt increase signals operational deterioration rather than strategic leverage increase. For highly seasonal businesses, evaluate on TTM basis only.

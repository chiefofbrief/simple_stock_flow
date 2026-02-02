# Screening Analysis Skill

**⚠️ DRAFT - This skill file is a preliminary draft and may require refinement based on actual usage patterns.**

## Prerequisites

**Before executing this skill, you must:**
1. Read this entire skill file - Contains workflow and analysis framework
2. Have valuation data available for the target ticker(s)

**Required Files:**
- Price history data: `{TICKER}_prices.json` (from `prices.py`)
- Earnings data: `{TICKER}_earnings.json` (from `earnings.py`)
- Valuation analysis output from `valuation.py` (terminal output or redirected to file)

**How to Generate Required Files:**
```bash
# Batch processing recommended for screening multiple tickers
python scripts/ticker/prices.py TICKER1 TICKER2 TICKER3
python scripts/ticker/earnings.py TICKER1 TICKER2 TICKER3

# Run valuation analysis
python scripts/valuation.py TICKER1 TICKER2 TICKER3
```

**Data Location:**
- `data/analysis/{TICKER}/{TICKER}_prices.json`
- `data/analysis/{TICKER}/{TICKER}_earnings.json`

---

## Analysis Methodology

**Objective:** Quick fundamental screening to identify candidates worth deeper analysis.

**Framework:**
This is a preliminary filter, not a buy/sell decision. The screening analysis answers:
1. **Price behavior** - Recent changes, volatility, positioning vs. historical levels
2. **Earnings quality** - Trends, volatility, vs. analyst expectations
3. **Price-earnings relationship** - Correlation strength and implications

**Decision Outcome:**
- **Pass:** Proceed to statement analysis (financial_statements.py)
- **Maybe:** Flag concerns but consider for deeper analysis
- **Fail:** Skip or deprioritize

---

## Workflow

Analyze each ticker against the screening framework. Document findings in structured format.

**Tone Guidance:** Brief and analytical. Focus on flags (positive or negative). Use specific data points. Avoid speculation.

### Analysis Questions

For each ticker, address the following:

#### 1. Price Behavior Analysis

**Recent Price Changes:**
- Has the price changed significantly recently? (1-mo, 1-yr changes)
- What is the magnitude and direction?

**Volatility Assessment:**
- How volatile is the price? (5-yr CV, coefficient of variation)
- Is volatility elevated vs. typical levels?

**Positioning:**
- Where is current price relative to 5-yr average?
- Where is current price relative to 52-week high/low?
- Trend: Improving, stable, or deteriorating?

#### 2. Earnings Trend Analysis

**Historical Trends (5 years):**
- Is EPS growing, stable, or declining?
- What is the 5-yr CAGR?
- Are there outlier years?

**Recent Trends (4 quarters):**
- What is the quarterly EPS trend?
- Any significant shifts in recent quarters?

**Volatility:**
- How volatile are earnings? (CV)
- Is earnings stability acceptable for valuation confidence?

#### 3. Earnings vs. Expectations

**Consensus Comparison:**
- How does most recent EPS compare to analyst consensus estimate?
- What is the range of analyst estimates?
- Beat, meet, or miss expectations?

**Implications:**
- Does the market already reflect this information?
- Any surprises that warrant investigation?

#### 4. Price-Earnings Correlation

**Correlation Strength:**
- What is the correlation between price and earnings over 5 years?
- Strong positive correlation (>0.7): Price tracks fundamentals
- Weak/negative correlation (<0.5): Potential mispricing or structural change

**Current P/E Positioning:**
- Current P/E vs. 5-yr average P/E
- Is the stock trading at a premium or discount?
- Context: Is this justified by earnings trends?

**Price-EPS Divergence:**
- Has price moved independently of earnings recently?
- Potential undervaluation (price lags strong earnings) or overvaluation (price exceeds earnings growth)?

---

## Required Output Format

For each ticker analyzed:

```markdown
# Screening Analysis: {TICKER}

**Date:** {YYYY-MM-DD}
**Recommendation:** [PASS / MAYBE / FAIL]

---

## Quick Summary

**Price:** ${current_price}
- 1-mo: {+/- X%}
- 1-yr: {+/- X%}
- vs 5-yr avg: {+/- X%}

**Earnings (TTM EPS):** ${eps}
- 5-yr CAGR: {X%}
- vs Consensus: {Beat/Meet/Miss by X%}

**Valuation:**
- P/E (current): {X}
- P/E (5-yr avg): {X}
- Price-EPS Correlation: {0.XX}

**Key Flags:**
- [List 2-3 most important positive or negative signals]

---

## Detailed Analysis

### 1. Price Behavior

**Recent Changes:**
- 1-month: {+/- X%} - [Brief interpretation]
- 1-year: {+/- X%} - [Brief interpretation]

**Volatility:**
- 5-yr CV: {X%} - [Low/Moderate/High relative to typical stock volatility]

**Positioning:**
- Current: ${price}
- 5-yr Average: ${avg}
- Delta: {+/- X%} - Trading [above/below/at] historical average
- 52-week range: ${low} - ${high} - Currently at [X%] of range

**Assessment:** [1-2 sentences on price behavior implications]

---

### 2. Earnings Trends

**5-Year Historical:**
| Metric | Value | Interpretation |
|--------|-------|----------------|
| 5-yr CAGR | {X%} | [Growing/Stable/Declining] |
| Volatility (CV) | {X%} | [Stable/Erratic] |
| Outliers | {Years if any} | [Context if applicable] |

**Recent Quarters (TTM):**
- Q1: ${eps}
- Q2: ${eps}
- Q3: ${eps}
- Q4: ${eps}
- Trend: [Improving/Stable/Declining]

**Assessment:** [1-2 sentences on earnings quality]

---

### 3. Earnings vs. Expectations

**Most Recent EPS:** ${actual_eps}
**Consensus Estimate:** ${consensus_eps}
**Delta:** {Beat/Miss by X%}

**Analyst Range:**
- Low: ${low_estimate}
- High: ${high_estimate}
- Range: {X%} - [Narrow/Wide consensus]

**Assessment:** [1-2 sentences on whether expectations are met and implications]

---

### 4. Price-Earnings Relationship

**Correlation:** {0.XX}
- Strength: [Strong/Moderate/Weak] - {Interpretation: Price tracks fundamentals vs potential disconnect}

**Valuation Context:**
- Current P/E: {X}
- 5-yr Avg P/E: {X}
- Premium/Discount: {+/- X%}

**Divergence Check:**
- Price 5-yr CAGR: {X%}
- EPS 5-yr CAGR: {X%}
- Delta: {X% points} - [Price outpacing/lagging earnings]

**Assessment:** [2-3 sentences on valuation and any apparent mispricing]

---

## Screening Decision

**Recommendation:** [PASS / MAYBE / FAIL]

**Rationale:**
- [Key reason 1]
- [Key reason 2]
- [Key reason 3]

**Red Flags (if any):**
- [List significant concerns]

**Next Steps:**
- If PASS: Proceed to statement analysis and peer comparison
- If MAYBE: [Specify what additional context is needed]
- If FAIL: [Specify disqualifying factors]
```

---

## Multi-Ticker Screening Summary

When screening multiple tickers, provide a comparative summary:

```markdown
# Screening Summary: Batch Analysis

**Date:** {YYYY-MM-DD}
**Tickers Analyzed:** {N}

| Ticker | Decision | Key Signal | P/E Current | P/E 5yr Avg | Price vs Avg | EPS CAGR | Correlation |
|--------|----------|------------|-------------|-------------|--------------|----------|-------------|
| {TICKER1} | PASS | {Signal} | {X} | {X} | {+/-X%} | {X%} | {0.XX} |
| {TICKER2} | FAIL | {Signal} | {X} | {X} | {+/-X%} | {X%} | {0.XX} |
| {TICKER3} | MAYBE | {Signal} | {X} | {X} | {+/-X%} | {X%} | {0.XX} |

**Top Candidates (PASS):**
1. {TICKER} - [Brief rationale]
2. {TICKER} - [Brief rationale]

**Borderline (MAYBE):**
1. {TICKER} - [What needs clarification]

**Rejected (FAIL):**
1. {TICKER} - [Disqualifying factor]

**Recommended Next Steps:**
- Deep dive on: {TICKER1, TICKER2}
- Monitor for: {TICKER3}
```

---

## Decision Guidelines

**PASS Indicators:**
- Price has moved significantly vs historical average (potential opportunity)
- Earnings trend is positive or stable with low volatility
- P/E is below historical average with strong correlation
- Recent EPS meets or beats expectations with narrow analyst range
- No major red flags in price behavior

**MAYBE Indicators:**
- Mixed signals (e.g., strong earnings but elevated valuation)
- High volatility requiring context from deeper analysis
- Weak correlation suggesting structural change (needs investigation)
- Recent price movement lacking clear fundamental driver

**FAIL Indicators:**
- Deteriorating earnings trend with high volatility
- P/E significantly above historical average without justification
- Consistent misses vs. analyst expectations
- Price-earnings correlation breakdown suggesting fundamental problems
- Price moving opposite to earnings (bearish divergence)

---

## Notes

**Data Sources:**
- `valuation.py` provides: P/E current, P/E 5yr avg, price-EPS correlation, Forward Delta
- `prices.py` provides: Price changes, volatility (CV), positioning vs 5-yr average
- `earnings.py` provides: EPS history, CAGR, volatility, consensus comparison

**Tool Usage:**
- Read JSON files directly (they are small, structured data)
- Extract relevant fields for each analysis question
- Calculate any missing metrics if needed

**Screening vs. Deep Analysis:**
- This is a filter, not a valuation
- Focus on identifying candidates worth deeper investigation
- Statement analysis (financial_statements.py) is where the real work begins
- Sentiment analysis (sentiment.py) provides additional context after screening

**Flexibility:**
- Thresholds are guidelines, not hard rules
- Context matters - a FAIL in one area may be offset by strength elsewhere
- Industry context may shift what constitutes "normal" volatility or valuation

---

**⚠️ DRAFT NOTICE:** This skill file is a preliminary draft. Expected refinements:
- Decision threshold calibration based on actual screening results
- Industry-specific volatility and P/E benchmarks
- Integration with sector rotation and macro context
- Refinement of PASS/MAYBE/FAIL criteria

# Screening Analysis Skill

**⚠️ DRAFT - This skill file is a preliminary draft and may require refinement based on actual usage patterns.**

## Context

**Purpose:** Quick fundamental screening to identify candidates worth deeper analysis. This is a preliminary assessment, not a buy/sell decision.

**Available Data:**
- Price history: `{TICKER}_prices.json` (from `prices.py`)
- Earnings data: `{TICKER}_earnings.json` (from `earnings.py`)
- Valuation analysis: Output from `valuation.py`

---

## Key Questions to Address

For each ticker being screened, analyze the following:

### Price Behavior
- Has the price changed significantly recently? (1-mo, 1-yr)
- How volatile is the price? (5-yr coefficient of variation)
- Where is the current price relative to historical averages (5-yr average) and recent trends (52-week range)?

### Earnings Trends
- What is the earnings trend over the past 5 years? (CAGR, outliers)
- What is the earnings trend over the past 4 quarters?
- How volatile are earnings? (CV - does this affect valuation confidence?)

### Earnings vs. Expectations
- How does the most recent EPS compare to analyst consensus estimate?
- What is the range of analyst estimates? (Narrow vs. wide)
- Does the market already reflect this information?

### Price-Earnings Relationship
- What is the correlation between price and earnings over 5 years?
  - Strong correlation (>0.7): Price tracks fundamentals
  - Weak correlation (<0.5): Potential mispricing or structural change
- Current P/E vs. 5-yr average P/E - premium or discount?
- Has price moved independently of earnings recently? (Divergence signals)

---

## Output Guidance

Provide a concise screening assessment that addresses the key questions above. Include:

- **Summary snapshot:** Price, earnings, and valuation metrics at a glance
- **Analysis:** Address each question with specific data points
- **Flags:** Note significant signals (positive or negative)
- **Assessment:** Is this candidate worth deeper analysis? What are the key considerations?

When screening multiple tickers, a comparative table can help identify relative strengths:

| Ticker | Price vs 5yr Avg | EPS CAGR | P/E vs Avg | Correlation | Key Signal |
|--------|------------------|----------|------------|-------------|------------|
| ...    | ...              | ...      | ...        | ...         | ...        |

**Flexibility:** The format can adapt to the situation. What matters is addressing the key questions and providing clear signals about whether deeper analysis is warranted.

---

## Notes

**Available metrics from scripts:**
- `valuation.py`: P/E current, P/E 5yr avg, price-EPS correlation, Forward Delta
- `prices.py`: Price changes, volatility (CV), positioning vs 5-yr average
- `earnings.py`: EPS history, CAGR, volatility, consensus comparison

**Context:**
- This is a preliminary filter to identify candidates worth deeper investigation
- Statement analysis (financial_statements.py) is the deep dive
- Sentiment analysis provides additional context after screening

**Remember:** Flexibility is important. Context matters. A weakness in one area may be offset by strength elsewhere. Industry norms vary.

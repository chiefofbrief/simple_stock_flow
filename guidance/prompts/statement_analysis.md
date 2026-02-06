# Role: Financial Statement Analyst

**Objective:** Deep financial statement analysis to assess value drivers, risk factors, and establish baseline for projections. This is fundamental analysis, not an investment decision.

---

## Preparation

**Required Reading:**
- `Stock Analysis Guidelines.md` - Core investment principles and framework

**Available Data:**
- `{TICKER}_statements.md` - Consolidated statement analysis with historical data, statistics, peer comparisons
- `../glossaries/seeds.md` - Interpretation guidance for 8 projection seeds
- `../glossaries/priority_metrics.md` - Interpretation guidance for 13 priority metrics (8 undervaluation + 5 risk)
- `../glossaries/secondary_metrics.md` - Interpretation guidance for 17 secondary metrics

---

## Analysis Framework: Three-Dimension Analysis

Apply this framework to all metrics:

1. **Absolute Level & Peer Positioning**
   - Current value vs. 5-year average - is this typical?
   - How does the target compare to peers?
   - Per glossary, is this level healthy or concerning?

2. **Trends & Divergences**
   - CAGR, slope, recent deltas - improving, stable, or deteriorating?
   - Are peer trends converging or diverging?
   - Are recent changes consistent with historical patterns?

3. **Volatility & Outliers**
   - Is performance consistent or erratic? (Coefficient of variation)
   - Are there outliers? What might they indicate per glossary?
   - How does volatility compare to peers?

---

## Pass 1: Projection Seeds Baseline

Read `../glossaries/seeds.md` and review the **Projection Seeds** section in statements markdown.

Analyze each of the 8 seeds using the three-dimension framework:

### The 8 Projection Seeds:
- **Revenue** - Top-line growth and stability
- **COGS %** - Cost of goods as percentage of revenue
- **SG&A %** - Selling, general, administrative expense percentage
- **R&D %** - Research and development expense percentage
- **D&A** - Depreciation and amortization
- **CapEx** - Capital expenditures
- **Total Debt** - Debt obligations
- **Working Capital Components** - Current assets and liabilities

### Questions to Address:
- What are the baseline patterns for each seed? (5-year average, CAGR, trends, volatility)
- How do patterns compare to peers? (If peer data available)
- Are there concerning patterns or notable changes?
- What do these patterns suggest about the business model and stability?

---

## Pass 2: Undervaluation & Risk Assessment

Read `../glossaries/priority_metrics.md` and review the **Priority Metrics** section in statements markdown.

### Undervaluation Metrics (8 priority metrics)

Analyze using the three-dimension framework:

- **Free Cash Flow** - Actual cash generation vs. what you'd pay for it
- **Operating Cash Flow** - Sustainability of cash generation
- **NCAV (Net Current Asset Value)** - Graham's net-net signal (if positive, strong signal)
- **ROTC % (Return on Total Capital)** - Are assets productive?
- **ROE % (Return on Equity)** - Are returns to shareholders attractive?
- **Operating Leverage** - Potential for growth amplification (fixed cost structure)
- **Revenue (trends)** - Business growth trajectory
- **Operating Margin %** - Core business profitability before financing

### Questions to Address:
- What do these metrics reveal about value generation?
- Are returns attractive relative to capital deployed?
- Is the business generating cash or consuming it?
- What's driving profitability or constraining it?

### Risk Metrics (5 priority metrics)

Analyze using the three-dimension framework:

- **Debt/OCF** - Credit quality and bankruptcy risk indicator (glossary: best single measure)
- **Accruals Gap** - Earnings quality indicator (large gaps signal manipulation risk)
- **OCF/Net Income** - Are earnings converting to cash or accounting fiction?
- **Depreciation & Amortization** - Manipulation detection via peer comparison
- **Working Capital (trends)** - Income statement validation (harder to manipulate than earnings)

### Questions to Address:
- What are the key risk factors?
- Is credit quality strong, adequate, or concerning?
- Are earnings converting to cash?
- Any signals of earnings manipulation or quality issues?
- How does risk compare to peers?

---

## Pass 3: Secondary Metrics (Brief Scan)

Read `../glossaries/secondary_metrics.md` as needed.

Review the 17 secondary metrics grouped by category. Detail only if anomalies warrant investigation.

### Operations Context (4 metrics):
- Gross Margin %, Net Margin %, D&A % of Revenue, D&A % of OCF

### Financial Health Context (8 metrics):
- Debt/Total Assets %, Tangible Equity/Total Assets %, Current Ratio, Quick Ratio, EBIT Coverage, Debt to Tangible Equity, Short-Term Debt % of Current Liabilities, Cash % of Total Assets

### Efficiency Context (5 metrics):
- Receivables vs Revenue Growth, DSO (Days), Inventory vs COGS Growth, Inventory Turnover, Capex/Depreciation

### Questions to Address:
- Are there any notable anomalies or outliers?
- Do any secondary metrics warrant deeper investigation?
- What additional context do they provide?

---

## Pass 4: Synthesis

Provide a comprehensive narrative addressing:

### Value & Risk Assessment
- What do the financial statements reveal about value generation?
- What do they reveal about risk levels?
- What's driving earnings? What's constraining earnings?
- How does the company compare to peers? (If available)

### Investigation Items
Based on the analysis, identify items requiring further investigation:

**From Financial Analysis:**
- What questions does the data raise?
- What patterns need explanation or validation?
- Are there claims in news/sentiment that can be disputed using this data?

**Guidance on Investigation Items:**
- Favor slightly broader categories over overly specific items
- Examples: "review earnings calls", "examine notes to financial statements", "investigate working capital trends"
- Avoid naming specific manipulation techniques unless clearly indicated by the data

**Examples:**
- High inventory buildup → Investigate: Normal lead-time buying or demand weakness?
- Depreciation below peer average → Investigate: Conservative accounting or asset understatement?
- Working capital deterioration → Investigate: Business model shift or cash flow stress?
- Strong cash flow but weak GAAP earnings → Investigate: Intangible investments or temporary timing?

### Context for Decision-Making
- What does the financial picture suggest about the business?
- Where might perception (from sentiment analysis) diverge from financial reality?
- What additional data or research would strengthen the analysis?

---

## Output

**Append to TOP of:** `data/analysis/{TICKER}/{TICKER}_statements.md`

Read the existing file first, then prepend your analysis with a date header separator:

```
---
# STATEMENT ANALYSIS - [DATE]
---

[Your analysis here]

---
```

Then append the existing file content below.

Provide a clear narrative that:
- Applies three-dimension framework systematically
- Addresses what the data shows and why it matters
- Uses glossaries for interpretation guidance
- Compares to peers when available
- Identifies items requiring further investigation
- Looks for opportunities where data disputes or validates external claims

**Flexibility:** Let materiality drive depth. Elaborate on critical items, be brief on standard items. Use evidence from the data.

---

## Notes

**Available Statistical Fields in Statements Markdown:**
- Current, 5-year average, CAGR, slope, recent delta %, coefficient of variation (CV), outliers, YTD annualized

**Remember:**
- This is qualitative interpretation of already-calculated metrics
- Three-dimension framework (absolute/trends/volatility) applies to all metrics
- Peer context adds valuable perspective
- Focus on analysis, not investment decisions
- GAAP vs. economic reality matters (per Stock Analysis Guidelines.md)
- **External Data:** If citing data not from the script outputs, explicitly state the source

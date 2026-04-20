# Financials Analysis Prompt

## Role
You are an expert financial analyst. Your task is to analyze the provided financial statement data for **{TICKER}** and produce a concise, insightful report.

---

## Step 1: Gather Context

### Required Context
Read the following before doing anything else:
- `GEMINI.md` — The foundational Analysis Philosophy & Guidelines.
- `Data/tickers/{TICKER}/{TICKER}_Thesis.md` — The stock's thesis and prior analysis context.
- `Data/tickers/{TICKER}/{TICKER}_financial_analysis.md` — Financial metrics for {TICKER} and any peers. Run: `python Scripts/financials.py {TICKER} --peers {PEER}` (default: 1 peer; 0 or 2 peers are also valid — your call).
- If `{TICKER}` has an `AI SC` Sector Theme (check `Stock_Tracker.md` or `{TICKER}_Thesis.md`), read the relevant layer section of `context_ai_supply_chain.md`.

**STOP. Wait for user approval before proceeding to Step 2.**

---

## Step 2: Analyze & Generate Report

### Analysis Guidelines
- Evaluate the data against the Output Format below.
- All insights must leverage the provided data. Explicitly specify which data points led to your conclusion.
- **Per-metric dimensions:** For each metric in Part A, address: (1) how the current figure compares to historical levels, (2) the long-term trend and volatility (5yr), (3) the short-term trend and volatility (past 4 quarters), and (4) what the Metric Interpretations below indicate about the trend and current value.
- **Peer comparison:** If peer data is provided, compare the target directly against peers within each metric.
- **Reference:** Consult source material summaries (`Source Material/summaries/`) when an item would benefit from additional context, especially as it pertains to fundamental analysis, financial statement analysis, accounting mechanics and gimmicks, options strategies, or reflexivity theory and boom/bust models. Refer to `Source Material/summaries/insights_index.md` for a thematic map. *CRITICAL WARNING: Do not access Source Material/raw/ without explicit user permission to avoid burning compute.*
- **Metric Interpretations:** The section at the bottom of this prompt matches exactly the metrics being analyzed and should serve as your primary source of context for each metric before formulating your analysis.

### Deliverable

**Questions:**
1. **Data Check:** Have all metrics been sourced directly from `{TICKER}_financial_analysis.md` — no outside data introduced?
2. **Peer Check:** If peer data was provided, has each metric in Part A been compared against peers?
3. **Per-Metric Check:** Has each metric been assessed across all four dimensions (current vs. historical, long-term trend, short-term trend, and guidance inference)?
4. **Synthesis Check:** Do the Part B questions draw meaningfully on the per-metric work in Part A?
5. **Summary Check:** Does the Financials Summary accurately reflect the findings?

### Output Format

#### {TICKER} Financial Analysis

**Part A — Metric Analysis**
*For each metric, write a concise paragraph synthesizing the current level, trend, and what the guidance implies. If peer data is provided, compare directly.*

**Revenue**
[Analysis]

**Operating Margin**
[Analysis]

**Operating Cash Flow**
[Analysis]

**Free Cash Flow**
[Analysis]

**OCF / Net Income**
[Analysis]

**Working Capital**
[Analysis]

**Operating Leverage**
[Analysis]

**Capital Expenditures & D&A**
[Analysis]

**Debt Profile**
[Analysis — covers Debt/Total Assets and Debt/OCF]

---

**Part B — Synthesis**

**1. What do revenue growth and operating margins reveal about the health and durability of the core business?**
[Answer]

**2. Do the cash flow metrics confirm or contradict what the income statement shows — and what does that tell us about earnings quality?**
[Answer]

**3. What does the working capital trend reveal about whether growth is self-funding or consuming cash beyond what growth justifies?**
[Answer]

**4. How sensitive is operating income to revenue changes, and what does that imply for risk and upside?**
[Answer]

**5. What do capital expenditures and depreciation reveal about how much the business must reinvest just to maintain its position?**
[Answer]

**6. What does the debt profile tell us about financial risk and the company's ability to service its obligations?**
[Answer]

**7. What do the metrics reveal about the stock's risk and downside?**
[Answer]

**8. What do the metrics reveal about the stock's potential and upside?**
[Answer]

**9. What new questions, concerns, or opportunities do the metrics raise, and which should be investigated further?**
[Answer]

**Financials Summary**
[A concise paragraph summarizing the findings. This text will be copied to the Thesis file.]

- **Action:** Ask: *"Do you approve this analysis? Should I update the Thesis file and Stock Tracker?"*

**STOP. Wait for user approval before proceeding to Step 3.**

---

## Step 3: Commit

Upon explicit user approval:
- Update **### Financials** in `Data/tickers/{TICKER}/{TICKER}_Thesis.md` with the full analysis.
- Update `Stock_Tracker.md` — advance **Current Phase** for `{TICKER}` to the next phase.

**STOP. Wait for user approval before committing.**

---

## Metric Interpretations

1. **Revenue**

**Description**:
Revenue is the foundation of all profitability metrics and the top-line measure of business scale.

**Interpretation**:
- Revenue growth substantially above industry with maintained margins indicates strengthening position; growth above industry with compressing margins suggests buying share through price cuts.
- Companies maintaining price increases through downturns demonstrate pricing power; those forced to cut prices reveal commodity-like competition.
- When revenue declines, distinguish between industry-wide pressure (potentially creating sector-wide opportunity if prices become depressed) versus company-specific weakness indicating loss of competitive position.
- Red flag: Growth substantially outpacing competitors without operational explanation warrants investigation and could signal aggressive accounting.

**Context and Considerations**:
- Revenue growth without margin improvement creates no shareholder value—acceleration alone is meaningless if profit per dollar of sales remains constant or declines.
- Rapid growth attracts competition and rarely persists indefinitely.
- Revenue quality depends on conversion to cash. Monitor the relationship between revenue growth and receivables/inventory growth—significant divergences may indicate revenue is not representing completed economic transactions. See Working Capital metric.
- Contrarian opportunity: Industry-wide revenue decline creating sector-wide price depression when an individual company's competitive position and market share remain intact.

---

2. **Operating Margin (Formula: Operating Income ÷ Revenue × 100)**

**Description**:
Shows management performance before financial structure and taxes—the clearest measure of whether the core business generates durable profit at scale.

**Interpretation**:
- Stable margins over 5-7 years indicate permanence of earning power.
- High margins relative to peers suggest competitive advantages—pricing power, cost advantages, or operational excellence. Such advantages may be sustainable if protected by moats (brand strength, network effects, regulatory barriers, proprietary technology).
- Narrower margins create greater danger—modest adverse changes can quickly produce losses.

**Context and Considerations**:
- Margins well above asset-based returns attract competition; margins below normal may improve as weak competitors exit.
- Confirm management continues investing in the business (see Capital Expenditures). The risk is cutting investment to boost near-term margins while impairing long-term competitiveness through deferred maintenance, reduced R&D, or eliminated advertising.
- Contrarian opportunity: Depressed margins in mature, established companies with solid market positions when driven by temporary factors (one-time charges, transient input cost spikes, short-term demand weakness).

---

3. **Operating Cash Flow**

**Description**:
Measures the actual cash generated by business operations, cutting through accounting discretion to reveal economic reality. Most valuable precisely when income statements are least reliable—in highly leveraged companies, troubled firms, and situations where accounting choices distort reported results.

**Interpretation**:
- Companies can dress up earnings temporarily through accounting choices, but cannot manufacture cash. When income statements and cash flow diverge significantly, it signals either aggressive accounting or deteriorating business fundamentals.
- Strongly positive OCF in mature companies indicates self-funding capability and financial strength.

**Context and Considerations**:
- Contrarian opportunity: Temporarily depressed OCF in fundamentally sound businesses where the divergence from earnings is driven by transient rather than structural factors.

---

4. **Free Cash Flow (Formula: Operating Cash Flow - Capital Expenditures)**

**Description**:
Free cash flow represents the cash an owner can pocket after paying all expenses and making necessary maintenance investments—"the well from which all returns are drawn." It is the ultimate measure of value creation regardless of how that value is deployed (dividends, buybacks, growth investment).

**Interpretation**:
- Consistent FCF generation indicates a self-funding business not dependent on external capital.
- Strong current FCF generation means nothing if the business model is deteriorating or if the company benefited from unsustainable temporary factors.

**Context and Considerations**:
- Self-funding companies avoid painful dependence on external financing. During credit crunches, external financing becomes expensive or unavailable; self-funding companies gain decisive competitive advantage by continuing essential investments while credit-dependent competitors retrench.
- Loss of flexibility feeds on itself: downturn hits → forced choice between cutting profit-enhancing investments or increasing external financing dependence → either path leads to further flexibility loss.
- Contrarian opportunity: Strong FCF generation in out-of-favor companies where the market focuses on reported earnings weakness while ignoring cash generation capacity.

---

5. **OCF / Net Income (Formula: Operating Cash Flow ÷ Net Income)**

**Description**:
Measures earnings quality by comparing reported profits to actual cash collection.

**Interpretation**:
- Ratios consistently near or above 1.0 indicate high-quality earnings backed by cash; ratios substantially below 1.0 reveal gaps between reported profits and cash reality.
- > 1.1: Conservative accounting or efficient working capital management—high quality earnings.
- 0.8 - 1.1: Reasonable earnings quality.
- < 0.8 (especially if deteriorating vs. peers): Earnings significantly exceed cash generation, suggesting potential revenue recognition issues, working capital consumption, or reserve inadequacy.

**Context and Considerations**:
- Contrarian opportunity: In highly leveraged companies, heavy debt loads create large interest expenses that depress net income, yet the company may generate strong cash flow because depreciation provides actual cash available for debt service. Traditional accounting returns can decline while actual cash compounding remains strong—focus on cash generation capacity rather than accounting returns on book equity in these situations.

---

6. **Working Capital (Formula: Current Assets - Current Liabilities)**

**Description**:
Measures the capital employed in day-to-day operations. It tells you how efficiently a company converts its operations into actual cash, and whether growth is self-funding or a cash drain.

**Interpretation**:
- When WC grows faster than revenue (e.g., 30% versus 10%), it indicates cash consumption through deteriorating collection, inventory accumulation, or supplier payment issues—the company is consuming cash beyond what growth justifies.
- Two distinct patterns:
  - Healthy pattern: Payables grow faster than receivables and inventory, meaning vendors' trade credit funds working capital expansion from sales growth. Suppliers are essentially financing the company's growth through trade credit. The company isn't tying up its own cash to fund expansion.
  - Dangerous pattern: Inventory builds disproportionately to sales (goods sitting unsold), while receivables expand (customers paying slowly). This widens the gap between cash needs and supplier financing. It can cascade: deteriorating credit quality causes vendors to tighten terms, which forces the company to seek expensive external financing or cut operations.
- During periods with losses, pattern recognition becomes critical:
  - Favorable: Inventory shrinks faster than losses accumulate, and cash actually improves or payables decline—management is preserving liquidity through the difficult period.
  - Unfavorable: Losses are financed by drawing down cash or piling up current liabilities. Working capital depletes, indicating the company is burning through liquidity concurrent with operational losses.

**Context and Considerations**:
- Growing businesses consume cash building working capital, but working capital as a percentage of sales should remain fairly constant absent business model changes.
- Watch for covenant risk in leveraged companies. Bank agreements often cap total debt. Once a company hits that ceiling, it loses the ability to borrow its way through a rough patch and may be forced to cut investment or operations to stay compliant—potentially at the worst possible time.
- Contrarian opportunity: When the market fixates on near-term earnings weakness, it sometimes ignores a strong working capital position—a liquid, well-managed balance sheet that gives the company staying power through a downturn. That gap between perception and financial reality can be where value hides.

---

7. **Operating Leverage (Formula: % Change in Operating Income ÷ % Change in Revenue)**

**Description**:
Measures how dramatically operating income changes relative to sales volume changes. Reveals both the opportunity for earnings acceleration and the risk of volatility inherent in the fixed-cost structure.

**Interpretation**:
- High operating leverage creates powerful earnings inflection potential. Once fixed costs are covered, each incremental revenue dollar contributes its full margin directly to operating profit—modest sales increases can produce dramatic earnings growth.
- Operating leverage >3× indicates strong earnings sensitivity where revenue growth translates to disproportionate profit growth.
- The same structure that amplifies gains in good times amplifies losses in bad times. When combined with high financial leverage, operating leverage creates particularly severe asymmetric risk—small revenue shortfalls can drive operating income below levels needed to cover interest expense, triggering financial distress.
- Red flag: Operating leverage increasing (rising PP&E %) while revenue growth decelerates.

**Context and Considerations**:
- Contrarian opportunity: Companies with high operating leverage temporarily suffering from low capacity utilization, or businesses with high operating leverage in growing markets—in both cases, the magnification effect works strongly in investors' favor once revenue inflects.

---

8. **Capital Expenditures**

**Description**:
Capex reveals how much cash a business must reinvest just to maintain its competitive position—and how much it's spending to grow.

**Interpretation**:
- The capex/depreciation ratio is a quick lens on capital intensity and growth posture:
  - Ratio <1.0: The company is spending less than its assets are depreciating. This is either an asset-light business model (positive) or underinvestment that will eventually impair competitiveness (negative).
  - Ratio ≈1.0: Maintenance mode. The company is replacing assets roughly as they wear out, consistent with a mature, stable business not in aggressive growth or contraction.
  - Ratio >1.5: Active growth investment beyond replacement. Acceptable, even desirable, if returns on that investment are strong. Concerning if sustained high capex isn't translating into revenue or margin growth.

**Context and Considerations**:
- A business that grows with minimal capex generates far more free cash flow than one that must constantly reinvest to stay competitive. A company spending heavily just to defend its current position (airlines, telecom, utilities) is in a fundamentally different position than one choosing to invest from a position of strength.
- Industry context is essential: software and asset-light business models can scale with minimal incremental capex; manufacturing, energy, and infrastructure businesses require capex roughly proportional to revenue. Cross-industry comparisons are misleading without this adjustment.
- Watch for capex cuts during downturns as a warning sign. Management may be protecting near-term cash flow at the expense of future competitiveness.
- Contrarian opportunity: Companies with a history of high capex transitioning to lower-intensity models (e.g., outsourcing manufacturing, shifting to software/services) may generate a step-change in free cash flow that the market hasn't priced in yet.

---

9. **Depreciation & Amortization**

**Description**:
Non-cash charges that reduce reported earnings but don't require cash outlays in the current period.

**Interpretation**:
- Historical depreciation rate (as % of PP&E) reveals asset intensity:
  - High rates (8-10%) signal an asset-heavy business requiring continuous reinvestment.
  - Low rates (2-3%) indicate an asset-light model with better cash conversion.

**Context and Considerations**:
- For highly leveraged companies, depreciation provides an interest coverage cushion—the company may generate sufficient cash to service debt even when reported earnings appear inadequate. Over the long term, however, companies must replace depreciating assets, so this cushion is temporary.
- Contrarian opportunity: High D&A companies generate more cash than income statements suggest, creating potential hidden value—particularly relevant in leveraged situations.
- Contrarian opportunity: Overly conservative depreciation (rates above peers) understates true earnings; rates materially below peers may signal expense understatement to inflate earnings.
- Key manipulation patterns: writing down assets in bad years to reduce future depreciation, extending useful life assumptions under earnings pressure, and arbitrary year-to-year policy changes with no clear relationship between charges and the property account.

---

10. **Debt / Total Assets (Formula: Total Debt ÷ Total Assets × 100)**

**Description**:
Shows what proportion of the asset base is financed with debt versus equity.

**Interpretation**:
- 30-40%: Moderate leverage—optimal range for many businesses
- Above 60%: High leverage—elevated risk but potential for strong equity returns if well-managed
- Rising ratios indicate leveraging up without corresponding earning power growth, potentially impairing credit quality.

**Context and Considerations**:
- Permanent short-term debt must be included (many borrowers rely on short-term debt that's never actually repaid but rather continuously renewed).
- Convertible debt counts as debt until it's actually converted to equity, not when conversion options exist.
- Contrarian opportunity: Moderate leverage in stable businesses can enhance equity returns without excessive risk.

---

11. **Debt / Operating Cash Flow (Formula: Total Debt ÷ Operating Cash Flow; expressed in years)**

**Description**:
Measures the time required to eliminate all debt if 100% of operating cash flow were dedicated to debt repayment.

**Interpretation**:
- < 3 years: Strong debt service capacity—excellent credit quality, indicates financial strength and capacity for strategic initiatives.
- 3-6 years: Moderate capacity—acceptable for most businesses.
- > 6 years: Weak capacity, elevated default risk.

**Context and Considerations**:
- It's the best single credit quality measure because it's built from two comparatively hard numbers less subject to manipulation than earnings-based metrics. For example, under-depreciation merely moves money between pockets without affecting cash flow. A company with $60M debt and $20M OCF could retire debt in 3 years—clearly more flexible than $80M debt with $10M OCF requiring 8 years.
- Ratio rising due to OCF decline rather than debt increase signals operational deterioration rather than strategic leverage increase.

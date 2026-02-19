
We are updating our workflow. You are not permitted to make any edits to files without my written approval. Any old files should be archived, not deleted (unless we are just moving them). Review my instructions carefully at all times, and never assume or hallucinate or use your own knowledge unless you ask first; always rely on my instructions and our source material. All new files will go in the folder WORKFLOW v1. 

Here is what we have done thus far; review the list of completed tasks below, and standby for instructions: 
   1. Workflow V1 Setup: Created WORKFLOW v1 directory structure.
   2. Script Migration: Moved peters_digest.py, price.py, earnings.py, shared_utils.py and all digest scripts to WORKFLOW v1/Scripts/.
   3. Path Updates: Updated peters_digest.py to point to the new location of digest scripts and save output to WORKFLOW v1/Peter's Digest/. Updated docs/COMMANDS.md.
   4. Prompt Creation: Created WORKFLOW v1/Prompts/price_analysis_prompt.md.
   5. Execution: Ran Peter's Digest for today.
   6. Analysis: Generated and prepended the market analysis to the daily digest file.
   7. Git Sync: Pushed all changes to the remote repository.
   8. Stock Tracker Update: Added "Earnings/Valuation Analysis" section to WORKFLOW v1/Stock Tracker.md.
   9. Earnings Prompt: Created WORKFLOW v1/Prompts/earnings_analysis_prompt.md with specific analysis questions and data inputs.
   10. Financials Script: Created WORKFLOW v1/Scripts/financials.py to fetch FMP data (Annual & Quarterly), calculate Earnings Risk, Quality, and ROI metrics, and generate detailed
       markdown reports with statistical analysis (CAGR, CV, Deltas).
   11. Script Validation: Verified financials.py accuracy against AAPL SEC filings and confirmed manual TTM calculation logic.
   12. Tracker Enhancements: Added "Earnings Risk", "Earnings Quality", and "ROI" subsections to WORKFLOW v1/Stock Tracker.md.
   13. Script Update (Quarterly Data): Enhanced financials.py to output "Recent Quarterly Trends" (last 4 quarters + deltas) alongside the annual data tables.
   14. Script Testing: Verified the enhanced financials.py output with AAPL.
   15. Metrics Prompts: Created WORKFLOW v1/Prompts/earnings_risk_prompt.md, earnings_quality_prompt.md, and roi_prompt.md with interchangeable roles and specific metrics.

Let's create WORKFLOW v1/financials_glossary.md to define key terms and interpretation guidelines referenced in the new prompts. The glossary should include the following metrics, all of which are in the financials script and are addressed in the prompts:
1. earnings risk:
   -  Debt / Total Assets: [Debt = S]
   -  Debt / Operating Cash Flow: [P]
   -  NCAV (Net Current Asset Value): [P]
   -  Accruals Gap: [P]
   -  CapEx: [S]
   -  Depreciation & Amortization: [P, S]
   -  Working Capital: [P]
2. earnings quality:
    - Revenue: [P, S]
    - Operating Margin: [P]
    - Operating Cash Flow: [P]
    - Free Cash Flow: [P]
    - OCF / Net Income: [P]
3. roi:
    - ROTC (Return on Total Capital): [P]
    - ROE (Return on Equity): [P]
    - Operating Leverage: [P]
  
Let's structure the glossary in 3 primary sections that correspond to the sections above. For items with 'S' in brackets, include '[Seed]' next to its title (you don't need to know what this means and it need not be explained; it's just for me to have for reference). Let's start with the earnings risk section; here is what to include for each item:

1. **Debt / Total Assets (Formula: Total Debt ÷ Total Assets × 100)**

**Description**: 
Shows what proportion of the asset base is financed with debt versus equity, revealing the company's capital structure and financial risk profile.

**Interpretation**:
- 30-40%: Moderate leverage—optimal range for many businesses
- > 60%: High leverage—elevated risk but potential for strong equity returns if well-managed
- Rising ratios indicate leveraging up without corresponding earning power growth, potentially impairing credit quality

**Context and Considerations**:
- Permanent short-term debt must be included (many borrowers rely on short-term debt that's never actually repaid but rather continuously renewed).
- Convertible debt counts as debt until it's actually converted to equity, not when conversion options exist.
- Moderate leverage in stable businesses can enhance equity returns without excessive risk.

2. **Debt / Operating Cash Flow (Formula: Total Debt ÷ Operating Cash Flow; expressed in years)**

**Description**:
Measures the time required to eliminate all debt if 100% of operating cash flow were dedicated to debt repayment. 

**Interpretation**:
- < 3 years: Strong debt service capacity—excellent credit quality, indicate financial strength and capacity for strategic initiatives.
- 3-6 years: Moderate capacity—acceptable for most businesses
- > 6 years: Weak capacity, elevated default risk

**Context and Considerations**:
- It's the best single credit quality measure because it's built from two comparatively hard numbers less subject to manipulation than earnings-based metrics.
      - For example, under-depreciation, a common earnings manipulation technique, merely moves money between pockets without affecting cash flow. The ratio literally shows: company with $60M debt and $20M OCF could liquidate debt in 3 years dedicating 100% of flow—clearly more flexible than $80M debt with $10M flow needing 8 years.
-  Ratio rising due to OCF decline rather than debt increase is a bad sign (signals operational deterioration rather than strategic leverage increase).

3. **NCAV (Net Current Asset Value) (Formula: Current Assets - Total Liabilities)**

**Description**:
Represents current assets minus all liabilities and senior claims, providing a rough liquidation value measure.

**Interpretation**:
- Market cap < NCAV: Extraordinary bargain—market values entire business below liquid assets
- Market cap near NCAV (within 20-30%): Potential bargain worth investigating—minimal premium for fixed assets and ongoing operations
- Market cap at 2-3× NCAV: May still be attractive if assets undervalued and earning power improving

**Context and Considerations**:
- When market cap persistently trades below NCAV, one of two things must be true: (1) the price is too low—an exceptional bargain, or (2) the company should be liquidated. When a company's market capitalization trades at or below NCAV, the market is valuing the entire business at less than its liquid assets alone, assigning zero or negative value to all fixed assets, intangibles, and ongoing business operations.

4. **Accruals Gap (Formula: (Net Income - Operating Cash Flow) ÷ Total Assets × 100)**

**Description**:
Measures the difference between reported earnings and operating cash flow, scaled by total assets.

**Interpretation**:
- > 3% of assets (or growing while peers remain stable): Earnings exceed cash generation materially, requiring investigation
- Small or near-zero: Minimal difference between earnings and cash suggests high earnings quality
- Negative (cash flow exceeds earnings): Negative accruals (cash flow exceeding earnings) in growing businesses indicate very high quality earnings—company may be conservative in revenue recognition or collecting cash before recognizing revenue.

**Context and Considerations**:
- Large positive gaps indicate significant differences between accounting profits and cash reality.
- Adding working capital changes to cash flow analysis frequently reveals problems not apparent from EBITDA or net income trends alone. Reported earnings often exceed true economic profits specifically through gambits involving inventories or receivables—delayed write-offs, premature revenue recognition, inadequate reserves. Amount of working capital needed represents fairly constant percentage of sales, so material increases in inventories or receivables as percentage of sales is red flag that accruals gap will detect.

5. **Capital Expenditures**

**Description**:
reveals how much cash a business must reinvest just to maintain its competitive position — and how much it's spending to grow. 

**Interpretation**:
- The capex/depreciation ratio is a quick lens on capital intensity and growth posture:
      - Ratio <1.0: The company is spending less than its assets are depreciating. This is either an asset-light business model (positive) or underinvestment that will eventually impair competitiveness (negative). 
      - Ratio ≈1.0: Maintenance mode. The company is replacing assets roughly as they wear out, consistent with a mature, stable business not in aggressive growth or contraction.
      - Ratio >1.5: Active growth investment beyond replacement. Acceptable, even desirable, if returns on that investment are strong. Concerning if sustained high capex isn't translating into revenue or margin growth.

**Context and Considerations**:
- A business that grows with minimal capex generates far more free cash flow than one that must constantly reinvest to stay competitive.
- A company that must spend heavily just to defend its current position (airlines, telecom, utilities) is in a fundamentally different position than one choosing to invest from a position of strength.
- Industry context is essential: software and asset-light business models can scale with minimal incremental capex; manufacturing, energy, and infrastructure businesses require capex roughly proportional to revenue. Cross-industry comparisons are misleading without this adjustment.
- Watch for capex cuts during downturns as a warning sign. Management may be protecting near-term cash flow at the expense of future competitiveness.
- Contrarian opportunity: Companies with a history of high capex that are transitioning to lower-intensity models (e.g., outsourcing manufacturing, shifting to software/services) may generate a step-change in free cash flow that the market hasn't priced in yet.

6. **Depreciation & Amortization**

**Description**:
Represent non-cash charges that reduce reported earnings but don't require cash outlays in the current period. 

**Interpretation**:
- Historical depreciation rate (as % of PP&E) reveals asset intensity:
      - High rates (8-10%) signal asset-heavy business requiring continuous reinvestment. 
      - Low rates (2-3%) indicate asset-light model with better cash conversion. 

**Context and Considerations**:
- The gap between reported earnings and cash generation is particularly important for assessing highly leveraged companies and detecting accounting manipulation. For highly leveraged companies, depreciation provides an interest coverage cushion—the company may generate sufficient cash to service debt even when reported earnings appear inadequate. This non-cash nature means actual cash available exceeds what income statements suggest. However, over the long term, companies must replace depreciating assets, so this cushion is temporary.
- Companies showing materially lower depreciation rates than peers may be understating expenses to inflate earnings.
- Write-down schemes involve management writing down assets in bad years to reduce future depreciation, manufacturing higher future earnings through accounting rather than operations.
- Companies extending useful lives when under earnings pressure signal potential manipulation.
- Lack of depreciation policy disclosure, arbitrary year-to-year changes, or no clear relationship between charges and property account size are all red flags.
- High D&A companies generate more cash than income statements suggest—particularly valuable in leveraged situations
- Overly conservative depreciation (rates above peers) understates true earnings, creating hidden value
- Historical capex/depreciation relationship shows growth trajectory: capex consistently exceeding depreciation by wide margin indicates growth requiring external funding; capex approximating depreciation signals self-funding maturity.
- New asset additions generate future depreciation based on useful lives and methods
- Changes to useful life assumptions or depreciation methods; verify consistency with historical policy

7. **Working Capital (Formula: Current Assets - Current Liabilities)**

**Description**:
Measures the capital employed in day-to-day operation. It tells you how efficiently a company converts its operations into actual cash, and whether growth is self-funding or a cash drain.

**Interpretation**:
- When WC grows faster than revenue (e.g., 30% versus 10%), it indicates cash consumption through deteriorating collection, inventory accumulation, or supplier payment issues. in other words, the company is consuming cash beyond what growth justifies. 
- Two distinct patterns:
       - Healthy pattern: Payables grow faster than receivables and inventory, meaning vendors' trade credit funds working capital expansion from sales growth. Suppliers are essentially financing the company's growth through trade credit. The company isn't tying up its own cash to fund expansion.
       - Dangerous pattern: Inventory builds disproportionately to sales (goods sitting unsold), while receivables expand (customers paying slowly). This widens the gap between cash needs and supplier financing. It can cascade: deteriorating credit quality causes vendors to tighten terms, which forces the company to seek expensive external financing or cut operations.
- During periods with losses, pattern recognition becomes critical:
      - Favorable: Inventory shrinks faster than losses accumulate, and cash actually improves or payables decline. Current-asset value is maintained while cash-asset position improves—management is preserving liquidity.
      - Unfavorable: Losses are financed by drawing down cash or piling up current liabilities. Working capital depletes, indicating the company is burning through liquidity concurrent with operational losses.

**Context and Considerations**:
- Growing businesses consume cash building working capital, but working capital as percentage of sales should remain fairly constant absent business model changes.
- Watch for covenant risk in leveraged companies. Bank agreements often cap total debt. Once a company hits that ceiling, it loses the ability to borrow its way through a rough patch and may be forced to cut investment or operations to stay compliant — potentially at the worst possible time.
- The contrarian opportunity: When the market fixates on near-term earnings weakness, it sometimes ignores a strong working capital position — a liquid, well-managed balance sheet that gives the company staying power through a downturn. That gap between perception and financial reality can be where value hides.

---------------------------------

1. earnings risk:
   -  Debt / Total Assets: [Debt = S]
   -  Debt / Operating Cash Flow: [P]
   -  NCAV (Net Current Asset Value): [P]
   -  Accruals Gap: [P]
   -  CapEx: [S]
   -  Depreciation & Amortization: [P, S]
   -  Working Capital: [P]
2. earnings quality:
    - Revenue: [P, S]
    - Operating Margin: [P]
    - Operating Cash Flow: [P]
    - Free Cash Flow: [P]
    - OCF / Net Income: [P]
3. roi:
    - ROTC (Return on Total Capital): [P]
    - ROE (Return on Equity): [P]
    - Operating Leverage: [P]


**PROCESS:**

**Quant Analysis:**
1. price.
2. earnings.
3. earnings risk:
   -  Debt / Total Assets: [Debt = S]
   -  Debt / Operating Cash Flow: [P]
   -  NCAV (Net Current Asset Value): [P]
   -  Accruals Gap: [P]
   -  CapEx: [S]
   -  Depreciation & Amortization: [P, S]
   -  Working Capital: [P]
4. earnings quality:
    - Revenue: [P, S]
    - Operating Margin: [P]
    - Operating Cash Flow: [P]
    - Free Cash Flow: [P]
    - OCF / Net Income: [P]
5. roi:
    - ROTC (Return on Total Capital): [P]
    - ROE (Return on Equity): [P]
    - Operating Leverage: [P]

**Qual Analysis**:
1. external sentiment (news and social media):
    - What are "authoratative" sources saying about the stock?
    - What is social media saying about the stock?
    - Are there particular catalysts/events that are driving sentiment?
    - Does our quantiative analysis support or reject the prevailing sentiment?
2. internal sentiment (earnings calls):
    - What are analysts paying attention to?
    - What narrative is management trying to push?
    - Does internal sentiment align with external sentiment?
4. Notes (financial statments) / MD&A:
    - What do the filings reveal about questions/concerns raised by prior analyses?
    - Do the filings align with prior analyses, or are there areas of divergence?
    - Are there risks that were not identified in prior analyses?


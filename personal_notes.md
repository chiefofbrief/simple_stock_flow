
We are updating our workflow. You are not permitted to make any edits to files without my written approval. Any old files should be archived, not deleted (unless we are just moving them). Review my instructions carefully at all times, and never assume or hallucinate or use your own knowledge unless you ask first; always rely on my instructions and our source material. All new files will go in the folder WORKFLOW v1. Here is what we have done thus far: 
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
  Next Step:
   16. Glossary Creation: Create WORKFLOW v1/financials_glossary.md to define key terms and interpretation guidelines referenced in the new prompts.

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


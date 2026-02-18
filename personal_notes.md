
We are updating our workflow. You are not permitted to make any edits to files without my written approval. Any old files should be archived, not deleted (unless we are just moving them). Review my instructions carefully at all times, and never assume or hallucinate or use your own knowledge unless you ask first; always rely on my instructions and our source material. All new files will go in the folder WORKFLOW v1. Here is what we did yesterday: 
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

Let's start by creating a section in the Stock Tracker file called Earnings/Valuation Analysis. This will be the second section after price analysis. 

Now, we will work on the new earnings analysis prompt. Review the price_analysis prompt for context; the earnings prompt should follow a similar format. The earnings script alreads provides the data exaclty as we need it; the job of the prompt is analysis. Our focus is on these questions; the analysis should explicitly answer each of these questions concisely:
  - How does the current P/E ratio compare to historical levels?
  - What is the long-term earnings trend and volatility? (past 5 years)
  - What is the short-term earnings trend and volatility? (past 12 months)
  - What is the correlation between price and earnings?
  - How do the upcoming earnings estimates compare to the company’s past performance?
  - FOR LOSERS ONLY:
      - Are earnings decreasing along with the price?
   
the prompt should be created inside the prompts folder inside workflow v1. again, the structure should mirror that of the price analysis prompt. 

next, we will break the financial statement analysis into 3 smaller analyses, all 3 of which will occur in this order following earnings analysis. These are 3 separate steps, but they all leverage the same data:
  1. earnings risk.
  2. earnings quality.
  3. roi.

This is the workflow: Use one script to fetch the financial statement data (income statement, cash flow, balance sheet) using FMP's API. Save each statement as JSON (raw data), and create an aggregated JSON file with the metrics we want. We can also create a markdown file/txt file to view the output as we do now in the old script. Then, use one to three prompts for analysis (we can have one prompt that gets re-used for all 3 analyses since they largely share the same guidance, one prompts with 3 passes, or one prompt for each analysis). Don't worry about the prompts now, we will address that later.

We need to create a new script for this updated structure. We also need the new script to switch from Alphavantage to the FMP API as the data source. These changes, while significant, may not be as large as you think; most, if not all the metrics we want to review in these analyses are probably included in the old scripts (fetch_financials, calc_metrics, calc_seeds, financial_statements, etc.). The old scripts also do a great job of calculating metrics and presenting the data, so it's more a task of taking the components and remixing/tweaking them, rather than building from scratch (although we must create a new script, not change the old ones). 

Here are the metrics we want to include for each section; if you have any uncertainty about the calculation, refer to the glossaries (primary metrics glossary, seed glossary):
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

Let's start by reviewing the old scripts to see if/where we currently fetch/tabulate all of these metrics. After that is established, we can determine how to create the new script.  


Our first main deliverable will be the new price prompt. The price script alreads provides the data exaclty as we need it; the job of the prompt is analysis. Our focus is on these questions; the analysis should explicitly answer each of these questions concisely: 
   - How does the current price compare to historical levels?
   - What is the long-term price trend and volatility? (past 5 years)
   - What is the short-term price trend and volatility? (past 12 months)
   - FOR LOSERS ONLY:
        - How does the current price drop compare to the biggest drawdowns in the stock's history?
        - What is the delta between the current price and its average over the past 12 months?

The objective of the price analysis is to understand if the current price is low/normal/high, and in the case of losers, if the price drop is an anomaly (or if it's part of the stock's normal volatility or a larger downward trend). In addition to answering the questions above, the analysis should also produce a 'price summary' which concisely articulates the findings from each question (if insightful). After the analysis has been completed for all stocks/tickers, the price summaries for approved stocks should be copied and pasted into the STOCK TRACKER file in the Price Analaysis section.  




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



**screening prompts:**
- we have completed the script updates fr our screening phase. we have two scripts, price and earnings.
- now we need to make two prompts, one for price, and the other for earnings (really the second is price and eanrings, kind of a holistic thing). the price prompt will be used after running the price script. the earnings prompt will be used after running the earnings script. both prompts will rely on/use the script outputs as their primary input.
- the prompts can be relatively simple; the output from the scripts is already strcutured in such a way that they 'feed' the llm the data we care about in an easy-to-digest fashion.
- for price, these are our primary questions; the output is already well-formatted to answer these questions: "How does the current price compare to historical levels?" — The vs1Y–vs5Y columns, 52w position, CAGR, and reversion upside tell this story. Is the stock actually cheap, or just cheaper than a recent peak? "How volatile is the price?" — CV, z-score, and drop/max drawdown. A 20% drop in a stock with 0.15 CV is a different signal than a 20% drop in a stock with 0.50 CV. Losers — additional question: "How does the recent drop compare to historical drops and volatility?" 
- questions for earnings: 1) What is the earnings trend and volatility; 2) How do recent earnings compare to earnings estimates by analysts?; 3) What is the relationhsip between price and earnings?
- these questions should be answered for each ticker an appended/prepended to the txt file ouput. the answers should be 1-2 sentences each. the answers should be copied and pasted over to the session notes as subsections/bullets under each ticker in the screening list (once we move to the deeper analyses like sentinment or ststaments we make a file for the ticker, but until then all context should be saved in session notes).
- what questions do you propose for price and earnings? Perhaps you can do a better job of phrasing my questions, but now you know what I care about and why the output is designed as it is. 

let's discuss all these updates prior to implementation. 


**additional screening items:**
- we have successfuly updated the price and earnings scripts, as well as the daily digest. our screening phase is almost ready for deployment in its new form. however, we have a coupld more items to address.
- first, what is the usage/behavior of the price/earnings scripts with regard to tickers/commands? Do they accept tickers in the command line? Is there a limit on the number of tickers for either (I wouldn't do more than 20 at a time most likely but just asking).
- does either script allow, or defualt to, capturing tickers from the session notes in the screening list)? I think the price script may have something, but not sure. If not, how can we implement this while also preserving the ability to manually enter tickers? A wrapper? To be clear, I am asking to have a script that captures the tickers from the screening list in session notes file, and runs them. let's think about how to do this.
- i would like to include concise answers to our critical 2-3 questions for price and earnings in the session notes post-analysis. we can discuss formatting, and how we should design the prompts to do this (we will have two promppts, one for price analysis and the other for price and earnings analysis). these will likely replace the current screening prompt (which will be archived). we may also need to update the session notes structure to reflect this multi-pass approach (maybe, it maye have already been updated). 

for now, let's focus on the items other than the prompts; we'll return to those.


**Peter's Digest:**
- did we implement vector search for ai news? Or just boolean? (check ai_news script)
- can we add prominent section headers for each source? and clear breaks between section? Review the format of the last 2 daily digests for context. This is a nice to have, not a need to have; only implement if it doesn't take a lot of work.
- for some reason, the date is correct sometimes, and sometimes it isn't. for example, it will call 2-13 digest 2-14. an idea why?

**Screening:**
- review SCREENING_PROCESS.md to understand the updates we are making.
- I completed the price section, but looking at it again, I have a concern: It does not capture the recent trend. The screening_process doc may be outdated, so review the price script to see if it matches the notes in the screening doc. If yes, let's discuss how to address my concerns.
- We have not made modifications to the earnings script. Once we have finished up with price, we will move onto this. The three main questions that i'd like to answer:
- -- 1) What is the earnings trend and volatility;
- -- 2) How do recent earnings compare to earnings estimates by analysts (e.g., consensus estimated EPS for next quarter)? This question is essentialy asking: What is the delta between what they have done in the past and what they are expected to do?
- -- 3) What is the relationhsip between price and earnings? this question is simple but has big implications: if they are detached, there may be an opportunity for sentiment arbitrage (earnings are trending up, but price is flat/down); if they are corrleated, it can still be a positive signal, or confirmaiton of why the price is dropping (both price and eanrings on a downtrend). I don't think the 'metrics' in the screening_process.md file properly capture these questions, and we can use them as inputs but do not have to follow them; look at the price script to see how it handled comparisons and you will see what I mean. And of course, the P/E ratio and P/E ratio trend is part of this. 
- for both price and earnings in the previous drafts of the scripts and data, we were capturing both recent (past 12 months, past 4 quarters) and long-term trends (past 5 years). we have not done the same in our updated price script I believe, or in the plan this far for earnings. you can review the Daily_Screening_2026-02-11.txt to see what I am referring to if you'd like. Let's discuss if/how the recen trend may make sense to incorporate. 
- Will the P/E (which is just the tabluation of the price and eanrings, not a separate API call) be included in the earnings script? If Yes, how? Will the script look at the already fetched price data to arrive at P/E? What trends/comparisons do we want to make for P/E?
- In my opinion, some standardization across price, earnings, and P/E would be beneficial for comparisons where applicable. For example, we should probably have P/E time period comparisons match earnings, which should match price where possible. the price analysis is its own step and can be detached from the earnings step, but having totally different sets of metrics and time periods may be confusing. 


**PROCESS:**
1. price.
2. earnings.
3. earnings risk:
   -  Debt: [S]
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
5. ROI
    - ROTC (Return on Total Capital): [P]
    - ROE (Return on Equity): [P]
    - Operating Leverage: [P]

  


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


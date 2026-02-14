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


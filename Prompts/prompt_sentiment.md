# Context Configuration
- **Target Ticker:** {TICKER}
- **Required Data:** `Data/tickers/{TICKER}/{TICKER}_sentiment.md` (Run: `python Scripts/sentiment.py {TICKER} --all`)
- **Required Context:** 
    - Analysis Philosophy & Guidelines (`GEMINI.md`)
    - Screening Context (`Data/tickers/{TICKER}/{TICKER}_Thesis.md`)
    - Financials Analysis (from `Data/tickers/{TICKER}/{TICKER}_Thesis.md`)
    - For [AI]-tagged tickers ONLY: `AI_Guidelines.md`
- **Output:**
    - Update **DEEP DIVE > Sentiment** in `Data/tickers/{TICKER}/{TICKER}_Thesis.md` with the full analysis.
    - Update **THESIS > Synthesis & Recommendation** in `Data/tickers/{TICKER}/{TICKER}_Thesis.md` with a refined synthesis.
    - Append concise summary to `Stock_Tracker.md` under `### {TICKER} > **Sentiment**`.

# Sentiment Analysis Prompt

## Role
You are an expert financial analyst. Your task is to analyze the provided news and social media data to produce a concise, insightful report on the market's perception of the stock.

## Input Data
You will be provided with:
1.  **Ticker Symbol**: The stock symbol.
2.  **News Headlines & Summaries**: Recent news articles from major financial outlets, including dates and sources.
3.  **Social Media Content**: Trending posts and discussions from platforms like Reddit, TikTok, and YouTube.

## Analysis Guidelines

Analyze the data to answer the following questions. **Crucially, all insights must derive from the provided news and social media content. Your answers must be insightful, explicitly explaining the "why" behind the findings rather than simply stating the sentiment. You must explicitly reference specific articles, posts, or trends that support your conclusions.**

*   **Reference:** Consult source material summaries (`Source Material/summaries/`) when an item would benefit from additional context, especially as it pertains to fundamental analysis, financial statement analysis, accounting mechanics and gimmicks, options strategies, or reflexivity theory and boom/bust models. Refer to `Source Material/summaries/insights_index.md` for a thematic map. CRITICAL WARNING:* Do not access Source Material/raw/ without explicit user permission to avoid burning compute.

## Output Format

Please structure your response exactly as follows:

### {TICKER} Sentiment Analysis

**1. What are major news outlets saying about the stock?**
[Answer using specific source content]

**2. What is social media saying about the stock?**
[Answer using specific source content]

**3. Is sentiment improving, deteriorating, or stable over the lookback period?**
[Answer using specific source content]

**4. Are there identifiable catalysts driving sentiment — and are they forward or backward looking?**
[Answer using specific source content]

**5. Does sentiment align with our financial analysis, or are there significant divergences and concerns warranting further investigation?**
[Answer using specific source content]

---
**Thesis Update (Section: Synthesis & Recommendation)**
[Propose an update to the thesis based on the sentiment analysis. Synthesize how this new evidence shifts, supports, or challenges the existing thesis. Include a PASS/FILTERED recommendation for this step.]

---
**Sentiment Summary**
[A concise paragraph summarizing the findings. This text will be copied to the Stock Tracker.]

---
**Instructions for the Assistant:**
1. **Wait for Approval:** Present this complete analysis and the proposed Thesis update to the user.
2. **Explicit Ask:** You **MUST** ask: *"Do you approve these updates and the recommendation to [PASS/FILTER]? Should I update the Thesis file and Stock Tracker?"*
3. **Write on Approval:** Only write the analysis and summary to the files after the user gives explicit approval.

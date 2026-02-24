# Context Configuration
- **Target Ticker:** {TICKER}
- **Required Data:** `Data/tickers/{TICKER}/{TICKER}_sentiment.md` (Run: `python scripts/sentiment.py {TICKER}`)
- **Required Context:** 
    - Financials Analysis (from `Data/tickers/{TICKER}/{TICKER}_Thesis.md`)
    - `Discovery_Context.md` (Read to see if it mentions why the stock is being screened)
    - For [AI]-tagged tickers ONLY: `AI_Guidelines.md`
- **Output:**
    - Append full analysis to `Data/tickers/{TICKER}/{TICKER}_Thesis.md` under `## Sentiment`.
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

Analyze the data to answer the following questions. **Crucially, all insights must derive from the provided news and social media content. You must explicitly reference specific articles, posts, or trends that support your conclusions.**

*   **Reference:** Consult the "Analysis Philosophy & Guidelines" and "Source Material" sections in your system instructions (`Gemini.md`) for additional context or analytical frameworks if needed.

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
**Sentiment Summary**
[A concise paragraph summarizing the findings. This text will be copied to the Stock Tracker.]

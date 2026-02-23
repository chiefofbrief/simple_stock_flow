# Context Configuration
- **Target Ticker:** {TICKER}
- **Required Data:** `data/tickers/{TICKER}/{TICKER}_earnings_calls.md` (Run: `python scripts/earnings_calls.py {TICKER}`)
- **Required Context:** 
    - Financials, Sentiment, Footnotes (from `data/tickers/{TICKER}/{TICKER}_Research_Thesis.md`)
    - For [AI]-tagged tickers ONLY: `AI_Guidelines.md`
- **Output:**
    - Append full analysis to `data/tickers/{TICKER}/{TICKER}_Research_Thesis.md` under `## Earnings Calls`.
    - Append concise summary to `data/screening/Tracker.md` under `### {TICKER} > **Earnings Calls**`.

# Earnings Call Analysis Prompt

## Role
You are an expert financial analyst. Your task is to analyze the provided earnings call transcript and produce a concise, insightful report.

## Input Data
You will be provided with:
1.  **Ticker Symbol**: The stock symbol.
2.  **Earnings Call Transcript**: Text content of the management discussion and Q&A session.
3.  **Previous Analyses**: Key findings from prior financial and sentiment analyses to compare against.

## Analysis Guidelines

Analyze the data to answer the following questions. **Crucially, all insights must leverage the provided transcript. You must explicitly cite specific statements or excerpts that led to your conclusion.**

*   **Reference:** Consult the "Analysis Philosophy & Guidelines" and "Source Material" sections in your system instructions (`Gemini.md`) for additional context or analytical frameworks if needed.

## Output Format

Please structure your response exactly as follows:

### {TICKER} Earnings Call Analysis

**1. Does management's characterization of the business align with previous analyses — or are there notable deflections, omissions, or contradictions?**
[Answer using specific excerpts or citations from the transcript]

**2. Are there any explanations that add meaningful context to specific findings from the previous analyses?**
[Answer using specific excerpts or citations from the transcript]

**3. Has management's language or tone shifted relative to the prior call — increased hedging, new risk disclosures, or topics that have quietly disappeared from discussion?**
[Answer using specific excerpts or citations from the transcript]

**4. What are analysts concerned or excited about?**
[Answer using specific excerpts or citations from the transcript]

**5. How do analysts' focus areas align with our previous analyses?**
[Answer using specific excerpts or citations from the transcript]

---
**Earnings Call Summary**
[A concise paragraph summarizing the findings. This text will be copied to the Stock Tracker.]

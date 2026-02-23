# Context Configuration
- **Target Ticker:** {TICKER}
- **Required Data:** `data/tickers/{TICKER}/{TICKER}_notes_mda.md` (Run: `python scripts/footnotes.py {TICKER}`)
- **Required Context:** 
    - Financials, Sentiment (from `data/tickers/{TICKER}/{TICKER}_Research_Thesis.md`)
    - For [AI]-tagged tickers ONLY: `AI_Guidelines.md`
- **Output:**
    - Append full analysis to `data/tickers/{TICKER}/{TICKER}_Research_Thesis.md` under `## Footnotes`.
    - Append concise summary to `data/screening/Tracker.md` under `### {TICKER} > **Footnotes**`.

# Footnotes & MD&A Analysis Prompt

## Role
You are an expert financial analyst. Your task is to analyze the provided Footnotes and Management's Discussion and Analysis (MD&A) from the company's financial reports.

## Input Data
You will be provided with:
1.  **Ticker Symbol**: The stock symbol.
2.  **MD&A / Footnotes Content**: Text excerpts or summaries from the 10-K/10-Q filings.
3.  **Financials & Sentiment Context**: Key findings from the previously generated financial and sentiment analyses. You must read and utilize this context to inform your analysis of the footnotes.

## Analysis Guidelines

Analyze the text to answer the following questions. **Crucially, all insights must leverage the provided text.**

*   **Reference:** Consult the "Analysis Philosophy & Guidelines" and "Source Material" sections in your system instructions (`Gemini.md`) for additional context or analytical frameworks if needed.

## Output Format

Please structure your response exactly as follows:

### {TICKER} Footnotes & MD&A Analysis

**1. Do the footnotes/MD&A reveal anything material not captured in the financial statements?**
[Answer using specific details from the text]

**2. Do the footnotes/MD&A add any meaningful context to the sentiment analysis?**
[Answer using specific details from the text]

**3. If there is negative sentiment or concerns, do the footnotes/MD&A alleviate or heighten those concerns?**
[Answer using specific details from the text]

**4. If there is positive sentiment or opportunities, do the footnotes/MD&A support or undermine them?**
[Answer using specific details from the text]

**5. Are there any disclosures that appear incomplete, inconsistent with the financial statements, or that warrant deeper investigation?**
[Answer using specific details from the text]

---
**Footnotes & MD&A Summary**
[A concise paragraph summarizing the findings. This text will be copied to the Stock Tracker.]

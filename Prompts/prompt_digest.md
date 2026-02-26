# Context Configuration
- **Target Ticker:** All tickers/themes in the Daily Digest
- **Required Data:** `Peter's Digest/Daily_Digest_{DATE}.md`
- **Required Context:** Analysis Philosophy & Guidelines (`GEMINI.md`)
- **Output:** Prepend analysis to the top of `Peter's Digest/Daily_Digest_{DATE}.md` (below the main "Peter's Digest" header).

# Role: Expert Financial Analyst
**Objective:** Synthesize news data into actionable investment flags by applying the "Analysis Philosophy & Guidelines" framework. Scan the data to identify high-conviction "leads," but do not perform a full analysis (Focus on "Why this warrants your time" rather than "The final verdict").

## Data Intake
Before beginning any analysis, read **every** headline and post title within the provided Peter's Digest file. Ensure no data point is skipped or overlooked.

## Framework
Use the guidelines in your system instructions (`GEMINI.md`) as your primary framework for interpreting market events.
*   **Standard analysis:** Use the "Analysis Philosophy & Guidelines" for all standard analysis.
*   **AI sector:** Consult `AI_Guidelines.md` when analyzing stocks within the AI value chain.

## The Analysis
*Prepend this analysis to the **top** of the generated Daily Digest file (below the main "Peter's Digest" header).*

The analysis must begin with the title:
## Stock & Markets Analysis

### 1. Market & Macro Overview
Briefly set the scene using the market context guidelines.
*   **Indicators:** Note significant moves in Gold/Commodities, Treasury Yields, and Economic Data (Inflation, Sentiment, etc.).
*   **Sentiment:** Characterize current market sentiment based on the data. Let the data drive the characterization.

### 2. General Stock News Analysis
Analyze the intake data through the lens of the Analysis Philosophy, focusing on identifying divergence rather than consensus.
*   **Narrative vs. Reality:** Note the facts, but don't accept explanations at face value. Market narratives often rationalize price movements after the fact. Consider alternative explanations.
*   **Edge Opportunities:** Look for claims in news coverage that might be disputed or validated using financial statements or research—where perception may diverge from reality.

### 3. AI Ecosystem Positioning (Sector-Specific)
For AI-related news, apply `AI_Guidelines.md` to identify relevant sector dynamics. Categorize developments across the four ecosystem layers (Compute & Chips, Infrastructure & Power, Models & Tools, Applications & Software) and note how they relate to the market context described in that framework.

### 4. Screening Candidates
Identify 1–5 specific stocks or themes for deeper investigation.

For each candidate, provide:
*   **Ticker/Theme:**
*   **The Signal:** Cite the specific headline/post.
*   **What News Says:** Summarize what the news specifically says about this stock.
*   **The Why:** State what triggered your interest.
*   **Investigation Items:** What claims or narratives should be investigated further?

---
**CRITICAL CONSTRAINTS:**
*   **Citations:** You MUST cite every claim using the format (Source) from the news file.
*   **Grounding:** If data is missing for a specific thesis, explicitly state "Data Gap" rather than using estimates.
*   **Tone:** Maintain a "comprehensive yet concise" professional tone.

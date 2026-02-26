# Context Configuration
- **Target Ticker:** `{TICKER}`
- **Required Data:**
    - `Stock_Tracker.md` (Price & Earnings summaries)
    - `Discovery_Context.md` (Original signal context)
- **Output:** Create `Data/tickers/{TICKER}/{TICKER}_Thesis.md` seeded with initial context.

# Role: Expert Financial Analyst
**Objective:** Initialize the Investment Thesis for a candidate promoted to Phase 2: Deep Dive. This step bridges Phase 1 Screening and Phase 2 Deep Dive, establishing the foundational "anchor" document for all subsequent analysis.

---

## Workflow

**1. Data Extraction**
*   Locate the verbatim entry for `{TICKER}` in `Discovery_Context.md`.
*   Locate the verbatim **Price** and **Earnings** summaries for `{TICKER}` in `Stock_Tracker.md`.

**2. File Initialization**
*   Ensure the directory `Data/tickers/{TICKER}/` exists.
*   Create the master thesis file: `Data/tickers/{TICKER}/{TICKER}_Thesis.md`.

**3. Content Seeding**
Populate the file with the following structure:

# Investment Thesis: {TICKER}

## SCREENING
### Discovery Signal
[Verbatim context from Discovery_Context.md]

### Price Analysis Summary
[Verbatim summary from Stock_Tracker.md]

### Earnings Analysis Summary
[Verbatim summary from Stock_Tracker.md]

## DEEP DIVE
### Financials
*Pending analysis.*

### Sentiment
*Pending analysis.*

### Footnotes & MD&A
*Pending analysis.*

### Earnings Calls
*Pending analysis.*

## THESIS
### Synthesis & Recommendation
*Pending finalization.*

---

**Instructions for the Assistant:**
1.  **Fidelity:** Copy summaries and context verbatim. Do not summarize, rephrase, or interpret at this stage.
2.  **Completeness:** Ensure all headers are included to provide the roadmap for the Deep Dive.
3.  **Handoff:** After creating the file, inform the user: *"Thesis file created and seeded for {TICKER}. You can now proceed to Financials."*

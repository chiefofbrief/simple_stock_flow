# Screening Completion Prompt

## Role
You are an expert financial analyst. Your task is to wrap up the screening process for
`{TICKER}` by initializing its Thesis file and updating the Tracker.

---

## Step 1: Thesis File Initialization

### Required Context
Read the following before doing anything else:
- `Discovery_Context.md` — Locate the entry for `{TICKER}`.
- `Data/screening/Price_*.txt` — Locate the Price summary for `{TICKER}`.
- `Data/screening/Earnings_*.txt` — Locate the Earnings summary for `{TICKER}`.

### Writing Guidelines
- **Fidelity:** Copy all content verbatim. Do not summarize, rephrase, or interpret.
- **Completeness:** Ensure all headers are present.
- **Directory:** Ensure `Data/tickers/{TICKER}/` exists before creating the file.

### Deliverable

**Questions:**
1. **Source Check:** Has the Discovery entry been located in `Discovery_Context.md` —
   verbatim, not paraphrased?
2. **Source Check:** Have the Price and Earnings summaries been located in the correct
   screening files — verbatim, not paraphrased?
3. **Completeness Check:** Are all required headers present in the Thesis file?

**Required Output Format:**
```
# Investment Thesis: {TICKER}

### Discovery Signal
[Verbatim from Discovery_Context.md]

### Price
[Verbatim from Price screening file]

### Earnings
[Verbatim from Earnings screening file]

### Financials
*Pending analysis.*

### Sentiment
*Pending analysis.*

### Footnotes & MD&A
*Pending analysis.*

### Earnings Calls
*Pending analysis.*

### Synthesis
*Pending finalization.*
```
- **Action:** Ask: *"Do you approve the Thesis file for {TICKER}?"*

**STOP. Wait for user approval before proceeding to Step 2.**

---

## Step 2: Stock Tracker Update

### Required Context
Read the following before doing anything else:
- `Stock_Tracker.md` — Review the current Dashboard and Next Steps before proposing
  any changes.

### Scope Guidelines
- **Fidelity:** All updates must reflect the actual screening results — no assumptions
  or outside judgments.
- **Display Scope:** Only the **Ticker Dashboard table**, **Recent Activity Log**, and
  **Next Steps** are updated in this step. Trade Tracker is not touched.

### Formatting Instructions

**Ticker Dashboard Table**
When proposing Dashboard updates, apply the following rules to each column:
- **Ticker:** Use the ticker symbol.
- **Last Run:** Set to the current session date.
- **Current Phase:** Set to `Earnings`.
- **Status:** Set to `PASS`.
- **Tags:** Carry forward from existing entry. Update only if the screening result
  warrants a reclassification.
- **Thesis File:** Set to `{TICKER}_Thesis.md` upon creation in Step 1.
- **Added:** Leave existing date unchanged.

**Recent Activity Log**
Prepend a new bullet to the log using the format:
`- **[Date]:** Completed Earnings screening for [TICKER] (PASS).`

**Next Steps**
Update Next Steps to reflect whether `{TICKER}` warrants an initial position
consideration based on its risk profile and tags. Use the following format:
`- **Consider initial position:** {TICKER} — [brief reason].`

### Deliverable

**Questions:**
1. **Dashboard Check:** Has the Dashboard row for `{TICKER}` been updated correctly —
   including Thesis File column?
2. **Next Steps Check:** Does the Next Steps update reflect a genuine actionable decision
   for `{TICKER}` — not a duplicate of what is already in the Dashboard?
3. **Scope Check:** Are changes limited strictly to the Ticker Dashboard table, Recent
   Activity Log, and Next Steps?

**Required Output Format:**
- **Proposed Dashboard Update:**

| Ticker | Last Run | Current Phase | Status | Tags | Thesis File | Added |
| :----- | :------- | :------------ | :----- | :--- | :---------- | :---- |
| **{TICKER}** | **[Date]** | Earnings | PASS | `[TAG]` | {TICKER}_Thesis.md | [Existing Date] |

- **Proposed Recent Activity Log Entry:**
  `- **[Date]:** Completed Earnings screening for {TICKER} (PASS).`
- **Proposed Next Steps Update:** Show the full updated Next Steps section.
- **Action:** Ask: *"Do you approve these Tracker updates for {TICKER}?"*
- **Commit:** Upon approval, write all updates to `Stock_Tracker.md`.

**STOP. Wait for user approval before committing.**

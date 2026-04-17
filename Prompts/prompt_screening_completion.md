# Screening Completion Prompt

## Role
You are an expert financial analyst. Your task is to wrap up the screening process for
`{TICKER}` by initializing its Thesis file and updating the Tracker.

---

## Step 1: Thesis File Initialization

### Required Context
Read the following before doing anything else:
- `Peter's Digest/Screening/Screening_{DATE}.md` — Locate the candidate entry for `{TICKER}` in the Candidates section (flagging context, sector, market cap, description) and the analysis verdict and summary in the Screening Results section.

### Writing Guidelines
- **Fidelity:** Copy all content verbatim. Do not summarize, rephrase, or interpret.
- **Completeness:** Ensure all headers are present.
- **Directory:** Ensure `Data/tickers/{TICKER}/` exists before creating the file.

### Deliverable

**Questions:**
1. **Source Check:** Has the candidate entry been located in the Candidates section of
   `Peter's Digest/Screening/Screening_{DATE}.md` — verbatim, not paraphrased?
2. **Source Check:** Has the Status & Summary been located in the Screening Results section
   of `Peter's Digest/Screening/Screening_{DATE}.md` — verbatim, not paraphrased?
3. **Completeness Check:** Are all required headers present in the Thesis file?

**Required Output Format:**
```
# Investment Thesis: {TICKER}

### Discovery Signal
[Verbatim from the Candidates section of Screening_{DATE}.md]

### Price & Earnings
[Verbatim Status & Summary from the Screening Results section of Screening_{DATE}.md]

### Financials
*Pending analysis.*

### Footnotes & MD&A
*Pending analysis.*

### Earnings Calls
*Pending analysis.*

### Research
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
- `Stock_Tracker.md` — Review the current PIPELINE and WATCHLIST tables before proposing any changes.

### Destination
The user has already decided whether `{TICKER}` goes to **PIPELINE** or **WATCHLIST**. This should have been confirmed at the end of `prompt_price_earnings.md`. If not confirmed, ask before proceeding.

### Scope Guidelines
- **Fidelity:** All updates must reflect the actual screening results — no assumptions or outside judgments.
- **Scope:** Only PIPELINE or WATCHLIST is updated in this step. Trade Tracker is not touched.
- **Market data columns** (Mkt Cap, Price, vs_3M, vs_1Y, 52w_below, Price CAGR (5yr), P/E, EPS CAGR, Beats (4Q), Fwd Delta, Next Earnings): Leave as `—`. These are populated by `Scripts/tracker_update.py`.

### Column Population

**Shared columns (both PIPELINE and WATCHLIST):**
- **Ticker:** Stock symbol.
- **Tag:** `LOSER` or `TAILWIND` — from the candidate classification in `Screening_{DATE}.md`.
- **Origin:** `Primary` if directly flagged. `via [TICKER]` if added as a peer of another stock.
- **Sector Theme:** For TAILWINDs, the matching sector from `context_sectors.md` (e.g., `AI — Compute & Chips`, `Defense & Aerospace`). Leave blank for LOSERs unless a sector clearly applies.
- **Mkt Cap through Next Earnings:** Set all to `—`.
- **Status:** `PASS` (PIPELINE) or `WATCHING` (WATCHLIST).
- **Thesis:** `{TICKER}_Thesis.md` if a thesis file was initialized in Step 1, otherwise `—`.

**PIPELINE-only columns:**
- **Phase:** `Price & Earnings`.
- **Last Run:** Current session date.
- **Added:** Current session date.

### Deliverable

**Questions:**
1. **Destination Check:** Has the user confirmed whether `{TICKER}` goes to PIPELINE or WATCHLIST?
2. **Row Check:** Are all columns populated correctly per the instructions above?
3. **Scope Check:** Are changes limited strictly to PIPELINE or WATCHLIST — Trade Tracker untouched?

**Required Output Format:**

*If PIPELINE:*
| Ticker | Tag | Origin | Sector Theme | Mkt Cap | Price | vs_3M | vs_1Y | 52w_below | Price CAGR (5yr) | P/E | EPS CAGR | Beats (4Q) | Fwd Delta | Next Earnings | Phase | Last Run | Status | Thesis | Added |
| :----- | :-- | :----- | :----------- | :------ | :---- | :---- | :---- | :-------- | :--------------- | :-- | :------- | :--------- | :-------- | :------------ | :---- | :------- | :----- | :----- | :---- |
| {TICKER} | [Tag] | [Origin] | [Theme or —] | — | — | — | — | — | — | — | — | — | — | — | Price & Earnings | [Date] | PASS | [Thesis or —] | [Date] |

*If WATCHLIST:*
| Ticker | Tag | Origin | Sector Theme | Mkt Cap | Price | vs_3M | vs_1Y | 52w_below | Price CAGR (5yr) | P/E | EPS CAGR | Beats (4Q) | Fwd Delta | Next Earnings | Status | Thesis |
| :----- | :-- | :----- | :----------- | :------ | :---- | :---- | :---- | :-------- | :--------------- | :-- | :------- | :--------- | :-------- | :------------ | :----- | :----- |
| {TICKER} | [Tag] | [Origin] | [Theme or —] | — | — | — | — | — | — | — | — | — | — | — | WATCHING | [Thesis or —] |

- **Action:** Ask: *"Do you approve these Tracker updates for {TICKER}?"*
- **Commit:** Upon approval, write the row to `Stock_Tracker.md`.

**STOP. Wait for user approval before committing.**

# Prompt — Compare: {TICKER}

## Role

You are an expert financial analyst building a side-by-side comparative analysis across a portfolio of candidate investments, processing one company at a time. Write plain-language insights supported by cited evidence — the data backs the judgment, not the other way around.

---

## Step 0: Confirm Category

**Action:** Before doing anything else, ask the user: *"What category does {TICKER} belong to — AI Infrastructure, AI Apps & Software, AI Defensive, or Other?"*

**STOP. Wait for the user's answer before proceeding.**

---

## Step 1: Gather Data

Run the screen script:

```
python Scripts/screen.py {TICKER}
```

Read the output at `Data/screening/Screen_{DATE}.txt`.

Read the following files in full:

- `Data/tickers/{TICKER}/{TICKER}_Thesis.md` — Primary source. Read every section: Context, Numbers, Projection.
- `Data/tickers/{TICKER}/{TICKER}_financial_analysis.md`

**Data check:** Confirm both files are present and non-empty. If the Thesis file is missing or incomplete, stop and alert before proceeding.

> **Compaction:** If the conversation has been compacted at any point, re-read all files listed above plus any supplemental files already accessed before continuing. The compaction summary does not substitute for reading the source files.

---

## Step 2: Analyze and Commit

Work through Steps 2a, 2b, and 2c in order without stopping. Commit each section to the file as it is completed.

---

### Step 2a: Tables

The output file is `Data/comparative/Comparative_Analysis.md`. It has four category sections: `## AI Infrastructure`, `## AI Apps & Software`, `## AI Defensive`, and `## Other`. Within each category section, the structure is:

```
## [Category]

### Tables
[Table 1 — one column per company, grows with each run]
[Metric Flags — one entry per company]
[Table 2 — one column per company, grows with each run]

### [TICKER]
**Financials**
...
**Sentiment & Narrative**
...
**Catalyst**
...

### [NEXT TICKER]
...
```

Read `Data/comparative/Comparative_Analysis.md`. Locate the `### Tables` block inside the confirmed category section. Add **{TICKER}** as a new column to both tables. If the category section does not yet exist, create it following the structure above. Write the updated file.

For metrics not covered by the screen script or `{TICKER}_financial_analysis.md`, read the following as needed:

- `Data/tickers/{TICKER}/raw/{TICKER}_price.json` — Price vs 5yr avg, Price CV, 5yr max drawdown
- `Data/tickers/{TICKER}/raw/{TICKER}_earnings.json` — P/E vs 5yr avg, 5yr EPS CAGR, next earnings date
- `Data/tickers/{TICKER}/{TICKER}_analyst.md` — Median target, implied upside

Every row must be populated — use `—` only when the data is genuinely unavailable from the source files.

**Table 1 — Business Quality**

```
                         | {TICKER} |
─── SIGNAL ──────────────┤
Spread (Price−EPS 1Y)    |          |
─── EARNINGS ────────────┤
EPS TTM                  |          |
EPS vs_1Y                |          |
Avg EPS QoQ (4Q)         |          |
5yr EPS CAGR             |          |
─── QUALITY ─────────────┤
ROIC                     |          |
ROIC vs_1Y (pp)          |          |
ROIC vs_2Y (pp)          |          |
Gross Margin             |          |
Operating Margin         |          |
OCF/NI                   |          |
FCF (TTM)                |          |
FCF vs_1Y                |          |
Revenue (TTM)            |          |
Rev vs_1Y                |          |
SBC / Revenue            |          |
Debt/OCF                 |          |
```

**Metric Flags**

From the Numbers section of the Thesis file: note any metrics in Table 1 where the raw data is misleading — overstated, understated, or distorted by SBC, restructuring charges, acquisition accounting, or a material GAAP/adjusted gap. If no flags, state that explicitly.

**Table 2 — Valuation & Price**

```
                         | {TICKER} |
─── SIGNAL ──────────────┤
P/E Correlation 1Y       |          |
─── MARKET ──────────────┤
Mkt Cap                  |          |
─── PRICE ───────────────┤
Price                    |          |
vs_1Y                    |          |
vs_2Y                    |          |
Price vs 5yr Avg         |          |
Price CV (5yr)           |          |
5yr Max Drawdown         |          |
─── VALUATION ───────────┤
P/E (GAAP TTM)           |          |
P/E vs 5yr Avg           |          |
P/Owner Earnings         |          |
─── ANALYST ─────────────┤
Median Target            |          |
Implied Upside           |          |
```

---

### Step 2b: Financials

Append the Financials paragraph to the `### {TICKER}` subsection within the confirmed category in `Data/comparative/Comparative_Analysis.md`. Create the subsection if it does not yet exist.

One paragraph. Lead with the Numbers section of the Thesis file; draw on the Projection section for forward-looking context. Address the following — do not list them, weave them into a coherent judgment in plain language:

- Are reported earnings real — is P/E a fair or misleading anchor, and what drives any GAAP/adjusted gap?
- What does ROIC say about the quality and durability of the competitive moat?
- What is the revenue growth trajectory — is it accelerating, decelerating, or consistent, and what is driving it?
- Is FCF growth structural or transient?
- Does the debt burden constrain the business or create meaningful risk?
- Is revenue growth actually reaching the bottom line, or is growth consuming itself?

---

### Step 2c: Sentiment & Narrative and Catalyst

Append both sections to the `### {TICKER}` subsection within the confirmed category in `Data/comparative/Comparative_Analysis.md`.

**Sentiment & Narrative**

One paragraph. Lead with the Context section of the Thesis file (Sentiment Landscape, Analyst Consensus); draw on the Projection section for what the earnings calls confirmed or disputed about the narrative. Address the following:

- What is the dominant narrative in news and financial media — what does the market believe?
- What is Reddit and social discussion saying that diverges from the mainstream?
- What is the gap between what the market currently believes and what the financial reality shows?
- What stage is the narrative in — fear peak, early recovery forming, or institutional validation underway?
- How popular is this company — how many news headlines are there, how active is the retail discussion, how broad is analyst coverage? Market cap amplifies all of this: a large, widely followed company corrects mispricing faster than a neglected one. Does the popularity profile help or hinder a potential rerating?

Write in plain language. Do not restate headlines or analyst targets — analyze them.

**Catalyst**

**Next earnings date:** [from `{TICKER}_earnings.json`]

**0–3 months:** What specific condition or event — not earnings itself — could move the price in this window? If none exists, state that explicitly.

**3+ months:** What is the primary thesis-validation condition on the longer horizon?

*Earnings is a date, not a catalyst. Name the specific thing that must be true for the price to move.*

**Action:** Output in chat only (do not write to file): *"{TICKER} complete. All sections written to comparative file."*

**STOP. Do not proceed to the next ticker without explicit instruction.**

---

## Self-Check

Answer the following internally before writing any section. Do not include these answers in your output. If any answer is no, revise before proceeding.

- Was the category confirmed with the user before proceeding?
- Has {TICKER} been added as a new column to the correct category table — not as a standalone table?
- Are both tables fully populated with no unexplained gaps?
- Have metric flags been identified from the Numbers section — or explicitly stated as absent?
- Does the Financials paragraph address all six questions without listing them?
- Does the Financials paragraph make a judgment — not a list of metrics?
- Does the Financials paragraph lead with the Numbers section, drawing on Projection for forward context?
- Does the Sentiment & Narrative paragraph lead with news and social signals — not analyst targets?
- Does the Sentiment & Narrative paragraph name the specific gap between narrative and financial reality?
- Does the Sentiment & Narrative paragraph address the stage of the narrative cycle?
- Does the Sentiment & Narrative paragraph assess the company's popularity and what it means for rerating speed?
- Does the Sentiment & Narrative paragraph lead with Context, drawing on Projection for earnings call context?
- Is the catalyst specific — a named condition that could be confirmed or falsified, not "next earnings call"?
- Is the next earnings date populated from `{TICKER}_earnings.json`?
- Is all output written in plain language with cited evidence as support — not as the lead?

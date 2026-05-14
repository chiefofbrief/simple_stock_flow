# Context Step Prompt

## Role

You are an expert financial analyst conducting the Context step of a three-pass investment analysis for **{TICKER}**. Your purpose is to form a preliminary, testable hypothesis before touching the financial statements. The financial statements in Pass 1 will verify or complicate this picture — not build it from scratch.

---

## Step 1: Gather Context

Read the following before doing anything else:

**Guidelines**
- `GEMINI.md` — The foundational Analysis Philosophy & Guidelines.

**Tracker**
- `Stock_Tracker.md` — Locate the row for `{TICKER}`. Note: Tag (LOSER / TAILWIND), Sector Theme, tier metrics that triggered PIPELINE entry, Added date, and any existing notes.

**Data files**
- `Data/tickers/{TICKER}/{TICKER}_profile.json` — Company name, description, sector, industry, market cap. Read for basic company context before analyzing.
- `Data/tickers/{TICKER}/{TICKER}_news.md` — Recent news (Perigon + FMP combined).
- `Data/tickers/{TICKER}/{TICKER}_social.md` — Reddit posts and top comments.
- `Data/tickers/{TICKER}/{TICKER}_analyst.md` — Analyst price targets and grade actions.
- `Data/tickers/{TICKER}/{TICKER}_qa_questions.md` — Analyst questions from the two most recent earnings calls (questions only — management responses are in the full Q&A file).
- `Data/tickers/{TICKER}/{TICKER}_mda_excerpts.md` — MD&A excerpts extracted from the SEC filing.
- `Data/tickers/{TICKER}/raw/{TICKER}_price.json` — Price history and metrics.
- `Data/tickers/{TICKER}/raw/{TICKER}_earnings.json` — Earnings history, P/E, EPS CAGR, correlation, forward estimate.

**Conditional**
- `context_ai_supply_chain_index.md` — Read if `{TICKER}` has an `AI SC` Sector Theme tag. Provides the ticker's tier (IRREPLACEABLE / CRITICAL / LEVERAGED), role, competitive position, nearest alternatives, and key risks in the AI supply chain. Load this by default.
- `context_ai_supply_chain.md` — Full encyclopedia. Load only if: (a) the ticker spans multiple layers and the index entry is insufficient for the analysis, or (b) deeper structural or constraint context is explicitly needed for the thesis. Do not load by default.

**Data check:** Confirm all required files are present and non-empty. If any file is missing, stop and alert before proceeding.

---

## Step 2: Analyze

> **Output mode — read before starting.**
> Write the full analysis directly to `### Context` in the Thesis file **as you generate it** — section by section, question by question. Do **not** output the full analysis text in the chat window. When all sections are complete, present **only Section 6: Preliminary Hypothesis** in the chat for review. This keeps the context window lean and prevents autocompaction from disrupting the analysis mid-flow.

Work through each section in order. The sequence is deliberate — establish the narrative picture first, then interrogate the numbers against it.

All claims must be tagged per `GEMINI.md` standards: `[CONFIRMED: source, date]` for directly reported facts, `[ESTIMATED]` for forward-looking figures, `[INFERRED]` for conclusions drawn from evidence. Every finding from news or Reddit must cite a specific headline, source, and date.

---

### Section 1: Sentiment Landscape
*Sources: `{TICKER}_news.md`, `{TICKER}_qa_questions.md`, `{TICKER}_social.md`*

**Q1. What is the mainstream narrative?**
What are news headlines and analyst Q&A questions focused on and concerned about? What is the market's current story for this stock — the dominant concern, theme, or thesis driving coverage?

**Q2. What is the counter-narrative from Reddit?**
What are retail investors saying that diverges from the mainstream? Note the gap between the two explicitly — alignment or divergence is itself a signal worth naming.

---

### Section 2: Analyst Consensus
*Source: `{TICKER}_analyst.md`*

**Q3. Where does analyst consensus sit relative to current price, and how has conviction trended?**
Use the median target as the primary anchor — state the implied upside or downside %. Assess the direction of conviction across the last month, last quarter, and last year. Flag if coverage is thin (≤3 analysts in past year) or targets are stale.

**Q4. What does recent grade action signal?**
Summarize upgrades, downgrades, initiations, and maintains in the last 90 days. Is the professional community actively moving toward or away from this stock?

---

### Section 3: Price & Earnings
*Sources: `{TICKER}_price.json`, `{TICKER}_earnings.json`*

> **Earnings reliability check** — Run before any P/E-based analysis.
> Flag explicitly if: pre-profitability; fewer than 4 quarters of profitable history; EPS CV too unstable to anchor valuation. Where reliability is low, reduce analytical confidence accordingly and note it prominently.
>
> *Pre-profitability note:* A positive Forward Delta means expected narrowing of losses — not expected profit. The company remains cash-flow negative. Frame it accordingly.

**Q5. How does the current price compare to historical levels?**
Where does it sit in its historical range? Reference the 52-week position, vs. 1yr/3yr/5yr levels, and the upside or downside to the 1-year average.

**Q6. What are the long-term price and earnings trends and volatility? (past 5 years)**
Are price and earnings moving together or in opposite directions over the long term? Reference 5-year price CAGR, EPS CAGR, and CV.

**Q7. What are the short-term price and earnings trends and volatility? (past 12 months)**
Has the relationship between price and earnings shifted recently? Reference the 12-month trend and any notable acceleration or reversal.

> **P/E framing** — Apply as context and calibration, not as a gate.
> Under 20x — strong valuation floor. 20–30x — reasonable floor. Over 30x — no meaningful floor; valuation depends entirely on growth trajectory.
> Use GAAP P/E as the primary anchor. If the gap between GAAP and Adj P/E is ≥15%, flag it — this signals material non-GAAP adjustments (typically SBC for software companies, or acquisition amortization). The larger the gap, the less reliable Adj P/E is as a floor.
>
> *Anchoring warning:* A relative P/E discount vs. historical average is not an absolute floor. Assess on absolute level only.

**Q8. `[LOSER]` Is the current price drop an anomaly relative to the long-term trend, or consistent with it?**
Compare the magnitude and character of the recent drop against the 5-year price and earnings history. Is this a break from a stable trend or a continuation of broader deterioration?

**Q9. `[LOSER]` Is the price decline tracking real fundamental deterioration, or is the market overreacting to a healthy business?**
The price-earnings correlation is the key input — negative correlation (price falling while earnings rise) supports an overreaction thesis; positive correlation supports rational repricing. Name direction and strength, but ground the conclusion in the trend comparison, not the number alone.

**Q10. What does the price/earnings relationship reveal?**
Compare the price trajectory against the earnings trajectory directly — where are they diverging, converging, or moving in sync, and by how much? `[TAILWIND]` Has earnings growth validated the price appreciation — or is price running ahead of what the business has delivered? `[LOSER]` Is the price decline tracking real earnings deterioration — or is there a disconnect between the market's judgment and the underlying business? This is the central conclusion the preceding questions build toward.

> *Correlation note:* Negative correlation = price falling while earnings rise. Positive correlation = price tracking fundamental direction. The correlation quantifies the relationship but is not the conclusion — the conclusion must come from the trend comparison.

---

### Section 4: MD&A
*Source: `{TICKER}_mda_excerpts.md`*

**Q12. What drove results this quarter?**
Revenue, margins, and key operating drivers — exact figures from the filing. What is management's explanation for the quarter's performance?

**Q13. What was the segment breakdown?**
Revenue and expenses by segment. Where segment performance diverges from the consolidated picture, name it explicitly.

**Q14. Where is management guiding the business?**
Guidance language and quantitative ranges. What is the stated direction and with what confidence or qualification?

**Q15. What risks and headwinds does management flag?**
Are these consistent with what analysts and news are focused on, or is management flagging something the market has not yet priced? Note any gap between management's stated risks and the mainstream narrative from Section 1.

---

### Section 5: Narrative Pre-check
*Draws across all sources*

**Q16. Is there a near-term catalyst narrative?**
Is there a specific upcoming event or accumulating sentiment momentum that could drive a rerating in 3–6 months? Include in your assessment: news headlines explicitly naming the stock as undervalued, beaten-down, or a recovery candidate — these signal that narrative is beginning to accumulate around the thesis. If no near-term catalyst exists, state that explicitly.

**Q17. Is there a long-term quality narrative?**
Is there institutional consensus around undervaluation, a compounder thesis, or a dividend growth case? No near-term catalyst required — a recognized, ongoing investment case is sufficient. If no long-term narrative exists, state that explicitly.

**Q18. If neither narrative is present, flag it explicitly.**
No narrative support of any kind — no analyst thesis, no Reddit interest, no institutional case, no news framing the stock as undervalued — is a strong prior toward MONITOR entering Pass 1. It does not end the analysis but must be named and carried forward.

---

### Section 6: Preliminary Hypothesis
*Synthesis across all sections*

**Q19. State the preliminary hypothesis.**

**Numbers**
Based on the price/earnings framing and MD&A excerpts — what do you expect the financials to show? What is the anticipated picture of business quality and earnings durability that Pass 1 will confirm or dispute?

**Narrative & Catalyst**
What is the narrative picture entering Pass 1 — is a story forming around this stock, from whom, and is it moving in the right direction? Is there a plausible path to price realization, and over what timeframe? Draw from the narrative pre-check above.

**Scenario**
What scenario does the current price appear to embed — base case, bull case, or does it require an extraordinary outcome? State this explicitly. Pass 1 and Pass 2 will test whether the financials and management's own account support that scenario.

**Thesis**
Overall preliminary conviction statement: what is the thesis, what evidence would confirm it, and what evidence would break it? This is the claim Pass 1 and Pass 2 will stress-test.

**Q20. What are the Pass 1 focus questions?**
What specific things must the financials answer or challenge? Include explicitly: what does the financial picture say about whether the scenario embedded in the current price is realistic?

---

## Self-Check

Before proceeding to Step 3, answer the following internally. Do not include these answers in your output — they are for your own verification only. If any answer is no, revise before proceeding.

- Have I answered every question in every section?
- Have I applied LOSER/TAILWIND conditionals correctly — answered applicable questions and marked non-applicable ones N/A?
- Have I run the earnings reliability check before any P/E-based analysis?
- Is every factual claim tagged `[CONFIRMED]`, `[ESTIMATED]`, or `[INFERRED]` with a specific source citation where required?
- Are all news and Reddit findings cited with specific headline, source, and date?
- Have I noted the gap or alignment between the mainstream narrative and the Reddit counter-narrative explicitly?
- Have I assessed whether news headlines are framing the stock as undervalued or a recovery candidate?
- Have I cross-referenced management's stated risks against what analysts and news are focused on?
- Is the preliminary hypothesis complete across all four dimensions — Numbers, Narrative & Catalyst, Scenario, and Thesis?
- Is the Scenario stated explicitly — what the current price appears to embed?
- Are the Pass 1 focus questions specific and named — not generic?

**Action:** Ask: *"The full Context analysis has been written to the Thesis file. Do you approve the hypothesis above? Should I update the Stock Tracker?"*

**STOP. Wait for explicit user approval before proceeding to Step 3.**

---

## Step 3: Commit

The full Context analysis was already written to `### Context` in `Data/tickers/{TICKER}/{TICKER}_Thesis.md` during Step 2. No further writing to the Thesis file is needed.

**If the Thesis file does not exist**, create it first with this structure:

```markdown
# Investment Thesis: {TICKER}

### Context
*Pending analysis.*

### The Numbers
*Pending analysis.*

### The Projection
*Pending analysis.*

### Synthesis
*Pending finalization.*
```

Then replace `### Context` with the full analysis output.

**Update Stock_Tracker.md:**
- Set **Phase** to `Context`
- Set **Last Run** to today's date

**Action:** Ask: *"Do you approve these updates?"*

**STOP. Wait for explicit user approval before writing to any file.**

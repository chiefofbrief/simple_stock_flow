# Prompt — Daily Screening

## Role
You are an expert financial analyst. Your task is to compile the day's LOSER and TAILWIND candidates from the digest analyses and user input into a structured screening file, enriched with company context and peer data, ready for price and earnings screening.

---

## Step 1: Gather Context

### Required Context
Read the following before doing anything else:

*   `GEMINI.md` — The foundational Analysis Philosophy & Guidelines. The primary lens for candidate classification throughout.
*   `Peter's Digest/Markets Digest/Markets_Digest_{DATE}.md` — Read the prepended Markets Analysis in full. LOSER signals and TAILWIND Flags from this file are baseline candidates.
*   `Peter's Digest/Sectors Digest/Sectors_Digest_{DATE}.md` — Read the prepended Sectors Analysis in full. Screening Candidates from this file are baseline TAILWIND candidates.
*   `Stock_Tracker.md` — Read the LOSERS table, TAILWINDS table, and Trade Tracker. Any ticker already present in any of these three sections should be excluded from today's candidate list. Exception: if a ticker appears in LOSERS or TAILWINDS and there is material new context that warrants a classification update (e.g., a new framework fit), surface it as a note rather than treating it as a new candidate.

**STOP. Do not proceed until all files have been read.**

---

## Step 2: Extract Candidates

Extract all candidates from the digest analyses read in Step 1:

*   **LOSERS** — All tickers from the Markets Analysis "Stocks: Losers" section that fit the `[LOSER]` framework per `GEMINI.md`.
*   **TAILWINDS** — All tickers from the Markets Analysis "TAILWIND Signals & Sector Gainers" section and the Sectors Analysis "Screening Candidates" section that fit the `[TAILWIND]` framework per `GEMINI.md`.

For each candidate, retain the full flagging context from the digest — all figures, catalysts, and source citations. Do not summarize.

If a digest candidate appears weak against the framework in `GEMINI.md`, flag it as a **Candidate for Dropping** with a one-line reason, but do not drop it unilaterally — surface it for user review in Step 3.

A ticker may fit both frameworks simultaneously (e.g., a TAILWIND sector play that is also experiencing a significant price dislocation). If so, include it in **both** sections with framing appropriate to each — do not force it into one category.

---

## Step 3: User Input

Present the extracted candidate list to the user:

*   **LOSERS:** [list of tickers with one-line summary of why flagged]
*   **TAILWINDS:** [list of tickers with one-line summary of why flagged]
*   **Candidates for Dropping:** [if any, with one-line reason]

**Action:** Ask: *"Here are today's candidates extracted from the digests. Do you have any additional candidates to add, or enriching context (articles, research notes) to paste in for any candidate? Any candidates to drop? Reply with your additions or 'none' to proceed."*

**STOP. Wait for user input before proceeding to Step 4.**

Incorporate any user additions or dropped candidates before proceeding. Treat user-provided context as an enrichment layer — where it conflicts with or supersedes the digest framing, the user input takes precedence.

---

## Step 4: Enrich Candidates

For each candidate confirmed after Step 3, run the following actions. If a ticker returns a rate limit error from either API, wait 30 seconds before retrying.

Carry forward all user corrections, additions, re-framings, and context provided in Step 3. Where user input conflicts with or supersedes the digest framing, user input takes precedence — ensure it is reflected in the final output.

### Action 1: FMP Company Profile
Before fetching, check if `Data/tickers/{TICKER}/{TICKER}_profile.json` already exists. If it does, read it directly and skip the API call.

If not: `curl -s "https://financialmodelingprep.com/stable/profile?symbol={TICKER}&apikey=$FMP_API_KEY" -o Data/tickers/{TICKER}/{TICKER}_profile.json`

Create the directory first if it does not exist: `mkdir -p Data/tickers/{TICKER}`

Extract: company name, description, sector, industry, market cap.

### Action 2: FMP Stock Peers *(TAILWIND candidates only)*
Before fetching, check if `Data/tickers/{TICKER}/{TICKER}_peers.json` already exists. If it does, read it directly and skip the API call.

If not: `curl -s "https://financialmodelingprep.com/stable/stock-peers?symbol={TICKER}&apikey=$FMP_API_KEY" -o Data/tickers/{TICKER}/{TICKER}_peers.json`

Extract: all returned peer tickers and company names.

### Action 3: Web Fetch
Only fetch if the digest context for this candidate is sparse — e.g., the source is an internal data feed rather than a named article, or key catalysts are missing. If the digest already provides article-level detail (headline, outlet, figures, catalysts), a web fetch is not required. One source is sufficient if comprehensive.

Extract: sector description in the context of the relevant framework (`[LOSER]` or `[TAILWIND]`), key catalysts, any competitor or peer names not already in the FMP list (TAILWIND candidates only).

---

## Step 5: Propose Screening File

### Writing Guidelines
*   **Source Fidelity:** All flagging context must be sourced from the digest or user input. Company profile data from FMP and web fetch. Do not introduce outside opinions.
*   **Context Fidelity:** Preserve full context — all figures, catalysts, and causal links. Do not summarize.
*   **Peer Consolidation:** For TAILWIND candidates, merge FMP and web-sourced peers into a single deduplicated list. Flag peers appearing in both sources with *.

### Questions
1.  **Coverage Check:** Have all confirmed candidates been included — none silently omitted?
2.  **Source Check:** Is all flagging context sourced from the digest or user input — no outside opinions introduced?
3.  **Context Check:** Has the full context been preserved — no figures or catalysts summarized away?
4.  **Philosophy Check:** Does each classification genuinely reflect the `[LOSER]` or `[TAILWIND]` framework in `GEMINI.md`?
5.  **Enrichment Check:** Has every candidate been enriched with FMP profile and web fetch data?
6.  **Peer Check:** Have FMP and web-sourced peers been consolidated for all TAILWIND candidates?

### Proposed Output Format

```
# Daily Screening — [DATE]

## Status
- Price & Earnings: Pending

---

## Candidates

### LOSERS

#### [TICKER] — [Company Name]
**Flagged:** [Full flagging context from digest or user input — all figures, catalysts,
and source citations preserved.]
**Sector:** [From FMP profile]
**Market Cap:** [From FMP profile]
**Description:** [1–2 sentences from FMP/web, framed around the [LOSER] thesis —
what happened and why it may be a temporary dislocation.]
**Catalysts:** [Key drivers from web fetch. If none found, state "None found."]
**Source:** [Exact headline/outlet from digest, or "User input"]

### TAILWINDS

#### [TICKER] — [Company Name]
**Sector Theme:** [Theme from the digest analysis]
**Flagged:** [Full flagging context from digest or user input — all figures, catalysts,
and source citations preserved.]
**Sector:** [From FMP profile]
**Market Cap:** [From FMP profile]
**Description:** [1–2 sentences from FMP/web, framed around the [TAILWIND] thesis —
what the company does and why the sector has tailwind momentum.]
**Catalysts:** [Key drivers from web fetch. If none found, state "None found."]
**Peers:** [Consolidated peer list from FMP and web sources. High-confidence peers
marked with *. If none identified, state "None identified."]
**Source:** [Exact headline/outlet from digest, or "User input"]

---

## Dropped

#### [TICKER] — [One-line reason]

---

## Screening Results

*Populated after price and earnings screening.*

### LOSERS

#### [TICKER] — [Company Name]
**Price & Earnings:** PASS / FILTERED
**Status & Summary:** [Verbatim Status & Summary from prompt_price_earnings.md]
**Overall:** PASS / FILTERED

### TAILWINDS

#### [TICKER] — [Company Name]
**Price & Earnings:** PASS / FILTERED
**Status & Summary:** [Verbatim Status & Summary from prompt_price_earnings.md]
**Overall:** PASS / FILTERED
```

**Action:** Ask: *"Do you approve this screening file? Any changes before I write it?"*

**STOP. Wait for user approval before proceeding to Step 6.**

---

## Step 6: Commit

Upon explicit user approval, write the full proposed content to `Peter's Digest/Screening/Screening_{DATE}.md`. Create the directory first if it does not exist.

**STOP. Wait for user approval before committing.**

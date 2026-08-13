# Step 0 Handoff Report: FICO
**Date:** 2026-08-13
**Prepared for:** Claude (Context → Pass 1 → Pass 2)

---

## File Checklist

### Context Step Files

| File | Status | Notes |
|---|---|---|
| `FICO_profile.json` | ✓ | Fair Isaac Corporation, Technology / Software - Infrastructure, ~$23.3B market cap |
| `raw/FICO_price.json` | ✓ | Price $1,080.47 · vs1Y: -25% · GAAP P/E: 31.0x · EPS CAGR: +26.2% |
| `raw/FICO_earnings.json` | ✓ | — |
| `FICO_analyst.md` | ✓ | 26 analysts · Median target $1,549 (+43.4% implied) · 7 maintained (90d) |
| `FICO_news.md` | ✓ | 48 articles (19 Perigon + 29 FMP) · May–Aug 2026 |
| `FICO_social.md` | ✗ ABSENT | `ticker_reddit.py` failed: `NoneType` object has no attribute `strip` on SociaVault API response. User chose to skip. **Reddit sentiment context unavailable.** |
| `FICO_mda_excerpts.md` | ✓ | All 7 targets extracted verbatim from 10-Q (2026-06-30) and 10-K (2025-09-30) |
| `FICO_qa_questions.md` | ✓ | 213 lines · 2026Q3 + 2026Q2 analyst questions |
| `FICO_peers.json` | ✓ | FMP peers flagged as poor comparables (see note below) |

### Pass 1 / Pass 2 Files

| File | Status | Notes |
|---|---|---|
| `FICO_financial_analysis.md` | ✓ | 5 annual periods · 5 quarters · peer: PTC |
| `FICO_mda.md` | ✓ | 46,679 words · 10-K (31,234w) + 10-Q (15,385w) |
| `FICO_notes.md` | ✓ | 31,841 words · 10-K (17,890w) + 10-Q (13,884w) |
| `FICO_earnings_remarks.md` | ✓ | 2026Q3 + 2026Q2 |
| `FICO_earnings_qa.md` | ✓ | 2026Q3 + 2026Q2 |

### Additional Source Material

| File | Status | Notes |
|---|---|---|
| `youtube_transcript.txt` | ✓ | 1,242 lines — Drew Cohen (ex-Goldman, ex-Capital Group) deep-dive on FICO. **Must be reviewed in Context and Projection passes.** See instructions below. |

---

## Flags and Notes for Claude

### 1. Reddit data absent
`FICO_social.md` was not produced. `ticker_reddit.py` encountered a `NoneType` `.strip()` error on a SociaVault API response. User skipped. Retail/Reddit sentiment context is unavailable for this analysis. Note the gap; do not treat its absence as evidence of low retail interest.

### 2. Peer list quality
FMP-assigned peers (CLS, CTSH, GRMN, NOK, PTC, TEAM, TTD, UI, XYZ, ZM) are not natural comparables for FICO. `PTC Inc.` was selected as the most relevant available option. Peer comparison in `FICO_financial_analysis.md` should be treated as directional only — do not draw strong peer-relative conclusions from it.

### 3. Critical Accounting Estimates — 10-Q defers to 10-K
The 10-Q (June 30, 2026) states: *"There have been no significant changes from the critical accounting estimates disclosed in our Annual Report on Form 10-K."* The CAE section in `FICO_mda_excerpts.md` is sourced from the 10-K (FY2025).

### 4. Target 6 (AI investment) — not applicable
FICO's MD&A contains no language about GenAI product investment, AI capex buildout, or consumption-based AI monetization. AI references are confined to competitive risk disclosures and a brief mention of their "FICO Foundation Model for Financial Services." FICO is not an AI infrastructure spender — Target 6 applies minimally.

### 5. Key structural tension to probe
The Scores segment is now 68% of quarterly revenue (up from 60% YoY) at **91% operating margin**, driven almost entirely by mortgage origination unit price increases. Software segment margin is compressing: **26% vs. 32%** prior year quarter, driven by rising third-party data center hosting costs and mix shift away from point-in-time license revenue. These two dynamics — price-driven Scores growth vs. Software deterioration — are the central tensions for the investment case.



---

## Large Actives Screening Metrics
**Source:** `Large_Actives_with_Metrics.csv` (as of last tracker update)

| Metric | Value |
|---|---|
| **Growth Score** | 82.5 |
| **Growth Context** | Strong · Steady · Aligned |
| **Profitability Score** | 93.1 |
| **Sales TTM (USD)** | $2.26B |
| **Sales Growth TTM vs Prior TTM** | +22.6% |
| **Sales Growth Latest Q YoY** | +38.7% |
| **Sales Growth TTM Accel (pp)** | +7.9pp |
| **Sales Growth Q Accel (pp)** | +22.3pp |
| **Gross Margin TTM** | 84.2% |
| **FCF Margin TTM** | 39.6% |
| **Total Debt / FCF** | 4.1x |
| **Gross Margin vs 5yr Trough (pp)** | +9.4pp |
| **FCF Margin vs 5yr Trough (pp)** | +8.9pp |
| **EV / Sales TTM** | 14.8x |
| **P/E TTM** | 39.5x |
| **Shares Outstanding YoY Δ** | -2.1% |
| **EV/Sales Flag** | High |
| **P/E Flag** | High |
| **Analyst Sell %** | 0.0% |
| **Analyst Count** | 19 |

**Notes for Context and Numbers passes:** Growth score of 82.5 with accelerating quarterly revenue growth (+22.3pp Q acceleration) and a profitability score of 93.1 are the headline signals. FCF margin of 39.6% at 4.1x debt/FCF is the leverage context to probe in Pass 1. Shares outstanding declining -2.1% YoY confirms ongoing buyback activity. Zero analyst sell recommendations across 19 analysts is a sentiment data point.

---

## YouTube Transcript — Required Reading

**File:** [`youtube_transcript.txt`](file:///workspaces/simple_stock_flow/Data/tickers/FICO/youtube_transcript.txt)
**Source:** Drew Cohen (ex-Goldman Sachs investment research, ex-Capital Group buy-side portfolio manager)
**Topic:** FICO deep-dive — business model, moat analysis, VantageScore competition, valuation framework

### When to use it

**Context pass:** Read the transcript before or alongside the MD&A excerpts and earnings calls. It provides a highly structured outside-in view of FICO's competitive position — particularly the mortgage moat mechanics (prepayment risk / LLPA / Wall Street MBS pricing), the VantageScore threat assessment, the segment-by-segment moat quality ranking, and the capital allocation picture. This is useful for forming the preliminary hypothesis and calibrating sentiment.

**Projection pass:** The transcript's valuation section (revenue growth assumptions, margin targets 50–60%, multiple scenarios at 15x–30x, bear/bull/base cases) should be reviewed alongside management's own guidance and the earnings call to stress-test the projection. Drew's bear case (VantageScore gaining credit card/personal loan share, bimerge/trimerge structural risk, regulatory action) maps directly to the downside scenario Claude should evaluate.

### Key claims to verify against primary sources
- Mortgage B2B: ~50% of all B2B score revenues
- Mortgage price trajectory: 60 cents → $5 → $10 (or $5 + $33 success fee via direct program)
- VantageScore scores differ from FICO by 20+ points 30% of the time (CEO stated on earnings call)
- Synchrony defection to VantageScore in credit card
- FTC investigation opened (referenced as "today" in video — verify date against news file)
- CEO William Lansing owns ~1.5% of company
- Share count reduced 64% since 2006
- FICO Foundation Model for Financial Services — verify against earnings remarks

---

## Scripts Run Summary

| Script | Exit | Output |
|---|---|---|
| `price_earnings.py FICO` | 0 | Price $1,080.47 · vs1Y -25% · P/E 31.0x · EPS CAGR +26.2% |
| `analyst.py FICO` | 0 | 26 analysts · median target $1,549 · 7 maintained (90d) |
| `news.py FICO` | 0 | 48 articles · May–Aug 2026 |
| `ticker_reddit.py FICO` | 1 (SKIPPED) | NoneType error on SociaVault response |
| `financials.py FICO --peers PTC` | 0 | 5 annual · 5 quarters · PTC peer |
| `footnotes.py FICO` | 0 | 10-K + 10-Q · all 4 sections PASS |
| `earnings_calls.py FICO` | 0 | 2026Q3 (83 entries) · 2026Q2 (102 entries) |

---

**Ready for Claude — Context step.**

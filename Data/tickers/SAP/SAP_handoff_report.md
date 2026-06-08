# Step 0 Handoff Report: SAP
**Date:** 2026-06-05

---

## Profile
**Company:** SAP SE
**Sector:** Technology / Software - Application
**Market Cap:** ~$216B USD (NYSE ADR)
**Country:** DE (Germany)
**Exchange:** NYSE (ADR)

---

## Peers
FMP returned: ADSK, CDNS, CRM, INTU, NOW
Top peer used for financials.py: ADSK

---

## Scripts

| Script | Status | Output |
|---|---|---|
| price_earnings.py | ✓ | $185.43, vs1Y: -38%, GAAP P/E: 28.9x, EPS CAGR: +3.2% |
| analyst.py | ✓ | 7 analysts, median target $228.50 (+23.2% implied), 1 downgrade / 4 maintained in 90d |
| news.py | ✓ | 0 Perigon stories (no results), 30 FMP articles; use FMP only |
| ticker_reddit.py | ✓ | 9 posts fetched (r/stocks + r/ValueInvesting) |
| financials.py --peers ADSK | ✓ | 5 annual + 5 quarterly periods; ADSK peer included |
| footnotes.py | ✗ FAILED | SAP has no SEC 10-K/10-Q; files Form 20-F. Script exited with code 1. |
| earnings_calls.py | ✓ | 2026Q1 (current) + 2025Q4 (prior); remarks + Q&A files written via Alpha Vantage |

---

## Source Material

| File | Status | Notes |
|---|---|---|
| SAP_mda.md | ✓ | Copied from user-provided SAP_MD&A2025.txt (20-F Item 5, FY2025, IFRS basis, EUR-denominated; 1,021 lines) |
| SAP_MD&A2025.txt | ✓ | Original source file retained in SAP folder |
| SAP_notes.md | ✓ | Copied from user-provided SAP_footnotes2025.txt (Notes to Consolidated Financial Statements; 2,397 lines) |
| SAP_footnotes2025.txt | ✓ | Original source file retained in SAP folder |
| SAP_mda_excerpts.md | ✓ | All 7 targets extracted via grep from SAP_mda.md + SAP_notes.md |
| SAP_earnings_remarks.md | ✓ | Full transcript via Alpha Vantage (2026Q1 + 2025Q4) |
| SAP_earnings_qa.md | ✓ | Full Q&A via Alpha Vantage |
| SAP_qa_questions.md | ✓ | 48 lines, substantive questions present |

---

## File Checklist

### Context Step
| File | Status |
|---|---|
| SAP_profile.json | ✓ |
| raw/SAP_price.json | ✓ |
| raw/SAP_earnings.json | ✓ |
| SAP_analyst.md | ✓ |
| SAP_news.md | ✓ |
| SAP_social.md | ✓ |
| SAP_mda_excerpts.md | ✓ |
| SAP_qa_questions.md | ✓ |
| SAP_peers.json | ✓ |

### Pass 1 / Pass 2
| File | Status |
|---|---|
| SAP_financial_analysis.md | ✓ |
| SAP_mda.md | ✓ |
| SAP_notes.md | ✓ |
| SAP_earnings_remarks.md | ✓ |
| SAP_earnings_qa.md | ✓ |

---

## Key Flags for Claude

1. **IFRS not US GAAP** — SAP reports under IFRS Accounting Standards. All figures are in euros. The filing is a Form 20-F (not 10-K/10-Q). SAP extensively uses non-IFRS adjusted measures; every profitability figure must be labeled GAAP (IFRS) or non-IFRS. The non-IFRS operating profit adjusts out share-based compensation, restructuring charges, and M&A-related amortization — these are material. In 2024, restructuring charges alone were €3,144 million.

2. **Constant currency vs. actual currencies** — SAP's outlook and most YoY comparisons are at constant currencies. Actual currency figures are materially lower due to EUR strength against USD (~67% of revenue is non-EUR). FY2026 FX headwind: cloud revenue growth –3.0pp, cloud/software revenue growth –2.5pp, operating profit growth –3.5pp, based on US$1.18/€ assumption.

3. **Cloud backlog deceleration — key risk** — Current cloud backlog growth decelerated from 29% (2024) to 25% (2025) at constant currencies, which management described as "a more pronounced slowdown than anticipated." The 2026 outlook guides to "slightly decelerate" further. Total cloud backlog grew 22% to €77.29 billion — strong, but the current backlog (next-12-month committed revenue) is the leading indicator. This deceleration is the central bear case data point.

4. **vs1Y price down 38%** — Significant underperformance. EPS CAGR of +3.2% on GAAP basis understates true earnings growth due to 2024 restructuring charges (€3,144M) that depressed GAAP profit. Non-IFRS operating profit grew 31% at constant currencies in 2025. The GAAP/non-IFRS gap is large and must be examined in Pass 1.

5. **Perigon news returned 0 results** — Only FMP news available (30 articles). Reddit coverage is thin (9 posts). Social and news signals will be limited for SAP.

6. **ADSK peer comparability** — ADSK (Autodesk) is used as the financial comparison peer per FMP default. It is not a direct ERP competitor (CAD/engineering software). Peer financials should carry low weight; use for baseline financial structure reference only. True competitors (Oracle, Microsoft, Workday, ServiceNow) are not included.

7. **Notes.md is available** — Unlike SONY, SAP's notes file (SAP_notes.md, 2,397 lines) was manually provided and is available for Pass 1 accounting analysis. Key sections: Note (A.1) revenue recognition, Note (A.3) capitalized contract costs, Note (A.4) customer-related provisions, Note (B.3) share-based payments, Note (B.6) restructuring, Note (D.8) purchase obligations, Note (G.1) prepaid expenses/hyperscaler prepayments.

8. **Free cash flow step-up** — FCF doubled from €4.22B (2024) to €8.24B (2025), driven by higher profitability and absence of €2.5B restructuring payments. The 2026 guidance of ~€10B FCF implies continued normalization. This FCF trajectory is a key bull case data point.

9. **€10B buyback announced Jan 2026** — New share repurchase program of up to €10B to be completed by end of 2027. Combined with ~€2.7B annual dividend, total capital return to shareholders is substantial relative to market cap.

10. **Customer NPS below target** — Customer NPS of 9 in 2025 fell below the target range of 12–16 and below 2024's score of 12. SAP is switching to Cloud CSAT as its 2026 KPI. This is a retention/churn risk indicator worth investigating in the earnings call.

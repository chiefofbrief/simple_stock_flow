# Guidance Index

Analysis guidance files and prompts for LLM-driven analysis workflows.

## Foundational Frameworks (`guidance/frameworks/`)

| File | Description |
|------|-------------|
| `stock_analysis_guidelines.md` | Core investment principles: margin of safety, intrinsic value, GAAP vs. economic reality, analysis limitations. Draws from Graham/Dodd, Buffett, and financial theory. Required reading for all analysis prompts. |
| `ai_stock_analysis.md` | AI sector-specific framework: reflexive boom dynamics, ecosystem layers (compute/chips, infrastructure/power, models/tools, applications), circular revenue loop, exit signals. Used in conjunction with Stock Analysis Guidelines for AI stocks. |

---

## Analysis Prompts (`guidance/prompts/`)

Structured prompts designed for `@[prompt file]` invocation with script outputs.

| File | Purpose | Data Inputs |
|------|---------|-------------|
| `news_analysis.md` | Market news synthesis: macro overview, AI ecosystem positioning, investment flags, screening candidates with investigation items. | `discovery.py` daily/weekly digest |
| `screening_analysis.md` | Preliminary screening: price behavior, earnings trends, price-earnings correlation, P/E positioning. Filter to identify candidates worth deeper analysis. | `prices.py`, `earnings.py`, `valuation.py` |
| `sentiment_analysis.md` | Multi-source sentiment synthesis: cross-source themes, material events, narrative validation, perception vs. reality gaps, investigation items. | `sentiment.py` master output |
| `statement_analysis.md` | Deep financial analysis: 8 projection seeds, 13 priority metrics (8 undervaluation + 5 risk), 17 secondary metrics. Three-dimension framework (absolute/trends/volatility). | `financial_statements.py` master output |
| `notes_analysis.md` | Notes & MD&A disclosure analysis: investigation-driven search of SEC filings, red flag scan, synthesis. Builds on prior statement and sentiment analyses. | `sec_filings.py` output + prior analyses |

---

## Workflow Sequence

See **`docs/CLAUDE.md` → Default Workflow** for the standard 5-step pipeline and system initiative expectations.

---

## Key Concepts

**Projection Seeds:** 8 fundamental metrics for forward projections (Revenue, COGS%, SG&A%, R&D%, D&A, CapEx, Debt, Working Capital)

**Priority Metrics:**
- 8 undervaluation metrics: FCF, OCF, NCAV, ROTC, ROE, Operating Leverage, Revenue trends, Operating Margin
- 5 risk metrics: Debt/OCF, Accruals Gap, OCF/Net Income, D&A, Working Capital trends

**Three-Dimension Analysis:** Metrics analyzed across absolute level & peer positioning, trends & divergences, volatility & outliers

**Investigation Items:** Questions raised during analysis requiring further research through multiple data sources (financial statements, news, web searches, etc.)

---

## Glossaries (`guidance/glossaries/`)

Referenced by analysis prompts for metric interpretation.

| File | Coverage |
|------|----------|
| `seeds.md` | Interpretation guidance for 8 projection seeds |
| `priority_metrics.md` | Interpretation guidance for 13 priority metrics |
| `secondary_metrics.md` | Interpretation guidance for 17 secondary metrics |
| `notes.md` | Search terms, red flag patterns, and interpretation guidance for disclosure analysis |

---

## Analysis Output Conventions

Outputs are saved to `data/tickers/{TICKER}/`:
- Screening analysis: Prepended to `data/screening/Daily_Screening_YYYY-MM-DD.txt`
- Statement analysis: Prepended to `{TICKER}_statements.md`
- Sentiment analysis: Prepended to `{TICKER}_sentiment.md`
- Notes & MD&A analysis: Prepended to `{TICKER}_notes_mda.md`
- News analysis: Appended to discovery digest or separate file

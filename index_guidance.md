# Guidance Index

Analysis guidance files and prompts for LLM-driven analysis workflows.

## Guidance Files (`Guidance/`)

### Foundational Frameworks

| File | Description |
|------|-------------|
| `Stock Analysis Guidelines.md` | Core investment principles: margin of safety, intrinsic value, GAAP vs. economic reality, analysis limitations. Draws from Graham/Dodd, Buffett, and financial theory. Required reading for all analysis prompts. |
| `AI Stock Analysis.md` | AI sector-specific framework: reflexive boom dynamics, ecosystem layers (compute/chips, infrastructure/power, models/tools, applications), circular revenue loop, exit signals. Used in conjunction with Stock Analysis Guidelines for AI stocks. |

---

### Analysis Prompts

Structured prompts designed for `@[prompt file]` invocation with script outputs.

| File | Purpose | Data Inputs |
|------|---------|-------------|
| `News Analysis Prompt.md` | Market news synthesis: macro overview, AI ecosystem positioning, investment flags, screening candidates with investigation items. | `discovery.py` daily/weekly digest |
| `Screening Analysis Prompt.md` | Preliminary screening: price behavior, earnings trends, price-earnings correlation, P/E positioning. Filter to identify candidates worth deeper analysis. | `prices.py`, `earnings.py`, `valuation.py` |
| `Sentiment Analysis Prompt.md` | Multi-source sentiment synthesis: cross-source themes, material events, narrative validation, perception vs. reality gaps, investigation items. | `sentiment.py` master output |
| `Statement Analysis Prompt.md` | Deep financial analysis: 8 projection seeds, 13 priority metrics (8 undervaluation + 5 risk), 17 secondary metrics. Three-dimension framework (absolute/trends/volatility). | `financial_statements.py` master output |

---

## Typical Workflow Sequence

From `CLAUDE.md`:

```
Discovery → Screening → Analysis (Sentiment + Fundamentals) → Iterative Investigation
```

1. **Discovery** - `discovery.py` → `News Analysis Prompt.md`
2. **Screening** - `prices.py`, `earnings.py`, `valuation.py` → `Screening Analysis Prompt.md`
3. **Sentiment Analysis** - `sentiment.py` → `Sentiment Analysis Prompt.md`
4. **Fundamental Analysis** - `financial_statements.py` → `Statement Analysis Prompt.md`
5. **Iterative Investigation** - Use indexes, sources, and additional tools

---

## Key Concepts

**Projection Seeds:** 8 fundamental metrics for forward projections (Revenue, COGS%, SG&A%, R&D%, D&A, CapEx, Debt, Working Capital)

**Priority Metrics:**
- 8 undervaluation metrics: FCF, OCF, NCAV, ROTC, ROE, Operating Leverage, Revenue trends, Operating Margin
- 5 risk metrics: Debt/OCF, Accruals Gap, OCF/Net Income, D&A, Working Capital trends

**Three-Dimension Analysis:** Metrics analyzed across absolute level & peer positioning, trends & divergences, volatility & outliers

**Investigation Items:** Questions raised during analysis requiring further research through multiple data sources (financial statements, news, web searches, etc.)

---

## Glossaries (Referenced by Analysis Prompts)

| File | Coverage |
|------|----------|
| `GLOSSARY_seeds.md` | Interpretation guidance for 8 projection seeds |
| `GLOSSARY_priority_metrics.md` | Interpretation guidance for 13 priority metrics |
| `GLOSSARY_secondary_metrics.md` | Interpretation guidance for 17 secondary metrics |

---

## Analysis Output Conventions

Outputs are saved to `data/analysis/{TICKER}/`:
- Screening analysis: Typically displayed in terminal (not saved)
- Statement analysis: `{TICKER}_ANALYSIS_statement.md`
- Sentiment analysis: `{TICKER}_ANALYSIS_sentiment.md`
- News analysis: Appended to discovery digest or separate file

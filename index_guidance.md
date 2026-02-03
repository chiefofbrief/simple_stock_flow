# Guidance Index

Analysis guidance files and skill files (prompts).

## Guidance Files (`Guidance/`)

High-level frameworks and prompts for analysis workflows.

| File | Description |
|------|-------------|
| `Stock Analysis Guidelines.md` | Core investment principles: margin of safety, intrinsic value, GAAP vs. economic reality, analysis limitations. Draws from Graham/Dodd, Buffett, and financial theory. |
| `AI Stock Analysis.md` | AI sector-specific framework: reflexive boom dynamics, ecosystem layers (compute/chips, infrastructure/power, models/tools, applications), circular revenue loop, exit signals. |
| `News Analysis Prompt.md` | Comprehensive news synthesis prompt: market/macro overview, AI ecosystem positioning, investment flags, screening candidates. Integrates multiple guidance sources and defines output structure. |

---

## Skill Files (`skills/`)

Task-specific analysis prompts for LLM execution. All marked as **DRAFT** status.

| File | Description | Data Inputs |
|------|-------------|-------------|
| `README.md` | Overview of skill file philosophy, workflow sequence, data flow, and output conventions. |
| `SKILL_screening.md` | Preliminary screening questions: price behavior, earnings trends, price-earnings correlation, P/E positioning. | `prices.py`, `earnings.py`, `valuation.py` outputs |
| `SKILL_statement_analysis.md` | Deep financial analysis: 8 projection seeds, 13 priority metrics (undervaluation + risk), three-dimension analysis (absolute/trends/volatility), investigation items. | `financial_statements.py` master output |
| `SKILL_news.md` | News coverage analysis: projection seed validation, investigation items, material events, narrative validation, sentiment. | `news.py` outputs (Perigon/AlphaVantage JSON) |
| `SKILL_sentiment_analysis.md` | Multi-source sentiment synthesis: cross-source themes, brand perception, signal vs. noise filtering. | `sentiment.py` master output |

---

## Analysis Workflow Reference

From `skills/README.md`:

```
Discovery → Screening → Statement Analysis → Sentiment/News → Synthesis
```

Typical script sequence:
1. `discovery.py` - Market scanning
2. `valuation.py`, `prices.py`, `earnings.py` - Screening inputs
3. `financial_statements.py` - Deep fundamental analysis
4. `sentiment.py` (or individual `news.py`) - External perspective
5. LLM synthesis using guidance and skill files

---

## Key Concepts

**Projection Seeds:** 8 fundamental metrics for forward projections (Revenue, COGS%, SG&A%, R&D%, D&A, CapEx, Debt, Working Capital)

**Investigation Items:** Flagged questions tracked in `{TICKER}_tracking.md` for resolution through multiple data sources

**Three-Dimension Analysis:** Metrics analyzed across absolute level, trends, and volatility

**Analysis Output Locations:** `data/analysis/{TICKER}/{TICKER}_ANALYSIS_[type].md` (screening not saved, others: statement, news, sentiment)

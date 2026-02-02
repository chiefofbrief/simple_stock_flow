# News Analysis Skill

**⚠️ DRAFT - This skill file is a preliminary draft and may require refinement based on actual usage patterns.**

## Context

**Purpose:** Analyze news coverage to validate or challenge company narrative and address investigation items from statement analysis.

**Available Data:**
- `{TICKER}_news_perigon.json` - Aggregated stories (default: 3 months)
- `{TICKER}_news_alphavantage.json` - Individual articles with sentiment scores (default: 3 months)
- `{TICKER}_tracking.md` - For context on investigation items from statement analysis

**Tool Guidance:** Use Explore agent for processing JSON files (they can be large). Read tool for targeted sections if needed.

---

## Key Questions to Address

Review the news JSON files and address:

### External Perspective on Projection Seeds
- Do news events affect confidence in any of the 8 projection seeds?
- Does news validate or challenge the historical baselines from statement analysis?

**The 8 Projection Seeds:**
Revenue, COGS %, SG&A %, R&D %, D&A, CapEx, Total Debt, Working Capital Components

### Investigation Items
- Do seed-linked investigation items from `{TICKER}_tracking.md` get addressed by news?
- Do non-seed investigation items get addressed?
- What new questions emerge from news coverage?

### Material Events & Sentiment
- Any material events affecting the investment thesis?
  - M&A/strategic developments
  - Competitive dynamics
  - Market reactions (analyst upgrades/downgrades)
  - Regulatory/legal (external developments)
- What is current sentiment? (Last 30 days + trend over full period)
- Any outlier sentiment events?

### Narrative Validation
- Where does news validate the company's narrative (from filings/calls)?
- Where does news contradict or challenge?
- Where is news silent despite relevance?

---

## Output Guidance

Provide a news analysis addressing the questions above. Include:

- **Material findings:** Events, themes, or sentiment affecting the thesis (cite headlines, dates, sources)
- **Investigation items:** What gets addressed, what's new, what's unresolved
- **Sentiment assessment:** Current tone, trend, outliers
- **Narrative check:** Where news validates vs. contradicts company statements

**Flexibility:** Focus on materiality. News may be silent on some items - that's informative too. Let importance drive depth.

---

## Notes

**Data Sources:**
- Perigon: Aggregated stories with source clustering
- AlphaVantage: Individual articles with sentiment scores (-1 to +1)

**Materiality:**
- Focus on events affecting fundamentals, not just price movements
- Multiple sources provide validation
- Analyst commentary on financial metrics is particularly relevant

**Integration:**
- Statement analysis establishes baseline and investigation items
- News provides external validation or challenge
- Track significant findings in `{TICKER}_tracking.md`

**Remember:** External perspective is valuable but not definitive. Contradictions warrant investigation - who's right?

# Sentiment Analysis Skill

**⚠️ DRAFT - This skill file is a preliminary draft and may require refinement based on actual usage patterns.**

## Context

**Purpose:** Synthesize sentiment across multiple sources to understand external perspectives on the stock.

**Available Data:**
- `{TICKER}_sentiment.md` - Aggregated sentiment from master script (news, reddit, tiktok, youtube)
- `{TICKER}_tracking.md` - For context on investigation items from statement analysis

**Data Sources in sentiment markdown:**
- **News** (3-month default): Institutional/analytical perspective
- **Reddit** (30-day default): Retail investor perspective
- **TikTok/YouTube** (this-month default): Consumer/brand perspective

---

## Key Questions to Address

Review the sentiment markdown and address:

### Multi-Source Sentiment
- What is the overall sentiment across sources? (Institutional, retail, consumer)
- Where do sources converge vs. diverge? What does this reveal?
- Are there notable sentiment shifts or outlier events? When and why?

### Material Themes & Events
- What recurring themes emerge across multiple sources?
- Any material events affecting the investment thesis?
  - M&A/strategic developments
  - Competitive dynamics
  - Product/service reception
  - Brand perception shifts

### Investigation Items
- Do any investigation items from `{TICKER}_tracking.md` get addressed by sentiment?
- What new questions or concerns emerge from sentiment analysis?

### Narrative Validation
- Where does sentiment validate the company's narrative (from filings/calls)?
- Where does sentiment contradict or challenge the narrative?
- What's missing? Where is sentiment silent despite relevance?

---

## Output Guidance

Provide a sentiment synthesis that addresses the questions above. Include:

- **Cross-source summary:** Where sources agree, where they diverge, and what this means
- **Material findings:** Key themes, events, or signals affecting the thesis
- **Investigation items:** What gets resolved, what's new, what remains unanswered
- **Assessment:** How does sentiment affect your view of the investment case?

**Flexibility:** Let materiality drive the analysis. Some sources may be more relevant than others depending on the company (e.g., consumer brands vs. enterprise software). Format can adapt to the situation.

---

## Notes

**Source Perspectives:**
- News: Analyst opinions, institutional coverage, market reactions
- Reddit: Retail sentiment, price catalysts, community discussion
- Social media: Brand perception, consumer feedback, viral moments

**Materiality:**
- Look for themes across multiple sources or sustained coverage
- One-off posts or isolated comments are less meaningful
- Focus on sentiment that might affect fundamentals or valuation

**Integration:**
- Statement analysis establishes baseline and investigation items
- Sentiment adds external perspective and validation
- Track significant findings in `{TICKER}_tracking.md`

**Remember:** Sentiment complements fundamentals but doesn't replace them. Divergence between sentiment and strong fundamentals can reveal opportunities.

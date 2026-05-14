# Software Prompt Edits — Working Log

Base prompt: `prompt_the_context_v1.md` → `prompt_the_context_software.md`
Approach: v1 as base, targeted additions. No verbatim changes to base text unless explicitly approved.

---

## prompt_the_context_software.md

### Role paragraph
**Approved text:**
> You are an expert financial analyst conducting the Context step of a three-pass investment analysis for **{TICKER}**, a software company navigating AI disruption. Your purpose is to form a preliminary, testable hypothesis before touching the financial statements — assessing not just what the business does, but what scenario the current price embeds, whether AI represents a net threat or opportunity to the core business, and where sentiment sits relative to demonstrated results. The financial statements in Pass 1 will verify or complicate this picture — not build it from scratch.

### Step 1 files — Conditional block
No change. SC index remains Conditional as in v1.

### Q2 (Counter-narrative from Reddit)
No change.

### Section 2 — Analyst Consensus (Q3/Q4)
No change.

### Q17 (Narrative Pre-check — minor edit)
**Approved text:**
> Is there institutional consensus around undervaluation, a compounder thesis, or a recovery/AI monetization case?

### Q18 (Narrative Pre-check)
No change.

---

## prompt_the_numbers_software.md

### Role paragraph
**Approved text:**
> You are conducting Pass 1: The Numbers for **{TICKER}**, a software company navigating AI disruption. Your purpose is to determine whether the business's financial health confirms or disputes the preliminary hypothesis established in the Context step. The earnings call and synthesis in Pass 2 will test whether the thesis is timely — your job here is to establish whether the business itself warrants a thesis at all.

### Step 1 files — Conditional block
No change. SC index remains Conditional as in v1.

### Metrics (Revenue, Capex & D&A, Debt Profile)
No change.

### Synthesis Q4 (new question)
**Approved text:**
> **4. Is AI investment translating to measurable revenue or margin impact — or is it still a cost without demonstrated payoff?**
> What do the financials show about AI-related spending vs. any visible contribution to revenue growth, margin expansion, or competitive positioning? Is the investment phase compressing or extending?

*(AI supply chain version label not needed — this is the software version's equivalent.)*

### Self-Check (additions)
**Approved text:**
> - Has the AI & Competitive Position mandatory grep section been completed — all terms searched and findings interpreted?
> - Has Synthesis Q4 been answered with specific financial evidence, not generic assertions?

### Accounting Cat 2 — bullet edit
**Approved text:**
> - Capitalization policies for software development, internal costs, and internally developed AI features — costs expensed vs. capitalized, and whether the policy has changed

(Replaces: "Capitalization policies for software development, internal costs, or other discretionary items")

---

## prompt_the_projection_software.md

### Role paragraph
**Approved text:**
> You are conducting Pass 2: The Projection for **{TICKER}**, a software company navigating AI disruption. Your purpose is to read the most recent earnings call against the financial picture already established, assess whether the thesis is timely, and produce the final assessment. The Context step formed the hypothesis and established the narrative picture. The Numbers step tested it against the financials. This step asks: does management's most recent account of the business hold up, and is there a credible path to price realization?

### Step 1 files — Conditional block
No change. SC index remains Conditional as in v1.

### Self-Check (additions)
**Approved text:**
> - Have the Reflexivity and AI Disruption Position dimensions been answered with specific evidence from all three passes — not generic assertions?
> - Have the Q5 risk-side and upside-side tracking items been explicitly addressed?

### Synthesis — Invalidation section (new)
**Approved text:**
> **Invalidation**
> Specific, observable developments that would make this thesis wrong and trigger reassessment or exit. Not "fundamentals deteriorate" — name specific metrics, events, or thresholds.

### Synthesis — two new dimensions (after Scenario)
**Approved text:**

> **Reflexivity**
> Where does this company sit in the reflexivity cycle (Soros)? Assess the negative loop explicitly: AI fear → price drop → multiple compression → talent/customer confidence erosion → weaker results → more fear. Is this loop already in motion — and if so, how far has it progressed? Is there evidence of reversal, or is it self-reinforcing?

> **AI Disruption Position**
> Where does this company sit on the AI disruption spectrum — defending a legacy moat, actively transforming via AI, or both? What evidence from all three passes supports that position, and what would signal that the disruption risk is accelerating or that the monetization opportunity is materializing?

### Q5 (addition)
**Approved text:**
> In addition, the following must be explicitly tracked regardless of whether they appeared in the open questions list:
>
> *Risk side:* (a) Is AI disrupting the core business in ways management is not fully disclosing — seat reductions, churn, or pricing pressure from consumption/agent-based alternatives? (b) Is AI investment compressing margins with no demonstrated ROI timeline?
>
> *Upside side:* (c) Are AI features driving measurable revenue uplift — new pricing tiers, attach rates, or expansion revenue? (d) Is net revenue retention improving, or does management's account suggest AI monetization is accelerating ahead of current financials?

### Q3
**Approved text:**
> **Q3. What is management saying about the path forward — guidance figures, growth targets, margin trajectory? Where does guidance diverge from the historical trend established in The Numbers?**
> Summarize explicit forward guidance figures. Label all as forward-looking. Where guidance implies acceleration or deceleration relative to the historical trend, flag the delta. Where management cites adjusted figures, check whether the GAAP equivalent is disclosed. On AI investment specifically: is spending expected to compress or expand margins near-term, and over what timeframe does management expect a return?

### Q2
**Approved text:**
> **Q2. Does management's characterization of business performance align with what The Numbers established — or are there notable deflections, omissions, or contradictions? Where does the call add context that the financial statements couldn't?**
> Cite specific excerpts from both calls. Note where they differ from each other and where either diverges from the findings in The Numbers. What did management say that the financials could not have told us? Pay particular attention to: (a) how management characterizes AI's impact on the business — threat, opportunity, or both — and whether this is backed by specific metrics or framed in general terms; (b) any AI monetization or adoption progress not visible in the financial statements — pricing changes, customer wins, product adoption rates.

### TODO — also apply to prompt_the_numbers_ai.md
Same base list header change ("Common terms to consider:" → "Flag-driven searches (run for each flag raised in Metrics):") to prevent LLM treating base searches as optional.

### Targeted Searches — base list header change
**Approved text:**
> **Flag-driven searches (run for each flag raised in Metrics):**

(Replaces "Common terms to consider:" — no change to the list itself.)

### Targeted Searches — mandatory addition
**Approved text:**
> **AI & Competitive Position — always run regardless of Metrics flags.** Grep `{TICKER}_notes.md` and `{TICKER}_mda.md` for the following terms. For each search, record findings and interpret what they reveal:
>
> - `artificial intelligence` / `AI` — surface any AI-specific product, investment, or risk disclosures
> - `remaining performance obligation` / `RPO` — quantify contracted forward revenue
> - `net revenue retention` / `net dollar retention` — customer expansion and churn signals
> - `capitalized software` / `internal-use software` — how AI development costs are being treated
> - `consumption` / `credit` / `usage-based` — flags pricing model shifts away from seats
> - `seat` / `per seat` — confirms or tracks seat-based model
> - `agent` / `agentic` — surfaces AI agent product disclosures
> - `OpenAI` / `Microsoft` / `Anthropic` / `Copilot` / `Gemini` — named AI partnerships or competitive references
> - `competi` — surface named competitors from the competition or risk sections

### Self-Check (addition)
**Approved text:**
> - Have I answered Q16 (AI initiatives, ROI, investment timeline) and Q19 (AI threat vs. opportunity framing) — not generically but with specific evidence from the data files?

### Q20, Q21 (Preliminary Hypothesis — renumbered from Q19, Q20)
No changes to content. Renumbered due to new Q19 insertion.

### Q19 (Narrative Pre-check — new question)
**Approved text:**
> **Q19. Is AI a net threat or net opportunity to this business — and which does the market appear to be pricing?**
> Is the price decline primarily driven by AI disruption fear, or by fundamental deterioration unrelated to AI? Is there evidence the market is overestimating the threat, underestimating the opportunity, or correctly pricing both?

### Q16 (MD&A — new question)
**Approved text:**
> **Q16. What is management saying about AI — and is there evidence of real impact?**
> What AI initiatives or products is the company pursuing, and is AI framed as a threat to the core business, an enhancement of it, or both? What ROI or monetization signals exist — attach rates, new pricing tiers, customer adoption metrics, or revenue contribution? What is the stated investment cost and timeline for returns — is AI spending still in "investment mode" with no demonstrated payoff, or is monetization beginning to show in the results?

### Q8, Q9, Q10 (Price & Earnings — LOSER/TAILWIND tags removed, made unconditional)
**Approved text:**
> **Q8. Is the current price drop an anomaly relative to the long-term trend, or consistent with it?**

> **Q9. Is the price decline tracking real fundamental deterioration, or is the market overreacting to a healthy business?**

> **Q10. What does the price/earnings relationship reveal?**
> Compare the price trajectory against the earnings trajectory directly — where are they diverging, converging, or moving in sync, and by how much? Is the price decline tracking real earnings deterioration — or is there a disconnect between the market's judgment and the underlying business? This is the central conclusion the preceding questions build toward.

### Q1 (Sentiment Landscape)
**Approved text:**
> **Q1. What is the mainstream narrative?**
> What are news headlines and analyst Q&A questions focused on and concerned about? What is the market's current story for this stock — the dominant concern, theme, or thesis driving coverage? Is the narrative grounded in demonstrated results, or driven by fear of AI disruption not yet reflected in the financials? Is there a gap between what the market is concerned about and what the company has actually reported? Conversely, is the market underweighting genuine AI monetization progress?

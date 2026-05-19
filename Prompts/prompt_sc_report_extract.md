# SC Report Extract Prompt (Gemini)

## Role

You are extracting verbatim passages from an attached company filing to support AI supply chain investment research. Your only job is to read the attached content and copy relevant text under six labeled categories. You do not analyze, summarize, or interpret anything.

**Output:** Provide your entire response as a single markdown code block.

---

## Reading Instruction

Read the entire attached content before extracting anything. Do not skim or keyword-search. Read for meaning — a passage about demand buried in Risk Factors is still relevant to Category 2, even if the section heading doesn't match.

**Rules:**
- Copy passages **exactly as written** — every figure, percentage, dollar amount, qualifier, and hedging phrase intact
- Do **not** paraphrase, compress, or reword — not even one sentence
- Do **not** add commentary or transitions between excerpts
- If multiple passages address the same category, include all of them — separate with a blank line and label the source section in brackets: `[Risk Factors]`, `[MD&A]`, `[Results of Operations]`, etc.
- Named companies, customers, and specific figures are always higher priority than generic language — "robust hyperscaler demand" is worth less than a sentence naming Microsoft alongside a dollar figure
- If a category is genuinely not addressed in the attached content: write `Not found.`

---

## Categories

**Category 1 — AI Supply Chain Role**
What does this company do in the AI ecosystem, in its own words? Look for: product or service descriptions tied to AI infrastructure, chip design, AI workloads, data centers, or AI-enabled hardware. Extract the passages that most directly defines their AI-specific role — not a general company overview.

**Category 2 — Demand Evidence**
What AI-driven demand is the company seeing, and from whom? Prioritize: named customers or customer types (specific companies, hyperscalers, cloud providers, AI labs), quantified demand (backlog figures, order rates, revenue attributed to AI, contract values), and language about committed versus anticipated demand. The distinction between "we have $X contracted" and "we expect strong demand" matters — extract both if both appear, and preserve the exact language.

**Category 3 — Capital Deployment**
What is the company investing in, and how much? Look for: capital expenditure figures and trajectories, R&D spending tied to AI, specific infrastructure or product buildout descriptions with dollar amounts, named facilities or programs. Extract passages with numbers. Skip generic "we are investing in AI" language unless it includes a specific figure or named initiative.

**Category 4 — Monetization and Returns**
What revenue is the company generating from AI investments, and what does management say about the timeline for returns? Look for: revenue attributed to specific AI products or features, pricing model descriptions (seat-based, consumption, token/credit-based), stated timelines for when investments are expected to generate returns, language about whether current buildout is backed by contracted demand or is speculative. This is the "what's coming back" category — extract any passage where management describes the path from investment to revenue.

**Category 5 — Supply Constraints and Bottlenecks**
What is this company unable to fully deliver, and what is gating its own growth or its customers' operations? Look for: capacity constraint language, lead time disclosures, supply shortages affecting the company or its customers, production limits, statements about demand exceeding supply. Passages where management says they cannot meet demand, or where an input or resource is described as tight or limited, are the target.

**Category 6 — Competition**
Who are the named competitors, and how does management characterize their competitive position? Look for: specific company names identified as competitors, market share language with figures, descriptions of competitive moat or structural advantage, pricing pressure from named players. 

---

## Output Format

````markdown
## [Company Name] ([TICKER])
*Source: [Document type — 10-K / 10-Q / MD&A / Earnings Transcript / etc.], [Period]*

### 1. AI Supply Chain Role
> [verbatim]

### 2. Demand Evidence
> [verbatim]

### 3. Capital Deployment
> [verbatim]

### 4. Monetization and Returns
> [verbatim]

### 5. Supply Constraints and Bottlenecks
> [verbatim]

### 6. Competition
> [verbatim]
````

## LLM Agreement

**Respond to the following prior to starting the task**:
- Do you understand and agree to this task?
- Have you thoroughly read the instructions?
- Will you read the source material in full at the start of the process? Every single word?
- Will you extract ALL relevant excerpts without paraphrasing, condesning, etc.?

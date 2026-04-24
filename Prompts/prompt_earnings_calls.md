# Earnings Call Analysis Prompt

## Role
You are an expert financial analyst. Your task is to analyze the provided earnings call transcripts for **{TICKER}** and produce a concise, insightful report.

---

## Step 1: Gather Context

### Required Context
Read the following before doing anything else:
- `GEMINI.md` — The foundational Analysis Philosophy & Guidelines.
- `Data/tickers/{TICKER}/{TICKER}_Thesis.md` — The stock's thesis, including all prior analyses (Financials, Footnotes & MD&A, Sentiment).
- `Data/tickers/{TICKER}/{TICKER}_earnings_remarks.md` — Prepared remarks for the last two quarters. Run: `python Scripts/earnings_calls.py {TICKER}`
- `Data/tickers/{TICKER}/{TICKER}_earnings_qa.md` — Q&A session for the last two quarters. Run: `python Scripts/earnings_calls.py {TICKER}`
- If `{TICKER}` has an `AI SC` Sector Theme (check `Stock_Tracker.md` or `{TICKER}_Thesis.md`), read the relevant layer section of `context_ai_supply_chain.md`.

**STOP. Wait for user approval before proceeding to Step 2.**

---

## Step 2: Analyze & Generate Report

### Analysis Guidelines
- Analyze the transcripts to answer the questions in the Output Format below.
- All insights must leverage the provided transcripts. Explicitly cite specific statements or excerpts that led to your conclusion.
- Cross-reference against all prior analyses in the Thesis file — the earnings call is the lens through which management's narrative is tested against the hard data.
- **Call Weighting:** The two calls are not equal in strategic weight. The call covering full-year results and annual guidance typically contains the more material disclosures — long-term targets reiterated or revised, annual segment performance, and the strategic reset for the coming year. The more recent call is usually incremental. Identify which call carries more weight before beginning the analysis, and ensure both are read with equal care. Where the two calls diverge in tone, data, or emphasis, note it explicitly.
- **Open Questions Check:** Before answering the output questions, return to the **Footnotes & MD&A** section of the Thesis. List every item explicitly flagged for Earnings Call investigation. For each, state: (a) whether management addressed it on either call, (b) what was said (with citation), and (c) whether the answer strengthens, weakens, or leaves the thesis unchanged. Items not addressed should be flagged as unresolved and carried forward to the Research phase.
- **Reference:** Consult `Source Material/summaries/` when an item would benefit from additional context, especially as it pertains to fundamental analysis, reflexivity theory, and boom/bust models. Refer to `Source Material/summaries/insights_index.md` for a thematic map. *CRITICAL WARNING: Do not access Source Material/raw/ without explicit user permission to avoid burning compute.*
- **Quality bar:** See the **Example Analysis** at the bottom of this prompt. It illustrates the required level of rigor, depth, and specificity — how management statements are cited and tested against prior analyses, how tone shifts between calls are identified, and how open questions from prior phases are tracked to resolution or escalated. Do not replicate its findings or structure mechanically; every company's earnings calls present different patterns and challenges.
- **Forward vs. backward labeling (required):** Management guidance figures (EPS targets, margin baselines, growth rates) are forward-looking and must be labeled as such. Do not blend guidance with historical actuals in the same valuation argument. Where forward guidance diverges from historical trends, flag the delta explicitly.
- **GAAP vs. adjusted labeling (required):** When management cites non-GAAP figures (adjusted EPS, non-GAAP operating income, adjusted EBITDA), label them explicitly as adjusted and note whether the GAAP equivalent is available. Do not accept management's adjusted framing without checking whether the excluded items are genuinely non-recurring.
- **Cross-section consistency (required):** For every figure cited from the earnings call that also appears in the Financials or Footnotes sections, verify consistency. Management-stated figures that contradict prior analysis conclusions must be flagged and investigated — not silently adopted.

### Deliverable

**Questions:**
1. **Data Check:** Have all findings been sourced directly from the earnings call transcripts — no outside data introduced?
2. **Call Weighting Check:** Has the more strategically material call been identified, and have both calls been read with equal care?
3. **Cross-Reference Check:** Has each significant management claim been evaluated against the prior financial, footnotes, and sentiment analyses?
4. **Open Questions Check:** Has every item flagged in the Footnotes phase for Earnings Call investigation been explicitly addressed or flagged as unresolved?
5. **Tone Check:** Has language and tone been assessed for shifts relative to the prior call?
6. **Summary Check:** Does the Earnings Call Summary accurately reflect the findings?
7. **Labeling Check:** Are all forward-looking figures (guidance, targets) labeled as such, and all non-GAAP figures labeled as adjusted? Are historical actuals and forward guidance kept separate in valuation arguments?
8. **Consistency Check:** Have all figures cited from the calls been verified against the Financials and Footnotes sections? Any discrepancy must be resolved and documented.

### Output Format

#### {TICKER} Earnings Call Analysis

**Call Orientation**
[1–2 sentences identifying which of the two calls carries more strategic weight and why — e.g., full-year results + annual guidance vs. incremental quarterly update. This frames the weighting applied throughout the analysis.]

**1. Does management's characterization of the business align with previous analyses — or are there notable deflections, omissions, or contradictions?**
[Answer using specific excerpts or citations from the transcript. Draw from both calls; note where they differ.]

**2. Are there any explanations that add meaningful context to specific findings from the previous analyses?**
[Answer using specific excerpts or citations from the transcript]

**3. Has management's language or tone shifted relative to the prior call — increased hedging, new risk disclosures, or topics that have quietly disappeared from discussion?**
[Answer using specific excerpts or citations from the transcript]

**4. What are analysts concerned or excited about?**
[Answer using specific excerpts or citations from the transcript]

**5. How do analysts' focus areas align with our previous analyses?**
[Answer using specific excerpts or citations from the transcript]

**6. Were the open questions from the Footnotes phase resolved?**
[List each item flagged for Earnings Call investigation in the Footnotes & MD&A section. For each: state whether it was addressed, cite what was said, and assess whether the answer strengthens, weakens, or leaves the thesis unchanged. Flag any items that remain unresolved and should carry into the Research phase.]

**Earnings Call Summary**
[A concise paragraph summarizing the findings. This text will be copied to the Thesis file.]

- **Action:** Ask: *"Do you approve this analysis? Should I update the Thesis file and Stock Tracker?"*

**STOP. Wait for user approval before proceeding to Step 3.**

---

## Step 3: Commit

Upon explicit user approval:
- Update **### Earnings Calls** in `Data/tickers/{TICKER}/{TICKER}_Thesis.md` with the full analysis.
- Update `Stock_Tracker.md` — advance **Current Phase** for `{TICKER}` to the next phase.

**STOP. Wait for user approval before committing.

---

## Example Analysis

The following is a completed Earnings Call Analysis for INTU (Intuit). It is included to illustrate the required level of rigor, depth, and specificity — how management statements are cited and tested against prior analyses, how tone shifts between calls are identified, how open questions from the Footnotes phase are tracked to resolution or escalation, and how analyst Q&A is used to surface gaps. Do not replicate its findings or structure mechanically; every company's earnings calls present different patterns and challenges.

---

#### INTU Earnings Call Analysis

*Two calls reviewed: Q4 FY2025 (August 2025, full-year results) and Q1 FY2026 (November 2025). The Q4 call is the more strategically material of the two — it covers the full tax season outcome, the AI agent platform launch, and the FY2026 guidance set. The Q1 call is largely incremental confirmation.*

**1. Does management's characterization of the business align with previous analyses — or are there notable deflections, omissions, or contradictions?**
Management's characterization strongly aligns with the top-line performance identified in the Financials phase. Q1 FY2026: revenue $3.9B (+18%), Online Ecosystem +21% (+25% ex-Mailchimp), mid-market (QBO Advanced + IES) ~40% Online Ecosystem revenue growth, Credit Karma +15% (credit cards 10pts, auto insurance 3pts), Desktop decelerating to 6% heading to low single-digits. These confirm the secular narrative.

The Q4 FY2025 call contained the most important single data point across both calls: TurboTax Live grew 47% in FY2025 — a 30-point acceleration from the prior year — with customer growth of 24%. This is the most direct evidence that INTU is successfully pivoting the consumer segment toward high-value assisted tax, which is structurally important for the thesis and largely absent from the Footnotes analysis. Management also disclosed that Credit Karma drove 1 full point of TurboTax revenue growth in FY2025 — the TurboTax/Credit Karma platform flywheel is no longer theoretical. Additionally, the Q4 call confirmed IES billed new customers in Q4 were "up nearly 2x versus Q3," with one customer (200+ entities) expanding immediately after signing. On the Q1 call, IES contract count at quarter-end was "nearly 50% higher than at the end of Q4" — this velocity signal was not mentioned in prepared remarks for Q1 and is more forward-looking than the revenue growth rate. QuickBooks Live customer growth of 61% in Q1 — the B2B analog to TurboTax Live — received one sentence in prepared remarks but confirms the done-for-you model is gaining traction on both sides of the platform.

On profitability quality: management heavily promoted Non-GAAP operating income ($1.3B vs. $953M in Q1, GAAP operating income +36% for FY2025) without disclosing the $2.02B SBC burden or the $208M YoY restructuring reversal embedded in the FY2025 GAAP comparison. This is standard earnings call practice — full GAAP reconciliations are in the press release — but the gap between Non-GAAP framing and true owner earnings ($4.82B) is not visible to a listener focused only on the call. The IRS Direct File threat is absent from both calls and from the MD&A; management's silence is noted but requires context (see question 3 below).

**2. Are there any explanations that add meaningful context to specific findings from the previous analyses?**
Six operational details materially update or extend the prior analyses:

- **Pricing Exhaustion:** CFO Aujla explicitly attributed the deceleration in Online Services to 17% (Q1) to lapping prior-year pricing in payments and payroll: "less pricing pressure heading into fiscal '26 compared to what we experienced in '25." Future GBS top-line growth must come from volume and mix, not pricing. This is the single clearest headwind to the 15-20% long-term GBS growth target.
- **Mailchimp Drag and Lag:** Mailchimp revenue was down slightly in both Q4 and Q1. Management explained the pull-back on marketing was intentional while fixing "product and onboarding friction" for small businesses. The ~6-month subscription lag means a double-digit exit rate in Q4 FY2026 requires the product fixes to land by early calendar year 2026. Both the CEO and CFO confirmed this is tracking to plan.
- **Customer Attrition Beat Post-Pricing Change:** CFO Aujla on the Q1 call: "even after we did the price changes and the lineup innovation there last July, we saw that our customer attrition again came in below our expectations." This is direct evidence of pricing power and customer stickiness absent from both the financial and footnotes analyses. It materially strengthens the durability argument in the LOSER thesis.
- **Online ARPC Acceleration:** The Q4 call disclosed that Online Ecosystem ARPC growth accelerated more than 3 points to 14% in FY2025 — the highest in recent history, driven by mix shift toward mid-market. This is the financial confirmation that the upmarket push is monetizing, not just adding contract volume.
- **Credit Karma Lightbox and Flywheel:** The 32% FY2025 and 15% Q1 growth was explained as market share gains in personal loans and credit cards facilitated by Lightbox (financial partners embed proprietary credit models directly in INTU's ecosystem, enabling pre-approved offers without hard credit pulls). Long-term guidance reaffirmed at 10-15% for Credit Karma, based on "year-round benefits that lead to engagement, monetization, and TurboTax growth."
- **AI Search Risk Rebuttal (Q4 call):** Management's response: <15% of INTU's entire portfolio comes from search; AI search is currently ~1% of total traffic; Credit Karma relies on in-app users, not SEO. The CFO added that AI search traffic "converts significantly better through the sales funnel" — presenting it as a potential tailwind. This does not eliminate the risk entirely but substantially reduces it as a near-term concern.

**3. Has management's language or tone shifted relative to the prior call — increased hedging, new risk disclosures, or topics that have quietly disappeared from discussion?**
The Q4 call tone was confident and forward-leaning — management was describing a peak-year result (TurboTax Live 47%, Credit Karma 32%) and issuing initial FY2026 guidance of 12-13% total revenue growth. Importantly, this guidance implies a deceleration from 16% in FY2025, which was not foregrounded. The deceleration is structurally explained by pricing exhaustion and Mailchimp, but it represents a step-down from recent performance, not an acceleration.

By Q1, macro hedging increased modestly. Goodarzi noted consumers are "stretched" and "very intentional about where they spend money," citing Gen Z credit card balances up 20-30% and subprime/near-prime credit scores down ~10 points. In B2B, real estate, advertising, and some manufacturing segments are "down significantly." The critical qualifier present in both calls: these conditions have stabilized — "credit scores have sort of stabilized," credit card balances "have generally stabilized." This is a meaningful difference from deteriorating conditions. CFO Aujla hedged Credit Karma's H2 trajectory: "the comps do get harder as we lap prior year's strong performance." International headwinds on paying customer growth (online paying customers grew only 5% in FY2025, held down by Mailchimp and international) were disclosed on the Q4 call and never resurfaced on Q1 — the scope of the Mailchimp drag on international is an unresolved question.

The most significant new narrative on the Q1 call was the OpenAI/ChatGPT partnership: Intuit apps deeply integrated within ChatGPT, leveraging 800M weekly active users as a top-of-funnel acquisition channel with no revenue share, Intuit models and data remaining within INTU's "four walls." The unexamined risk: if customers discover and engage with financial products via ChatGPT, OpenAI owns the relationship context while INTU provides the backend. Whether this creates customer acquisition dependency on a third-party platform was not discussed. Management's framing of "it doesn't matter where the customer is, we enjoy the same economics" may be correct today but assumes partnership terms don't shift as OpenAI's own financial services ambitions evolve.

Capital allocation signals from both calls: $748M stock buyback in Q4, $851M in Q1, 15% dividend increase to $1.20/quarter. Management buying back aggressively at current prices is a direct endorsement of the LOSER thesis from the people with the most information.

**4. What are analysts concerned or excited about?**
Analysts are most excited about: the OpenAI partnership (questioning data privacy and economics); the rapid ~40% IES/QBO Advanced revenue growth and the accountant partnership flywheel; Credit Karma market share gains; and AI agent adoption (2.8M customers, 80%+ repeat usage, accounting agent saving up to 12 hours/month).

Concern focused on: U.S. consumer health and whether INTU's macro signals had deteriorated (answered directly by management, stabilization confirmed); the timeline for Mailchimp's re-acceleration; and the Online Accounting (+25%) vs. Online Services (+17%) delta — Kash Rangan specifically probed whether cross-selling momentum was stalling, attributing the delta correctly to pricing lap (confirmed by CFO).

On the Q4 call, analysts probed: AI agent monetization timeline (management: not in guidance, focused on engagement first); AI search risk and QuickBooks lead generation; the TurboTax Live playbook sustainability; Credit Karma cyclicality; and Mailchimp recovery timeline.

**5. How do analysts' focus areas align with our previous analyses?**
Analysts correctly tracked Mailchimp drag, the upmarket mix shift, consumer macro health, and Credit Karma cyclicality — all central to the prior analyses. On the Q4 call, the AI search risk question was asked and answered substantively, filling one of the gaps flagged in the Footnotes phase.

However, several thesis-relevant items went unprobed across both calls: no analyst asked about the IRS Direct File threat; no analyst challenged the gap between Non-GAAP and GAAP margins or the SBC burden; no analyst asked about international headwinds on paying customer growth beyond Mailchimp; and no analyst probed the OpenAI partnership for dependency risk. The SBC and restructuring omissions are a real gap but a nuanced one — sophisticated sell-side analysts have full GAAP reconciliations available and may have judged these as well-understood. The IRS Direct File silence is the more legitimate blind spot, though the TurboTax Live 47% result provides the most credible implicit rebuttal.

**6. Were the open questions from the Footnotes phase resolved?**
- **IRS Direct File threat:** Not addressed on either call or in the MD&A. However, the TurboTax Live 47% growth result is the most credible implicit rebuttal — IRS Direct File targets simple self-prepared returns while INTU's growth is concentrated in assisted tax. Thesis impact: partially resolved, risk reduced but not eliminated. Carry forward to Research phase.
- **AI disruption / search risk:** Addressed substantively on the Q4 call. Management's <15% search-traffic rebuttal and the "converts better" framing substantially reduce near-term concern. Thesis impact: strengthened. Resolved.
- **Mailchimp re-acceleration:** Timeline confirmed as Q4 FY2026, dependent on product fixes landing by early calendar year 2026. Management confirmed it is tracking to plan. Thesis impact: unchanged — monitoring required. Partially resolved.
- **OpenAI partnership risk:** Surfaced on Q1 call as new information not in prior phases. Dependency risk (OpenAI owning the relationship context) not addressed by management. Thesis impact: new open question. Carry forward to Research phase.
- **International headwinds:** Disclosed on Q4 call, not revisited on Q1. Scope beyond Mailchimp is unknown. Thesis impact: unresolved. Carry forward to Research phase.

**Earnings Call Summary**
The two calls together paint a picture that is more constructive than the prior analysis suggested. The single most important fact across both calls — TurboTax Live 47% growth in FY2025, a 30-point acceleration, with QuickBooks Live running at 61% in Q1 FY2026 — confirms that the done-for-you platform strategy is working on both sides of the business and represents a structural hedge against the IRS Direct File threat. ARPC accelerated 3+ points to 14%, IES contract count grew nearly 50% in one quarter, and customer attrition came in below expectations after a price increase: signals of pricing power and expanding monetization. Credit Karma's platform flywheel (1 point of TurboTax revenue growth, stabilized consumer health, Lightbox share gains) is now operational rather than theoretical.

The tension in the thesis remains: the FY2026 guidance of 12-13% total revenue growth is a step-down from 16%, driven by pricing exhaustion and Mailchimp; true owner earnings ($4.82B) are materially below the gross FCF ($6.84B) that first-pass analysis implies; the $208M restructuring tailwind inflates the FY2025 operating income comparison; international headwinds are underexplored; and the OpenAI partnership introduces a long-term platform dependency risk that management has not addressed. Management's aggressive capital return ($1.6B in buybacks across Q4+Q1, 15% dividend increase) is the clearest signal that they believe the stock is cheap at current prices — which, at ~17x owner earnings on an 18%+ revenue compounder with expanding margins, is a defensible view. The [LOSER] thesis holds, with the caveat that the next leg of growth must be volume- and mix-driven rather than price-driven.**

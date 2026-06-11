# AI ROI Analysis
*Date: 2026-06-11 | Source: Theses, earnings calls, and MD&A for META, MSFT, AMZN, CRM, SAP*

---

## TL;DR — Plain English Verdict

**META** — AI is already paying for itself in the one place it's deployed (ad targeting), but they're spending $130B+ a year on a "superintelligence" moonshot the CEO can't yet attach any revenue to. You're paying for a proven slot machine bolted to an unproven one.

**MSFT** — They're selling a ton of AI ($37B and growing fast), and people use Copilot daily, but the customers haven't actually proven it pays off on *their* books yet — Microsoft is openly waiting for that to happen before budgets reallocate. Quality business, ROI on the new spend is a "trust us, the cloud playbook worked last time."

**AMZN** — The most honest of the group: their CEO basically admitted enterprises are getting real value from AI mostly in cost-cutting (automation, fraud), not new revenue, and a big chunk of the demand is Amazon's own portfolio companies (Anthropic) buying Amazon's cloud with Amazon's money. Real engine, partly circular fuel.

**CRM** — Agentforce is growing 200%+ and is the cleanest "is the customer paying again" signal (top users spending 1.5x), but it's still only 2.6% of revenue and they're eating the AI model costs with zero margin benefit so far. Promising, immaterial, and quietly margin-dilutive today.

**SAP** — The sleeper: AI is attached to 66–90% of their big deals and is genuinely cutting customers' implementation costs, but that same tooling is shrinking their partners' billings and management is shifting to consumption pricing that may lower revenue per customer. AI is helping them win but might cannibalize the model.

---

## Is AI a Net Positive Right Now?

Yes — but a thin and lopsided one. Across all five, the demonstrated ROI is real but concentrated in two buckets: (1) the seller's own internal productivity (Amazon's 5-people-in-65-days, Salesforce's flat engineering headcount), and (2) customer **cost avoidance**. The thing the bull case actually needs — enterprises generating *new revenue* and measurably expanding their AI spend because the ROI is obvious — is largely still "starting to come to production" (Jassy's words) or undisclosed (CRM won't give NRR).

So the net-positive verdict rests on cost savings, which is real but inherently *capped* — you can only cut costs to zero. The uncapped, narrative-sustaining prize (AI-driven revenue growth) is not yet in the numbers. Nobody in this corpus is showing the revenue-side ROI that justifies the capex trajectory. They're showing efficiency, then asking you to believe efficiency becomes growth.

---

## Risk/Reward on the Capex, Right Now

**Asymmetric to the downside at the infrastructure layer, more balanced at the application layer.**

**The capex spenders (META, MSFT, AMZN)** are committing $130B–$200B/year *each* against ROI cases that are, by their own words, qualitative ("trajectory," "we're confident this will be the case"). The downside is clear and quantified (FCF compression, ROIC decline, $364B of obligations); the upside is real but unquantified and back-loaded. That's a poor risk/reward *shape* — you're funding a definite cost against a probabilistic, undated payoff. The saving grace is these are cash machines that can absorb the bet without blowing up.

**The application layer (CRM, SAP)** has better risk/reward because the bet is smaller, the demand signal is more direct (attach rates, expansion spend), and the downside is "growth disappoints" rather than "$200B of capex strands." But their upside is also capped by the consumption-pricing transition, which both are warning could compress revenue per customer.

**The trap in the whole setup:** the spending is front-loaded and contractually committed; the ROI is back-loaded and faith-based. That's exactly the configuration where a narrative can turn fast — not because AI stops working, but because the market stops accepting "trajectory" as an answer and starts demanding the revenue line. Nothing in this corpus would satisfy that demand today. The capex is a bet that cost-avoidance ROI converts into revenue ROI before investor patience runs out — and right now that conversion is asserted, not shown.

---

## Summary Table

| Company | Demand-side ROI signal | Quality of evidence | Key bear tell |
|---------|----------------------|-------------------|---------------|
| META | Advertiser ROI (impression/price growth) | High — flows through P&L | Everything beyond ads: no plan, just "trajectory" |
| MSFT | Copilot daily usage = Outlook | Medium — usage, not outcome | Seat growth +6%; customer ROI deferred to IT budget reshaping |
| AMZN | Internal: 5 people / 65 days; Enterprise: cost avoidance | Low-medium — anecdotal | Circular demand; enterprise revenue-gen AI still "starting to come to production" |
| CRM | Agentforce expansion spend (top 10 spend 1.5x) | Medium — expansion data, no NRR | 2.6% of revenue; margin-neutral on token absorption; CRPO +9% |
| SAP | AI attach 66%+ in order entry; migration cost reduction | Medium — attach is funnel entry, not outcome | Consumption pricing compresses revenue per customer; services revenue declining |

**The pattern:** Every company has strong sell-side AI metrics (ARR, attach, seats). None has clean customer-outcome ROI data — it's either absent, anecdotal, or one step removed. The honest moment is Jassy saying enterprise AI success is concentrated in *cost avoidance*, not revenue generation. That's the demand-side tell — and it's consistent across the corpus.

---

## From the Theses and Earnings Calls — Full Bull/Bear by Company

### META

**What their AI actually does:** Improves the ad targeting algorithm. That's it for the monetized part. Everything else (Muse AI assistant, Llama, superintelligence lab) is pre-revenue.

**Bull:** The targeting improvement is genuinely flowing through the P&L — impression volume +19% YoY, price per ad +12% YoY. This is real, measurable, customer-facing ROI for advertisers. Zuckerberg on Q1'26 analyst call: *"there is still a lot of room to continue improving recommendations over the rest of the year."*

**Bear:** When asked directly what ROI signposts he watches on the massive capex, Zuckerberg said: *"the things that we are watching are to make sure that we are on track building leading models and leading product... I do not think we have a very precise plan for exactly how each product is going to scale month over month."* That is the CEO of a company spending $125–145B in 2026 telling you his ROI framework is vibes and trajectory. Management also declined to guide 2027 capex, saying they *"continue to underestimate"* compute needs. The monetization path for everything beyond ad targeting is described qualitatively — "superintelligence," "agentic experiences." No named customers, no contracts, no revenue attached. ROIC declining: 32.2% (2021) → 23.4% (TTM), with invested capital growing rapidly.

---

### MSFT

**What their AI actually does:** Azure cloud (inference/training), Copilot (M365 + GitHub), security AI. $37B AI ARR, +123% YoY.

**Bull:** The numbers are real. Azure +40% YoY. GitHub Copilot has measurable productivity signal (they reference coding speed improvements across call). Satya on Q3'26 call: *"It is at the same level as Outlook — this is a daily habit of intense usage."* On customer ROI: *"customers are going to evaluate it by eval — where they are seeing the value of tokens... Where they see the outcome — the eval on the token — whether it is improving revenue or efficiency."* At least they have a framework.

**Bear:** M365 Copilot seats only +6%. That's the demand-side tell — 20M seats sounds big but seat growth is decelerating. When the analyst asked directly how to think about ROI on CapEx, Amy Hood's answer: *"many investors are trying to draw a direct line"* — then deflected to gross margin percentages rather than customer ROI data. Cloud gross margins are being compressed: cost of Intelligent Cloud revenue up 47% on +30% revenue growth. Satya's own framing on seat-vs-consumption transition is the most honest signal in the repo: *"IT budgets will be reshaped by a combination of business outcomes making their way into IT budgets and reallocation from other line items."* Translation: customers haven't yet proven this out on their own P&Ls, and MSFT is waiting for them to do so before IT budgets reallocate. CapEx $190B +61%, no ROI timeline disclosed.

---

### AMZN

**What their AI actually does:** AWS sells inference/training to AI labs (Anthropic, OpenAI) and enterprises. Internally, AI is changing how Amazon builds software.

**Bull:** Jassy gave the best unscripted customer ROI anecdote in the corpus: *"Normally, that would have taken 40 or 50 people about a year to do. We took five really smart, AI-forward-thinking people building on agentic coding tools, and those five people rebuilt it in 65 days."* That's a real internal productivity signal. On enterprise adoption: *"The largest absolute place that we see enterprises having success is in projects that are around cost avoidance and productivity — things like business process automation or fraud."* That's an honest characterization of where ROI is actually showing up — cost avoidance, not revenue generation. AWS +28% YoY, $364B backlog.

**Bear:** The $364B backlog includes a >$100B Anthropic commitment — *"That does not include the recent deal that we announced with Anthropic for over $100 billion."* Amazon invested in Anthropic, Anthropic buys AWS with that capital. This is circular demand, not organic enterprise ROI. FCF near zero. Jassy's own Q4 Q&A when pushed on ROIC proof: *"We have deep experience understanding demand signals... we are confident this will be the case here"* — conviction claim, no evidence. Revenue-generating AI applications are described as still arriving: *"the number of projects... that we are now starting to see come to production around brand-new experiences... is also very significant."* Starting to. Come to production.

---

### CRM

**What their AI actually does:** Agentforce — autonomous agents that handle service requests, qualify leads, answer questions. This is the closest thing to a direct enterprise AI ROI test in this corpus.

**Bull:** This is the cleanest demand-side data point in the repo. Agentforce ARR $1.2B, +205% YoY. Internal proof: *"four million autonomous service transactions on help.salesforce.com."* Top 10 AWU customers *"have spent more than 1.5x over the past year"* — that's expansion revenue from AI users, meaning customers found enough value to spend more. Engineering headcount flat for 2 years while output grows = internal productivity proof. Salesforce/Anthropic Slackbot driving *"~3% company productivity improvement."* At least they measured it.

**Bear:** Agentforce is $1.2B ARR on $42B TTM revenue — 2.6% of revenue. Spectacular growth rate on an immaterial base. The critical data point that management won't disclose: NRR (net revenue retention). When an analyst pushed on translating AWU (Agentic Work Units) to revenue, Marc Benioff answered by talking about headcount efficiency, not customer ROI. On gross margin impact of absorbing token costs (paying OpenAI/Anthropic): *"we anticipate being neutral on gross margins... we're building efficiencies into our product development to control costs."* Neutral. They are absorbing AI model costs into their margin structure with no margin expansion from AI yet. CRPO growth only 9% — the leading revenue indicator. The consumption-pricing transition (Flex Credits) creates a specific risk: if customers buy credits and don't use them because ROI is unclear, renewal compression follows. Q2 guide already described as *"narrowly missing analyst expectations."*

---

### SAP

**What their AI actually does:** Joule AI assistant embedded in S/4HANA (ERP), AI migration tools that reduce ERP implementation cost/time. The most interesting ROI story because SAP sits on top of enterprise data that AI needs.

**Bull:** The most concrete AI attach metric in the corpus. *">2/3 of cloud order entry contained SAP Business AI — a >20pp jump from Q3 2025"* (Q4'25). *"90% of top 50 deals contained AI"* (Q1'26). AI migration tools are measurably compressing ERP implementation costs — Christian Klein: *"customers want to see the cost come down for ERP migrations... AI tooling for ERP migration sold very well."* This is genuine customer ROI: lower implementation cost = faster time-to-value. CFO Dominik Asam on the data moat: *"much of what we do is around hard monetary transactions in complex end-to-end processes... assurance that numbers are precise is ultrahigh."* SAP's AI has an audit/compliance angle that pure LLM outputs can't match.

**Bear:** The attach rate is at the top of the funnel (order entry), not at production deployment. Klein's Q1'26 admission: *"the focus was on making this AI productive, putting those agents into production with our customers. That progressed really well"* — the word "progressed" means it's not done. The consumption-pricing transition risk is explicit from management: Klein said the shift *"could temporarily compress revenue per customer."* The services revenue line is already declining because AI migration tools are reducing what system integrators (SAP's implementation partners) charge — *"the increase in adoption of these AI migration tools naturally reduces the budgets billed to system integrators."* That's deflationary for the broader SAP ecosystem. Cloud backlog decelerated 29% → 25% CC, and management itself flagged it as *"more pronounced than anticipated."* Klein's response when asked if customers are building agents outside the SAP ecosystem: *"We see examples... but nothing that keeps me up at night."* That phrasing is exactly what keeps investors up at night.

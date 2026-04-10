# Context — Sectors

*Last updated: [DATE]*

---

## AI

### Overarching Context

**Reflexive Dynamics**
AI is exhibiting reflexive dynamics: high stock prices lower the cost of capital for Big Tech, enabling record-breaking CapEx (projecting $500B+ total in 2026). Understanding the circular revenue dynamics and where they might break is key to evaluating positions across the ecosystem.

* **The Circular Loop:** Hyperscalers fund AI Labs/Startups → Startups spend that capital on Hyperscaler cloud credits and chips → Revenues grow, justifying more CapEx.
* **The Big Tech Subsidy:** Hyperscalers are absorbing enormous demand risk across the supply chain, creating a subsidy for the entire ecosystem.
* **The Revenue Imperative:** The application layer must eventually generate ~$600B in revenue to justify the current infrastructure buildout.
* **The "Jevons' Paradox" of Efficiency:** Software compression breakthroughs that reduce AI model memory size have historically lowered the barrier to entry. Rather than acting as a headwind for hardware, this efficiency tends to accelerate mass adoption, sustaining or increasing overall hardware demand.

**Signals to Monitor**
* **CapEx Direction:** Hyperscalers cutting CapEx or shifting focus from "Execution" back to "Discovery."
* **GPU Spot Pricing:** Surges or collapses in GPU rental rates (e.g., H100 hourly rates) acting as a real-time barometer for compute constraints and demand.
* **Turning Point Signals:** Excesses concealed during the rise (e.g., unpaid cloud credits, startup failures) beginning to surface.
* **Revenue Gap Recognition:** The $600B revenue gap being acknowledged by the market as insurmountable.
* **Memory Cycle Risks:** A collapse in DRAM/NAND spot prices, which historically signals that data center inventory building has peaked.
* **Consumer Supply Chain Crowding:** Track component-driven price hikes in non-AI consumer tech (e.g., LPDDR4 RAM prices rising "seven-fold"). Signals that AI infrastructure demand is actively cannibalizing the broader semiconductor and memory supply chain.
* **Server Memory Ratios:** With NAND memory content in AI servers doubling over the last year, memory is shifting from a peripheral component to a primary cost center and bottleneck.

---

### Compute & Chips

#### Context
* **The Inference Shift:** As Agentic AI scales, hardware demand is shifting from pure training to an "inference inflection" (e.g., Vera Rubin, Groq). Watch for specialized inference chips challenging Nvidia's moat.
* **Foundry Leverage:** TSMC (TSM) is the dominant foundry with a systematic underbuilding strategy to maintain pricing power.
* **Semiconductor Moats:** NVIDIA (NVDA) dominates but faces "customer defection risk" as hyperscalers develop Custom Silicon (TPUs, Trainium, Graviton).
* **Memory Constraints:** Monitor whether HBM and DRAM remain structural bottlenecks or if capacity investments lead to cyclical gluts. Current forecasts show Q2 2026 conventional DRAM contract prices rising roughly 60% QoQ and NAND flash jumping over 70%. High component prices may also trigger pullbacks in consumer electronics volume.
* **Depreciation Risk:** New chip cycles (e.g., Blackwell B100) offer massive performance gains (2.5x), rapidly devaluing older hardware (H100).

#### Recent Signals & Developments
*No entries yet.*

#### Risks
* Customer defection as hyperscalers develop custom silicon
* Capacity overbuild leading to cyclical glut in memory
* Export controls constraining addressable market
* High component prices triggering pullbacks in consumer electronics volume

#### Companies of Interest
TSM, NVDA, AMD, AVGO, ASML, AMAT, LRCX, KLAC, MU, SSNLF, HXSCL (SK Hynix)

---

### Networking & Optical

#### Context
* **Optical Interconnects as Scaling Solution:** As AI cluster sizes grow, optical interconnects are emerging as the primary solution for data transfer latency constraints.
* **Supplier Lock-in:** Hyperscalers are signing 2–3 year guaranteed contract minimums for transceivers and optical circuit switches amid supply constraints. This transforms cyclical hardware suppliers into high-margin, mission-critical utilities.
* **The Copper Debate:** Copper interconnects remain a competing solution at shorter distances; watch for shifts in hyperscaler preference between copper and optical.

#### Recent Signals & Developments
*No entries yet.*

#### Risks
* Copper interconnect alternatives limiting optical TAM at shorter distances
* Concentration risk — a handful of hyperscaler customers hold significant leverage on contract terms
* Technology transitions (co-packaged optics) could disrupt incumbent transceiver suppliers

#### Companies of Interest
LITE, CLS, AAOI

---

### Infrastructure & Power

#### Context
* **Demand Shock:** Data center REITs are experiencing a "demand shock" with guaranteed 15–20 year leases.
* **Physical Bottlenecks & Thermal Management:** After the 2024 "land grab," 2025–2026 are Execution Years. As advanced silicon processors approach reliable operating junction temperatures of 100°C, traditional air cooling becomes unviable, forcing a structural shift to liquid cooling systems.
* **The Human Logistics Constraint:** Power and cooling aren't the only bottlenecks. The physical labor required to build 2-gigawatt campuses is tapped out, driving massive multi-million dollar contracts simply to house and support the construction armies.
* **Redesign Risk:** Chip advances (e.g., warm-water cooling requirements) can trigger mid-build data center redesigns, causing delays and cost overruns.
* **Cascading Earnings Impact:** Physical holdups don't just delay construction revenue — they delay the revenue generated by operating the completed facility, amplifying the financial impact of bottlenecks.
* **The "Neocloud" AI Factories:** A new sub-layer of dedicated AI cloud providers has emerged, securing multi-billion dollar, multi-year capacity contracts from major hyperscalers (e.g., $25B+ backlogs from Meta and Microsoft) to build dedicated, liquid-cooled GPU clusters.

#### Recent Signals & Developments
*No entries yet.*

#### Risks
* Execution risk on large-scale builds — labor, permitting, grid interconnection delays
* Grid moratoriums in key markets limiting available capacity
* Redesign risk from chip generation transitions
* Cascading delays amplifying the financial impact beyond the construction phase

#### Companies of Interest
MSFT, AMZN, GOOGL, META, DLR, EQIX, VRT, ETN, JCI, SBGSY, TH, JBL, NBIS, CRWV

---

### Nuclear & Energy

#### Context
* **AI Power Demand as Structural Driver:** The scale of AI data center buildouts is creating sustained, long-duration power demand that renewable intermittency cannot reliably serve, elevating the case for nuclear baseload.
* **The Nuclear Renaissance:** SMRs (Small Modular Reactors) are emerging as the favored solution for dedicated AI campus power, with active DoD and hyperscaler interest.
* **Government Catalysts:** OTA (Other Transaction Authority) and the Reactor Pilot Program are accelerating deployment pathways outside traditional NRC certification timelines.
* **Mine-to-Megawatt:** The supply chain extends from uranium mining through enrichment and fuel fabrication to reactor components — domestic supply chain security is a key theme alongside reactor deployment.

#### Recent Signals & Developments
*No entries yet.*

#### Risks
* NRC design certification timelines remain long even with accelerated pathways
* SMR economics unproven at scale — cost overruns are a historical pattern in nuclear
* Capacity factor and reliability risk for first-of-kind designs
* Uranium price volatility affecting project economics

#### Companies of Interest
CCJ, BWXT

---

### Software & Disruption

#### Context
* **Consolidation:** The "Big 5" Finalists (OpenAI, Anthropic, Google, Meta, xAI) are consolidating the frontier model layer.
* **Switching Costs:** Low for model providers; much higher for orchestration/agent frameworks and data services.
* **The Revenue Test:** Applications must generate revenue to support all underlying layers.
* **Software Disruption vs. Moat Durability:** AI tools (including "vibe-coding") create a narrative that existing enterprise software can be replicated or replaced. Counter-arguments center on switching costs, network effects, deep integrations, and the difficulty of replicating embedded enterprise workflows at scale. This tension extends to credit markets, where disruption concerns are affecting software companies' ability to refinance debt.
* **Edge AI & Specialized Data Moats:** AI is breaking into the physical world. Look for companies processing AI data at the edge on proprietary hardware (satellites, autonomous vehicles, diagnostic machines) or using multimodal data libraries as the operating system for specialized fields.
* **The Opportunity:** Application developers benefit most from the "Subsidy Effect" as compute prices decline.

#### Recent Signals & Developments
*No entries yet.*

#### Risks
* Low switching costs at the model layer expose incumbents to rapid displacement
* The revenue test: application layer revenue may not materialize at the scale needed to justify infrastructure buildout
* Debt refinancing risk for software companies facing AI disruption narratives
* Reflexivity reversal: if the circular loop breaks, the application layer loses the subsidy effect

#### Companies of Interest
PLTR, SNOW, MDB, DDOG, CRWD, PANW, IBM, ORCL, CRM, ADBE, NOW, WDAY, INTU, HUBS, TSLA, PL, SOUN, TEM

---

## Critical Minerals & Rare Earths

### Context
* **The Mine-to-Magnet Imperative:** Physical AI infrastructure cannot be built without secure domestic supply chains. The U.S. government and defense sector are actively subsidizing decoupling from the Chinese monopoly on heavy rare earths. Elements like Terbium and Dysprosium are currently commanding up to a 5x price premium outside of China, benefiting domestic processors.
* **The Copper Constraint:** Global copper demand is forecasted to reach over 40 million tons by 2040, driven by electrification and data center buildouts. This supply-demand gap elevates the strategic value of advanced explorers situated near existing mining infrastructure.
* **Vertical Integration:** Mine-to-magnet vertical integration is a key differentiator — companies controlling the full supply chain from mining through separation and magnet production carry strategic premium.

### Recent Signals & Developments
*No entries yet.*

### Risks
* Chinese rare earth processing dominance is deeply entrenched — domestic alternatives face cost and scale disadvantages
* Permitting and environmental timelines for new mines remain long
* Rare earth price volatility driven by Chinese export policy

### Companies of Interest
MP, UURAF, UUUU, USAR, NB, CCJ, BWXT, NVRED

---

## Defense & Aerospace

### Context
* **Dual-Use Technology:** Defense spending increasingly overlaps with AI and space infrastructure themes — autonomous systems, edge AI, geospatial intelligence, and satellite-to-cellular are all dual-use.
* **Autonomous Warfare:** Drone autonomy and hypersonic development are active procurement priorities.
* **Space Infrastructure:** The Space Development Agency and commercial space are building persistent low-earth orbit constellations for communications and intelligence.

### Recent Signals & Developments
*No entries yet.*

### Risks
* Budget and continuing resolution uncertainty affecting multi-year contract visibility
* Program cancellation or restructuring risk on large defense programs
* Geopolitical de-escalation reducing near-term procurement urgency

### Companies of Interest
*No entries yet.*

# Context — Sectors

*Last updated: 2026-04-15*

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
* **CapEx Direction:** Hyperscalers cutting CapEx or shifting focus from "Execution" back to "Discovery." Note: 2026 hyperscaler CapEx expectations have roughly doubled from prior forecasts (Google the most extreme example). The binding constraint has shifted — hyperscalers are no longer capital-constrained but strictly silicon-constrained (advanced logic and memory fabrication capacity).
* **GPU Spot Pricing:** Surges or collapses in GPU rental rates (e.g., H100 hourly rates) acting as a real-time barometer for compute constraints and demand.
* **Turning Point Signals:** Excesses concealed during the rise (e.g., unpaid cloud credits, startup failures) beginning to surface.
* **Revenue Gap Recognition:** The $600B revenue gap being acknowledged by the market as insurmountable.
* **Memory Cycle Risks:** A collapse in DRAM/NAND spot prices, which historically signals that data center inventory building has peaked.
* **Consumer Supply Chain Crowding:** Track component-driven price hikes in non-AI consumer tech (e.g., LPDDR4 RAM prices rising "seven-fold"). Signals that AI infrastructure demand is actively cannibalizing the broader semiconductor and memory supply chain.
* **Server Memory Ratios:** With NAND memory content in AI servers doubling over the last year, memory is shifting from a peripheral component to a primary cost center and bottleneck.
* **AI Lab ARR Scaling:** Sustained growth rate of token consumption as a demand health check. With AI tool ROI currently estimated at 5–10x, demand remains highly inelastic to current price increases — the break would come from ROI compression, not price sensitivity.

---

### Compute & Chips

#### Context
* **The Inference Shift:** As Agentic AI scales, hardware demand is shifting from pure training to an "inference inflection" (e.g., Vera Rubin, Groq). Watch for specialized inference chips challenging Nvidia's moat. Importantly, the hardware market is bifurcated by workload type: training workloads retain best price-performance on H100s (a structural reason older Hopper demand stays sticky), while large mixture-of-experts (MoE) inference workloads run best on the latest large world-size systems (e.g., GB300 NVL72). Agentic AI is also driving a 4x spike in CPU demand — from 30M cores/GW to 120M cores/GW — as CPUs handle the orchestration overhead of multi-agent workflows alongside GPU token generation.
* **Heterogeneous Memory Architecture:** The "one-size-fits-all" server memory model (DDR5) is giving way to a heterogeneous stack tuned for specific AI workload phases. Analysts identify a structural efficiency hierarchy: **SRAM** (ultra-fast, low-capacity, for caches and token-serialized "decode" functions) > **HBM** (stacked, massive bandwidth for parallel "prefill" functions) > **LPDDR5X** (low-power, moving from mobile to servers for efficiency-at-scale) > **DDR5** (general-purpose, high-capacity, but least efficient). In environments where power and cooling are fixed constraints, memory is becoming an active design variable rather than a fixed component.
* **N3 Wafer Scarcity:** TSMC's N3 node is the single biggest constraint in the AI supply chain. AI-related silicon (accelerators, host CPUs, networking) is consuming ~60% of N3 wafer output in 2026, modeled to reach 86% by 2027 — nearly entirely squeezing out smartphone and CPU wafers. Effective N3 utilization is on track to exceed 100% in H2 2026; TSMC cannot expand cleanroom space quickly enough. Their CapEx only exceeded its prior peak in 2025, and they were caught flat-footed by the pace of AI demand.
* **Arm's Market Position:** Arm CPUs already account for ~40% of the cloud data center market (Futurum Group), with over 1 billion deployed Neoverse cores — driven by hyperscaler custom Arm chips (AWS Graviton, Azure Cobalt, Google Axion). Arm is now transitioning from pure IP licensing to direct silicon production with its AGI CPU, making it a new competitive force in the data center CPU market while simultaneously supplying the architecture underlying its licensees' custom chips.
* **Semiconductor Moats:** NVIDIA (NVDA) dominates but faces "customer defection risk" as hyperscalers develop Custom Silicon (TPUs, Trainium, Graviton). This risk is now quantified: ASIC-based AI servers are forecast to account for 27.8% of total AI server shipments in 2026, rising to ~40% by 2030 (TrendForce). The economic logic is also quantified: AWS expects Trainium to save "tens of billions of capex dollars per year" and deliver several hundred basis points of operating margin advantage for inference workloads vs. third-party chips — making custom silicon a margin imperative, not just a supply hedge.
* **Memory Constraints:** HBM is absorbing incremental DRAM wafer capacity, structurally crowding out commodity DRAM. On a wafer-per-bit basis, HBM consumes ~3× more capacity than commodity DRAM — a gap widening to ~4× with HBM4 and further with HBM4E. HBM content per accelerator is growing rapidly: Rubin Ultra carries ~4× more HBM than Blackwell; TPU v8AX and Trainium3 are migrating from 8-Hi to 12-Hi stacks. Importantly, reallocating capacity from weakening consumer markets (e.g., a 10% smartphone shipment decline) would release only ~3% of total DRAM demand — insufficient to move the needle. LPDDR5 and DDR5 contract prices tracked toward ~4x and ~5x year-on-year increases respectively in Q1 2026 — parabolic moves consistent with the structural shortage thesis. Also monitor conventional DRAM and NAND flash contract pricing as leading indicators (Q2 2026 forecasts: DRAM +60% QoQ, NAND +70%). As major suppliers accelerate toward HBM and DDR5, they are exiting niche markets (2D NAND, SLC NAND, niche DRAM), creating second-order supply gaps being filled by smaller, lower-tier players.
* **Memory Market: LTA Structuralization:** The memory market is shifting from short-term/quarterly contracts to a Long-Term Agreement (LTA)-only model spanning 3–5 years. The catalyst is custom AI silicon: memory specs and volumes are locked in at the design stage, making early multi-year procurement commitments a structural necessity. LTAs are reserved for major CSPs (Microsoft, Google, Amazon, Meta, Alibaba, ByteDance) — not offered broadly. This reduces memory supplier cyclicality, improves capex planning visibility, and keeps long-term capacity committed to Big Tech, reinforcing the structural bottleneck thesis.
* **Foundry Diversification:** The TSMC supply shock — compounded by the geographic concentration of TSMC's advanced packaging capacity in Taiwan — is pushing customers toward alternatives on both supply and geopolitical risk grounds. Intel Foundry is gaining favor backed by US government support, with its EMIB advanced packaging technology attracting serious interest from hyperscalers seeking a geographically diversified alternative. Samsung Foundry has secured Tesla's AI5/AI6 programs and entered NVIDIA's datacenter supply chain. CoWoS packaging constraints are simultaneously easing as front-end N3 wafer availability becomes the dominant bottleneck; CoWoS packaging is being outsourced to OSATs (ASE/SPIL, Amkor).
* **Depreciation Risk:** New chip cycles (e.g., Blackwell B100) offer massive performance gains (2.5x), rapidly devaluing older hardware (H100).

#### Recent Signals & Developments
* **AMD-Meta Structural Partnership (2026):** AMD and Meta have struck a landmark **$100B, 6 GW chip deal** as the AI infrastructure race intensifies. This represents a massive quantitative anchor for the "Big Tech Subsidy" and validates AMD as a primary beneficiary of the multi-year hyperscaler CapEx cycle.
* **SOCAMM Adoption (2026):** The emergence of **SOCAMM** (Small Outline Compression Attached Memory Module) as a form factor for LPDDR5X in servers addresses a primary operational risk. By bridging high efficiency with serviceability (replaceability), SOCAMM enables LPDDR5X to transition from mobile to production server environments without the "soldered" maintenance penalty.
* **GPU Spot Pricing: Supply Exhaustion (Q1–Q2 2026):** H100 1-year rental contracts rose ~40% from $1.70/hr (October 2025 trough) to $2.35/hr (March 2026), defying prior expectations that Hopper pricing would decline with Blackwell's ramp. On-demand capacity is effectively sold out across all GPU types; p6-b200 spot instances on AWS are trading at $14/hr. Blackwell lead times extend to June–July 2026; all capacity through August–September 2026 is already committed. Existing H100 contracts are being renewed at original rates for 4-year extensions through 2028. Illustrating the severity: two large AWS customers independently asked to purchase every single Graviton instance available in 2026 — AWS declined to preserve availability for other customers.
* **Intel EMIB-T & TSMC US Packaging Acceleration (2026–2028):** Intel is in active discussions with Google and Amazon to provide EMIB-T advanced packaging for their ASIC programs (TPUs and Trainium); commitments are targeted for H2 2026, with customers reportedly willing to prepay in the billions. Intel CFO highlighted advanced packaging as the "more interesting part" of the Foundry business with ~40% gross margin potential. Intel's Malaysia assembly operations come online in 2026; New Mexico (Fab 9, Fab 11X) is already in mass production for 3D packaging. In parallel, TSMC is accelerating its US advanced packaging facility — construction beginning Q2 2026 (one quarter ahead of prior expectations), targeting operations late 2027–2028, deploying SoIC, CoW, and CoPoS technologies. Both moves are partly driven by customer demand for geographic diversification away from Taiwan-concentrated packaging capacity.
* **Arm AGI CPU Launch (2026):** Arm launched its first directly supplied data center CPU (AGI CPU), with Meta as co-developer and inaugural customer; OpenAI, Cerebras, Cloudflare, and others also adopting. Built on TSMC 3nm (adding further N3 demand), with a striking liquid-cooled vs. air-cooled performance differential: 45,000+ cores/rack liquid-cooled vs. 8,000+ air-cooled — a 5x gap that vividly illustrates the liquid cooling performance premium. The AGI CPU is explicitly targeting neoclouds that cannot justify the overhead of custom silicon design, positioning it as an off-the-shelf alternative to bespoke Broadcom/Marvell solutions.
* **Custom Silicon Scaling: Amazon & Broadcom-Google (2026–2031):** Amazon's in-house silicon business is already on track for $20B+ in annual revenue; CEO Andy Jassy confirmed exploring external rack sales to third parties, citing a potential $50B run rate if the unit operated as a standalone business (exploratory at this stage). Separately, Broadcom has entered a long-term agreement with Google to develop and supply future generations of custom AI chips and related rack components through 2031 — a multi-year structural commitment that further entrenches the AVGO-GOOGL custom silicon relationship and reduces Google's NVDA dependency.
* **Memory LTA Deals Accelerating (H1 2026):** All three major memory suppliers are moving to multi-year agreements simultaneously. Micron secured its first 5-year strategic customer agreement (disclosed at March 2026 earnings) and is in active discussions with multiple clients. Samsung adopted a strict 3-year minimum LTA policy for all new contracts starting 2026, with late-stage negotiations underway with AMD, Microsoft, and Google. SK Hynix is pursuing a 5–7 year LTA with Google for commodity DRAM (with an option to extend a further 2 years tied to next-gen HBM supply, given SK Hynix is Google's primary HBM3E supplier), expected to finalize H1 2026; separately in final coordination with Microsoft on a 3-year DDR5 LTA valued at "tens of trillions of won." Deals include downside price floors and upfront prepays of 10–30% of total contract value.
* **OEM Repricing Loop (2026):** OEMs repriced AI servers well beyond underlying component cost increases to manage margin risk → compressed project returns for operators → slow-rolled or abandoned deployments → supply withheld from the rental market → rental market tightened further. A self-reinforcing dynamic worth monitoring as a leading indicator of supply withholding.
* **Industry N3 Convergence (2026):** Every major AI accelerator platform has converged on TSMC N3 simultaneously: NVIDIA (Rubin on 3NP), AMD (MI350X and MI400 tiles on N3), Google (TPU v7 fully on N3E, TPU v8 remaining on N3), AWS (Trainium3 on N3P, large H2 ramp), and Meta (MTIA on N3). This synchronized convergence is the structural driver of the N3 capacity squeeze.
* **Samsung 2nm Yield Struggles & TSMC Moat Reinforcement (April 2026):** Samsung Foundry's 2nm yields are reportedly stalled at ~55%, below the ~60% threshold required for mass production, prompting Qualcomm to select TSMC's N2P for its next-generation flagship Snapdragon. Samsung retains Tesla's AI5/AI6 autonomous driving chip programs and domestic AI startup DeepX, but the yield gap concretely anchors the competitive moat TSMC holds at advanced nodes. (Source: TrendForce/Semiconductors, April 2026)

#### Risks
* Customer defection as hyperscalers develop custom silicon
* Capacity overbuild leading to cyclical glut in memory — *partially mitigated by the accelerating shift to 3–5 year LTAs locking in Big Tech demand, but risk remains for commodity tiers not covered by LTAs*
* Export controls constraining addressable market
* High component prices triggering pullbacks in consumer electronics volume
* China's domestic memory industry is rapidly scaling — driven by aggressive capital formation (HK listings, multi-billion dollar procurement LTAs) and deliberate domestic buildout. Over time this could: compete with incumbents in commodity/niche tiers; erode the efficacy of US export controls as a geopolitical lever; and bifurcate the global memory market into separate Western and Chinese supply chains.

#### Companies of Interest
TSM, NVDA, AMD, AVGO, ASML, AMAT, LRCX, KLAC, MU, SSNLF, HXSCL (SK Hynix), AMKR, ASX, ARM, META

---

### Networking & Optical

#### Context
* **Optical Interconnects as Scaling Solution:** As AI cluster sizes grow, optical interconnects are emerging as the primary solution for data transfer latency constraints.
* **Supplier Lock-in:** Hyperscalers are signing 2–3 year guaranteed contract minimums for transceivers and optical circuit switches amid supply constraints. This transforms cyclical hardware suppliers into high-margin, mission-critical utilities.
* **The Copper Debate:** Copper interconnects remain a competing solution at shorter distances; watch for shifts in hyperscaler preference between copper and optical.
* **Dark Fiber as AI Training Substrate:** Turning multiple disparate data centers into unified AI training factories (e.g., Nvidia Spectrum-XGS) requires purpose-built dark fiber connectivity. This is a structural new demand vector for dark fiber distinct from general data center networking — it requires dedicated, high-capacity point-to-point links between facilities.
* **Rural Data Center Fiber Demand:** New AI data centers are increasingly being built in tier-two markets where power is available rather than in major metros. Backhauling this traffic to carrier-neutral interconnection facilities is highly inefficient, driving dedicated fiber and wave buildouts along routes that didn't previously require this infrastructure. Lumen has identified "dozens of new data center clusters across the US" requiring fiber, wave, and IP services and is actively building a specialized AI fabric to serve them.

#### Recent Signals & Developments
* **Fiber Optic Demand Surge (Q1 2026):** Fiber optic cables are explicitly cited alongside GPUs, DRAM, and NAND as components experiencing price spikes from the AI demand inflection. Confirms that the infrastructure buildout is pressuring the full networking supply chain, not just compute and memory.
* **Optical Transceiver Sales Doubling (2026):** LightCounting forecasts Ethernet optical transceiver sales for AI clusters to double in 2026 — a concrete demand signal for transceiver suppliers tied directly to AI cluster buildout pace.

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
* **Physical Bottlenecks & Thermal Management:** After the 2024 "land grab," 2025–2026 are Execution Years. As advanced silicon processors approach reliable operating junction temperatures of 100°C, traditional air cooling becomes unviable, forcing a structural shift to liquid cooling systems. Cooling accounts for up to 60% of a facility's total energy costs — making liquid cooling (which materially reduces energy consumption vs. air) a margin driver, not just a thermal necessity. AI data center reference designs now standardly assume liquid interfaces; this has crossed from an emerging option to a baseline architectural assumption.
* **The Human Logistics Constraint:** Power and cooling aren't the only bottlenecks. The physical labor required to build 2-gigawatt campuses is tapped out, driving massive multi-million dollar contracts simply to house and support the construction armies.
* **Redesign Risk:** Chip advances (e.g., warm-water cooling requirements) can trigger mid-build data center redesigns, causing delays and cost overruns.
* **Cascading Earnings Impact:** Physical holdups don't just delay construction revenue — they delay the revenue generated by operating the completed facility, amplifying the financial impact of bottlenecks.
* **The "Neocloud" AI Factories:** A new sub-layer of dedicated AI cloud providers has emerged, securing multi-billion dollar, multi-year capacity contracts from major hyperscalers (e.g., $25B+ backlogs from Meta and Microsoft) to build dedicated, liquid-cooled GPU clusters.
* **The Infrastructure Readiness Gap:** Less than 10% of existing US data center inventory is currently capable of supporting "true AI-dense critical load" (JLL). The vast majority of traditional enterprise facilities operate at lower power densities with inadequate air cooling — underscoring the scale of the buildout still required and the structural advantage of purpose-built neocloud facilities.
* **Enterprise Evaluation Shift:** Only 22.8% of AI initiatives successfully meet their original ROI objectives once in production (HyperFrame Research), reflecting a wide gap between AI experimentation and production-scale deployment. As a result, enterprise evaluation criteria have shifted: a year ago, conversations focused solely on capacity and price; today enterprises are evaluating infrastructure providers on production reliability, lifecycle controls, automated health checks, and stable performance under sustained demand — a shift that favors mature, purpose-built neocloud platforms over capacity-only providers.

#### Recent Signals & Developments
* **Neocloud Market Power Shift (late 2025–2026):** Before late 2025, GPU rental pricing was competitive. By early 2026, Neoclouds and Hyperscalers are firmly in control — demanding higher prepays (20%+), longer contract terms, and setting deployment timelines on their own schedule. Mid-term contracts (3 months to 3+ years) are the most economically relevant segment and the best real-time indicator of marginal demand tightening.
* **Long-Term Offtakes (2026):** Major AI labs are locking in 50MW–100MW clusters (equivalent to ~24,000–48,000 GB300 NVL72 GPUs) on 4–5 year terms. Hyperscalers are backstopping these deals in exchange for a share of project revenue — reinforcing the circular loop dynamic. CoreWeave's $21B AI compute contract with Meta (announced April 2026) provides a concrete anchor for the scale of individual neocloud deals.
* **Gas Turbine Demand Spike (Q1 2026):** Gas turbines are explicitly cited alongside GPUs and memory as components experiencing price spikes from the AI demand inflection, confirming that power generation equipment is becoming a binding constraint in the infrastructure buildout.
* **Midwest Data Center Geography Shift (2026):** Midwestern data centers already constitute a third of all U.S. capacity and will account for more than half of new capacity coming online, driven by power scarcity in traditional markets like Northern Virginia. Synergy Research Group is tracking a pipeline of 803 data center projects (just over half in the U.S.), with secondary markets — New Albany (Ohio), Atlanta, and others — absorbing demand that legacy Tier-1 markets can no longer accommodate. (Source: Fierce Network / Synergy Research Group, April 2026)
* **Behind-the-Meter Alternative Power at Scale (April 2026):** Oracle committed to up to 2.8GW of Bloom Energy fuel cell power to support U.S. cloud infrastructure projects — the largest known behind-the-meter alternative power commitment to date. Signals that grid constraints are severe enough to drive hyperscalers toward multi-gigawatt on-site generation rather than grid interconnection. (Source: Fierce Network, April 2026)

#### Risks
* Execution risk on large-scale builds — labor, permitting, grid interconnection delays
* Grid moratoriums in key markets limiting available capacity
* Redesign risk from chip generation transitions
* Cascading delays amplifying the financial impact beyond the construction phase
* Neocloud financial/credit risk: operators frequently deploy GPUs before facilities are fully operational, relying on short-term bridge financing that assumes rapid time-to-revenue. If supply chains, construction, or power procurement slip, GPU assets sit idle, revenue assumptions break, and refinancing becomes extremely difficult. Lenders are already highly cautious on neocloud deals, scrutinizing utilization assumptions and long-term demand visibility.
* Water scarcity and quality as an emerging operational constraint — as liquid cooling becomes the baseline architecture, water availability and treatment become critical dependencies. Facilities in water-constrained regions are already resorting to recycled water with on-site storage and treatment; water quality failures (biological growth, corrosion, scaling) represent a direct operational risk to liquid-cooled infrastructure

#### Companies of Interest
MSFT, AMZN, GOOGL, META, DLR, EQIX, VRT, ETN, JCI, SBGSY, TH, JBL, NBIS, CRWV, IREN

---

### Nuclear & Energy

#### Context
* **AI Power Demand as Structural Driver:** The scale of AI data center buildouts is creating sustained, long-duration power demand that renewable intermittency cannot reliably serve, elevating the case for nuclear baseload.
* **The Nuclear Renaissance:** SMRs (Small Modular Reactors) are emerging as the favored solution for dedicated AI campus power, with active DoD and hyperscaler interest.
* **Government Catalysts:** OTA (Other Transaction Authority) and the Reactor Pilot Program are accelerating deployment pathways outside traditional NRC certification timelines.
* **Mine-to-Megawatt:** The supply chain extends from uranium mining through enrichment and fuel fabrication to reactor components — domestic supply chain security is a key theme alongside reactor deployment.

#### Recent Signals & Developments
* **Gas Turbine Demand Spike (Q1 2026):** Gas turbines are spiking in price alongside GPUs, memory, and fiber — a direct signal that AI data center power demand is now pressuring conventional power generation equipment supply chains. Relevant as a leading indicator of which power infrastructure companies may see accelerating order books.
* **AWS Power & CapEx Scale (2025–2027):** AWS stood up 3.9GW of new power capacity in 2025 and expects to double its total power footprint by end of 2027. AWS committed ~$200B in capex in 2026, driven by concrete customer commitments rather than demand forecasts — with monetization expected primarily in 2027–2028.
* **White House Space Nuclear Policy (April 2026):** The White House released a policy directing NASA, the Pentagon, and the Department of Energy to develop space nuclear power systems with a launch target as soon as 2028. Adds a third government accelerant alongside OTA and the Reactor Pilot Program, specifically extending the nuclear mandate into space infrastructure. (Source: SpaceNews, April 2026)

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
* **Edge AI & Specialized Data Moats:** AI is breaking into the physical world. Look for companies processing AI data at the edge on proprietary hardware (satellites, autonomous vehicles, diagnostic machines) or using multimodal data libraries as the operating system for specialized fields. The physical forcing function: fiber latency physics constrain round-trip processing to ~1ms per 125 miles; AR/VR applications require <3ms latency while typical carrier targets are ~10ms — a gap that can only be closed by processing data locally at the edge rather than sending it back to central data centers.
* **The Opportunity:** Application developers benefit most from the "Subsidy Effect" as compute prices decline.

#### Recent Signals & Developments
* **Anthropic Exploring Custom Silicon (2026):** Anthropic is in early-stage exploration of in-house chip design in response to the compute shortage constraining Claude's growth — no committed design or dedicated team yet, and may ultimately continue relying on external hardware. Current training mix spans AWS Trainium, Google TPUs, and NVIDIA GPUs. Broadcom has separately signed a deal to provide Anthropic with ~3.5 GW of AI compute capacity using Google's AI processors starting 2027. Anthropic's multi-cloud strategy spans CoreWeave, Google/Broadcom, Microsoft Azure, and AWS — with projected total cloud spend of ~$80B through 2029. Signals that even the application layer is being pushed toward vertical integration by supply scarcity, and that a single AI lab can represent an enormous, multi-year demand pipeline for infrastructure providers.
* **Agentic Token Demand Inflection (Q1 2026):** Anthropic ARR surged from ~$9B (end of 2025) to over $30B (April 2026) — more than tripling in a single quarter — driven by Claude 4.6 Opus and Claude Code. Growth was compute-constrained; actual demand exceeded available supply. Critically, this demand surge is not concentrated in one player: open models (GLM, Kimi K2.5) and native media generation platforms (Seedance) are also contributing, confirming demand is broad-based and global. Multi-agent workloads executing multi-step tasks with high concurrency and continuous iteration are the primary driver of the token demand inflection. A direct and major data point for the "Revenue Imperative" thesis — the application layer is generating real revenue at scale, with the binding constraint now supply, not demand.

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
* **Orbital Data Centers:** A structural subset of the "Edge AI" theme. As terrestrial data centers face land and power constraints, the orbital data center market is emerging as an edge compute frontier. This requires vertically integrated satellite-compute-rocket platforms and specialized thermal management systems to handle AI-dense critical loads in orbit.

### Recent Signals & Developments
* **US Space Investment Policy Anchor (2026):** The US government has set a structural goal to attract at least **$50 billion of new investment** in American space markets by 2028. This serves as a multi-year policy tailwind for the sector, similar to the CHIPS Act.
* **Structural Bottlenecks Acknowledged (2026):** Industry leaders and policymakers have cautioned that capital alone cannot solve the sector's structural bottlenecks, emphasizing that speed and near-perfect execution are the primary gating factors for the industry's resurgence.
* **Amazon Acquires Globalstar ($11.57B, April 2026):** Amazon is acquiring Globalstar for $11.57 billion, consolidating a major LEO satellite-to-cellular constellation under a hyperscaler umbrella. Confirms the strategic value of LEO communications infrastructure and marks Amazon as a direct structural player in the space theme alongside its AWS data center buildout. (Source: Fierce Network, April 2026)
* **Space Command Maneuverable Satellite Doctrine (April 2026):** Space Command is pushing a new warfighting model shifting from fixed spacecraft to maneuverable, refuelable assets for orbital warfare. BAE Systems and Lockheed Martin have unveiled new maneuvering satellite designs in direct response. Represents a structural procurement shift — not an incremental upgrade — with wargames planned to test the concept. (Source: SpaceNews, April 2026)

### Risks
* Budget and continuing resolution uncertainty affecting multi-year contract visibility
* Program cancellation or restructuring risk on large defense programs
* Geopolitical de-escalation reducing near-term procurement urgency

### Companies of Interest
Phantom Space (Public status unconfirmed)
*

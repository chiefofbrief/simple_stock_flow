# Context — Sectors

*Last updated: 2026-04-20*

---

## AI

### Structural Themes

**Reflexive Dynamics**
AI is exhibiting reflexive dynamics: high stock prices lower the cost of capital for Big Tech, enabling record-breaking CapEx (projecting $500B+ total in 2026). Understanding the circular revenue dynamics and where they might break is key to evaluating positions across the ecosystem.

* **The Circular Loop:** Hyperscalers fund AI Labs/Startups → Startups spend that capital on Hyperscaler cloud credits and chips → Revenues grow, justifying more CapEx.
* **The Big Tech Subsidy:** Hyperscalers are absorbing enormous demand risk across the supply chain, creating a subsidy for the entire ecosystem.
* **The Revenue Imperative:** The application layer must eventually generate ~$600B in revenue to justify the current infrastructure buildout.
* **The "Jevons' Paradox" of Efficiency:** Software compression breakthroughs that reduce AI model memory size have historically lowered the barrier to entry. Rather than acting as a headwind for hardware, this efficiency tends to accelerate mass adoption, sustaining or increasing overall hardware demand.

#### Watch
* **CapEx Direction:** Hyperscalers cutting CapEx or shifting focus from "Execution" back to "Discovery." Note: 2026 hyperscaler CapEx expectations have roughly doubled from prior forecasts (Google the most extreme example). The binding constraint has shifted — hyperscalers are no longer capital-constrained but strictly silicon-constrained (advanced logic and memory fabrication capacity).
* **GPU Spot Pricing:** Surges or collapses in GPU rental rates (e.g., H100 hourly rates) acting as a real-time barometer for compute constraints and demand.
* **Turning Point Signals:** Excesses concealed during the rise (e.g., unpaid cloud credits, startup failures) beginning to surface.
* **Revenue Gap Recognition:** The $600B revenue gap being acknowledged by the market as insurmountable.
* **Memory Cycle Risks:** A collapse in DRAM/NAND spot prices, which historically signals that data center inventory building has peaked.
* **Consumer Supply Chain Crowding:** Track component-driven price hikes in non-AI consumer tech (e.g., LPDDR4 RAM prices rising "seven-fold"). Signals that AI infrastructure demand is actively cannibalizing the broader semiconductor and memory supply chain.
* **Server Memory Ratios:** With NAND memory content in AI servers doubling over the last year, memory is shifting from a peripheral component to a primary cost center and bottleneck.
* **AI Lab ARR Scaling:** Sustained growth rate of token consumption as a demand health check. With AI tool ROI currently estimated at 5–10x, demand remains highly inelastic to current price increases — the break would come from ROI compression, not price sensitivity.

### Current Status
The sector is in peak infrastructure execution mode. Hyperscaler CapEx commitments for 2026 have roughly doubled from prior forecasts, driven by concrete customer demand rather than speculation. The binding constraint is no longer capital but silicon — TSMC N3 wafer capacity is effectively spoken for through 2026 and into 2027. The application layer is beginning to validate the Revenue Imperative: Anthropic ARR more than tripled in a single quarter (Q1 2026), with growth compute-constrained rather than demand-constrained. The reflexive loop remains intact and accelerating.

---

### Compute & Chips

#### Structural Themes
* **The Great Rebalance:** Agentic AI is driving a structural fourfold surge in CPU core demand — from 30M cores/GW to 120M cores/GW — shifting system architectures from 1:8 CPU:GPU ratios toward 1:1 or 1:2 as "Orchestration" (task planning, tool calling) becomes the primary bottleneck, accounting for over 90% of total inference latency.
* **The Inference Shift:** Hardware demand is shifting from pure training to an "inference inflection." The market is bifurcated by workload type: training workloads retain best price-performance on H100s (keeping Hopper demand structurally sticky), while large MoE inference workloads run best on the latest large world-size systems (e.g., GB300 NVL72). Watch for specialized inference chips challenging Nvidia's moat.
* **Heterogeneous Memory Architecture:** The "one-size-fits-all" DDR5 model is giving way to a hierarchy tuned for specific workload phases: **SRAM** (ultra-fast, low-capacity, decode) > **HBM** (high bandwidth, prefill) > **LPDDR5X** (low-power, moving from mobile to servers) > **DDR5** (general-purpose). In power- and cooling-constrained environments, memory has become an active design variable rather than a fixed component.
* **N3 Wafer Scarcity:** TSMC's N3 node is the single biggest constraint in the AI supply chain. AI-related silicon is consuming ~60% of N3 wafer output in 2026, modeled to reach 86% by 2027 — nearly entirely squeezing out smartphone and CPU wafers — with effective utilization on track to exceed 100% in H2 2026. TSMC cannot expand cleanroom space quickly enough — their CapEx only exceeded its prior peak in 2025, and they were caught flat-footed by the pace of AI demand.
* **Arm's Market Position:** Arm CPUs already account for ~40% of the cloud data center market (Futurum Group), with over 1 billion deployed Neoverse cores — driven by hyperscaler custom Arm chips (AWS Graviton, Azure Cobalt, Google Axion). Arm is transitioning from pure IP licensing to direct silicon production (AGI CPU), making it a new competitive force while simultaneously supplying the architecture underlying its licensees' custom chips.
* **Semiconductor Moats & Custom Silicon:** NVIDIA dominates but faces structural customer defection as hyperscalers develop custom silicon (TPUs, Trainium, Graviton). ASICs are forecast at 27.8% of AI server shipments in 2026, rising to ~40% by 2030 (TrendForce). AWS expects Trainium to save "tens of billions of capex dollars per year" and deliver several hundred basis points of operating margin advantage for inference — making custom silicon a margin imperative, not just a supply hedge.
* **HBM Structural Crowdout:** HBM absorbs ~3× more DRAM wafer capacity per bit than commodity DRAM — widening to ~4× with HBM4 and further with HBM4E. HBM content per accelerator is growing rapidly (Rubin Ultra carries ~4× more HBM than Blackwell; TPU v8AX and Trainium3 migrating from 8-Hi to 12-Hi stacks). Reallocating capacity from weakening consumer markets would release only ~3% of total DRAM demand — insufficient to move the needle. As major suppliers accelerate toward HBM and DDR5, they are exiting niche markets (2D NAND, SLC NAND, niche DRAM), creating second-order supply gaps being filled by smaller, lower-tier players.
* **Memory Market: LTA Structuralization:** The memory market is shifting from short-term/quarterly contracts to Long-Term Agreements (3–5 years). The catalyst is custom AI silicon: memory specs and volumes are locked in at the design stage, making early multi-year procurement commitments a structural necessity. LTAs are reserved for major CSPs (Microsoft, Google, Amazon, Meta, Alibaba, ByteDance) — not offered broadly — reducing supplier cyclicality, improving CapEx visibility, and keeping long-term capacity committed to Big Tech.
* **Foundry Diversification:** The geographic concentration of TSMC's advanced packaging capacity in Taiwan is pushing customers toward alternatives on supply and geopolitical grounds. Intel Foundry (EMIB) is gaining favor backed by US government support; Samsung Foundry is also gaining share. CoWoS packaging constraints are easing as N3 wafer availability becomes the dominant bottleneck; CoWoS is being outsourced to OSATs (ASE/SPIL, Amkor).
* **Depreciation Risk:** New chip cycles (e.g., Blackwell) offer massive performance gains (~2.5x), rapidly devaluing prior-generation hardware — a structural dynamic benefiting leading-edge suppliers and pressuring operators holding older inventory.
* **China Domestic Memory & Export Controls:** China's domestic memory industry is scaling aggressively via HK listings and multi-billion dollar procurement LTAs. Over time this could erode US export control efficacy and bifurcate the global memory market into separate Western and Chinese supply chains. Export restrictions remain a structural ceiling on addressable market for US chip companies — unlikely to ease under current geopolitical conditions.

##### Watch
* N3 utilization rates — approaching 100%+ in H2 2026; monitor TSMC capacity commentary
* GPU spot pricing — H100 hourly rates as a real-time demand barometer
* DRAM/NAND contract pricing — leading indicators for data center inventory cycle peak
* Custom silicon market share trajectory — 27.8% → ~40% by 2030; pace of adoption matters
* China domestic memory scaling — threat to commodity tiers and export control efficacy
* Intel 18A yield progress — gating factor for the foundry diversification thesis

#### Current Status
The sector is in acute supply scarcity. GPU compute is effectively sold out through late 2026 — Blackwell lead times extend to June–July with all capacity through August–September committed. H100 spot pricing has rebounded ~40% from its October 2025 trough to ~$2.35/hr; on-demand capacity is exhausted across all GPU types. Memory prices are inflecting sharply: LPDDR5X and DDR5 contract prices tracking ~4–5x year-on-year increases, with Q2 2026 DRAM and NAND contract pricing forecast at +60% and +70% QoQ respectively. The structural driver is industry-wide convergence on TSMC N3, where effective utilization is on track to exceed 100% in H2 2026. Custom silicon is gaining share rapidly — ASICs at 27.8% of AI server shipments in 2026, with AMD-Meta's $100B deal anchoring the multi-year hyperscaler CapEx cycle.

#### Developments
* **Nvidia Vera Standalone Launch (2026):** Nvidia decoupled the Vera CPU (Olympus architecture) for standalone sales to capture the structural demand surge in agentic server configurations. Early partners include Alibaba, Cloudflare, CoreWeave, and Nscale.
* **Arm AGI CPU Launch (2026):** Arm's historic pivot from IP licensing to direct silicon — a 136-core CPU built on TSMC N3, with Meta as co-developer and inaugural customer; OpenAI, Cerebras, Cloudflare, and others also adopting. Liquid-cooled vs. air-cooled performance differential: 45,000+ cores/rack vs. 8,000+ — a 5x gap illustrating the liquid cooling performance premium. Targeting neoclouds unable to justify the overhead of bespoke custom silicon design.
* **Intel 18A Yield & Delay Reports (April 2026):** Yield issues (<50%) on the Intel 18A process for Clearwater Forest and Diamond Rapids threaten mass production timelines, potentially pushing delivery into 2027 — a competitive opening for TSMC-based EPYC Venice.
* **HBM4 Strategy Divergence (2026):** Samsung chasing 80% yields on 1c-based HBM4 using a performance-first SF4 logic base die; SK Hynix trimmed HBM4 shipments by 30% due to Rubin delays, redirecting capacity to HBM3E.
* **DDR5 Margin Flip (2026):** Micron reported non-HBM (DDR5) margins now exceeding HBM profitability, projecting 81% gross margin in Q3 FY26 as HBM3E oversupply and Rubin delays temporarily shift pricing power.
* **AMD-Meta Structural Partnership (2026):** AMD and Meta struck a landmark **$100B, 6 GW chip deal** — a major quantitative anchor for the "Big Tech Subsidy" and validation of AMD as a primary beneficiary of the multi-year hyperscaler CapEx cycle.
* **SOCAMM Adoption (2026):** Emergence of SOCAMM (Small Outline Compression Attached Memory Module) for LPDDR5X in servers — bridging high efficiency with serviceability to enable LPDDR5X's transition from mobile to production server environments without the "soldered" maintenance penalty.
* **GPU Spot Pricing: Supply Exhaustion (Q1–Q2 2026):** H100 1-year rental contracts rose ~40% from $1.70/hr (October 2025 trough) to $2.35/hr (March 2026), defying prior expectations that Hopper pricing would decline with Blackwell's ramp. On-demand capacity effectively sold out across all GPU types; p6-b200 spot instances on AWS trading at $14/hr. Blackwell lead times extend to June–July 2026; all capacity through August–September committed. Existing H100 contracts are being renewed at original rates for 4-year extensions through 2028. Two large AWS customers independently asked to purchase every Graviton instance available in 2026 — AWS declined to preserve availability.
* **Intel EMIB-T & TSMC US Packaging Acceleration (2026–2028):** Intel in active discussions with Google and Amazon to provide EMIB-T advanced packaging for their ASIC programs; commitments targeted for H2 2026 with customers reportedly willing to prepay in the billions. Intel CFO highlighted advanced packaging as the "more interesting part" of the Foundry business with ~40% gross margin potential. Intel's Malaysia assembly operations come online in 2026; New Mexico (Fab 9, Fab 11X) is already in mass production for 3D packaging. In parallel, TSMC is accelerating its US advanced packaging facility — construction beginning Q2 2026 (one quarter ahead of prior expectations), targeting operations late 2027–2028, deploying SoIC, CoW, and CoPoS technologies.
* **Custom Silicon Scaling: Amazon & Broadcom-Google (2026–2031):** Amazon's in-house silicon already tracking $20B+ annual revenue; CEO Andy Jassy confirmed exploring external rack sales (~$50B run rate potential if standalone, exploratory). Broadcom entered a long-term agreement with Google to develop and supply future generations of custom AI chips and rack components through 2031 — further entrenching the AVGO-GOOGL relationship and reducing Google's NVDA dependency.
* **Memory LTA Deals Accelerating (H1 2026):** Micron secured its first 5-year strategic customer agreement (March 2026 earnings) and is in active discussions with multiple clients. Samsung adopted a strict 3-year minimum LTA policy for all new contracts, with late-stage negotiations with AMD, Microsoft, and Google. SK Hynix pursuing a 5–7 year LTA with Google for commodity DRAM and a 3-year DDR5 LTA with Microsoft valued at "tens of trillions of won." Deals include downside price floors and 10–30% upfront prepays.
* **OEM Repricing Loop (2026):** OEMs repriced AI servers beyond underlying component cost increases to manage margin risk → compressed project returns → slow-rolled deployments → supply withheld from rental market → rental market tightened further. A self-reinforcing dynamic and leading indicator of supply withholding.
* **Industry N3 Convergence (2026):** Every major AI accelerator platform converged on TSMC N3 simultaneously: NVIDIA (Rubin on 3NP), AMD (MI350X/MI400 on N3), Google (TPU v7 on N3E, TPU v8 on N3), AWS (Trainium3 on N3P), Meta (MTIA on N3). The structural driver of the N3 capacity squeeze.
* **Samsung 2nm Yield Struggles (April 2026):** Samsung Foundry 2nm yields stalled at ~55%, below the ~60% mass production threshold. Qualcomm selected TSMC N2P for its next-generation Snapdragon. Samsung retains Tesla's AI5/AI6 programs and domestic AI startup DeepX — but the yield gap concretely anchors TSMC's competitive moat at advanced nodes. (Source: TrendForce, April 2026)

#### Companies of Interest
TSM, NVDA, AMD, AVGO, ASML, AMAT, LRCX, KLAC, MU, SSNLF, HXSCL (SK Hynix), AMKR, ASX, ARM, META

---

### Networking & Optical

#### Structural Themes
* **Optical Interconnects as Scaling Solution:** As AI cluster sizes grow, optical interconnects are the primary solution for data transfer latency constraints. Co-packaged optics (CPO) represent a potential technology transition that could disrupt incumbent transceiver suppliers.
* **Supplier Lock-in:** Hyperscalers are signing 2–3 year guaranteed contract minimums for transceivers and optical circuit switches amid supply constraints — transforming cyclical hardware suppliers into high-margin, mission-critical utilities. Concentration risk remains: a handful of hyperscaler customers hold significant leverage on contract terms.
* **The Copper Debate:** Copper interconnects remain a competing solution at shorter distances; hyperscaler preference between copper and optical at varying link lengths is an ongoing structural debate with real TAM implications for optical suppliers.
* **Dark Fiber as AI Training Substrate:** Building multi-datacenter AI training factories (e.g., Nvidia Spectrum-X) requires dedicated, high-capacity point-to-point dark fiber links — a structural new demand vector distinct from general data center networking.
* **Rural Data Center Fiber Demand:** New AI data centers are increasingly sited in tier-two markets for power availability. Backhauling traffic to carrier-neutral facilities is inefficient, driving dedicated fiber and wave buildouts along routes that didn't previously require this infrastructure. Lumen has identified "dozens of new data center clusters across the US" requiring fiber, wave, and IP services and is actively building a specialized AI fabric to serve them.

##### Watch
* Hyperscaler preference shifts between copper and optical at various link lengths
* Co-packaged optics adoption timeline — could restructure the transceiver supplier landscape
* Dark fiber and wave buildout pace in non-traditional markets

#### Current Status
Optical transceiver demand is surging alongside AI cluster buildout — LightCounting forecasts Ethernet transceiver sales for AI clusters to double in 2026. Supply constraints are pushing hyperscalers to sign multi-year guaranteed minimums, locking in supplier revenue streams. Fiber optic cables are experiencing price spikes alongside GPUs, DRAM, and NAND, confirming the infrastructure buildout is pressuring the full networking supply chain. Nvidia's $6B strategic investment sweep across Marvell, Coherent, and Lumentum signals an attempt to architect control over the interconnect layer.

#### Developments
* **Nvidia "Full Stack" Interconnect Strategy (2026):** Nvidia secured architectural control over the interconnect layer via $6B in strategic investments in Marvell, Coherent, and Lumentum — ensuring third-party custom chips remain dependent on Nvidia-defined NVLink Fusion and CPO frameworks.
* **Coherent-Lite Adoption (2026):** Emergence of O-band "Coherent-Lite" transceivers for 10–40km "Campus Reach" links, reducing power by 50% vs. traditional coherent optics.
* **Fiber Optic Demand Surge (Q1 2026):** Fiber optic cables explicitly cited alongside GPUs, DRAM, and NAND as components experiencing price spikes — confirms the infrastructure buildout is pressuring the full networking supply chain, not just compute and memory.
* **Optical Transceiver Sales Doubling (2026):** LightCounting forecasts Ethernet optical transceiver sales for AI clusters to double in 2026 — a concrete demand signal tied directly to AI cluster buildout pace. (Source: LightCounting, 2026)

#### Companies of Interest
LITE, CLS, AAOI, MRVL, COHR

---

### Infrastructure & Power

#### Structural Themes
* **Demand Shock:** Data center REITs are experiencing a "demand shock" with guaranteed 15–20 year leases — a structural shift in the nature and duration of demand commitments.
* **Liquid Cooling as Baseline Architecture:** As advanced silicon processors approach 100°C reliable operating junction temperatures, traditional air cooling becomes unviable. Cooling accounts for up to 60% of a facility's total energy costs — liquid cooling materially reduces this and has crossed from an emerging option to a baseline architectural assumption in AI data center reference designs.
* **The Human Logistics Constraint:** Physical labor required to build 2-gigawatt campuses is tapped out, driving massive multi-million dollar contracts simply to house and support construction workforces.
* **Redesign Risk:** Chip generation transitions can trigger mid-build data center redesigns, causing delays and cost overruns. Physical holdups delay not just construction revenue but the operating revenue of the completed facility — amplifying the financial impact of bottlenecks.
* **The "Neocloud" AI Factories:** A sub-layer of dedicated AI cloud providers has emerged, securing multi-billion dollar, multi-year capacity contracts from hyperscalers (e.g., $25B+ backlogs from Meta and Microsoft) to build dedicated, liquid-cooled GPU clusters. Less than 10% of existing US data center inventory is currently capable of supporting "true AI-dense critical load" (JLL) — underscoring the scale of buildout remaining and the structural advantage of purpose-built facilities.
* **Enterprise Production Reality:** Only 22.8% of AI initiatives successfully meet their original ROI objectives in production (HyperFrame Research). Enterprise evaluation criteria have shifted from capacity/price to production reliability, lifecycle controls, and stable performance under sustained demand — favoring mature, purpose-built neocloud platforms over capacity-only providers.
* **Neocloud Financial Risk:** Operators frequently deploy GPUs before facilities are fully operational, relying on short-term bridge financing that assumes rapid time-to-revenue. Supply chain, construction, or power procurement slippage leaves GPU assets idle and makes refinancing extremely difficult. Lenders are already scrutinizing utilization assumptions and long-term demand visibility.
* **Water Scarcity as Emerging Constraint:** As liquid cooling becomes the baseline architecture, water availability and treatment quality become critical dependencies. Water quality failures (biological growth, corrosion, scaling) represent direct operational risk; facilities in water-constrained regions are already resorting to recycled water with on-site storage and treatment.

##### Watch
* Neocloud prepay and contract term trends — leading indicator of marginal demand tightening
* Mid-term GPU rental contracts (3 months to 3+ years) — the most economically relevant segment and best real-time demand signal
* Grid interconnection timelines and moratoriums — binding constraint in key markets
* Behind-the-meter power commitments — scale and pace of on-site generation as grid alternative

#### Current Status
The sector has transitioned from the 2024 land grab to full execution mode. Neocloud pricing power has shifted decisively — operators now demand 20%+ prepays, longer contract terms, and set deployment timelines on their own schedule. Major AI labs are locking in 50–100MW clusters (~24,000–48,000 GB300 NVL72 GPUs) on 4–5 year terms; CoreWeave's $21B Meta contract anchors the scale of individual deals. Grid constraints are now severe enough to push Oracle to commit 2.8GW of Bloom Energy fuel cell power as behind-the-meter generation. The Midwest is absorbing overflow demand — currently a third of US capacity and projected to account for more than half of new supply coming online. The construction workforce itself is a binding bottleneck.

#### Developments
* **Microsoft/Nscale Capacity Grab (April 2026):** Microsoft secured 30,000 Nvidia Rubin GPUs in Norway after OpenAI dropped out — indicating a "catch-up" phase in hyperscale capacity after previous spending curbs.
* **Logistics Demand Surge (2026):** Savills reports the DC supply chain is triggering 8.46 million sq ft of logistics demand in Europe (~8,900 sq ft per MW) as suppliers take traditional warehouse space to support the buildout.
* **Neocloud Market Power Shift (late 2025–2026):** Before late 2025, GPU rental pricing was competitive. By early 2026, Neoclouds and Hyperscalers are firmly in control — demanding higher prepays (20%+), longer contract terms, and setting deployment timelines on their own schedule.
* **Long-Term Offtakes (2026):** Major AI labs locking in 50MW–100MW clusters on 4–5 year terms. Hyperscalers backstopping deals in exchange for a share of project revenue — reinforcing the circular loop. CoreWeave's $21B AI compute contract with Meta (April 2026) is the concrete scale anchor.
* **Gas Turbine Demand Spike (Q1 2026):** Gas turbines cited alongside GPUs, memory, and fiber as components experiencing price spikes — confirming power generation equipment is a binding constraint in the infrastructure buildout.
* **Midwest Data Center Geography Shift (2026):** Midwestern data centers constitute a third of all US capacity and will account for more than half of new capacity coming online, driven by power scarcity in traditional markets. Synergy Research Group tracking a pipeline of 803 DC projects; secondary markets (New Albany, Atlanta) absorbing demand Tier-1 markets can no longer accommodate. (Source: Fierce Network / Synergy Research Group, April 2026)
* **Behind-the-Meter Alternative Power at Scale (April 2026):** Oracle committed to up to 2.8GW of Bloom Energy fuel cell power for US cloud infrastructure projects — the largest known behind-the-meter alternative power commitment to date. Signals grid constraints are severe enough to drive hyperscalers toward multi-gigawatt on-site generation. (Source: Fierce Network, April 2026)

#### Companies of Interest
MSFT, AMZN, GOOGL, META, DLR, EQIX, VRT, ETN, JCI, SBGSY, TH, JBL, NBIS, CRWV, IREN

---

### Nuclear & Energy

#### Structural Themes
* **AI Power Demand as Structural Driver:** The scale of AI data center buildouts creates sustained, long-duration baseload demand that renewable intermittency cannot reliably serve — elevating the structural case for nuclear.
* **The Nuclear Renaissance:** SMRs (Small Modular Reactors) are emerging as the favored solution for dedicated AI campus power, with active DoD and hyperscaler interest. SMR economics remain unproven at scale, cost overruns are a historical nuclear pattern, and capacity factor and reliability risk for first-of-kind designs is a distinct hazard from cost — the buildout thesis is real but execution risk is material on multiple dimensions.
* **Government Catalysts:** OTA (Other Transaction Authority) and the Reactor Pilot Program are accelerating deployment pathways outside traditional NRC certification timelines. White House space nuclear policy adds a third accelerant. NRC design certification timelines remain long even with these pathways — a structural constraint on deployment speed.
* **Mine-to-Megawatt Supply Chain:** The supply chain extends from uranium mining through enrichment, fuel fabrication, and reactor components — domestic supply chain security is a structural theme alongside reactor deployment. Uranium price volatility affects project economics.

##### Watch
* SMR design certifications — NRC progress on accelerated pathways
* Hyperscaler nuclear procurement announcements
* Uranium spot prices — leading indicator for project economics
* Gas turbine pricing — near-term proxy for AI power demand pressure on conventional generation equipment

#### Current Status
Still early-stage but gaining policy and commercial momentum. AWS stood up 3.9GW of new power capacity in 2025 and plans to double its total footprint by end of 2027. Gas turbines are spiking in price alongside compute components, confirming power generation equipment is a binding near-term constraint. Government policy is stacking — OTA, the Reactor Pilot Program, and the White House space nuclear directive create a multi-front acceleration environment, though commercial SMR deployments at scale remain years out.

#### Developments
* **Gas Turbine Demand Spike (Q1 2026):** Gas turbines spiking in price alongside GPUs, memory, and fiber — a direct signal that AI data center power demand is now pressuring conventional power generation equipment supply chains.
* **AWS Power & CapEx Scale (2025–2027):** AWS stood up 3.9GW of new power capacity in 2025 and expects to double its total power footprint by end of 2027. AWS committed ~$200B in capex in 2026, driven by concrete customer commitments, with monetization expected primarily in 2027–2028.
* **White House Space Nuclear Policy (April 2026):** White House policy directing NASA, the Pentagon, and DoE to develop space nuclear power systems with a launch target as soon as 2028 — extending the nuclear mandate into space infrastructure alongside OTA and the Reactor Pilot Program. (Source: SpaceNews, April 2026)

#### Companies of Interest
CCJ, BWXT

---

### Software & Disruption

#### Structural Themes
* **Frontier Model Consolidation:** The "Big 5" (OpenAI, Anthropic, Google, Meta, xAI) are consolidating the frontier model layer. Switching costs are low at the model layer but much higher for orchestration/agent frameworks and data services — the durable moats sit above and below the raw model.
* **The Revenue Test:** Application layer revenue must ultimately support all underlying infrastructure layers. The ~$600B Revenue Imperative is the macro test; individual ARR scaling rates are the micro signal.
* **Software Disruption vs. Moat Durability:** AI tools (including "vibe-coding") create a narrative that enterprise software can be replicated or replaced. Counter-arguments center on switching costs, network effects, deep integrations, and the difficulty of replicating embedded enterprise workflows at scale. This tension is now affecting software companies' ability to refinance debt — a real credit market signal, not just a narrative.
* **Edge AI & Specialized Data Moats:** AI is breaking into the physical world. Companies processing AI data at the edge on proprietary hardware (satellites, autonomous vehicles, diagnostic machines) or using multimodal data libraries as the operating system for specialized fields carry structural data moats. Fiber latency physics constrain round-trip processing to ~1ms per 125 miles; AR/VR requires <3ms while typical carrier targets are ~10ms — a gap only closable by local edge processing.
* **The Subsidy Effect:** Application developers benefit most from declining compute prices as infrastructure CapEx absorbs demand risk. This subsidy compresses as the reflexive loop matures.
* **Vertical Integration Pressure:** Supply scarcity is pushing even the application layer toward custom silicon — a single AI lab can represent an enormous, multi-year demand pipeline for infrastructure providers.

##### Watch
* AI Lab ARR growth rates — pace of Revenue Imperative validation
* Token demand breadth — broad-based vs. single-player driven growth matters for systemic durability
* Software company debt refinancing conditions — early signal of disruption narrative becoming a credit event
* Model switching cost erosion — speed of displacement at the model layer

#### Current Status
The application layer is generating real revenue at scale. Anthropic ARR surged from ~$9B to over $30B in Q1 2026 — more than tripling in a single quarter — driven by Claude 4.6 Opus and Claude Code, with growth compute-constrained rather than demand-constrained. Demand is broad-based and global: open models (GLM, Kimi K2.5) and native media generation platforms (Seedance) are contributing alongside the major labs. Multi-agent, multi-step workloads executing with high concurrency are the primary driver of the token demand inflection. The Revenue Imperative thesis is being validated from the demand side; the binding constraint has flipped from demand to supply.

#### Developments
* **Anthropic Exploring Custom Silicon (2026):** Anthropic in early-stage exploration of in-house chip design in response to compute shortage constraining Claude's growth — no committed design or dedicated team yet, and may ultimately continue relying on external hardware. Current training mix spans AWS Trainium, Google TPUs, and NVIDIA GPUs. Broadcom has signed a deal to provide Anthropic ~3.5 GW of AI compute capacity using Google's AI processors starting 2027. Anthropic's projected total cloud spend ~$80B through 2029, spanning CoreWeave, Google/Broadcom, Microsoft Azure, and AWS.
* **Agentic Token Demand Inflection (Q1 2026):** Anthropic ARR surged from ~$9B to over $30B in a single quarter — growth was compute-constrained, with actual demand exceeding available supply. Multi-agent workloads executing multi-step tasks with high concurrency and continuous iteration are the primary driver. A direct data point for the Revenue Imperative thesis: the application layer is generating real revenue at scale with the binding constraint now supply, not demand.

#### Companies of Interest
PLTR, SNOW, MDB, DDOG, CRWD, PANW, IBM, ORCL, CRM, ADBE, NOW, WDAY, INTU, HUBS, TSLA, PL, SOUN, TEM

---

## Critical Minerals & Rare Earths

### Structural Themes
* **The Mine-to-Magnet Imperative:** Physical AI infrastructure cannot be built without secure domestic supply chains. The US government and defense sector are actively subsidizing decoupling from the Chinese monopoly on heavy rare earths. Terbium and Dysprosium currently command up to a 5x price premium outside China, benefiting domestic processors.
* **The Copper Constraint:** Global copper demand is forecast to exceed 40 million tons by 2040, driven by electrification and data center buildouts — elevating the strategic value of advanced explorers near existing mining infrastructure.
* **Vertical Integration Premium:** Mine-to-magnet vertical integration is a key differentiator — companies controlling the full supply chain from mining through separation and magnet production carry strategic premium. Chinese rare earth processing dominance is deeply entrenched; domestic alternatives face cost and scale disadvantages.
* **Structural Headwinds:** Permitting and environmental timelines for new mines remain long. Rare earth price volatility is largely driven by Chinese export policy — a geopolitical variable outside domestic control.

#### Watch
* Chinese rare earth export policy — the primary price and supply lever
* DARPA Smash Program milestones — if successful, structurally undermines the Chinese processing monopoly
* Domestic processing capacity ramp — commercial scale is the missing link

### Current Status
Decoupling efforts are accelerating via government subsidies, but commercial-scale domestic alternatives remain limited. Rare earth prices outside China are elevated (up to 5x premium on key elements), providing near-term margin support for domestic processors. The DARPA Smash program is the most structurally significant catalyst on the horizon.

### Developments
* **DARPA "Smash" Program (2026):** A 4-year initiative for near-zero-waste separation of all 80 stable elements — aimed at rendering the Chinese processing monopoly obsolete and solving broader mineral shortages.

### Companies of Interest
MP, UURAF, UUUU, USAR, NB, CCJ, BWXT, NVRED

---

## Defense & Aerospace

### Structural Themes
* **Dual-Use Technology:** Defense spending increasingly overlaps with AI and space infrastructure themes — autonomous systems, edge AI, geospatial intelligence, and satellite-to-cellular are all dual-use.
* **Autonomous Warfare:** Drone autonomy and hypersonic development are active procurement priorities.
* **Space Infrastructure:** The Space Development Agency and commercial space are building persistent LEO constellations for communications and intelligence. The US government has set a structural goal to attract at least **$50B of new investment** in American space markets by 2028 — a multi-year policy tailwind analogous to the CHIPS Act.
* **Orbital Data Centers:** A structural subset of the Edge AI theme. As terrestrial data centers face land and power constraints, the orbital data center market is emerging as an edge compute frontier — requiring vertically integrated satellite-compute-rocket platforms and specialized thermal management for AI-dense critical loads in orbit.
* **"Combat-Ready Force" Doctrine:** Space Force's structural shift from rhetoric to execution, focusing on maneuverable and refuelable orbital assets to counter contested environments. Budget and continuing resolution uncertainty remain a constraint on multi-year contract visibility.

#### Watch
* Congressional budget and CR developments — affects multi-year procurement visibility
* Space nuclear and SMR policy execution — defense and NASA deployment timelines
* Hyperscaler LEO infrastructure acquisitions — signals strategic convergence of Big Tech and space
* Maneuverable satellite doctrine adoption pace — procurement shift from fixed to mobile assets is structural but execution timeline uncertain

### Current Status
The sector is gaining structural policy support simultaneously across multiple vectors. Amazon's $11.57B Globalstar acquisition confirms hyperscaler entry into LEO communications infrastructure. Space Command is advancing a maneuverable satellite warfighting model, with BAE Systems and Lockheed Martin already responding with new designs. The $50B investment target and White House space nuclear policy provide multi-year macro tailwinds. Industry leaders acknowledge that capital is not the constraint — speed and execution are the gating factors.

### Developments
* **Global X Space Tech ETF ($ORBX, 2026):** Launch of the first passively managed "pure-play" space tech ETF amid sector IPOs and growing orbital compute interest.
* **Turion Space Series B ($75M, 2026):** Validates structural demand for maneuverable satellite fleets in a "combat-ready" orbital domain.
* **US Space Investment Policy Anchor (2026):** US government set a structural goal to attract at least **$50 billion of new investment** in American space markets by 2028.
* **Structural Bottlenecks Acknowledged (2026):** Industry leaders and policymakers cautioned that capital alone cannot solve the sector's structural bottlenecks — speed and near-perfect execution are the primary gating factors.
* **Amazon Acquires Globalstar ($11.57B, April 2026):** Amazon acquiring Globalstar for $11.57 billion, consolidating a major LEO satellite-to-cellular constellation under a hyperscaler umbrella. Confirms strategic value of LEO communications infrastructure and marks Amazon as a direct structural player in the space theme. (Source: Fierce Network, April 2026)
* **Space Command Maneuverable Satellite Doctrine (April 2026):** Space Command pushing a warfighting model shifting from fixed spacecraft to maneuverable, refuelable assets for orbital warfare. BAE Systems and Lockheed Martin unveiled new maneuvering satellite designs in direct response; wargames planned to test the concept. (Source: SpaceNews, April 2026)

### Companies of Interest
Phantom Space (Public status unconfirmed)

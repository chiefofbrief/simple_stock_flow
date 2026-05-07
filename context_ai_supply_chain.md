# AI Supply Chain — Layer Map

*Last updated: 2026-05-07*

A layer-by-layer map of the AI supply chain for investment research. Each layer has distinct investment characteristics, structural tailwinds, and company-level theses. This document is self-contained — it incorporates both layer-level detail and the macro dynamics previously maintained separately.

---

## Stack Overview

| Layer | Description |
| :--- | :--- |
| [ 1. Raw Materials & Mining ] | ← upstream inputs |
| [ 2. Semiconductor Equipment & EDA/IP ] | ← fabrication tools, chip design software |
| [ 3. Foundries & Advanced Packaging ] | ← wafer production, chip assembly |
| [ 4. Compute Silicon ] | ← GPUs, CPUs, custom ASICs |
| [ 5. Memory Silicon ] | ← HBM, DRAM, NAND |
| [ 6. Networking & Custom Silicon ] | ← merchant silicon, ASICs, SmartNICs |
| [ 7. Optical & Physical Connectivity ] | ← transceivers, switches, fiber cable |
| [ 8. Power Generation & Grid ] | ← turbines, fuel cells, grid equipment |
| [ 9. Data Center Infrastructure ] | ← buildings, cooling, power delivery |
| [ 10. Hyperscalers & Cloud ] | ← demand drivers, platform builders |
| [ 11. Neoclouds ] | ← pure-play AI compute providers |
| [ 12. Physical AI & Robotics ] | ← edge inference, autonomous systems |
| [ 13. AI-Native Applications ] | ← vertical software, data, agents |

---

## Priority Research Threads

*Cross-cutting investigations that require synthesis across multiple layers and companies. These are not company profiles — they are open research questions where the answer materially affects investment decisions. New threads are added when a structural bottleneck or opportunity is identified that cannot be captured in a single company entry. Threads are marked Resolved when the investment question is answered (position taken, opportunity confirmed absent, or thesis superseded).*

---

### Thread 1: Glass Fiber Cloth Supply Chain
**Status:** Active — structural bottleneck, no near-term resolution
**Why it matters:** Glass fiber cloth is a low-profile raw material sitting beneath every AI server PCB — and a single supplier controls most of the market with no new capacity until mid-2027. Nittobo's near-monopoly in T-glass and NER-glass means this one company is a gating factor on the entire AI server supply chain. This is a Layer 2–3 constraint with direct cost implications for CCL producers, PCB fabricators, and every AI server OEM.
**What we know:**
- Glass fiber cloth is the critical input for Copper Clad Laminates (CCL), the primary PCB substrate material. CCL cost breakdown: copper foil ~42%, resin ~26%, glass fiber cloth ~19%.
- Nittobo controls ~90% of T-glass market share and 60–70% of NER-glass. No new capacity expected until mid-2027 at earliest. Capacity constraints are not expected to ease until then, which will continue to affect costs and lead times across the AI server supply chain.
- Nvidia Rubin GPU substrate has significantly increased layer count and total area vs. prior generation. Cableless rack designs add demand for orthogonal backplanes and midplanes. Rubin LPX rack (inference-optimized, disaggregated) expands total glass fiber consumption further.
- High-end CCL grades M6–M10 (classified by signal loss) are required for AI server applications. Supply is tighter at higher grades.
**Open questions:**
- Who are the CCL laminate producers between Nittobo and PCB fabricators, and do any publicly trade?
- Which PCB fabricators serve the AI server market (Tripod, TTM, Shengyi), and are any public and investable?
- Can any alternative material (low-loss organic, ceramic) substitute for T-glass at acceptable cost and performance for high-end AI server PCBs?
- What is the pricing power signal from Nittobo — are CCL and PCB producers passing cost increases through to OEMs, and is this showing up in server BOM inflation?
**Investable angles:**
- Nittobo (privately held, Japanese) — not directly investable but a key cost signal for AI server economics
- CCL/PCB names: requires further research to identify publicly traded names exposed to the supply squeeze

---

### Thread 2: Glass Substrate Advanced Packaging
**Status:** Active — technology transition underway, timeline uncertain
**Why it matters:** As AI chip package sizes grow, organic substrates are hitting physical limits — warpage under heat during assembly reduces yield and becomes increasingly unmanageable at large die areas. Glass (core substrates and interposers) solves the warpage problem and enables the next generation of advanced packaging. This is a Layer 3 technology transition with implications for Intel's foundry differentiation, Corning's cross-layer thesis, and the entire OSAT supply chain.
**What we know:**
- Traditional organic substrates warp under high temperatures during assembly. Warpage directly reduces manufacturing yield and scales worse as package sizes grow — driven by the AI chip trend toward larger, more complex packages.
- Two glass-based solutions are emerging: (1) **glass core substrate** — replaces the traditional organic core layer with glass; (2) **glass interposer** — replaces silicon interposers with glass, enabling better signal integrity and lower cost at scale.
- Intel debuted its first EMIB + glass core substrate sample in January 2026. A "No SeWaRe" (no sealing warp result) validates mechanical integrity — mass production one step closer. Intel committed to glass substrates in its advanced packaging roadmap as early as 2023, making them the earliest and most publicly committed mover.
- Corning has glass manufacturing expertise across multiple domains (optical fiber, display glass, specialty glass). Their specific play in glass core/interposer is uninvestigated — this is an open research priority.
**Open questions:**
- What is Corning's specific glass substrate program — glass core, glass interposer, or both? What is the volume/timeline/customer pipeline?
- Are any TSMC CoWoS customers (Nvidia, AMD, Google) moving toward glass substrates, or is Intel the only mass-production-intent user?
- Who supplies the raw glass panels used in glass core/interposer (Corning, AGC, Schott)? Is there a supply bottleneck at the panel level analogous to the Nittobo situation in glass fiber cloth?
- What yield rates are Intel achieving on glass core vs. organic? How long before glass substrate is cost-competitive with organic at volume?
- Do OSATs (AMKR, ASX) have glass substrate capability, or does this require new equipment and process development?
**Investable angles:**
- Intel (INTC) — earliest public mover; glass core substrate could become a foundry differentiation moat if competitors are 2+ years behind on process readiness
- Corning (GLW) — potential cross-layer beneficiary if their glass manufacturing expertise translates to glass substrate volume production; currently unconfirmed — research priority
- Glass panel suppliers: AGC (Japan, not yet investable via US market), Schott (private) — requires further identification of investable names

---

### Thread 3: CPO (Co-Packaged Optics) Testing Bottleneck
**Status:** Active — structural gap before volume ramp
**Why it matters:** Co-packaged optics (CPO) integrates optical transceivers directly into switch ASICs, eliminating pluggable modules. This is the next major Layer 7 transition — it reduces power consumption by ~30–50%, reduces latency, and is required for 800G/1.6T scale-out interconnect bandwidth. CPO introduces entirely new test challenges: testing photonic integrated circuits (PICs) at wafer and package level has no standardized automated solution today. This is a Layer 2 (equipment) and Layer 7 (connectivity) intersection.
**What we know:**
- Current PIC inspection is manual, >100 seconds per device, no unified industry standards. This is not viable for high-volume production.
- Teradyne acquired Quantifi Photonics in 2025 — their first explicit move into automated PIC test. Positions Teradyne as the incumbent-with-a-head-start for automated CPO test equipment.
- Advantest is the primary competitor. Their photonics test capability is less established but they have the financial resources and semiconductor test infrastructure to catch up.
- TSMC's COUPE (Co-packaged Optics Using Photonics Extension) platform was entering volume production in 2026 — creates forced demand for automated PIC test at TSMC scale.
- CPO is not yet mainstream in AI servers — transition timeline is 2026–2028 based on current roadmaps. Test equipment procurement leads production ramps by 12–18 months.
**Open questions:**
- How large is the TAM for CPO test equipment, and at what volumes does it become material to Teradyne/Advantest revenue?
- Has Advantest acquired or built comparable PIC test capability? What is their current CPO test roadmap?
- Who manufactures the PIC dies used in CPO (Intel Silicon Photonics, Coherent, Marvell)? Do they have in-house test capability or are they dependent on external ATE?
- What is the timeline from TSMC COUPE volume production to volume CPO deployment in hyperscaler racks?
- Are there any pure-play CPO test equipment companies (private or public) that Teradyne/Advantest would need to acquire?
**Investable angles:**
- Teradyne (TER) — Quantifi acquisition is the clearest CPO test investment thesis; monitor for CPO test revenue disclosure and COUPE-related order flow
- Advantest (ATEYY/6857) — if they close the CPO test gap, they become a competing thesis; currently less clear
- Coherent (COHR) — CPO transceiver and PIC manufacturer; in the demand stream as both a supplier and a test customer
- Marvell (MRVL) — CPO ASIC integration; if CPO becomes the switching standard, Marvell's CPO-capable ASICs are a direct beneficiary

---

## Structural Dynamics

*The mental models that make this stack interpretable. Read these before the constraint map.*

**The Reflexive Loop.** Hyperscalers fund AI labs and startups → labs spend that capital on cloud credits and chips → hyperscaler revenues grow, justifying more CapEx → which funds more labs. The loop is self-reinforcing: high stock prices lower the cost of capital, enabling record CapEx, which generates revenue, which justifies more CapEx. This is why upstream constraints compound rather than self-correct — every layer of the stack is being pulled forward simultaneously by the same demand engine. The loop has a logical endpoint: the application layer must eventually generate revenue at a scale that validates the infrastructure investment. Track this through AI lab ARR growth rates, cloud AI services revenue acceleration, and token demand breadth. When the loop is healthy, every constraint in this document is a tailwind for the companies best positioned to relieve it.

**The Constraint Migration Pattern.** Bottlenecks in this stack do not disappear — they move. Capital was the binding constraint in 2023; silicon became the constraint in 2024–2025; power is the emerging constraint for 2027–2028. Understanding where the bottleneck is today and where it is migrating is more valuable than tracking any single layer in isolation. The "Where Constraints Are Heading" section operationalizes this framework. Each migration creates a new set of beneficiaries and makes the prior set's pricing power transient.

**Jevons' Paradox.** As AI becomes more efficient — cheaper to run, smaller models, better inference optimization — total hardware demand increases rather than decreases. Efficiency lowers the cost of deploying AI, which makes it accessible to more users and more use cases, which expands total consumption beyond what the efficiency gains saved. Every model compression breakthrough, every inference optimization, every cost-per-token reduction has historically accelerated adoption and increased aggregate hardware demand. This is the standing structural rebuttal to the bearish argument that efficiency gains will reduce demand for chips, memory, and power.

---

## Stack Snapshot

*Last updated: 2026-05-07*

The AI infrastructure buildout is in peak execution mode. Capital is no longer the binding constraint — silicon, memory, power, and construction labor are all strained simultaneously, an unusual confluence that reflects the true scale of the demand shock. The reflexive loop remains intact and accelerating.

**Demand Signal — AI Labs:** The private foundation model companies (Anthropic, OpenAI, xAI, Mistral) are the single largest upstream demand signal in the stack. Their compute purchases, infrastructure commitments, and GPU reservation volumes flow directly into hyperscaler and neocloud revenue. Track them through proxies: Anthropic ARR surged from ~$9B to over $30B in Q1 2026 — more than tripling in a single quarter — with growth compute-constrained rather than demand-constrained. OpenAI's Oracle and CoreWeave commitments, xAI's cluster buildout, and Anthropic's ~$80B projected cloud spend through 2029 are all upstream demand anchors. When these labs accelerate, every layer from Layer 3 upstream tightens.

### Current Constraint Map

| Layer | Status | Key Signal | Highest-Conviction Names |
|---|---|---|---|
| 1. Raw Materials & Mining | Tightening | Rare earth ex-China prices at 5x premium; uranium demand building | MP, CCJ, FCX |
| 2. Semiconductor Equipment & EDA/IP | Tightening | TSMC CapEx at high end of $52–56B range; N2/A16 buildout sustained through decade | ASML, LRCX, KLAC, AMAT, CDNS, SNPS |
| 3. Foundries & Advanced Packaging | **Shortage** | N3 utilization on track to exceed 100% H2 2026; Q2 revenue +32% YoY at 65.5–67.5% gross margin | TSM, AMKR |
| 4. Compute Silicon | **Shortage** | GPU sold out through Aug–Sep 2026; CPU prices +10–20% server / lead times 8–12 weeks; agentic CPU:GPU ratio shift from 1:8 → 1:1–1:2 driving simultaneous GPU + CPU shortage | NVDA, AMD, INTC, ARM |
| 5. Memory Silicon | **Shortage** | HBM demand exceeds 3-year supply; Q1 2026 actuals: DRAM +83% / NAND +160% QoQ; Q2 2026 forecast: DRAM +58–63% / NAND +70–75% QoQ; NAND market forecast to quadruple vs. 2025 | MU, HXSCL |
| 6. Networking & Custom Silicon | Tightening | ASIC share rising 27.8% → ~40% by 2030; design win pipelines accelerating | AVGO, MRVL |
| 7. Optical & Physical Connectivity | **Shortage** | Transceiver demand doubling 2026; hyperscaler-backed fiber expansion into secondary markets | COHR, GLW, ANET |
| 8. Power Generation & Grid | Tightening → Shortage | Gas turbine prices spiking; grid moratoriums forcing behind-the-meter generation | GEV, BE, ETN |
| 9. Data Center Infrastructure | Tightening | Construction labor tapped out; liquid cooling mandatory; dielectric fluid supply now a gating risk | VRT, TH |
| 10. Hyperscalers & Cloud | Silicon-constrained | CapEx roughly doubled vs. prior forecasts; hardware inflation passing through to end users | AMZN, GOOGL, MSFT, META |
| 11. Neoclouds | Supply tight | Market flipped to seller-controlled; demand broadening beyond Big Tech to enterprise finance | CRWV, NBIS |
| 12. Physical AI & Robotics | Early buildout | Tesla AI5 tape-out confirms dedicated custom silicon demand vector for physical AI | NVDA (Jetson), QCOM |
| 13. AI-Native Applications | Demand strong | Daily token calls 100B (early 2024) → 140T (March 2026); compute-constrained not demand-constrained | PLTR, CRWD, NOW |

### Where Constraints Are Heading

*Forward-looking hypotheses — update as signals evolve.*

**N3 shortage is structurally accelerating custom silicon adoption.** GPU scarcity forces hyperscalers to deepen Trainium, TPU, and custom ASIC programs faster than planned. The longer N3 stays constrained, the more structurally committed hyperscalers become — making the shift away from merchant NVDA silicon durable rather than opportunistic. AVGO and MRVL compound as the primary beneficiaries. *Watch: new hyperscaler custom silicon program announcements.*

**As N3 capacity builds (2027–2028), the bottleneck migrates to Power.** Every new chip needs a data center; every data center needs power. The current silicon squeeze is masking what will become a severe power generation and grid constraint at scale. Energy infrastructure — GEV, VST, CEG, CCJ, BWXT — is the next layer to position in as silicon supply eases. *Watch: TSMC N2/A16 capacity ramp timelines as the timing trigger.*

**Power tightening raises the premium on efficiency across the entire stack.** When power is the binding operational constraint, anything delivering more compute per watt gains structural value — liquid cooling (VRT), LPDDR5X over DDR5, ARM architectures, on-site generation (GEV, BE). This is a second-order tailwind benefiting efficiency plays regardless of which specific silicon or generation technology wins.

**Intel 18A is the most important foundry relief valve to watch.** Production-ready 18A yields would unlock meaningful N3-alternative capacity for AMD and hyperscaler ASIC programs currently queued at TSMC. Current yields below 50% make this a 2027 story at best — but any positive yield disclosure is a high-signal event for the foundry diversification thesis and a headwind for TSM pricing power. *Watch: Intel 18A yield disclosures at earnings.*

**DeepSeek V4's KV cache compression is a watch item for NAND demand.** DeepSeek V4 achieved a 90% reduction in KV cache relative to its predecessor — SemiAnalysis explicitly flagged NAND Flash investors to watch out. The Jevons' paradox counter-argument (cheaper inference → more adoption → more aggregate demand) has historically held and remains the structural base case. But if frontier model efficiency gains compress per-inference NAND consumption faster than deployment volumes grow, the NAND bull thesis requires monitoring. *Watch: successor model KV cache ratios; per-inference NAND consumption vs. total inference volume growth.*

**Memory shortage is pushing architectural alternatives into the mainstream.** HBM constraints and surging DRAM prices are accelerating SOCAMM/LPDDR5X adoption as server memory alternatives. If SOCAMM gains production traction, it opens new addressable market for memory suppliers with mobile-heritage efficiency expertise and creates disruption risk for legacy DDR5 server memory configurations. *Watch: SOCAMM production announcements from Micron and SK Hynix.*

### Priority Tracker List

*Organized by thesis type, not rank.*

**Current Beneficiaries** — directly pricing into active shortages now:
NVDA, TSM, MU, HXSCL, COHR, GEV, VRT, AVGO

**Flow Beneficiaries** — positioned for where constraints are migrating next:
MRVL, AMKR, BE, CCJ, BWXT, VST, CEG, ETN, LRCX, KLAC

---

## 1. Raw Materials & Mining

*Profile: Commodity/cyclical with geopolitical premium; long permitting timelines; China processing monopoly is the structural overhang for rare earths; government subsidy tailwind for domestic players.*

Upstream inputs — rare earth elements, copper, uranium, and specialty materials that physical AI infrastructure cannot be built without. Demand is structural and growing across all three vectors simultaneously: rare earths for magnets and electronics, copper for electrification and data center buildout, uranium for the nuclear renaissance powering AI campuses.

### Persistent Themes

**China monopoly on rare earth processing creates a durable geopolitical premium.** China controls the majority of global rare earth processing capacity. Ex-China prices for key magnet materials (Terbium, Dysprosium) are running at up to 5x premium. Domestic decoupling subsidies are accelerating but commercial-scale alternatives remain years out. The moat for companies with integrated mine-to-magnet operations outside China is structural, not cyclical. The DARPA Smash program — a 4-year initiative for near-zero-waste separation of all 80 stable elements — is the most structurally significant catalyst on the horizon; success would render the Chinese processing monopoly obsolete. USA Rare Earth's Serra Verde acquisition is the most significant Western supply chain development to date: by 2027, the combined entity is projected to account for more than 50% of non-China heavy rare earth production, with Brazilian ionic clay feedstock feeding a fully integrated US magnet manufacturing chain. *Watch: DARPA Smash program milestones; USAR Serra Verde integration and Round Top production timeline; Chinese rare earth export policy as the primary price lever.*

**Copper demand is a direct, underappreciated AI infrastructure play.** Data centers and electrification buildout are structural copper demand drivers layered on top of existing EV demand. Global copper demand is forecast to exceed 40 million tons by 2040. Unlike rare earths, copper demand is broad-based and less geopolitically constrained — but supply growth is slow and permitting timelines are long. *Watch: data center construction pace as a leading copper demand indicator.*

**Nuclear renaissance is building durable uranium demand.** SMRs and nuclear PPAs are becoming the preferred long-term power solution for AI campuses. Uranium demand from the power sector has a multi-year ramp ahead regardless of near-term SMR deployment timelines. *Watch: SMR design certifications; hyperscaler nuclear PPA announcements; uranium spot prices as a project economics indicator.*

### Recent Developments

* **DARPA "Smash" Program (2026):** A 4-year initiative for near-zero-waste separation of all 80 stable elements — aimed at rendering the Chinese processing monopoly obsolete and solving broader mineral shortages. The most structurally significant rare earth catalyst currently in the pipeline.
* **USA Rare Earth / Serra Verde Acquisition (May 2026):** USA Rare Earth (Nasdaq: USAR, ~$4.9B market cap) agreed to acquire Serra Verde Group for approximately $2.8B ($300M cash + 126.849M shares at $19.95). Serra Verde operates Pela Ema in Brazil — Latin America's only producing rare earths mine, yielding heavy rare earths including Dysprosium (Dy), Terbium (Tb), Yttrium, Neodymium, and Praseodymium from soft, near-surface ionic clays requiring no drilling or blasting. By 2027, Serra Verde is expected to account for more than 50% of total heavy rare earth production outside China. Stage 1 nameplate capacity: 6,400 tonnes/year of total rare earth oxides; 25-year mine life; projected EBITDA $550–650M annualized by end of next year. The deal includes a 15-year offtake agreement financed by US government agencies with minimum floor prices for four magnetic rare earths. Serra Verde closed a $565M DFC funding package two months before the announcement. The combined entity connects Brazilian feedstock to USA Rare Earth's planned Oklahoma magnet plant, Round Top Texas project (production late 2028), and recently acquired UK magnet maker Less Common Metals — the most complete mine-to-magnet integration outside China now in construction. USAR shares jumped 15% on the announcement.

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| MP | MP Materials | Only US rare earth miner with mine-to-magnet integration; primary beneficiary of domestic decoupling subsidies |
| CCJ | Cameco | Largest publicly traded uranium producer; primary beneficiary of nuclear renaissance demand |
| FCX | Freeport-McMoRan | Largest publicly traded copper miner; leveraged to AI data center and electrification copper demand |
| SCCO | Southern Copper | High-margin copper producer; long reserve life and low-cost operations |
| UUUU | Energy Fuels | US uranium and rare earth producer; dual exposure to nuclear buildout and REE decoupling |
| BWXT | BWX Technologies | Nuclear reactor components, fuel, and services; DoD and commercial SMR exposure; also in Layer 8 |
| UURAF | Appia Rare Earths | Early-stage rare earth explorer; speculative exposure to domestic supply chain buildout |
| USAR | USA Rare Earth | Acquiring Serra Verde (Pela Ema mine) to build the most complete mine-to-magnet heavy REE integration outside China; by 2027 projected >50% of non-China heavy rare earth production; Oklahoma magnet plant + Round Top TX + UK Less Common Metals |
| NB | Niocorp Developments | *[TBD — needs research]* |

---

## 2. Semiconductor Equipment & EDA/IP

*Profile: Oligopoly/monopoly moats at multiple sub-layers; revenue tied to foundry CapEx cycles with a lag; high recurring service revenue provides downside cushion; export controls ceiling on China revenue.*

The tools and software that make chip fabrication possible — and the IP that underlies chip design. An oligopoly toll road on the entire AI silicon buildout: every wafer produced requires equipment from this layer, and every chip designed requires EDA software and licensed IP cores. Two distinct but related sub-layers: capital equipment (ASML, AMAT, LRCX, KLAC) and design software/IP (Cadence, Synopsys, ARM).

### Persistent Themes

**The capital equipment toll road is structural and irreplaceable.** Every chip manufactured for AI — regardless of designer — runs through this layer's tools. ASML holds a monopoly on EUV lithography; KLAC holds near-monopoly on process control metrology; no alternative sources exist for leading-edge nodes. Revenue lags foundry CapEx by 12–18 months, providing visibility into multi-year order books. TSMC CapEx only exceeded its prior peak in 2025 — equipment demand stays elevated through the decade as N2/A16 expansions proceed. *Watch: TSMC CapEx guidance as the primary leading indicator; N2/A16 node qualification timelines.*

**EDA software and chip IP are an underappreciated second toll road.** Cadence and Synopsys together account for over 60% of the global EDA market and 70% of the IP market. Every AI accelerator designed — whether by NVDA, AMD, or a hyperscaler building custom silicon — requires their software. ARM licenses the architecture underlying virtually every custom AI chip being built by hyperscalers to reduce NVDA dependency, making it a royalty on the custom silicon trend itself. These share the same oligopoly moat characteristics as the capital equipment layer. *Watch: ARM architecture adoption rate in hyperscaler custom silicon programs; Cadence/Synopsys revenue growth as a leading indicator of chip design activity volume.*

**Export controls insulate incumbents while capping China TAM.** US and Dutch restrictions limit equipment sales to China, constraining revenue but also protecting incumbents from Chinese competition in unrestricted markets. Net effect is mildly positive for moat durability — the ceiling is known and priced; the insulation is structural.

### Recent Developments

* **TSMC CapEx at High End of Guidance (April 2026):** TSMC confirmed 2026 CapEx will hit the high end of its $52–56B range, focused heavily on AI and HPC. Provides exact quantitative backing for the multi-year equipment order book thesis — capital flow from Layer 3 to Layer 2 remains at peak levels.
* **ASML-Mistral Strategic Partnership (September 2025):** ASML invested $1.5B (11%) in Mistral AI — a direct investment at the other end of the supply chain, signaling equipment makers are taking positions in the application layer as vertical integration accelerates across the stack.
* **N2/A16 Node Buildout Driving Multi-Year Order Books (2025–2026):** TSMC CapEx exceeded its prior peak in 2025 for the first time, generating multi-year equipment order visibility. N2/A16 qualification timelines are the primary gating factor for the next equipment upgrade cycle.
* **Applied Materials and Besi Hybrid Bonding System — HBM4 Production Equipment (2026):** Applied Materials and Besi jointly developed a hybrid bonding inline system recently ordered by SK Hynix (~$15M / KRW 20B) — SK Hynix's first hybrid bonding equipment purchase intended for mass production. The system combines Applied Materials' CMP and plasma processing tools with Besi's hybrid bonder. Samsung has also adopted Besi equipment for development-stage hybrid bonding. Hybrid bonding production adoption is expected at HBM4 (gradual introduction H2 2026 into 2027). This is a named equipment revenue event tied directly to next-generation HBM packaging — a new, incremental demand vector for both companies. See also Layer 5.

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| ASML | ASML Holding | Monopoly on EUV lithography — the single most irreplaceable tool in advanced chip manufacturing |
| AMAT | Applied Materials | Broadest equipment portfolio across deposition, etch, and inspection; most diversified revenue across node types |
| LRCX | Lam Research | Dominant in etch and deposition; high leverage to memory CapEx cycles (HBM buildout) |
| KLAC | KLA Corporation | Near-monopoly in process control and metrology; high-margin service revenue makes it the most defensive equipment play |
| CDNS | Cadence Design Systems | EDA software duopolist; required for every advanced chip design; AI chip design activity boom is a direct revenue driver |
| SNPS | Synopsys | EDA software duopolist alongside Cadence; silicon IP portfolio; merger with Ansys expands simulation moat |
| ARM | Arm Holdings | Architecture royalty on every Arm-based chip shipped — including hyperscaler custom silicon built to reduce NVDA dependency; also listed under Layer 4 |
| BESI | Besi (BE Semiconductor Industries) | Hybrid bonding equipment for advanced packaging — SK Hynix and Samsung are customers; HBM4 production ramp is the primary near-term revenue event; listed on Euronext Amsterdam |

---

## 3. Foundries & Advanced Packaging

*Profile: Extremely capital-intensive; TSMC holds a structural moat at leading nodes; geographic concentration in Taiwan is the primary systemic risk; advanced packaging is a separate and increasingly critical sub-layer.*

Wafer fabrication and chip assembly — the physical manufacturing layer and the source of the most acute hardware constraint in the current stack. TSMC N3 utilization is on track to exceed 100% in H2 2026, with every major AI accelerator converged on the same node simultaneously.

### Persistent Themes

**TSMC's N3 monopoly on AI silicon is the single most acute constraint in the stack.** NVDA Rubin, AMD MI400, Google TPU v7/v8, AWS Trainium3, and Meta MTIA have all converged on N3 simultaneously. AI-related silicon is consuming approximately 60% of N3 wafer output in 2026, modeled to reach 86% by 2027 — nearly entirely squeezing out smartphone and CPU wafers. TSMC cannot expand cleanroom space fast enough; their CapEx only exceeded its prior peak in 2025, and they were caught flat-footed by the pace of AI demand. This gives TSMC exceptional pricing power — N3 margins are projected to exceed the corporate average in H2 2026. *Watch: TSMC N3 utilization disclosures; capacity commentary at earnings.*

**Advanced packaging is becoming a distinct, high-value sub-layer.** CoWoS and SoIC packaging are no longer commodity back-end services — they are performance-critical steps that TSMC is increasingly internalizing. OSAT companies (AMKR, ASX) benefit from overflow as TSMC's internal capacity is insufficient to meet demand. CoWoS is being outsourced to OSATs as N3 wafer availability becomes the dominant bottleneck; CoPoS is the next-generation architecture targeting mass production 2028–2029. *Watch: CoWoS capacity allocation announcements; CoPoS pilot line progress; TSMC OSAT outsourcing volumes.*

**Packaging materials are the next hidden bottleneck below the wafer layer.** Advanced packaging complexity is driving demand for specialty materials — glass fiber cloth, high-grade CCL laminates, and glass substrates — that have single-source or near-monopoly suppliers with multi-year capacity lead times. Nittobo's glass fiber cloth monopoly (no new capacity until mid-2027) and the organic-to-glass substrate transition are both maturing simultaneously with the Nvidia Rubin generation ramp. These are not silicon constraints — they sit one layer below, in the materials and PCB supply chain — and are almost entirely absent from mainstream investment analysis. *Watch: Nittobo capacity announcements; Intel glass substrate mass production timeline; CCL pricing trends as a leading indicator.*

**TSMC is deliberately not pricing to scarcity — leaving value on the table to protect ecosystem stability.** Despite running N3 utilization above 100% in H2 2026, TSMC has not meaningfully raised wafer prices to reflect the extreme scarcity. The decision is deliberate: TSMC is prioritizing long-term customer relationships over near-term margin extraction. This means TSMC's reported pricing power understates its actual ability to extract value — and any shift toward value-based pricing (which TSMC could execute unilaterally given its monopoly position) would be immediately accretive. *Watch: TSMC pricing commentary at earnings as the signal of any philosophy shift.*

**Foundry diversification is a structural theme, not a near-term reality.** Intel 18A and Samsung 2nm are the only credible N3 alternatives. Intel yields remain below 50%; Samsung 2nm yields are stuck in the mid-50% range against TSMC's reported 80–90% at the same node. Government subsidies (CHIPS Act, EU Chips Act) are accelerating domestic fab buildout but commercially viable alternatives are a 2027+ story at best. *Watch: Intel 18A yield disclosures — any improvement is a high-signal event for the diversification thesis.*

### Recent Developments

* **TSMC Q2 2026 Guidance: Pricing Power and N2 Ramp (April 2026):** TSMC guided Q2 2026 revenue to $39.0–40.2B (+32% YoY, +10% QoQ) with gross margins of 65.5–67.5%. N3 margins are projected to exceed the corporate average in H2 2026 — concrete financial proof of extreme pricing power amid the shortage. The N2 ramp beginning H2 2026 will dilute full-year gross margins by 2–3%, as will overseas fab expansion — quantifying the steep cost of geographic diversification.
* **TSMC CoWoS Expansion & CoPoS Roadmap (April 2026):** TSMC is targeting 115,000–140,000 CoWoS wafers per month by end of 2026, rising to ~170,000 by 2027. The CoPoS pilot line is confirmed for June 2026, with mass production targeted 2028–2029. CoPoS is architecturally necessary to overcome traditional packaging size limits for increasingly massive AI ASICs and GPUs.
* **TSMC CoWoS Financial Profile and Technology Roadmap (2026–2029):** CoWoS ASP is approximately $10,000 per wafer — on par with a 7nm advanced logic node — with current advanced packaging margins below TSMC's overall average but projected to reach comparable gross margin levels as volumes scale. Advanced packaging contributed approximately 10% to TSMC's 2025 revenue, a share expected to continue rising. Capacity projections: 1.3 million CoWoS units in 2026, rising to 2 million in 2027 (overall advanced packaging capacity +80% from 2022 to 2027). Technology roadmap: TSMC currently produces 5.5-reticle CoWoS and plans 14-reticle CoWoS by 2028, enabling approximately 10 compute dies and 20 HBM stacks per package. SoIC A14-on-A14 targeted for production in 2029, delivering 1.8x higher die-to-die I/O density vs. N2-on-N2 SoIC. TSMC has reduced SoIC deployment timelines by up to 75%. Advanced packaging facility in Arizona targeted for 2029 to serve North American CSPs.
* **Industry N3 Convergence (2026):** Every major AI accelerator platform converged on TSMC N3 simultaneously — NVIDIA (Rubin on 3NP), AMD (MI350X/MI400 on N3), Google (TPU v7 on N3E, TPU v8 on N3), AWS (Trainium3 on N3P), Meta (MTIA on N3). The structural driver of the N3 capacity squeeze.
* **TSMC 3nm and 2nm Capacity Expansion (2026–2028):** TSMC is breaking its historical practice of halting capacity additions once a process reaches target output — AI demand has forced a reset. 3nm monthly output: 120,000–130,000 wafers at end of 2025; revised target 180,000 wafers/month by end of 2026 — approximately 40% year-on-year growth and 20% above original estimates. Incremental 3nm sources: new Southern Taiwan Science Park fab (mass production H1 2027), Arizona second fab (3nm, H2 2027), Kumamoto Japan second fab (3nm, 2028). 2nm ramp: from 30,000–40,000 wafers/month at end of 2025 to approximately 100,000 wafers/month by end of 2026 — a 1.4x–2.1x increase in a single year — with strong yield performance across Hsinchu and Kaohsiung fabs from the start of mass production in late 2025. N2P and A16 follow on the roadmap. Even with 3nm output exceeding original targets, available capacity remains insufficient to meet demand.
* **Samsung 2nm Yield Gap vs. TSMC (April 2026):** Samsung 2nm yields are stuck in the mid-50% range; TSMC has reportedly reached 80–90% at the same node. Samsung's Taylor, Texas fab is past 90% mass production readiness targeting H2 2026 ramp for Tesla AI5/AI6, but the yield gap confirms TSMC's frontier monopoly remains intact. Qualcomm selected TSMC N2P for its next-generation Snapdragon.
* **Tesla-Intel "Terafab" Initiative (April 2026):** Tesla is partnering with Intel to build its own wafer fab targeting silicon chip production around 2029. Tesla has initiated direct outreach to AMAT, LRCX, and Tokyo Electron for equipment. The most extreme extension of the custom silicon thesis — an AI end-user attempting to internalize physical manufacturing. TSMC's response noting 3–5 year build-to-ramp cycles highlights the structural timeline constraints on breaking foundry monopolies. See also Layer 2.
* **Intel EMIB-T & TSMC US Packaging Acceleration (2026–2028):** Intel in active discussions with Google and Amazon to provide EMIB-T advanced packaging for their ASIC programs; commitments targeted for H2 2026 with customers reportedly willing to prepay in the billions. Intel CFO highlighted advanced packaging as the "more interesting part" of Foundry with ~40% gross margin potential. TSMC accelerating its US advanced packaging facility — construction beginning Q2 2026, one quarter ahead of schedule, targeting operations late 2027–2028.
* **Broadcom-Google Long-Term Agreement (2026–2031):** Broadcom entered a long-term agreement with Google to develop and supply future generations of custom AI chips and rack components through 2031. See also Layer 6.
* **Glass Fiber Cloth Bottleneck — Nittobo Monopoly (2026–2027):** Glass fiber cloth is a critical raw material for Copper Clad Laminates (CCL), the primary component of Printed Circuit Boards underlying every AI server. CCL cost breakdown: copper foil ~42%, resin ~26%, glass fiber cloth ~19%. Nittobo (Tokyo Stock Exchange) holds approximately 90% global market share in T-glass and 60–70% in NER-glass — a near-total monopoly on this input. Nittobo has no new capacity coming online until mid-2027 at the earliest, meaning the bottleneck cannot be relieved before then regardless of demand. Nvidia's Rubin generation is driving a step-change in demand: higher layer count, larger substrate area, cableless backplane/midplane designs, and the new Rubin LPX inference rack all increase glass fiber cloth consumption per system. This is a hidden single-point-of-failure in the AI server supply chain that has received almost no investment attention. *Research priority: Nittobo investability and any non-Nittobo glass fiber cloth producers.*
* **Glass Substrate Breakthrough — Intel as Early Mover (2026):** Traditional organic substrates are reaching physical limits as AI chip package sizes grow — warpage under high temperatures directly reduces manufacturing yield. Two glass-based solutions are emerging: Glass Core Substrate (replaces the core layer of the substrate with glass) and Glass Interposer (replaces the silicon interposer with glass), offering superior thermal and mechanical properties. Intel committed to glass substrates in its advanced packaging roadmap in 2023 and debuted its first sample combining EMIB packaging with a glass core substrate in January 2026. A recent "No SeWaRe" qualification result for Intel signals mass production is moving closer. Glass substrate suppliers are a research priority — Corning (GLW, already in Layer 7 for fiber optics) has glass expertise that is directly applicable to this product category and warrants investigation as a potential cross-layer supply chain position.
* **Intel Q1 2026 Earnings — Foundry Turn (Q1 2026):** Intel foundry revenue $5.4B (+16% YoY); external foundry revenue $174M. Yields improving 7%+ per month, already hitting year-end targets ahead of schedule — the fastest yield improvement rate Intel has disclosed. Google committed to multiyear Intel CPU deployments and is co-developing a custom IPU. Tesla confirmed 14A process for the $20B TeraFab Austin project. Net foundry loss $2.4B (improved $72M quarter-over-quarter) — losses remain significant but the trajectory has changed materially. Intel repurchased a 49% stake in Ireland Fab 34 for $14.2B to regain direct capacity control. See also Layer 4.
* **Intel Foundry Customer Pipeline Expansion (2026):** Apple is reportedly evaluating Intel's 18A-P node for its M-series chips, with potential products as early as 2027 (unconfirmed — described as Apple "weighing" and "evaluating"). Google is exploring Intel's EMIB (Embedded Multi-die Interconnect Bridge) advanced packaging technology for its TPU v8e. Tesla CEO Musk confirmed Tesla will adopt the 14A node for chips used in the TeraFab Austin complex — the first named 14A customer. If Apple commits, it would be the highest-profile external foundry customer Intel has ever disclosed. *Flag: Apple and Google angles are exploratory, not confirmed orders.*

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| TSM | Taiwan Semiconductor | Irreplaceable foundry moat at leading nodes; only manufacturer capable of producing the world's most advanced AI silicon at scale; pricing power intensifying with N3 scarcity |
| AMKR | Amkor Technology | Leading OSAT; direct beneficiary of CoWoS packaging overflow and geographic diversification demand |
| ASX | ASE Technology | Largest OSAT globally; direct beneficiary of advanced packaging capacity outsourcing from TSMC |
| SSNLF | Samsung Electronics | Foundry #2; gaining AI supply chain share (Tesla AI5/AI6) but yield gap vs. TSMC limits leading-edge competitiveness |
| INTC | Intel | Foundry yields improving 7%+/month — trajectory has changed; EMIB-T advanced packaging and 14A (Tesla TeraFab) are near-term anchors; Google + Tesla customer commitments validate the thesis; 18A mass production still a 2027+ story |

---

## 4. Compute Silicon

*Profile: Highest direct leverage to AI demand; NVDA has exceptional near-term pricing power but faces long-term customer defection risk; AMD is the primary alternative; ARM captures royalties across the custom silicon trend.*

The chips that run AI workloads — GPUs for training and inference, CPUs for orchestration, and the custom ASICs hyperscalers are building to reduce NVDA dependency. GPU compute is effectively sold out through August–September 2026. H100 spot pricing has rebounded approximately 40% from its October 2025 trough to $2.35/hr. CPU compute is simultaneously constrained: the agentic AI ratio shift from 1:8 to 1:1–1:2 CPU:GPU is driving server CPU prices up 10–20% and extending lead times from 1–2 weeks to 8–12 weeks — a shortage dynamic that did not exist in prior AI CapEx cycles.

### Persistent Themes

**NVDA's CUDA ecosystem is the dominant moat — and the primary long-term risk.** Nvidia's GPU dominance is reinforced by CUDA, which has become the industry standard programming environment for AI. Developer lock-in via years of CUDA-native code makes switching costly. Nvidia has also made strategic acquisitions to bolster its position — the 2019 Mellanox acquisition provides the architecture to connect GPUs in a network, allowing Nvidia's systems to function more efficiently than competitors. The primary long-term risk is hyperscalers deepening custom silicon programs to escape NVDA dependency — ASICs are forecast at 27.8% of AI server shipments in 2026, rising to ~40% by 2030. *Watch: ASIC share of AI server shipments as the pace indicator; GPU spot pricing as the real-time demand barometer.*

**The agentic shift is restructuring chip demand architecture.** Agentic AI is driving a structural surge in CPU core demand — from approximately 30M cores/GW to 120M cores/GW — shifting system architectures from 1:8 CPU:GPU ratios toward 1:1 or 1:2 as orchestration (task planning, tool calling) becomes the primary bottleneck, accounting for over 90% of total inference latency. This bifurcates the market: training workloads retain best price-performance on H100s (keeping Hopper demand sticky), while large MoE inference workloads run best on latest large-scale systems. *Watch: CPU:GPU ratio trends in hyperscaler procurement.*

**The inference shift is creating demand for efficiency-optimized silicon.** Hardware demand is shifting from pure training toward inference. Inference prioritizes cost per token and latency over raw throughput — favoring chips optimized for efficiency, including custom ASICs and ARM-based designs. AWS expects Trainium to save tens of billions in CapEx per year and deliver several hundred basis points of operating margin advantage for inference — making custom silicon a margin imperative, not just a supply hedge. *Watch: inference vs. training revenue mix in hyperscaler disclosures.*

**ARM is a royalty on the custom silicon trend itself.** Every hyperscaler custom chip built on ARM architecture — Graviton, Trainium, Cobalt — generates a royalty for ARM. ARM CPUs already account for approximately 40% of the cloud data center market with over 1 billion deployed Neoverse cores. ARM is transitioning from pure IP licensing to direct silicon production (AGI CPU), adding a second growth vector while simultaneously supplying the architecture underlying its licensees' custom chips. *Watch: ARM architecture adoption rate in hyperscaler custom silicon; AGI CPU customer announcements.*

### Recent Developments

* **Used H200 Systems Appreciating in Value (April 2026):** In the Chinese market, a used H200 system purchased for RMB 2.45M in February 2025 is now valued at RMB 3M after more than a year of operation — a 20%+ appreciation. Compute hardware typically depreciates rapidly; appreciation on used one-year-old servers is the ultimate proof of a severe, unyielding supply constraint that overrides normal hardware economics.
* **GPU Spot Pricing: Supply Exhaustion (Q1–Q2 2026):** H100 1-year rental contracts rose approximately 40% from $1.70/hr (October 2025 trough) to $2.35/hr (March 2026). On-demand capacity effectively sold out across all GPU types; p6-b200 spot instances on AWS trading at $14/hr. Blackwell lead times extend to June–July 2026; all capacity through August–September committed. Existing H100 contracts being renewed at original rates for 4-year extensions through 2028. Two large AWS customers independently asked to purchase every Graviton instance available in 2026 — AWS declined. GB300 NVL72 delivers approximately 17x higher throughput than an optimized H100 in FP8, and 32x higher in FP4 (which Hopper lacks entirely) — Blackwell generates roughly 30x more tokens per second than Hopper on frontier workloads.
* **Nvidia Pricing Gap and Software Optimization Leverage (2026):** SemiAnalysis identifies a massive gap between Nvidia's cost-based pricing floor and the value-based pricing ceiling for Vera Rubin NVL72: the minimum rental price required for neoclouds to hit a 15% IRR is $4.92/hr/GPU; the maximum a customer would pay at parity with GB300 cost-per-FLOP is $12.25/hr/GPU. A hypothetical 40% server price hike by Nvidia would still deliver below-trend cost improvements for end users while enabling neoclouds to charge $8.00/hr and earn a 38% IRR — implying Nvidia has substantial untapped pricing power it has not yet exercised. Separately, software-only optimizations (wideEP, disaggregation, MTP) can take a B300 running DeepSeek from ~1,000 tokens/sec/GPU to ~14,000 tokens/sec/GPU — a 14x throughput increase from software alone, illustrating that the value of the hardware platform compounds with software investment independently of new chip generations.
* **Nvidia Networking Price Discrimination (2026):** Nvidia charges neoclouds a 94% premium on networking switches vs. hyperscalers (who use custom ODM/OEM solutions). However, this 94% networking premium translates to only a ~10% increase in the all-in capital cost of a 72-GPU rack-scale server — meaning neoclouds absorb a structurally higher networking cost that is large in percentage terms but manageable in absolute TCO terms.
* **Nvidia Vera Standalone Launch (2026):** Nvidia decoupled the Vera CPU (Olympus architecture) for standalone sales to capture the structural demand surge in agentic server configurations. Early partners include Alibaba, Cloudflare, CoreWeave, and Nscale. Specs: 88 cores/176 threads, TSMC N3, CoWoS-R packaging, 1.8 TB/s NVLink-C2C interconnect for memory sharing with GPUs. A full Vera CPU Rack houses 256 CPUs (22,528 cores / 45,056 threads / 400 TB of memory).
* **Arm AGI CPU Launch and Verda First Deployment (2026):** Arm's historic pivot from IP licensing to direct silicon — a 136-core Neoverse V3 CPU built on TSMC 3nm, co-designed with Meta as inaugural customer; OpenAI, Cerebras, Cloudflare, SK Telecom, SAP, F5, Positron, and Rebellions also adopting. Air-cooled rack: 30 blades, 8,160 cores, 36kW. Liquid-cooled rack: 336 AGI CPUs, 45,000+ cores, 200kW — a 5.6x core density advantage over air-cooled. Verda (formerly DataCrunch, $117M raised, data centers in Finland and Iceland on 100% renewable energy) is the first neocloud deploying Arm AGI CPUs alongside Nvidia GB300 and VR200 racks. Arm and Nvidia have collaborated on server specifications to allow AI agents to autonomously assign workloads across both Arm AGI CPUs and Nvidia GPUs within the same cluster — a cross-vendor workload orchestration capability relevant to the agentic CPU demand story.
* **AMD-Meta Structural Partnership (2026):** AMD and Meta struck a $100B, 6GW chip deal — a major anchor for the hyperscaler CapEx cycle and validation of AMD as a primary NVDA alternative. AMD's EPYC Venice (Zen 6 architecture, TSMC N2, CoWoS-L + SoIC) delivers 256 cores / 512 threads — the highest thread count of any server CPU currently available — positioning AMD to capture disproportionate share of the agentic CPU demand surge.
* **Intel 18A Yield Issues (April 2026):** Yields below 50% on Intel 18A threatening mass production timelines — a competitive opening for AMD's TSMC-based EPYC Venice. See also Layer 3.
* **OEM Repricing Loop (2026):** OEMs repriced AI servers beyond underlying component cost increases → compressed project returns → slow-rolled deployments → supply withheld from rental market → rental market tightened further. A self-reinforcing supply-withholding dynamic and leading indicator of continued market tightness.
* **CPU Price Surge and Lead Time Extension (Q1–Q2 2026):** Server CPU prices rose 10–20% since March 2026; consumer CPU prices 5–10%. Lead times extended from 1–2 weeks to 8–12 weeks. AMD is planning two consecutive price increase rounds (Q2 + Q3) totaling a cumulative 16–17%; Intel implemented server CPU price adjustments April 1 and is expected to implement a further 8–10% round in H2. TSMC is breaking its historical practice of halting N3 capacity additions at target levels — expanding further to serve the simultaneous surge in both CPU and AI ASIC demand at the same node. Intel and Tesla leadership share a unified view that the entire global semiconductor supply chain has failed to keep pace with the acceleration in demand. Intel CEO Lip-Bu Tan: the CPU:GPU ratio "used to be 1 to 8, is now 1 to 4, and for agentic and multi-agent workloads it is moving towards parity or even better." Intel CFO David Zinsner: training workloads run at roughly 7–8 GPUs per CPU; inference compresses that to 3–4:1. Google SVP Amin Vahdat: "CPUs are not replacing specialized accelerators — they are orchestrating them." TSMC note: currently cannot distinguish AI data center CPU orders from PC/desktop CPU orders, and therefore excludes CPUs from AI revenue classifications — meaning TSMC's reported AI revenue materially understates the AI-driven demand hitting its fabs. Intel Q1 2026 10-Q confirms the pricing story from the bottom up: data center segment revenue up with a 27% ASP increase while Intel actually shipped 5% fewer server CPUs — pure pricing power without volume growth. Demand exceeded supply sufficiently that Intel is now monetizing edge-bin dies (previously scrapped for failing high-end specs), reclassified as lower-tier SKUs and sold at reduced prices rather than discarded.
* **Meta Graviton5 CPU Land Grab (Q2 2026):** Meta is purchasing tens of millions of AWS Graviton5 cores in a deal that goes beyond silicon — AWS is hosting the full stack including power, networking, and data center infrastructure. Graviton5 specs: 192 Arm Neoverse V3 cores, TSMC 3nm, DDR5-8800, PCIe Gen6, 600MB total cache (2MB L2/core + 192MB L3). Meta is also a launch customer for the Arm AGI CPU. The fact that an operator at Meta's scale — with deep experience running custom infrastructure — is locking in external cloud CPU capacity confirms the agentic CPU shortage is acute enough to override hyperscaler self-sufficiency instincts.
* **Intel Q1 2026 Earnings (Q1 2026):** Intel data center revenue $5.1B (+22% YoY), $1.5B operating profit. ASIC segment ~$1B in revenue, doubled YoY and +30% QoQ — Intel's ASIC business is now material. Foundry revenue $5.4B (+16% YoY); yields improving 7%+ per month, already hitting year-end targets ahead of schedule. Google committed to multiyear Intel CPU deployments and is collaborating on a custom Infrastructure Processing Unit (IPU). Tesla confirmed the 14A process for the $20B TeraFab project in Austin. Net loss $4.28B ($2.4B from foundry). Intel repurchased a 49% stake in Ireland Fab 34 for $14.2B to regain capacity control. See also Layer 3.
* **Google-Nvidia Virgo Network and Vera Rubin Scale (2026):** Google's new Virgo Networking fabric enables the Vera Rubin A5X instance to scale to 960,000 GPUs across multiple sites — the largest single-fabric GPU deployment architecture announced. Google has quietly deployed well over 1 million Nvidia GPUs across its global fleet for internal products and cloud services. Nvidia Omniverse and Isaac Sim are now available on the Google Cloud Marketplace, extending the Nvidia simulation platform into Google's physical AI developer ecosystem. See also Layer 10.

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| NVDA | Nvidia | Dominant GPU+software (CUDA) ecosystem; highest leverage to AI CapEx cycle; primary risk is custom silicon displacement over a 3–5 year horizon |
| AMD | Advanced Micro Devices | Primary GPU alternative to NVDA; $100B AMD-Meta deal validates multi-year hyperscaler CapEx share; MI-series ramp is the key execution test |
| ARM | Arm Holdings | Royalty on every Arm-architecture chip shipped — including hyperscaler custom silicon built to reduce NVDA dependency; transitioning to direct silicon (AGI CPU); also listed under Layer 2 |
| INTC | Intel | Data center CPU revenue +22% YoY; ASIC segment doubled YoY to ~$1B; foundry yields improving 7%+/month; Google + Tesla customer anchors validate turnaround; net losses remain large but trajectory improving |
| NXPI | NXP Semiconductors | Data center revenue ~$200M in FY2025, guiding "$500M+" by end of 2026; positioned in system cooling, power supply, board management, and control plane switching for AI servers; Q1 2026 revenue $3.18B (+12% YoY), Q2 guide $3.45B (+18% YoY) |

---

## 5. Memory Silicon

*Profile: Cyclical but with a structural floor from HBM demand; HBM is high-margin and capacity-constrained with LTA pricing; three-player oligopoly with SK Hynix holding the technology lead.*

The memory that feeds AI workloads — HBM for accelerator bandwidth, DRAM for servers, NAND for storage. Q2 2026 contract pricing forecast at +60% DRAM and +70% NAND quarter-on-quarter. LTA structuralization is changing the investment characteristics of the layer.

### Persistent Themes

**HBM is the highest-conviction structural theme in memory.** High Bandwidth Memory is not a commodity — it is a performance-critical, capacity-constrained component with differentiated technology and LTA pricing. HBM absorbs approximately 3x more DRAM wafer capacity per bit than commodity DRAM — widening to approximately 4x with HBM4. HBM content per accelerator is growing rapidly: Rubin Ultra carries approximately 4x more HBM than Blackwell; TPU v8AX and Trainium3 migrating from 8-Hi to 12-Hi stacks. Every AI accelerator generation requires more HBM; the demand floor is structural. SK Hynix holds the technology lead as the primary HBM3E supplier to NVDA and Google. *Watch: HBM wafer allocation disclosures; HBM4 qualification timelines at NVDA; SK Hynix HBM yield commentary.*

**Heterogeneous memory architecture is replacing one-size-fits-all DDR5.** The "one-size-fits-all" DDR5 model is giving way to a hierarchy tuned for specific workload phases: SRAM (ultra-fast, low-capacity, decode) → HBM (high bandwidth, prefill) → LPDDR5X (low-power, moving from mobile to servers) → DDR5 (general-purpose). In power- and cooling-constrained environments, memory has become an active design variable rather than a fixed component. This creates a multi-tier opportunity set across the memory supplier landscape. *Watch: LPDDR5X and LPDDR6 server adoption rates; SOCAMM production announcements.*

**LTA structuralization is reducing cyclicality for the best-positioned suppliers.** The memory market is shifting from quarterly contracts to 3–5 year Long-Term Agreements. Custom AI silicon locks in memory specs and volumes at the design stage, making early multi-year procurement commitments structurally necessary. LTAs are reserved for major CSPs — not offered broadly — reducing supplier cyclicality, improving CapEx visibility, and keeping long-term capacity committed to Big Tech. *Watch: LTA deal announcements and pricing terms; downside price floors as indicators of contract structure.*

**HBM crowdout is creating second-order supply gaps in commodity memory.** As major suppliers accelerate toward HBM and DDR5, they are exiting niche markets (2D NAND, SLC NAND, niche DRAM), creating supply gaps being filled by smaller, lower-tier players. AI infrastructure demand is also actively cannibalizing the broader semiconductor supply chain — LPDDR4 RAM prices rising seven-fold is a concrete example of AI CapEx pressuring non-AI consumer tech components. *Watch: niche memory price trends; consumer tech component price spikes as a crowdout signal.*

### Recent Developments

* **LPDDR6 Commercial Rollout for Edge AI (April 2026):** Tesla's AI6 and AI6.5 chips will adopt LPDDR6 memory, with commercial rollout expected H2 2026. LPDDR6 delivers 10.6–14.4 Gbps bandwidth — approximately 1.5x higher than LPDDR5X. Samsung is joining SK Hynix in this supply chain starting with AI6. The memory upgrade cycle extends beyond data center HBM into edge AI, opening a distinct high-bandwidth TAM and giving Samsung a meaningful foothold while it struggles with HBM yields.
* **DRAM/NAND Contract Pricing Inflection (Q1–Q2 2026):** LPDDR5X and DDR5 contract prices tracking approximately 4–5x year-on-year increases. Q1 2026 actuals per TrendForce: DRAM contract prices +83% QoQ; NAND +160% QoQ. Q2 2026 forward projections: DRAM +58–63% QoQ, NAND +70–75% QoQ. Omdia raised its full-year 2026 semiconductor forecast to +62.7%; the DRAM market is forecast to nearly double in value and NAND could quadruple vs. 2025; computing and data storage alone projected to exceed $700B, +90% YoY. Meaningful supply relief is unlikely before well into 2027.
* **HBM4 Strategy Divergence (2026):** Samsung chasing 80% yields on 1c-based HBM4 using a performance-first SF4 logic base die. SK Hynix trimmed HBM4 shipments by 30% due to Rubin delays, redirecting capacity to HBM3E — a near-term tactical adjustment, not a strategic retreat. ISSCC 2026 confirmed Samsung's front-end 1c node yields at approximately 50% — a direct risk to HBM4 profit margins alongside the performance gap vs. SK Hynix. SK Hynix is adopting TSMC's N12 logic process for its HBM4 base die; Micron is pursuing a lower-cost internal CMOS approach, explicitly differentiating on cost rather than performance at the base die layer.
* **DDR5 Margin Flip (2026):** Micron reported non-HBM (DDR5) margins now exceeding HBM profitability, projecting 81% gross margin in Q3 FY26 as HBM3E oversupply and Rubin delays temporarily shift pricing power to commodity DRAM.
* **Memory LTA Deals Accelerating (H1 2026):** Micron secured its first 5-year strategic customer agreement (March 2026) and is in active discussions with multiple clients. Samsung adopted a strict 3-year minimum LTA policy for all new contracts, with late-stage negotiations with AMD, Microsoft, and Google. SK Hynix pursuing a 5–7 year LTA with Google for commodity DRAM and a 3-year DDR5 LTA with Microsoft valued at "tens of trillions of won." Deals include downside price floors and 10–30% upfront prepays.
* **SK Hynix Q1 2026 Record Earnings (Q1 2026):** SK Hynix posted its fourth consecutive record quarter: KRW 52.5T in revenue (first quarter ever exceeding KRW 50T), KRW 37.6T in operating profit (5x year-over-year), and a 72% operating margin — outpacing Micron at 67.6% and TSMC at 58%. DRAM accounted for 78% of revenue; NAND 21%. HBM customer demand over the next three years already exceeds available supply capacity; SK Hynix explicitly stated it cannot accommodate all customer requests. The company is transitioning to an LTA-only model (3–5 year agreements) with major tech customers including Microsoft and Google, abandoning traditional short-term contracts entirely.

* **SSD Retail Price Surge (Q1–Q2 2026):** Samsung and Kingston issued notices raising SSD prices 10%+ across their lineups; Samsung and Western Digital separately raised high-end M.2 SSD prices by up to 2x within the same month. A 1TB SSD now retails for $300–330, up from under $100 a year ago — a 3–4x increase; 8TB SSDs are selling above $4,000. Counterfeit Samsung 990 Pro drives are surfacing in retail channels — a concrete signal that the shortage premium has made counterfeiting economically viable.

* **ISSCC 2026 — Memory Technology Disclosures (April 2026):** Samsung demonstrated a 12-high HBM4 stack delivering 3.3 TB/s at 13 Gb/s per pin (vs. JEDEC's 6.4 Gb/s baseline) with 2048 IO pins. SK Hynix demonstrated 1c LPDDR6 at 14.4 Gb/s and GDDR7 at 48 Gb/s. SanDisk/Kioxia achieved record NAND density with their 332-layer BiCS10 at 37.6 Gb/mm² in QLC configuration.
* **SK Hynix Hybrid Bonding Validation and Equipment Order (2026):** SK Hynix completed validation of 12-high HBM using hybrid bonding and ordered a joint Applied Materials/Besi hybrid bonding inline system (~KRW 20 billion / approximately $15M) — the first hybrid bonding equipment order by SK Hynix intended for mass production. Samsung has also adopted Besi equipment for development-stage work, while testing additional hybrid bonders from SEMES (noted as less mature). Hybrid bonding adoption is expected to begin at scale with HBM4, with gradual introduction H2 2026 into 2027 as 16-high stacks are commercialized. SK Hynix will continue advancing its existing MR-MUF technology to bridge near-term demand while hybrid bonding economics and yields mature — the company has already secured the capability to meet height standards for up to 16-high stacks using MR-MUF. See also Layer 2 for the equipment vendor impact.

* **SOCAMM Adoption and Pricing (2026):** Emergence of SOCAMM for LPDDR5X in servers — bridging high efficiency with serviceability to enable LPDDR5X's transition from mobile to production server environments without the "soldered" maintenance penalty. Nvidia's Vera Rubin NVL72 utilizes SOCAMM as its primary memory architecture, establishing SOCAMM as a production-grade standard rather than an emerging alternative. Estimated Q1 2026 SOCAMM contract pricing is approximately $8/GB, with projections of over $13/GB by end of 2026 as Vera Rubin demand scales — a 60%+ price increase within a single year on a product entering mass deployment. DRAM fabs are already running above 90% utilization; overall memory prices are up approximately 6x in the past year. If SOCAMM achieves production traction at scale, it opens a significant new addressable market and creates structural disruption risk for legacy DDR5 server memory configurations.

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| MU | Micron Technology | Only US-headquartered memory supplier; HBM3E ramp and DDR5 margin expansion are near-term catalysts; LTA deals reducing cyclicality |
| HXSCL | SK Hynix | HBM technology leader (primary HBM3E supplier to NVDA/Google); highest leverage to HBM demand cycle |
| SSNLF | Samsung Electronics | Memory #1 by volume but lagging SK Hynix on HBM yields; LPDDR6 edge AI supply chain entry is the near-term recovery foothold |

---

## 6. Networking & Custom Silicon

*Profile: Design-win driven with long lead times; less directly cyclical than GPU/memory; structural growth tied to both cluster scale-up and custom silicon adoption; Broadcom and Marvell are the primary ASIC suppliers.*

Merchant networking chips, SmartNICs, and custom ASICs — the silicon that moves data within and between AI clusters, and the chip design layer hyperscalers contract to reduce NVDA dependency. ASIC share of AI server shipments is forecast at 27.8% in 2026, rising toward 40% by 2030.

### Persistent Themes

**Custom silicon is a megatrend compounding through Broadcom and Marvell.** Hyperscalers are deepening custom AI accelerator programs (TPUs, Trainium, custom inference chips) to reduce NVDA dependency and capture margin. AVGO's long-term Google agreement through 2031 illustrates the multi-year contracted nature of this revenue. Long design-to-revenue lead times create backlog visibility — current design wins translate into multi-year contracted revenue streams. Amazon's in-house silicon is already tracking $20B+ annual revenue; CEO Andy Jassy has confirmed exploring external rack sales with ~$50B run rate potential if pursued as a standalone business. *Watch: new hyperscaler custom silicon program announcements; ASIC market share trajectory; Broadcom-Google and Marvell design cycle timelines.*

**Networking fabric is becoming a primary cluster performance constraint.** As GPU cluster sizes grow, the interconnect fabric connecting accelerators becomes a bottleneck. Marvell and Broadcom supply the switch silicon and SerDes underlying both NVLink and Ethernet-based clusters. Nvidia's $6B investment sweep across Marvell, Coherent, and Lumentum is partly defensive — ensuring NVLink Fusion and CPO frameworks remain architecturally relevant even as hyperscalers build around NVDA silicon. *Watch: Nvidia NVLink Fusion adoption vs. Ethernet-based alternatives.*

### Recent Developments

* **Nvidia "Full Stack" Interconnect Strategy (2026):** Nvidia secured architectural control over the interconnect layer via $6B in strategic investments in Marvell, Coherent, and Lumentum — ensuring third-party custom chips remain dependent on Nvidia-defined NVLink Fusion and CPO frameworks.
* **Broadcom-Google Long-Term Agreement (2026–2031):** Broadcom entered a long-term agreement with Google to develop and supply future generations of custom AI chips and rack components through 2031. See also Layer 3.
* **Amazon Custom Silicon Revenue Scale (2026):** Amazon's in-house silicon tracking $20B+ annual revenue; Jassy confirmed exploring external rack sales with ~$50B run rate potential.
* **Extreme Networks Q3 FY2026 Earnings (Q3 2026):** Shares surged 28% on Q3 results: revenue $316.9M (+11% YoY), net income tripled to $10.6M, adjusted EPS $0.26 vs. $0.24 consensus. SaaS ARR $236.4M (+29% YoY, accelerating from 13% in Q3 2025 → 25% last quarter → 29% now) — software growing more than twice as fast as hardware revenue. Full-year guidance raised to $1.275B–$1.28B. Products: Extreme Platform ONE (launched July 2025, AI assistant for centralized switch/AP monitoring and configuration) and ExtremeCloud IQ (cloud-based network management with malicious wireless traffic detection). CEO confirmed memory supply constraints are "fully addressed" via targeted sourcing, product redesign, and strategic purchase commitments. The accelerating SaaS ARR growth rate confirms AI-driven network management adoption is in early-stage compounding.
* **ASIC Design Win Pipeline by Vendor (2026–2028):** The most complete public breakdown of which design houses are building which chips for which hyperscalers through 2028: Broadcom — TPU v7 (Ironwood), TPU v8ax (Sunfish); Marvell — Trainium 2, Maia 300 (Griffin), Maia 200 (Braga), A15; Alchip — Trainium 3, Trainium 4, TPU v8x (Zebrafish), TPU v9; Global Unichip Corp. (GUC) — Axion N4A, Cobalt 200; MediaTek — TPU v9, MTIA 300, MTIA 400, Titan v1 (Nexus), Titan v3, X1, Apple Baltra-Sotra, SoftBank Izanagi 1 and 2. Alchip and MediaTek are capturing significant hyperscaler ASIC design volume despite being underfollowed relative to Broadcom and Marvell. GUC is the primary designer for Google's and Microsoft's Arm-based CPUs.

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| AVGO | Broadcom | Primary custom ASIC supplier to hyperscalers (Google TPU, Meta); long-term contracted revenue through 2031; also dominant in networking switch silicon |
| MRVL | Marvell Technology | Custom ASIC and cloud networking silicon; AWS Trainium and Azure custom chip programs; Nvidia $6B investment adds strategic validation; three acquisitions in five months (XConn $540M PCIe/CXL, Celestial AI $3.25B optical interconnect, Polariton plasmonic circuits) extending the platform into optical connectivity |
| EXTR | Extreme Networks | AI-driven network management software and switches; SaaS ARR $236.4M (+29% YoY, accelerating); Extreme Platform ONE integrates AI assistant management across data center switches and wireless infrastructure |

---

## 7. Optical & Physical Connectivity

*Profile: Infrastructure lock-in via multi-year supply contracts; transceiver demand doubling in 2026; co-packaged optics (CPO) is a medium-term technology transition; fiber cable is an overlooked beneficiary.*

The physical layer connecting AI clusters — optical transceivers, networking switches, and fiber cables. Ethernet transceiver sales for AI clusters are forecast to double in 2026. Hyperscalers are signing 2–3 year guaranteed supply contracts, transforming cyclical hardware suppliers into high-margin, mission-critical utilities.

### Persistent Themes

**Transceiver demand is in shortage and supply contracts are locking in preferred suppliers.** AI cluster buildout requires high volumes of optical transceivers; demand is doubling in 2026. Multi-year guaranteed minimum contracts are locking in supplier revenue streams. Supplier concentration risk remains — a handful of hyperscaler customers hold significant leverage on contract terms — but the supply shortage is currently the more relevant dynamic. *Watch: hyperscaler transceiver contract announcements; supply constraint duration.*

**Co-packaged optics (CPO) is the medium-term technology transition to watch — and testing is the current bottleneck.** CPO moves optical components closer to the switch ASIC to reduce power and latency — a meaningful performance improvement for AI cluster economics. CPO could disrupt incumbent transceiver suppliers while creating new opportunities for vertically integrated players. Nvidia's CPO framework investments are partly about controlling this transition. The critical near-term constraint is not design but testing: a single Photonic Integrated Circuit (PIC) inspection currently takes over 100 seconds and relies on manual alignment (single-mode fiber core is 800x larger than an optical waveguide — nanometer-level precision is required). The industry lacks unified testing standards; TSMC's COUPE platform is entering volume production in 2026 but the absence of automated, high-throughput test equipment is the gating factor for mass production. Teradyne and Advantest are the dominant ATE vendors racing to solve this. *Watch: CPO qualification timelines at hyperscalers; automated PIC test throughput milestones; Nvidia CPO framework adoption.*

**The copper vs. optical debate has real TAM implications.** Copper interconnects remain a competing solution at shorter link distances. Hyperscaler preference between copper and optical at varying link lengths is an ongoing structural debate — resolution will materially affect the addressable market for optical transceiver suppliers. *Watch: hyperscaler preference shifts at different link lengths.*

**Fiber cable is the most overlooked beneficiary in the layer.** New AI data centers are increasingly sited in tier-two markets for power availability. Backhauling traffic requires dedicated fiber and wave buildouts along routes that previously had no infrastructure. Lumen has identified dozens of new data center clusters across the US requiring fiber, wave, and IP services and is actively building a specialized AI fabric. Corning dominates fiber cable manufacturing and is a direct, underfollowed beneficiary. Dark fiber buildout for multi-datacenter AI training factories adds a second demand vector distinct from general data center networking. *Watch: data center construction permits in secondary markets as a leading fiber demand indicator; dark fiber and wave buildout pace in non-traditional markets.*

### Recent Developments

* **Hyperscaler-Backed Fiber Expansion (April 2026):** Zayo announced an 8,000 route-mile (15 million fiber-mile) network expansion directly backed by a major AI infrastructure customer, connecting power-available secondary markets (Reno, Omaha, Columbus) to established hubs (Ashburn, Chicago). AI bandwidth demand is projected to grow 6x by 2030. Hyperscalers are now directly bankrolling US internet backbone expansion to connect power-constrained secondary markets — structurally validating dark fiber as a massive, distinct demand vector for GLW.
* **Optical Transceiver Sales Doubling (2026):** LightCounting forecasts Ethernet optical transceiver sales for AI clusters to double in 2026.
* **Fiber Optic Demand Surge (Q1 2026):** Fiber optic cables cited alongside GPUs, DRAM, and NAND as components experiencing price spikes — confirms the infrastructure buildout is pressuring the full networking supply chain.
* **Coherent-Lite Adoption (2026):** Emergence of O-band "Coherent-Lite" transceivers for 10–40km "Campus Reach" links, reducing power by 50% vs. traditional coherent optics.
* **Nvidia Full Stack Interconnect Investment (2026):** $6B strategic investment sweep across Marvell, Coherent, and Lumentum. See Layer 6 for full context.
* **Marvell Optical Acquisition Spree (Q4 2025–Q1 2026):** Marvell executed three acquisitions in five months to build an end-to-end optical connectivity platform: Celestial AI (optical interconnect startup, $3.25B base / up to $5.5B contingent on product milestones, closed Q4 2025); XConn Technologies (PCIe and CXL switching silicon, ~$540M, closed early 2026); Polariton Technologies (ETH Zurich spin-out, plasmonic circuits for optical modulators enabling higher-density parallel links at ultra-low energy per bit, terms undisclosed, 2026). Marvell is combining Polariton's plasmonics with its own silicon photonics and DSP capabilities to target coherent, scale-across, and data center optical interconnect platforms for next-generation architectures. The pace and scale of M&A signals Marvell is making a full-stack bet on CPO and advanced optical connectivity as a distinct, durable revenue layer — not merely an adjacency. See also Layer 6.
* **Nokia Q1 2026 Earnings — Optical Surge (Q1 2026):** Nokia optical division revenue +56% YoY to €821M ($959M), driven directly by AI data center connectivity investment and the March 2025 Infinera acquisition. Group comparable sales grew only 3% to €4.5B — the optical unit is carrying the company while legacy radio/mobile networks remain a drag (radio revenue -5% YoY, representing 35% of total revenue). Nokia raised Network Infrastructure growth guidance to 12–14% (from 6–8% in January) and guided full-year operating profit of €2.0–2.5B. Nokia revised its hyperscaler CapEx estimate sharply upward from $540B to over $700B for 2026, citing AI demand. Nokia-Nvidia partnership announced but enterprise market reaction still pending. Nokia is the most direct pure-play on the AI data center optical boom among publicly traded European telecom vendors.
* **CPO Testing Bottleneck (2026):** CPO mass production is being gated by the absence of automated, standardized test equipment — not chip design. A single PIC wafer-level inspection currently takes over 100 seconds on average due to the nanometer-level optical alignment required. The industry is running four distinct test stages (PIC wafer-level, EIC-PIC wafer-level, Optical Engine-level, advanced package module-level) with no unified standards and largely manual operations. TSMC's COUPE platform is entering volume production in 2026 using SoIC Face-to-Face stacking. Teradyne (acquired Quantifi Photonics 2025; first high-volume 300mm double-sided wafer probe system for silicon photonics) and Advantest (UFO Probe Card; V93000-Triton photonic test system) are the two ATE incumbents building solutions. FormFactor and Keysight are supplying components into these platforms. Whoever solves automated PIC testing at scale controls the CPO ramp timeline.

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| COHR | Coherent Corp | Vertically integrated optical components and transceivers; Nvidia $6B investment validates strategic position in AI interconnect stack |
| ANET | Arista Networks | Dominant data center networking switch vendor; strong position in AI cluster Ethernet fabric |
| GLW | Corning | Dominant fiber optic cable manufacturer; direct beneficiary of rural data center fiber demand surge and hyperscaler-backed backbone expansion; glass substrate expertise warrants investigation as a potential Layer 3 cross-layer position (glass core substrates and interposers are an emerging advanced packaging material — research priority) |
| LITE | Lumentum | Optical components supplier; Nvidia strategic investment; exposure to both transceiver and CPO transition |
| MRVL | Marvell Technology | Building end-to-end optical platform via Celestial AI ($3.25B), Polariton (plasmonic circuits), and XConn (PCIe/CXL); also listed under Layer 6 |
| CSCO | Cisco Systems | Incumbent networking vendor; AI cluster opportunity but legacy business creates drag |
| AAOI | Applied Optoelectronics | Small-cap transceiver supplier; high leverage to AI cluster buildout but limited moat vs. larger competitors |
| NOK | Nokia | Optical division +56% YoY driven by AI data center connectivity and Infinera acquisition; legacy radio networks drag; most direct European pure-play on AI optical infrastructure boom |
| TER | Teradyne | Semiconductor test equipment and collaborative robots; acquired Quantifi Photonics (2025) to enter CPO/silicon photonics test — first mover in automated PIC test equipment; also in Layer 12 |

---

## 8. Power Generation & Grid Equipment

*Profile: Long-cycle capital equipment with multi-year order books; AI data center power demand is a new, large, and durable demand vector; behind-the-meter generation emerging as grid interconnection constraints worsen.*

The energy infrastructure feeding AI data centers — gas turbines, fuel cells, grid equipment, and utilities. The most undertracked layer relative to its structural demand signal. Gas turbine prices are now spiking alongside GPUs and memory — a direct signal that power generation equipment is a binding infrastructure constraint.

### Persistent Themes

**Power is the next binding constraint after silicon.** AI data centers require sustained, high-density baseload power that the grid cannot reliably supply in key markets. Grid interconnection moratoriums in Northern Virginia — the most established data center market — are already forcing buildout to secondary markets and driving behind-the-meter generation at scale. As N3 capacity builds out (2027–2028), power becomes the dominant constraint across the stack. US data centers could consume up to 12% of the nation's total electricity by 2030, up from approximately 4% today — and even rapid efficiency gains will not come close to offsetting the surge. *Watch: grid interconnection queue timelines in key markets; TSMC N2/A16 ramp as the silicon-to-power timing trigger.*

**Gas turbine oligopoly is pricing in the demand shock.** GE Vernova and Siemens Energy hold the oligopoly on large-scale gas turbine manufacturing. Lead times are extending and prices are spiking — a direct signal that generation equipment is becoming a binding infrastructure constraint. Order books are multi-year. *Watch: GEV and Siemens Energy order book disclosures at earnings.*

**Behind-the-meter generation is becoming a structural theme, not a niche workaround.** Oracle's 2.8GW Bloom Energy fuel cell commitment is the largest known behind-the-meter power commitment to date — a signal that hyperscalers are accepting higher-cost on-site generation over grid interconnection uncertainty. *Watch: scale and pace of behind-the-meter commitments from hyperscalers; Bloom Energy order book.*

**Nuclear is the preferred long-term baseload solution.** SMRs and nuclear PPAs are the favored long-term answer for AI campus power — zero-emission, always-on, high-density. AWS stood up 3.9GW of new power capacity in 2025 and expects to double its total power footprint by end of 2027. Cameco (uranium supply) and BWXT (reactor components) are the primary pure-play public exposures. Oklo's 14GW+ pipeline — predominantly from data center operators including Meta, Equinix, and Switch — is the most concrete proof that hyperscaler SMR procurement has moved from exploration to serious multi-decade contracting. Commercial SMR scale deployments remain years out (Oklo targets first delivery 2027) but the procurement pipeline is now large enough to be investable. *Watch: SMR design certifications; Oklo first-reactor delivery timeline; hyperscaler nuclear PPA announcements; uranium spot prices.*

**The Midwest is absorbing overflow demand as primary markets hit grid limits.** Midwestern data centers constitute approximately one third of all US capacity and will account for more than half of new capacity coming online, driven by power scarcity in traditional Tier-1 markets. *Watch: data center siting announcements in secondary markets.*

### Recent Developments

* **GE Vernova Q1 2026 Blowout Earnings (Q1 2026):** Orders $18.3B (+71% YoY) — nearly 2x Q1 revenue of $9.3B, meaning GEV is building backlog faster than it can ship. EPS $17.44 vs. $1.97 consensus — a 9x earnings beat. EBITDA $896M vs. $770M expected. GEV now targets a $200B backlog by end of 2026, two years ahead of prior schedule. Approximately 100GW of power turbines are under contract; 4GW shipped in Q1. AI data centers account for approximately 20% of orders, with traditional utility customers accounting for the remaining 80% — AI demand is additive on top of an already full order book. GEV stock had already risen 204% in the prior 12 months before this print. The numbers confirm the power constraint thesis has fully arrived at the equipment layer.
* **Oracle/Bloom Energy Project Jupiter (Doña Ana County, NM):** Oracle is the anchor tenant at Project Jupiter — a data center campus in Doña Ana County, New Mexico, hosting OpenAI AI infrastructure. Oracle signed an expanded Bloom Energy partnership to procure up to 2.8GW of Bloom SOFCs (in addition to an initial 1.2GW contracted previously). Total Project Jupiter investment: up to $165 billion; 1,400 acres, four data center buildings — upon completion, Bloom's fuel cells will power one of the largest data center microgrids in the United States. Bloom's SOFCs are fuel-agnostic (natural gas, biogas, hydrogen) and aligned with 800V DC architecture. Oracle's data center uses a closed-loop, non-evaporative cooling system — no water draw from local water supply, directly addressing AI campus water constraint. Additional Bloom commitments in the same period: Equinix deploying Bloom fuel cells across 19 data centers at 100MW+ combined; American Electric Power signed a separate 1GW SOFC deal to power AI data centers off-grid; Bloom signed a $5B AI infrastructure partnership with Brookfield. The Oracle 2.8GW total and AEP 1GW together represent the clearest public evidence that behind-the-meter fuel cell power has moved from niche to mainstream AI infrastructure strategy.
* **AWS Power & CapEx Scale (2025–2027):** AWS stood up 3.9GW of new power capacity in 2025 and expects to double its total power footprint by end of 2027. AWS committed approximately $200B in CapEx in 2026, driven by concrete customer commitments, with monetization expected primarily in 2027–2028.
* **White House Space Nuclear Policy (April 2026):** White House directing NASA, the Pentagon, and DoE to develop space nuclear power systems with a launch target as soon as 2028 — extending the nuclear mandate into space infrastructure alongside OTA and the Reactor Pilot Program.
* **Midwest Data Center Geography Shift (2026):** Synergy Research Group tracking a pipeline of 803 DC projects; secondary markets absorbing demand Tier-1 markets can no longer accommodate. The Midwest projected to account for more than half of new US capacity coming online.
* **Oklo SMR Pipeline (2026):** Oklo (NYSE: OKLO) is developing the 75MW Aurora Powerhouse SMR, targeting first reactor delivery 2027. Total pipeline exceeds 14GW, with the vast majority of commitments signed with data center operators. Named deals: Meta (hyperscale data center power, terms undisclosed), Equinix 500MW, Switch non-binding 12GW Master Power Agreement through 2044, Prometheus Hyperscale 100MW LOI. Oklo was selected for both the DOE Nuclear Reactor Pilot Program (one of 11 advanced nuclear companies) and the DOE Advanced Nuclear Fuel Pilot Project. The Switch 12GW agreement is the largest single power commitment in the SMR pipeline. Oklo's customer list — Meta, Equinix, Switch — confirms that dedicated SMR procurement is moving from hyperscaler experimentation to serious multi-decade contracting.
* **Natural Gas CCGT Cost Surge and Equipment Backlogs (2025–2026):** BloombergNEF data: new CCGT plant construction cost surged 66%, from under $1,500/kW in 2023 to $2,157/kW in 2025; equipment prices are more than 195% above 2019 levels; average construction lead times extended by 23%; delivery backlogs are now stretching past 2029. Despite costs, demand for dispatchable behind-the-meter power is pulling in new modular entrants: Crusoe signed a deal with Boom Supersonic in December 2025 for 1.21GW of 42MW modular "Superpower turbines" — container-scale natural gas turbines targeting rapid-deployment data center power. The cost surge and backlog length directly confirm gas turbine generation capacity has crossed into shortage territory, reinforcing GEV's pricing power and order book durability.
* **NRC Part 57 Fast-Track Microreactor Framework (2026):** The U.S. Nuclear Regulatory Commission unveiled Part 57, a proposed licensing framework tailored specifically for microreactors, paired with a new Office of Advanced Reactors (OAR). Key provisions: construction permit and operating license timelines compressing to six months to one year; fleet-scale approvals (a single licensed operator overseeing an entire fleet of identical reactors); pathway for limited construction prior to receiving NRC permits; transportable microreactor accommodations; NRC OAR using AI to accelerate its own internal review processes. NRC Chairman Ho K. Nieh stated explicitly: "Regulatory uncertainty is capital risk." Estimated savings for the nuclear industry: $3.76B–$11.84B depending on discount rate. No specific public companies named in the Part 57 announcement, but the regulatory unlock is material for all nuclear companies in this layer — Part 57 removes the most frequently cited deployment timeline risk for SMR and microreactor projects.
* **X-Energy IPO and Uranium Supply Gap (2026):** X-Energy (Amazon-backed SMR developer) raised approximately $1.02 billion in a US IPO — the largest public market nuclear capital raise in recent history and concrete validation of institutional appetite. Concurrent development: Denison Mines Corp. and NexGen Energy received the first Canadian uranium mine construction approvals since 2004, for Wheeler River and Rook I projects in Saskatchewan. Critical structural context: US uranium mine production is expected to reach only approximately 1 million pounds in 2026 against annual US consumption exceeding 50 million pounds — a 50:1 supply-demand gap that makes uranium a structural import dependency regardless of near-term domestic nuclear capacity expansion.
* **Nvidia Nuclear Investments and Digital Twin Partnerships (2026):** Nvidia has made strategic investments in TerraPower (advanced nuclear) and Commonwealth Fusion Systems (fusion). Nvidia, Siemens, and CFS are building a digital twin of the CFS fusion reactor to accelerate commercial deployment. Separately, Nvidia and Oklo partnered with Los Alamos National Laboratory to develop AI-driven nuclear infrastructure — using physics and chemistry-based AI models and digital twins to advance reactor deployment and fuel validation. Nvidia is now a structural participant in the nuclear energy layer, not just a chip company: its simulation platform is being used to design the power infrastructure that will run its own chips.

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| GEV | GE Vernova | Q1 2026: orders $18.3B (+71% YoY, nearly 2x revenue), EPS $17.44 vs. $1.97 expected, $200B backlog target by end 2026 two years early; 100GW under contract; AI = ~20% of orders — the most direct and confirmed public play on the power constraint thesis |
| ETN | Eaton Corporation | Power management and electrical infrastructure; inside-the-fence power distribution for data centers; also in Layer 9 |
| BE | Bloom Energy | Fuel cell power generation; Oracle's 2.8GW commitment is a major validation of the behind-the-meter thesis |
| VST | Vistra Energy | Merchant power generator with direct AI data center PPAs; nuclear and gas fleet |
| CEG | Constellation Energy | Largest US nuclear operator; direct PPAs with hyperscalers (Microsoft); pure-play nuclear/clean baseload for AI |
| CCJ | Cameco | Largest publicly traded uranium producer; also listed under Layer 1 |
| BWXT | BWX Technologies | Nuclear reactor components, fuel, and services; DoD and commercial SMR exposure; also listed under Layer 1 |
| SMEGF | Siemens Energy | European gas turbine and grid equipment oligopolist; co-beneficiary of global AI power demand surge |
| OKLO | Oklo | SMR developer with 14GW+ pipeline (majority data center); Meta, Equinix, and Switch as anchor customers; first Aurora Powerhouse reactor targeted 2027; DOE Reactor Pilot Program participant |
| X-Energy | X-Energy | Amazon-backed SMR developer; raised $1.02B in US IPO; TRISO-fueled high-temperature gas-cooled reactor technology |

---

## 9. Data Center Infrastructure

*Profile: Infrastructure/REIT-like for operators; equipment suppliers have high leverage to cooling and power delivery CapEx; liquid cooling crossing from optional to mandatory; less than 10% of existing inventory meets AI-dense requirements.*

The physical facilities, cooling systems, and internal power delivery that house AI compute. Construction labor for 2-gigawatt campuses is tapped out. Liquid cooling has crossed from optional to mandatory — cooling accounts for up to 60% of a facility's total energy costs, and liquid cooling materially reduces this while enabling higher GPU densities.

### Persistent Themes

**Liquid cooling is a structural upgrade cycle, not a product transition.** Less than 10% of existing US data center inventory supports AI-dense critical load. The retrofit and greenfield buildout required to support AI workloads creates a multi-year equipment cycle. Liquid cooling is now mandatory for high-density GPU deployments — traditional air cooling becomes unviable as advanced silicon processors approach 100°C reliable operating junction temperatures. *Watch: Vertiv backlog growth and lead times as the primary indicator; liquid cooling retrofit contract announcements.*

**Dielectric fluid is the hidden supply chain bottleneck for liquid cooling.** The industry is entirely dependent on liquid cooling to run next-gen GPUs, making non-conductive dielectric fluid a mission-critical consumable. The dominant chemistry — 3M's Novec, a PFAS "forever chemical" — was withdrawn at end of 2025, forcing the data center supply chain into an abrupt chemical transition. Operators must now secure compliant alternatives (synthetics, plant-based, or highly refined petrochemicals) with a Global Warming Potential below 300, or high-density GPU deployments will stall. Running legacy PFAS fluids risks expensive forced phase-outs; securing next-gen fluids is now a gating factor for standing up new capacity. *Watch: regulatory phase-outs of existing fluid chemistries; supply bottlenecks for sub-300 GWP alternatives delaying cluster deployments.*

**Data center REITs are experiencing the strongest leasing environment in their history.** Vacancy rates at or near record lows; new builds often pre-leased before construction begins; long-term leases renewing at higher rates. Hyperscalers are signing guaranteed 15–20 year leases — a structural shift in the nature and duration of demand commitments. Operators with established footprints, secured power contracts, and scalable land banks command premium pricing. *Watch: pre-lease rates on new builds; power contract security as a differentiator between operators.*

**Construction labor and logistics are binding near-term constraints.** Building 2-gigawatt AI campuses requires specialized construction expertise that is currently fully committed. The DC supply chain is triggering approximately 8.46 million sq ft of logistics demand in Europe alone (~8,900 sq ft per MW). Target Hospitality's workforce housing business is a direct proxy for data center construction activity. *Watch: data center construction permit activity in secondary markets.*

**Chip generation transitions create redesign risk and cost overruns.** When new chip generations require different power and cooling specifications, mid-build data center redesigns cause delays and cost overruns — amplifying the financial impact of bottlenecks across the stack. *Watch: new chip generation announcement timelines vs. data center build schedules.*

**Water availability is an emerging operational dependency.** As liquid cooling becomes the baseline architecture, water availability and treatment quality become critical dependencies. Water quality failures represent direct operational risk; facilities in water-constrained regions are already resorting to recycled water with on-site storage and treatment. *Watch: water stress indices for major data center markets.*

### Recent Developments

* **Agentic AI Infrastructure Management (April 2026):** Equinix launched Fabric Intelligence, upgrading its interconnection fabric into a multi-agent system using model context protocol (MCP) — deploying specialized agents to dynamically provision and spin network capacity up or down based on traffic spikes. Lumen Technologies is deploying a parallel agentic network strategy with Blue Planet. Agentic AI is now actively managing physical infrastructure, not just running on it — turning passive network layers into programmable, sticky AI systems and deepening colocation moats. See also Layer 13.
* **Neocloud Market Power Shift (Late 2025–2026):** Before late 2025, GPU rental pricing was competitive. By early 2026, neoclouds and hyperscalers are firmly in control — demanding 20%+ prepays, longer contract terms, and setting deployment timelines on their own schedule.
* **Midwest Geography Shift (2026):** Midwestern data centers constitute approximately one third of US capacity and will account for more than half of new capacity coming online. See Layer 8 for full context.
* **Microsoft/Nscale Capacity Grab (April 2026):** Microsoft secured 30,000 Nvidia Rubin GPUs in Norway after OpenAI dropped out — indicating a catch-up phase in hyperscale capacity after previous spending curbs.
* **Logistics Demand Surge (2026):** Savills reports the DC supply chain is triggering 8.46 million sq ft of logistics demand in Europe (~8,900 sq ft per MW) as suppliers take traditional warehouse space to support the buildout.
* **Vertiv Acquires Strategic Thermal Labs (2026):** Vertiv acquired cold-plate design specialist Strategic Thermal Labs (STL), based in Georgetown, Texas (60,000 sq ft office and manufacturing facility). Terms undisclosed. STL brings expertise in cold-plate design, server-side liquid cooling, and high-density thermal validation — specifically at the interface between the server and its liquid cooling infrastructure. The acquisition deepens Vertiv's chip-level engineering capability as GPU power densities approach thresholds where system-level liquid cooling design becomes a direct performance and reliability variable.

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| VRT | Vertiv Holdings | Dominant data center power and cooling infrastructure; liquid cooling transition is a direct structural tailwind; highest leverage to AI-dense facility buildout |
| ETN | Eaton Corporation | Power management and UPS systems; inside-the-fence electrical infrastructure for data centers; also in Layer 8 |
| DLR | Digital Realty | Data center REIT; long-term lease structure benefits from AI demand shock; stable income with AI demand tailwind |
| EQIX | Equinix | Colocation and interconnection REIT; network-dense facilities and carrier-neutral hubs; agentic infrastructure management deepening platform moat |
| TH | Target Hospitality | Workforce housing for large construction projects; direct proxy for data center construction labor demand |
| SBGSY | Schneider Electric | Power management and data center automation; European equivalent to Eaton/Vertiv |
| JCI | Johnson Controls | Cooling and building management systems; AI data center cooling exposure alongside legacy HVAC |
| JBL | Jabil | Contract manufacturer for data center hardware and components; AI server supply chain exposure |
| IREN | IREN Limited | AI compute and power infrastructure; bitcoin miner transitioning to AI workloads |

---

## 10. Hyperscalers & Cloud

*Profile: Mega-cap with diversified revenue streams; AI is simultaneously a CapEx cost and a revenue opportunity; the reflexive loop benefits them most; valuation risk tied to application layer revenue validation.*

The integrated demand drivers, infrastructure builders, model developers, and platform providers. They sit at multiple layers simultaneously — buying compute, building data centers, developing models, and selling AI services. CapEx commitments for 2026 have roughly doubled from prior forecasts, driven by concrete customer demand rather than speculation. The binding constraint is no longer capital but silicon — hyperscalers would spend more if supply allowed.

### Persistent Themes

**Vertical integration into custom silicon is a structural margin decision, not a supply hedge.** AWS estimates Trainium saves tens of billions of CapEx dollars per year and delivers several hundred basis points of operating margin advantage for inference. Every hyperscaler is building custom silicon (Trainium/Graviton, TPU, Cobalt) to reduce NVDA dependency and capture the margin currently flowing to Nvidia. Amazon's in-house silicon is already tracking $20B+ annual revenue. *Watch: custom silicon adoption rate as share of total AI compute spend; Trainium/TPU/Cobalt performance vs. NVDA benchmarks.*

**Platform lock-in is deepening as enterprise AI workloads go into production.** The cloud platform layer has high switching costs for enterprise AI workloads — different interfaces, proprietary APIs, egress fees that penalize migration. As enterprises embed AI into core workflows, the platform becomes sticky. The battle is for AI workload share, not just general compute — and switching costs compound with every production deployment. *Watch: enterprise AI workload production deployment announcements; egress fee and interoperability policy changes.*

**The hyperscaler-AI lab relationship creates mutual dependency and exclusive interlocks.** Microsoft-OpenAI, Amazon-Anthropic, and Google-Anthropic partnerships bind AI labs into specific cloud infrastructure while giving hyperscalers preferred access to frontier model capabilities. These are not arm's-length commercial relationships — they are strategic interlocks that shape the competitive dynamics of both the cloud and model layers simultaneously. Anthropic pledged to spend over $100B on AWS technologies over the next 10 years (updated from the prior ~$80B total cloud spend figure across all providers through 2029) — with the expanded deal covering current and future Trainium chips, tens of millions of Graviton CPUs, and up to 5GW of capacity. Amazon is investing an additional $5B in Anthropic with a potential total commitment of up to $20B. *Watch: AI lab cloud spend commitments; exclusivity terms in hyperscaler-lab partnerships; Anthropic AWS utilization rate as the demand signal.*

**CapEx commitments are silicon-constrained, not capital-constrained.** Hyperscaler CapEx for 2026 has roughly doubled from prior forecasts — Google the most extreme accelerator. The binding constraint has shifted from capital to silicon; hyperscalers would spend more if supply allowed. This means demand is structurally stronger than CapEx figures suggest, and any silicon supply relief flows directly into additional spend. *Watch: CapEx guidance vs. actuals; hyperscaler commentary on silicon availability as the gating factor.*

### Recent Developments

* **Cloud Providers Pass Through Hardware Inflation (April 2026):** Chinese hyperscalers began raising prices for AI compute, signaling an end to subsidized market-share grabs. Alibaba Cloud raised rates for compute card offerings by 5–34% and storage by 30%; Tencent Cloud implemented a 5% hike across AI compute and container services. Broad-based hardware cost inflation (silicon, memory, optics) is being pushed to the application layer — and end-user demand is strong enough to absorb the price hikes.
* **2026 CapEx Roughly Doubles Prior Forecasts:** Google the most extreme accelerator. Binding constraint has shifted from capital to silicon — hyperscalers are silicon-constrained, not capital-constrained.
* **AWS Power & CapEx Scale (2025–2027):** AWS committed approximately $200B in CapEx in 2026, driven by concrete customer commitments. Monetization expected primarily in 2027–2028. AWS stood up 3.9GW of new power capacity in 2025 and expects to double its total power footprint by end of 2027.
* **Amazon Custom Silicon Revenue Scale (2026):** Amazon's in-house silicon tracking $20B+ annual revenue; Jassy confirmed exploring external rack sales with ~$50B run rate potential.
* **Microsoft/Nscale Capacity Grab (April 2026):** Microsoft secured 30,000 Nvidia Rubin GPUs in Norway after OpenAI dropped out — a catch-up phase following previous spending curbs.
* **Anthropic-AWS Expanded Commitment (2026–2035):** Amazon invested an additional $5B in Anthropic (potential total up to $20B). Anthropic pledged to spend over $100B on AWS technologies over the next 10 years — covering current and future Trainium chips, tens of millions of Graviton CPU chips, and up to 5GW of capacity for training and powering Claude models. AWS customers can now access Anthropic's full Claude Platform directly from their existing AWS account without additional credentials or contracts. Anthropic uses AWS as its primary training and cloud provider for mission-critical workloads. Separately, Broadcom signed a deal to provide Anthropic approximately 3.5GW of AI compute capacity using Google's AI processors starting 2027.
* **Google TPU 8 — Dual-Track Silicon (2026):** Google unveiled TPU 8 in two purpose-built variants. TPU 8t (training): 9,600 chips per superpod delivering 121 exaflops of FP4 compute — nearly tripling the prior Ironwood generation — with 2 petabytes of HBM and the new Virgo Network (19.2 Tbps scale-up bandwidth, 4x data center bandwidth increase); a single training cluster can scale to more than 1 million TPU chips. TPU 8i (inference/agentic): 1,152 chips per pod delivering 11.6 exaflops FP8, 80% better performance-per-dollar vs. Ironwood, 5x on-chip latency reduction via a new Collectives Acceleration Engine, and 2x better performance-per-watt. Both chips run on Google's Axion Arm-based CPUs, support liquid cooling, and will be generally available in 2026. Google's custom silicon program is now producing dedicated training and inference chips simultaneously — the most comprehensive in-house silicon roadmap among the hyperscalers.
* **Google Compute Lead (Epoch AI, 2026):** Google acquired more cumulative AI compute (measured in millions of H100 equivalents) between Q1 2022 and Q4 2025 than Microsoft, Meta, or Amazon — making it the most compute-intensive hyperscaler by this metric despite being the third-largest by cloud revenue. Gemini usage has climbed to 27% of the AI model market.
* **Google $40B Anthropic Investment (2026):** Google is investing up to $40 billion in Anthropic: $10 billion upfront, with the remaining $30 billion payable upon undisclosed performance milestones. Google had previously invested more than $3.75 billion across multiple earlier rounds and holds approximately 14% of Anthropic (disclosed in 2025 court documents). Concurrent arrangements: Anthropic pledged $50 billion in US data center commitments alongside Fluidstack, with Google providing the financial backing for these specific data center projects to host Anthropic's infrastructure. Broadcom and Google signed a separate deal securing 3.5GW of Google TPUs for Anthropic starting 2027. Anthropic also signed a separate cloud deal with CoreWeave. Anthropic currently uses all three major cloud platforms (Google, AWS, and Microsoft) — the Google $40B commitment makes Google the largest single capital provider to Anthropic by deal size, though AWS is the primary training provider. See also Layer 13.

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| AMZN | Amazon | AWS is the largest cloud platform; Trainium/Graviton custom silicon program most advanced and economically compelling; ~$200B 2026 CapEx driven by committed customer demand |
| MSFT | Microsoft | Azure + OpenAI partnership creates the strongest enterprise AI platform; Copilot and Azure OpenAI Service are the leading AI monetization vehicles |
| GOOGL | Alphabet | Most vertically integrated AI stack; TPU 8 (121 exaflops training / 80% better perf/dollar inference) is the most comprehensive in-house silicon roadmap among hyperscalers; most cumulative AI compute deployed per Epoch AI; most extreme CapEx accelerator; AI search monetization is the key near-term risk/opportunity |
| META | Meta Platforms | Largest open-source AI model (Llama); $100B AMD deal and CoreWeave contracts reflect massive infrastructure commitment; monetization via advertising AI, not cloud services |

---

## 11. Neoclouds

*Profile: High revenue growth and backlog visibility via multi-year contracts; high execution and financial risk from bridge financing; pricing power has shifted decisively to operators; CoreWeave's $21B Meta contract anchors deal scale.*

Purpose-built AI compute providers — dedicated, liquid-cooled GPU clusters operated on multi-year contracts for hyperscalers and AI labs. The GPU rental market has flipped from competitive to seller-controlled. Operators now demand 20%+ prepays and set deployment schedules on their own timeline.

### Persistent Themes

**The market has flipped from competitive to seller-controlled.** Before late 2025, GPU rental pricing was competitive. By early 2026, neoclouds are firmly in control — demanding higher prepays, longer contract terms, and setting deployment timelines. CoreWeave's $21B Meta contract is the concrete scale anchor. Major AI labs are locking in 50–100MW clusters (~24,000–48,000 GB300 NVL72 GPUs) on 4–5 year terms; hyperscalers are backstopping deals in exchange for a share of project revenue. *Watch: contract term length and prepayment requirements as pricing power indicators; mid-term GPU rental contract pricing as the most economically relevant demand signal.*

**Bridge financing risk is the primary downside.** Neoclouds frequently deploy GPUs before facilities are fully operational, relying on short-term bridge financing that assumes rapid time-to-revenue. Supply chain, construction, or power procurement slippage leaves GPU assets idle and makes refinancing extremely difficult. Only 22.8% of AI initiatives successfully meet their original ROI objectives in production. *Watch: neocloud debt refinancing terms; GPU delivery vs. facility readiness timelines.*

**Purpose-built AI-dense inventory is structurally scarce.** Less than 10% of existing US data center inventory is capable of supporting true AI-dense critical load. The greenfield buildout required to serve this demand is a multi-year pipeline, creating durable demand for new capacity from qualified operators with established power contracts and liquid cooling infrastructure.

**Demand is broadening beyond Big Tech and AI labs.** Enterprise verticals — specifically high-frequency finance — are now deploying capital at hyperscaler scale for frontier GPU cluster access. This broadens the neocloud demand base and further secures revenue visibility beyond the current concentrated customer set. *Watch: non-Big Tech enterprise neocloud contract announcements as demand broadening indicators.*

### Recent Developments

* **Jane Street $6B CoreWeave Contract (April 2026):** Quantitative trading firm Jane Street signed a $6B AI cloud capacity deal with CoreWeave (incorporating Nvidia Vera Rubin hardware) and made a $1B equity investment at $109/share. Frontier-scale GPU cluster demand is expanding beyond Big Tech and AI labs into enterprise finance — a meaningful demand broadening signal that further secures neocloud revenue visibility.
* **CoreWeave $21B Meta Contract (April 2026):** The concrete scale anchor for individual neocloud deal size and validation of the multi-year contracted revenue model.
* **Long-Term Offtakes Accelerating (2026):** Major AI labs locking in 50MW–100MW clusters on 4–5 year terms. Hyperscalers backstopping deals in exchange for project revenue share.
* **Anthropic-AWS Expanded Commitment (2026–2035):** Anthropic pledged $100B+ on AWS over 10 years; Amazon investing additional $5B (up to $20B total). Anthropic's total cloud commitments span CoreWeave, Google/Broadcom, Microsoft Azure, and AWS — validating neocloud demand at the lab level. See also Layer 10.
* **GPU Cluster TCO: Gold Neoclouds Structurally Cost-Advantaged (2026):** A detailed 3-scenario TCO analysis comparing Gold-tier neoclouds, hyperscalers, and Silver-tier neoclouds across large LLM pretraining, multimodal RL research, and inference endpoints finds hyperscalers charge a 1.10x–1.61x premium over Gold neoclouds primarily due to support costs, storage pricing, and GPU rates. Silver-tier neoclouds carry a 1.01x–1.15x premium mostly from goodput loss (cluster downtime and failed checkpoints). For large training workloads, Gold-tier neoclouds (purpose-built GPU clusters with high goodput and competitive storage) are structurally cheaper than hyperscalers — reinforcing the CoreWeave thesis that purpose-built beats general-purpose for AI training at scale.
* **Brookfield Acquires Ori Neocloud (2026):** Brookfield Asset Management acquired Ori, a neocloud provider previously backed by Saudi Aramco. A global infrastructure capital allocator entering pure-play AI compute signals the asset class is maturing from venture-backed startups to institutional infrastructure — a potential precursor to REIT-like capital structures and lower cost of capital for the sector.
* **OpenAI Growth Slowdown and Oracle Abilene Shortfall (2026):** OpenAI missed its goal of reaching 1 billion weekly active accounts by end of 2025 and is experiencing subscriber churn. The Oracle Abilene, Texas campus — the centerpiece of a $300B data center commitment — has only 2 of 8 buildings operational; OpenAI and Oracle have reportedly shelved plans to expand the campus due to disagreements over financing terms. OpenAI CFO Sarah Friar warned executives the company may struggle to finance its data center buildout "if revenue doesn't grow fast," prompting board scrutiny of infrastructure contracts. OpenAI's annualized run rate stands at $24 billion (late March 2026) vs. Anthropic's $30 billion run rate. Both companies are preparing public listings: OpenAI expects to list as soon as Q4 2026 at approximately $1 trillion valuation; Anthropic hired a law firm in December and has launched discussions with potential underwriters. The Oracle Abilene operational shortfall is a direct negative data point for Oracle OCI and GPU partnership revenue visibility near-term. See also Layer 13.

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| CRWV | CoreWeave | Largest neocloud; $21B Meta contract and $6B Jane Street deal anchor multi-year revenue visibility; execution and refinancing risk are the key risks |
| NBIS | Nebius Group | European-focused AI cloud; infrastructure and compute platform; earlier stage than CoreWeave |
| IREN | IREN Limited | Transitioning from bitcoin mining to AI compute; power infrastructure assets are the underlying value |
| WULF | TeraWulf | Bitcoin miner transitioning to AI compute; housing 70MW of AMD MI300X for Core42 (G42) — early signal of mining-to-AI infrastructure conversion at meaningful scale |

---

## 12. Physical AI & Robotics

*Profile: Hardware-intensive with longer commercialization timelines than software; distinct edge inference chip demand; industrial and defense customer bases; falling hardware cost curves are the key enabler.*

AI brought into the physical world — robotics, autonomous vehicles, drones, and edge inference systems. A structurally distinct layer from AI-native software applications: different investment characteristics, different company set, different demand dynamics. Edge AI silicon demand is emerging as a separate and growing demand vector from data center compute.

### Persistent Themes

**Falling compute costs and better AI models are unlocking robotics at scale.** Industrial robotics has been constrained for years by software limitations. Improved AI models combined with falling inference hardware costs are enabling robots to move beyond repetitive, structured tasks into variable environments. Nearly four million industrial robotic systems are already deployed globally; AI upgrades create a retrofit and expansion cycle on top of an existing installed base. Humanoid robot costs are falling toward approximately $50,000 per unit — a threshold that begins to enable broader commercial deployment. *Watch: AI-enabled industrial robot shipment data; humanoid cost curve benchmarks; autonomous vehicle commercial deployment milestones.*

**Edge inference silicon is a growing and structurally distinct demand vector.** Physical AI systems require on-device inference — real-time processing of sensor data without cloud round-trips. Fiber latency physics constrain round-trip processing to approximately 1ms per 125 miles; AR/VR requires under 3ms while typical carrier targets are approximately 10ms — a gap only closable by local edge processing. This creates demand for chips optimized for edge inference that is structurally separate from data center GPU demand and grows independently as autonomous systems scale. *Watch: edge AI chip shipment volumes; autonomous vehicle regulatory approvals.*

**Defense and industrial reshoring are structural demand tailwinds.** Defense applications (surveillance, autonomous systems, logistics support) and industrial automation driven by reshoring create durable, less cyclical demand for physical AI systems. These customer bases have longer procurement cycles but more stable demand profiles than consumer robotics. *Watch: defense autonomous systems procurement announcements; reshoring-driven factory automation CapEx.*

**Nvidia's simulation platform is a strategic position in physical AI training.** NVDA's Omniverse and Isaac platforms are used to generate synthetic training data for physical AI systems — robots, autonomous vehicles, industrial systems — before real-world deployment. This gives Nvidia a structural position in physical AI beyond edge inference chips: control over the training environment itself. *Watch: Omniverse/Isaac adoption rates among robotics developers.*

### Recent Developments

* **Tesla AI5 Tape-out & Hardware Pipeline (April 2026):** Elon Musk confirmed the tape-out of Tesla's AI5 chip. Tesla is securing dedicated 2nm production capacity at Samsung's Taylor fab and transitioning to next-generation LPDDR6 memory for AI6 iterations. A major physical AI operator is driving its own dedicated custom silicon and memory demand vector entirely separate from the cloud data center buildout — filling a critical data gap for this layer.
* **ABB Robotics — SoftBank Acquisition + Nvidia Omniverse Integration (2026):** ABB Group agreed to sell its robotics unit to SoftBank Group for $5.3B. The unit employs ~7,000 people and houses its US headquarters and factory in Auburn Hills, Michigan. ABB launched PoWa, a new high-speed cobot family (7–30kg payload, 5.8 m/s top speed, under-1-hour deployment) bridging the gap between collaborative robots and traditional industrial robots. ABB integrated Nvidia Omniverse libraries into its RobotStudio software; the resulting RobotStudio HyperReality subscription product launches H2 2026 for robot simulation and real-world deployment validation. The cobot market is growing ~20% annually through 2028. Note: if the SoftBank acquisition closes, ABB (ABB Ltd) ceases to be the relevant public ticker for robotics exposure — SoftBank (SFTBY) becomes the primary vehicle.
* **Distributed AI Inference Architecture (2026):** Physical AI — robots, autonomous vehicles, drones — is forcing a structural shift toward distributed compute architectures: on-device (microsecond response for safety-critical control), local data center (low-latency edge inference), and central hyperscale data center (non-latency-sensitive training and GenAI). Fiber latency physics make centralized-only architectures physically impossible for real-time control. Industrial users in oil/gas and manufacturing are actively migrating from wired to wireless connectivity for on-site edge AI workloads. Qualcomm's edge inference thesis is directly validated by this architectural shift — on-device processing is not a feature preference but a physics requirement for physical AI applications.

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| NVDA | Nvidia | Jetson platform for edge AI inference; Omniverse/Isaac simulation platform for physical AI training; also in Layer 4 |
| QCOM | Qualcomm | Edge AI inference chips for mobile, automotive, and industrial applications; distributed inference architecture (device + local DC + central DC) is a physics requirement for physical AI — validates AI-on-device as structurally necessary, not optional |
| ABB | ABB Ltd | Industrial robotics and automation; AI-enabled upgrade cycle; robotics unit being sold to SoftBank for $5.3B — if closed, SFTBY becomes the primary public vehicle for this exposure |
| ROK | Rockwell Automation | Industrial automation and control systems; AI integration into factory workflows |
| ISRG | Intuitive Surgical | Robotic-assisted surgery; AI integration enhancing training and real-time decision support |
| TER | Teradyne | Semiconductor test equipment and collaborative robots (Universal Robots); dual exposure to chip test and industrial automation |

---

## 13. AI-Native Applications

*Profile: Highly varied — from infrastructure-like data platforms to high-moat vertical AI to commoditizing point solutions; switching costs high for deeply integrated platforms, low for model-layer tools; application layer revenue is the validation endpoint for the entire infrastructure buildout.*

Software built on top of the AI stack — data infrastructure, AI agents, vertical applications, and cybersecurity. Demand is strong and broad-based; the binding constraint is now compute supply, not customer demand. Anthropic ARR surged from approximately $9B to over $30B in Q1 2026 — more than tripling in a single quarter.

### Persistent Themes

**The application layer is validating the infrastructure buildout from the demand side.** The infrastructure buildout implies a revenue obligation at the application layer that must ultimately be validated — track it through AI lab ARR growth rates, cloud AI services revenue acceleration, and token demand breadth. Anthropic's Q1 2026 ARR surge is the most direct data point: demand is real, broad-based, and global; the binding constraint has flipped from demand to supply. Multi-agent, multi-step workloads executing with high concurrency are the primary driver of the token demand inflection. *Watch: AI lab ARR growth rates; token demand breadth (broad-based vs. single-player driven); cloud AI services revenue growth (AWS Bedrock, Azure OpenAI, Vertex AI).*

**Proprietary data is the durable moat; raw model access is commoditizing.** Companies with hard-to-replicate proprietary datasets — PLTR's government and enterprise integrations, SNOW's data cloud network effects, TEM's clinical oncology data — have the most defensible positions. Model access itself is becoming a commodity as open-source models improve; the data layer is where durable competitive advantage accrues. Frontier model consolidation among the Big 5 (OpenAI, Anthropic, Google, Meta, xAI) means the model layer is increasingly concentrated at the top and competitive below. *Watch: proprietary data acquisition announcements; open-source model capability vs. frontier model gap.*

**Cybersecurity is non-discretionary AI spend with a structurally expanding attack surface — and agentic AI is the next frontier.** AI is simultaneously expanding the attack surface (more endpoints, more agents, more data flows) and enabling faster threat detection. CRWD and PANW are positioned as AI-native security platforms. Enterprises cannot defer this spending — it grows with AI adoption. Agentic AI is creating a new security surface: autonomous agents interacting with enterprise systems, external APIs, and cloud infrastructure require guardrails, visibility, and runtime protection that traditional posture-only tools cannot provide. Real-time event streaming (detecting breaches in seconds vs. legacy batch tools taking 15+ minutes) is now a competitive differentiator. *Watch: enterprise security budget allocation to AI-native platforms; agentic AI security contract announcements.*

**Agentic AI is the next step-change in token demand and platform lock-in.** AI agents interacting autonomously with enterprise systems generate far larger token volumes than single-query interactions. As agentic workflows move from experimentation to production, they create a compounding demand multiplier for compute and a compounding lock-in effect for integrated platforms. Systems of record — the enterprise platforms where agentic AI must integrate — become the new switching cost moat. Agentic AI is now also managing physical infrastructure directly (see Layer 9), further expanding the scope of the workload shift. *Watch: agent workflow production deployment rates; enterprise platform integration depth; agentic token demand as share of total.*

**Value is migrating from infrastructure to model labs as inference economics flip.** The 2023–2025 period saw infrastructure layers capture almost all AI value. That is reversing: AI model labs (Anthropic, OpenAI) are now capturing disproportionate value as token production costs fall sharply while end-user ROI compounds. Anthropic's inference gross margins expanded from 38% to 70%+ not from price hikes but from infrastructure cost reductions — labs are capturing the efficiency gains while customers experience extreme ROI. Inference providers (Fireworks, Baseten, Fal) are also seeing widening margins and hyper-growth revenues as token delivery becomes structurally cheaper. The implication: the application and model layers are entering a period of margin expansion while infrastructure layer pricing power is partly capped by ecosystem management decisions (TSMC explicitly not raising prices to protect long-term relationships; Nvidia not yet pricing to value). *Watch: AI lab gross margin trends; inference provider margin expansion; Nvidia pricing decisions on Vera Rubin vs. GB300 as the margin extraction signal.*

**The software disruption narrative has real credit market consequences.** AI tools create a narrative that enterprise software can be replicated or replaced. This tension is now affecting software companies' ability to refinance debt — a real credit market signal, not just a valuation narrative. The counter-argument centers on switching costs, network effects, deep integrations, and the difficulty of replicating embedded enterprise workflows at scale. *Watch: software company debt refinancing conditions as an early disruption signal.*

### Recent Developments

* **Agentic Token Demand Inflection (Q1 2026):** China's National Data Administration reported daily token calls jumped from 100 billion in early 2024 to over 140 trillion by March 2026 — a approximately 1,000x increase — fueled by video generation (Seedance) and multi-step workflow agents (OpenClaw). Provides hard volumetric proof that the application layer is generating the massive end-user compute consumption required to validate the upstream infrastructure buildout.
* **Anthropic ARR Surge (Q1–Q2 2026):** Anthropic ARR surged from approximately $9B to over $44B year-to-date — roughly 5x in a single cycle, with growth compute-constrained rather than demand-constrained. Multi-agent workloads executing multi-step tasks with high concurrency are the primary driver. Anthropic's gross margins on inference infrastructure expanded from 38% to over 70%, driven by inference cost reductions rather than price hikes — the most direct evidence that AI model labs are now capturing disproportionate value as infrastructure costs fall faster than token prices. Blended actual cost per million tokens on agentic workloads is approximately $0.99 despite a $5/$25 sticker price — high cache hit rates (90%+) and cheap cached inputs ($0.50/MTok) mean the effective price is approximately 5x lower than headline pricing.
* **Anthropic Exploring Custom Silicon (2026):** Anthropic in early-stage exploration of in-house chip design in response to compute shortage constraining Claude's growth — no committed design or dedicated team yet. Signals that even application layer companies are being pulled upstream by compute scarcity.
* **Frontier Model Consolidation:** The Big 5 (OpenAI, Anthropic, Google, Meta, xAI) are consolidating the frontier model layer. Switching costs are low at the raw model layer but much higher for orchestration frameworks, agent integrations, and data services — the durable moats sit above and below the raw model.
* **CrowdStrike Multi-Cloud and Agentic AI Security (Q2 2026):** CrowdStrike expanded its real-time Cloud Detection and Response (CDR) to Google Cloud Platform, completing full coverage of all three major clouds (AWS + Azure + GCP). Named Google Cloud Security Partner of the Year for Infrastructure Protection for the second consecutive year. Designated as a launch partner for the Google Agent Cloud Ecosystem — Google's open platform for agentic AI applications — to deliver guardrails, visibility, and runtime control as agentic AI moves into production. CrowdStrike's real-time event streaming engine surfaces detections in seconds vs. 15+ minutes for legacy batch-processing tools, a critical differentiator as AI-powered attackers pivot between systems faster than humans can respond. Regional Google Cloud infrastructure deployment solves data residency friction for multinational customers.
* **Salesforce Agentforce Operations Launch (May 2026):** Salesforce launched Agentforce Operations, an agentic system automating back-office workflows — built on Salesforce's acquisition of Regrello (business process automation, supply chain focus). Key design: natural language configuration (managers describe changes in email; agent implements with approval), radical transparency (full audit trail of every agent action), and workflow blueprints enabling deployment 80x faster than legacy tools. Beta integration with Salesforce Flow (Salesforce's no-code automation tool) expected May 2026. Available now. AWS is making a parallel move into the same application layer with Amazon Connect: expanding from cloud contact center into four vertical agentic SaaS offerings — Amazon Connect Customer AI (identity verification, payment workflows), Connect Decisions (supply chain/logistics agentic optimization powered by Amazon's Chronos2 time-series forecasting model), Connect Talent (volume-hiring automation built on Amazon's own 250,000-seasonal-worker hiring experience), and Connect Health (patient verification, appointment management, clinical documentation). Both Salesforce and AWS are moving up the stack from platforms into industry-specific agentic applications — competing for the same enterprise workflow automation budget.
* **Frontier Model Competitive Dynamics and the Cost-Per-Task Era (Q1–Q2 2026):** OpenAI's GPT-5.5 post-training utilized a 100,000-GPU GB200 NVL72 cluster — the largest known single post-training compute deployment. SemiAnalysis argues public benchmarks are increasingly unreliable for real-world utility (MMLU saturated at 86.4% by GPT-4 in 2023; SWE-bench contamination confirmed across multiple frontier models); "cost per task" and token efficiency are emerging as the true north star metrics. Engineers pay 6x premiums for latency-optimized "fast modes" to maintain coding flow state — latency over absolute quality. DeepSeek V4 achieved 90% KV cache reduction vs. its predecessor and introduced MoE architecture delivering 1.5–1.96x inference speedups. The coding agent market is the most contested frontier model battleground: whoever wins developer workflows wins the compounding lock-in that comes with deep toolchain integration.

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| PLTR | Palantir | AI platform with deep government and enterprise data integrations; AIP bootcamp model driving rapid enterprise adoption; highest moat in the layer |
| NOW | ServiceNow | Enterprise workflow automation; AI Agents on the Now platform are the growth vector; deep enterprise integration moat |
| CRWD | CrowdStrike | AI-native cybersecurity platform with full multi-cloud CDR coverage (AWS + Azure + GCP); launch partner for Google Agent Cloud Ecosystem securing agentic AI; Falcon consolidation thesis; non-discretionary spend that grows with AI adoption |
| PANW | Palo Alto Networks | Security platform consolidation play; AI-driven threat detection; platformization strategy |
| SNOW | Snowflake | Data cloud with strong network effects; AI data platform and Cortex AI expanding the platform moat |
| DDOG | Datadog | AI observability and monitoring; benefits from proliferation of AI workloads needing instrumentation |
| ORCL | Oracle | Database incumbency plus cloud infrastructure buildout; OCI gaining AI workload share; $300B OpenAI cloud deal anchors demand scale |
| MDB | MongoDB | Developer data platform; flexible document model suits AI application data structures |
| TEM | Tempus AI | Clinical AI with proprietary oncology data library; specialized data moat in healthcare |
| IBM | IBM | Hybrid cloud and enterprise AI (watsonx); legacy business drag but enterprise relationships are sticky |
| PL | Planet Labs | Daily satellite imagery data; geospatial AI with proprietary data moat |
| SOUN | SoundHound AI | Voice AI platform; automotive and enterprise deployments |
| CRM | Salesforce | Agentforce Operations launched (May 2026) — agentic back-office automation built on Regrello acquisition; 80x faster deployment vs. legacy tools; direct competitor to AWS Connect in enterprise workflow automation |

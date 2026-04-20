# AI Supply Chain — Layer Map

*Last updated: 2026-04-20*

A layer-by-layer map of the AI supply chain for investment research. Each layer has distinct investment characteristics, structural tailwinds, and company-level theses. Use this alongside `context_sectors.md` (macro dynamics) to identify tracker candidates and prioritize deep dives.

---

## Stack Overview

```
[ 1. Raw Materials & Mining          ]  ← upstream inputs
[ 2. Semiconductor Equipment         ]  ← fabrication tools
[ 3. Foundries & Advanced Packaging  ]  ← wafer production, chip assembly
[ 4. Compute Silicon                 ]  ← GPUs, CPUs, custom ASICs
[ 5. Memory Silicon                  ]  ← HBM, DRAM, NAND
[ 6. Networking & Custom Silicon     ]  ← merchant silicon, ASICs, SmartNICs
[ 7. Optical & Physical Connectivity ]  ← transceivers, switches, fiber cable
[ 8. Power Generation & Grid         ]  ← turbines, fuel cells, grid equipment
[ 9. Data Center Infrastructure      ]  ← buildings, cooling, power delivery
[ 10. Hyperscalers & Cloud           ]  ← demand drivers, platform builders
[ 11. Neoclouds                      ]  ← pure-play AI compute providers
[ 12. AI-Native Applications         ]  ← vertical software, data, agents
```

---

## Stack Status & Constraint Map

*Last updated: 2026-04-20*

The AI infrastructure buildout is in peak execution mode. Demand is real, broad-based, and growing faster than the supply chain can respond at multiple layers simultaneously. The binding constraints have migrated from capital (no longer the issue) to physical supply — silicon, memory, power, and construction labor are all strained at once, which is unusual and reflects the scale of the demand shock. The reflexive loop (high valuations → cheap capital → more CapEx → more demand) remains intact.

### Where the Constraints Are

* **Raw Materials & Mining — Tightening:** Rare earth prices outside China running at up to 5x premium on key elements (Terbium, Dysprosium); uranium demand building with nuclear renaissance; copper demand structurally rising with electrification and data center buildout. Domestic decoupling subsidies are accelerating but commercial-scale alternatives remain years out. *Beneficiaries: MP, CCJ, FCX*

* **Semiconductor Equipment — Tightening:** TSMC CapEx — which only exceeded its prior peak in 2025 — is driving multi-year equipment order books. N2/A16 node buildout will sustain elevated equipment demand through the decade. Export controls cap China revenue but insulate incumbents from competition. *Beneficiaries: ASML, LRCX, KLAC, AMAT*

* **Foundries & Advanced Packaging — Shortage:** The most acute hardware constraint in the stack. TSMC N3 utilization is on track to exceed 100% in H2 2026, nearly entirely squeezing out smartphone and CPU wafers. Every major AI accelerator (NVDA Rubin, AMD MI400, Google TPU v7/v8, AWS Trainium3, Meta MTIA) has converged on N3 simultaneously. TSMC cannot expand cleanroom space fast enough. *Beneficiaries: TSM (pricing power), AMKR, ASX (CoWoS packaging overflow)*

* **Compute Silicon — Shortage:** GPU compute effectively sold out through August–September 2026. H100 spot pricing up ~40% from October 2025 trough to $2.35/hr; existing contracts being renewed for 4-year extensions through 2028. Blackwell lead times extend to June–July 2026 with all capacity committed. Two large AWS customers independently asked to purchase every available Graviton instance in 2026 — AWS declined. *Beneficiaries: NVDA, AMD*

* **Memory Silicon — Shortage:** HBM capacity constrained by wafer allocation; LPDDR5X and DDR5 contract prices tracking ~4–5x year-on-year increases; Q2 2026 DRAM and NAND contract pricing forecast at +60% and +70% QoQ respectively. LTA structuralization (3–5 year deals) is locking Big Tech into preferred supplier positions and reducing cyclicality. *Beneficiaries: MU, HXSCL*

* **Networking & Custom Silicon — Tightening:** Not a hard shortage, but ASIC design win pipelines are accelerating as hyperscalers deepen custom silicon programs to reduce NVDA dependency. ASIC share of AI server shipments forecast at 27.8% in 2026, rising toward 40% by 2030. Long design-to-revenue lead times mean current wins translate into multi-year contracted revenue. *Beneficiaries: AVGO, MRVL*

* **Optical & Physical Connectivity — Shortage:** Ethernet transceiver sales for AI clusters forecast to double in 2026; fiber optic cables experiencing price spikes alongside GPUs and memory; hyperscalers signing 2–3 year guaranteed supply contracts. Lumen actively building a specialized AI fabric to serve dozens of new rural data center clusters. *Beneficiaries: COHR, GLW, ANET*

* **Power Generation & Grid — Tightening, approaching shortage in key markets:** Gas turbines are spiking in price alongside GPUs and memory — a direct signal that power generation equipment is becoming a binding infrastructure constraint. Grid interconnection moratoriums in established markets (Northern Virginia) are severe enough that Oracle committed to 2.8GW of Bloom Energy fuel cell power as behind-the-meter generation rather than wait for grid interconnection. *Beneficiaries: GEV, BE, ETN*

* **Data Center Infrastructure — Tightening:** Construction labor to build 2-gigawatt campuses is tapped out. Less than 10% of existing US inventory supports AI-dense critical load. Liquid cooling has crossed from optional to mandatory, creating a structural upgrade cycle across the existing base. *Beneficiaries: VRT, TH*

* **Hyperscalers & Cloud — Silicon-constrained, demand strong:** CapEx commitments for 2026 have roughly doubled from prior forecasts, driven by committed customer demand. The binding constraint is no longer capital but silicon and power — hyperscalers would spend more if supply allowed. AI cloud services revenue is growing rapidly but the full Revenue Imperative (~$600B) has not yet been validated.

* **Neoclouds — Supply tight, pricing power with operators:** GPU rental market has flipped from competitive to seller-controlled. Operators now demand 20%+ prepays and longer contract terms, setting deployment schedules on their own timeline. CoreWeave's $21B Meta contract anchors the scale of individual deals. Bridge financing risk is the primary downside.

* **AI-Native Applications — Demand strong, compute-constrained:** Anthropic ARR tripled in Q1 2026, with growth compute-constrained rather than demand-constrained. Demand is broad-based and global. The Revenue Imperative thesis is being validated from the demand side; the binding constraint has flipped from demand to supply.

---

### Constraint Flow

*Forward-looking inferences from current bottlenecks. These are hypotheses, not facts — update as signals evolve.*

* **N3 shortage is structurally accelerating custom silicon adoption:** GPU scarcity forces hyperscalers to deepen Trainium, TPU, and custom ASIC programs faster than originally planned. The longer N3 stays constrained, the more committed hyperscalers become — making the shift away from merchant NVDA silicon structural rather than opportunistic. AVGO and MRVL are the compounding beneficiaries. Watch: new hyperscaler custom silicon program announcements as the leading signal.

* **As N3 capacity eventually builds (2027–2028), the bottleneck likely migrates to Power:** Every new chip produced needs a data center, and every data center needs power. The current silicon squeeze is masking what will become a severe power generation and grid constraint at scale. Energy infrastructure — GEV, VST, CEG, nuclear (CCJ, BWXT) — is the next layer to position in as silicon supply eases. Watch: TSMC N2/A16 capacity ramp timelines as the trigger.

* **Power tightening raises the premium on efficiency across the entire stack:** When power is the binding operational constraint, anything that delivers more compute per watt gains structural value — liquid cooling (VRT), LPDDR5X over DDR5, ARM architectures, on-site generation (GEV, BE). This is a second-order tailwind that benefits efficiency plays regardless of which specific silicon or power generation technology wins.

* **Intel 18A yield improvement is the most important foundry relief valve to watch:** If Intel achieves production-ready yields on 18A, it unlocks meaningful N3-alternative capacity for AMD and hyperscaler ASIC programs currently queued at TSMC. Current yields (<50%) make this a 2027 story at best — but any positive yield disclosure is a high-signal event for the foundry diversification thesis and a modest headwind for TSM's pricing power.

* **Memory shortage is pushing architectural alternatives into the mainstream:** HBM constraints and surging DRAM prices are accelerating adoption of SOCAMM/LPDDR5X as server memory alternatives. If SOCAMM gains production traction, it opens a new addressable market for memory suppliers with mobile-heritage efficiency expertise and creates a second-order disruption risk for legacy DDR5 server memory configurations.

---

## 1. Raw Materials & Mining

*Upstream inputs: rare earth elements, copper, uranium, and specialty materials that physical AI infrastructure cannot be built without.*

**Investment characteristics:** Commodity/cyclical with geopolitical premium; government subsidy tailwind for domestic players; long permitting and development timelines; China processing monopoly is the structural overhang for rare earths.

### Structural Themes
*See `context_sectors.md` → Critical Minerals & Rare Earths*

#### Watch
*See `context_sectors.md` → Critical Minerals & Rare Earths → Watch*

### Current Status
*See `context_sectors.md` → Critical Minerals & Rare Earths → Current Status*

### Developments
*See `context_sectors.md` → Critical Minerals & Rare Earths → Developments*

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| MP | MP Materials | Only US rare earth miner with mine-to-magnet integration; primary beneficiary of domestic decoupling subsidies |
| UUUU | Energy Fuels | US uranium and rare earth producer; dual exposure to nuclear buildout and REE decoupling |
| UURAF | Appia Rare Earths | Early-stage rare earth explorer; speculative exposure to domestic supply chain buildout |
| USAR | US Critical Materials | *[TBD — needs research]* |
| NB | Niocorp Developments | *[TBD — needs research]* |
| CCJ | Cameco | Largest publicly traded uranium producer; primary beneficiary of nuclear renaissance demand |
| FCX | Freeport-McMoRan | Largest publicly traded copper miner; leveraged to AI data center and electrification copper demand |
| SCCO | Southern Copper | High-margin copper producer; long reserve life and low-cost operations |

---

## 2. Semiconductor Equipment

*The tools that make chip fabrication possible. An oligopoly "toll road" on the entire AI silicon buildout — every wafer produced requires their machines.*

**Investment characteristics:** Oligopoly/monopoly moats (ASML on EUV, AMAT/LRCX/KLAC on etch, deposition, and inspection); revenue tied to foundry CapEx cycles but with a lag; high recurring service revenue provides downside cushion; export controls are a ceiling on China revenue.

### Structural Themes
* **The Toll Road Dynamic:** Every chip manufactured for AI — regardless of whether it's NVDA, AMD, TSM's own designs, or custom silicon — runs through this layer's tools. Moats are structural: ASML holds a monopoly on EUV lithography; KLAC on process control metrology. No alternative sources exist for leading-edge nodes.
* **CapEx Cycle Leverage:** Equipment spending is a leading indicator of fab capacity expansion. The N3 squeeze and planned N2/A16 expansions are driving multi-year equipment order books. TSMC's CapEx lag (peaked only in 2025) means equipment demand stays elevated through the decade.
* **Export Controls as Ceiling:** US and Dutch export restrictions limit equipment sales to China — a structural constraint on TAM but also a competitive moat insulator for incumbents operating in unrestricted markets.

#### Watch
* TSMC CapEx guidance — leading indicator of equipment order flows
* N2/A16 node qualification timelines — gating factor for next equipment upgrade cycle
* Export control scope changes — affects China revenue ceiling for AMAT, LRCX, KLAC

### Current Status
*[TBD — needs research/synthesis]*

### Developments
*[TBD — needs research/synthesis]*

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| ASML | ASML Holding | Monopoly on EUV lithography — the single most irreplaceable tool in advanced chip manufacturing |
| AMAT | Applied Materials | Broadest equipment portfolio across deposition, etch, and inspection; most diversified revenue across node types |
| LRCX | Lam Research | Dominant in etch and deposition; high leverage to memory CapEx cycles (HBM buildout) |
| KLAC | KLA Corporation | Near-monopoly in process control and metrology; high-margin service revenue makes it the most defensive equipment play |

---

## 3. Foundries & Advanced Packaging

*Wafer fabrication and chip assembly. The physical manufacturing layer — capital-intensive, geography-concentrated, and the source of the N3 supply squeeze.*

**Investment characteristics:** Extremely capital-intensive; TSMC holds a structural moat at leading nodes; advanced packaging (CoWoS, SoIC) is a separate and increasingly critical sub-layer; geographic concentration in Taiwan is the primary systemic risk; Samsung and Intel Foundry are structurally disadvantaged but gaining share via government support and customer diversification demand.

### Structural Themes
*See `context_sectors.md` → Compute & Chips → Structural Themes (N3 Wafer Scarcity, Foundry Diversification)*

#### Watch
*See `context_sectors.md` → Compute & Chips → Watch*

### Current Status
*See `context_sectors.md` → Compute & Chips → Current Status*

### Developments
*See `context_sectors.md` → Compute & Chips → Developments (Intel 18A, Samsung 2nm, Intel EMIB-T, Industry N3 Convergence)*

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| TSM | Taiwan Semiconductor | Irreplaceable foundry moat at leading nodes; only manufacturer capable of producing the world's most advanced AI silicon at scale |
| SSNLF | Samsung Electronics | Foundry #2; gaining AI supply chain share (Tesla AI5/AI6) but yield gap vs. TSMC limits leading-edge competitiveness |
| INTC | Intel | Foundry turnaround thesis; EMIB advanced packaging is the near-term opportunity; 18A yield issues are the key risk |
| AMKR | Amkor Technology | Leading OSAT (outsourced semiconductor assembly and test); beneficiary of CoWoS packaging overflow and geographic diversification demand |
| ASX | ASE Technology | Largest OSAT globally; direct beneficiary of advanced packaging capacity outsourcing from TSMC |

---

## 4. Compute Silicon

*The chips that run AI workloads — GPUs for training and inference, CPUs for orchestration, and the custom ASICs hyperscalers are building to reduce NVDA dependency.*

**Investment characteristics:** Highest direct leverage to AI demand; NVDA has exceptional pricing power but faces long-term customer defection risk; AMD is the primary alternative; ARM is a royalty/licensing model with exposure to every custom chip built on its architecture; custom silicon (not publicly traded directly) is the structural threat.

### Structural Themes
*See `context_sectors.md` → Compute & Chips → Structural Themes (The Great Rebalance, The Inference Shift, Semiconductor Moats & Custom Silicon)*

#### Watch
*See `context_sectors.md` → Compute & Chips → Watch*

### Current Status
*See `context_sectors.md` → Compute & Chips → Current Status*

### Developments
*See `context_sectors.md` → Compute & Chips → Developments (Nvidia Vera, Arm AGI CPU, AMD-Meta, GPU Spot Exhaustion)*

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| NVDA | Nvidia | Dominant GPU+software (CUDA) ecosystem; highest leverage to AI CapEx cycle; primary risk is custom silicon displacement over a 3-5 year horizon |
| AMD | Advanced Micro Devices | Primary GPU alternative to NVDA; $100B AMD-Meta deal validates multi-year hyperscaler CapEx share; MI-series ramp is the key execution test |
| ARM | Arm Holdings | Royalty on every Arm-architecture chip shipped — including hyperscaler custom silicon built to reduce NVDA dependency; transitioning to direct silicon (AGI CPU) |
| INTC | Intel | CPU incumbency plus foundry optionality; Gaudi AI accelerators are subscale vs. NVDA/AMD; turnaround risk is high |

---

## 5. Memory Silicon

*The memory that feeds AI workloads — HBM for accelerator bandwidth, DRAM for servers, NAND for storage. Structurally elevated by AI demand but retains underlying cyclicality.*

**Investment characteristics:** Cyclical but with a structural floor from HBM demand; HBM is a high-margin, capacity-constrained product with LTA pricing; commodity DRAM and NAND retain more cycle exposure; LTA structuralization is reducing near-term cyclicality for CSP-exposed suppliers; three-player oligopoly (Micron, SK Hynix, Samsung) with SK Hynix holding the HBM technology lead.

### Structural Themes
*See `context_sectors.md` → Compute & Chips → Structural Themes (HBM Structural Crowdout, Heterogeneous Memory Architecture, Memory Market: LTA Structuralization)*

#### Watch
*See `context_sectors.md` → Compute & Chips → Watch (DRAM/NAND contract pricing)*

### Current Status
*See `context_sectors.md` → Compute & Chips → Current Status*

### Developments
*See `context_sectors.md` → Compute & Chips → Developments (HBM4 Strategy Divergence, DDR5 Margin Flip, Memory LTA Deals, SOCAMM)*

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| MU | Micron Technology | Only US-headquartered memory supplier; HBM3E ramp and DDR5 margin expansion are near-term catalysts; LTA deals reducing cyclicality |
| HXSCL | SK Hynix | HBM technology leader (primary HBM3E supplier to NVDA/Google); highest leverage to HBM demand cycle |
| SSNLF | Samsung Electronics | Memory #1 by volume but lagging SK Hynix on HBM yields; aggressive HBM4 push is the recovery thesis |

---

## 6. Networking & Custom Silicon

*Merchant networking chips, SmartNICs, and custom ASICs. The silicon that moves data within and between AI clusters — and the chip design layer hyperscalers contract to reduce NVDA dependency.*

**Investment characteristics:** Design-win driven; less directly cyclical than GPU/memory; Broadcom and Marvell are the primary custom ASIC suppliers to hyperscalers; structural growth tied to both cluster scale-up (more chips per cluster) and custom silicon adoption (more hyperscaler ASIC programs); long design-to-revenue lead times create visibility but also lag.

### Structural Themes
* **Custom Silicon Megatrend:** Hyperscalers are contracting Broadcom and Marvell to design custom AI accelerators (TPUs, Trainium, custom inference chips) to reduce NVDA dependency. ASIC share of AI server shipments forecast at 27.8% in 2026, rising to ~40% by 2030. AVGO's long-term Google agreement through 2031 and AMD-Meta deal illustrate the multi-year contracted nature of this revenue.
* **Networking as a Scaling Bottleneck:** As GPU cluster sizes grow, the networking fabric connecting accelerators becomes a primary performance constraint. Marvell and Broadcom supply the switch silicon and SerDes underlying Nvidia NVLink and Ethernet-based clusters alike.
* **Nvidia's Strategic Response:** Nvidia's $6B investment sweep across Marvell, Coherent, and Lumentum is partly defensive — ensuring its NVLink Fusion and CPO frameworks remain architecturally relevant even as hyperscalers build around NVDA silicon.

#### Watch
* Hyperscaler custom ASIC program announcements — new design wins for AVGO/MRVL
* ASIC market share vs. NVDA GPU trajectory — pace of 27.8% → 40% shift
* Broadcom-Google and Marvell design cycle timelines — revenue recognition lag

### Current Status
*[TBD — needs research/synthesis]*

### Developments
*See `context_sectors.md` → Compute & Chips → Developments (Custom Silicon Scaling: Amazon & Broadcom-Google)*

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| AVGO | Broadcom | Primary custom ASIC supplier to hyperscalers (Google TPU, Meta); long-term contracted revenue through 2031; also dominant in networking switch silicon |
| MRVL | Marvell Technology | Custom ASIC and cloud networking silicon; AWS Trainium and Azure custom chip programs; Nvidia $6B investment adds strategic validation |

---

## 7. Optical & Physical Connectivity

*The physical layer connecting AI clusters: optical transceivers, networking switches, and the fiber cables that carry traffic between and within data centers.*

**Investment characteristics:** Infrastructure lock-in via multi-year supply contracts; transceiver demand doubling in 2026; co-packaged optics (CPO) is a medium-term technology transition that could disrupt incumbents; fiber cable manufacturers are an overlooked beneficiary of the rural data center buildout.

### Structural Themes
*See `context_sectors.md` → Networking & Optical → Structural Themes*

#### Watch
*See `context_sectors.md` → Networking & Optical → Watch*

### Current Status
*See `context_sectors.md` → Networking & Optical → Current Status*

### Developments
*See `context_sectors.md` → Networking & Optical → Developments*

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| COHR | Coherent Corp | Vertically integrated optical components and transceivers; Nvidia $6B investment validates strategic position in AI interconnect stack |
| LITE | Lumentum | Optical components supplier; Nvidia strategic investment; exposure to both transceiver and CPO transition |
| AAOI | Applied Optoelectronics | Small-cap transceiver supplier; high leverage to AI cluster buildout but limited moat vs. larger competitors |
| MRVL | Marvell Technology | Networking switch silicon; also listed under Layer 6 |
| ANET | Arista Networks | Dominant data center networking switch vendor; strong position in AI cluster Ethernet fabric |
| CSCO | Cisco Systems | Incumbent networking vendor; AI cluster opportunity but legacy business creates drag |
| GLW | Corning | Dominant fiber optic cable manufacturer; direct beneficiary of rural data center fiber demand surge; overlooked vs. component plays |

---

## 8. Power Generation & Grid Equipment

*The energy infrastructure feeding AI data centers — gas turbines, fuel cells, grid equipment, and utilities. The most undertracked layer relative to the structural demand signal.*

**Investment characteristics:** Long-cycle capital equipment with multi-year order books; gas turbine lead times are already extending; AI data center power demand is a new, large, and durable demand vector layered on top of existing electrification demand; behind-the-meter generation is emerging as a separate theme as grid interconnection constraints worsen.

### Structural Themes
* **AI as a Power Demand Shock:** AI data centers require sustained, high-density baseload power that the grid cannot reliably supply in key markets. Grid moratoriums in Northern Virginia, the most established DC market, are pushing buildout to secondary markets and driving behind-the-meter generation at scale.
* **Gas Turbines as Near-Term Bottleneck:** Gas turbines are spiking in price alongside GPUs and memory — a direct signal that power generation equipment is becoming a binding constraint. GE Vernova and Siemens Energy hold the oligopoly on large-scale gas turbine manufacturing; lead times are extending.
* **Behind-the-Meter at Scale:** Oracle's 2.8GW Bloom Energy fuel cell commitment is the largest known behind-the-meter power commitment to date — a structural signal that hyperscalers are accepting higher-cost on-site generation over grid interconnection uncertainty.
* **Nuclear as Long-Term Baseload:** SMRs are the favored long-term solution for dedicated AI campus power. Cameco (uranium) and BWXT (reactor components/fuel) are the primary pure-play exposures. Commercial SMR deployments at scale remain years out.
* **Utilities with AI Exposure:** Certain merchant power generators (Vistra, Constellation) have direct AI data center power purchase agreements — a distinct thesis from equipment manufacturers.

#### Watch
* Gas turbine order book disclosures from GEV and Siemens Energy
* Behind-the-meter power commitment scale and pace
* Grid interconnection queue timelines in key markets
* SMR design certifications and first commercial deployments

### Current Status
*[TBD — needs research on GEV, Siemens Energy, BE, VST, CEG order books and AI exposure]*

### Developments
*See `context_sectors.md` → Infrastructure & Power → Developments (Gas Turbine Demand Spike, Behind-the-Meter Power) and Nuclear & Energy → Developments*

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| GEV | GE Vernova | Spinoff of GE's power and grid business; dominant gas turbine manufacturer with direct exposure to AI data center power demand; most direct public play on power generation equipment shortage |
| SMEGF | Siemens Energy | European gas turbine and grid equipment oligopolist; co-beneficiary of global AI power demand surge |
| ETN | Eaton Corporation | Power management and electrical infrastructure; inside-the-fence power distribution for data centers; also listed under Layer 9 |
| BE | Bloom Energy | Fuel cell power generation; Oracle's 2.8GW commitment is a major validation; behind-the-meter alternative to grid interconnection |
| VST | Vistra Energy | Merchant power generator with direct AI data center PPAs; nuclear and gas fleet |
| CEG | Constellation Energy | Largest US nuclear operator; direct power purchase agreements with hyperscalers (Microsoft); pure-play nuclear/clean baseload for AI |
| CCJ | Cameco | Largest publicly traded uranium producer; also listed under Layer 1 |
| BWXT | BWX Technologies | Nuclear reactor components, fuel, and services; DoD and commercial SMR exposure |

---

## 9. Data Center Infrastructure

*The physical facilities, cooling systems, and internal power delivery that house AI compute. The "execution layer" — land, power delivery, liquid cooling, and construction.*

**Investment characteristics:** Infrastructure/REIT-like characteristics for operators (DLR, EQIX); equipment suppliers (VRT, ETN, Schneider) have high leverage to cooling and power delivery capex; liquid cooling is crossing from optional to mandatory, creating a structural upgrade cycle; less than 10% of existing inventory meets AI-dense requirements — a multi-year greenfield build ahead.

### Structural Themes
*See `context_sectors.md` → Infrastructure & Power → Structural Themes*

#### Watch
*See `context_sectors.md` → Infrastructure & Power → Watch*

### Current Status
*See `context_sectors.md` → Infrastructure & Power → Current Status*

### Developments
*See `context_sectors.md` → Infrastructure & Power → Developments*

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| VRT | Vertiv Holdings | Dominant data center power and cooling infrastructure; liquid cooling transition is a direct structural tailwind; highest leverage to AI-dense facility buildout |
| ETN | Eaton Corporation | Power management and UPS systems; inside-the-fence electrical infrastructure for data centers |
| JCI | Johnson Controls | Cooling and building management systems; AI data center cooling exposure alongside legacy commercial HVAC |
| SBGSY | Schneider Electric | Power management and data center automation; European equivalent to Eaton/Vertiv in many markets |
| DLR | Digital Realty | Data center REIT; long-term lease structure benefits from AI demand shock; less AI-dense than neoclouds but stable |
| EQIX | Equinix | Colocation and interconnection REIT; network-dense facilities and carrier-neutral hubs; structural AI demand beneficiary |
| TH | Target Hospitality | Workforce housing for large construction projects; direct exposure to data center construction labor bottleneck |
| JBL | Jabil | Contract manufacturer for data center hardware and components; AI server supply chain exposure |
| NBIS | Nebius Group | European AI cloud and infrastructure; neocloud characteristics — listed separately under Layer 11 |
| CRWV | CoreWeave | *See Layer 11* |
| IREN | IREN Limited | AI compute and power infrastructure; bitcoin miner transitioning to AI workloads |

---

## 10. Hyperscalers & Cloud

*The integrated demand drivers, infrastructure builders, model developers, and platform providers. They sit at multiple layers simultaneously — buying compute, building data centers, developing models, and selling AI services.*

**Investment characteristics:** Mega-cap with diversified revenue streams; AI is both a capital cost (CapEx) and a revenue opportunity (cloud AI services); the reflexive loop benefits them most — rising stock prices fund CapEx, which generates revenue, which justifies more CapEx; competition is between themselves and with open-source; valuation risk tied to whether AI cloud revenue materializes at the pace CapEx assumes.

### Structural Themes
* **The Reflexive Loop Beneficiaries:** Hyperscalers sit at the center of the circular AI capital loop — they fund startups, who spend on cloud credits, generating revenue that justifies more CapEx. They are both the demand driver and a primary beneficiary of the buildout.
* **Vertical Integration Imperative:** Each hyperscaler is building custom silicon (AWS Trainium/Graviton, Google TPU, Azure Cobalt) to reduce NVDA dependency and capture margin. AWS estimates Trainium saves "tens of billions of capex dollars per year." This is not a supply hedge — it's a structural margin decision.
* **Platform Lock-In:** The cloud platform layer (AWS, Azure, GCP) has high switching costs for enterprise AI workloads. As enterprises embed AI into production workflows, the platform becomes sticky. The battle is for AI workload share, not just general compute.
* **Model Development Arms Race:** Google (Gemini), Meta (Llama), Microsoft/OpenAI (GPT), Amazon (no frontier model but heavy OpenAI/Anthropic customer) are all investing directly in frontier models as a platform moat.

#### Watch
* CapEx guidance and actual spend vs. prior forecasts — primary signal for AI investment pace
* Cloud AI revenue growth (AWS Bedrock, Azure OpenAI, Vertex AI) — Revenue Imperative validation
* Custom silicon adoption rate — how fast Trainium/TPU/Cobalt displace NVDA GPU spend
* Operating margin trajectory — does AI CapEx compress margins or do AI services revenue expand them?

### Current Status
*[TBD — needs synthesis of hyperscaler earnings and AI revenue metrics]*

### Developments
*[TBD — pull from context_sectors.md and earnings updates]*

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| AMZN | Amazon | AWS is the largest cloud platform; Trainium/Graviton custom silicon program is the most advanced and economically compelling; $200B 2026 CapEx driven by committed customer demand |
| MSFT | Microsoft | Azure + OpenAI partnership creates the strongest enterprise AI platform; Copilot and Azure OpenAI Service are the leading AI monetization vehicles |
| GOOGL | Alphabet | Most vertically integrated AI stack (TPUs, models, cloud, search); Google the most extreme CapEx accelerator; AI search monetization is the key near-term risk/opportunity |
| META | Meta Platforms | Largest open-source AI model (Llama); $100B AMD deal and CoreWeave contracts reflect massive infrastructure commitment; monetization via advertising AI, not cloud services |

---

## 11. Neoclouds

*Purpose-built AI compute providers — dedicated, liquid-cooled GPU clusters operated on multi-year contracts for hyperscalers and AI labs.*

**Investment characteristics:** High revenue growth and backlog visibility (multi-year contracts); high execution and financial risk (bridge financing, GPU deployment before facilities are ready); pricing power has shifted decisively to operators; less than 10% of existing data center inventory supports their workloads — structural demand for purpose-built capacity; CoreWeave's $21B Meta contract anchors the deal scale.

### Structural Themes
*See `context_sectors.md` → Infrastructure & Power → Structural Themes (The "Neocloud" AI Factories, Neocloud Financial Risk)*

#### Watch
*See `context_sectors.md` → Infrastructure & Power → Watch*

### Current Status
*See `context_sectors.md` → Infrastructure & Power → Current Status*

### Developments
*See `context_sectors.md` → Infrastructure & Power → Developments (Neocloud Market Power Shift, Long-Term Offtakes)*

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| CRWV | CoreWeave | Largest neocloud; $21B Meta contract anchors multi-year revenue visibility; execution and refinancing risk are the key risks |
| NBIS | Nebius Group | European-focused AI cloud; infrastructure and compute platform; earlier stage than CoreWeave |
| IREN | IREN Limited | Transitioning from bitcoin mining to AI compute; power infrastructure assets are the underlying value |

---

## 12. AI-Native Applications

*Software built on top of the AI stack — data infrastructure, AI agents, vertical applications, and cybersecurity. The layer that must ultimately generate the revenue to justify the infrastructure buildout.*

**Investment characteristics:** Highly varied — ranges from infrastructure-like data platforms (SNOW, MDB) to high-moat vertical AI (PLTR) to commoditizing point solutions; the Revenue Imperative test plays out here; switching costs are high for deeply integrated platforms, low for model-layer tools; disruption risk from AI coding tools applies to some incumbents in this layer.

### Structural Themes
* **The Revenue Imperative:** The application layer must ultimately generate ~$600B in revenue to justify the current infrastructure buildout. Agentic token demand and Anthropic's ARR tripling in Q1 2026 are early validation signals — but the full revenue gap has not been closed.
* **Data Moats as the Durable Edge:** Companies with proprietary, hard-to-replicate datasets (PLTR's government/enterprise data integrations, SNOW's data cloud network effects, TEM's clinical data) have the most defensible positions. Raw model access is commoditizing; proprietary data is not.
* **Cybersecurity as Non-Discretionary AI Spend:** AI is expanding the attack surface while also enabling faster threat detection. CRWD and PANW are positioned as AI-native security platforms — spending that enterprises cannot defer.
* **Vertical AI vs. Horizontal Platforms:** Vertical AI (TEM in oncology, PL in geospatial, SOUN in voice) can build deeper moats via domain-specific data and workflows. Horizontal platforms face more direct model-layer substitution risk.

#### Watch
* AI Lab ARR growth rates — pace of Revenue Imperative validation
* Token demand breadth — broad-based vs. single-player driven
* Software company debt refinancing conditions — disruption narrative becoming a credit event
* Agent workflow adoption in enterprise — leading indicator of switching cost lock-in

### Current Status
*See `context_sectors.md` → Software & Disruption → Current Status*

### Developments
*See `context_sectors.md` → Software & Disruption → Developments*

### Companies

| Ticker | Company | One-line thesis |
|---|---|---|
| PLTR | Palantir | AI platform with deep government and enterprise data integrations; AIP bootcamp model is driving rapid enterprise adoption; highest moat in the layer |
| SNOW | Snowflake | Data cloud with strong network effects; AI data platform and Cortex AI are expanding the platform moat |
| MDB | MongoDB | Developer data platform; flexible document model suits AI application data structures |
| DDOG | Datadog | AI observability and monitoring; benefits from proliferation of AI workloads needing instrumentation |
| CRWD | CrowdStrike | AI-native cybersecurity platform; Falcon platform consolidation is the thesis; non-discretionary spend |
| PANW | Palo Alto Networks | Security platform consolidation play; AI-driven threat detection; platformization strategy |
| NOW | ServiceNow | Enterprise workflow automation; AI Agents on the Now platform are the growth vector; deep enterprise integration moat |
| ORCL | Oracle | Database incumbency plus cloud infrastructure buildout; OCI is gaining AI workload share; data center construction commitments are a direct supply chain play |
| TEM | Tempus AI | Clinical AI with proprietary oncology data library; specialized data moat in healthcare |
| PL | Planet Labs | Daily satellite imagery data; geospatial AI edge case with proprietary data moat |
| SOUN | SoundHound AI | Voice AI platform; automotive and enterprise deployments |
| IBM | IBM | Hybrid cloud and enterprise AI (watsonx); legacy business drag but enterprise relationships are sticky |

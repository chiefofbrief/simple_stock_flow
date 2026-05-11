# Workflow Update Plan
*Temporary planning document — delete when changes are complete.*
*Session date: 2026-05-11*

---

## Context

Triggered by review of Howard Marks' AI bubble memo. The core diagnosis: our flow analyzes AI companies using sound best practices but does not actively interrogate AI-specific structural risks (circular revenue, debt-financed capex, leadership durability, valuation scenario dependency). Separately, the synthesis step concludes with a verdict label rather than an expected value estimate — which answers "what should I do?" but not "what am I likely to make?"

**Standing rule for all prompts:** Every prompt must give equal weight to both directions of the investment question — skeptical/downside and opportunity/upside. Unbalanced prompts produce unbalanced outputs.

---

## Status

| # | File | Status | Notes |
|---|------|--------|-------|
| 1 | `GEMINI.md` | ✅ DONE | All changes applied |
| 2 | `prompt_the_context_ai.md` | ✅ DONE | New file written and balanced |
| 3 | `prompt_the_numbers_ai.md` | ✅ DONE | All changes applied |
| 4 | `prompt_the_projection.md` | ✅ DONE | Verdict removed, EV framework added, balance applied |
| 5 | `prompt_the_projection_ai.md` | ✅ DONE | New file written |
| 6 | `context_ai_supply_chain_index.md` | 🔲 PENDING | Remove financial drift |
| 7 | `prompt_ai_supply_chain_update.md` | 🔲 PENDING | Minor clarification on index scope |

**Not changing:** `prompt_the_context.md` (base), `prompt_the_numbers.md` (base), `prompt_setup.md`, `prompt_tracker_review.md`, digest prompts.

---

## Change 1: GEMINI.md ✅ DONE

Changes applied:
- **Analytical balance** principle added (replaced Devil's Advocate tactical instruction)
- **Cross-Section Consistency** — removed tactical timing instruction, kept the principle
- **AI SC TAILWIND candidates** note added under Investment Types
- **P/E discipline + growth** paragraph added to Financials section
- **Demonstrated growth as value** paragraph added to Margin of Safety section
- **Expected Value** definition added as final paragraph of Financials section
- **Architecture** updated: `[Verdict]` → `[Assessment]`; verdict taxonomy removed; workflow table updated with AI prompt variants for Steps 1, Pass 1, Pass 2
- **Thesis Files** note updated: "Verdict" → "Assessment (Expected Value)"

---

## Change 2: `prompt_the_context_ai.md` ✅ DONE

New file written. Key decisions:
- Full AI version — not a base copy with bolt-on additions
- LOSER conditionals removed (Q8/Q9 from base)
- Supply chain index required read (not optional), actively used throughout
- Q1 — bidirectional: FOMO overestimation AND market underestimation symmetric framing
- Q3 — bidirectional: enthusiasm ahead of results OR market not pricing genuine progress
- Q11 — scenario embedded in price (new)
- Q14 — added: capex vs. revenue guidance divergence flag
- Q16 — new: path from investment to revenue (capex commitments, circular arrangements, timelines)
- Q17 — structural vs. narrative tailwind; thesis confidence ≠ investment attractiveness
- Q20 — reflexivity cycle position
- Q21 — bubble lens (overestimation)
- Q22 — underestimation lens (equal depth counterpart to Q21)
- Section 6 — added Scenario framing to hypothesis

---

## Change 3: `prompt_the_numbers_ai.md` 🔲 NEXT

**Base:** `prompt_the_numbers.md` — read before proposing changes.

**Approach:** Integrate AI structural questions into existing sections. Weave in, don't bolt on. Apply balance check before writing.

**Questions to integrate (placement TBD on review of base prompt):**
- Capex vs. revenue growth — spending ahead of demand or tracking commitments?
- Financing structure — operating cash flow, equity, or debt/SPVs/vendor financing?
- Revenue quality — related-party flows, circular transactions, vendor financing arrangements?
- Asset useful life vs. financing horizon — do the assets outlive the debt?
- Productivity → profit — are efficiency gains reaching the P&L or being competed away?

**Balance check required:** For each skeptical/risk question added, ensure there is a symmetric opportunity question. Underestimation lens applies here too — e.g., is the AI contribution to margins/revenue being undercounted?

---

## Change 4: `prompt_the_projection.md` 🔲 PENDING (all stocks)

**Decision: Remove verdict entirely. Replace Synthesis with EV framework.**

New Synthesis format:
- **Numbers** — unchanged
- **Narrative & Catalyst** — unchanged
- **Expected Value** — narrative framing ("dollar for 70 cents / dollar for a dollar / dollar for 120 cents"). Bull and bear scenarios as subcomponents, not standalone required sections. "We have no idea" is a valid answer — state it with specific reasons. Support with figures but conclusion is qualitative.
- **Invalidation** — unchanged

Pre-profitability: frame EV around probability of business model working, not EPS-derived targets.

Note: "Decision" label also removed — no forced taxonomy. EV narrative concludes the analysis.

**Balance check required** before writing.

---

## Change 5: `prompt_the_projection_ai.md` 🔲 PENDING (AI SC stocks)

**Base:** Updated `prompt_the_projection.md` (includes EV framework).

**Questions to integrate throughout existing sections (no separate AI block):**
- Capex ROI — specific return metrics and customer commitments, or self-justifying buildout language?
- Valuation scenario dependency — does the current price require an extraordinary outcome, or does it hold in commodity/slower-adoption scenario?
- Reflexivity position — installation phase or deployment phase? Does the call change this assessment?
- Financing risk — does call language raise flags not covered in The Numbers?
- Revenue sustainability — clear path to self-sustaining profit, or dependent on continued capital market access?

**Balance check required** — symmetric questions: is the call revealing AI monetization upside the market hasn't priced? Is the deployment phase closer than the market assumes?

---

## Change 6: `context_ai_supply_chain_index.md` 🔲 PENDING

**Rule:** Capex/revenue figures acceptable only when explaining a structural supply chain dynamic. Balance sheet observations, FCF, earnings quality → remove.

**Entries flagged:** GOOGL ($77.5B debt note), AMZN (TTM FCF note), ORCL (financing framing around Abilene), CRWV (debt refinancing language), MSFT ($25B component pricing note). Review all others on pass-through.

---

## Change 7: `prompt_ai_supply_chain_update.md` 🔲 PENDING

Add one line to Index editorial rules: financial metrics (balance sheet, FCF, debt levels, earnings quality) do not belong in index entries unless they directly explain a supply chain constraint or structural dynamic.

Here is the complete word-for-word proposal. Discuss before I write to any file.                                                                                   
   
  ---                                                                                                                                                                
  Context AI — 2 changes
                        
  Q9 — remove [TAILWIND] tag
                                                                                                                                                                     
  Old:
                                                                                                                                                                     
  ▎ Q9. [TAILWIND] Has price appreciation been validated by earnings growth, or is price running ahead of fundamentals?                                              
   
  New:                                                                                                                                                               
                  
  ▎ Q9. Has price appreciation been validated by earnings growth, or is price running ahead of fundamentals?

  ---
  Q20 — add installation/deployment as separate dimension
                                                                                                                                                                     
  Old:
                                                                                                                                                                     
  ▎ Q20. Where is this company in the reflexivity cycle?
  ▎ Are improving fundamentals reinforcing the narrative (early-to-mid loop), or is the narrative now running independently of fundamentals (late loop, fertile 
  ▎ fallacy territory)? Cite specific evidence from news, price action, and analyst behavior. If the evidence is ambiguous, say so.                                  
   
  New:                                                                                                                                                               
                  
  ▎ Q20. Where is this company in the reflexivity cycle, and where is it in its AI lifecycle?                                                                        
  ▎ These are two distinct questions — assess each separately.
  ▎                                                                                                                                                                  
  ▎ Reflexivity (Soros framework): Are improving fundamentals reinforcing the narrative (early-to-mid loop), or is the narrative now running independently of        
  ▎ fundamentals (late loop, fertile fallacy territory)? Cite specific evidence from news, price action, and analyst behavior. If the evidence is ambiguous, say so. 
  ▎                                                                                                                                                                  
  ▎ AI lifecycle position (Perez framework): Is the company still in the installation phase — infrastructure buildout ahead of proven demand, heavy capex and losses 
  ▎ are expected and arguably justified — or is it beginning to show deployment-phase characteristics — revenue from AI investments becoming visible, a credible path
  ▎  to profit extraction taking shape? A company can be in a justified installation phase while still in the early reflexivity loop, or generating genuine          
  ▎ deployment-phase returns while sentiment has already overextrapolated them. Name both positions and note whether they are aligned or diverging.

  ---
  Numbers AI — 7 questions rewritten, B8 strengthened
                                                                                                                                                                     
  All "For AI SC stocks:" qualifiers removed. AI content integrated into the answer template directly.
                                                                                                                                                                     
  ---             
  Part A — Revenue                                                                                                                                                   
                  
  Old answer template:
                                                                                                                                                                     
  ▎ [Analysis. For AI SC stocks: note whether deferred revenue is growing (positive forward signal) or shrinking. Does revenue growth track what is known about      
  ▎ contracted demand from the Context step? Note: circular revenue and vendor financing questions cannot be answered from financial statements alone — flag for     
  ▎ Accounting Checklist investigation if revenue quality is uncertain.]                                                                                             
                  
  New:

  ▎ [Analysis. Note whether deferred revenue is growing — a positive signal that contracted demand is building ahead of recognition — or shrinking. Assess whether   
  ▎ revenue growth tracks the scale of AI infrastructure investment underway: demand-driven revenue growth and capex-driven revenue growth have different 
  ▎ implications for durability. Revenue quality — whether growth reflects genuine external customer demand versus circular arrangements or vendor financing between 
  ▎ counterparties — cannot be determined from financial statements alone. Flag for Accounting Checklist Category 1 investigation if revenue concentration, 
  ▎ counterparty relationships, or growth patterns raise questions.]

  ---
  Part A — Capital Expenditures & D&A

  Old answer template:

  ▎ [Analysis. For AI SC stocks: (1) Is capex growing faster than revenue, and at what ratio? A company spending at 2x its revenue growth rate with no visible       
  ▎ contracted demand explanation carries different risk than one with customer commitments backing the buildout. (2) What is the implied depreciation rate for AI 
  ▎ infrastructure assets? Conservative useful life assumptions (longer lives) depress current D&A and inflate reported earnings. The risk is asymmetric: the        
  ▎ earnings benefit accumulates gradually over years; when technology is superseded the write-off is sudden. Nobody knows when AI hardware becomes obsolete — that 
  ▎ unpredictability is precisely what makes long useful life assumptions dangerous. Flag for Accounting Checklist Category 2 investigation.]

  New:

  ▎ [Analysis. Is capex growing faster than revenue — and at what ratio? A company investing at 2x its revenue growth rate without visible contracted demand         
  ▎ explanation carries different risk than one with customer commitments backing the buildout. What is the implied depreciation rate for AI infrastructure assets 
  ▎ (annual D&A ÷ gross PP&E)? Conservative useful life assumptions inflate current reported earnings by suppressing D&A; the risk is asymmetric — the earnings      
  ▎ benefit accumulates gradually over years, but when AI hardware is superseded the write-off is sudden, and nobody knows when that is. Flag for Accounting 
  ▎ Checklist Category 2 investigation.]

  ---
  Part A — Debt Profile

  Old answer template:

  ▎ [Analysis — covers Debt/Total Assets and Debt/OCF. For AI SC stocks: note whether the debt trajectory suggests leveraged buildout pacing ahead of revenue.       
  ▎ Standard ratios may understate total financial exposure if off-balance-sheet structures exist — flag for Accounting Checklist Category 3 investigation if debt 
  ▎ levels or trajectory warrant it.]                                                                                                                                
                  
  New:

  ▎ [Analysis — covers Debt/Total Assets and Debt/OCF. Note whether the debt trajectory suggests leveraged buildout pacing ahead of revenue. Standard ratios may     
  ▎ understate total financial exposure — AI infrastructure buildouts have used SPVs, VIEs, and vendor financing arrangements to move debt off balance sheet while 
  ▎ retaining operational exposure. Flag for Accounting Checklist Category 3 investigation if debt levels, trajectory, or off-balance-sheet signals warrant it.]     
                  
  ---
  Part B Q1

  Old answer template:

  ▎ [Answer. For AI SC stocks: is the operating margin trajectory consistent with AI-driven operating leverage — i.e., is revenue growth dropping more than          
  ▎ proportionally to the bottom line? This cannot be determined from financial statements alone; reference Context step findings and flag for targeted MD&A search 
  ▎ if the trend is ambiguous.]                                                                                                                                      
                  
  New:

  ▎ [Answer. Is the operating margin trajectory consistent with AI-driven operating leverage — revenue growth dropping more than proportionally to the bottom line?  
  ▎ Because the source of margin improvement (AI productivity versus other factors) cannot be isolated from financial statements alone, cross-reference the Context 
  ▎ step findings and flag for targeted MD&A search if the trend is ambiguous.]                                                                                      
                  
  ---
  Part B Q5

  Old answer template:

  ▎ [Answer. For AI SC stocks: does the capex pace reflect contracted customer demand or speculative buildout ahead of proven demand? Is the depreciation schedule   
  ▎ realistic given that AI hardware obsolescence is unpredictable — and what would a more conservative useful life assumption imply for reported earnings?]
                                                                                                                                                                     
  New:            

  ▎ [Answer. Does the capex pace reflect contracted customer demand — visible in backlog, deferred revenue, or named customer commitments — or speculative buildout  
  ▎ ahead of proven demand? Is the stated depreciation schedule realistic given that AI hardware obsolescence is unpredictable? If useful life assumptions appear 
  ▎ long relative to peers or industry norms, quantify what a more conservative assumption would imply for reported earnings.]                                       
                  
  ---
  Part B Q6

  Old answer template:

  ▎ [Answer. For AI SC stocks: do the standard ratios appear to capture the full financial exposure, or are there signals that off-balance-sheet structures, vendor  
  ▎ financing, or contingent commitments may materially change the picture?]
                                                                                                                                                                     
  New:            

  ▎ [Answer. Do the standard leverage ratios appear to capture the full financial exposure? Off-balance-sheet structures, vendor financing arrangements, and         
  ▎ contingent commitments tied to AI infrastructure buildout can materially change the true leverage picture — note whether the Accounting Checklist Category 3 
  ▎ findings alter the debt assessment from what the standard ratios show.]                                                                                          
                  
  ---
  Part B Q8 — strengthened

  Old answer template:

  ▎ [Answer. For AI SC stocks: is there evidence that AI investments are generating returns ahead of consensus expectations — through pricing power, margin          
  ▎ expansion, or contracted revenue commitments not yet visible in reported figures? Does the supply chain tier (from the index) support a case that pricing power 
  ▎ or structural demand is understated in current financials?]                                                                                                      
                  
  New:

  ▎ [Answer. Are the AI investments generating measurable financial returns? Specific signals to look for: operating margin expanding faster than revenue growth     
  ▎ (leverage materializing); deferred revenue growing faster than reported revenue (contracted demand building ahead of recognition); revenue per customer or ASP 
  ▎ increasing (pricing power); D&A declining as a percentage of revenue while capex continues (assets being deployed productively). Does the supply chain tier (from
  ▎  the index) support a case that structural demand or pricing power is understated in current reported figures — real returns not yet visible at the consolidated 
  ▎ level?]

  ---
  Projection AI — Q2, Q3, Q5, Q8, Q11 rewritten; self-check updated
                                                                                                                                                                     
  ---
  Q2 — integrate and add upside                                                                                                                                      
                  
  Old ends with:

  ▎ For AI SC stocks: does management's account confirm or sidestep the capex-to-revenue path, revenue quality, and circular arrangement questions flagged in The    
  ▎ Numbers? Where management describes revenue from counterparties who are also capital partners, infrastructure partners, or joint venture participants, note this 
  ▎ explicitly and assess whether it represents genuine external demand or a circular arrangement.                                                                   
                  
  New — full Q2 text:

  ▎ Q2. Does management's characterization of business performance align with what The Numbers established — or are there notable deflections, omissions, or         
  ▎ contradictions? Where does the call add context that the financial statements couldn't?
  ▎ Cite specific excerpts from both calls. Note where they differ from each other and where either diverges from the findings in The Numbers. Pay particular        
  ▎ attention to three things: (a) how management characterizes the capex-to-revenue path — does the account confirm or sidestep the demand visibility and investment
  ▎  cycle questions flagged in The Numbers? (b) revenue descriptions involving counterparties who are also capital partners or infrastructure partners — assess 
  ▎ whether the revenue represents genuine external demand or a circular arrangement; (c) AI monetization or deployment gains management describes that the financial
  ▎  statements couldn't capture — specific customer wins, utilization improvements, or pricing progress that materially changes the picture established in The 
  ▎ Numbers.

  ---
  Q3 — integrate and add upside

  Old ends with:

  ▎ For AI SC stocks: does capex guidance continue to pace ahead of revenue guidance, or is there language about contracted customer demand that justifies the       
  ▎ buildout? Is guidance supported by named customers, committed contracts, or specific return-on-investment targets — or is the framing self-justifying ("investing
  ▎  to meet future demand," "building for the opportunity ahead")? The distinction between contracted demand and speculative buildout is the central question.      
                  
  New — full Q3 text:

  ▎ Q3. What is management saying about the path forward — guidance figures, growth targets, margin trajectory? Where does guidance diverge from the historical trend
  ▎  established in The Numbers?
  ▎ Summarize explicit forward guidance figures. Label all as forward-looking. Where guidance implies acceleration or deceleration relative to the historical trend, 
  ▎ flag the delta. Where management cites adjusted figures, check whether the GAAP equivalent is disclosed. On the AI investment cycle specifically: is the capex   
  ▎ trajectory backed by contracted customer demand — named customers, committed contracts, specific ROI targets — or described in terms of future opportunity? The 
  ▎ former de-risks the investment thesis; the latter extends the installation phase. Also note where guidance implies AI-driven margin improvement or revenue       
  ▎ acceleration ahead of what The Numbers established — these are upside signals that materially change the EV picture.

  ---
  Q5 — integrate, balance risk and upside tracking
                                                                                                                                                                     
  Old ends with the four AI risk-tracking items.
                                                                                                                                                                     
  New — full Q5 text:                                                                                                                                                
   
  ▎ Q5. For each open question listed at the end of The Numbers — was it addressed on either call?                                                                   
  ▎ List every open question from The Numbers. For each: (a) was it addressed on either call? (b) cite what was said directly. (c) does the answer strengthen, 
  ▎ weaken, or leave the thesis unchanged? Any item not addressed must be flagged as unresolved — none carried forward silently.                                     
  ▎
  ▎ In addition, the following must be explicitly tracked regardless of whether they appeared in the open questions list:                                            
  ▎               
  ▎ Risk side: (a) Is the AI investment cycle moving toward self-funding from cash generation, or does continued growth still require ongoing external capital? (b)  
  ▎ Do off-balance-sheet structures, SPVs, or vendor financing arrangements get addressed, clarified, or avoided on the call? (c) Does management acknowledge AI 
  ▎ asset useful life and obsolescence risk, or is that topic absent? (d) Are circular arrangement flags from The Numbers accounting checklist addressed or          
  ▎ deflected?    
  ▎
  ▎ Upside side: (e) Does the call reveal AI deployment progress not visible in the financial statements — utilization rates, customer adoption metrics, or          
  ▎ contracted demand building ahead of revenue recognition? (f) Does management describe pricing power or structural demand that hasn't yet appeared in reported 
  ▎ figures? (g) Is there language suggesting the investment-to-revenue timeline is compressing — deployment closer than the financials implied?                     
  ▎               
  ▎ Flag all unresolved items in the assessment.

  ---
  Q8 — integrate and add upside
                               
  Old ends with the AI analyst-probing addition.
                                                                                                                                                                     
  New — full Q8 text:
                                                                                                                                                                     
  ▎ Q8. What does the Q&A reveal that the prepared remarks don't? Management answers under questioning often differ from the prepared narrative — surface those gaps 
  ▎ explicitly.
  ▎ Prepared remarks are managed; Q&A responses are less so. Where management's tone, specificity, or framing shifts under questioning, note it. Hedges introduced   
  ▎ only under questioning, figures disclosed only when pressed, and topics deflected rather than answered are all informative. Assess both directions: where        
  ▎ analysts probe capex ROI, revenue sustainability, financing structures, or the path to self-funding — does management become more or less specific than in 
  ▎ prepared remarks? And where analysts probe or endorse AI monetization progress, deployment acceleration, or competitive positioning — does management's tone or  
  ▎ specificity under questioning reveal more conviction than the prepared narrative suggested? Both the evasions and the endorsements under pressure are signals.

  ---
  Q11 — separate reflexivity from lifecycle
                                                                                                                                                                     
  Old:
                                                                                                                                                                     
  ▎ Q11. Is the structural thesis intact per the earnings call?
  ▎ Where is this company in the reflexivity cycle — still in the installation phase (capex building enthusiasm, revenues following at a lag), or beginning the 
  ▎ transition to the deployment phase...                                                                                                                            
   
  New:                                                                                                                                                               
                  
  ▎ Q11. Is the structural thesis intact per the earnings call?                                                                                                      
  ▎ Assess two distinct dimensions:
  ▎                                                                                                                                                                  
  ▎ Reflexivity update: Has the earnings call changed the reflexivity position established in Context? Are improving fundamentals still reinforcing the narrative —  
  ▎ or has the call revealed that sentiment has begun running ahead of what the business can support? Cite specific evidence: management tone, Q&A dynamics, guidance
  ▎  relative to expectations, and how the call's reception compares to the prior one.                                                                               
  ▎               
  ▎ AI lifecycle position: Where is this company in its AI investment cycle — still in the installation phase (infrastructure buildout, heavy capex, losses or thin  
  ▎ margins are expected), or beginning the deployment phase (revenue from AI investments becoming visible, margins expanding, a credible path to self-sustaining 
  ▎ profit taking shape)? Does the call provide specific evidence of deployment-phase progress — contracted demand, named customer wins, margin expansion from AI    
  ▎ utilization, pricing power materializing — that the market has not yet priced? Or does the call reveal the installation phase extending — capex commitments 
  ▎ growing faster than revenue visibility, guidance language shifting toward future demand rather than contracted backlog?
  ▎
  ▎ Reference both the reflexivity position and the lifecycle assessment established in Context. State explicitly whether the call confirms, strengthens, or weakens 
  ▎ each. What would confirm or break the thesis in 3–6 months?
                                                                                                                                                                     
  ---             
  Self-check — update two items
                                                                                                                                                                     
  Old:
                                                                                                                                                                     
  ▎ - Have the four AI-specific open questions been explicitly tracked through the call — self-sustaining investment cycle, off-balance-sheet structures, useful     
  ▎ life/obsolescence, and circular arrangement flags? If any were not addressed by management, have they been flagged as unresolved in the assessment?
  ▎ - Is the reflexivity/installation-vs-deployment position assessment grounded in specific call evidence — not assumed from prior steps? Has the call either       
  ▎ confirmed or shifted the framing established in Context?                                                                                                         
   
  New:                                                                                                                                                               
                  
  ▎ - Have both the risk-side and upside-side Q5 tracking items been explicitly addressed — self-sustaining investment cycle, off-balance-sheet structures, useful   
  ▎ life/obsolescence, and circular arrangement flags on the risk side; deployment progress, pricing power, and timeline compression on the upside side? Are 
  ▎ unresolved items flagged in the assessment?                                                                                                                      
  ▎ - Are the reflexivity update and the AI lifecycle position update both grounded in specific call evidence — assessed separately, not conflated? Has the call 
  ▎ confirmed or shifted each framing established in Context?                                                                                                        
   
  ---                                                                                                                                                                
  That's the full set. Does this all look right before I write to the files?
                                                                             
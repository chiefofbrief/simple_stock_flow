# MSFT News Data
**Generated:** 2026-05-10 14:08
**Date Range:** 2026-02-09 to 2026-05-10

## Summary Statistics

### Coverage
- **Perigon:** 10 stories (aggregated from 10 media items)
- **FMP:** 30 articles from 18 sources
- **Total:** 40 items

### Time Distribution
| Month | Perigon | FMP |
|-------|---------|-----|
| 2026-05 | 10 | 10 |
| 2026-04 | 0 | 10 |
| 2026-03 | 0 | 10 |

### Sentiment Distribution

**Perigon** (avg composite: +0.053)
- Positive-leaning: 4 stories
- Neutral: 0 stories
- Negative-leaning: 6 stories

---

## Perigon Stories (10 stories)

### 2026-05-10 | AI arms race expected free cash flow dip
**Sentiment:** -0.20 (pos: 0.26, neg: 0.47, neu: 0.27)

Big Tech’s AI buildout is shifting Alphabet, Amazon, Meta, and Microsoft from cash generators toward heavy infrastructure spenders, as capex for data centers, chips, servers, and power takes a growing share of operating cash. Analysts say free cash flow is set to plunge to the lowest levels not seen since 2014, with Morgan Stanley estimating hyperscalers could spend roughly $805 billion this year and as much as $1.1 trillion next year. Wall Street forecasts also project combined free cash flow for Amazon, Alphabet, Microsoft, and Meta around $4 billion in the third quarter, down sharply from much higher post-COVID averages. The strain is already visible in specific companies’ actions—Amazon is expected to burn cash and has large planned 2026 spending, while Meta has issued significant debt and paused buybacks. Even as Alphabet remains free-cash-flow positive, it’s doing so at its weakest level in more than a decade and has reduced repurchases, underscoring that investors are increasingly judging whether AI spending will convert into future cash. Overall, analysts view the cash pressure as temporary, hinging on AI-driven revenue growth that could improve cash generation later.

**Key Points:**
- Morgan Stanley’s estimate for AI-related spending explicitly includes Oracle alongside Amazon, Alphabet, Meta, and Microsoft—hyperscalers “could spend nearly $805 billion this year” (up from an earlier $765 billion projection).
- The scale of the planned AI buildout is so large that Morgan Stanley-linked commentary says 2026 spending would be “roughly equal to what all non-tech companies in the S&P 500 spent combined in 2025,” with the expected ~$800B in 2026 “nearly double the 2025 levels and about three times what was spent in 2024.”
- Amazon’s cash drain is quantified: Visible Alpha estimates a roughly “$10 billion cash burn,” and the firm is projected to spend more cash than it generates this year; additionally, its announced “plans to invest $200 billion in 2026” are described as the largest among peers.

---

### 2026-05-10 | CVE-2026-26129 Copilot Business Chat reported data exposure
**Sentiment:** -0.05 (pos: 0.22, neg: 0.27, neu: 0.52)

Multiple newly flagged vulnerabilities across Microsoft AI agent/assistant deployments and several third-party web applications present high, attacker-friendly paths to data exposure and account/session compromise. In Microsoft 365 Copilot Business Chat, attackers may be able to trigger information disclosure through largely permissionless probing of widely used chat sessions, with risk rising where many users (including partners) can initiate sessions that reference internal or regulated content. Separate guidance warns that publicly reachable M365 “published agents” could allow remote privilege elevation that expands beyond agent interfaces into broader tenant/service permissions via changed scope and shared connectors. A public proof-of-concept for remote SQL injection in a pharmacy sales and inventory system is rated priority 1 because it can enable manipulation or extraction of operational data once the internet-facing endpoint is reached. Stored XSS in DivvyDrive is also treated as priority 1, since malicious payloads persist and execute whenever authenticated users view affected pages, potentially enabling session theft or account takeover within impacted browser contexts. Across all cases, the recommended response is rapid vendor patching paired with compensating controls like restricting or disabling exposed agent features, enforcing least-privilege and safer query practices, and tightening web input handling and monitoring.

**Key Points:**
- For publicly reachable Microsoft 365 “published agents,” Redpacket Security’s guidance includes concrete monitoring/detection steps: look for spikes in agent execution/management API calls from new IPs or service principals, and alert on changes to agent permission scopes or agent configuration by atypical identities; it also recommends patching first via staging validation before wider rollout.
- For Copilot Business Chat information disclosure, the article adds that defenders should correlate tenant logs with “new or anomalous client IP/user agents” initiating chat sessions at volume, and—if possible—inspect for content-type anomalies in assistant outputs such as unexpected document excerpts.
- In the pharmacy sales/inventory remote SQL injection case, the compensating-control example is specific: add WAF rules targeting `ajax.php?action=save_user` and enforce strict input validation for `id`; the hunting guidance also calls for SQL error patterns and response-time spikes tied to crafted inputs.

---

### 2026-05-10 | DekaBank adds 150,000 Microsoft shares
**Sentiment:** +0.20 (pos: 0.36, neg: 0.16, neu: 0.47)

Recent 13F filings show continued institutional interest in Microsoft, with multiple asset managers increasing or initiating positions across the latest reporting periods. Hendershot Investments, Argo Wealth Advisory, Means Investment, and DekaBank Deutsche Girozentrale all reported added stakes, with Microsoft remaining a top holding for several of them. The filings also reflect broad participation by large investors, including major moves by Norges Bank, Nuveen, and UBS Asset Management, while overall institutional ownership is reported at about 71% of the company’s shares. Other reports indicate a two-way flow—thousands of institutional investors added shares while thousands reduced positions—underscoring that enthusiasm is paired with selective trimming. Microsoft insider activity during the past six months leaned toward sales rather than purchases. Analyst coverage cited in the reports remains broadly bullish, including reiterated “buy” calls and higher price targets from research firms.

**Key Points:**
- Hendershot Investments raised its Microsoft stake 5.4% in the fourth quarter—buying an additional 3,296 shares to total 64,291 shares. Microsoft was 4.0% of Hendershot’s portfolio, the fund’s 7th-largest holding, worth about $31.092 million.
- Argo Wealth Advisory initiated a new Microsoft position in the fourth quarter, purchasing 8,121 shares valued at approximately $3.928 million. Microsoft accounted for about 2.3% of Argo’s portfolio, making it the fund’s 11th-largest holding.
- UBS Asset Management Americas disclosed a sharp Microsoft increase: UBS AM A boosted its stake by 500.0% during the third quarter, rising to 59,543,261 shares after adding 49,618,571 shares (reported value: about $30.84 billion).

---

### 2026-05-10 | Nebius stock rallies on $643M Eigen AI
**Sentiment:** +0.74 (pos: 0.77, neg: 0.04, neu: 0.19)

Nebius Group has agreed to acquire Eigen AI for about $643 million, aiming to fold Eigen’s inference optimization technology into its Token Factory to shift from infrastructure services toward a higher-value Platform as a Service model with more recurring revenue. The company says the move is supported by a $2 billion equity investment from Nvidia and by multi-year, multi-billion dollar AI infrastructure and platform agreements with Meta and Microsoft. Nebius’s planned data center expansion is positioned to capitalize on these contracted commitments, which also deepen its access to GPU supply channels. In financial markets, NBIS shares opened around $177 and traded near their 52-week high, with analysts listing a “Moderate Buy” consensus. Still, one view highlights that execution risk remains: heavy capital expenditures and losses could persist if capacity utilization and operating leverage don’t translate into durable GAAP profitability. Investors are watching upcoming results closely to judge whether the contracted backlog turns into scalable, cash-generating performance.

**Key Points:**
- Institutional ownership in Nebius has risen to 21.9%, with Mitsubishi UFJ Asset Management increasing its stake by 230.6%.
- Nebius says its data center expansion includes a planned 310 megawatt facility in Finland, tying the GPU-supply and capacity buildout directly to the new platform push.
- The Meta and Microsoft agreements were described with specific headline sizes—about $27 billion for Meta and about $19.4 billion for Microsoft—raising both the potential for utilization/ARR and the execution bar for margins as deployments scale.

---

### 2026-05-10 | 2026 AI glossary released by TechCrunch
**Sentiment:** -0.15 (pos: 0.20, neg: 0.35, neu: 0.45)

As AI tools move from novelty to core business infrastructure, several outlets are publishing updated “glossaries” to help non-specialists understand the jargon that now dominates tech conversations. The TechCrunch-linked guide focuses on the practical mechanics behind modern systems, defining terms such as large language models, hallucinations, inference, and training/correction approaches like retrieval-augmented generation and reinforcement learning from human feedback. Other versions of the glossary frame the same problem at a higher level, clarifying concepts like artificial general intelligence, which different major groups define somewhat differently, and “AI agents,” described as tools that can carry out multistep tasks using multiple technologies. The materials also simplify developer building blocks such as API endpoints, likening them to software “buttons” that integrations and agents can invoke. Across the sources, the goal is consistent: demystify what the words mean, reduce confusion—even among experts—and keep the reference current as the field evolves.

**Key Points:**
- TechCrunch says it released its “massive glossary” on May 9 to translate machine-learning jargon into “plain English,” specifically targeting the backend mechanisms behind the tools people use every day.
- A separate glossary push referenced in the coverage (from CNET) frames the need for clarity around “hallucinations” by emphasizing that readers must understand “exactly why a system makes things up.”
- The glossary material connects core terms to real-world deployments by tying the under-the-hood vocabulary to named assistants/models: OpenAI’s ChatGPT, Anthropic’s Claude, Google’s Gemini, Meta’s Llama, Microsoft’s Copilot, and Mistral’s Le Chat.

---

### 2026-05-10 | Microsoft begins Xbox Mode rollout Windows 11 PCs
**Sentiment:** +0.17 (pos: 0.35, neg: 0.18, neu: 0.48)

Microsoft is rolling out “Xbox Mode” (formerly the full-screen experience/FSE) to Windows 11 PCs—starting in selected markets and on a staggered basis—so the interface works like a console for desktops, laptops, tablets, and handheld PCs. The feature replaces the traditional desktop with a controller-first, full-screen gaming dashboard that minimizes background distractions/notification clutter and can be toggled back to the normal Windows desktop. Xbox Mode is designed to pull game libraries into one place, combining Xbox Game Pass with storefronts such as Steam, Epic Games Store, EA Play (and, in some descriptions, Ubisoft Connect) while allowing controller-friendly browsing and launching. Access is offered through Settings > Gaming > Xbox mode and via shortcuts like Windows + F11, with Microsoft also surfacing the option through the Xbox app and Game Bar to keep it easy to reach. The update is tied to Microsoft’s broader Project Helix effort and had been tested in Xbox/Windows Insider builds before reaching stable users via KB5083631 on Windows 11 24H2 and 25H2, though rollout can be uneven and multi-monitor support may have issues; one report also claims the UI can reduce memory use by about 1–2GB on tested hardware. (https://www.qoo10.co.id/en/tech/94045/windows-11-gets-xbox-mode-a-full-screen-console-interface-pushes-the-desktop-aside/; https://www.qoo10.co.id/en/tech/93883/microsoft-expands-xbox-mode-across-windows-11-pcs-bringing-a-console-like-gaming-experience/; https://pokde.net/system/software/operating-system/xbox-mode-windows-11; https://assets.thehansindia.com/technology/tech-news/microsoft-brings-console-like-xbox-mode-to-windows-11-pcs-and-tablets-1072000; https://www.business-standard.com/technology/tech-news/full-screen-experience-xbox-mode-available-windows-11-pc-tablet-126050400323_1.html)

**Key Points:**
- Microsoft says Xbox Mode is meant to make PCs feel like dedicated game machines by providing quick access not only to installed titles and Game Pass, but also to cloud gaming.
- For the initial rollout, Microsoft has not disclosed which specific regions will receive Xbox Mode first, only that it is launching in selected markets.
- One report compares Xbox Mode to Steam’s Big Picture, describing it as a controller-first, console-style UI on Windows 11 that minimizes reliance on keyboard and mouse for browsing and launching games.

---

### 2026-05-10 | Trump plans H-1B wage hike, $18B cost
**Sentiment:** -0.30 (pos: 0.18, neg: 0.48, neu: 0.34)

President Trump’s administration is proposing major increases to the required minimum wages for H-1B and PERM visas, including raising the entry-level qualifying salary for roles such as a software engineer to about $162,000 in San Francisco, $132,000 in New York, and $113,000 in Dallas—nearly 30% higher than current thresholds. The Department of Labor proposal would also change how “prevailing wages” are calculated by moving the anchor for entry-tier pay from the 17th percentile to the 34th, with larger jumps higher up the wage levels. An analysis cited by the report estimates the rule could cost H-1B-using employers at least $18 billion in the first 12 months, rising to as much as $43 billion annually within three years, and supporters argue the changes are meant to stop foreigners from undercutting American wages. But the higher salary floors could deter hiring and reduce opportunities for younger or less-established talent, as employers may choose not to sponsor visas that become more expensive. The effect would stack with other immigration-cost changes already underway, including a $100,000 fee for new H-1B petitions that a federal judge upheld after industry and state challenges.

**Key Points:**
- The Department of Labor’s proposed prevailing-wage change was released on March 27, and the proposal would reset not just entry-level pay but the entire wage ladder by shifting the entry-tier anchor from the 17th percentile to the 34th percentile.
- The rule would be especially steep for senior roles: DOL projected that Level IV (senior-tier) wages would jump by moving the anchor from the 67th to the 88th percentile—such as a Level IV data scientist in Silicon Valley potentially seeing the wage floor rise by more than $45,000, with some occupation/metro combinations reaching or exceeding $208,000.
- In explaining the wage proposal, the administration said H-1B visa holders are “generally offered about $10,000 less a year” than their U.S. counterparts, arguing the program is being used in ways that undercut domestic workers.

---

### 2026-05-10 | Global AI use rises; adoption divide widens
**Sentiment:** -0.27 (pos: 0.30, neg: 0.57, neu: 0.13)

Microsoft’s Global AI Diffusion Report finds that generative AI use rose to 17.8% of the world’s working-age population in the first quarter of 2026, up from 16.3% previously, with 26 economies now exceeding 30% adoption. However, the report says the adoption gap is widening between developed and developing countries, with 27.5% usage in developed economies versus 15.4% in the developing world. Microsoft attributes the divide to uneven access to internet connectivity, basic digital skills, and electricity, alongside lingering model-performance advantages in English that slow adoption in many non-English-speaking regions. The UAE leads global adoption at 70.1%, followed by Singapore, Norway, Ireland, and France, while the United States ranks 21st at 31.3% despite hosting major AI models such as ChatGPT, Claude, and Gemini; China is reported at 16.4%, and some data is missing for parts of the world where Microsoft’s telemetry coverage is limited. Microsoft says its estimates rely mainly on Windows and Microsoft-linked products and partially miss Apple device usage, but it also points to improving support for Asian languages as a driver of momentum in parts of Asia. On jobs, the company argues AI coding tools could increase demand for developer work, while cautioning it is too early to determine AI’s full labor-market impact.

**Key Points:**
- Microsoft reported a sharp rise in developer activity: “Git pushes … rose 78 percent year over year,” which it cited as evidence of increased coding activity alongside generative AI tools.
- For its estimates, Microsoft said it relied on anonymized telemetry data and made adjustments for “differences in OSes, device market share, Internet access and country populations,” adding that it continues refining its measurement approach.
- Microsoft said some regions were missing from its consolidated data, naming Russia, Iran and China as areas where reporting was incomplete.

---

### 2026-05-10 | TCLBANKER trojan targets 59 platforms via WhatsApp,Outlook
**Sentiment:** -0.27 (pos: 0.12, neg: 0.39, neu: 0.48)

Elastic Security Labs says the Brazilian banking trojan TCLBANKER (REF3076) is a major update to earlier LATAM malware families and is delivered via a trojanized Logitech installer that abuses the legitimately signed Logi AI Prompt Builder using DLL side-loading. After installation, it includes both a banking credential-theft module targeting 59 banking, fintech, and crypto sites and a worm component that propagates through victims’ WhatsApp and Microsoft Outlook accounts. The malware is engineered to evade analysis and automated detection by using sandbox/anti-debug checks, disabling ETW telemetry and security hooks, and applying environment fingerprinting plus multiple geofencing signals to confirm the target is in Brazil. Once active, it monitors browser activity in near real time to detect targeted sites and uses full-screen WPF overlays to imitate login and update screens while enabling additional remote-control and data-collection capabilities. For propagation, the WhatsApp module hijacks existing authenticated WhatsApp Web sessions in Chromium-based browsers, copies session artifacts, bypasses bot protections, and then uses the victim’s contacts to send phishing messages, while the Outlook component similarly leverages authenticated access to spread further.

**Key Points:**
- TCLBANKER’s delivery chain includes a malicious MSI bundled inside a ZIP, and its DLL loader uses the filename “screen_retriever_plugin.dll,” masquerading as a legitimate Flutter plugin. Elastic also reports the installer deploys two embedded .NET Reactor-protected payloads (the banking trojan module and the worm module).
- The malware contains a “comprehensive watchdog subsystem” that scans for analysis tooling and terminates immediately if detected—Elastic lists targets including x64dbg, Ghidra, dnSpy, IDA Pro, Process Hacker, Frida, and CheatEngine. Additionally, the malicious DLL only executes when loaded by specific processes (e.g., “logiaipromptbuilder.exe” or “tclloader.exe”).
- Elastic details the ETW tampering technique: the loader patches “EtwEventWrite” using the instruction sequence “xor eax, eax; ret” and generates direct syscall trampolines to bypass security hooks, rather than relying solely on higher-level evasion.

---

### 2026-05-10 | Alphabet market value nears Nvidia No.1
**Sentiment:** +0.67 (pos: 0.76, neg: 0.10, neu: 0.14)

Alphabet is moving quickly toward overtaking Nvidia as the world’s most valuable company after a surge in its stock, driven by accelerating AI monetization and a rebound in Google Cloud. Following its latest earnings, Alphabet’s market cap jumped to about $4.67T—bringing the gap with Nvidia to roughly $200B and narrowing to a point where some analysts see Alphabet as likely to take the top spot by mid-May. The shift is tied to strong cloud growth (up about 63% in the first quarter), record acceleration since 2020, and rapidly growing revenue from generative-AI–based products, alongside steady YouTube ad strength and a growing subscription base. Investors also view Alphabet as benefiting from “measurable” AI demand converting into recurring services, while Nvidia’s valuation has been more vulnerable to broader AI supply-chain sentiment—after reporting and market coverage raised concerns about end-demand predictability around major AI buyers like OpenAI. Overall, multiple accounts frame this as a broader transition from an AI chip race to a full-stack contest in which cloud, software, and custom hardware can capture more of the value chain than chips alone.

**Key Points:**
- Alphabet’s custom AI chips have moved beyond pilots: CEO Sundar Pichai said Google has begun selling its custom AI processors directly to some customers, and those chips “have already been used by Anthropic,” according to one report interpreting Alphabet’s earnings backdrop.
- Nvidia’s recent market-pressure was not attributed to weaker results from the chipmaker itself: one report said Nvidia posted $68.1 billion in revenue for its latest quarter and that its data center revenue rose 75%—while sentiment shifted after coverage tied to end-demand predictability around major AI buyers.
- Hightower Advisors’ Stephanie Link tied the stock rerating to AI infrastructure spending dynamics—saying the move was “really about hyperscaler capex spend” and “early signs of better monetization,” especially versus the broader AI ‘food chain,’ which includes “data centers, grid and power.”

---

## FMP Articles (30 articles)

### 2026-05-10 | Microsoft's African data center falters on payment demands, Bloomberg News reports
**Source:** Reuters
**URL:** https://www.reuters.com/world/africa/microsofts-african-data-center-falters-payment-demands-bloomberg-news-reports-2026-05-10/

A Microsoft data center site in East Africa ​has been delayed by ‌disagreements with the Kenyan government over the company's request ​for guaranteed payments, Bloomberg ​News reported on Sunday citing ⁠people familiar with the ​matter.

---

### 2026-05-10 | The AI Threat Google Couldn't Mount: Why This Expert Says Microsoft's $70 Billion Cash Cow Is Vulnerable Now
**Source:** 24/7 Wall Street
**URL:** https://247wallst.com/investing/2026/05/10/the-ai-threat-google-couldnt-mount-why-this-expert-says-microsofts-70-billion-cash-cow-is-vulnerable-now/

On the We Study Billionaires podcast (episode TIP813), Stig Brodersen laid out a bear case that puts Microsoft's Office cash cow squarely in the crosshairs of generative AI.

---

### 2026-05-10 | Chip Stocks Are Soaring While Software Slows. Is a Reversal Looming?
**Source:** 24/7 Wall Street
**URL:** https://247wallst.com/investing/2026/05/10/chip-stocks-are-soaring-while-software-slows-is-a-reversal-looming/

The 2026 tape has split in two. Semiconductor stocks have ripped higher on AI infrastructure demand, while software names that powered the last cycle have stalled or rolled over.

---

### 2026-05-10 | SCHB and SPTM Are Both Excellent Broad Market Funds. Here's How to Choose.
**Source:** Fool - Investing News
**URL:** https://www.fool.com/coverage/etfs/2026/05/10/schb-and-sptm-are-both-excellent-broad-market-funds-here-s-how-to-choose/

Both ETFs charge just 0.03%, but differ in holdings, sector weightings, and risk profiles. See how their approaches impact long-term portfolio construction.

---

### 2026-05-09 | Great News for Microsoft Stock Investors
**Source:** The Motley Fool
**URL:** https://www.fool.com/investing/2026/05/09/great-news-for-microsoft-stock-investors/

Microsoft's (MSFT 1.33%) management team said the magic words every shareholder loves to hear.

---

### 2026-05-09 | Paul Tudor Jones Warns Trump-Era Market Boom Could End in a 35% Crash. Here’s Why He’s Still Buying Stocks
**Source:** 247 Wallst
**URL:** https://247wallst.com/investing/2026/05/09/paul-tudor-jones-warns-trump-era-market-boom-could-end-in-a-35-crash-heres-why-hes-still-buying-stocks/

Wall Street has embraced the return of pro-growth economic policies, lighter regulation, and an AI spending boom, helping push U.S. stocks to record territory again under President Donald Trump. Yet as warning signs pile up, legendary investor Paul Tudor Jones says the same forces driving markets higher today may also be laying the groundwork for... Paul Tudor Jones Warns Trump-Era Market Boom Could End in a 35% Crash. Here's Why He's Still Buying Stocks

---

### 2026-05-09 | Amazon CEO Andy Jassy Has Good News and Bad News for Nvidia Investors
**Source:** Fool - Investing News
**URL:** https://www.fool.com/investing/2026/05/09/amazon-ceo-andy-jassy-has-good-news-and-bad-news-f/

Amazon is seeing accelerating demand for AI services, but it's not all going to Nvidia.

---

### 2026-05-09 | BlackRock's Larry Fink Says AI Is Creating a New Trillion Dollar Asset Class — And Trump's Policies May Accelerate It
**Source:** 24/7 Wall Street
**URL:** https://247wallst.com/investing/2026/05/09/blackrocks-larry-fink-says-ai-is-creating-a-new-trillion-dollar-asset-class-and-trumps-policies-may-accelerate-it/

Artificial intelligence has already reshaped the stock market.

---

### 2026-05-09 | MSFT's Place in a Shifting AI Landscape
**Source:** Schwab Network
**URL:** https://www.youtube.com/watch?v=vu6ySvbGcj0

Microsoft (MSFT) is standing out as a defensive AI leader, leveraging its enterprise scale and infrastructure investments to stay competitive, according to Jed Ellerbroek. He highlights strong Azure growth, steady positioning in AI chips versus Nvidia (NVDA) and Micron (MU), and strength extending into cyclicals like United Rentals (URI) as infrastructure demand builds.

---

### 2026-05-09 | Microsoft: The Best Time To Buy Is When Others Continue To Ignore
**Source:** Seeking Alpha
**URL:** https://seekingalpha.com/article/4901917-microsoft-best-time-to-buy-when-others-continue-to-ignore

Microsoft Corporation continues to grind at the bottom of the valley, trading at just 22.7x forward earnings, close to a 5-year low. MSFT maintains robust FCF margins near 20%, with adjusted EPS growth expected to average 15% over the next two years despite AI investment headwinds. What slowdown? Azure is still projected to deliver 39.5% growth in the current quarter, and Copilot adoption rose 33% quarter-over-quarter, highlighting ongoing monetization potential.

---

### 2026-04-10 | The Best Quantum Computing Stocks to Buy Today
**Source:** The Motley Fool
**URL:** https://www.fool.com/investing/2026/04/10/the-best-quantum-computing-stocks-to-buy-today/

Pure play IonQ holds the world record for the most accurate quantum computing. Microsoft and Alphabet serve as excellent legacy quantum investing alternatives.

---

### 2026-04-10 | Microsoft Azure Still Poised To Crush Estimates Despite $150 Billion Spending Fears: Analyst
**Source:** Benzinga
**URL:** https://www.benzinga.com/analyst-stock-ratings/reiteration/26/04/51761533/microsoft-azure-still-poised-to-crush-estimates-despite-150-billion-spending-fears-analyst

Slowinski said on Thursday that investors are increasingly scrutinizing how Microsoft allocates constrained GPU capacity across internal initiatives and external customers, including AI model development.

---

### 2026-04-10 | Microsoft Seen Gaining From Copilot, Azure Momentum
**Source:** GuruFocus
**URL:** https://www.gurufocus.com/news/8787062/microsoft-seen-gaining-from-copilot-azure-momentum

Microsoft (MSFT, Financials) has been stuck in an awkward spot lately. Investors still believe in the company's long-term AI position, but they also want cleare

---

### 2026-04-10 | Live Nasdaq Composite: Market Recovery Underway Amid Economic Tailwinds
**Source:** 247 Wallst
**URL:** https://247wallst.com/investing/2026/04/10/live-nasdaq-composite-market-recovery-underway-amid-economic-tailwinds/

Live Updates The analyst who called NVIDIA in 2010 just named his top 10 AI stocks Wall Street is pouring billions into AI, but most investors are buying the wrong stocks. The analyst who first identified NVIDIA as a buy back in 2010 - before its 28,000% run - has just pinpointed 10 new AI... Live Nasdaq Composite: Market Recovery Underway Amid Economic Tailwinds

---

### 2026-04-10 | Why Citi Is Betting on Palantir and Microsoft as the Software Stock Slump Refuses to Let Up
**Source:** Barrons
**URL:** https://www.barrons.com/articles/palantir-microsoft-software-stocks-slump-cec95b4d

The firm downgrades a handful of software stocks including Docusign, Autodesk, and Veeva Systems.

---

### 2026-04-10 | The 'Mag 7' Just Became The 'Lag 7': Analyst
**Source:** Benzinga
**URL:** https://www.benzinga.com/analyst-stock-ratings/analyst-color/26/04/51752126/the-mag-7-just-became-the-lag-7-analyst

On CNBC Squawk Box, Craig Johnson of Piper Sandler said the market remains "bullish, but with a lowercase b," expects roughly 5% upside, and sees better opportunities outside the "Mag 7," favoring rotation into sectors like energy over big tech.

---

### 2026-04-10 | Microsoft: Temporary CapEx Panic Masks The Long-Term Edge
**Source:** Seeking Alpha
**URL:** https://seekingalpha.com/article/4889744-microsoft-stock-temporary-capex-panic-masks-the-long-term-edge

Microsoft is rated a strong buy at $374.33, with Wall Street mispricing its AI-driven transformation and temporary FCF compression. MSFT's shift to agentic AI orchestration, custom silicon (Maia 200/Cobalt 200), and the M365 E7 suite positions it to absorb SaaS budget consolidation and defend margins. Risks include $281B OpenAI concentration, potential seat deflation from autonomous agents, and possible re-rating if forced into power generation.

---

### 2026-04-10 | Microsoft Corporation $MSFT Shares Sold by Allspring Global Investments Holdings LLC
**Source:** Defense World
**URL:** https://www.defenseworld.net/2026/04/10/microsoft-corporation-msft-shares-sold-by-allspring-global-investments-holdings-llc.html

Allspring Global Investments Holdings LLC decreased its position in Microsoft Corporation (NASDAQ: MSFT) by 1.3% in the undefined quarter, according to its most recent filing with the Securities and Exchange Commission. The fund owned 3,442,207 shares of the software giant's stock after selling 45,657 shares during the quarter. Microsoft comprises about 2.6% of

---

### 2026-04-10 | Rep. Cleo Fields Purchases Shares of Alphabet Inc. (NASDAQ:GOOG)
**Source:** Defense World
**URL:** https://www.defenseworld.net/2026/04/10/rep-cleo-fields-purchases-shares-of-alphabet-inc-nasdaqgoog.html

Representative Cleo Fields (Democratic-Louisiana) recently bought shares of Alphabet Inc. (NASDAQ: GOOG). In a filing disclosed on April 07th, the Representative disclosed that they had bought between $1,001 and $15,000 in Alphabet stock on March 16th. The trade occurred in the Representative's "MORGAN STANLEY - E*TRADE #2" account. Representative Cleo Fields also recently made the following

---

### 2026-04-10 | Prediction: These Will Be the 5 Largest Companies in the Stock Market by 2030
**Source:** The Motley Fool
**URL:** https://www.fool.com/investing/2026/04/10/prediction-these-will-be-the-5-largest-companies-i/

Nvidia should stay atop the market cap rankings if artificial intelligence infrastructure spending holds up. If AI spending increases to the degree that some projections predict, Broadcom and Taiwan Semiconductor could make their way onto the list of the world's five biggest companies.

---

### 2026-03-11 | Microsoft plans to ship prototype of next Xbox console to developers in 2027
**Source:** CNBC
**URL:** https://www.cnbc.com/2026/03/11/microsoft-plans-to-ship-prototype-of-next-xbox-to-developers-in-2027.html

Microsoft's next-generation game console will feature AMD silicon, as did the Xbox Series X and Series S from 2020, an executive said on Wednesday. Jason Ronald, a vice president in Microsoft's Xbox division, said in a blog post that the new console "delivers an order of magnitude leap in ray tracing performance and capability.

---

### 2026-03-11 | Microsoft's brief in Anthropic case shows new alliance and willingness to challenge Trump administration
**Source:** GeekWire
**URL:** https://www.geekwire.com/2026/microsofts-brief-in-anthropic-case-shows-new-alliance-and-willingness-to-challenge-trump-administration/

Microsoft filed a friend-of-the-court brief in Anthropic's lawsuit against the Department of War, urging a judge to block the Pentagon's supply chain risk designation.

---

### 2026-03-11 | Microsoft backs Anthropic in legal fight over Pentagon AI ban
**Source:** Proactive Investors
**URL:** https://www.proactiveinvestors.com/companies/news/1088744

Microsoft Corp (NASDAQ:MSFT) has filed a legal brief supporting Anthropic in its challenge to the Pentagon's designation of the AI company as a “supply-chain risk,” which effectively barred it from federal contracts. The Department of Defense ended all contracts with Anthropic last month after the company refused to remove safeguards limiting military use of its AI model, Claude, including restrictions on mass surveillance and fully autonomous weapons.

---

### 2026-03-11 | The Big 3: BIDU, JETS, MSFT
**Source:** Schwab Network
**URL:** https://www.youtube.com/watch?v=a_2QRV4Y9-o

"It's going to get downright crazy" when it comes to market moves, says @Theotrade's Don Kaufman, urging investors to keep your heads on a swivel for the remainder of the trading week. As for his Big 3, he leans bearish on Baidu (BIDU) and Microsoft (MSFT) but bullish on the U.S. Global Jets ETF (JETS) after the airline industry's strong sell-off.

---

### 2026-03-11 | 2 Stocks That Will Be Worth More Than Apple by 2028
**Source:** The Motley Fool
**URL:** https://www.fool.com/investing/2026/03/11/2-stocks-that-will-be-worth-more-than-apple-2028/

Alphabet and Microsoft are growing faster than Apple. Both companies produce more net income than Apple.

---

### 2026-03-11 | AmeriTrust CEO on scaling used vehicle leasing as it targets $1T auto finance market
**Source:** Proactive Investors - Finance
**URL:** https://www.proactiveinvestors.com/companies/news/1088741/ameritrust-ceo-on-scaling-used-vehicle-leasing-as-it-targets-1t-auto-finance-market-1088741.html

AmeriTrust Financial Technologies Inc (OTCQB:AMTFF, TSX-V:AMT) CEO Jeff Morgan talked with Proactive's Stephen Gunnion about the company’s strategy to scale...

---

### 2026-03-11 | Microsoft Trades at a Premium P/S: Buy, Sell or Hold the Stock?
**Source:** Zacks Investment Research
**URL:** https://www.zacks.com/stock/news/2882372/microsoft-trades-at-a-premium-p-s-buy-sell-or-hold-the-stock?cid=CS-STOCKNEWSAPI-FT-analyst_blog|most_popular_stocks-2882372

MSFT trades at a premium P/S despite strong cloud growth and Copilot expansion, as rising AI capex and slowing Azure growth push investors toward a Hold stance.

---

### 2026-03-11 | Why Jefferies thinks Supermarket Income REIT is worth buying after solid update
**Source:** Proactive Investors - Finance
**URL:** https://www.proactiveinvestors.com/companies/news/1088713/why-jefferies-thinks-supermarket-income-reit-is-worth-buying-after-solid-update-1088713.html

Jefferies has reiterated its 'buy' rating on Supermarket Income REIT PLC (LSE:SUPR, OTC:SUPIF), the London-listed grocery property investor, with a 90p...

---

### 2026-03-11 | Stock Market Today: Major Indexes Mixed After Inflation Data Matches Expectations; Oil Sits Near $85 With IEA Set to Decide on Releasing Reserves
**Source:** Investopedia
**URL:** https://www.investopedia.com/stock-market-today-dow-jones-s-and-p-500-031126-11923524

Major stock indexes were mixed after an important reading on consumer inflation Wednesday, while oil prices hovered near $85 a barrel ahead of an International Energy Agency decision on whether to release strategic reserves to stabilize prices.

---

### 2026-03-11 | Microsoft backs Anthropic in Pentagon blacklist battle, urges temporary restraining order
**Source:** CNBC Television
**URL:** https://www.youtube.com/shorts/bdKecS3noXE

Microsoft threw its support behind Anthropic on Tuesday, saying a judge should issue a restraining order that would block the Pentagon's designation of the artificial intelligence giant as a supply chain risk "for all existing contracts."

---

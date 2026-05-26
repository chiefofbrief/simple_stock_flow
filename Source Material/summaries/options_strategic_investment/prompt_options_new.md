# prompt_options_new.md
## Options Implementation — New Position
### For Use After Thesis Completion on {TICKER}

---

## Role and Purpose

You are conducting an options implementation analysis for **{TICKER}**. A thesis has
already been completed. Your purpose is to determine the most appropriate way to
express that thesis — whether through outright stock purchase, an options structure,
or a combination — and to produce a specific, actionable recommendation with full
cost and expected return calculations.

This is not a mechanical filter. It is an analytical process that synthesizes the thesis,
current market data, and options pricing into a recommendation. The recommendation
may be to simply buy the stock. That is a valid and sometimes correct output.

**This prompt is for new positions only.** No stock or options position is currently
held. If a position is already held, use `prompt_options_existing.md` instead.

**Default position size: $5,000 net options outlay** (premium paid minus any premium
received). This reflects the general principle that no more than 15% of risk capital
should be committed to call buying at any one time — the $5,000 default is a risk
management constraint, not an arbitrary limit. Override only if explicitly instructed,
with stated justification.

---

## Step 1: Gather Inputs

Read the following before doing anything else. Do not proceed to Step 2 until all
inputs are confirmed present.

### 1A: From the Thesis File

Read `Data/tickers/{TICKER}/{TICKER}_Thesis.md` in full. Extract and state
explicitly:

**Price and target:**
- Current stock price
- Bear case price (or range)
- Base case price (or range) and implied upside %
- Bull case price (or range) and implied upside %
- Expected value narrative (e.g., "dollar for 70 cents")

**Catalyst and timing:**
- Catalyst type (earnings, re-rating, macro, structural)
- Catalyst timing: specific date if known, or estimated window
- Catalyst timing certainty grade from the thesis (e.g., A / B / C, or High /
  Moderate / Low)

**Holding period:**
- Expected holding period stated in the thesis (e.g., "12–18 months")

**Dividend:**
- Dividend status: yes / no
- Approximate annual yield if applicable

**Expected move character:**
- Does the thesis imply a moderate re-rating over time, or a large rapid move
  driven by a hard catalyst?

**Invalidation conditions:**
- Extract the specific thesis-wrong conditions from the Synthesis section.
  These become the basis for the mental stop in the recommendation.

**Critical framing:** The gap between "right on the stock" and "right on the call"
is timing. A thesis that plays out over 18 months on a 9-month call is a loss
regardless of how correct the fundamental analysis is. The call buyer must have
a view on *when* the market will recognize what the thesis already knows — not
just *that* it will. Positive fundamentals can take months or years to be
recognized. Call buying compresses that timeline into the life of the option.

### 1B: Market Data Required

The following must be present before analysis begins. If any item is missing,
stop and request it before proceeding.

| Data Item | Source |
|---|---|
| Full options chain (calls and puts, strikes ±20% of current price, all expirations from ~3 months to furthest LEAPS available) | CBOE: cboe.com/delayed_quotes/{ticker}/quote_table — set Options Range to "All," pull all expirations |
| For each contract: Last, Bid, Ask, IV, Delta, Theta, Vega, Volume, Open Interest | Same CBOE chain |
| Historical volatility stack: 10-day, 20-day, 50-day, 100-day HV | Marketchameleon, Barchart, or equivalent |
| IV percentile (52-week) and IV 52-week low and high | Marketchameleon or equivalent |
| Current T-bill rate (90-day) | Treasury.gov or equivalent |

**Data check:** Confirm all required market data is present before proceeding.
If the options chain covers fewer than three expirations, stop and request it.
If HV data is unavailable, note this explicitly and proceed with IV as the sole
volatility reference.

---

## Step 2: Define the Structure Menu

Identify which structures are viable for this situation. Every analysis includes
outright stock purchase as one option. Eliminate structures that clearly do not
fit before running calculations — but note that cost calculations in Step 3 may
surface a structure as the only workable option even if it would not be a first
choice on other grounds.

State which structures are on the menu and briefly note why any were eliminated.
Proceed to Step 3 with surviving structures only.

### Structure A — Buy Stock Outright

Always on the menu. The baseline against which all options structures are
compared. Most appropriate when options premiums are expensive relative to the
expected move, the holding period is open-ended, or simplicity is the priority.

**Capital efficiency check:** Before committing full capital to stock purchase,
compare the total cost against simply buying the equivalent call. Long stock
requires full capital; the equivalent call requires only the premium. When
long-term stock ownership is not a requirement, the call is often the more
capital-efficient structure.

### Structure B — Long Call (Outright Purchase)

The primary options vehicle. On the menu unless IV is above the 70th percentile
AND the range width is narrow (less than 15 percentage points absolute), making
premium cost prohibitive relative to the expected move. Requires no margin account.

**Three legitimate use cases:**
1. Upside leverage with limited dollar risk — particularly for volatile names
   where full stock ownership would expose too much capital to downside.
2. Placeholder while awaiting capital — buy calls now, exercise when full
   capital arrives.
3. Participation with a price condition — willing to own the stock only if it
   proves capable of rallying to a target level.

### Structure C — LEAPS Call as Stock Substitute

On the menu only if: a deeply ITM LEAPS call exists with little or no time
premium (2 points or less), AND the stock price makes 100-share ownership
impractical within the position size limit.

**Before recommending Structure C, run the substitution decision rule:**
1. Complete the full substitution calculation (Section 3H).
2. Find the implied cost of the embedded protection.
3. Check the actual market price of the LEAPS put at the equivalent strike.
4. If the put price is less than the implied cost of protection → buy the put
   and keep the stock. It is cheaper, retains dividends, avoids the tax event,
   and sidesteps the wash sale issue.
5. If the put price is greater → the substitution may be more economical.

In practice, the put almost always wins for dividend-paying stocks with
meaningful cost basis. The substitution strategy is primarily useful when the
stock is at a loss and pays no dividend.

**Dividend correction for dividend-paying stocks:** Before evaluating whether
the LEAPS call is fairly priced, apply Fisher Black's two-step correction:
(1) subtract the present value of expected dividends before expiration from the
stock price and compute the theoretical call value; (2) compute the theoretical
call value assuming expiration just before the last ex-dividend date. Use the
higher of the two resulting values. Any options analytics platform applies this
automatically — confirm it is being used.

**Four caveats — address all before recommending Structure C:**
1. Does the stock sale generate a taxable capital gain?
2. Does buying the call while still holding the stock constitute a wash sale?
3. Does the company pay a dividend that will be forfeited?
4. Does the target LEAPS call trade at or near parity (≤2 points time premium)?
   This is the necessary condition for the economics to work.

### Structure D — Bull Call Spread

On the menu only if: the outright call cost for a meaningful number of contracts
genuinely exceeds $5,000 AND IV is above the 50th percentile.

**Bull spreads are confirmed inferior in expected return studies under the
fat-tail distribution.** Include only when cost constraints make the outright
call genuinely unworkable, and flag this explicitly in the recommendation.

**Pre-trade commission check:** Before evaluating any bull spread, calculate
the full round-trip commission cost on both legs (open and close). Include
commissions in the net debit formula. If commissions make maximum profit
negligible, the spread should not be entered regardless of the thesis.
Spreading fewer than 5 contracts typically makes commissions uneconomic as
a percentage of maximum profit.

**Short strike distance screen:** Before any other spread evaluation, calculate
2× the ATM call's time value premium. The short strike must sit within this
distance of the current stock price. If the only workable spread requires a
short strike beyond this threshold, maximum profit is a low-probability outcome
— the spread is not viable for this thesis.

**Timing constraint:** Bull spreads are not for quick moves. Spread differential
widens mainly as a function of time, not rapid price movement. On a quick move
— even a moderate one — the outright call outperforms. The spread's advantage
grows the longer the stock takes to reach the target. If the expected move is
large and fast, buy the call outright.

### Excluded Structures

Naked puts or calls on individual stocks, calendar spreads, covered call writing
on new positions, diagonal spreads (buy LEAPS call, sell near-term OTM call),
and any structure with undefined or very large downside risk.

**On diagonal spreads specifically:** Do not sell near-term OTM calls against
a long LEAPS call as a cost-reduction hedge. Above the short strike, the short
option's delta can exceed the long option's delta — the position becomes net
short the market above that level. A spread that loses money when the stock
rises is not a bull spread.

---

## Step 3: Run the Numbers

Run all calculations simultaneously for every structure on the menu, across a
range of strikes and expirations. Do not pre-select a strike before running
the numbers — let the calculations surface the optimal contract.

Write the full analysis to `Data/tickers/{TICKER}/{TICKER}_Options.md` as you
generate it, section by section. When all calculations are complete, present
**only the Structure Comparison Table and the Recommendation** in chat.

### 3A: IV and Volatility Assessment

Complete this before any cost or expected return work.

**What "time value premium" actually represents:** What is conventionally called
"time value premium" is a function of both time remaining and implied volatility
— not time alone. A high premium on a near-term option may reflect elevated IV,
not just duration. This distinction matters when comparing option prices across
strikes and expirations.

**Check 1 — IV regime:**

| IV Percentile | Range Width | Interpretation |
|---|---|---|
| < 30th percentile | > 20 pts absolute | Favorable for buyers: IV expansion may contribute alongside stock appreciation. Structural entry advantage. |
| < 30th percentile | < 15 pts absolute | Low percentile but expansion potential limited. Not expensive but IV tailwind is modest. |
| 30th–70th percentile | Any | Neutral. Expected return calculations determine attractiveness. |
| > 70th percentile | Any | Elevated premium. IV headwind: a flat stock with falling IV can produce a loss even without an adverse move. Consider whether stock purchase is more cost-effective. |

The range matters as much as the percentile. A 5th-percentile reading with a
39%–45% absolute range offers negligible expansion potential. A 5th-percentile
reading with a 25%–80% range offers a substantial potential tailwind. Always
check both.

**For LEAPS specifically:** Buy LEAPS when both implied volatility AND interest
rates are low. Both inflate LEAPS call prices independently over a 2-year holding
period. When either is elevated, the buyer is paying a premium unrelated to the
stock thesis. Interest rate and dividend sensitivity for LEAPS is far larger than
for short-term options — see the LEAPS section of the Interpretive Reference.

**Check 2 — HV stack shape:**

- Stack slopes down from longer to shorter periods (10-day is the lowest):
  stock has been quieting. Options likely cheap relative to recent history.
  Favorable for buyers.
- Stack slopes up from longer to shorter periods (10-day is the highest):
  volatility currently elevated. Options may be expensive relative to
  longer-term norm. Caution for buyers.
- Stack is flat: neutral.

Note: violent back-and-forth price action produces a higher HV reading than
a straight-line move of the same magnitude. A high 10-day HV reading may
reflect choppiness rather than a directional trend.

**Check 3 — Select the conservative volatility input:**

Use the **lowest reading in the HV stack** as the volatility input for all
expected return and probability calculations. This biases the analysis against
the buy decision. If the position looks attractive under this pessimistic
assumption, it has genuine margin of safety.

Exception: if the stock has been in distress or unusually volatile for more
than 100 days, use the long-lookback median: compute the 20-day, 50-day, and
100-day HV at each historical point over the past 600–1,000 trading days and
use the median of those calculations. This counterbalances recent episodic
behavior. Note: volatilities are unstable no matter how carefully computed —
the long-lookback median mitigates the problem; it does not solve it.

**State the selected volatility input explicitly before proceeding.**

**Check 4 — Composite IV and relative cheapness within the chain:**

When the options chain provides individual IV for each contract, compare each
option's individual implied volatility against the composite IV (weighted by
volume and distance from ATM, with near-zero weight given to deeply ITM or
OTM options). The contract whose individual IV is lowest relative to the
composite is the relatively cheap option within the chain — prefer it over
one that merely looks cheap on absolute premium. Do not buy an option simply
because its absolute premium is low; buy the one that is cheap relative to
where the stock's volatility actually is.

**Check 5 — Volatility skew:**

Check for skew before selecting a strike:
- *Vertical skew* (lower strikes carry higher IV than higher strikes): OTM puts
  are expensive relative to ATM puts. When the vertical skew is steep, compare
  cost per unit of protection explicitly before defaulting to the first OTM strike.
- *Horizontal skew* (elevated IV on options expiring just after a known event):
  near-term options carry inflated premium relative to longer-dated ones. If IV
  is elevated near a binary event, the expected IV contraction after the event
  is a headwind for buyers entering now.

**Check 6 — Is low IV exploitable or structurally justified?**

Before treating low IV as a structural entry advantage, assess the reason:
- *Exploitable:* IV is low because the stock is depressed, out-of-favor, or
  under a temporary sentiment overhang. The business characteristics are
  unchanged. Buying calls in this environment captures two potential tailwinds
  — stock price appreciation and IV expansion.
- *Structurally justified:* The business has permanently changed and future
  price movement will genuinely be smaller. Low IV may be correct and should
  not be bought on a volatility basis alone.

The fundamental thesis answers this question directly. If the stock is cheap
due to a temporary overhang or unrecognized catalyst, low IV is exploitable.
If the business has permanently deteriorated, low IV may be correct.

**Check 7 — IV spike warning signals:**

Before entering on an IV spike, assess whether it reflects public information
or possible insider activity. Two warning signals suggest the market is pricing
in a corporate event — meaning entry at that point means buying peak IV just
before resolution:
1. Dramatic volume increase propagating across multiple strikes and expirations
   simultaneously.
2. Simultaneous IV spike combined with a rising stock price.

The combination of expensive options AND a rising stock price is the key tell.
The better entry was before the spike. An IV spike following a known public
event (earnings miss, broad sector selloff) is analyzable and may represent
an entry opportunity — the information is symmetric. An IV spike with
simultaneous stock price rise and unusual cross-chain volume should be avoided.

### 3B: Liquidity Screen

Before calculating anything, eliminate illiquid contracts:
- Open interest below 100 contracts, OR
- Bid-ask spread exceeds 10% of the midpoint: (ask − bid) / midpoint > 0.10

Note any contracts eliminated. Proceed with surviving contracts only.

Low open interest means wide spreads and difficult exits — especially critical
for a 3–12 month position that may need to be rolled or exited early. Liquidity
at the specific strike and expiration matters more than headline volume on the
stock itself.

### 3C: Strike and Expiration Range

Evaluate all surviving contracts across strikes from approximately 15–20% below
to 15–20% above the current stock price, across all available expirations from
~3 months to the furthest LEAPS.

**Delta by holding period — use as the primary guide to strike selection:**

| Holding Period | Target Delta | Rationale |
|---|---|---|
| Short-term (1–2 weeks) | > 0.80 | Option must respond to every move in the underlying |
| Intermediate (weeks to 2 months) | ~0.50–0.60 | Less exact timing; position must survive larger swings |
| Long-term / fundamental thesis (months, uncertain timing) | Lower delta acceptable | Duration matters more than delta at entry; LEAPS appropriate |

The shorter the strategy, the higher the delta should be. For a multi-month
fundamental thesis with wide timing uncertainty, buying sufficient duration is
more important than delta at entry.

**Default priors — use as starting points, let calculations confirm or override:**

| Situation | Default Prior |
|---|---|
| Uncertain timing, moderate expected move (most value investor situations) | ATM or first ITM; 6–9 month minimum expiration |
| High timing certainty, large rapid move expected | First OTM; 3–6 months |
| LEAPS (12+ months) | First OTM often competitive — compare explicitly with ITM |
| IV above 70th percentile | Wider strikes if using spread; or lean toward stock purchase |

**ATM vs. ITM vs. OTM — the core trade-off:**

Time value premium is largest when the stock is at the strike and falls in both
directions. Key relationships:
- ATM: carries the most time value — you pay the most for time at the strike.
- Slightly ITM: time value drops modestly while intrinsic value picks up real
  stock exposure. Reduces time value exposure without giving up meaningful
  upside leverage.
- Deeply ITM: mostly intrinsic value, low time premium, near stock-like
  exposure. Can trade at a discount to intrinsic value in extreme cases —
  check this before assuming the LEAPS substitution is economical.
- OTM: pure time premium; requires a large move before any intrinsic value
  accumulates.

**The slow-grind risk for OTM calls:** A stock grinding up moderately on an
OTM call can produce a loss even with a correct directional thesis. If XYZ
rises from 65 to 68 slowly, the OTM July 70 call may lose money before
expiration because time decay exceeds modest intrinsic value accumulation —
while the ITM July 60 call is definitively profitable. OTM calls require both
direction and speed. Default to ITM or ATM for value investor situations with
uncertain timing.

**For LEAPS strike selection specifically:** The flat delta curve reverses the
ITM default from short-term calls. An ATM 2-year LEAPS has delta ~0.70; the
first OTM may have delta ~0.50 at roughly half the price — competitive on
percentage return per dollar invested. Compare explicitly rather than defaulting
to ITM. This logic applies only to the first OTM strike; deeply OTM LEAPS have
near-zero delta and should be avoided.

**Thesis scenario cross-check:** After identifying candidate strikes, verify
that the break-even at expiration falls within or below the thesis base case
price range. A break-even above the base case requires the bull case to be
correct just to recover premium — flag this explicitly if it occurs.

### 3D: Cost Calculation

For each contract under evaluation:
Entry cost per contract  = Ask price × 100
Contracts within $5K     = floor($5,000 ÷ (Ask × 100))
Total outlay             = Contracts × Ask × 100

Use the **ask price** for conservative cost estimation. In execution, enter a
limit order at the midpoint of bid and ask. For spreads:
Net debit        = Long leg ask − Short leg bid
Total outlay     = Net debit × 100 × number of spreads

Never use last sale prices for cost estimation — use bid and ask only. Last
sale prices do not determine actual spread execution price; the only way to
determine the market price for a spread is from the bid and ask of both options.

### 3E: Break-Even Calculations
Long call break-even at expiration   = Strike + Premium paid per share
Bull spread break-even               = Lower strike + Net debit
Bull spread maximum profit           = Higher strike − Lower strike − Net debit

**Dividend adjustment:** For dividend-paying stocks, adjust the effective stock
price downward by expected dividends over the option's life before calculating
break-even. The call is priced as if the stock were already at the
ex-dividend-adjusted level — the call buyer does not receive dividends and the
market discounts them accordingly.

Break-even at expiration is the worst-case measure. The position can be
profitable before expiration if the stock moves favorably and/or IV expands.

### 3F: Expected Return Calculation

Run for each contract under evaluation. This is the core quantitative output.

**Required inputs:**
- p = current stock price
- v = conservative volatility input from Step 3A (annualized)
- t = realistic holding period in years — use expected exit horizon from the
  thesis, not the expiration date (most positions are exited before expiration)
- Standard deviation assumption: **0.7** — this is the correct default for a
  conservative buyer. Using 1.0 standard deviation is excessive: there is only
  approximately a 16% probability of a stock moving at least one full standard
  deviation over a fixed period. At 0.7 standard deviations, the probability
  is approximately 25% — more realistic and more honest about what the
  calculation actually reflects.

**Step 1 — Time-period volatility:**
$$v_t = v \times \sqrt{t}$$

**Step 2 — Upside stock target:**
$$q_{up} = p \times e^{(0.7 \times v_t)}$$

**Step 3 — Estimate call price at upside target.**
Use greeks as a shortcut for pre-expiration estimates:
$$\text{Call}_{up} \approx \text{Current call price} + (\Delta \times \text{stock move up})$$
For a conservative estimate, assume IV stays flat — no IV expansion credit
applied. If the upside target moves past expiration, use intrinsic value plus
a small residual time value estimate.

Note on the delta shortcut: this is an approximation that degrades for large
expected moves or long time horizons. For LEAPS positions or when the upside
target implies a large stock move, use Black-Scholes at the target stock price
with reduced time remaining (original expiration minus the holding period) for
a more accurate estimate. Any options analytics platform computes this directly.

**Step 4 — Percentage profit:**
$$\text{\% profit} = \frac{\text{Call}_{up} - \text{Entry price}}{\text{Entry price}}$$

**Step 5 — Downside stock target:**
$$q_{down} = p \times e^{(-0.7 \times v_t)}$$

Note: downside distance is slightly smaller than upside due to lognormal
distribution properties.

**Step 6 — Estimate call price at downside target:**
$$\text{Call}_{down} \approx \text{Current call price} + (\Delta \times \text{stock move down})$$

**Step 7 — Percentage loss:**
$$\text{\% loss} = \frac{\text{Entry price} - \text{Call}_{down}}{\text{Entry price}}$$

**Step 8 — Reward/risk ratio:**
$$\text{Reward/risk} = \frac{\text{\% profit}}{\text{\% loss}}$$

Interpretation:
- > 1.5: Attractive for a conservative buyer
- 1.0–1.5: Marginal; weigh against simplicity of stock purchase
- < 1.0: Unattractive at this strike/expiration; evaluate adjacent contracts

**Step 9 — Probability of profit.**

Primary method — formal lognormal probability:
$$P(\text{above strike}) = 1 - N\left(\frac{\ln(\text{strike} / p)}{v_t}\right)$$

Use delta as a quick sanity check only. The formal formula gives the probability
of expiring in-the-money at the endpoint only. The probability of the option
trading in-the-money at *any point* before expiration is materially higher — a
19% endpoint probability corresponds to approximately a 33% "ever" probability.
For a call buyer who intends to sell before expiry, the "ever" probability is the
relevant figure. Treat the endpoint probability as a minimum estimate, not the
complete picture. The fat-tail distribution widens this gap further.

**Step 10 — Simple expected profit.**

Default probability weights — these are symmetric; adjust only if the thesis
provides specific reason to deviate (e.g., a strong directional asymmetry from
the thesis scenario analysis):
- P(up) = 0.25 (the 0.7σ upside move has ~25% probability)
- P(down) = 0.25 (symmetric)
- P(flat) = 0.50 (the most common outcome)

Flat scenario call price estimate:
$$\text{Call}_{flat} \approx \text{Current price} - (\theta \times \text{days in holding period})$$

$$\text{Expected profit} = (P_{up} \times \text{\% profit} \times \text{Outlay})
+ (P_{flat} \times \text{flat gain/loss} \times \text{Outlay})
- (P_{down} \times \text{\% loss} \times \text{Outlay})$$

$$\text{Expected return} = \frac{\text{Expected profit}}{\text{Outlay}}$$

**Step 11 — Repeat for all contracts under evaluation.**

Produce two ranked lists and write to file:
- **Aggressive list:** ranked by % profit (Step 4) — surfaces ATM or slightly
  OTM calls
- **Conservative list:** ranked by reward/risk ratio (Step 8) — surfaces ITM
  calls

**Three limitations apply to all probability calculations:**
1. The output is heavily biased by the volatility input — use the conservative
   rule (lowest HV reading). The results are only as reliable as the input.
2. The lognormal distribution understates large moves by 12–20 times at the
   tails. The three-scenario framework is a practical simplification. Where the
   decision is close, use a fat-tail Monte Carlo simulation — most options
   analytics platforms provide this directly.
3. The formula gives endpoint probability only. The probability of the option
   touching a price at any point during its life is materially higher. No single
   number should be treated as a precise forecast — the goal is a calibrated
   sense of whether risk/reward is genuinely attractive across a range of
   assumptions.

**Note on ranking across multiple stocks:** Never rank by equal assumed
percentage moves. A volatile stock has a much higher probability of moving 10%
than a non-volatile stock. Assume each stock moves in line with its own
volatility; rank by expected return per dollar invested.

### 3G: Position Vega Check

For each structure, state the position vega explicitly:
Position vega = Contracts × 100 × Individual vega (from chain)

- **Positive position vega** (long calls): benefits from IV expansion. Correct
  when IV is low and the thesis involves a catalyst that may drive both price
  and volatility higher. An IV spike simultaneously mitigates losses if the
  stock declines — the crash cushion. This crash cushion is strongest at
  low-IV entry and absent at high-IV entry.
- **Negative position vega** (bull spreads): hurt by IV expansion. Appropriate
  only when IV is already elevated and expected to fall. If IV is low at entry,
  negative vega works against the position even if the stock moves favorably.
  When a thesis resolves quickly and violently — the scenario where fundamental
  work pays off most rapidly — the outright call captures the IV spike as a
  bonus; the spread is hurt by it.

If position vega sign does not match the IV environment, flag this explicitly.

### 3H: LEAPS Substitution Calculation (Structure C Only)

Run only if Structure C survived Step 2 and the substitution decision rule
favors substitution over buying the put outright.
Stock sale proceeds (if substituting from existing holding)    $___
Less stock commission                                         −$___
Cost of LEAPS call (ask × 100)                               −$___
Less option commission                                        −$___
Total credit balance (to be placed in T-bill)                  $___
Annual T-bill interest on credit balance                        +$___
Costs of switching:
Time value premium of LEAPS call                           −$___
Annual dividend forfeited (if any)                         −$___
Total commissions                                          −$___
Net annual cost of substitution = Total costs − T-bill interest  $___

The freed capital must be placed in a T-bill or 1-year CD — this locks in the
rate used in the calculation and prevents the freed cash from being deployed
elsewhere in a way that negates the protection.

---

## Step 4: Synthesize and Recommend

With all calculations written to file, produce the synthesis. This is a judgment
that weighs cost, structure, timing, thesis alignment, and follow-up burden
together — not a summary of calculations.

### 4A: Structure Comparison Table

Surface in chat:

| Structure | Contracts | Total Outlay | Max Loss | Break-Even | Reward/Risk | Position Vega | IV Alignment | Follow-Up Burden |
|---|---|---|---|---|---|---|---|---|
| Stock purchase | 100 shares | $X | Full stock cost | Purchase price | N/A | N/A | N/A | Low |
| [Structure B — specific contract] | | | | | | | | |
| [Other surviving structures] | | | | | | | | |

### 4B: Recommendation

Surface in chat. Address each of the following explicitly:

**Structure and rationale:** Why this structure fits this thesis better than
the alternatives. Reference timing certainty, IV regime, position vega
alignment, and the thesis expected value narrative.

**Thesis alignment check:** Does the break-even fall within the thesis base
case price range? Does the expiration cover the thesis holding period without
requiring a roll? State both explicitly.

**Contract specifics:**
- Strike price and expiration date
- Number of contracts (within $5K default, or state the override and reason)
- Total outlay at the ask; realistic execution at the midpoint
- Break-even price at expiration

**What the position requires:** What must the stock do, and over what
timeframe, for this position to be profitable? Reference the thesis base case
price specifically — e.g., "the thesis base case of $X implies approximately
Y% profit on this position if reached by [date]."

**What breaks the position:** At what stock price does the position become a
loss worth cutting? State the technical level that serves as the mental stop
— based on the stock chart, not the option price. Cross-reference against
the thesis invalidation conditions where applicable.

**What was not chosen and why:** Briefly state why the next-best alternative
was passed over.

---

## Step 5: Self-Check

Verify the following before presenting anything in chat. If any answer is no,
revise before presenting.

- Were all thesis inputs extracted and stated explicitly, including bear/base/
  bull case prices, catalyst timing grade, holding period, and invalidation
  conditions?
- Is all required market data present? Were any missing items flagged?
- Was the IV assessment (all 7 checks) completed before any cost calculations?
- Was the conservative volatility input explicitly stated and used throughout?
- Was a liquidity screen applied before calculating expected returns?
- Were calculations run across a range of strikes and expirations — not
  pre-selected?
- Does the position vega sign match the IV environment? If not, was this flagged?
- Was the reward/risk ratio calculated for each contract evaluated?
- Does the recommended contract fit within the $5K default, or was the override
  stated and justified?
- Were break-even, probability of profit, and expected return all stated for the
  recommended contract?
- Was the LEAPS substitution decision rule applied if Structure C was on the
  menu, with all four caveats addressed?
- Does the break-even fall within the thesis base case price range? Was this
  stated explicitly?
- Does the expiration cover the thesis holding period? Was this stated explicitly?
- Was the recommendation stated with a specific strike, expiration, contract
  count, and total outlay — not just a structural description?
- Was the full analysis written to file before anything was surfaced in chat?

**STOP. After surfacing the Structure Comparison Table and Recommendation in
chat, wait for explicit user approval before treating the recommendation as
final or logging anything to the Stock Tracker.**

---

---

# INTERPRETIVE REFERENCE

---

## On Implied Volatility

**IV is the only unknown in the option pricing equation.** All other inputs are
observable. Getting the IV assessment right matters more than picking the exact
strike.

**IV is a poor predictor of actual volatility.** The market systematically
underestimates large moves because traders anchor toward middle-of-the-road
estimates — extreme predictions are more likely to be wrong, so market-makers
bias toward the center of the historical range. Large moves in either direction
are chronically underpriced. The investor who does the fundamental work to
identify a large move before the market prices it in is buying options that
will, in retrospect, have been too cheap.

**Volatility buying is a contrarian strategy.** The best entry conditions are
when option sellers are aggressive, buyers are timid, and IV has been pushed to
a trough by supply/demand dynamics with no fundamental basis. This is precisely
the environment that accompanies a depressed, out-of-favor stock — the value
investor's natural hunting ground.

**IV expansion can overcome weeks of time decay.** A stock at 100 that goes
nowhere for a month while IV rises from 20% to 26% leaves a 3-month ATM call
essentially unchanged in value. At high IV entry (80%+), IV must rise to 99%+
just to offset one month of decay.

**The range matters as much as the percentile.** A 5th-percentile reading with
a 39%–45% absolute range offers negligible expansion potential. A 5th-percentile
reading with a 25%–80% range offers a substantial potential tailwind. Always
check both.

**LEAPS IV operates in a narrower absolute range than short-term options.**
Near-term options may range from 14% to 40% in IV; LEAPS from 17% to 32%.
A LEAPS at the 20th percentile of its own range may look cheap, but that range
spans only 15 percentage points. Do not expect large vega gains from a LEAPS
position even at a low IV percentile. For LEAPS, the primary profit driver is
stock price appreciation. The IV expansion benefit is more relevant for
shorter-dated calls.

**Panic drops often spike IV simultaneously.** In a rapid stock decline,
implied volatility frequently rises — partially offsetting the option's loss
from the stock move. This crash cushion is strongest at low-IV entry and absent
at high-IV entry.

**Put and call IV are linked.** Put and call IV at the same strike cannot
diverge for long — conversion arbitrage enforces alignment. A spike in put IV
pulls call IV up with it, and vice versa.

---

## On Time Decay

**At 3+ months remaining, time decay is not the primary enemy.** Theta is small
relative to delta and vega at this duration. Theta only dominates in the final
weeks. This is why the default is 6–9 month minimum expirations — it keeps the
position on the flat part of the decay curve.

**The square root rule governs relative pricing.** A 9-month option does not
cost three times a 3-month option — it costs approximately √3 times as much in
time premium. Longer-dated options are proportionally cheaper per unit of time.
Buying duration is efficient, not expensive.

**Check the HV stack shape as a quick pre-entry screen.** A downward-sloping
stack (10-day lowest, 100-day highest) means the stock has been quieting —
options are likely cheap relative to recent history. An upward-sloping stack
means volatility is currently elevated — a caution flag for buyers entering
into a spike rather than a trough. Note: violent back-and-forth price action
produces a higher HV reading than a straight-line move of the same magnitude.
A high 10-day HV reading may reflect choppiness rather than a directional trend.

**Roll before the curve bends.** Decay accelerates sharply at approximately
6 months remaining for ATM options and approximately 12 months remaining for
OTM options. These are mandatory roll triggers for LEAPS positions.

**The four-variable trap.** The interplay of stock price, strike, time, and
volatility can work against each other simultaneously. A rising stock price
pushes a call up while decreasing time drives it down. The core risk for a
thesis-driven call buyer: if the thesis plays out slowly — the stock grinds up
rather than moves decisively — time decay can eat premium faster than intrinsic
value accumulates, especially on OTM calls. This argues for: buying calls with
sufficient time remaining, not going too far out of the money, and having a
view on *when* the thesis will be recognized, not just *that* it will.

**Cumulative LEAPS decay is real despite small daily rates.** An 18-month ATM
LEAPS loses approximately 25% of its value in 6 months on a flat stock. Do not
be misled by the small daily number.

---

## On Strike Selection

**Delta is the primary guide — not absolute price.** A cheap OTM call requires
a large move just to break even. The correct comparison is reward per dollar
invested at the expected stock move, using delta to estimate the option's
response.

**For LEAPS, the delta curve is flat — do not assume ITM dominates.** A LEAPS
ATM call has delta ~0.70; the first OTM call may have delta ~0.50 at half the
price. The OTM call gains approximately 70% as much per stock move but costs
50% as much — competitive on percentage return. Compare explicitly rather than
defaulting to ITM. This logic applies only to the first OTM strike.

**ITM for moderate expected moves; OTM for large expected moves.** A value
investor thesis recovering to fair value (moderate re-rating) favors ITM. A
thesis with a hard catalyst driving a large move may favor the first OTM strike
on percentage return grounds.

**The slow-grind risk is real.** A stock grinding up modestly on an OTM call
can produce a loss even if the thesis is correct. The OTM call requires both
direction and speed. When timing is uncertain, the ITM call is more forgiving.

---

## On LEAPS Specifically

**Use a model, not your eyes.** A 2-year LEAPS with eight times the time
remaining of a 3-month call sells for only about four times as much —
confirming the square root rule. The LEAPS does not look cheap just because it
costs less than 8× the short-term call. Price it properly before drawing
conclusions.

**Interest rates and dividends are major factors for LEAPS.** For short-term
options these are rounding errors. For LEAPS, a ½% rate change moves an ATM
2-year call by ~0.55 points; a $0.25/quarter dividend change moves an ITM
2-year call by ~1.50 points. Condensed sensitivity reference:

| Variable | Increment | 2-yr ATM Call | 2-yr ITM Call |
|---|---|---|---|
| Stock Price | +1 pt | +0.70 | +0.89 |
| Volatility | +1% | +0.48 | +0.33 |
| Interest Rate | +½% | +0.55 | +0.72 |
| Dividend | +$0.25/qtr | −1.18 | −1.50 |

A company raising its dividend during the life of a LEAPS call creates a pricing
headwind. A dividend increase benefits LEAPS puts. This asymmetry is a further
argument for keeping the stock and buying the put rather than substituting.

**LEAPS puts are right for protection, wrong for speculation.** The low delta
of a LEAPS put (~0.30 ATM) means it barely moves on daily stock declines —
a feature for a multi-year hedge and a bug for directional bearish speculation.

**Volatility expansion is a second engine of return.** When buying LEAPS at
historically low IV, rising volatility can preserve or increase the call's
value even on a flat or mildly declining stock. A 5% relative increase in
volatility is sufficient to keep an ATM 2-year call at its entry price after
one month of decay. Confirm whether current IV is near the low end of its
historical range before entry.

---

## On Bull Spreads

**Bull spreads have negative position vega.** An IV spike hurts them even if
the stock moves in the right direction. When a thesis resolves quickly and
violently — the scenario where fundamental work pays off most rapidly — the
outright call captures the IV spike as a bonus; the spread is hurt by it.

**Use bull spreads only in a narrow set of conditions:** IV is already elevated,
the expected move is moderate and gradual, and cost constraints make the
outright call genuinely unworkable.

**The spread's advantage over the outright call grows over time, not
immediately.** On a quick move in the underlying, the outright call outperforms
because spread differential widens mainly as a function of time. If the thesis
requires months to play out and the expected move is moderate, the spread
becomes relatively more attractive.

---

## On Fat Tails and Why Option Buying Is Favored

**Stocks move far more than standard models predict.** In any 30-day period,
even in the quietest markets, approximately 1 in 10 stocks makes a move of
3 or more standard deviations. The lognormal model assigns near-zero probability
to these events.

**The quantified gap is large.** Empirical data across 2.5 million stock trading
days shows actual 4σ+ downside moves occur more than **12 times** the lognormal
prediction; actual 4σ+ upside moves occur approximately **20 times** the
lognormal prediction. The call buyer at low IV is systematically undercharged
for the actual distribution of outcomes.

**Expected return studies under the correct fat-tail distribution show:**
- Option buying strategies fare much, much better than conventional wisdom
  suggests
- Covered writing loses its apparent advantage over stock ownership entirely
- Bull spreads are confirmed inferior regardless of which distribution is assumed
- Strategies with limited profit potential and large downside risk are inferior
  in the real distribution of stock outcomes

These conclusions come from Monte Carlo simulation using the actual empirical
distribution of stock moves — not the lognormal model.

**McMillan's governing rule:** Strategies with limited profit potential and
unlimited or large risk potential are inferior strategies in the actual
distribution of stock outcomes. The conventional broker advice — don't buy
options, do covered writes — is built on a distribution model that understates
large moves by 12 to 20 times. The correct conclusion from the data is the
opposite.

**Fat tails are a structural tailwind for the prepared option buyer — not a
standalone rationale for buying deeply OTM options.** The full case for option
buying requires all three elements together: (1) low IV entry, (2) a specific
fundamental thesis with a catalyst, and (3) the fat-tail distribution providing
more probability of a large favorable move than the market prices in. Fat tails
alone do not justify option purchases.

**The asymmetry of error reinforces the buying bias.** A mistake in buying
volatility is limited to the premium paid — survivable. A mistake in selling
volatility on individual stocks can be devastating.

---

## On Execution

**Always use limit orders** at the midpoint of bid and ask. Adjust if not
filled within a few minutes. Never use market orders on options.

**Never leg into a spread.** Enter multi-leg orders as a single spread
transaction specifying the net debit. The broker can split quotes on individual
legs in ways a retail investor cannot replicate by legging in.

**Never leg out of a spread after a favorable move.** Close as a single spread
transaction. Taking profit on the long leg while holding the short leg naked
introduces undefined risk inconsistent with the original position.

**Open interest is a liquidity gate.** Low open interest means wide spreads
and difficult exits — especially critical for a 3–12 month position that may
need to be rolled or exited early.

**Always sell in the secondary market to close.** Never exercise to liquidate.
Exercising destroys remaining time value. The only exception: when specifically
intending to own the underlying stock as the intended outcome.

---

*A worked example will be added after the first live analysis is completed.*

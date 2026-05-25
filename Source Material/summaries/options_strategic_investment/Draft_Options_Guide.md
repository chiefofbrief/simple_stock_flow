# Options Decision Guide
## For Use After Thesis Completion on {TICKER}

---

## Role

You are conducting an options analysis for **{TICKER}**. A thesis has already been
completed. Your purpose is to determine the most appropriate way to express that
thesis — whether through outright stock purchase, an options structure, or a
combination — and to produce a specific, actionable recommendation with full
cost and expected return calculations.

This is not a mechanical filter. It is an analytical process that synthesizes the
thesis, current market data, and options pricing into a recommendation. The
recommendation may be to simply buy the stock. That is a valid and sometimes
correct output.

**Default position size: $5,000 net options outlay** (premium paid minus any
premium received). Override only if explicitly instructed.

---

## Step 1: Gather Inputs

Read the following before doing anything else.

**From the Thesis File**
- `Data/tickers/{TICKER}/{TICKER}_Thesis.md` — Read the full Thesis. Extract:
  - Thesis type: LOSER or TAILWIND
  - Current stock price and price target
  - Catalyst type and timing certainty (high / moderate / low)
  - Expected holding period
  - Dividend status and approximate yield
  - Whether a position is already held, and if so, how many shares at what
    cost basis

**Market Data Required**

The following must be provided by the user or fetched before analysis begins.
If any item is missing, stop and request it before proceeding.

| Data Item | Source | Why Needed |
|---|---|---|
| Full options chain (calls and puts, strikes ±20% of current price, all expirations from ~3 months to furthest LEAPS available) | CBOE quote table: cboe.com/delayed_quotes/{ticker}/quote_table — set Options Range to "All," pull all expirations | Strike and expiration analysis, cost and expected return calculations |
| For each contract: Last, Bid, Ask, IV, Delta, Theta, Vega, Volume, Open Interest | Same CBOE chain | Pricing, greeks, liquidity screening |
| Historical volatility stack: 10-day, 20-day, 50-day, 100-day HV | Marketchameleon, Barchart, or equivalent free source | Conservative volatility input selection |
| IV percentile (52-week) and IV 52-week low and high | Marketchameleon or equivalent | IV regime assessment |
| Current T-bill rate (90-day) | Treasury.gov or equivalent | LEAPS substitution calculation if needed |

**Data check:** Confirm all required market data is present before proceeding.
If the options chain is missing or covers fewer than three expirations, stop
and request it. If HV data is unavailable, note this explicitly and proceed
with IV as the sole volatility reference.

---

## Step 2: Define the Menu of Available Structures

Based on the thesis inputs and market data, identify which structures are
viable for this specific situation. Every analysis includes outright stock
purchase as one option. Eliminate structures that clearly do not fit before
running calculations — but note that cost calculations in Step 3 may surface
a structure as the only workable option even if it would not be a first
choice on other grounds.

**Structure A — Buy Stock Outright**
Always on the menu. The baseline against which all options structures are
compared. Most appropriate when options premiums are expensive relative to
the expected move, the holding period is open-ended, or simplicity is the
priority.

**Structure B — Long Call (Outright Purchase)**
The primary options vehicle for this playbook. On the menu unless IV is
above the 70th percentile AND the range width is narrow (less than 15
percentage points absolute), making premium cost prohibitive relative to
the expected move. Requires no margin account.

**Structure C — LEAPS Call as Stock Substitute**
On the menu only if: a deeply ITM LEAPS call exists with little or no time
premium (2 points or less), AND the stock price makes 100-share ownership
impractical within the position size limit. Requires the full substitution
calculation in Step 3. No margin account required; freed capital goes to
T-bills.

**Structure D — Bull Call Spread**
On the menu only if: the outright call cost for a meaningful number of
contracts genuinely exceeds $5,000 AND IV is above the 50th percentile
(meaning the spread's negative position vega is not working against an
IV expansion thesis). Bull spreads are confirmed inferior in expected
return studies under the fat-tail distribution when options are fairly
priced. Include only when cost constraints make it the only viable options
structure, and flag this explicitly.

**Structure E — Protective Put on Existing Position**
On the menu only if a position is already held in this stock. Check the
no-cost collar calculation first — if achievable with a call strike above
the thesis price target, it dominates the outright put purchase.

**Structure F — No-Cost Collar on Existing Position**
On the menu only if a position is already held AND the stock's implied
volatility is high enough that selling a far-OTM call can fund the put
purchase at zero net debit. The required call strike must be above the
thesis price target — if it is not, the collar caps the thesis upside
and should not be used. Requires margin account for the short call.

**Structures excluded from this playbook:**
Naked puts or calls on individual stocks, calendar spreads as primary
positions, covered call writing on new positions, and any structure with
undefined or very large downside risk on individual stocks.

State which structures are on the menu and briefly note why any structure
was eliminated. Proceed to Step 3 with the surviving structures only.

---

## Step 3: Run the Numbers

> **Output mode:** Write the full analysis — all calculations, all structures,
> all tables — directly to `Data/tickers/{TICKER}/{TICKER}_Options.md` as you
> generate it, section by section. Do **not** output the full analysis in the
> chat window. When all calculations are complete, present **only the Structure
> Comparison Table and the Recommendation** in chat for review.

Run all calculations simultaneously for every structure on the menu, across
a range of strikes and expirations. Do not pre-select a strike before running
the numbers — let the calculations surface the optimal contract.

### 3A: IV and Volatility Assessment

Complete this before any cost or expected return work. Write findings to file.

**Check 1 — IV regime:**

| IV Percentile | Range Width | Interpretation |
|---|---|---|
| < 30th percentile | > 20 pts absolute | Favorable for buyers: IV expansion may contribute alongside stock appreciation. Structural entry advantage for long calls and long puts. |
| < 30th percentile | < 15 pts absolute | Percentile is low but expansion potential is limited. Options not expensive but IV tailwind is modest. |
| 30th–70th percentile | Any | Neutral. Expected return calculations determine attractiveness. |
| > 70th percentile | Any | Elevated premium. IV headwind: a flat stock with falling IV can produce a loss even without an adverse price move. Bull spread becomes relatively more attractive. Consider whether stock purchase is more cost-effective. |

**Check 2 — HV stack shape:**

- Stack slopes down from longer to shorter periods (10-day is the lowest):
  stock has been quieting. Options likely cheap relative to recent history.
  Favorable for buyers.
- Stack slopes up from longer to shorter periods (10-day is the highest):
  volatility currently elevated. Options may be expensive relative to
  longer-term norm. Caution for buyers.
- Stack is flat: neutral.

**Check 3 — Select the conservative volatility input:**

Use the **lowest reading in the HV stack** as the volatility input for all
expected return and probability calculations. This biases the analysis
against the buy decision. If the position looks attractive under this
pessimistic assumption, it has genuine margin of safety.

Exception: if the stock has been in distress or unusually volatile for
more than 100 days, use the long-lookback median: compute the 20-day,
50-day, and 100-day HV at each historical point over the past 600–1,000
trading days and use the median of those calculations.

**State the selected volatility input explicitly before proceeding.**

### 3B: Liquidity Screen

Before calculating anything, eliminate illiquid contracts:
- Open interest below 100 contracts, OR
- Bid-ask spread exceeds 10% of the midpoint: (ask − bid) / midpoint > 0.10

Note any contracts eliminated. Proceed with surviving contracts only.

### 3C: Strike and Expiration Range

Evaluate all surviving contracts across strikes from approximately 15–20%
below to 15–20% above the current stock price, across all available
expirations from ~3 months to the furthest LEAPS.

**Default priors — use as starting points, let calculations confirm or
override:**

| Situation | Default Prior |
|---|---|
| Uncertain timing, moderate expected move (most value investor situations) | ATM or first ITM; 6–9 month minimum expiration |
| High timing certainty, large rapid move expected | First OTM; 3–6 months |
| LEAPS (12+ months) | First OTM often wins on % return per dollar — compare explicitly with ITM |
| IV above 70th percentile | Wider strikes if using spread; or lean toward stock purchase |

### 3D: Cost Calculation

For each contract under evaluation:
Entry cost per contract = Ask price × 100
Contracts within $5K = floor($5,000 ÷ (Ask × 100))
Total outlay = Contracts × Ask × 100

Use the **ask price** for conservative cost estimation. In execution, enter
a limit order at the midpoint of bid and ask. For spreads:
Net debit = Long leg ask − Short leg bid
Total outlay = Net debit × 100 × number of spreads

Never use last sale prices for cost estimation — use bid and ask only.

### 3E: Break-Even Calculations
Long call break-even at expiration  = Strike + Premium paid per share
Bull spread break-even              = Lower strike + Net debit
Bull spread maximum profit          = Higher strike − Lower strike − Net debit
Protective put effective floor      = Stock cost − (Put intrinsic value − Put premium)

Break-even at expiration is the worst-case measure. The position can be
profitable before expiration if the stock moves favorably and/or IV expands.

### 3F: Expected Return Calculation

Run for each contract under evaluation. This is the core quantitative output.

**Required inputs:**
- p = current stock price
- v = conservative volatility input from Step 3A (annualized)
- t = realistic holding period in years — use expected exit horizon, not
  expiration date (most positions are exited before expiration)
- Standard deviation assumption: **0.7** (approximately 25% probability
  of occurring; more realistic than 1.0 standard deviation)

**Step 1 — Time-period volatility:**
$$v_t = v \times \sqrt{t}$$

**Step 2 — Upside stock target:**
$$q_{up} = p \times e^{(0.7 \times v_t)}$$

**Step 3 — Estimate call price at upside target.**
Use greeks as a shortcut for pre-expiration estimates:
$$\text{Call}_{up} \approx \text{Current call price} + (\Delta \times \text{stock move up})$$
For a conservative estimate, assume IV stays flat — no IV expansion credit.
If the upside target moves past expiration, use intrinsic value plus a small
residual time value estimate.

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
Use delta as a floor estimate of the probability of expiring in-the-money.
The probability of being in-the-money at some point during the holding
period is meaningfully higher than the delta — treat delta as the
pessimistic bound.

**Step 10 — Simple expected profit.**

Default probability weights — adjust only if the thesis provides specific
reason to deviate:
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
- **Aggressive list:** ranked by % profit (Step 4) — surfaces ATM or
  slightly OTM calls
- **Conservative list:** ranked by reward/risk ratio (Step 8) — surfaces
  ITM calls

### 3G: Position Vega Check

For each structure, state the position vega explicitly:
Position vega = Contracts × 100 × Individual vega (from chain)

- **Positive position vega** (long calls, long puts, calendar spreads):
  benefits from IV expansion. Correct when IV is low and the thesis involves
  a catalyst that may drive both price and volatility higher. An IV spike
  simultaneously mitigates losses if the stock declines — the crash cushion.
- **Negative position vega** (bull spreads, covered calls, credit spreads):
  hurt by IV expansion. Appropriate only when IV is already elevated and
  expected to fall. If IV is low at entry, negative vega works against the
  position even if the stock moves favorably.

If position vega sign does not match the IV environment, flag this
explicitly in the synthesis.

### 3H: LEAPS Substitution Calculation (Structure C Only)

Run only if Structure C survived Step 2.
Net credit generated:
Stock sale proceeds (if substituting from existing holding)    $___
Less stock commission                                         -$___
Cost of LEAPS call (ask × 100)                               -$___
Less option commission                                        -$___
Total credit balance (to be placed in T-bill)                  $___
Annual T-bill interest on credit balance                        +$___
Costs of switching:
Time value premium of LEAPS call                             -$___
Annual dividend forfeited (if any)                           -$___
Total commissions                                            -$___
Net annual cost of substitution = Total costs − T-bill interest  $___

Then check: is the LEAPS put at the same strike available in the market at
a price less than the implied cost of the substitution? If yes, buying the
put and keeping the stock is strictly better. If no, the substitution may
be more efficient.

Four caveats — address all before recommending Structure C:
1. Does the stock sale generate a taxable capital gain?
2. Does buying the call while still holding the stock constitute a wash sale?
3. Does the company pay a dividend that will be forfeited?
4. Does the target LEAPS call trade at or near parity (≤2 points time
   premium)? This is the necessary condition for the economics to work.

---

## Step 4: Synthesize and Recommend

With all calculations written to file, produce the synthesis. This is a
judgment that weighs cost, structure, timing, thesis alignment, and
follow-up burden together — not a summary of calculations.

### 4A: Structure Comparison Table

Produce this table and surface it in chat:

| Structure | Contracts | Total Outlay | Max Loss | Break-Even | Reward/Risk | Position Vega | IV Alignment | Follow-Up Burden |
|---|---|---|---|---|---|---|---|---|
| Stock purchase | 100 shares | $X | Full stock cost | Purchase price | N/A | N/A | N/A | Low |
| [Structure B — specific contract] | | | | | | | | |
| [Other surviving structures] | | | | | | | | |

### 4B: Recommendation

Surface in chat. Address each of the following explicitly:

**Structure and rationale:** Why this structure fits this thesis better than
the alternatives. Reference the specific thesis type (LOSER/TAILWIND),
timing certainty, IV regime, and position vega alignment.

**Contract specifics:**
- Strike price and expiration date
- Number of contracts (within $5K default, or state the override and reason)
- Total outlay at the ask; realistic execution at the midpoint
- Break-even price at expiration

**What the position requires:** What must the stock do, and over what
timeframe, for this position to be profitable? Be specific — "the stock
must reach $X by approximately [date], or IV must expand from Y% toward
Z%" is the required level of specificity.

**What breaks the position:** At what stock price does the position become
a loss worth cutting? State the technical level that serves as the mental
stop — based on the stock chart, not the option price.

**What was not chosen and why:** Briefly state why the next-best alternative
was passed over. This prevents the recommendation from appearing arbitrary.

---

## Step 5: Monitoring and Follow-Up

Write to file. State these specifically for the recommended contract.

**Flag 1 — Roll trigger:**
- ATM LEAPS: roll when approximately **6 months** remain
- OTM LEAPS: roll when approximately **12 months** remain
- Standard calls (3–9 months): begin evaluating exit or roll when
  **6 weeks** remain
These are the inflection points where decay accelerates from manageable
to rapid.

**Flag 2 — Early assignment risk (spreads and collars only):**
Monitor time value premium on any short option. If it drops to $0.10 or
less, close or roll before it reaches parity. For dividend-paying stocks:
if time value on the short call falls below the upcoming dividend amount
before the ex-date, early assignment is likely — close or roll before
the ex-date.

**Flag 3 — Favorable move follow-up:**

*Spread conversion (default follow-up for this playbook):*
If the long call has appreciated substantially and a higher-strike call
can be sold against it to cover the original cost, create a bull spread
at zero net cost. This locks in a floor while retaining upside to the
short strike. It is never the worst outcome at any stock price. Use when
the thesis has partially played out but meaningful upside remains.

*Trailing stop (best for a strong trend):*
Do nothing and place a mental stop at a technical support level on the
underlying stock. Every adjustment to a profitable position is a bearish
action. In a strong trend, "do nothing with a trailing stop" maximizes
profits.

*Partial exit:*
If multiple contracts are held, selling one-third to one-half at a
substantial gain while holding the remainder is a reasonable middle path.

*Full liquidation:*
Most appropriate when the thesis has fully played out or the position
has reached the price target. Always sell the option in the secondary
market — never exercise to liquidate. Exercising destroys remaining
time value and incurs full stock commissions.

**Flag 4 — Adverse move follow-up:**

*Cut the loss:*
If the stock breaks below a key technical support level, place a market
(not held) order to sell the call. Base the exit trigger on the stock
chart, not the option price. Stop orders on options produce poor
executions.

*Roll down (if thesis is still intact):*
If the thesis remains valid but timing was wrong, the roll-down may
recover break-even without adding capital. Sell two of the current
options, buy one at the next lower strike — for approximately even money.
If a meaningful additional debit is required, the roll-down is not worth
executing. The new break-even will be substantially lower; the trade-off
is capped upside above the lower strike.

Do not average down by buying more of the same option. The roll-down
into a spread is cheaper, produces a lower break-even, and reduces the
probability of a total loss.

---

## Step 6: Commit

Write the complete analysis to:
`Data/tickers/{TICKER}/{TICKER}_Options.md`

Sections written to file:
- IV and Volatility Assessment (Step 3A)
- Liquidity Screen results (Step 3B)
- Cost, break-even, and expected return calculations for all evaluated
  contracts (Steps 3D–3F)
- Position vega for each structure (Step 3G)
- LEAPS substitution calculation if applicable (Step 3H)
- Aggressive and conservative ranked lists (Step 3F)
- Structure Comparison Table (Step 4A)
- Full Recommendation (Step 4B)
- Monitoring and Follow-Up specifics for the recommended contract (Step 5)

**Action:** Present only the Structure Comparison Table and Recommendation
in chat. Ask: *"Do you approve this recommendation? Should I log it to the
Stock Tracker?"*

**STOP. Wait for explicit user approval before updating any tracker or
treating the recommendation as final.**

---

## Step 7: Self-Check

Before presenting anything in chat, verify the following internally.
Do not include these answers in output. If any answer is no, revise before
presenting.

- Is all required market data present? Were any missing items flagged?
- Was the IV assessment completed before any cost calculations?
- Was the conservative volatility input (lowest HV reading) explicitly
  stated and used throughout?
- Was a liquidity screen applied before calculating expected returns?
- Were calculations run across a range of strikes and expirations —
  not pre-selected?
- Does the position vega sign match the IV environment? If not, was
  this flagged explicitly?
- Was the reward/risk ratio calculated for each contract evaluated?
- Does the recommended contract fit within the $5K default outlay, or
  was the override stated and justified?
- Were break-even, probability of profit, and expected return all
  stated for the recommended contract?
- Was the LEAPS substitution calculation run if Structure C was on
  the menu, with all four caveats addressed?
- Was the recommendation stated with a specific strike, expiration,
  contract count, and total outlay — not just a structural description?
- Were monitoring flags stated specifically for the recommended contract?
- Was the full analysis written to file before anything was surfaced
  in chat?

---

## Interpretive Reference

### On Implied Volatility

**IV is the only unknown in the option pricing equation.** All other
inputs are observable. Getting the IV assessment right matters more
than picking the exact strike.

**IV is a poor predictor of actual volatility.** The market systematically
underestimates large moves because traders anchor toward middle-of-the-road
estimates. Options are often underpriced ahead of large moves — precisely
the moves that thesis-driven investors are positioned to anticipate.
Premiums paid at low IV entry will, in retrospect, have been too low if
the thesis plays out with a large price move.

**IV expansion can overcome weeks of time decay.** A stock at 100 that
goes nowhere for a month while IV rises from 20% to 26% leaves a 3-month
ATM call essentially unchanged in value. At high IV entry (80%+), IV must
rise to 99%+ just to offset one month of decay — a near-impossible
requirement in most circumstances.

**The range matters as much as the percentile.** A 5th-percentile reading
with a 39%–45% absolute range offers negligible IV expansion potential.
A 5th-percentile reading with a 25%–80% range offers a substantial
potential tailwind. Always check both.

**Panic drops often spike IV simultaneously.** In a rapid stock decline,
implied volatility frequently rises — partially offsetting the option's
loss from the stock move. This crash cushion is strongest at low-IV entry
and absent at high-IV entry. The Crash of 1987 produced a VIX move from
~36% to ~150% in one day; some OEX call holders at low IV broke even
or made money despite the worst single-day market decline on record.

### On Time Decay

**At 3+ months remaining, time decay is not the primary enemy.**
Theta is small relative to delta and vega at this duration. Theta only
dominates in the final weeks. This is why the playbook defaults to
6–9 month minimum expirations — it keeps the position on the flat part
of the decay curve.

**The square root rule governs relative pricing.** A 9-month option does
not cost three times a 3-month option — it costs approximately √3 times
as much in time premium. Longer-dated options are proportionally cheaper
per unit of time. Buying duration is efficient, not expensive.

**Roll before the curve bends.** Decay accelerates sharply at approximately
6 months remaining for ATM options and approximately 12 months remaining
for OTM options. These are mandatory roll triggers for LEAPS positions.

### On Strike Selection

**Delta is the primary guide — not absolute price.** A cheap OTM call
requires a large move just to break even. The correct comparison is
reward per dollar invested at the expected stock move, using delta to
estimate the option's response.

**For LEAPS, the delta curve is flat — do not assume ITM dominates.**
A LEAPS ATM call has delta ~0.70; the first OTM call may have delta
~0.50 at half the price. The OTM call gains approximately 70% as much
per stock move but costs 50% as much — competitive on percentage return.
Compare explicitly rather than defaulting to ITM.

**ITM for moderate expected moves; OTM for large expected moves.**
A LOSER thesis recovering to fair value (moderate re-rating) favors ITM.
A TAILWIND thesis with a hard catalyst driving a large move may favor
the first OTM strike on percentage return grounds.

### On Bull Spreads

**Bull spreads have negative position vega.** An IV spike hurts them
even if the stock moves in the right direction. When a thesis resolves
quickly and violently — the scenario where fundamental work pays off
most rapidly — the outright call captures the IV spike as a bonus; the
spread is hurt by it.

**Use bull spreads only in a narrow set of conditions:** IV is already
elevated, the expected move is moderate and gradual, and the cost
constraint makes the outright call genuinely unworkable. Do not use
bull spreads as a default cost-reduction tool — the vega cost is real
and often exceeds the premium saved.

**If the outright call is expensive, the "bullish spread" is superior
to the call bull spread:** buy the call, simultaneously sell an OTM
put credit spread to fund part of the premium cost. This preserves
the long call's positive vega while reducing net outlay. The trade-off
is additional downside risk below the short put's strike — a stop-loss
is required.

### On Fat Tails and Why Option Buying Is Favored

**Stocks move far more than standard models predict.** In any 30-day
period, even in the quietest markets, approximately 1 in 10 stocks makes
a move of 3 or more standard deviations. The market prices options using
the lognormal model, which assigns near-zero probability to these events.
The option buyer at low IV is systematically undercharged for the actual
distribution of outcomes.

**Expected return studies under the correct fat-tail distribution show:**
- Option buying strategies fare much better than conventional wisdom suggests
- Covered writing loses its apparent advantage over stock ownership
- Bull spreads are confirmed inferior regardless of which distribution
  is assumed
- Strategies with limited profit potential and large downside risk are
  inferior strategies in the real distribution of stock outcomes

This is the empirical foundation for buying rather than selling options
on individual stocks in this playbook.

### On Execution

**Always use limit orders** at the midpoint of bid and ask. Adjust if
not filled within a few minutes. Never use market orders on options.

**Never leg into a spread.** Enter multi-leg orders as a single spread
transaction specifying the net debit. The broker can split quotes on
individual legs in ways a retail investor cannot replicate by legging in.

**Open interest is a liquidity gate.** Low open interest means wide
spreads and difficult exits — especially critical for a 3–12 month
position that may need to be rolled or exited early.

**Always sell in the secondary market to close.** Never exercise to
liquidate. Exercising destroys remaining time value and incurs full
stock commissions on both sides.

---

## Worked Example: INTU (May 2026)

The following is a partial worked example using INTU data. It illustrates
the required level of specificity — how numbers are shown, how interpretive
guidance is applied inline, and what the recommendation looks like. This
is a format model, not a complete INTU analysis.

---

**Thesis inputs:**
- Thesis type: LOSER — stock has underperformed on AI disruption fears
  that may be overstated; re-rating thesis as TurboTax AI integration
  proves defensible
- Current stock price: $318.50
- Price target: $380 (19% upside)
- Catalyst: Quarterly earnings in ~8 weeks; longer-term re-rating over
  6–12 months
- Timing certainty: Low-to-moderate
- Holding period estimate: 6–9 months
- Dividend: ~$1.00/year (<0.35% yield)
- Existing position: None

---

**Step 3A: IV and Volatility Assessment**

Hypothetical inputs for illustration:
- Current composite IV: ~48% (average across near-the-money strikes)
- IV 52-week range: 28%–65% (absolute width: 37 points)
- IV percentile: ~55th percentile
- HV stack: 10-day 42%, 20-day 38%, 50-day 35%, 100-day 32%

Stack shape: slopes upward from longer to shorter periods — stock has
been heating up recently relative to its longer-term norm. Mild caution
signal for buyers.

IV regime: 55th percentile with a 37-point range is moderate. Not cheap
enough to call a structural entry advantage; not expensive enough to avoid
options. Some elevated-IV premium is embedded in current prices.

Conservative volatility input: **32%** (100-day HV — the lowest reading
in the stack).

---

**Step 3B: Liquidity Screen**

From the May 29 chain (7 days to expiration): all near-the-money strikes
show volume 80+ and open interest well above 100. No contracts eliminated
on liquidity grounds. However, the May 29 expiration is too short for this
thesis. Analysis focuses on longer expirations. For this example, assume
September 2026 and January 2027 contracts are available with comparable
liquidity.

---

**Step 3D–3F: Cost and Expected Return — September 2026 $320 Call
(Illustrative)**

Hypothetical pricing: Ask $22.00, Delta 0.52, Theta −$0.07/day, Vega 0.13

Cost calculation:
- Cost per contract: $22.00 × 100 = $2,200
- Contracts within $5K: floor($5,000 ÷ $2,200) = **2 contracts**
- Total outlay: **$4,400**

Break-even at expiration: $320 + $22 = **$342.00**

Expected return:

v_t = 0.32 × √0.50 = 0.32 × 0.707 = **0.226**

q_up = 318.50 × e^(0.7 × 0.226) = 318.50 × 1.171 = **$372.95**

At $373, intrinsic value = $53. With ~1 month remaining at that point,
estimated residual time value ~$2. Estimated call price: **$55**.
No IV expansion credit applied.

% profit = ($55 − $22) / $22 = **150%**

q_down = 318.50 × e^(−0.7 × 0.226) = 318.50 × 0.854 = **$272.00**

At $272, the September $320 call is deep OTM with ~4 months remaining.
Estimated call price: **$3**.

% loss = ($22 − $3) / $22 = **86%**

Reward/risk = 150% / 86% = **1.74** → Attractive (above 1.5 threshold)

Probability of profit: delta ~0.52 → floor estimate ~52% probability of
expiring in-the-money. Probability of being in-the-money at some point
during 6 months is meaningfully higher — treat 52% as the pessimistic bound.

Expected profit:
- Flat: Call_flat ≈ $22 − ($0.07 × 180 days) = $22 − $12.60 = $9.40
  Flat gain/loss = ($9.40 − $22) / $22 = −43%
- Expected = (0.25 × 150% × $4,400) + (0.50 × −43% × $4,400)
  + (0.25 × −86% × $4,400)
  = $1,650 − $946 − $946 = **−$242**

Expected profit is slightly negative under conservative inputs, driven
by the flat scenario's time decay. This reflects the moderate IV regime —
not a disqualifying result, but it signals that this trade is directional
and requires the stock to move. The January 2027 call (2 additional months
of duration) would reduce the flat-scenario decay drag and improve expected
profit — evaluated next.

---

**Step 3G: Position Vega**

September $320 call: Position vega = 2 × 100 × 0.13 = **+26**
Positive position vega. Consistent with the 55th percentile IV environment
— not a structural mismatch. Any IV expansion above 48% is incremental
benefit not included in the expected return calculation above.

---

**Structure Comparison Table (surfaced in chat):**

| Structure | Contracts | Total Outlay | Max Loss | Break-Even | Reward/Risk | Position Vega | IV Alignment | Follow-Up |
|---|---|---|---|---|---|---|---|---|
| Stock outright | 100 shares | $31,850 | $31,850 | $318.50 | N/A | N/A | N/A | Low |
| Long Call Sep $320 | 2 | $4,400 | $4,400 | $342.00 | 1.74 | +26 (positive) | Moderate fit | Low-moderate |
| Long Call Jan $320 (LEAPS) | 2 | ~$4,800 est. | $4,800 | ~$344.00 est. | Est. ~2.0+ | Higher positive | Better fit | Low |

---

**Recommendation (surfaced in chat):**

**Primary structure: Long Call — January 2027 $320 strike, 2 contracts,
estimated outlay ~$4,800 at ask.**

*Rationale:* The LOSER thesis has low-to-moderate timing certainty — the
market may take 6–12 months to recognize the AI defensibility argument.
The January 2027 expiration gives the thesis the full runway without
requiring a roll. The flat-scenario time decay drag is substantially
lower at ~14 months remaining than at ~4 months remaining (September).
The ATM strike matches the expected moderate re-rating rather than a
large, rapid move. Positive position vega is appropriate for the moderate
IV environment — the position benefits from any IV normalization higher
during the holding period. Expected reward/risk is estimated above 2.0x
for January vs. 1.74x for September, driven by the lower theta drag.

*What the position requires:* The stock must reach approximately $344
by January 2027 to break even at expiration. The price target of $380
implies approximately 160%+ profit on the options position. The thesis
must surface within the holding period — if INTU remains range-bound
through early 2027, the position will lose approximately 40–50% of its
value from time decay alone.

*What breaks the position:* If INTU breaks below the $290 technical
support level, place a market (not held) order to sell both calls. Do
not use an option price stop.

*What was not chosen:* The September $320 call was passed over because
the thesis holding period is 6–12 months — September provides only 4
months, creating unnecessary roll risk and higher theta drag. The stock
outright was passed over because the options position provides equivalent
directional exposure with defined maximum loss ($4,800 vs. $31,850) and
meaningful upside leverage on the 19% price target.

# prompt_options_existing.md
## Options Implementation — Existing Position Review
### For Use After Thesis Completion on {TICKER}

---

## Role and Purpose

You are conducting an options implementation review for **{TICKER}**. A thesis has
already been completed and a position is currently held — either stock, options, or
a combination. Your purpose is to assess the current position against the thesis,
determine whether any action is warranted, and produce a specific, actionable
recommendation.

This is not a mechanical filter. It is an analytical process that synthesizes the
thesis, the current position, current market data, and options pricing into a
recommendation. The recommendation may be to do nothing. That is a valid and
sometimes correct output.

**This prompt is for existing positions only.** If no position is currently held,
use `prompt_options_new.md` instead.

The thesis remains the foundation. All position decisions flow from thesis status
first. No tactical adjustment is appropriate when the thesis is broken — only a
clean exit.

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
- Catalyst timing certainty grade from the thesis

**Holding period:**
- Expected holding period stated in the thesis
- How much of that holding period has already elapsed

**Dividend:**
- Dividend status: yes / no
- Approximate annual yield if applicable

**Invalidation conditions:**
- Extract the specific thesis-wrong conditions from the Synthesis section.
  These are the objective basis for determining thesis status below.

**Thesis status — state explicitly before proceeding:**

Assess thesis status against the invalidation conditions and current data:
- **Intact:** No invalidation condition has been triggered. Financial results
  and/or price action are consistent with the thesis playing out.
- **Partially intact:** The thesis is directionally correct but one or more
  elements have weakened — timing has slipped, a catalyst has been delayed,
  or a specific metric has moved in the wrong direction without fully
  invalidating the case.
- **Broken:** One or more invalidation conditions have been triggered, OR the
  fundamental basis for the thesis no longer holds regardless of price action.

**The entire follow-up decision tree branches on thesis status. State it
explicitly and support it with specific evidence before proceeding to Step 2.**

### 1B: Current Position Details

The following must be provided before analysis begins. If any item is missing,
stop and request it.

| Item | Detail Required |
|---|---|
| Position type | Stock only / long call / bull spread / collar / combination |
| Entry price | Stock cost basis or option premium paid per contract |
| Strike and expiration | For any options held |
| Contracts held | Number of contracts |
| Current market value | Current price of the position |
| Unrealized P&L | Dollar amount and percentage |
| Time remaining | Days or months to expiration on any options |
| Any short options held | Strike, expiration, premium originally received |
| Long-term holding status | Has the stock crossed the long-term capital gains threshold? |

### 1C: Market Data Required

The following must be present before analysis begins. If any item is missing,
stop and request it.

| Data Item | Source |
|---|---|
| Current stock price | Any real-time or delayed quote |
| Full options chain (calls and puts, strikes ±20% of current price, all expirations from ~3 months to furthest LEAPS) | CBOE: cboe.com/delayed_quotes/{ticker}/quote_table |
| For each contract: Last, Bid, Ask, IV, Delta, Theta, Vega, Volume, Open Interest | Same CBOE chain |
| Historical volatility stack: 10-day, 20-day, 50-day, 100-day HV | Marketchameleon, Barchart, or equivalent |
| IV percentile (52-week) and IV 52-week low and high | Marketchameleon or equivalent |

**Data check:** Confirm all required data is present before proceeding. If the
options chain covers fewer than three expirations, stop and request it.

---

## Step 2: Thesis Status Gate

Before evaluating any structure or tactic, apply the thesis status gate.

**If thesis is BROKEN:**
- Recommend a clean exit of the entire position.
- Do not apply any defensive tactic to extend a position where the investment
  case no longer holds. Rolling down, spreading, or adding protection on a
  broken thesis delays the loss while adding complexity and cost.
- State the specific invalidation condition that was triggered.
- Proceed directly to Step 4 with the exit recommendation. Skip Steps 2–3.

**If thesis is INTACT or PARTIALLY INTACT:**
- Proceed to Step 3 to assess the current position and identify available actions.
- For partially intact thesis: note which element has weakened and how it affects
  the holding period estimate and price target range.

---

## Step 3: Position Assessment and Available Actions

Work through each section below that applies to the current position type.
If the position combines stock and options, work through both the relevant
stock section and the relevant options section.

### ESP: Equivalent Stock Position

For any position combining stock and options, calculate net directional exposure
before evaluating any action:
ESP = Number of contracts × 100 × Delta

Long calls and long stock produce positive ESP (bullish). Long puts and short
stock produce negative ESP (bearish).

**Example:** Long 100 shares (delta 1.00) + long 1 protective put (delta −0.30):
ESP = 100 − 30 = **+70** — the position participates in 70% of upside moves
and is partially insulated on the downside.

As the stock declines and a put moves deeper ITM (delta rising toward −1.00),
ESP drops toward zero — the protection working as intended. When ESP approaches
zero, evaluate whether rolling the put to a higher strike makes sense to restore
upside participation. Monitor ESP as the position ages; it is a live read on
whether the hedge is still functioning or has become so deep ITM that adjustment
is warranted.

State the current ESP before evaluating any action.

### 3A: Roll Trigger Check (Options Positions)

Check immediately for any options held. These are the inflection points where
decay accelerates from manageable to rapid — act before the curve bends, not
after.

| Option Type | Roll When |
|---|---|
| ATM LEAPS call | ~6 months remaining |
| OTM LEAPS call (20% OTM) | ~12 months remaining |
| Standard calls (3–9 months) | ~6 weeks remaining |

**Cumulative LEAPS decay warning:** Daily LEAPS decay appears trivial — less
than ¼% per day at 18 months remaining. But cumulative decay is real: an
18-month ATM LEAPS loses approximately 25% of its value in 6 months on a flat
stock. Do not be misled by the small daily number. If the thesis remains intact
at the roll trigger, roll forward rather than watch premium erode at an
accelerating rate.

If a roll trigger is active, flag it explicitly and address it in the
recommendation.

### 3B: Early Assignment Risk Check (Short Options)

Check immediately for any short options held.

**Flag any position with less than 1 month of life remaining on any options
leg.** These require active management — close, roll, or allow expiration —
and should not be left unmonitored.

Monitor time value premium on any short option. If it drops to $0.10 or less,
close or roll before it reaches parity.

**For short calls on dividend-paying stocks:** If time value on the short call
falls below the upcoming dividend amount before the ex-date, early assignment
is likely on the ex-date itself. Close or roll before the ex-date.

**For short puts on dividend-paying stocks:** If time value premium on the
short put falls below the upcoming dividend amount before the ex-date,
assignment the day *after* the ex-date is likely. The put holder collects the
dividend first, then exercises. Close or roll before the ex-date.

If an assignment risk flag is active, flag it explicitly and address it in the
recommendation.

### 3C: Favorable Move — Long Call Position

If the long call has an unrealized gain, five actions are available. Every
adjustment is a bearish action against a bullish position — each one reduces
participation in a continuing move. Weigh this explicitly before acting.

**1. Spread conversion (default follow-up):**
If a higher-strike call can be sold against the long call to create a bull
spread at zero or minimal net cost, this is never the worst outcome at any
stock price — it produces the largest profits if the stock remains in the
middle range and eliminates all downside risk below the original strike while
retaining upside to the short strike. Preferred when the thesis has partially
played out but meaningful upside remains.

**2. Roll up (most aggressive):**
Sell the appreciated call, recover original capital, use accrued profits to
buy multiple higher-strike calls. Appropriate only when expecting a large
further move with genuine conviction. Speculative acceleration — not a
default action.

**3. Trailing stop (best for a strong trend):**
Do nothing and place a mental stop at a technical support level on the
underlying stock. Every adjustment to a profitable position is a bearish
action. In a strong trend, "do nothing with a trailing stop" maximizes profits.

**4. Partial exit:**
Sell one-third to one-half at a substantial gain while holding the remainder.
Having taken partial profits, it is psychologically easier to hold the
remainder through volatility.

**5. Full liquidation:**
Most appropriate when the thesis has fully played out or the position has
reached the thesis price target. Always sell the option in the secondary
market — never exercise to liquidate. Exercising destroys remaining time value.

**Profit-taking symmetry:** A 100% profit on a $100 call deserves the same
consideration as a 100% profit on a $500 call. Do not hold a low-cost call to
a higher absolute profit threshold just because the initial outlay was small —
percentage return is the correct measure.

### 3D: Adverse Move — Long Call Position

**Thesis status check first.** If the thesis is broken, cut the loss — do not
apply defensive tactics to extend a position where the investment case no longer
holds.

**Cut the loss (thesis broken or stock breaks key support):**
If the stock breaks below a key technical support level, place a market (not
held) order to sell the call. Base the exit trigger on the stock chart, not the
option price. Stop orders on options produce poor executions.

**Roll down into bull spread (thesis intact, wrong on timing):**
If the thesis remains valid but timing was wrong, the roll-down may recover
break-even without adding capital. Sell two of the current options, buy one
at the next lower strike — for approximately even money. The new break-even
will be substantially lower; the trade-off is capped upside above the lower
strike.

Pre-condition: must be executable at even money or small debit. If a meaningful
additional debit is required, the roll-down is not worth executing.

Do not average down by buying more of the same option. The roll-down into a
spread is cheaper, produces a lower break-even, and reduces the probability
of a total loss.

**Calendar spreads on losing call positions are excluded.** If the stock
rallies before the near-term expiration, the short call is at a loss while
the long call may not have recovered — losses on both sides simultaneously.
The roll-down is strictly superior when executable at even money.

### 3E: Structure E — Protective Put on Existing Stock Position

On the menu when stock is held without options protection and the thesis is
intact or partially intact.

**Strike selection:** Default to the slightly OTM put — the first available
strike below the current stock price. This achieves the best balance between
protection cost and profit drag.
- Deep ITM put: eliminates nearly all profit potential. Almost never appropriate.
- Slightly OTM put: meaningful moderate-decline protection at reasonable cost.
  Synthetic equivalent of slightly ITM call — the correct default.
- Deep OTM put: appropriate only as a disaster hedge against severe drawdown,
  not for hedging moderate pullbacks. The OTM put's suppressed pre-expiration
  response (time value evaporates rapidly when the put crosses into ITM
  territory) makes it an unreliable hedge for moderate moves.

**Expiration selection:** When the price differential between near-term and
longer-term ITM puts is 1 point or less, default to the longest available
expiration. Duration is nearly free for ITM puts — unlike calls, where longer
duration carries a meaningful time premium cost. If the thesis requires
multi-year protection, LEAPS puts are the right tool.

**LEAPS puts for protection:** The low delta of a LEAPS put (~0.30 ATM) means
it barely moves on daily stock declines — a feature for multi-year protection
(slow daily cost, large payoff at the scenario requiring the hedge) and a bug
for short-term directional speculation. For portfolio protection over the
thesis holding period, LEAPS puts are correct.

**Delta sizing for full hedge:**
Put delta = Corresponding call delta − 1
Full delta hedge on 100 shares requires puts with combined delta = −100
At put delta −0.60: approximately 2 puts needed per 100 shares
Partial hedges are acceptable — size to the degree of protection required,
not automatically to full delta neutrality.

**OTM put time value retention:** OTM puts hold time value longer than
equivalent OTM calls on the other side. If the stock drifts sideways, the OTM
put holds value better than expected — the insurance cost is not front-loaded.
Once a put moves deep ITM however, time value erodes rapidly — faster than an
equivalent ITM call would gain value on the upside. Check remaining time value
directly before assuming a deep ITM put still carries meaningful optionality.

**Tax warning:** Buying a protective put while holding stock short-term
eliminates the accrued holding period — the clock does not restart until the
put is sold. Safe entry: buy simultaneously with the stock, or only after
long-term holding status is already established. Consult a tax advisor before
buying a protective put on any position where the long-term threshold has not
been crossed.

**Dividend-adjusted put pricing:** Puts on dividend-paying stocks are more
expensive than equivalent calls — each expected ex-dividend reduction is priced
into the put premium. Calculate the dividend-adjusted put cost before comparing
protective put vs. collar structures.

### 3F: Structure F — No-Cost Collar on Existing Stock Position

On the menu when stock is held and put protection is wanted but the cash cost
of a protective put is prohibitive.

**Required condition:** The call strike must be above the thesis price target.
If the required call strike is at or below the price target, the collar caps
the thesis upside and should not be used — buy the put outright instead.

**Critical warning — do not collar a stock you will not sell:** If the stock
cannot or will not be sold under any circumstances (tax situation, family
holding, concentrated position), do not write calls against it. A short call
on a stock you refuse to deliver is effectively a naked call. In this situation,
buy the put outright and pay the premium.

**No-cost collar volatility screen:** Use the following to assess whether a
no-cost collar is achievable before running full calculations (approximate,
at ~2.5 years to expiration):

| Underlying Volatility | Achievable Call Strike (OTM Distance) |
|---|---|
| 30% | ~30% OTM |
| 40% | ~35% OTM |
| 50% | ~40% OTM |
| 70% | ~50% OTM |
| 100% | ~70% OTM |

Higher volatility names — exactly the kind of beaten-down stocks a value
investor tends to own — generate the most favorable collar terms. If the
required call strike falls above the thesis price target at the applicable
volatility level, the no-cost collar is worth evaluating.

**Partial collar:** Sell fewer calls than shares owned to fund the put while
preserving unlimited upside on the uncapped shares.
Minimum calls to sell = Put cost ÷ Call premium received per contract
Verify the resulting call strike is above the thesis price target before
executing.

**P&L profile and honest cost assessment:** The collar's P&L profile is
equivalent to a bull spread, but the covered writer retains full stock
ownership — the position cannot be entirely wiped out in a short period as a
bull spread can. The put's value is not primarily in expected return — in most
scenarios it is a pure cost. Its value lies in eliminating forced decisions
during a decline and removing the possibility of catastrophic loss.

**Collar adjustment after a sharp rally above the short call strike:** The
only exit is buying back the call at a large debit. There is no convenient
exit from a collar on the upside — this cost must be weighed at entry, not
after the fact. If the stock rallies substantially, calculate the cost of
buying back the short call and decide whether to keep the stock (pay the debit)
or accept assignment.

**Collar adjustment after a sharp decline:**
- Sell the put if the decline appears finished and full upside participation
  is wanted.
- Roll the put down to lock in partial gain while maintaining protection at
  a lower floor.
- Sell OTM puts against the owned put for additional credit (introduces
  downside risk below the short put strike).

### 3G: Structure G — Zero-Cost Bull Spread Overlay on Existing Stock Loss

On the menu when stock is held at an unrealized loss, implied volatility is
elevated, and the thesis remains intact or partially intact.

**Check this structure before averaging down in stock.** Elevated IV — common
for beaten-down stocks — is the condition that makes it achievable. If premiums
allow it, this is superior to buying more shares at the current depressed price:
lower break-even, same downside below the long strike, capped upside above the
short strike being the only cost.

**Structure:** Buy one lower-strike call, sell two higher-strike calls, for
even money or minimal net debit. No naked exposure: one short call is covered
by the stock; the other is part of a bull spread with the long call.

**Pre-condition:** Must be executable at even money or a small debit. Check
against actual bid and ask — not last sale prices — before proceeding. If not
achievable at even money, this structure should not be forced.

**Effect:** Substantially lowers the break-even on the stock position without
adding downside risk below the long strike. Only above approximately 2× the
distance of the short strike from current price does the original stock-only
position outperform.

### 3H: Favorable Move — Long Put Position

After a substantial gain on a protective put, five actions are available:

**1. Spread (default for hedgers):**
Sell an OTM put against the profitable ITM put to lock in a floor at zero cost.
Never the worst outcome at any price. Note: the put spread locks in a smaller
absolute floor than the equivalent call spread due to OTM put time value
retention — size the hedge accordingly.

**2. Roll down:**
Sell the appreciated put, recover original capital, use profits to buy multiple
lower-strike puts. Most aggressive — doubles contracts, largest profit if stock
continues to fall.

**3. Combine:**
Buy an OTM call while continuing to hold the put. Converts the position into a
structure that profits from a large move in either direction. Appropriate if the
primary concern is a violent reversal back upward.

**4. Liquidate:** Sell the put and take the profit.

**5. Do nothing with trailing stop:** Place a mental stop above the declining
stock. Every adjustment introduces bullish bias to a bearish position — harmful
if the stock continues to fall.

### 3I: Adverse Move — Long Put Position

**Roll up (thesis intact, stock has rallied against the put):**
If the put has lost value after a stock rally and the roll-up is executable at
even money (sell 2 current puts, buy 1 at next higher strike), execute it. New
break-even is raised substantially at no additional cost. If even money is not
achievable, sell the put outright.

**Put calendar spreads on losing put positions are excluded.** Near-term and
longer-term puts at the same strike can approach parity simultaneously on a
decline, producing losses on both sides. The roll-up is strictly superior when
executable at even money.

---

## Step 4: Synthesize and Recommend

With all assessments complete, produce the recommendation. This is a judgment
that weighs thesis status, position health, time remaining, and available
actions together — not a summary of checks.

Address each of the following explicitly:

**Current position assessment:**
- State the position type, entry price, current value, unrealized P&L, and
  time remaining on any options.
- State the current ESP.
- State thesis status (intact / partially intact / broken) and the specific
  evidence supporting that assessment.

**Roll and assignment flags:**
- Are any roll triggers active? If so, state which and what action is required.
- Is any early assignment risk present? If so, state which position and what
  action is required.

**Recommended action:**
- If thesis is broken: state the exit clearly — which option or stock to sell,
  in what order, using what order type.
- If thesis is intact or partially intact: state the specific action — name
  the structure, strike, expiration, and number of contracts. State the cost
  or credit generated.
- If no action is warranted: state this explicitly and state why.

**What the action accomplishes:** How does it change the position's risk
profile, break-even, ESP, and upside participation relative to the thesis
price targets?

**What was not chosen and why:** Briefly state why the obvious alternative
was passed over.

**What the position requires going forward:** What must the stock do, and
over what timeframe, for the adjusted position to be profitable? Reference
the thesis base case price specifically.

**Next monitoring event:** State the next specific date or trigger to
re-evaluate — roll trigger date, ex-dividend date, earnings date, or thesis
catalyst window.

---

## Step 5: Self-Check

Verify the following before presenting anything in chat. If any answer is no,
revise before presenting.

- Were all thesis inputs extracted and stated explicitly, including bear/base/
  bull case prices, holding period elapsed vs. remaining, and invalidation
  conditions?
- Were all current position details gathered and stated before any
  recommendation was made?
- Was thesis status stated explicitly and supported with specific evidence?
- If the thesis is broken, was a clean exit recommended rather than a defensive
  tactic?
- Was ESP calculated and stated for any combined stock-plus-options position?
- Were roll triggers checked for all options legs? Were active triggers flagged?
- Was early assignment risk assessed for all short options? Were flags stated?
- Was the zero-cost overlay (Structure G) checked before recommending averaging
  down in stock?
- Was the naked call warning applied before recommending any collar on a stock
  that cannot or will not be sold?
- If a protective put is being added to a short-term stock holding, was the
  tax warning addressed?
- Was the recommendation stated with specific strikes, expirations, contract
  counts, and order types — not just a structural description?
- Was the next monitoring event stated specifically?

**STOP. After surfacing the recommendation in chat, wait for explicit user
approval before executing or logging anything.**

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
Do not expect large vega gains from a LEAPS position even at a low IV percentile.
For LEAPS, the primary profit driver is stock price appreciation.

**Panic drops often spike IV simultaneously.** In a rapid stock decline, implied
volatility frequently rises — partially offsetting the option's loss from the
stock move. This crash cushion is strongest at low-IV entry and absent at
high-IV entry.

**Put and call IV are linked.** Put and call IV at the same strike cannot
diverge for long — conversion arbitrage enforces alignment. A spike in put IV
pulls call IV up with it, and vice versa. This matters when holding both long
calls and protective puts simultaneously.

---

## On Time Decay

**At 3+ months remaining, time decay is not the primary enemy.** Theta is small
relative to delta and vega at this duration. Theta only dominates in the final
weeks.

**The square root rule governs relative pricing.** A 9-month option does not
cost three times a 3-month option — it costs approximately √3 times as much
in time premium. Longer-dated options are proportionally cheaper per unit of
time.

**Roll before the curve bends.** Decay accelerates sharply at approximately
6 months remaining for ATM options and approximately 12 months remaining for
OTM options. These are mandatory roll triggers for LEAPS positions.

**Cumulative LEAPS decay is real despite small daily rates.** An 18-month ATM
LEAPS loses approximately 25% of its value in 6 months on a flat stock. Do not
be misled by the small daily number.

**The four-variable trap.** The interplay of stock price, strike, time, and
volatility can work against each other simultaneously. If the thesis plays out
slowly — the stock grinds up rather than moves decisively — time decay can eat
premium faster than intrinsic value accumulates, especially on OTM calls.

---

## On Strike Selection

**Delta is the primary guide — not absolute price.** A cheap OTM call requires
a large move just to break even. The correct comparison is reward per dollar
invested at the expected stock move, using delta to estimate the option's
response.

**For LEAPS, the delta curve is flat — do not assume ITM dominates.** A LEAPS
ATM call has delta ~0.70; the first OTM call may have delta ~0.50 at half the
price — competitive on percentage return. Compare explicitly. This logic applies
only to the first OTM strike.

**ITM for moderate expected moves; OTM for large expected moves.** A thesis
recovering to fair value (moderate re-rating) favors ITM. A thesis with a hard
catalyst driving a large move may favor the first OTM strike.

**The slow-grind risk is real.** A stock grinding up modestly on an OTM call
can produce a loss even if the thesis is correct. When timing is uncertain, the
ITM call is more forgiving.

---

## On LEAPS Specifically

**Use a model, not your eyes.** A 2-year LEAPS with eight times the time
remaining of a 3-month call sells for only about four times as much. The LEAPS
does not look cheap just because it costs less than 8× the short-term call.
Price it properly before drawing conclusions.

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
of a LEAPS put (~0.30 ATM) means it barely moves on daily stock declines — a
feature for a multi-year hedge and a bug for directional bearish speculation.

---

## On Bull Spreads

**Bull spreads have negative position vega.** An IV spike hurts them even if
the stock moves in the right direction. When a thesis resolves quickly and
violently, the outright call captures the IV spike as a bonus; the spread is
hurt by it.

**Use bull spreads only in a narrow set of conditions:** IV is already elevated,
the expected move is moderate and gradual, and cost constraints make the
outright call genuinely unworkable.

**The spread's advantage over the outright call grows over time, not
immediately.** On a quick move, the outright call outperforms. If the thesis
requires months to play out and the expected move is moderate, the spread
becomes relatively more attractive.

---

## On Fat Tails and Why Option Buying Is Favored

**Stocks move far more than standard models predict.** In any 30-day period,
even in the quietest markets, approximately 1 in 10 stocks makes a move of
3 or more standard deviations.

**The quantified gap is large.** Empirical data across 2.5 million stock trading
days shows actual 4σ+ downside moves occur more than **12 times** the lognormal
prediction; actual 4σ+ upside moves occur approximately **20 times** the
lognormal prediction.

**Expected return studies under the correct fat-tail distribution show:**
- Option buying strategies fare much, much better than conventional wisdom
  suggests
- Covered writing loses its apparent advantage over stock ownership entirely
- Bull spreads are confirmed inferior regardless of which distribution is assumed
- Strategies with limited profit potential and large downside risk are inferior

**McMillan's governing rule:** Strategies with limited profit potential and
unlimited or large risk potential are inferior strategies in the actual
distribution of stock outcomes.

**Fat tails are a structural tailwind for the prepared option buyer — not a
standalone rationale for buying deeply OTM options.** The full case requires
all three: (1) low IV entry, (2) a specific fundamental thesis with a catalyst,
and (3) the fat-tail distribution providing more probability of a large favorable
move than the market prices in.

**The asymmetry of error reinforces the buying bias.** A mistake in buying
volatility is limited to the premium paid — survivable. A mistake in selling
volatility on individual stocks can be devastating.

---

## On Execution

**Always use limit orders** at the midpoint of bid and ask. Never use market
orders on options.

**Never leg into a spread.** Enter multi-leg orders as a single spread
transaction specifying the net debit.

**Never leg out of a spread after a favorable move.** Close as a single spread
transaction. Taking profit on the long leg while holding the short leg naked
introduces undefined risk.

**Open interest is a liquidity gate.** Low open interest means wide spreads and
difficult exits — especially critical for a position that may need to be rolled
or exited early.

**Always sell in the secondary market to close.** Never exercise to liquidate.
Exercising destroys remaining time value. The only exception: when specifically
intending to own or deliver the underlying stock as the intended outcome.

---

*A worked example will be added after the first live analysis is completed.*

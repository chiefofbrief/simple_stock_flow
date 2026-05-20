# Chapter 16: Put Option Buying — Extracted Insights for the Conservative Options Playbook

---

## Framing: The Put as a Leveraged Alternative to Short Selling

The purchase of a put option provides leverage in the case of a downward move by the
underlying stock. It is an alternative to the short sale of stock in the same way that
buying a call is a leveraged alternative to buying stock. If the underlying stock declines
substantially, the put buyer can make profits considerably in excess of his initial
investment. If the stock rises instead, the put buyer has limited risk — he can lose only
the amount originally paid for the put.

**The simplest use case:** When expecting a price decline in the underlying stock, the
investor may either short the stock or buy a put. The put limits the dollar loss to the
premium paid while preserving substantial downside leverage.

**Position-sizing rule:** The same 15% risk capital limit that applies to call buying
applies to put buying. The relatively large percentage risks involved are identical in
character to those of call buying.

**In the playbook context:** Put buying serves two distinct purposes — speculative
(expecting a decline in a stock not owned) and protective (hedging a long stock position
against adverse price moves). The mechanics of selection apply to both, but the
annotations throughout this chapter focus on the protective use case as the primary
application.

---

## 1. Selecting Which Put to Buy: ITM vs. OTM

The out-of-the-money put offers both higher reward potentials and higher risk potentials
than does the in-the-money put. If the underlying stock drops substantially, the
percentage returns from an OTM put will be greater. However, should the stock decline
only moderately, the in-the-money put will often prove to be the better choice. Since a
put option tends to lose its time value premium quickly as it becomes in-the-money, there
is an even greater advantage to purchasing the in-the-money put for moderate moves.

**Worked example:** XYZ is at 49.
- XYZ July 45 put: 1 (OTM)
- XYZ July 50 put: 3 (ITM)

If XYZ drops to 40 by expiration: July 45 put worth 5 (400% profit); July 50 put worth
10 (233% profit). The OTM put wins on a large, sustained decline.

If XYZ drops only to 45 by expiration: July 45 put expires worthless (100% loss); July
50 put worth 5 (67% profit). The ITM put wins on a moderate decline.

**The pre-expiration problem with OTM puts:** Most puts are liquidated before
expiration. If XYZ fell 5 points to 44 — a meaningful move in the put buyer's favor —
the July 45 put might increase only to 2–2½ points. This is disappointing because a call
going ITM on a 5-point move would behave much more favorably. The suppressed
response is a direct consequence of the ITM time value erosion dynamic from Chapter
15: as the put crosses the strike and goes ITM, time premium evaporates rapidly,
dampening the price gain.

**Conclusion:** When purchasing put options for speculation or protection, it is generally
best to concentrate on in-the-money puts unless a very substantial decline in the price
of the underlying stock is anticipated.

> **Annotation:** For the value investor using puts as a hedge on a long stock position,
> this guidance is decisive. The ITM put moves dependably with the stock from day one,
> behaves predictably before expiration, and does not require a large decline just to
> generate a meaningful offset to stock losses. The OTM put is appropriate only as a
> disaster hedge against a severe drawdown, not for hedging moderate pullbacks. Default
> to ITM puts for portfolio protection.

---

## 2. Buying Longer-Term ITM Puts: The Expiration Advantage Unique to Puts

Once a put is in-the-money, the time value premium decreases even in the longer-term
series. Since this time premium is small across all expirations, the put buyer can often
purchase a longer-term option for very little extra money, gaining more time to work with.

Call buyers are generally forced to avoid longer-term series because the extra cost is
disproportionate to the benefit, especially in a trading situation. The put buyer does not
have this disadvantage. If the longer-term put can be purchased for nearly the same price
as the near-term put, it should be preferred — it provides a cushion if the underlying
stock takes longer to decline than anticipated.

**Worked example:** XYZ common at 46.
- XYZ April 50 put: 4
- XYZ July 50 put: 4.50
- XYZ October 50 put: 5

None of these puts carry much time value premium. The buyer spending 1 extra point for
the October put gains six additional months. If the stock rises back to 50:
- April 50 put: ~1
- July 50 put: ~2.50
- October 50 put: ~3.50

The longest-term put suffered the smallest percentage loss on the adverse move because
it retains the most time value premium on recovery. If the stock continues to fall, all
three are profitable — the April put simply profits the most on an immediate decline.

> **Annotation:** This is a meaningful structural advantage of ITM puts over ITM calls.
> For the value investor buying a put to hedge a long stock position over a 3–12 month
> thesis period, the near-zero time premium differential across expirations means
> extending duration is nearly free. When the spread between near-term and longer-term
> ITM put prices is 1 point or less, default to the longest available expiration.

---

## 3. Delta of a Put: How Much the Put Moves with the Stock

The delta of a put is a negative number, reflecting the inverse relationship between put
price and stock price. The practical approximation:

> **Delta of put = Delta of call − 1**

This is accurate except when the put is deeply in-the-money.

**Delta benchmarks:**
- Deeply OTM put: delta near 0 — barely moves on modest stock declines.
- ATM put: delta approximately −.50.
- Deeply ITM put: delta near −1 — moves nearly point-for-point with stock declines.

The put's delta decreases slowly at first as the stock declines, then decreases much
more rapidly as the stock falls through the striking price, reaching approximately −1
as the stock falls only moderately below the strike. This reflects the fact that OTM
puts hold time premium well, while ITM puts approach parity quickly.

**Practical shortcut:** If the corresponding call has a delta of .40, the put delta is −.60.
This allows quick sizing of how many puts are needed to hedge a given stock position.
A position of 100 shares of long stock fully hedged requires puts with a combined delta
of +100 (to offset the stock's delta of 1.0 per share). At a put delta of −.60, approximately
2 puts are needed per 100 shares to approach a full delta hedge.

> **Annotation:** The delta relationship confirms the ITM put selection guidance. An ITM
> put with a delta near −1 moves almost point-for-point with a stock decline — it behaves
> like short stock, which is exactly what is needed for a hedge. An OTM put with a delta
> near 0 barely moves on modest declines, which is why it disappoints when the stock
> falls only moderately.

---

## 4. Ranking Put Purchases: Volatility-Adjusted Method

The same volatility-adjusted ranking methodology developed for calls in Chapter 3
applies to put purchases. Fixed-percentage rankings (e.g., "assume each stock falls 5%")
are useless and should be rejected — they do not incorporate the volatility of the
underlying stock. Rankings based on holding to expiration should also be rejected —
they do not reflect realistic holding periods of 30–90 days.

**The four-step ranking method for puts:**

1. Assume each underlying stock can decrease in price in accordance with its
   volatility over a fixed holding period (30, 60, or 90 days).
2. Estimate the put option prices after the decrease, accounting for remaining time
   premium.
3. Rank all potential put purchases by highest percentage reward for the aggressive
   list.
4. Estimate how much would be lost if the underlying stock instead rose in
   accordance with its volatility; rank all potential put purchases by best
   reward/risk ratio for the conservative list.

As with calls, this analysis requires a computer for accurate implementation across
all listed options. Use a data service that incorporates volatility and realistic holding
periods. **[Cross-reference: Chapter 28 mathematical techniques when notes are
available.]**

---

## 5. Always Sell to Close; Never Exercise to Liquidate

It is rarely to the put buyer's benefit to exercise the option in order to liquidate a
position. The cost of stock commissions makes exercising prohibitive for liquidation
purposes. This is true even if the option must be sold at a slight discount from parity
in the secondary market — the bid-ask cost of a below-parity sale is almost always
cheaper than paying stock commissions on both sides of the exercise transaction.

The only exception: when the investor actually intends to sell the underlying stock he
owns, in which case exercising the put to deliver his shares at the striking price is the
intended outcome.

---

## 6. Five Tactics for a Put Buyer with an Unrealized Profit

After the underlying stock has moved down and the put buyer has a substantial unrealized
gain, five tactics are available. These parallel the four call tactics from Chapter 3, with
the addition of a fifth tactic unique to puts: the combination.

**Background situation:**

| Original Trade | Current Prices |
|---|---|
| XYZ common: 52 | XYZ common: 45 |
| Bought XYZ October 50 put at 2 | XYZ October 50 put: 6 |
| | XYZ October 45 put: 2 |
| | XYZ October 45 call: 3 |

**The five tactics:**

**1. Liquidate** — sell the long put for a 4-point profit. No further upside or risk.
Least aggressive.

**2. Do nothing** — continue holding the October 50 put. If the stock reverses and
rises above 50 by expiration, everything is lost. If the stock continues to fall,
profits build substantially. The only tactic that can result in a loss at expiration.

**3. Roll down** — sell the October 50 put at 6, pocket the initial 2-point investment,
use the remaining 4 points to buy 2 October 45 puts at 2 each. No risk at
expiration since initial investment is recovered. If the stock continues to fall,
profits increase because the number of contracts has doubled.

**4. Spread** — sell the October 45 put at 2 against the long October 50 put. Net
cost of entire position = zero (paid 2 originally, received 2 from short put sale).
Maximum profit = 5 points if XYZ is anywhere below 45 at expiration. Zero risk
even if stock rises above 50.

**5. Combine** — buy the October 45 call at 3 while continuing to hold the October
50 put. Total combined cost = 5 points (2 for the put originally + 3 for the call).
No matter where XYZ is at expiration, this combination will be worth at least 5
points. If XYZ is above 50 or below 45, the combination is worth more than 5
points. Best tactic if the stock makes a dramatic move in either direction.

**Results at expiration:**

| XYZ at Expiration | Roll Down | Do Nothing | Spread | Liquidate | Combine |
|---|---|---|---|---|---|
| 30 | +$3,000 (B) | +$1,800 | +$500 | +$400 (W) | +$1,500 |
| 35 | +$2,000 (B) | +$1,300 | +$500 | +$400 (W) | +$1,000 |
| 41 | +$800 (B) | +$700 | +$500 | +$400 (W) | +$400 |
| 43 | +$400 | +$500 (B) | +$500 (B) | +$400 | +$200 (W) |
| 45 | $0 (W) | +$300 | +$500 (B) | +$400 | $0 (W) |
| 48 | $0 (W) | $0 (W) | +$200 | +$400 (B) | $0 (W) |
| 50 | $0 | −$200 (W) | $0 | +$400 (B) | $0 |
| 60 | $0 | −$200 (W) | $0 | +$400 | +$1,000 (B) |

*(B = best tactic; W = worst tactic)*

**Key conclusions:**

The spread tactic is never the worst outcome at any price — parallel to the call spread
finding in Chapter 3. However, the put spread is structurally less attractive than the
call spread equivalent: OTM puts hold time value better than OTM calls, so the short
leg of a put spread brings in less premium. The spread's floor-locking benefit is real
but smaller in dollar terms than the equivalent call spread.

The combine and roll-down are the most attractive of the five because neither has any
risk and both generate large profits if the stock moves substantially in either direction
(combine) or continues to fall (roll-down).

**The trailing stop principle:** Every time a put holder takes partial profits, rolls down,
or takes other adjusting measures, he is doing something bullish to a bearish position.
Those bullish actions are harmful if the underlying continues to decline. A trailing stop
placed above the declining stock price may be the best tactic of all — it allows profits
to run without introducing any bullish bias into the position.

> **Annotation:** For the value investor using puts as a portfolio hedge rather than
> a directional speculation, the most relevant tactic when the put has an unrealized
> gain is the spread (Tactic 4): sell an OTM put against the profitable ITM put to lock
> in a floor at zero cost. This eliminates the risk of the hedge reversing while preserving
> meaningful downside participation. The combine (Tactic 5) is appropriate if the
> primary concern is a violent reversal back upward — it converts the position into a
> structure that profits from a large move in either direction. Note that the put spread's
> reduced attractiveness (vs. the call spread) means the floor it locks in is smaller in
> absolute dollar terms; size the hedge accordingly.

---

## 7. The Rolling-Up Strategy: Salvaging a Losing Put Position

The put buyer who holds a put at an unrealized loss may be able to create a bear spread
that raises the break-even point without increasing total risk. This is the mirror of the
rolling-down strategy for calls described in Chapter 3.

**Worked example:**

An investor buys an XYZ October 45 put for 3 points with the stock at 45. The stock
rises to 48 and the put falls to 1.50. Without action: break-even at expiration = 42
(stock must fall 6 points from 48). With XYZ at 48, the October 50 put is selling for
3 points.

**The roll-up transaction:**

| Trade | Cost |
|---|---|
| Original: Buy 1 October 45 put at 3 | $300 debit |
| Later: Sell 2 October 45 puts at 1.50 each | $300 credit |
| Later: Buy 1 October 50 put at 3 | $300 debit |
| **Net position: Long 1 Oct 50, Short 1 Oct 45** | **$300 total debit** |

New break-even = 47 (stock needs to fall only 1 point from 48, vs. 6 points before).
Maximum profit = 2 points if XYZ is below 45 at expiration. Maximum loss unchanged
at $300 plus commissions, but now only realized if XYZ closes above 50 — a higher
threshold than the original position required.

The roll-up raises the break-even by 5 points and reduces the chance of realizing the
maximum loss, at the cost of capping maximum profit at 2 points.

**Pre-Trade Check — Even Money Requirement:**
This strategy should only be executed if the spread can be transacted at even money
or a small debit. Verify against actual bid-ask quotes — not last sale prices — before
acting. If a meaningful additional debit is required, the risk/reward improvement
diminishes and the trade may not be worthwhile. Never leg into this spread.

> **Annotation:** The rolling-up tactic is directly applicable to the value investor who
> bought a put to hedge a long stock position, the stock then rallied against the put, and
> the put now has a small residual value. Rather than selling the put for a small loss, the
> roll-up converts the dying put into a bear spread at no additional cost — raising the
> break-even substantially and reducing the probability of a total loss. The pre-condition
> is binding: if even money is not achievable, the original put should simply be sold.

---

## 8. The Calendar Spread as a Loss-Limiting Alternative — and Why It Is Inferior

When a put holder has an intermediate- or long-term put at an unrealized loss, selling
a near-term put at the same strike creates a calendar spread that reduces net cost if the
short put expires worthless.

**The critical failure mode:** Puts display different time value premium behavior than
calls. With the stock near the strike, the differential between near-term and longer-term
put prices does not widen meaningfully — unlike calls, where the near-term option
decays faster. If the stock falls back toward the strike before near-term expiration, both
puts approach parity simultaneously and the spread can be at a loss on both sides.

This failure mode cannot occur with the rolling-up strategy: even if the stock declines
after the roll-up spread is established, some profit is made on the rebound and no loss
is incurred on the decline.

**Conclusion:** The calendar spread is explicitly ranked inferior to the rolling-up
strategy for losing put positions. Default to rolling up. Use the calendar spread only
if rolling up is not executable at even money and the investor accepts the risk of a loss
even on a favorable stock decline.

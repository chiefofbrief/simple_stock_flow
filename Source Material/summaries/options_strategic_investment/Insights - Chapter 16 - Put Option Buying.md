# Chapter 16 — Put Option Buying: Extracted Insights for the Conservative Options Playbook

---

## 1. Selecting Which Put to Buy: ITM vs. OTM

"*The out-of-the-money put offers both higher reward potentials and higher risk
potentials than does the in-the-money put.* If the underlying stock drops substantially,
the percentage returns from having purchased a cheaper, out-of-the-money put will be
greater. However, should the underlying stock decline only moderately in price, the
in-the-money put will often prove to be the better choice. In fact, since a put option tends
to lose its time value premium quickly as it becomes an in-the-money option, there is an
even greater advantage to the purchase of the in-the-money put."

**Worked example — out-of-the-money vs. in-the-money put:**

XYZ is at 49 and the following prices exist:

XYZ July 45 put: 1 (out-of-the-money)
XYZ July 50 put: 3 (in-the-money)

If XYZ drops to 40 by expiration: the July 45 put is worth 5 points, a 400% profit. The
July 50 put is worth 10 points, a 233% profit over its initial purchase price of 3. Thus, in
a substantial downward move, the out-of-the-money put purchase provides higher reward
potential.

However, if the stock drops only moderately, to 45: the purchaser of the July 45 put
would lose his entire investment, since the put would be worthless at expiration. The
purchaser of the in-the-money July 50 put would have a 2-point profit.

**The pre-expiration problem with OTM puts:** The preceding analysis is based on
holding the put until expiration, which is generally an erroneous form of analysis, because
the buyer generally tends to liquidate in advance of expiration. "If the underlying stock
begins to drop below 45, the price of the put will not increase as rapidly as would the
price of a call that is going into-the-money."

**Example:** If XYZ fell by 5 points to 44 — definitely a move in the put buyer's favor —
he may find that the July 45 put has increased in value only to 2 or 2½ points. "This is
somewhat disappointing because, with call options, one would expect to do significantly
better on a 5-point stock movement in his favor. Thus, when purchasing put options for
speculation, *it is generally best to concentrate on in-the-money puts unless a very
substantial decline in the price of the underlying stock is anticipated.*"

> **Annotation:** For the value investor using puts as a hedge on a long stock position —
> the primary playbook use case — this guidance is decisive. The ITM put moves more
> dependably with the stock from day one, behaves predictably before expiration, and
> does not require a large decline just to break even. The muted response of the OTM put
> to a 5-point decline in the example (moving only to 2–2½ points) is the direct
> consequence of the ITM time value erosion dynamic established in Chapter 15: as the
> put crosses the strike and goes ITM, time premium evaporates rapidly, suppressing the
> price gain relative to what a call buyer would experience on an equivalent favorable
> move. The OTM put is appropriate only as a disaster hedge against a severe drawdown,
> not for hedging moderate pullbacks. Default to ITM puts for portfolio protection.

---

## 2. Buying Longer-Term ITM Puts: The Expiration Advantage Unique to Puts

"Once the put option is in-the-money, the time value premium will decrease even in the
longer-term series. Since this time premium is small in all series, the put buyer can often
purchase a longer-term option for very little extra money, thus gaining more time to work
with. Call option buyers are generally forced to avoid the longer-term series because the
extra cost is not worth the risk involved, especially in a trading situation. However, *the
put buyer does not necessarily have this disadvantage.* If he can purchase the longer-term
put for nearly the same price as the near-term put, he should do so in case the underlying
stock takes longer to drop than he had originally anticipated it would."

**Worked example:**

XYZ common, 46:
XYZ April 50 put, 4;
XYZ July 50 put, 4.50; and
XYZ October 50 put, 5.

None of these three puts have much time value premium in their prices. The buyer might
be willing to spend the extra 1 point and buy the longest-term put. If the stock should
drop in price immediately, he will profit, but not as much as if he had bought one of the
less expensive puts. However, should the stock rise in price, he will suffer less of a loss,
percentagewise, because if the stock rises back to 50, some amount of time value premium
will come back into the various puts, and the longest-term put will have the largest amount.
For example, if the stock rises back to 50:

XYZ April 50 put, 1;
XYZ July 50 put, 2.50; and
XYZ October 50 put, 3.50.

"The purchase of the longer-term October 50 put would have suffered the least loss,
percentagewise, in this event. Consequently, when one is purchasing an in-the-money
put, he may often want to consider buying the longest-term put if the time value premium
is small when compared to the time premium in the nearer-term puts."

> **Annotation:** This is an important structural advantage of ITM puts over ITM calls.
> For the value investor buying a put to hedge a long stock position over a 3–12 month
> thesis period, the near-zero time premium differential across expirations means that
> extending duration is nearly free. The longer-dated put provides a larger time cushion
> if the stock moves against the hedge before reversing, and loses less on a rebound. When
> the spread between near-term and longer-term ITM put prices is 1 point or less, default
> to the longest available expiration.

---

## 3. Delta of a Put: How Much the Put Moves with the Stock

"The delta of a put is a negative number, reflecting the fact that the put price and the
stock price are inversely related. *As an approximation, one could say that the delta of the
call option minus the delta of the put option with the same terms is equal to 1.* That is,

> Delta of put = Delta of call − 1."

This is an approximation and is accurate unless the put is deeply in-the-money.

"The delta of a put ranges between 0 and minus 1. If a July 50 put has a delta of −.50,
and the underlying stock rises by 1 point, the put will lose .50. The delta of a deeply
out-of-the-money put is close to zero. The put's delta would decrease slowly at first as the
stock declined in value, then would begin to decrease much more rapidly as the stock fell
through the striking price, and would reach a value of minus 1 (the minimum) as the
stock fell only moderately below the striking price. This is reflective of the fact that an
out-of-the-money put tends to hold time premium quite well and an in-the-money put
comes to parity rather quickly."

> **Annotation:** The delta relationship confirms the ITM put selection guidance in
> Section 1. An ITM put with a delta near −1 moves almost point-for-point with a decline
> in the stock — it behaves like short stock, which is exactly what is wanted for a hedge.
> An OTM put with a delta near 0 barely moves on modest declines, which is why it
> disappoints when the stock falls only moderately. The formula Delta of put = Delta of
> call − 1 is a practical shortcut: if the corresponding call has a delta of .40, the put delta
> is −.60 — useful for quickly sizing how many puts are needed to hedge a given stock
> position.

---

## 4. Always Sell to Close; Never Exercise to Liquidate

"It should be stated again that it is rarely to the option buyer's benefit to exercise the
option in order to liquidate. This precludes, of course, those situations in which the put
buyer actually wants to sell the stock. If, however, the option holder is merely looking to
liquidate his position, the cost of stock commissions makes exercising a prohibitive move.
*This is true even if he has to accept a price that is a slight discount from parity when he
sells his option.*"

> **Annotation:** The rule is unconditional for liquidation purposes: always sell the put in
> the secondary market, never exercise it. The bid-ask spread on even a slightly below-parity
> put sale will almost always be cheaper than paying stock commissions on both sides of
> the exercise transaction. The only exception is when the investor genuinely intends to
> sell the underlying stock he owns — in which case exercising the put to deliver his shares
> at the strike price may be the intended outcome anyway.

---

## 5. Five Tactics for a Put Buyer with an Unrealized Profit

After an underlying stock has moved down and the put buyer has a substantial unrealized
gain, McMillan identifies five tactics. The background situation for all five:

**TABLE 16-3. Background table for profit alternatives.**

| Original Trade | Current Prices |
|---|---|
| XYZ common: 52 | XYZ common: 45 |
| Bought XYZ October 50 put at 2 | XYZ October 50 put: 6 |
| | XYZ October 45 put: 2 |

The five tactics are:

1. **Liquidate** — sell the long put for a profit and do not reinvest.
2. **Do nothing** — continue to hold the long put.
3. **"Roll down"** — sell the long put, pocket the initial investment, and invest the
remaining proceeds in out-of-the-money puts at a lower strike.
4. **"Spread"** — create a spread by selling the out-of-the-money put against the put
already held.
5. **"Combine"** — create a combination by buying a call at a lower strike while
continuing to hold the put.

**Roll-down example (Tactic 3):** The trader receives 6 points from the sale of the October
50 put. He takes 2 points and puts it in his pocket, covering his initial investment. Then
he buys 2 October 45 puts at 2 points each with the remaining 4 points. "He has no risk
at expiration with this strategy, since he has recovered his initial investment. Moreover,
if the underlying stock should continue to fall rapidly, he could profit handsomely because
he has increased the number of put contracts that he holds."

**Spread example (Tactic 4):** Selling the October 45 put at 2 against the October 50
put brings in 2 points, which covers the initial 2-point purchase cost. "His 'cost' for this
spread is nothing; he has no risk, except for commissions." If XYZ rises above 50 by
expiration, all puts expire worthless — worst case, he recovers nothing. If XYZ is below
45 at expiration, the October 50 put will be worth 5 points more than the October 45 put,
and the spread can be liquidated for 5 points. "His maximum profit potential in the spread
situation is 5 points. This tactic would be the best one if the underlying stock stabilized
near 45 until expiration."

**Combine example (Tactic 5):** With XYZ at 45, there is an October 45 call selling for
3 points. The put holder buys this call:

Long 1 October 50 put — Combined cost: 5 points
Long 1 October 45 call

"No matter where the underlying stock is at expiration, this combination will be worth at
least 5 points. For example, if XYZ is at 46 at expiration, the put will be worth 4 and the
call worth 1; or if XYZ is at 48, the put will be worth 2 and the call worth 3. If the stock
is above 50 or below 45 at expiration, the combination will be worth more than 5 points.
Thus, the trader has no risk in this combination, since he has paid 5 points for it and will
be able to sell it for at least 5 points at expiration." This tactic is best if the underlying
stock makes a dramatic move either up or down by expiration.

**TABLE 16-4. Comparison of the five tactics.**

| By expiration, if XYZ … | the best strategy was … | and the worst strategy was … |
|---|---|---|
| Continues to fall dramatically | "Roll down" | Liquidate |
| Falls moderately further | Do nothing | Combine |
| Remains relatively unchanged | Spread | Combine or "roll down" |
| Rises moderately | Liquidate | "Roll down" or do nothing |
| Rises substantially | Combine | Do nothing |

**TABLE 16-5. Results of adopting each of the five tactics.**

| XYZ Price at Expiration | "Roll Down" Profit | Do-Nothing Profit | Spread Profit | Liquidate Profit | Combine Profit |
|---|---|---|---|---|---|
| 30 | +$3,000 (B) | +$1,800 | +$500 | +$400 (W) | +$1,500 |
| 35 | +2,000 (B) | +1,300 | +500 | +400 (W) | +1,000 |
| 41 | +800 (B) | +700 | +500 | +400 (W) | +400 |
| 42 | +600 (B) | +600 (B) | +500 | +400 | +300 (W) |
| 43 | +400 | +500 (B) | +500 (B) | +400 | +200 (W) |
| 45 | 0 (W) | +300 | +500 (B) | +400 | 0 (W) |
| 46 | 0 (W) | +200 | +400 (B) | +400 (B) | 0 (W) |
| 48 | 0 (W) | 0 (W) | +200 | +400 (B) | 0 (W) |
| 50 | 0 | −200 (W) | 0 | +400 (B) | 0 |
| 54 | 0 | −200 (W) | 0 | +400 (B) | +400 (B) |
| 60 | 0 | −200 (W) | 0 | +400 | +1,000 (B) |

B = best tactic; W = worst tactic.

"*The spread tactic never turns out to be the worst tactic*, although it is the best one only
if the underlying stock stabilizes."

"The advantage for the spread was substantial in call options, but in the case of puts,
the premium received for the out-of-the-money put is not as large, and therefore the
spread strategy loses some of its attractiveness."

On the roll-down and combine: "It would generally appear that the combination tactic
or the 'roll-down' tactic would be the most attractive, since neither one has any risk and
both could generate large profits if the stock moved substantially."

On trailing stops: "Every time one takes partial profits, rolls down, or takes other
measures, he is doing something bullish to his position. Those little bullish actions will
be harmful if the underlying continues to decline. Rather, a trailing stop, placed *above*
the declining stock price, might be the best tactic of all, because it allows one's profits
to run."

> **Annotation:** For the value investor using puts as a portfolio hedge rather than a
> directional speculation, the most relevant tactic when the put has an unrealized gain
> is the spread (Tactic 4): sell an OTM put against the profitable ITM put to lock in a
> floor on the position at zero cost. This eliminates the risk of the hedge reversing while
> preserving meaningful downside participation. The combine (Tactic 5) is the right
> choice if the investor's primary concern is a violent reversal back upward in the stock —
> it converts the position into a structure that profits from a large move in either direction.
> Note McMillan's caution that the put spread is less attractive than the call spread
> equivalent, because OTM puts hold time value better than OTM calls and therefore the
> short leg brings in less premium.

---

## 6. The "Rolling-Up" Strategy: Salvaging a Losing Put Position

"The put buyer who owns a put at a loss may be able to create a spread that allows him
to break even at a more favorable price at expiration. Such action will inevitably limit his
profit potential, but is generally useful in recovering something from a put that might
otherwise expire totally worthless."

**Worked example:**

An investor initially purchases an XYZ October 45 put for 3 points when the stock is at
45. The stock rises to 48 and the put is now selling for 1.50 points. "It is not unusual, by
the way, for a put to retain this much of its value even though the stock has moved up and
some amount of time has passed, since out-of-the-money puts tend to hold time value
premium rather well." With XYZ at 48, an October 50 put might be selling for 3 points.

Action: sell two October 45 puts at 1.50 each ($300 credit) and simultaneously buy one
October 50 put for 3 ($300 debit). Net cost: zero (commissions only).

**TABLE 16-6. Summary of rolling-up transactions.**

| | |
|---|---|
| Original trade: Buy 1 October 45 put for 3 with XYZ at 45 | $300 debit |
| Later: With XYZ at 48, sell 2 October 45's for 1.50 each | $300 credit |
| and buy 1 October 50 put for 3 | $300 debit |
| Net position: Long 1 October 50 put, Short 1 October 45 put | $300 debit |

Net position is a bear spread (long October 50, short October 45).

"*The investor has not increased his risk at all, but has raised the break-even point for
his position.* Without the effect of creating the spread, the put holder would need XYZ
to fall back to 42 at expiration in order to break even, since he originally paid 3 points for
the October 45 put." With the spread in place: at XYZ at 47 at expiration, the October 50
put is worth 3 points and the October 45 expires worthless — the investor recovers his
$300 cost. "His break-even point is raised from 42 to 47, a substantial improvement of
his chances for recovery."

The trade-off: maximum profit potential is now capped at 2 points (the 5-point maximum
spread width, less the 3 points paid to establish the original position). "He can no longer
gain substantially on a large drop in price by the underlying stock. This is normally of
little concern to the put holder faced with an unrealized loss and the potential for a total
loss."

Additionally: "he does not incur the maximum loss of his entire debit plus commissions,
unless XYZ closes above 50 at expiration. If XYZ is anywhere below 50, the October 50
will have some value and the investor will be able to recover something from the position.
*Thus, the introduction of the spread also reduces the chances of having to realize the
maximum loss.*"

"This action should be used only if the spread can be transacted at a small debit or,
preferably, at even money (zero debit)."

> **Annotation:** The rolling-up tactic is directly applicable to the value investor who
> bought a put to hedge a long stock position, the stock then rallied against the put, and
> the put now has a small residual value. Rather than selling the put for a small loss, the
> roll-up converts the dying put into a bear spread at no additional cost — raising the
> break-even and reducing the probability of a total loss. The key pre-condition McMillan
> specifies: the transaction must be executable at even money or a small debit. Verify this
> against actual bid-ask quotes before acting; do not leg into the spread.

---

## 7. The Calendar Spread as a Loss-Limiting Alternative — and Why It Is Inferior

"If the put that he is holding has an intermediate-term or long-term expiration date, he
might be able to create a calendar spread by selling the near-term put against the put that
he currently holds."

**Example:** An investor bought an XYZ October 45 put for 3 points when the stock was
at 45. The stock rises to 48 and the put falls to 1.50. He sells the near-term July 45 put
for 1 point. The ideal: the July 45 expires worthless, reducing the cost of the long put by
1 point. Then if the stock declined below 45, he could profit after July expiration.

"The major drawback to this strategy is that little or no profit will be made — in fact,
a loss is quite possible — if the underlying stock falls back to 45 or below before the
near-term July option expires. Puts display different qualities in their time value premiums
than calls do. With the stock at 45, the differential between the July 45 put and the
October 45 put might not widen much at all." In the example, if XYZ dropped quickly
back to 45, the July 45 might be worth 1.50 and the October worth 2.50 — the spreader
would have a loss on both sides. If the stock continues to decline below 45, "the spread
will most certainly become more of a loss as both puts come closer to parity."

"*This type of spread strategy is not as attractive as the 'rolling-up' strategy.* In the
'rolling-up' strategy, one is not subjected to a loss if the stock declines after the spread is
established, although he does limit his profits. The fact that the calendar spread strategy
can lead to a loss even if the stock declines makes it a less desirable alternative."

> **Annotation:** The calendar spread on a losing put is explicitly ranked inferior to the
> rolling-up strategy. The reason is structural: put time value premiums do not widen
> between near and far expirations the way call time value premiums do. The calendar
> spread in calls benefits from the near-term option decaying faster than the long-term one;
> in puts, this differential is much smaller and can work in reverse if the stock declines,
> driving both puts toward parity simultaneously. Default to the rolling-up strategy
> (Section 6) when faced with a losing put position. Use the calendar spread only if
> rolling up is not executable at even money and the investor is willing to accept the risk
> of a loss even on a favorable stock move.

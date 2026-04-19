# Chapter 7 — Bull Spreads Using Call Options: Extracted Insights for the Conservative Options Playbook

---

## 1. The Core Structure and Logic of the Bull Spread

"A *spread* is a transaction in which one simultaneously buys one option and sells
another option, with different terms, on the same underlying security. The basic idea
behind spreading is that the strategist is using the sale of one call to reduce the risk of
buying another call."

"The *bull spread* is one of the most popular forms of spreading. In this type of spread,
one buys a call at a certain striking price and sells a call at a higher striking price.
Generally, both options have the same expiration date. *A bull spread tends to be
profitable if the underlying stock moves up in price; hence, it is a bullish position.* The
spread has both limited profit potential and limited risk. Although both can be
substantial percentagewise, the risk can never exceed the net investment. In fact, a bull
spread requires a smaller dollar investment and therefore has a smaller maximum dollar
loss potential than does an outright call purchase of a similar call."

A call bull spread is always a debit transaction, since the call with the lower striking
price must always trade for more than the call with the higher price when both have the
same expiration date.

**Two formulas:**

> Break-even point = Lower striking price + Net debit of spread
>
> Maximum profit potential = Higher striking price − Lower striking price − Net debit
> of spread

**Worked example:** XYZ common at 32. XYZ October 30 call at 3; XYZ October 35
call at 1. Buy the October 30, sell the October 35 at a 2-point net debit.

Break-even = 30 + 2 = **32**
Maximum profit = 35 − 30 − 2 = **3 points ($300)**
Maximum loss = net debit = **2 points ($200)**

**TABLE 7-1. Results at expiration of bull spread.**

| XYZ Price at Expiration | October 30 Profit | October 35 Profit | Total Profit |
|---|---|---|---|
| 25 | −$300 | +$100 | −$200 |
| 30 | −300 | +100 | −200 |
| 32 | −100 | +100 | 0 |
| 35 | +200 | +100 | +300 |
| 40 | +700 | −400 | +300 |
| 45 | +1,200 | −900 | +300 |

"Note that *the spread has a maximum profit and this profit is realized if the stock is
anywhere above the higher striking price at expiration.* The maximum loss is realized if
the stock is anywhere below the lower strike at expiration, and is equal to the net
investment, 2 points in this example."

"*Therefore, the strategist establishing the bull spread is bullish, but not overly so.* If
he were rampantly bullish, he would merely buy the October 30 call outright. However,
the sale of the October 35 call against the purchase of the October 30 allows him to take
a position that will outperform the outright purchase of the October 30, dollarwise, as
long as the stock does not rise above 36 by expiration."

To verify: if one bought the October 30 outright for 3 points, he would have a 3-point
profit at expiration if XYZ were at 36. Both strategies have a 3-point profit at 36.
"Below 36, the bull spread does better because the sale of the October 35 call brings
in the extra point of premium. Above 36 at expiration, the outright purchase outperforms
the bull spread, because there is no limit on the profits that can occur in an outright
purchase situation."

> **Annotation:** The bull spread is the natural instrument for the value investor who
> believes in a stock but is uncertain about the magnitude or timing of the move, wants
> to reduce cost basis, and is willing to cap upside at a defined target price. The key
> trade-off: you give up everything above the short strike in exchange for a lower
> break-even and smaller maximum dollar loss.

---

## 2. Execution: Spread Orders, Pricing, and the Bid-Ask Problem

"*All spread transactions in which both sides of the spread are opening (initial)
transactions must be done in a margin account.* This means that the customer must
generally maintain a minimum equity in the account, normally $2,000."

"*The only way to determine the market price for a spread transaction is to know what
the bid and asked prices of the options involved are.*"

**Worked example:** An investor wants to buy the XYZ October 30 and sell the XYZ
October 35. Last sale prices suggest a 2-point debit. But:

| | Bid | Asked | Last Sale |
|---|---|---|---|
| October 30 call | 3.90 | 4.10 | 4.00 |
| October 35 call | 1.95 | 2.00 | 2.00 |

At market, the spreader pays 4.10 for the October 30 (the ask) and receives only 1.95
for the October 35 (the bid). Actual debit = **2.15 points** — significantly more than the
2-point difference in last sale prices. One might enter the order at a 2.10-point debit and
have a reasonable chance of being filled if the broker can split the quote on either leg.

"*One cannot assume that last sale prices are indicative of the price at which a spread
transaction can be executed.*" Practical screen: use only relatively liquid options — those
that have traded a substantial number of contracts in the previous session, where bid and
ask are more likely to be tight.

"*It is generally a poor idea to leg into a spread.* If the floor broker handling the
transaction knows the entire transaction, he has a much better chance of 'splitting a
quote,' buying on the bid, or selling on the offering."

On commissions: "*Commissions may represent a significant percentage of the profit
and net investment*, and should therefore be calculated before establishing the position.
If these commissions are included in the net debit to establish the spread, they
conveniently fit into the preceding formulae." To reduce commission impact
percentagewise, "it is generally advisable to spread at least 5 options at a time."

> **Annotation:** On a 2-point spread, paying 2.15 instead of 2.00 reduces maximum
> profit from 3 points to 2.85 — a 5% reduction in gross profit before commissions. The
> practical discipline: always enter as a single spread order with a specified net debit
> limit, use the bid-ask quotes (not last sale) to set that limit, and restrict spread
> candidates to liquid options where the quote is likely to be tight.

---

## 3. Degrees of Aggressiveness: Three Types of Bull Spread

**Aggressive (standard) bull spread:** The stock is near or slightly below the lower
striking price when the spread is established. "*Aggressive bull spreads are most
attractive when the underlying common stock is relatively close to the lower striking
price at the time the spread is established.* A bull spread established under these
conditions will generally be a low-cost spread with substantial profit potential, even
after commissions are included."

**Extremely aggressive (out-of-the-money) bull spread:** Both calls are out-of-the-money.
"These spreads are extremely inexpensive to establish and have large potential profits if
the stock should climb to the higher striking price by expiration. However, they are
usually quite deceptive in nature. The underlying stock has only a relatively remote
chance of advancing such a great deal by expiration, and the spreader could realize a
100% loss of his investment even if the underlying stock advances moderately, since both
calls are out-of-the-money. This spread is akin to buying a deeply out-of-the-money call
as an outright speculation. It is not recommended that such a strategy be pursued with
more than a very small percentage of one's speculative funds."

**Least aggressive (in-the-money) bull spread:** Both calls are in-the-money. "This is a
much less aggressive position, since it offers a large probability of realizing the maximum
profit potential, although that profit potential will be substantially smaller than the profit
potentials offered by the more aggressive bull spreads."

**Worked example of the ITM spread:** XYZ is at 37. The October 30 call is at 7; the
October 35 call is at 4. Both calls are in-the-money. Spread cost = 3 points (debit).
Maximum profit potential = 2 points, realized as long as XYZ is anywhere above 35 at
expiration. "That is, XYZ could *fall* by 2 points and the spreader would still make his
maximum profit." To realize the maximum loss, XYZ would need to decline 7 points to
fall below 30 — "it would have to be considered a rather low-probability event. This fact
adds to the less aggressive nature of this type of spread." Note: commission costs are
substantially larger here than in OTM spreads, because higher-priced options are
involved; they must be figured into profit calculations before entering.

> **Annotation:** For the conservative value investor, the ITM spread offers the widest
> cushion against being wrong — the maximum profit is earned even on a modest decline.
> The aggressive (standard) spread — stock near the lower strike — is appropriate when
> the investor has a firm price target above current levels and is willing to lose the full
> net debit if the stock goes nowhere. The OTM spread should be avoided except as a
> small speculative position; it is the functional equivalent of buying a deeply OTM call.

---

## 4. The Critical Timing Issue: Bull Spread vs. Outright Call Purchase

"With most types of spreads, it is necessary for some time to pass for the spread to
become significantly profitable, even if the underlying stock moves in favor of the
spreader. For this reason, *bull spreads are not for traders* unless the options involved
are very short-term in nature. If a speculator is bullishly oriented for a short-term
upward move in an underlying stock, it is generally better for him to buy a call outright
than to establish a bull spread. Since the spread differential changes mainly as a
function of time, small movements in price by the underlying stock will not cause much
of a short-term change in the price of the spread."

**Worked example of the short-term timing disadvantage:** XYZ is at 32. Bull spread:
long October 30 at 3, short October 35 at 1, net debit = 2 points. The stock jumps to 35
in one day. The October 30 is now worth approximately 5.50; the October 35 is worth
approximately 2.50. Bull spread value = 5.50 − 2.50 = 3.00 points = **1-point profit** (less
two commissions). Outright purchaser of the October 30 is ahead by **2.50 points** (less
one commission). "Clearly, then, for the shortest time period — one day — the outright
purchase outperforms the bull spread on a quick rise."

For 30 days: "the outright purchase still has the advantage if the underlying stock moves
up quickly. Even if the stock should advance above 35 in 30 days, the bull spread will
still have time premium in it and thus will not yet have reached its maximum spread
potential of 5 points."

"*The longer it takes for the underlying stock to advance, the more the advantage swings
to the spread.* Suppose XYZ does not get to 35 until expiration. In this case, the October
30 call would be worth 5 points and the October 35 call would be worthless. The outright
purchase of the October 30 call would make a 2-point profit less one commission, but the
spread would now have a 3-point profit, less two commissions. Even with the increased
commissions, the spreader will make more of a profit, both dollarwise and percentagewise."

**TABLE 7-2. Bull spread and outright purchase compared.**

| | Declines | Remains Relatively Unchanged | Advances Moderately | Advances Substantially |
|---|---|---|---|---|
| 1 week | Bull spread | Bull spread | Outright purchase | Outright purchase |
| 1 month | Bull spread | Bull spread | Outright purchase | Outright purchase |
| At expiration | Bull spread | Bull spread | Bull spread | Outright purchase |

"The spread will not produce as much of a profit on a short-term move, or on a
sustained, large upward move. It will, however, outperform the outright purchase of a
call if the stock advances slowly and moderately by expiration. Also, the spread always
involves fewer actual dollars of risk, because it requires a smaller debit to establish
initially."

**Strike distance as a partial remedy for the slow-widening problem:** "Many traders
are disappointed with the low profits available from a bull spread when the stock rises
almost immediately after the position is established. One way to partially offset the
problem with the spread not widening out right away is to use a greater distance between
the two strikes. When the distance is great, the spread has room to widen out, even
though it won't reach its maximum profit potential right away. Still, since the strikes are
'far apart,' there is more room for the spread to widen even if the underlying stock rises
immediately."

> **Annotation:** This is the most important structural trade-off in the chapter. The
> bull spread suits the value investor's core profile precisely: a thesis that requires months
> to play out, a moderate price target, and a preference for lower cost basis over maximum
> upside. If the expected move is large and fast — a hard catalyst, an imminent
> announcement — buy the call outright. If the thesis is "this stock is cheap and will
> re-rate over the next 3–6 months," the bull spread is the better vehicle.
>
> On strike distance: when uncertain whether the move will come quickly or slowly,
> widen the strikes. This reduces the timing penalty at the cost of a higher net debit and
> a higher required stock price for maximum profit.

---

## 5. Ranking Bull Spreads: Don't Use Maximum Profit; Incorporate Volatility

"In any ranking of bull spreads, *it is important not to rank the spreads by their maximum
potential profits at expiration.* Such a ranking will always give the most weight to deeply
out-of-the-money spreads, which can rarely achieve their maximum profit potential. It
would be better to screen out any spreads whose maximum profit prices are too far away
from the current stock price."

McMillan's simple volatility-adjusted screening method: "assume that the stock could,
at expiration, advance by an amount equal to twice the time value premium in an
at-the-money call. Since more volatile stocks have options with greater time value
premium, this is a simple attempt to incorporate volatility into the analysis. Also, since
longer-term options have more time value premium than do short-term options, this will
allow for larger movements during a longer time period. Percentage returns should
include commission costs."

> **Annotation:** The practical application of this screen: before entering a bull spread,
> calculate 2× the ATM call's time value premium. That is the maximum distance the
> short strike should be from the current stock price — beyond that, maximum profit
> becomes a low-probability outcome and the spread is effectively an OTM speculation.
> This single filter eliminates the most common ranking error and keeps the short strike
> within a realistic expected move. Among spreads that pass this screen, rank by
> percentage return on net debit after commissions, not by absolute profit.

---

## 6. When Options Are Expensive: The Bull Spread as a Cost-Reduction Tool

"Experienced traders often turn to bull spreads when options are expensive. The sale
of the option at the higher strike partially mitigates the cost of buying an expensive
option at the lower strike. However, one should not always use the bull spread approach
just because the options have a lot of time value premium, for he would be giving up a
lot of upside profit potential in order to have a hedged position."

> **Annotation:** The spread reduces cost but caps upside. The decision rule is whether
> the short strike aligns with a realistic price target. If the investor's thesis implies a
> target price near the short strike, the spread makes sense in high-IV environments. If
> the thesis requires a much larger move — a full re-rating well above the short strike —
> the spread sacrifices too much upside and the outright call is preferable despite the
> higher cost.

---

## 7. Follow-Up Action: Assignment Risk and Legging Out

"Since the strategy has both limited profit and limited risk, it is not mandatory for the
spreader to take any follow-up action prior to expiration. If the underlying stock
advances substantially, the spreader should watch the time value premium in the short
call closely in order to close the spread if it appears that there is a possibility of
assignment. This possibility would increase substantially if the time value premium
disappeared from the short call."

On closing: "The maximum credit that can be recovered from a bull spread is an amount
equal to the difference between the striking prices." In practice, "it is quite difficult to
obtain the entire 5-point credit even if expiration is quite near. Generally, one might ask
for a 4.80 or 4.90 credit." Always close as a spread transaction, not as two separate
orders. The net maximum profit after commissions is actually realized when the stock
is exactly at the higher striking price at expiration — if the stock is well above it, gross
profit is the same but commissions to liquidate are higher.

On legging out when the stock drops: if the short call can be repurchased at ⅛ or 1/16,
buying it back to lock in the short-side profit and holding the long call is acceptable.
"However, he should not be quick to repurchase it if it still has much more value than
that, unless he is closing out the entire spread. *At no time should one attempt to 'leg'
out after a stock price increase*, taking the profit on the long side and hoping for a stock
price decline to make the short side profitable as well. The risk is too great."

---

## 8. Using a Bull Spread to Lower Break-Even on a Stock Loss

A stockholder with an unrealized loss can overlay a bull spread to substantially lower the
break-even price at no additional capital outlay — one of the most actionable applications
in the playbook.

**Worked example:** Investor buys 100 shares of XYZ at 48. Stock falls to 42.
Without options: break-even = 48, requiring a 6-point rally from 42. Current prices:

XYZ common, 42; XYZ October 40 call, 4; XYZ October 45 call, 2.

Action: Buy one October 40 call at 4, sell two October 45 calls at 2 each.
Net cost = zero before commissions (2 × $200 credit = $400 = cost of October 40).

The position contains no naked options: one short October 45 is covered by the stock;
the other is part of a bull spread with the October 40.

Results if XYZ is at exactly 45 at October expiration:
- Two short October 45's expire worthless: +$400
- Long October 40 worth 5 points: +$100
- Total option profit: +$500
- Stock profit at 45 (bought at 48): −$300
- **Net total profit: +$200**

**TABLE 7-3. Lowering the break-even price on common stock.**

| XYZ Price at Expiration | Profit on Stock | Profit on Short Oct 45's | Profit on Long Oct 40 | Total Profit |
|---|---|---|---|---|
| 35 | −$1,300 | +$400 | −$400 | −$1,300 |
| 38 | −1,000 | +400 | −400 | −1,000 |
| 40 | −800 | +400 | −400 | −800 |
| 42 | −600 | +400 | −200 | −400 |
| 43 | −500 | +400 | −100 | −200 |
| 44 | −400 | +400 | 0 | 0 |
| 45 | −300 | +400 | +100 | +200 |
| 48 | 0 | −200 | +400 | +200 |
| 50 | +200 | −600 | +600 | +200 |

Break-even is lowered from 48 to **44** — only a 2-point rally from 42 is needed. The two
strategies produce identical results below 40 and are equal at 50. Between 40 and 50, the
new position outperforms. The stock would need to rally more than 8 points — from 42
to 50 — for the original stock-only position to outperform. "Only if the stock rallies very
sharply will the stock position outperform the total position."

This strategy can also be used as an **opening trade**: "an investor who is considering
buying XYZ at 42 might decide to buy the October 40 and sell two October 45's (for even
money) at the outset. The resulting position would not be inferior to the outright purchase
of XYZ stock, in terms of profit potential, unless XYZ rose above 46 by October
expiration."

> **Annotation:** This is a direct-entry tool for the value investor who owns a stock at a
> loss and still believes in the thesis. The zero-cost overlay lowers the required recovery
> from 6 points to 2 without adding downside risk below the lower strike. The key
> pre-condition: the option premiums must allow the transaction to be done at even money
> or a small debit — most likely when implied volatility is elevated, which is often the
> case for a beaten-down stock. Check this structure before averaging down in stock.

---

## 9. The Bull Spread as a Covered Write Substitute (Capital Efficiency)

"If there is an in-the-money call with little or no time premium remaining in it, its
purchase may be used as a substitute for buying the stock itself… *the profit potential of
owning a deeply in-the-money call can be very similar to owning the stock.* Since such
a call costs less to purchase than the stock itself would, the buyer is getting essentially
the same profit or loss potential with a smaller investment."

By then selling a call closer to the money against the deep ITM call, the investor creates
a bull spread with profit characteristics closely resembling a covered write — but at a
fraction of the capital required.

**Worked example:** XYZ common at 49. XYZ April 50 call at 3; XYZ April 35 call at 14
(no time premium — trades at parity). Buy the April 35 at 14, sell the April 50 at 3. Net
debit = $1,100.

**TABLE 7-4. Results for covered write and bull spread compared.**

| | Covered Write: Buy XYZ + Sell April 50 | Bull Spread: Buy April 35 + Sell April 50 |
|---|---|---|
| Maximum profit potential (stock over 50 in April) | $400 | $400 |
| Break-even point | 46 | 46 |
| Investment | $4,600 | $1,100 |

"Since the bull spread requires a much smaller investment, the spreader could put
$3,500 into interest-bearing securities. This interest could be considered the equivalent
of receiving the dividends on the stock. In any case, the spreader can lose only $1,100,
even if the stock declines substantially. The covered writer could have a larger unrealized
loss than that if XYZ were below 35 at expiration."

"Thus, the bull spread offers the same dollar rewards, the same break-even point,
smaller commission costs, less potential risk, and interest income from the fixed-income
portion of the investment. *While it is not always possible to find a deeply in-the-money
call to use as a 'substitute' for buying the stock, when one does exist, the strategist should
consider using the bull spread instead of the covered write.*"

Caution: "one would not want to put all of his money into such a strategy and forsake
covered writing, since, with bull spreads, he could be entirely wiped out in a moderate
market decline. In a covered writing strategy, one still owns the stocks even after a severe
market decline." The suggestion is a partial allocation — smaller capital in bull spreads,
balance in interest-bearing securities, with the same profit potential as the covered write.

> **Annotation:** The pre-condition — a deep ITM call trading at or near parity — is the
> binding constraint. It is most commonly found in LEAPS on stocks that have already
> moved significantly, or in shorter-term options after a large run-up where deep calls
> have been repriced to near-intrinsic. When it exists, the structure is unambiguously
> superior to the covered write on every metric except the one that matters in a crash:
> the covered writer still owns the stock. Worth screening for on any covered write
> candidate before committing capital to the stock position.

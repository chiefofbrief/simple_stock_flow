
# Chapter 7: Bull Spreads Using Call Options — Extracted Insights for the Conservative Options Playbook

---

## Foundational Vocabulary: Spread Categories and Pricing Terms

A *spread* is a transaction in which one simultaneously buys one option and sells another
option with different terms on the same underlying security. The basic idea: the sale of
one call reduces the risk of buying another.

**Three spread categories:**

- *Vertical spread:* Same expiration date, different striking prices. Example: buy XYZ
  October 30, sell XYZ October 35. This is the standard bull spread structure.
- *Horizontal spread:* Same striking price, different expiration dates. Example: sell XYZ
  January 35, buy XYZ April 35. Also called a calendar spread.
- *Diagonal spread:* Any combination of different strikes and different expirations.

**Credit vs. debit:**

- *Debit spread:* The buy side costs more than the sell side brings in — cash flows out.
  The call bull spread is always a debit spread, since the lower-strike call always trades
  for more than the higher-strike call when both share the same expiration.
- *Credit spread:* The sell side brings in more than the buy side costs — cash flows in.

**Hard prerequisites:**

All spread transactions in which both sides are opening transactions must be done in a
margin account with a minimum equity requirement, generally $2,000.

For the short call in a spread to be considered covered for margin purposes, the long
call must have an expiration date equal to or longer than the short call. A short call
with a longer expiration than the long call is not covered and will be margined as a
naked position.

---

## 1. The Core Structure and Logic of the Bull Spread

In a bull spread, one buys a call at a certain striking price and sells a call at a higher
striking price. Both options generally share the same expiration date — a vertical spread.
A bull spread is profitable if the underlying stock moves up; it has both limited profit
potential and limited risk. The risk can never exceed the net debit. A bull spread requires
a smaller dollar investment and therefore has a smaller maximum dollar loss than an
outright call purchase.

**Two formulas:**

> Break-even point = Lower striking price + Net debit of spread
>
> Maximum profit potential = Higher striking price − Lower striking price − Net debit

**Worked example:** XYZ common at 32. XYZ October 30 call at 3; XYZ October 35
call at 1. Buy the October 30, sell the October 35 at a 2-point net debit.

Break-even = 30 + 2 = **32**
Maximum profit = 35 − 30 − 2 = **3 points ($300)**
Maximum loss = net debit = **2 points ($200)**

**Results at expiration:**

| XYZ Price at Expiration | October 30 Profit | October 35 Profit | Total Profit |
|---|---|---|---|
| 25 | −$300 | +$100 | −$200 |
| 30 | −$300 | +$100 | −$200 |
| 32 | −$100 | +$100 | $0 |
| 35 | +$200 | +$100 | +$300 |
| 40 | +$700 | −$400 | +$300 |
| 45 | +$1,200 | −$900 | +$300 |

The spread has a maximum profit realized if the stock is anywhere above the higher
striking price at expiration. The maximum loss is realized if the stock is anywhere below
the lower striking price at expiration.

The strategist establishing the bull spread is bullish, but not overly so. If he were
rampantly bullish, he would buy the lower-strike call outright. The sale of the higher-
strike call allows the spread to outperform the outright call purchase, dollarwise, as long
as the stock does not rise above the crossover point by expiration. Above that point, the
outright purchase outperforms — there is no limit on the profits of an outright purchase,
while the spread is capped.

> **Annotation:** The bull spread is the natural instrument for the value investor who
> believes in a stock but is uncertain about the magnitude or timing of the move, wants
> to reduce cost basis, and is willing to cap upside at a defined target price. The key
> trade-off: everything above the short strike is forfeited in exchange for a lower
> break-even and smaller maximum dollar loss.

---

## 2. Execution: Spread Orders, Pricing, and the Bid-Ask Problem

**Always enter as a single spread order with a specified net debit limit.** Never leg
into a spread. The floor broker handling the full transaction has the ability to split
quotes on either leg — buying on the bid or selling on the offer — in ways that a retail
investor legging in separately cannot. Legging in removes this advantage and increases
execution risk on both sides.

**Last sale prices do not determine spread execution price.** The only way to determine
the actual market price for a spread is to know the bid and asked prices of both options.

**Worked example:** An investor wants to buy the XYZ October 30 and sell the XYZ
October 35. Last sale prices suggest a 2-point debit. But:

| | Bid | Asked | Last Sale |
|---|---|---|---|
| October 30 call | 3.90 | 4.10 | 4.00 |
| October 35 call | 1.95 | 2.00 | 2.00 |

At market, the spreader pays 4.10 for the October 30 (the ask) and receives only 1.95
for the October 35 (the bid). Actual debit = **2.15 points** — meaningfully more than the
2-point difference in last sale prices suggests. Enter the order at a specified net debit
limit (e.g., 2.10) and allow the broker to work it.

**Liquidity screen:** Restrict spread candidates to options that traded a substantial
number of contracts in the previous session. High trading activity means the bid-ask
spread is more likely to be tight and last sale prices are more likely to be representative.

**Pre-Trade Check — Commission Verification:**
Commissions can represent a significant percentage of the profit and net investment on
a spread and must be calculated before entering a position. McMillan recommends
spreading at least 5 options at a time to reduce commission impact as a percentage of
profit. At typical retail commission rates, spreading fewer contracts on a narrow debit
can render the trade uneconomic.

*Action item:* Verify Fidelity's per-contract commission structure for spread transactions
before sizing any bull spread. Calculate the full round-trip commission cost (both legs,
open and close) and include it in the net debit formula before evaluating whether the
trade is viable. If commissions included in the net debit make the maximum profit
negligible, the trade should not be entered regardless of the thesis.

---

## 3. Degrees of Aggressiveness: Three Types of Bull Spread

**Aggressive (standard) bull spread:** Stock is near or slightly below the lower striking
price when the spread is established. Generally a low-cost spread with substantial
profit potential even after commissions. Most commonly used.

**Extremely aggressive (OTM) bull spread:** Both calls are out-of-the-money. Very
inexpensive to establish with large potential profits — but the underlying stock has only
a remote chance of advancing far enough by expiration, and the spreader can realize a
100% loss even on a moderate advance, since both calls remain OTM. Functionally
equivalent to buying a deeply OTM call outright. Not recommended except as a very
small speculative position.

**Least aggressive (ITM) bull spread:** Both calls are in-the-money. High probability
of realizing maximum profit, though that profit is substantially smaller than aggressive
spreads. The maximum loss requires a large decline in the underlying.

**Worked example of the ITM spread:** XYZ is at 37. October 30 call at 7; October 35
call at 4. Both in-the-money. Spread cost = 3 points. Maximum profit = 2 points,
realized as long as XYZ is anywhere above 35 at expiration — the stock could actually
fall 2 points and maximum profit is still achieved. Maximum loss requires XYZ to fall
7 points below 30. Note: commission costs on ITM spreads are proportionally larger
because higher-priced options are involved; must be calculated before entering.

> **Annotation:** For the conservative value investor, the ITM spread offers the widest
> cushion — maximum profit is earned even on a modest decline from current levels. The
> aggressive (standard) spread is appropriate when the investor has a firm price target
> above current levels and is willing to lose the full net debit if the stock goes nowhere.
> The OTM spread should be avoided except as a small speculative position; it is
> functionally equivalent to buying a deeply OTM call.

---

## 4. The Critical Timing Issue: Bull Spread vs. Outright Call Purchase

Bull spreads are not for traders looking for quick moves. The spread differential changes
mainly as a function of time — small or rapid movements in the underlying stock do not
cause much short-term change in spread value.

**Worked example:** XYZ at 32. Bull spread: long October 30 at 3, short October 35 at
1, net debit = 2 points. Stock jumps to 35 in one day.
- October 30 now worth ~5.50; October 35 now worth ~2.50
- Bull spread value = 3.00 points = **1-point profit** (less two commissions)
- Outright October 30 purchaser: **2.50-point profit** (less one commission)

The outright purchase outperforms on a quick rise. The longer it takes for the stock
to advance, the more the advantage swings to the spread.

**Comparison table:**

| Scenario | Declines | Unchanged | Advances Moderately | Advances Substantially |
|---|---|---|---|---|
| 1 week | Bull spread better | Bull spread better | Outright purchase better | Outright purchase better |
| 1 month | Bull spread better | Bull spread better | Outright purchase better | Outright purchase better |
| At expiration | Bull spread better | Bull spread better | Bull spread better | Outright purchase better |

The spread outperforms the outright call if the stock advances slowly and moderately
by expiration, and always involves fewer actual dollars of risk. The outright purchase
outperforms on a quick move or a sustained large advance.

**Strike distance as a partial remedy:** Using a greater distance between strikes gives
the spread more room to widen even before expiration. When strikes are far apart, a
quick move in the underlying produces more spread widening — though it still won't
reach maximum profit potential immediately. This partially offsets the timing penalty
at the cost of a higher net debit and a higher required stock price for full profit.

> **Annotation:** This is the most important structural trade-off in the chapter. The bull
> spread suits the value investor's core profile precisely: a thesis that requires months to
> play out, a moderate price target, and a preference for lower cost basis over maximum
> upside. If the expected move is large and fast — a hard catalyst, an imminent
> announcement — buy the call outright. If the thesis is "this stock is cheap and will
> re-rate over the next 3–6 months," the bull spread is the better vehicle.
>
> On strike distance: when uncertain whether the move will come quickly or slowly,
> widen the strikes. This reduces the timing penalty at the cost of a higher net debit and
> a higher required stock price for maximum profit.

---

## 5. Ranking Bull Spreads: Incorporate Volatility, Not Maximum Profit

Never rank bull spreads by maximum potential profit at expiration. Such a ranking
always weights deeply OTM spreads most heavily — spreads that can rarely achieve
their maximum profit. Screen out any spread whose maximum profit price is too far
from the current stock price.

**Simple volatility-adjusted screening rule:** Assume the stock can advance by an
amount equal to twice the time value premium in an at-the-money call. Since more
volatile stocks have higher ATM time value premiums, and longer-term options have
more time value premium than short-term options, this single input incorporates both
volatility and duration into the screen. Any spread whose short strike falls beyond this
estimated advance should be excluded from consideration — maximum profit becomes
a low-probability outcome.

Among spreads that pass this screen, rank by percentage return on net debit after
commissions, not by absolute profit. This is the correct comparative metric.

> **Annotation:** This filter has a direct practical application: before entering any bull
> spread, calculate 2× the ATM call's time value premium. That figure is the maximum
> distance the short strike should sit above the current stock price. If the short strike
> is further away than that, the spread is effectively an OTM speculation, not a
> moderate-bullish position. Apply this screen before evaluating any other spread metric.

---

## 6. When Options Are Expensive: The Bull Spread as a Cost-Reduction Tool

Experienced traders turn to bull spreads when implied volatility is elevated and options
are expensive. The sale of the higher-strike call partially offsets the inflated cost of
buying the lower-strike call.

The decision rule is whether the short strike aligns with a realistic price target. If the
investor's thesis implies a target near the short strike, the spread makes sense in high-IV
environments — the short sale meaningfully reduces cost and the cap is acceptable. If
the thesis requires a much larger move well above the short strike, the spread sacrifices
too much upside and the outright call is preferable despite the higher cost.

> **Annotation:** For AI infrastructure names where IV can spike significantly around
> earnings or sector news, this is a live consideration. A bull spread entered during an
> IV spike reduces cost basis; an outright call entered at the same moment pays full
> inflated premium for upside that may never materialize if IV contracts. The spread's
> cost reduction is most valuable precisely when options feel most expensive.

---

## 7. Follow-Up Action: Assignment Risk and Closing the Spread

No mandatory follow-up action is required before expiration given the defined risk on
both sides. Two situations warrant attention:

**Stock advances substantially:** Watch the time value premium in the short call. If time
value premium disappears from the short call, assignment risk increases substantially.
Close the entire spread as a spread transaction — do not leg out. The maximum credit
recoverable equals the difference between the striking prices; in practice, ask for
slightly less (e.g., 4.80–4.90 on a 5-point spread) to obtain a fill.

**Never leg out after a stock price increase** by taking profit on the long side and holding
the short side naked in hopes of a decline. The risk introduced by holding a naked short
call is not consistent with the original position's risk profile.

**Stock declines:** If the short call can be repurchased at a minimal price (⅛ or 1/16),
buying it back locks in the short-side profit while retaining the long call for any
subsequent recovery. Do not repurchase the short call at significant value unless closing
the entire spread.

If the short side of a spread is assigned, the assignment can be satisfied by exercising
the long side of the spread.

---

## 8. Using a Bull Spread to Lower Break-Even on a Stock Loss

A stockholder with an unrealized loss can overlay a bull spread to substantially lower
the break-even price — often at no additional capital outlay. This is one of the most
actionable applications in the playbook.

**Worked example:** Investor owns 100 shares of XYZ purchased at 48. Stock falls to
42. Without options: break-even = 48, requiring a 6-point rally.

Current prices: XYZ October 40 call at 4; XYZ October 45 call at 2.

**Action:** Buy one October 40 call at 4, sell two October 45 calls at 2 each.
Net cost = zero before commissions ($400 credit from short calls = $400 debit for long
call). No naked exposure: one short October 45 is covered by the stock; the other is
part of a bull spread with the long October 40.

**Results at expiration:**

| XYZ at Expiration | Stock Profit | Short Oct 45s | Long Oct 40 | Total |
|---|---|---|---|---|
| 35 | −$1,300 | +$400 | −$400 | −$1,300 |
| 40 | −$800 | +$400 | −$400 | −$800 |
| 42 | −$600 | +$400 | −$200 | −$400 |
| 44 | −$400 | +$400 | $0 | $0 |
| 45 | −$300 | +$400 | +$100 | +$200 |
| 48 | $0 | −$200 | +$400 | +$200 |
| 50 | +$200 | −$600 | +$600 | +$200 |

Break-even lowered from 48 to **44** — only a 2-point rally from 42 required. Below 40,
both strategies produce identical results. Between 40 and 50, the overlay outperforms.
Only above 50 does the original stock-only position outperform — requiring more than
an 8-point rally from 42.

**As an opening trade:** Rather than buying XYZ at 42 outright, an investor could buy
the October 40 and sell two October 45s for even money at the outset. This opening
position is not inferior to owning the stock unless XYZ rises above 46 by expiration —
within that range, the options structure matches or outperforms the stock purchase.

**Follow-up if stock continues to decline:** The short call can be rolled down just as
in a covered write situation — buying back the short October 45 and selling a lower
strike — to adjust the position if the thesis requires more time.

**Pre-condition:** The transaction must be executable at even money or a small debit.
This is most likely when implied volatility is elevated — which is frequently the case
for a beaten-down stock. Always check whether the structure is available at even money
before considering averaging down in stock.

> **Annotation:** Check this structure before averaging down in stock. The zero-cost
> overlay lowers the required recovery substantially without adding downside risk below
> the lower strike. If the premiums allow it, this is strictly superior to buying more
> shares at the current depressed price — lower break-even, same downside below the
> long strike, capped upside above 50 being the only cost.

---

## 9. The Bull Spread as a Covered Write Substitute (Capital Efficiency)

When a deeply in-the-money call exists with little or no time premium remaining, its
purchase can substitute for buying the stock — the profit and loss profile of a deep ITM
call closely mirrors stock ownership. Selling a call closer to the money against it creates
a bull spread with covered write characteristics at a fraction of the capital required.

**Worked example:** XYZ common at 49. April 50 call at 3; April 35 call at 14 (at parity
— no time premium). Buy the April 35 at 14, sell the April 50 at 3. Net debit = $1,100.

**Comparison to covered write (buy stock at 49, sell April 50 at 3):**

| Metric | Covered Write | Bull Spread |
|---|---|---|
| Maximum profit (stock above 50) | $400 | $400 |
| Break-even point | 46 | 46 |
| Capital required | $4,600 | $1,100 |
| Maximum loss potential | Unlimited below 46 | $1,100 |

The remaining $3,500 not deployed in the spread can be placed in interest-bearing
securities — effectively replacing the dividend income forfeited by not owning the stock
outright. The spread offers the same dollar rewards, the same break-even, smaller
commission costs, less potential risk, and interest income from the freed capital.

**Caution:** The covered writer still owns the stock after a severe market decline. The
bull spread can be entirely wiped out in a moderate decline. This structure should be
a partial allocation — smaller capital in the spread, balance in interest-bearing
securities — not a wholesale replacement of covered writing.

**Pre-condition:** A deeply ITM call trading at or near parity. Most commonly found in
LEAPS on stocks that have already moved significantly, or in shorter-term options after
a large run-up. Screen for this structure on any covered write candidate before
committing full capital to the stock position.

> **Annotation:** When this structure is available, it is unambiguously superior to the
> covered write on every metric except one: the covered writer retains the stock in a
> crash. For AI infrastructure names where a large capital commitment to a single stock
> carries meaningful binary risk, the capital efficiency of this structure — same upside,
> defined maximum loss, freed capital earning interest — is directly aligned with the
> risk-reduction objective of the overall options program.
```

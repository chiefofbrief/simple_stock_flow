# Chapter 2: Covered Call Writing — Extracted Insights

---

## The Core Mechanics

"Covered call writing is the name given to the strategy by which one sells a call option while simultaneously owning the obligated number of shares of underlying stock." The writer should be mildly bullish, or at least neutral, toward the underlying stock. "By writing a call option against stock, one always decreases the risk of owning the stock."

The profit potential and break-even point are summarized by two formulas:

**Maximum profit potential = Strike price − Stock price + Call price**
**Downside break-even point = Stock price − Call price**

McMillan's base example, which all subsequent examples build on:
- Buy 100 XYZ at 48, sell XYZ July 50 call at 3
- Maximum profit: 50 − 48 + 3 = **5 points ($500)**
- Downside break-even: 48 − 3 = **45**
- If XYZ is below 50 at expiration, the call expires worthless and the investor keeps the $300 premium
- If XYZ rises to 60, the investor can either let the stock be called away at 50 (total profit = $300 + $200 = $500) or buy back the call at 10 (losing $700 on the option but retaining a 12-point unrealized stock gain — total profit still $500)

Table 2-1 (XYZ July 50 call, stock purchased at 48, call sold at 3):

| XYZ Price at Expiration | Stock Profit | Call Profit | Total Profit |
|-------------------------|--------------|-------------|--------------|
| 40                      | −$800        | +$300       | −$500        |
| 45                      | −300         | +300        | 0            |
| 48                      | 0            | +300        | +300         |
| 50                      | +200         | +300        | +500         |
| 55                      | +700         | −200        | +500         |
| 60                      | +1,200       | −700        | +500         |

"The strategy of owning the stock and writing the call will outperform outright stock ownership if the stock falls, remains the same, or even rises slightly. In fact, the only time that the outright owner of the stock will outperform a covered writer is if the stock increases in price by a relatively substantial amount during the life of the call."

---

## In-the-Money vs. Out-of-the-Money Writes

"In general, out-of-the-money covered writes offer higher potential rewards but have less risk protection than do in-the-money covered writes. In-the-money writes are more defensive covered writing positions."

McMillan's comparison example — XYZ at 45, two options considered:
- XYZ July 40 (ITM) selling at 8
- XYZ July 50 (OTM) selling at 1

"The in-the-money covered write of the July 40 affords 8 points, or nearly 18% protection down to a price of 37 (the break-even point) at expiration. The out-of-the-money covered write of the July 50 offers only 1 point of downside protection at expiration."

Table 2-2:

| In-the-Money Write (July 40) | | Out-of-the-Money Write (July 50) | |
|---|---|---|---|
| **Stock at Expiration** | **Total Profit** | **Stock at Expiration** | **Total Profit** |
| 35 | −$200 | 35 | −$900 |
| 37 | 0 | 40 | −400 |
| 40 | +300 | 44 | 0 |
| 45 | +300 | 45 | +100 |
| 50 | +300 | 50 | +600 |
| 60 | +300 | 60 | +600 |

Key observation from the table: the ITM write attains its maximum profit anywhere between 40 and 60 — even a 5-point decline still produces maximum profit. The OTM write requires a rise in price to reach maximum profit.

"Realizing the maximum profit potential with an out-of-the-money covered write always requires a rise in price by the underlying stock."

"One can construct a more aggressive position by writing an out-of-the-money call. One's outlook for the underlying stock should be bullish in that case. If one is neutral or moderately bearish on the stock, an in-the-money covered write is more appropriate. If one is truly bearish on a stock he owns, he should sell the stock instead of establishing a covered write."

"Should the stock remain the same or decline in price, the out-of-the-money write will generally underperform the in-the-money write. This is why the return if unchanged is a good comparison."

---

## The Total Return Concept

"The total return concept represents the true strategy in covered writing, whereby one views the entire position as a single entity and is not predominantly concerned with the results of his stock ownership."

"Those who believe in the total return concept of covered writing consider both downside protection and maximum potential return as important factors and are willing to have the stock called away, if necessary, to meet their objectives. When premiums are moderate or small, only in-the-money writes satisfy the total return philosophy."

"A true conservative covered write is one in which the total position is conservative — offering reduced risk and a good probability of making a profit. An in-the-money write, even on a stock that itself is not conservative, can become a conservative total position when the option itself is properly chosen."

McMillan's conservative write example — XYZ at 45, July 40 call at 8:
- Net cash investment: $4,500 − $800 = **$3,700**
- Maximum profit potential: **$300**
- Return: $300 / $3,700 = **just over 8% for the period** (well in excess of 10% annualized)
- Downside protection: 8 points, or about 18%
- "The total position is an investment that will not lose money unless XYZ common stock falls by more than 8 points, or about 18%; and is an investment that could return the equivalent of 10% annually should XYZ common stock rise, remain the same, or fall by 5 points (to 40). This is a conservative position."

"In a strategic sense, the total position described above is better and more conservative than one in which a writer buys a conservative stock — yielding perhaps 6 or 7% — and writes an out-of-the-money call for a minimal premium."

---

## Computing Return on Investment: The Three Required Metrics

"One should always know exactly what his potential returns are, including all costs, when he establishes a covered writing position."

McMillan identifies three statistics every covered writer must compute before entering a position:

1. **Return if exercised** — the return if the stock is called away
2. **Return if unchanged** (also called the *static return*) — "the return that would be realized if the underlying stock were unchanged when the option expired"
3. **Downside break-even point** — "the exact downside break-even point after all costs are included"

"In general, the annualized return if unchanged should be used as the comparative measure between various covered writes." This metric requires no assumption about stock price movement, making it the fairest comparison between ITM and OTM writes.

McMillan's full worked example — **buy 500 XYZ at 43, sell 5 XYZ July 45 calls at 3** (6-month call, cash account, commissions included at 3¢/share stock and $5/option contract):

**Table 2-3: Net Investment Required — Cash Account**

| | |
|---|---|
| Stock cost (500 shares at 43) | $21,500 |
| Plus stock purchase commissions | +15 |
| Less option premiums received | −1,500 |
| Plus option sale commissions | +25 |
| **Net cash investment** | **$20,040** |

**Table 2-4: Return if Exercised — Cash Account**

| | |
|---|---|
| Stock sale proceeds (500 shares at 45) | $22,500 |
| Less stock sale commissions | −15 |
| Plus dividends earned until expiration | +500 |
| Less net investment | −20,040 |
| **Net profit if exercised** | **$2,945** |

Return if exercised = $2,945 / $20,040 = **14.7%**

**Table 2-5: Return if Unchanged — Cash Account**

| | |
|---|---|
| Unchanged stock value (500 shares at 43) | $21,500 |
| Plus dividends | +500 |
| Less net investment | −20,040 |
| **Profit if unchanged** | **$1,960** |

Return if unchanged = $1,960 / $20,040 = **9.8%**

Note: no stock sale commission is included in the return if unchanged calculation, because in most cases one would continue to hold the stock and write another call.

**Table 2-6: Downside Break-Even Point — Cash Account**

| | |
|---|---|
| Net investment | $20,040 |
| Less dividends | −500 |
| Total stock cost to expiration | $19,540 |
| Divide by shares held | ÷500 |
| **Break-even price** | **39.08** |

**Table 2-7: Percent Downside Protection — Cash Account**

| | |
|---|---|
| Initial stock price | 43 |
| Less break-even price | −39.08 |
| Points of protection | 3.92 |
| Divide by original stock price | ÷43 |
| **Percent downside protection** | **9.1%** |

The same position on **margin** (50% margin rate, 10% annual interest):
- Net margin investment: **$9,283**
- Return if exercised: $2,407 / $9,283 = **25.9%**
- Return if unchanged: $1,422 / $9,283 = **15.3%**
- Break-even point — margin: **40.16** (higher than cash break-even of 39.08 due to margin interest charges)
- Percent downside protection — margin: **6.6%**

"The return on margin will always be higher than the return from cash" unless a fairly deep in-the-money write is being considered. However, "since the break-even point on margin is higher than that on cash, there is less percent downside protection in a margin covered write."

---

## What a Difference a Dime Makes

"Entering a covered writing order at the market may not be a prudent thing to do, especially if one's calculations for the potential returns are based on last sales or on closing prices in the newspaper."

Table 2.13 shows the effect of execution slippage on the same 500-share position:

| | Buy 43 / Sell 3 | Buy 43.10 / Sell 3 | Buy 43.10 / Sell 2.90 |
|---|---|---|---|
| Return if exercised | 14.7% cash / 25.9% margin | 14.4% cash / 25.3% margin | 14.1% cash / 24.6% margin |
| Return if unchanged | 9.8% cash / 15.3% margin | 9.8% cash / 15.3% margin | 9.5% cash / 14.7% margin |
| Break-even point | 39.08 cash / 40.16 margin | 39.18 cash / 40.26 margin | 39.28 cash / 40.36 margin |

McMillan's punchline: "Writing against 300 shares at those prices (43 for the stock and 3 for the call) is approximately the same return as writing against 500 shares if the stock costs 43.10 and the option brings in 2.90." Slippage of a dime on each leg effectively negates the benefit of the larger position size.

---

## Selecting a Covered Writing Position: The Conservative Guidelines

"In a conservative option writing strategy, one should be looking for minimum returns if unchanged of 1% per month, with downside protection of at least 10%, as general guidelines. Employing such criteria automatically forces one to write in-the-money options in line with the total return concept."

A 3-month write must offer at least 3% return if unchanged; a 6-month write at least 6%. "During periods of expanded option premiums, there may be so many writes that satisfy this criterion that one would want to raise his sights somewhat, say to 1½% or 2% per month."

McMillan recommends maintaining two ranked lists:
- List 1: ranked by annualized return if unchanged, showing all writes that afford at minimum 10% downside protection
- List 2: ranked by percentage downside protection, showing all writes that meet at least 12% annualized return if unchanged

"If premium levels shrink and the lists become quite small on a daily basis, one might consider expanding the criteria to view more potential situations. On the other hand, if premiums expand dramatically, one might consider using more restrictive criteria."

**On volatility and protection:** "It makes no sense to quote percent protection without knowing the volatility of the underlying stock. For example, 10% protection on AT&T is quite a bit more protection than the same percentage on a much more volatile stock, like Google."

**On stock selection:** "One does not necessarily have to be bullish on the underlying stock to take a covered writing position. As long as one does not foresee a potential decline in the underlying stock, he can feel free to establish the covered writing position." But: "If one is bearish, he should not take a covered writing position on that stock, regardless of the levels of protection that can be obtained." And more broadly: "One should not establish a covered write on a stock that he does not want to own."

**The long-term performance caveat:** "There is some mathematical basis to believe, in the long run, that moderately out-of-the-money covered writes will perform better than in-the-money writes." However, in falling or static markets the OTM writer has more risk. The ITM write appeals to investors "looking to earn a relatively consistent, moderate rate of return" and is consistent with preservation of capital.

---

## The Combined Write: Diversifying Return and Protection

When neither the ITM nor OTM write alone satisfies both return and protection criteria, McMillan proposes writing half the position against each.

"The writer may often do best by writing half of his position against in-the-moneys and half against out-of-the-moneys on the same stock. This is especially attractive for a stock whose out-of-the-money calls do not appear to provide enough downside protection, and at the same time, whose in-the-money calls do not provide quite enough return."

Example — XYZ at 42, 1,000 shares, 6-month calls:
- XYZ April 40 call at 4 (ITM)
- XYZ April 45 call at 2 (OTM)

Table 2.14:

| | ITM Write (10 April 40s) | OTM Write (10 April 45s) | Combined (5 each) |
|---|---|---|---|
| Return if exercised | 7.6% | 14.7% | 11.2% |
| Return if unchanged | 7.6% | 7.3% | 7.4% |
| Percent protection | 11.7% | 7.0% | 9.3% |

"The combined write — half of the position against the April 40s and the other half against the April 45s — offers the best balance of return and protection." The ITM write alone provides over 11% downside protection but only 1% per month return. The OTM write alone offers over 2% per month return but only 7% protection. The combined write offers nearly 1.5% per month and over 8% protection.

"The 'combined' write frees the covered writer from having to initially take a bearish (in-the-money write) or bullish (out-of-the-money write) posture on the stock if he does not want to. This is often necessary on a low-volatility stock trading between striking prices."

---

## Execution: Always Use a Net Order

"A simultaneous transaction of buying the stock and selling the option is the only way of assuring that both sides of the covered write are established at desired price levels. If one 'legs' into the position — that is, buys the stock first and then attempts to sell the option, or vice versa — he is subjecting himself to a risk."

"What the covered writer really wants to do is ensure that his net price is obtained. If he wants to buy stock at 43 and sell an option at 3, he is attempting to establish the position at 40 net. He normally would not mind paying 43.10 for the stock if he can sell the call at 3.10, thereby still obtaining 40 net."

A net covered writing order must be placed either directly with a brokerage firm's option desk or through the spread order entry system of an online broker. "Make sure your brokerage firm offers the placement of 'net' orders — either online or directly through an order desk." Note that there is no guarantee a net order will be filled — it is always a "not held" order.

---

## The Critical Word of Caution: Do Not Write Against Stock You Won't Sell

"Writing calls against stock that you have no intention of selling is tantamount to writing naked calls."

"If a stockholder is going to be frustrated and disappointed when he is not fully participating during a rally in his stock, he should not write a call in the first place."

McMillan describes the failure mode in full: an investor who refuses to let stock be called away will roll up for debits whenever the stock rises. If the stock is particularly strong, "these rolls for debits begin to weigh heavily on the psychology of the covered writer. Eventually, he wears down emotionally and makes a mistake." He either buys back all the calls for a large debit, leaving the entire position exposed after a large run-up, or begins selling OTM naked puts to bring in credits — "even worse, because the entire position is now leveraged tremendously, and a sharp drop in the stock price may cause horrendous losses."

"The best way to avoid this type of potentially serious mistake is to allow the stock to be called away at some point." If that is not feasible due to tax considerations or emotional ties: "One should be very cautious about writing covered calls against stocks that he doesn't intend to sell... perhaps buying a protective put would be a better strategy for such a stockholder."

**For the value investor:** This warning is particularly sharp. A value investor who has conviction on a name and doesn't want upside capped should not write covered calls against it — or should use the incremental return concept described below. Writing covered calls on a position you intend to hold indefinitely is not a conservative income strategy; it is an emotionally destabilizing one.

---

## Writing Against Stock Already Owned

When comparing returns on owned stock against potential writes on other stocks, McMillan notes that standard computer-generated ranked lists assume stock is purchased new. "One should note that such lists generally assume that stock is bought in order to establish the covered write; the returns are usually not computed and published for writing against stock already held."

The correct comparison: calculate returns on the owned stock as if no entry commission were paid, then compare those with the full-cost returns on the new stock. Commission costs for selling one stock and buying another may alter returns substantially enough that writing against the already-owned stock is preferable.

"The writer should pursue the best overall total return covered write. In fact, it can be a lethargic mistake to get lured into just writing against the same stock, month after month, or quarter after quarter, even if the returns have diminished."

---

## Follow-Up Action: The Three Categories

"Establishing a covered write, or any option position for that matter, is only part of the strategist's job. Once the position has been taken, it must be monitored closely so that adjustments may be made should the stock drop too far in price."

Follow-up action divides into three categories:
1. Protective action if the stock drops
2. Aggressive action when the stock rises
3. Action to avoid assignment when time premium disappears from an in-the-money call

---

## Protective Action: Rolling Down

"Follow-up action is generally taken by buying back the call that was originally written and then writing another call, with a different striking price and/or expiration date, in its place. Any adjustment of this sort is referred to as a rolling action. When the underlying stock drops in price, one generally buys back the original call — presumably at a profit since the underlying stock has declined — and then sells a call with a lower striking price. This is known as rolling down."

McMillan's example — buy XYZ at 51, sell XYZ January 50 call at 6:
- Maximum profit potential: 5 points. Downside protection: 6 points (break-even at 45)
- Stock declines to 45 over two months. Current prices: XYZ January 50 call at 1; XYZ January 45 call at 4
- Roll down: buy back January 50 at 1, sell January 45 at 4 — net **credit of 3 points**
- New downside break-even: **42**
- If XYZ remains at 45 at January expiration, the rolled position makes an additional $300 vs. only $100 remaining from the original call

"Rolling down gives more downside protection against a further drop in stock price and may also produce additional income if the stock price stabilizes."

Table 2.15:

| XYZ Price at Expiration | Profit from January 50 Write | Profit from Rolled Position |
|---|---|---|
| 40 | −$500 | −$200 |
| 42 | −300 | 0 |
| 45 | 0 | +300 |
| 48 | +300 | +300 |
| 50 | +500 | +300 |
| 60 | +500 | +300 |

"Consequently, the only case in which it does not pay to roll down is the one in which the stock experiences a reversal — a rise in price after the initial drop."

"Rolling down generally reduces the maximum profit potential of the covered write." In the example, rolling to the January 45 caps profits above 45 rather than above 50.

**When to roll:** "Technical support levels of the stock are often useful in selecting prices at which to roll down. If one rolls down after technical support has been broken, the chances of being caught in a stock-price-reversal situation would normally be reduced."

**The covered writer should place rolling orders as spread orders:** "The covered writer should be aware that whenever he rolls his position, the order can be placed as a spread order. This will normally help the writer to obtain a better price execution."

---

## The Locked-In Loss

A sudden steep decline can force a locked-in loss — "there is no option to which the writer can roll down that will provide him with enough premium to realize any profit if the stock were then called away at expiration."

McMillan's example — buy XYZ at 20, sell January 20 call at 2. Stock drops quickly to 16:
- XYZ January 20 call: 0.50
- XYZ January 15 call: 2.50

Rolling down from January 20 to January 15: buy at 0.50, sell at 2.50 — net credit of 2 points.

If XYZ is called away above 15:
- Stock loss: 20 − 15 = **5 points**
- Option profits: 1.50 (January 20) + 2.50 (January 15) = **4 points**
- **Net result: 1-point loss — the best possible outcome**

Table 2.16:

| Stock Price at Expiration | Profit from January 20 Write | Profit from Rolled Position |
|---|---|---|
| 10 | −$800 | −$600 |
| 15 | −300 | −100 |
| 18 | 0 | −100 |
| 20 | +200 | −100 |
| 25 | +200 | −100 |

"Even considering what has been shown about this loss, it is still correct for this writer to roll down to the January 15." The rolled-down position outperforms the original position unless the stock rallies back above 17 by expiration.

"Although it is not emotionally satisfying to be in an investment position that cannot produce a profit — at least for a limited period of time — it may still be beneficial to roll down to protect as much of the stock price decline as possible."

**Prevention:** "Perhaps the best way to avoid having to lock in losses would be to establish positions that are less likely to become such a problem. In-the-money covered writes on higher-priced stocks that have a moderate amount of volatility will rarely force the writer to lock in a loss by rolling down."

---

## The Partial Roll-Down

To avoid locking in a loss while still gaining some additional protection, roll down only part of the position.

Example continued — 1,000 shares XYZ at 20, 10 January 20 calls at 2. Stock falls to 16. Instead of rolling all 10 calls, the writer buys back only 5 January 20s and sells 5 January 15s:
- Realized gain from 5 January 20s: **$750**
- Remaining position: long 1,000 XYZ, short 5 January 20s, short 5 January 15s

If XYZ rallies back above 20: sell 500 XYZ at 20 (break even) + 500 at 15 (−$2,500 stock loss), offset by $1,000 from January 20s + $1,250 from January 15s + $750 realized gain = **$3,000 option profits vs. $2,500 stock losses = net gain of $500**.

Table 2-17 (stock at 15 at expiration):

| Strategy | Stock Loss | Option Profit | Total Loss |
|---|---|---|---|
| Original position | −$5,000 | +$2,000 | −$3,000 |
| Partial roll-down | −5,000 | +3,000 | −2,000 |
| Complete roll-down | −5,000 | +4,000 | −1,000 |

"The covered writer who would like to roll down, but who does not want to lock in a loss or who feels the stock may rebound somewhat before expiration, should consider rolling down only part of his position. If the stock should continue to drop, making it evident that there is little hope of a strong rebound back to the original strike, the rest of the position can then be rolled down as well."

**Expiration timing when rolling down:**
- Roll into a more distant expiration when fundamentally or technically concerned: more points of protection but reduces maximum profit potential for longer
- Roll into a near-term expiration when locking in a loss: "The best strategy may be to roll down into the near-term call, planning to capture one point of time premium in 3 months. In this way, he will be beginning to work himself out of the loss situation by availing himself of the most potential time premium decay in the shortest period of time."

---

## Aggressive Action: Rolling Up

When the stock rises sharply, the writer can roll up to a higher strike to increase profit potential — but at the cost of raising the break-even point.

McMillan's example — buy stock at 50, sell 6-month July 50 call at 6:
- Maximum profit: 6 points above 50. Break-even: 44
- Stock rallies to 60. July 50 now at 11, July 60 at 7

Roll up: buy back July 50 at 11, sell July 60 at 7 — **debit of 4 points**

- New break-even: 44 + 4 = **48**
- New maximum profit: 6 (original July 50 credit) + 7 (July 60 credit) − 11 (July 50 buyback) + 10 (stock gain to 60) = **12 points above 60**
- The original and rolled-up positions are equal at **54** at expiration

"Note that when one rolls up, there is a debit incurred. That is, the investor must deposit additional cash into the covered writing position."

"In summary, it can be said that rolling up increases one's profit potential but also exposes one to risk of loss if a stock price reversal should occur. Generally, it is not advisable to roll up if at least a 10% correction in the stock price cannot be withstood. One's initial goals for the covered write were set when the position was established. If the stock advances and these goals are being met, the writer should be very cautious about risking that profit."

**Rolling up for a credit at expiration:** On volatile stocks, it is occasionally possible to roll up to a higher strike at expiration for a credit rather than a debit. Example: XYZ at 50 at January expiration, January 45 call at 5, July 50 call at 7. Rolling from January 45 to July 50 generates a **2-point credit**. "Whenever one can roll up for a credit, a situation that would normally arise only on more volatile stocks, he should do so."

---

## Closing a Parity Write Early

When a written call has gone deeply in-the-money and trades at parity with zero time premium remaining, McMillan recommends closing the entire position rather than waiting out the remaining time.

Example: bought XYZ at 25, sold 6-month July 25 call at 3 (net cost 22). Three months later, XYZ has risen to 33 and the call is trading at 8 (parity).

Action: sell stock at 33, buy back call at 8 — effective net of 25 = maximum profit potential realized.

"The advantage of closing a parity covered write early is that one is realizing the maximum return in a shorter period than anticipated. He is thereby increasing his annualized return on the position."

Minor costs: additional commission on the option buy-back, possible loss of remaining dividend. In most cases these are small relative to the improvement in annualized return.

"One should place the order to close the position with his brokerage firm's option desk, to be executed as a 'net' order."

---

## Rolling Forward: Action at or Near Expiration

As expiration approaches and time premium disappears, the writer should consider rolling forward — buying back the current call and selling a longer-term call at the same strike.

**For in-the-money calls:** "The optimum time to roll forward is generally when the time value premium has completely disappeared from the call." Once the call trades at parity or a discount, arbitrageurs may exercise. Roll forward before this happens.

**For out-of-the-money calls:** Compare return per day. Roll forward when the longer-term call offers a higher daily return.

McMillan's per-day return example — 5 January 30 calls against 500 XYZ at 29.50, one month before expiration:
- January 30 call at 0.50; April 30 call at 2.50
- Commissions for rolling: approximately $100
- January 30: $250 remaining premium / 30 days = **$8.33/day**
- April 30: (5 × $250 − $100 commissions) / 120 days = $1,150 / 120 = **$9.58/day**
- Conclusion: roll forward to the April 30

"Rolling forward, since it involves a positive cash flow (that is, it is a credit transaction) simultaneously increases the writer's maximum profit potential and lowers the break-even point."

**Individual investor note:** "The individual or relatively small investor who owns only enough stock to write one series of options should generally not write the longest-term calls for this very reason. He may not be obtaining a particularly attractive level of premiums, but may feel he is forced to retain the position until expiration. Thus, he could be in a relatively poor write for as long as 9 months."

---

## When to Let Stock Be Called Away

Letting stock be called away is generally the wisest strategy when both of the following criteria are met:

1. Rolling forward offers only a minimal return
2. Rolling up and forward significantly raises the break-even point and leaves the position relatively unprotected should the stock drop in price

McMillan's example: covered write established at XYZ 49, April 50 call at 3 (break-even 46). Near expiration, XYZ has risen to 56. Available options: October 50 at 7 (only 1 point of time premium remaining); October 60 at 2.
- Rolling forward to October 50: makes at most 1 additional point — "an extremely low rate of return"
- Rolling up to October 60: costs 4 points (buy April 50 at 6, sell October 60 at 2), raising break-even from 46 to 50, with only 2 points of protection from current price of 56

"At this point, the writer has exhausted his alternatives for rolling. His remaining choice is to let the stock be called away and to use the proceeds to establish a covered write in a new stock, one that offers a more attractive rate of return with reasonable downside protection."

---

## The Partial Extraction Strategy

For investors who own appreciated stock with a low cost basis and face imminent assignment but do not want to sell all their shares, McMillan describes the partial extraction strategy: sell a portion of the stock to fund the buy-back of the written calls at zero net cost.

Example: long 3,000 XYZ at 50, short 30 February 45 calls at 5.00. Time premium has disappeared — assignment is imminent.

Action:
- Buy back 30 February 45 calls at 5.00 — cost: **$15,000**
- Sell 300 shares of XYZ at 50 — proceeds: **$15,000**
- Net cost: **zero**

Result: 2,700 shares remain unencumbered. The writer can then decide whether to sell calls against those shares or not.

Tax note: the option trade likely generates a short-term loss; the stock sale generates a long-term gain. The option loss can be applied against the stock gain, reducing net tax exposure.

"It should be used before the written call gets too deeply in the money. If one waits until the option gets very deeply in-the-money before applying the technique, then a much larger number of shares will have to be sold in order to extract the stock from the covered write."

---

## The Incremental Return Concept (Rolling for Credits)

For investors who want to participate in stock appreciation to a target price while simultaneously generating positive cash flow from option writing, McMillan describes the incremental return concept.

"The incremental return concept of covered call writing is a way in which the covered writer can earn the full value of stock appreciation between today's stock price and a target sale price, which may be substantially higher. At the same time, the writer can earn an incremental, positive return from writing options."

The foundation: "Write against only a part of the entire stock holding initially, and to write these calls at the striking price nearest the current stock price. Then, should the stock move up to the next higher striking price, one rolls up for a credit by adding to the number of calls written. Rolling for a credit is mandatory and is the key to the strategy."

McMillan's example — 1,000 shares XYZ at 60, target price 80:

Table 2.20:

| Action | Net Credit/Debit |
|---|---|
| **Day 1: XYZ = 60** | |
| Sell 3 XYZ October 60s at 7 | +$2,100 credit |
| **One month later: XYZ = 70** | |
| Buy back 3 Oct 60s at 11 | −$3,300 debit |
| Sell 5 Oct 70s at 7 | +$3,500 credit |
| **Two months later: XYZ = 80** | |
| Buy back 5 Oct 70s at 11 | −$5,500 debit |
| Sell 10 Oct 80s at 6 | +$6,000 credit |
| **Total net option credits** | **+$2,800** |

If XYZ remains above 80, all 1,000 shares are called away at the target price of 80 — the investor captures full appreciation from 60 to 80 plus $2,800 in option credits.

In a flat market, if a written call loses its time premium, the writer rolls forward to a more distant expiration at the same strike, keeping quantity constant and generating additional credits.

"If the target price is eventually reached, and the writer then decides that he wants to retain some of the stock, the 'partial extraction strategy' described earlier can be used when the written calls begin to lose their time value premium. Once the position is 'extracted,' a new, higher target can be set and the whole process begun once again."

**Minimum position size:** McMillan recommends at least 500 shares, preferably 1,000 or more, to make the strategy workable.

**Takeaway for the value investor:** The incremental return concept resolves the core tension between conviction and covered call writing. If you own an undervalued stock and believe it will reach a specific higher price, this strategy lets you participate fully in that appreciation while generating income along the way — provided you commit to letting the stock be called away at the target.

# Chapter 15: Put Option Basics — Extracted Insights for the Conservative Options Playbook

---

## Foundational Definition: What "In-the-Money" Means for Puts

The broad definition of an in-the-money option — an option that has intrinsic value —
covers both puts and calls. For calls, intrinsic value exists when the stock is above the
strike. For puts, intrinsic value exists when the stock is below the strike.

**Intrinsic value formulas:**

> Intrinsic value (call) = Stock price − Striking price (when stock is above strike)
>
> Intrinsic value (put) = Striking price − Stock price (when stock is below strike)

**ITM/OTM definitions — reversed for puts vs. calls:**

- A put is in-the-money when the underlying stock is *below* the striking price.
- A put is out-of-the-money when the underlying stock is *above* the striking price.

If XYZ is at 45: the July 50 put is in-the-money (stock below strike); the July 50 call
is out-of-the-money (stock below strike). If XYZ is at 55: the July 50 put is
out-of-the-money; the July 50 call is in-the-money.

---

## 1. Core Put Option Mechanics: The Mirror Image of Calls (With Key Differences)

In many respects, put strategies are the near-opposite of corresponding call strategies.
However, a put is not exactly the opposite of a call — the differences matter and are
detailed throughout this chapter.

The outright buyer of a put is hoping for a stock price decline. If the stock declines
well below the striking price, the put holder can buy stock in the open market and
exercise the put to sell that stock at the higher striking price, realizing a profit.

**Example:** XYZ is at 40. An XYZ July 50 put is worth at least 10 points — it grants
the right to sell XYZ at 50, which is 10 points above the current price. If the stock is
above the striking price at expiration, the put expires worthless.

**The same six pricing factors that govern calls govern puts:**

1. Price of the underlying stock
2. Striking price of the option
3. Time remaining until expiration
4. Volatility of the underlying stock
5. Dividend rate of the underlying stock
6. Current risk-free interest rate

The non-linear decay rule carries over: time value premium decays more rapidly in the
weeks immediately preceding expiration. The more volatile the underlying stock, the
higher the price of its puts and calls. The marketplace may at any time value options at
a higher or lower volatility than the stock actually exhibits — this is implied volatility,
as distinguished from actual (historical) volatility. Both concepts apply identically to
puts and calls.

**Exercise and assignment mechanics:**

When the holder of a put exercises, he sells stock at the striking price. The writer of a
put with the same terms is assigned an obligation to buy stock at the striking price.
This is the reverse of calls: the call holder exercises to buy stock; the call writer is
obligated to sell.

*Options available to the put holder upon exercise:*
- Sell stock already held in the portfolio at the striking price via exercise.
- Buy stock in the open market and immediately exercise the put to sell it at the
  higher striking price, capturing the spread.
- Short the underlying stock by exercising the put — delivering borrowed shares at
  the striking price. Requires ability to borrow the stock and margin collateral for
  the short sale.

*Options available to the put writer upon assignment:*
- Use the received stock to cover an existing short position in the underlying.
- Immediately sell the received stock in the open market.
- Retain the stock in the portfolio, paying for or margining it accordingly.

---

## 2. Time Value Premium for Puts: Formulas and the Key Asymmetry vs. Calls

> **Time value premium (in-the-money put)** = Put price + Stock price − Striking price
>
> **Time value premium (in-the-money call)** = Call price + Striking price − Stock price

In both cases, time value premium is the excess of option price over intrinsic value.

**Example:** XYZ is at 47 and the XYZ July 50 put is at 5. Intrinsic value = 50 − 47 = 3.
Time value premium = 5 + 47 − 50 = **2 points**.

The time value premium of a put is largest when the stock is at the striking price. As
the option becomes deeply in-the-money or deeply out-of-the-money, time value premium
shrinks substantially — identical to the behavior of calls.

**TABLE 15-1. Call and put options compared (XYZ July 50):**

| XYZ Stock Price | Call Price | Call Intrinsic | Call TVP | Put Price | Put Intrinsic | Put TVP |
|---|---|---|---|---|---|---|
| 40 | .50 | 0 | .50 | 9.75 | 10 | −.25* |
| 43 | 1 | 0 | 1 | 7 | 7 | 0 |
| 45 | 2 | 0 | 2 | 6 | 5 | 1 |
| 47 | 3 | 0 | 3 | 5 | 3 | 2 |
| **50** | **5** | **0** | **5** | **4** | **0** | **4** |
| 53 | 7 | 3 | 4 | 3 | 0 | 3 |
| 55 | 8 | 5 | 3 | 2 | 0 | 2 |
| 57 | 9 | 7 | 2 | 1 | 0 | 1 |
| 60 | 10.50 | 10 | .50 | .50 | 0 | .50 |
| 70 | 19.75 | 20 | −.25* | .25 | 0 | .25 |

*A deeply in-the-money option may trade at a discount from intrinsic value in advance
of expiration.

**Two structural facts from Table 15-1:**

**First:** The call generally sells for more than the put when the stock is at the strike.
With XYZ at 50, the call is worth 5 and the put is worth only 4. This is true in general,
except for stocks paying large dividends. The reason is the cost of carrying long stock,
enforced by arbitrage (see Section 5).

**Second — the critical asymmetry:** An in-the-money put loses time value premium
more quickly than an in-the-money call does. In Table 15-1, with XYZ at 43 (put 7
points ITM), the put has already lost all time value premium. But when the call is 7
points ITM (XYZ at 57), the call still retains 2 points of time value premium.

The reverse is also true: an out-of-the-money put holds time value premium better than
an out-of-the-money call does.

> **Annotation:** These two asymmetries have direct strategic implications. For
> protective puts: an ITM put bought as insurance sheds time value faster than an
> equivalent ITM call gains value on the upside. Once the stock falls far enough to push
> a protective put deep ITM, the remaining time value cushion is thin — the decision to
> roll down, sell, or exercise becomes urgent. Do not assume a deep ITM put retains
> meaningful optionality; check the time value premium directly.
>
> For OTM protective puts: the slower decay relative to OTM calls means the insurance
> cost is not front-loaded. An OTM put retains value longer if the stock drifts sideways
> rather than declining immediately, making it a more forgiving hedge than an equivalent
> OTM call position would be on the other side.

---

## 3. The Effect of Dividends on Put Premiums

Dividends are a negative factor on call option prices. The opposite is true for puts:
the larger the dividend, the more valuable the puts. When a stock goes ex-dividend,
its price is reduced by the amount of the dividend — the stock decreases in price, the
put becomes more valuable, and both buyers and sellers adjust put premiums accordingly.
Listed puts are not adjusted for cash dividend payments, but the option price itself
reflects the expected dividend payments.

**Example:** XYZ is at $25 and will pay $1 in dividends over the next 6 months. A
6-month put with strike 25 should automatically be worth at least $1: the stock will be
reduced in price by $1 in dividends over that period, leaving it at 24 and the put 1 point
in-the-money at minimum.

**Pre-ex-date rule:** On the day before a stock goes ex-dividend, the time value premium
of an in-the-money put should be at least as large as the impending cash dividend. If
XYZ is at 40 and is about to pay a $0.50 dividend, an XYZ January 50 put should sell
for at least 10.50 — because the stock will be reduced by $0.50 on the ex-dividend day,
and the put price must reflect that anticipated reduction.

> **Annotation:** For the value investor holding dividend-paying stocks, the dividend
> effect works in both directions. Protective puts on high-dividend names are naturally
> more expensive, reflecting each expected ex-date reduction. On the write side,
> cash-secured puts on dividend payers carry elevated assignment risk around ex-dates
> (see Section 4). Price the dividend-adjusted put premium before choosing between
> buying puts outright or using a spread structure.

---

## 4. Anticipating Early Assignment When Writing Puts Near Ex-Dividend Dates

When the time value premium of an in-the-money put disappears, there is a risk of
assignment regardless of time remaining until expiration — the same parity/discount
trigger that applies to calls (Chapter 1).

**The dividend-specific assignment gauge for put writers:**

If the time value premium of an in-the-money put is less than the amount of the
upcoming dividend, the writer should anticipate assignment the day *after* the
ex-dividend date.

Note the timing difference from calls: call assignment due to dividends occurs on the
ex-date itself (the holder exercises to collect the dividend). Put assignment occurs the
day after the ex-date — the put holder waits to collect the dividend first, then exercises
the put to sell the stock at the striking price.

**Why — worked example:**

XYZ is at 45 and will pay a $0.50 dividend. The XYZ July 50 put is at 5.25. Time value
premium = 5.25 + 45 − 50 = **0.25** — less than the $0.50 dividend.

An arbitrageur can:
1. Buy XYZ at 45.
2. Buy the July 50 put at 5.25.
3. Collect the $0.50 dividend (holds through ex-date).
4. Exercise the put the day after ex-date, selling XYZ at 50.

Total intake: 5 points on the stock (buy 45, sell 50) + $0.50 dividend = **5.50 points**.
Cost of put: 5.25 points. Net profit: **0.25 points**. The arbitrage works.

Consequence: as the ex-dividend date approaches, the time value premium of all
in-the-money puts on that stock will tend to equal or exceed the dividend amount —
arbitrageurs enforce this floor.

**The practical gauge:** The put writer must determine whether the time value premium
of the short put exceeds the upcoming dividend. If it does, assignment risk from the
dividend is low. If it does not, assignment the day after the ex-date is likely.

This differs from the call writer's gauge: the call writer only needs to check whether
the call is trading at or below parity, regardless of dividend size. The put writer must
specifically compare time value premium to the dividend amount.

> **Annotation:** Directly actionable for any put-writing strategy in the playbook,
> including cash-secured puts on stocks the investor wants to own at a lower price. On
> dividend-paying stocks, monitor the time value premium of any short ITM put against
> the upcoming dividend before the ex-date. If time value premium has eroded below the
> dividend amount, assignment the day after the ex-date is likely. Either close the
> position before the ex-date or be prepared to take delivery of the stock.

---

## 5. The Conversion: Why Put and Call Prices Are Linked

There is a structural relationship between put and call prices when both share the same
striking price and expiration date. They are not independent of one another.

A *conversion* is the riskless arbitrage that enforces this relationship:
1. Buy 100 shares of the underlying stock.
2. Buy 1 put at a certain striking price.
3. Sell 1 call at the same striking price.

If the stock drops, the long put covers it. If the stock rises, the long stock covers the
short call. No risk exists in either direction. If the put becomes cheap relative to the
call, arbitrageurs do conversions until prices realign. If the put becomes expensive
relative to the call, arbitrageurs do reversals (short stock, short put, long call) until
prices realign.

**Two durable consequences of this enforcement mechanism:**

1. A put will generally sell for less than a call when the stock is exactly at the
   striking price, unless the stock pays a large dividend. The cost of carrying long
   stock in the conversion is the source of this persistent difference.

2. A put loses time value premium more quickly in-the-money than a call does, and
   holds out-of-the-money time value premium better than a call does. Both
   asymmetries are structurally enforced by the conversion relationship.

The conversion link also means implied volatility cannot diverge between puts and calls
at the same strike for long: a spike in put IV pulls call IV up with it, and vice versa.

> **Annotation:** The IV linkage matters when simultaneously holding long puts for
> protection and long calls for upside participation — as in a thesis where both a
> continued upside move and a downside hedge are in place. A volatility event that
> drives up put IV benefits the protective put position while simultaneously inflating
> the cost of any new call purchases. Position sizing and entry timing for both legs
> should account for this linkage. The OTM put's slower decay relative to OTM calls
> also means that rolling a protective put — replacing an expiring OTM put with a new
> one — is less costly per unit of time than an equivalent rolling program in OTM calls
> would be on the upside.

# Chapter 15 — Put Option Basics: Extracted Insights for the Conservative Options Playbook

---

## 1. Core Put Option Mechanics: The Mirror Image of Calls (With Key Differences)

"In many respects, the put option and its associated strategies will be very nearly the
opposite of corresponding call-oriented strategies. However, *it is not correct to say that
the put is exactly the opposite of a call.*"

In the simplest terms, *the outright buyer of a put is hoping for a stock price decline*
in order for his put to become more valuable. If the stock were to decline well below the
striking price of the put option, the put holder could make a profit. The holder of the put
could buy stock in the open market and then exercise his put to sell that stock for a profit
at the striking price, which is higher.

**Example:** If XYZ stock is at 40, an XYZ July 50 put would be worth at least 10 points,
for the put grants the holder the right to sell XYZ at 50 — 10 points above its current
price. On the other hand, if the stock price were *above* the striking price of the put
option at expiration, the put would be worthless.

**In-the-money / out-of-the-money — definitions are reversed for puts:**

"*A put is considered to be in-the-money when the underlying stock is below the striking
price of the put option; it is out-of-the-money when the stock is above the striking
price.*" If XYZ is at 45, the XYZ July 50 put is in-the-money and the XYZ July 50 call
is out-of-the-money. However, if XYZ were at 55, the July 50 put would be
out-of-the-money while the July 50 call would be in-the-money.

---

## 2. Time Value Premium for Puts: Formulas and the Key Asymmetry vs. Calls

The intrinsic value of an in-the-money put is merely the difference between the striking
price and the stock price. The time value premium formulas differ between puts and calls:

> **Time value premium (in-the-money put)** = Put option price + Stock price − Striking price
>
> **Time value premium (in-the-money call)** = Call option price + Striking price − Stock price

**Example:** XYZ is at 47 and the XYZ July 50 put is selling for 5. The intrinsic value is
3 points (50 − 47), so the time value premium must be 2 points. Verified by formula:
5 + 47 − 50 = 2.

"*The time value premium of a put is largest when the stock is at the striking price of the
put.* As the option becomes deeply in-the-money or deeply out-of-the-money, the time
value premium will shrink substantially." This is true for both puts and calls.

**TABLE 15-1. Call and put options compared.**

| XYZ Stock Price | XYZ July 50 Call Price | Call Intrinsic Value | Call Time Value Premium | XYZ July 50 Put Price | Put Intrinsic Value | Put Time Value Premium |
|---|---|---|---|---|---|---|
| 40 | .50 | 0 | .50 | 9.75 | 10 | −.25* |
| 43 | 1 | 0 | 1 | 7 | 7 | 0 |
| 45 | 2 | 0 | 2 | 6 | 5 | 1 |
| 47 | 3 | 0 | 3 | 5 | 3 | 2 |
| 50 | 5 | 0 | 5 | 4 | 0 | 4 |
| 53 | 7 | 3 | 4 | 3 | 0 | 3 |
| 55 | 8 | 5 | 3 | 2 | 0 | 2 |
| 57 | 9 | 7 | 2 | 1 | 0 | 1 |
| 60 | 10.50 | 10 | .50 | .50 | 0 | .50 |
| 70 | 19.75 | 20 | −.25* | .25 | 0 | .25 |

*A deeply in-the-money option may actually trade at a discount from intrinsic value in
advance of expiration.*

Two structural facts emerge from Table 15-1 that govern put strategy throughout the
playbook:

**First:** "*The call will generally sell for more than the put when the stock is at the
strike.* Notice in Table 15-1 that, with XYZ at 50, the call is worth 5 points while the put
is worth only 4 points. This is true in general, except in the case of a stock that pays a
large dividend." The reason is the cost of carrying stock, enforced by arbitrage (see
Section 5).

**Second — the critical asymmetry:** "*An in-the-money put (stock is below strike) loses
time value premium more quickly than an in-the-money call does.* Notice that with XYZ
at 43 in Table 15-1, the put is 7 points in-the-money and has lost all its time value
premium. But when the call is 7 points in-the-money, XYZ at 57, the call still has 2
points of time value premium."

> **Annotation:** This asymmetry has direct implications for the value investor using puts
> as downside protection on a long stock position. An ITM put bought as insurance will
> shed its time value premium faster than an equivalent ITM call would gain it on the
> upside. Once the stock falls far enough to push the protective put deep ITM, the
> remaining time value cushion is thin and the decision to roll down, sell, or exercise
> becomes urgent. Do not assume a deep ITM put retains meaningful optionality — check
> the time value premium directly.

---

## 3. The Effect of Dividends on Put Premiums

"The dividend of the underlying stock is a negative factor on the price of its call options.
The opposite is true for puts. *The larger the dividend, the more valuable the puts will
be.* This is true because, as the stock goes ex-dividend, it will be reduced in price by the
amount of the dividend. That is, the stock will decrease in price and therefore the put
will become more valuable."

**Example:** XYZ is selling for $25 per share and will pay $1 in dividends over the next
6 months. Then a 6-month put option with strike 25 should automatically be worth at
least $1, regardless of any other factor concerning the underlying stock. During the next
6 months, the stock will be reduced in price by the amount of its dividends — $1 — and
if everything else remained the same, the stock would then be at 24. With the stock at 24,
the put would be 1 point in-the-money and would thus be worth at least its intrinsic value
of 1 point.

*On the day before a stock goes ex-dividend, the time value premium of an in-the-money
put should be at least as large as the impending cash dividend payment.* That is, if XYZ
is 40 and is about to pay a $.50 dividend, an XYZ January 50 put should sell for at least
10.50, because the stock will be reduced in price by the amount of its dividend on the
ex-dividend day.

> **Annotation:** For the value investor who holds dividend-paying stocks, the dividend
> effect works in both directions. On the buy side: protective puts on high-dividend names
> are naturally more expensive, reflecting the expected stock price reduction on each
> ex-date. On the write side: cash-secured puts on dividend payers carry elevated
> assignment risk around ex-dates (see Section 4). Price the dividend-adjusted put premium
> before choosing between buying puts outright or using a spread structure.

---

## 4. Anticipating Early Assignment When Writing Puts Near Ex-Dividend Dates

"*When the time value premium of an in-the-money put option disappears, there is a risk
of assignment, regardless of the time remaining until expiration.*"

The specific dividend-related assignment gauge for put writers: "If the time value premium
of an in-the-money put is less than the amount of the dividend to be paid, the writer may
often anticipate that he will be assigned immediately after the ex-dividend of the stock."

**Why — worked example:**

XYZ is at 45 and it will pay a $.50 dividend. The XYZ July 50 put is selling at 5.25. The
time value premium of the July 50 put is 25 cents — less than the amount of the dividend,
which is 50 cents. An arbitrageur can:

1. Buy XYZ at 45.
2. Buy the July 50 put at 5.25.
3. Collect the 50-cent dividend (must hold through the ex-date).
4. Exercise the put to sell XYZ at 50 (assignment falls on the day after the ex-date).

The arbitrageur makes 5 points on the stock (buy at 45, sell at 50 via exercise), plus the
50-cent dividend, for a total intake of 5.50 points. He paid 5.25 for the put. Net profit:
25 cents. "Thus, *as the ex-dividend date of a stock approaches, the time value premium
of all in-the-money puts on that stock will tend to equal or exceed the amount of the
dividend payment.*"

The practical gauge: "The put writer must determine if the time value premium of the put
exceeds the amount of the dividend to be paid. If it does, there is a much smaller chance
of assignment because of the dividend."

Note the difference from calls: "The call writer only needs to observe whether the call
was trading at or below parity, regardless of the amount of the dividend, as the
ex-dividend date approaches. The put writer must determine if the time value premium
of the put exceeds the amount of the dividend to be paid."

> **Annotation:** This is directly actionable for any put-writing strategy in the playbook —
> including cash-secured puts on stocks the investor wants to own at a lower price. On
> dividend-paying stocks, monitor the time value premium of any short ITM put against
> the upcoming dividend before the ex-date. If time value premium has eroded below the
> dividend amount, assignment the day after the ex-date is likely. Either close the position
> before the ex-date or be prepared to take delivery of the stock.

---

## 5. The Conversion: Why Put and Call Prices Are Linked, and What It Implies for Strategy

"*There is a relationship between put and call prices, when both have the same striking
price and expiration date. They are not independent of one another.*"

A conversion — the arbitrage that enforces this relationship — has no risk. The
arbitrageur does three things simultaneously:

1. Buy 100 shares of the underlying stock.
2. Buy 1 put option at a certain striking price.
3. Sell 1 call option at the same striking price.

If the stock drops, the long put covers it. If the stock rises, the long stock covers the
short call. "If the put becomes 'cheap' with respect to the call, arbitrageurs will move in
to do conversions and force the prices back in line. On the other hand, if the put becomes
expensive with relationship to the call, arbitrageurs will do reversals [short stock, short
put, long call] until the prices move back into line."

Two durable consequences of this enforcement mechanism:

1. "*A put option will generally sell for less than a call option when the underlying stock
is exactly at the striking price,* unless the stock pays a large dividend." (The cost of
carrying long stock in the conversion is the source of this persistent difference.)

2. "*A put option will lose its time value premium much more quickly in-the-money than
a call option will* (and, conversely, a put option will generally hold out-of-the-money
time value premium better than a call option will)."

> **Annotation:** The second consequence is the more strategically important one for the
> playbook. OTM puts bought as portfolio protection do not decay as fast as OTM calls
> do — the out-of-the-money time value premium holds better. This means the "insurance
> cost" of an OTM protective put is not front-loaded; the put retains value longer if the
> stock drifts sideways rather than declining immediately. Conversely, once a protective
> put goes deep ITM after a sharp decline, rolling it down promptly is important — the
> remaining time value erodes rapidly and the put approaches parity, leaving little
> optionality to recover from. The conversion/reversal framework also links implied
> volatility across puts and calls at the same strike: a spike in put IV will pull call IV up
> with it, which matters when simultaneously holding long puts for protection and long
> calls for upside participation.

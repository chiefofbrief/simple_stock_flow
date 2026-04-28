# Chapter 15 — User Notes
- The broad definition of an in-the-money option as “an option that has intrinsic value” would cover the situation for both puts and calls. Note that a put option has intrinsic value when the underlying stock is below the striking price of the put. The intrinsic value of an in-the-money put is merely the difference between the striking price and the stock price.
- This is not the same formula that was applied to in-the-money call options, although it is always true that the time value premium of an option is the excess value over intrinsic value.
- The same factors that determine the price of the call option also determine the price of the put option: price of the underlying stock, striking price of the option, time remaining until expiration, volatility of the underlying stock, dividend rate of the underlying stock, and the current risk-free interest rate (Treasury bill rate, for example).
- Certain facts remain true for the put option as they did for the call option. The rate of decay of the put option is not linear; that is, the time value premium will decay more rapidly in the weeks immediately preceding expiration. The more volatile the underlying stock, the higher will be the price of its options, both puts and calls. Moreover, the marketplace may at any time value options at a higher or lower volatility than the underlying stock actually exhibits. This is called implied volatility, as distinguished from actual volatility. Also, the put option is usually worth at least its intrinsic value at any time, and should be worth exactly its intrinsic value on the day that it expires.
- This put option pricing curve demonstrates the effect mentioned earlier, that a put option loses time value premium more quickly when it is in-the-money, and also shows that an out-of-the-money put holds a great deal of time value premium.
- The dividend of the underlying stock is a negative factor on the price of its call options. The opposite is true for puts. The larger the dividend, the more valuable the puts will be. This is true because, as the stock goes ex-dividend, it will be reduced in price by the amount of the dividend. That is, the stock will decrease in price and therefore the put will become more valuable. Consequently, the buyer of the put will be willing to pay a higher price for the put and the seller of the put will also demand a higher price. As with listed calls, listed puts are not adjusted for the payment of cash dividends on the underlying stock. However, the price of the option itself will reflect the dividend payments on the stock.
- On the day before a stock goes ex-dividend, the time value premium of an in-the-money put should be at least as large as the impending cash dividend payment. That is, if XYZ is 40 and is about to pay a $.50 dividend, an XYZ January 50 put should sell for at least 10.50. This is true because the stock will be reduced in price by the amount of its dividend on the day of the ex-dividend.
- When the holder of a put option exercises his option, he sells stock at the striking price. He may exercise this right at any time during the life of the put option. When this happens, the writer of a put option with the same terms is assigned an obligation to buy stock at the striking price. It is important to notice the difference between puts and calls in this case. The call holder exercises to buy stock and the call writer is obligated to sell stock. The reverse is true for the put holder and writer.
- When the holder of a put option exercises his right to sell stock, he may be selling stock that he currently holds in his portfolio. Second, he may simultaneously go into the open market and buy stock for sale via the put exercise. Finally, he may want to sell the stock in his short stock account; that is, he may short the underlying stock by exercising his put option. He would have to be able to borrow stock and supply the margin collateral for a short sale of stock if he chose this third course of action. The writer of the put option also has several choices in how he wants to handle the stock purchase that he is required to make. The put writer who is assigned must receive stock. (The call writer who is assigned delivery stock.) The put writer may currently be short the underlying stock, in which case he will merely use the receipt of stock from the assignment to cover his short sale. He may also decide to immediately sell stock in the open market to offset the purchase that he is forced to make via the put assignment. Finally, he may decide to retain the stock that is delivered to him; he merely keeps the stock in his portfolio. He would, of course, have to pay for (or margin) the stock if he decides to keep it.
- The writer of a put option can anticipate assignment in the same way that the writer of a call can. When the time value premium of an in-the-money put option disappears, there is a risk of assignment, regardless of the time remaining until expiration. In Chapter 1, a form of arbitrage was described in which Patna or firm traders, who pay little or no commissions, can take advantage of an in-the-money call selling at a discount to parity. Similarly, there is a method for these traders to take advantage of an in-the-money put selling at a discount to parity.
- Dividend payment dates may also have an effect on the frequency of assignment. For call options, the writer might expect to receive an assignment on the day the stock goes ex-dividend. The holder of the call is able to collect the dividend by so exercising, Things are slightly different for the writer of puts. He might expect to receive an assignment on the day after the ex-dividend date of the underlying stock. Since the writer of the put is obligated to buy stock, it is unlikely that anyone would put the stock to him until after the dividend has been paid. In any case, the writer of the put can use a relatively simple gauge to anticipate assignment near the ex-dividend date. If the time value premium of an in-the-money put is less than the amount of the dividend to be paid, the writer may often anticipate that he will be assigned immediately after the ex-dividend of the stock. This is quite different from the call option. It was shown in Chapter 1 that the call writer only needs to observe whether the call was trading at or below parity, regardless of the amount of the dividend, as the ex-dividend date approaches. The put writer must determine if the time value premium of the put exceeds the amount of the dividend to be paid. If it does, there is a much smaller chance of assignment because of the dividend. 
- 

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

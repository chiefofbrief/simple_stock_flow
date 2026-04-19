# Chapter 1: Definitions — Extracted Insights

---

## Time Value Premium: Where It Lives and Why It Matters

The *time value premium* is the amount by which the option premium exceeds its intrinsic value:

**Formula:** Call time value premium = Call option price + Striking price − Stock price

McMillan's worked example:
- XYZ trading at 48, XYZ July 45 call at 4
- Intrinsic value = 48 − 45 = 3
- Time value premium = 4 − 3 = **1**

If the call is out-of-the-money, the entire premium is time value:
- XYZ at 48, XYZ July 50 call at 2
- Intrinsic value = 0
- Time value premium = **2** (the full premium)

**Critical rule:** "An option normally has the largest amount of time value premium when the stock price is equal to the striking price. As an option becomes deeply in- or out-of-the-money, the time value premium shrinks substantially."

McMillan's Table 1-1 (XYZ July 50 call at various stock prices):

| XYZ Stock Price | Call Price | Intrinsic Value | Time Value Premium |
|-----------------|------------|-----------------|-------------------|
| 40              | ½          | 0               | ½                 |
| 43              | 1          | 0               | 1                 |
| 45              | 2          | 0               | 2                 |
| 47              | 3          | 0               | 3                 |
| **50**          | **5**      | **0**           | **5**             |
| 53              | 7          | 3               | 4                 |
| 55              | 8          | 5               | 3                 |
| 57              | 9          | 7               | 2                 |
| 60              | 10.50      | 10              | .50               |
| 70              | 19.50      | 20              | −.50*             |

*"A deeply in-the-money call may actually trade at a discount from intrinsic value, because call buyers are more interested in less expensive calls that might return better percentage profits on an upward move in the stock."

**Takeaway for the bullish value investor:** ATM options carry the most time value — you pay the most for time when you buy at-the-money. Deep ITM calls have mostly intrinsic value and low time premium, giving you more stock-like exposure with less decay drag. Deep OTM calls are pure time premium and require a large move just to break even. Notably, buying slightly ITM rather than ATM reduces your time value exposure without giving up meaningful upside leverage — the table shows time value dropping from 5 (ATM) to 4 (3 points ITM) while intrinsic value picks up 3 points of real stock exposure.

---

## Non-Linear Decay: The Square Root Rule

"The rate of decay of an option is not linear. An option's time value premium decays much more rapidly in the last few weeks of its life (that is, in the weeks immediately preceding expiration) than it does in the first few weeks of its existence."

**The rule:** "The rate of decay is actually related to the square root of the time remaining. Thus, a 3-month option decays (loses time value premium) at twice the rate of a 9-month option, since the square root of 9 is 3. Similarly, a 2-month option decays at twice the rate of a 4-month option (√4 = 2)."

McMillan's Table 1-4 shows a hypothetical July 50 call with 6 months remaining:

| XYZ Stock Price | Call Price | Intrinsic Value | Time Value Premium |
|-----------------|------------|-----------------|-------------------|
| 40              | 1          | 0               | 1                 |
| 45              | 2          | 0               | 2                 |
| 48              | 3          | 0               | 3                 |
| **50**          | **4**      | **0**           | **4**             |
| 52              | 5          | 2               | 3                 |
| 55              | 6.50       | 5               | 1.50              |
| 60              | 11         | 10              | 1                 |

With 6 months remaining the ATM call carries 4 points of time value. The same ATM call in Table 1-1 carries 5 points — reflecting more time remaining in that hypothetical. The curve drops as expiration approaches until on the final day the option is worth only its intrinsic value.

**Practical implication:** A 9-month option does not cost three times a 3-month option — it costs roughly √3 times as much in time premium. Longer-dated options are therefore *relatively cheap* per unit of time compared to short-dated ones. For a 3–12 month thesis, buying 6–9 month options (or LEAPS) lets you pay less per day of time while giving your thesis room to play out before decay accelerates in the final weeks.

---

## Volatility: The Hidden Driver of "Time Premium"

"The volatility of the underlying stock has a great deal to do with how much 'time premium' is in the option. So, really, 'time premium' is something of a misnomer, but it's the standard term."

"More volatile underlying stocks have higher option prices. This relationship is logical, because if a stock has the ability to move a relatively large distance upward, buyers of the calls are willing to pay higher prices for the calls — and sellers demand them as well."

McMillan's example: "If AT&T and Xerox sell for the same price (as they have been known to do), the Xerox calls would be more highly priced than the AT&T calls because Xerox is a more volatile stock than AT&T."

**Takeaway:** When screening undervalued stocks for call purchases, higher implied volatility means you are paying more for the same time. A low-volatility undervalued stock will have cheaper options — your entry cost is lower and your breakeven is closer. A high-volatility undervalued stock may be correct on the thesis but expensive to express via options.

---

## The Four-Variable Trap: Right Stock, Wrong Outcome

"The interplay of the four major variables — stock price, striking price, time, and volatility — can be quite complex. While a rising stock price (for example) is directing the price of a call upward, decreasing time may be simultaneously driving the price in the opposite direction."

McMillan's warning: "Thus, the purchaser of an out-of-the-money call may wind up with a loss even after a rise in price by the underlying stock, because time has eroded the call value."

**This is the central risk for a thesis-driven call buyer.** If your thesis plays out slowly — the stock grinds up rather than moves decisively — time decay can eat your premium faster than intrinsic value accumulates, especially on OTM calls. This argues for buying calls with sufficient time remaining and not going too far out of the money.

---

## Dividends Depress Call Premiums — And Create a Hidden Cost for Holders

"Dividends, however, tend to lower call option premiums: The larger the dividend of the underlying common stock, the lower the price of its call options. One of the most influential factors in keeping option premiums low on high-yielding stock is the yield itself."

McMillan's worked example:
- XYZ at $25, low volatility, pays $2/year in dividends ($0.50 quarterly)
- Over 6 months, XYZ will pay $1/share in dividends
- Stock price will be reduced by $1 when it goes ex-dividend
- "The call buyer makes a low bid — even for a 6-month call — because the underlying stock's price will be reduced by the ex-dividend reduction, and the call holder does not receive the cash dividends."
- The call buyer therefore values the XYZ July 25 call as if the stock were at 24, not 25

"In actual practice, option buyers tend to discount the upcoming dividends of the stock when they bid for the calls. However, not all dividends are discounted fully; usually the nearest dividend is discounted more heavily than are dividends to be paid at a later date."

**Takeaway for the value investor:** Many undervalued stocks are high-yield names. When you buy calls on a dividend-paying stock, you forfeit the dividend and pay a premium already discounted for it. You need a larger price appreciation to compensate. Factor the expected ex-dividend stock price reductions into your breakeven analysis using the forward-adjusted stock price, not the current price.

---

## Early Exercise: The Triggers and the Nuances

McMillan identifies three circumstances that signal early exercise:
1. A call that is in-the-money at expiration
2. An option trading at a discount prior to expiration
3. The underlying stock paying a large dividend and about to go ex-dividend

**The parity rule:** "The writer can usually expect an early exercise when the call is trading at or below parity."

**The time premium protection rule:** "If time premium is left in the call, the holder is always better off financially to sell that call in the secondary market rather than to exercise it."

McMillan's example: Prior to expiration, XYZ is trading at 50½, and the January 50 call is trading at 1.
- Time value premium = 1 + 50 − 50.50 = **0.50**
- "The call is not necessarily in imminent danger of being called, since it still has half a point of time premium left."

**The dividend-driven early exercise rule — with the critical nuance:** McMillan works through why a dividend larger than the time premium does *not* automatically trigger early exercise:

- XYZ at 50, going ex-dividend $1 tomorrow
- XYZ January 40 call at 10.25 (TVP = 10.25 + 40 − 50 = **0.25**)
- Arbitrageur buys call at 10.25, exercises, owns stock on ex-date
- Ex-date: XYZ opens at 49 (down $1 dividend)
- Stock gain: 49 − 40 = 9 points. Plus $1 dividend = 10 points total cash inflow
- Cost of call: 10.25
- **Result: net loss of 0.25. The arbitrage fails.**

"A dividend payment that exceeds the time premium in the call, therefore, does not imply that the writer will be assigned."

The actual trigger: early exercise via dividends only occurs when the option trades at parity or a discount — not merely because the dividend is large. "It is therefore very important for the writer to watch for discount situations on the day prior to the ex-date."

---

## Selling in the Secondary Market Almost Always Beats Exercising

"Generally, option holders incur higher commission costs through assignment than they do selling the option in the secondary market. So the public customer who holds an option is better off selling the option in the secondary market than exercising the call."

**Why this matters for a thesis-driven holder:** If you are long a call that has gone deep in-the-money as your thesis plays out, your instinct may be to exercise and take the stock. In most cases this is the wrong move. A deep ITM call still carries some residual time value — exercising destroys that time value immediately, whereas selling in the secondary market captures it. The only exception McMillan identifies is when you specifically want to own the underlying stock — "perhaps because it is attractive to him or because he wants to cover a short sale." If your value thesis has fully played out and you want to rotate into the stock for the long term, exercise may be appropriate. Otherwise, close the option.

---

## Open Interest as a Liquidity Screen

"While the magnitude of the open interest is not an extremely important piece of data for the investor, it is useful in determining the liquidity of the option in question. If there is a large open interest, then there should be little problem in making fairly large trades. However, if the open interest is small — only a few hundred contracts outstanding — then there might not be a reasonable secondary market in that option series."

**Practical application:** Before entering any position, check open interest on your intended strike and expiration. Low open interest means wide bid-ask spreads and the risk of being unable to exit at a fair price. For a 3–12 month thesis where you may need to roll or exit early, liquidity at your specific strike and expiration matters more than headline volume on the stock itself.

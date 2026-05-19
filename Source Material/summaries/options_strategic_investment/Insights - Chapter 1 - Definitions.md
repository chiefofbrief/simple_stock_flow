```markdown
# Chapter 1: Definitions — Extracted Insights

---

## The Six Pricing Factors (and Their Hierarchy)

An option's price is determined by six quantifiable factors:

1. Price of the underlying stock
2. Striking price of the option
3. Time remaining until expiration
4. Volatility of the underlying stock
5. Current risk-free interest rate (e.g., 90-day T-bill rate)
6. Dividend rate of the underlying stock

The first four are the major determinants. The latter two are generally less important, though the dividend rate can be significant for high-yield stocks. Critically, when the stock price is far above or far below the striking price, factors 2–6 become nearly irrelevant — the stock price dominates everything else at the extremes.

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

**Critical rule:** An option normally has the largest amount of time value premium when the stock price is equal to the striking price. As an option becomes deeply in- or out-of-the-money, the time value premium shrinks substantially.

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

*A deeply in-the-money call may actually trade at a discount from intrinsic value, because call buyers are more interested in less expensive calls that might return better percentage profits on an upward move in the stock.

**Takeaway for the bullish value investor:** ATM options carry the most time value — you pay the most for time when you buy at-the-money. Deep ITM calls have mostly intrinsic value and low time premium, giving you more stock-like exposure with less decay drag. Deep OTM calls are pure time premium and require a large move just to break even. Buying slightly ITM rather than ATM reduces your time value exposure without giving up meaningful upside leverage — the table shows time value dropping from 5 (ATM) to 4 (3 points ITM) while intrinsic value picks up 3 points of real stock exposure.

---

## "Time Value Premium" Is a Misnomer

The standard term "time value premium" implies that the non-intrinsic portion of an option's price is purely a function of time remaining. That is not accurate. Volatility of the underlying stock has a substantial influence on how much so-called "time premium" is in the option. The correct mental model is that this component reflects both time remaining *and* the market's expectation of how much the stock can move — volatility is embedded in what gets called "time premium." The term is standard and unavoidable, but understanding what it actually represents prevents misreading option prices.

---

## Non-Linear Decay: The Square Root Rule

The rate of decay of an option is not linear. An option's time value premium decays much more rapidly in the last few weeks of its life than in the first few weeks of its existence.

**The rule:** The rate of decay is related to the square root of the time remaining. A 3-month option decays at twice the rate of a 9-month option (√9 = 3). A 2-month option decays at twice the rate of a 4-month option (√4 = 2).

**The pricing corollary:** This same square root relationship governs relative option pricing — a 9-month option does not sell for three times the price of a 3-month option. It sells for roughly √3 times as much in time premium. Longer-dated options are therefore relatively cheap per unit of time compared to short-dated ones. The other pricing factors — especially volatility — also influence actual price relationships between different expirations, so the square root rule is a guide, not a formula.

McMillan's Table 1-4 (hypothetical July 50 call with 6 months remaining):

| XYZ Stock Price | Call Price | Intrinsic Value | Time Value Premium |
|-----------------|------------|-----------------|-------------------|
| 40              | 1          | 0               | 1                 |
| 45              | 2          | 0               | 2                 |
| 48              | 3          | 0               | 3                 |
| **50**          | **4**      | **0**           | **4**             |
| 52              | 5          | 2               | 3                 |
| 55              | 6.50       | 5               | 1.50              |
| 60              | 11         | 10              | 1                 |

With 6 months remaining the ATM call carries 4 points of time value. The same call in Table 1-1 (more time remaining) carries 5 points. On the final day of trading, the option is worth only its intrinsic value — time premium has fully decayed to zero.

**Practical implication:** For a 3–12 month thesis, buying 6–9 month options (or LEAPS) lets you pay less per day of time while giving your thesis room to play out before decay accelerates in the final weeks. The worst position to be in is long an OTM call in the last few weeks before expiration — decay is fastest and the stock needs to move the most.

---

## Volatility: The Hidden Driver of "Time Premium"

More volatile underlying stocks have higher option prices. If a stock has the ability to move a large distance upward, call buyers are willing to pay higher prices — and sellers demand them. McMillan's example: if AT&T and Xerox sell for the same price, Xerox calls would be more expensive because Xerox is the more volatile stock.

**Takeaway:** When screening undervalued stocks for call purchases, higher implied volatility means you are paying more for the same time and the same strike. A low-volatility undervalued stock will have cheaper options — your entry cost is lower and your breakeven is closer. A high-volatility undervalued stock may be correct on the thesis but expensive to express via options. Volatility is a cost of entry, not just a characteristic of the stock.

---

## The Four-Variable Trap: Right Stock, Wrong Outcome

The interplay of the four major variables — stock price, striking price, time, and volatility — can work against each other simultaneously. While a rising stock price pushes a call's price up, decreasing time may be simultaneously driving it down.

**The core risk:** The purchaser of an out-of-the-money call may wind up with a loss even after a rise in price by the underlying stock, because time has eroded the call value faster than intrinsic value accumulated.

This is the central risk for a thesis-driven call buyer. If your thesis plays out slowly — the stock grinds up rather than moves decisively — time decay can eat your premium faster than intrinsic value accumulates, especially on OTM calls. This argues for: (1) buying calls with sufficient time remaining, (2) not going too far out of the money, and (3) having a view on *when* the thesis will be recognized by the market, not just *that* it will be.

---

## Dividends Depress Call Premiums — And Create a Hidden Cost for Holders

Dividends tend to lower call option premiums. The larger the dividend of the underlying stock, the lower the price of its call options. Call buyers discount upcoming dividends when bidding for calls because the stock price will be reduced by the ex-dividend amount, and the call holder does not receive the cash dividend.

McMillan's worked example:
- XYZ at $25, pays $2/year ($0.50 quarterly)
- Over 6 months, XYZ will pay $1/share in dividends
- The call buyer values the XYZ July 25 call as if the stock were at 24, not 25, because the stock price will be reduced by $1 in ex-dividend reductions over the life of the call

In practice, not all dividends are discounted fully — the nearest dividend is discounted more heavily than dividends to be paid at a later date.

**Takeaway for the value investor:** Many undervalued stocks are high-yield names. When you buy calls on a dividend-paying stock, you forfeit the dividend and pay a premium already discounted for it. You need a larger price appreciation to compensate. Factor expected ex-dividend stock price reductions into your breakeven analysis using the forward-adjusted stock price, not the current price.

---

## Early Exercise: The Triggers and the Nuances

Three circumstances signal early exercise:
1. A call that is in-the-money at expiration
2. An option trading at a discount (or parity) prior to expiration
3. The underlying stock paying a large dividend and about to go ex-dividend

**The time premium protection rule:** If time premium remains in the call, the holder is always better off financially selling that call in the secondary market rather than exercising it. Early exercise destroys remaining time value.

McMillan's example: XYZ trading at 50½, January 50 call trading at 1.
- Time value premium = 1 + 50 − 50.50 = **0.50**
- The call is not in imminent danger of early exercise — it still has half a point of time premium remaining.

**The dividend-driven early exercise rule — with the critical nuance:** A dividend larger than the remaining time premium does *not* automatically trigger early exercise. McMillan's example:

- XYZ at 50, going ex-dividend $1 tomorrow
- XYZ January 40 call at 10.25 (TVP = 10.25 + 40 − 50 = **0.25**)
- Arbitrageur buys call at 10.25, exercises, owns stock on ex-date
- Ex-date: XYZ opens at 49 (down $1 dividend)
- Stock gain: 49 − 40 = 9 points. Plus $1 dividend = 10 points total cash inflow
- Cost of call: 10.25
- **Result: net loss of 0.25. The arbitrage fails.**

Early exercise via dividends only occurs when the option trades at parity or a discount — not merely because the dividend is large. Writers should watch for discount situations on the day prior to the ex-date specifically.

**Writer's timing rule:** Assignment notices are determined on open positions as of the close of trading each day. A writer who covers (buys back) the position at any point during a trading day cannot be assigned on that option that day. The window to act is before the close — once an assignment notice is received, it is too late to buy back the call.

**Cash account mechanics:** A holder who exercises in a cash account must pay for the stock in full — even if the stock is sold the same day. If there is not sufficient cash in the account, a margin call results. This is an operational risk worth knowing before exercising.

---

## Selling in the Secondary Market Almost Always Beats Exercising

Option holders generally incur higher commission costs through assignment (stock transaction on 100 shares) than they do selling the option in the secondary market. Beyond commissions, exercising a call that still has time value remaining destroys that time value immediately — the secondary market will pay you for it, assignment will not.

**Rule:** If time premium remains in the call, sell in the secondary market. Do not exercise.

The only exception: when you specifically want to own the underlying stock — to hold it long term or to cover a short sale. If your value thesis has fully played out and you want to rotate into the stock, exercise may be appropriate. Otherwise, close the option.

---

## Contract Size Adjustments: Stock Dividends

Standard listed options cover 100 shares. However, if the underlying stock pays a stock dividend, the contract size is adjusted accordingly and the strike price is recalculated. Example: if UVW pays a 5% stock dividend, options become contracts for 105 shares at an adjusted strike. A UVW April 38.10 call offered at $3.00 actually costs $315 ($3.00 × 105), not $300. Always verify contract size and strike adjustments on any stock that has had a recent stock dividend or split.

---

## Order Types

Standard order types are available on options: market orders, limit orders, stop orders, and stop-limit orders (availability depends on broker, but limit orders are standard). Each order must specify:

- Whether the transaction is a buy or sell
- The specific option (underlying, expiration, strike, call or put)
- Whether the trade is opening or closing a position
- Whether the transaction is a spread
- The desired price

**Practical note:** Use limit orders on options. Bid-ask spreads on options are wide relative to stocks, and market orders frequently execute at unfavorable prices. This is especially true on lower-liquidity strikes and expirations.

---

## Open Interest as a Liquidity Screen

Open interest measures the number of contracts currently outstanding in a given option series. Large open interest means an active secondary market and the ability to make reasonably sized trades without moving the price. Small open interest — a few hundred contracts — means a thin secondary market, wide bid-ask spreads, and potential difficulty exiting at a fair price.

**Practical application:** Before entering any position, check open interest on your intended strike and expiration. For a 3–12 month thesis where you may need to roll or exit early, liquidity at your specific strike and expiration matters more than headline volume on the stock itself. Low open interest is a reason to reconsider the strike or expiration, not just an inconvenience.
```

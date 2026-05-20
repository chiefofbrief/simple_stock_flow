# Chapter 17: Put Buying in Conjunction with Common Stock Ownership —
# Extracted Insights for the Conservative Options Playbook

---

## Framing: The Protective Put and the Synthetic Long Call

When one simultaneously owns both the common stock and a put on that same stock,
the position has limited downside risk during the life of the put. This position is also
called a *synthetic long call* because the profit graph has exactly the same shape as a
long call's. The two strategies — buying stock plus a put, and simply buying a call —
are equivalent in profit and loss potential, though they differ substantially in capital
required, dividend entitlement, and duration of ownership.

This equivalence is analytically useful throughout the chapter: conclusions about which
call to buy (from Chapter 3) translate directly into conclusions about which put to buy
for protection, and the total cost of stock plus put can always be compared against the
cost of simply buying the equivalent call outright.

**Three classes of investors who use protective puts:**

1. *The long-term holder not considering selling* — whose cost basis or tax situation
   makes selling impractical — uses the put to limit losses over a short-term horizon
   while retaining full upside participation and continued ownership.

2. *The investor establishing a new position* — buys the put simultaneously with the
   stock, immediately creating a position with limited downside risk and large upside
   potential. He can hold the stock through temporary setbacks without overreacting,
   since the put defines his maximum loss for the life of the option.

3. *The active trader who wants to eliminate stop-loss orders* — some fairly aggressive
   traders use protective puts specifically to avoid placing stop-loss orders on their
   stocks. A stop-loss order can be triggered by a temporary dip and exit the position
   permanently, only for the stock to subsequently recover. The put provides the same
   floor without the risk of being shaken out on a bad tick.

**Portfolio-level use:** The purchase of low-cost puts — typically slightly OTM — can
reduce the negative effects of a broad market decline on a portfolio's holdings. The
strategy is not about buying full ATM insurance on every position, but about selective,
inexpensive puts that prevent catastrophic losses during sustained downturns.

---

## 1. The Protective Put: Structure, Cost, and the Insurance Analogy

The put functions much like an insurance policy with a finite life.

**Example:** An investor owns XYZ at 52 and purchases an XYZ October 50 put for 2.
The put grants the right to sell XYZ at 50, so the most that can be lost on the stock is
2 points. Combined with the 2-point put cost, the maximum potential loss until October
expiration is 4 points — regardless of how far XYZ might decline. Any upside above the
purchase price is retained, less the 2-point cost of the put.

**Results at expiration:**

| XYZ at Expiration | Stock Profit | Put Profit | Total Profit |
|---|---|---|---|
| 30 | −$2,200 | +$1,800 | −$400 |
| 40 | −$1,200 | +$800 | −$400 |
| 50 | −$200 | −$200 | −$400 |
| 54 | +$200 | −$200 | $0 |
| 60 | +$800 | −$200 | +$600 |
| 70 | +$1,800 | −$200 | +$1,600 |
| 80 | +$2,800 | −$200 | +$2,600 |

If XYZ is below 48 at expiration, the put purchase proves beneficial. Above 48, the put
was a cost that reduced profits slightly. The strategy is not geared to maximizing profit
on the stock — it provides protection, eliminating the possibility of a devastating loss
during the life of the put.

The stock owner who has a put need not overreact to a downward move. He can afford
to sit back and wait during the life of the put, since he has built-in protection. This
behavioral advantage — avoiding forced decisions during a decline — is a real and
underappreciated benefit of the structure.

> **Annotation:** For the value investor, the protective put is the cleanest expression
> of the playbook's core goal: maintain full upside participation in a thesis while capping
> the cost of being wrong. The put-as-stop-loss substitute is particularly compelling —
> a stop-loss order exits the position permanently on a bad tick; a protective put keeps
> the investor in the position through temporary volatility while still defining the
> maximum loss. For AI infrastructure names where drawdowns of 20–30% on no
> fundamental change are common, the difference between a stop-loss and a protective
> put is often the difference between capturing the full thesis and being shaken out
> before it plays out.

---

## 2. Which Put to Buy for Protection: The Slightly OTM Strike Is the Target

**Deep ITM put — overly conservative:**

XYZ at 40; October 45 put at 5.50. Maximum loss = 0.50 points. But XYZ must rise
more than 5.50 points just to break even. The put eliminates nearly all downside risk
but also eliminates nearly all profit potential. Not a good strategy.

**Deep OTM put — disaster insurance only:**

XYZ at 40; October 35 put at 0.50. Maximum loss = 5.50 points (5 points on stock plus
0.50 put cost). This provides no protection against moderate declines — only against
a severe drawdown below 35. Appropriate only as catastrophic loss prevention, not
as a general hedge.

**Slightly OTM put — the target:**

The slightly out-of-the-money put achieves the best balance between protection cost
and profit drag. It keeps the floor close enough to current price to provide meaningful
protection against moderate declines while minimizing premium cost.

The synthetic equivalence confirms this: in Chapter 3, the slightly in-the-money call
was identified as offering the best risk/reward ratio for call buyers. Since long stock
plus long put equals a synthetic long call, the same conclusion applies in mirror image —
the slightly OTM put (equivalent to a slightly ITM call) is the correct default for
protective put buyers.

**Capital efficiency check:** Before buying stock plus a protective put, compare the
total cost to simply buying a call outright at the equivalent strike. Long stock plus an
OTM put requires full stock capital plus the put premium. The equivalent call requires
only the call premium. When a long-term stock holding is not required, the call may
be the more capital-efficient structure — see Chapter 7 for the ITM call covered write
substitute.

> **Annotation:** In practical terms, the slightly OTM strike means the first available
> strike below the current stock price. With XYZ at 40, the October 35 put (12.5% OTM)
> is too far to provide meaningful moderate-decline protection; the October 40 or
> October 37.50 is the correct target. The deep ITM put is almost never appropriate —
> the investor paying 5.50 for protection on a 40-dollar stock has essentially bought a
> Treasury bill with stock exposure removed.

---

## 3. Tax Warning: Buying a Put on a Short-Term Stock Holding Resets the Clock

If the stock owner is already a long-term holder at the time he buys the put, the put
purchase has no effect on his tax status. If the stock buyer buys the stock and the put
simultaneously and identifies the position as a hedge, there is also no effect on tax
status.

**However:** If one is currently a short-term holder of the common stock at the time
he buys a put, he eliminates any accrued holding period on his common stock.
Moreover, the holding period does not begin again until the put is sold.

**The 11-month example:** An investor buys stock and holds it for 5 months, then
purchases a put. He holds both the stock and the put for 6 more months, then sells
the put. Despite 11 months of stock ownership, his holding period for tax purposes
is zero — the 5 months before the put purchase are wiped out, and the clock does not
restart until the put is sold.

**Safe entry points:**
1. Buy the put simultaneously with the stock and identify it as a hedge.
2. Buy the put only after the stock has already qualified for long-term treatment.

Consult a tax advisor before buying a protective put on any stock holding where the
holding period has not yet crossed the long-term threshold.

---

## 4. The Collar: Adding a Put to a Covered Call Position

The purchase of an OTM put against a covered write position eliminates the risk of
large losses while modestly reducing overall return. One must include the put cost in
initial calculations to determine if the protection is worthwhile.

**Example:** XYZ at 39; October 40 call at 3; October 35 put at 0.50.

Standard covered write (buy stock at 39, sell October 40 call at 3):
- Maximum profit: 4 points (above 40)
- Break-even: 36
- Maximum loss: unlimited below 36

Adding the October 35 put at 0.50:
- Maximum profit reduced to 3.50 points
- Break-even raised to 36.50
- Maximum loss capped at 1.50 points (below 35)

**Results at expiration:**

| XYZ at Expiration | Stock | Oct 40 Call | Oct 35 Put | Total |
|---|---|---|---|---|
| 25 | −$1,400 | +$300 | +$950 | −$150 |
| 30 | −$900 | +$300 | +$450 | −$150 |
| 35 | −$400 | +$300 | −$50 | −$150 |
| 36.50 | −$250 | +$300 | −$50 | $0 |
| 40 | +$100 | +$300 | −$50 | +$350 |
| 50 | +$1,100 | −$700 | −$50 | +$350 |

The maximum risk is small and the writer never needs to roll down in a disadvantageous
situation. The covered write with a protective put is equivalent in profit/loss shape to
a bull spread — both produce the same capped-profit, limited-loss profile. The critical
difference: the covered writer can never lose all his investment in a short period of time
even in a severe decline, whereas the bull spreader can. The Chapter 7 covered write
substitute addresses this by investing only a small portion of available capital in the
spread and placing the remainder in fixed-income securities.

**The honest cost assessment:** Over time, the put only pays off in the tail scenario of
a large stock decline. In all other scenarios — modest decline, sideways, or rising — the
put is a cost that reduces return. The value is not in expected return but in removing
the forced roll-down decision and eliminating the possibility of catastrophic loss. For
the investor who finds himself making poor decisions under the pressure of a falling
stock and an uncapped loss, the put's emotional value alone may justify the cost.

> **Annotation:** The collar is the covered write with its Achilles heel removed. The
> covered writer's exposure to a sharp decline forces roll-down decisions at exactly the
> wrong moment — when the stock is falling and conviction is hardest to maintain. The
> protective put eliminates that forced decision entirely. For the value investor already
> writing covered calls, adding an OTM put when implied volatility is elevated converts
> the covered write into a defined-risk structure at minimal incremental cost — elevated
> IV makes the short call more valuable, partially offsetting the higher put premium.

---

## 5. The No-Cost Collar: Funding Put Protection by Selling an OTM Call

A stockholder who wants put protection but is dismayed by the cost may be able to sell
an OTM call whose proceeds completely cover the put purchase. The resulting no-cost
collar has no net debit. The "cost" is the foregone upside above the short call strike.

**LEAPS advantage:** Using LEAPS for the collar allows the short call strike to be set
very far OTM — often well above any realistic near-term price target — while still
generating enough premium to cover the put. This applies to individual investors, not
just institutions.

**Table: Highest call strike that pays for an ATM put (2.5 years to expiration)**

| Volatility of Underlying | Call Strike Distance OTM |
|---|---|
| 30% | 30% out of the money |
| 40% | 35% out of the money |
| 50% | 40% out of the money |
| 70% | 50% out of the money |
| 100% | 70% out of the money |

Higher volatility allows the short call to be struck further OTM while still covering the
put cost. A 50% volatility stock with 2.5 years to expiration allows a call struck 40%
above the current price to fully fund an ATM put — meaning the investor retains 40%
upside before any cap applies.

**LEAPS example:** In 1999, a company owned 5 million shares of Cisco (CSCO) at
approximately 130 with 50% volatility. A three-year put struck at 130 sold for
approximately the same price as a three-year call struck at 200. Full downside
protection at current price, with over 50% upside remaining, at zero net cost.

> **Annotation:** For the value investor holding a concentrated or low-basis stock
> position, the no-cost LEAPS collar is the most capital-efficient form of downside
> protection available. The key insight from the table: higher-volatility names — exactly
> the kind of beaten-down, undervalued stocks the value investor tends to own —
> generate the most favorable collar terms. Run the no-cost collar calculation before
> buying any protective put outright. If the required call strike is above a realistic price
> target for the stock over the collar's duration, the no-cost collar is strictly superior
> to paying cash for the put.

---

## 6. The Partial Collar: Preserving Some Upside While Funding the Put

The investor need not forfeit all upside to fund the put. By selling fewer calls than
shares owned, unlimited profit potential is retained on the uncapped shares.

**Example:** XYZ at 61; April 55 put at 1; April 65 call at 2.

Owner of 1,000 shares buys 10 April 55 puts ($1,000 cost). To fund the puts, sells only
5 April 65 calls ($1,000 credit). Net cost = zero. Result: 500 shares retain unlimited
upside; 500 shares are capped at 65.

**Comparing two structures:**
- Option A: Sell 5 April 65 calls — unlimited profit on 500 shares, 500 shares capped
  at 65.
- Option B: Sell 10 April 70 calls — all 1,000 shares capped at 70 (higher strike).

Both structures produce identical results if XYZ reaches 75: Option A averages 70
(500 shares at 75, 500 called at 65); Option B caps all shares at 70. Option A only
outperforms Option B if XYZ exceeds 75. Below 75, Option B is equal or better.

The sizing decision: solve for the minimum number of calls to sell that covers the put
cost, then verify that the resulting call strike is acceptably above the stock's realistic
price target.

---

## 7. Adjusting the Collar After a Large Move

**After a sharp stock decline:**

Three available actions:
1. *Sell the put* — if the majority of the decline appears finished, selling the now-
   valuable put (while the call has become nearly worthless) removes the protection
   but restores full upside participation if the stock rallies.
2. *Roll put (and optionally call) down to lower strikes* — taking a large credit from
   selling the now-valuable original put and replacing it with a lower-strike put.
   This locks in a portion of the put gain while maintaining downside protection at
   a new, lower floor.
3. *Sell OTM puts against the owned put* — brings in additional credit but exposes
   the stock to losses below the short put strike.

**After a sharp stock rally:**

"There is no convenient exit strategy from a collar on the upside." If the stock rallies
sharply above the short call strike, the only way out is to buy back the call at a large
debit. The unrealized stock gain can offset this, but the transaction is painful and the
investor must decide whether to keep the stock (by paying the debit) or accept
assignment and sell.

**Critical warning — do not write calls against stock you cannot or will not sell:**

"If one sells options against stock that he has no intention of selling, he is actually
writing naked calls in his own mind. That is, if one owns stock that 'can't' be sold —
perhaps the capital gains would be devastating or the stock has been 'in the family' for
a long time — then he should not sell covered calls against it, because he will be forced
into treating the calls as naked (if he refuses to sell the stock)."

In this situation: buy the put outright and pay the premium. Do not try to fund it by
capping a position that is intended to be held indefinitely.

> **Annotation:** The upside exit problem is the most underappreciated risk in the
> collar. When the stock rallies sharply above the short call strike, the investor faces
> a genuinely difficult choice — pay a large debit to remove the cap, or accept
> assignment on stock he may not want to sell. McMillan's naked call warning is the
> most important sentence in the chapter for the value investor: if the stock cannot
> or will not be sold, do not write calls against it under any circumstances. The collar's
> funding mechanism becomes a trap the moment the stock performs well. In that case,
> the correct structure is the outright protective put, paid for in cash, with no call sold
> against it.

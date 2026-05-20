# Chapter 25: Long-Term Option Strategies (LEAPS) —
# Extracted Insights for the Conservative Options Playbook

---

## Foundational Facts: What LEAPS Are

Long-term equity anticipation securities (LEAPS) are simply long-term listed options.
They are generally listed approximately 2.5 years before they expire, giving them
substantially more time than standard equity options. All listed equity LEAPS are
American-style — they can be exercised at any time during their life, just like
shorter-term equity options.

The factors influencing LEAPS prices are identical to those for any listed option:
underlying stock price, striking price, time remaining, volatility of the underlying stock,
risk-free interest rate, and dividend rate. The relative influence of these factors is more
pronounced for LEAPS than for shorter-term equity options — especially interest rates
and dividends, which are minor factors for short-term options but become major
determinants for long-term ones.

**The flat pricing curve:** The most immediately noticeable characteristic of LEAPS
pricing is that the curve is much flatter than for shorter-term options. Even at stock
prices 25% in- or out-of-the-money, a 2-year LEAPS carries so much time value that
its price does not vary as dramatically across strikes as a 3-month option does. This
flatness has direct implications for strike selection — covered in Section 6.

**Directional rules for interest rates and dividends:**
- Increases in interest rates → LEAPS call prices increase; LEAPS put prices increase.
- Increases in dividend payout → LEAPS call prices decrease; LEAPS put prices
  increase.

Both effects are far larger in magnitude for LEAPS than for short-term options.

---

## 1. The Cardinal Rule on LEAPS Valuation: Use a Model, Not Your Eyes

Do not be deluded into thinking that a LEAPS looks cheap merely by comparing its
price to a nearer-term option. Use a model to evaluate it, or at least use the output of
someone else's model.

A 2-year LEAPS, which has eight times the time remaining of a 3-month call, sells for
only about four times as much. This confirms that time decay is not linear. The LEAPS
might appear cheap to the casual observer, but these prices reflect fair value for a given
set of input parameters. One should be careful in evaluating LEAPS until acquiring
experience in observing how their prices relate to the shorter-term equity options with
which one is already experienced.

> **Annotation:** The value investor accustomed to comparing option prices by eyeballing
> premium relative to stock price will be systematically misled with LEAPS. A 2-year call
> that looks expensive at 14 may be fair value; one that looks cheap relative to a 6-month
> call at a quarter of the price may be priced exactly right. Run the model or use someone
> else's output. This is not optional.

---

## 2. The Master Entry Rule: Buy LEAPS When Rates and Volatility Are Low

This rule governs the entire chapter. Because LEAPS expose the buyer to interest rate
and volatility movements for such a long time, entry conditions matter more than they
do for short-term options.

As a general rule, one would want to be a buyer of LEAPS when interest rates are low
and when the volatilities implied in the marketplace are low. If the opposite is true —
high rates and high volatilities — lean toward strategies in which the sale of LEAPS is
used. Since the long-term nature of LEAPS exposes the holder to these movements for
such an extended period, positioning favorably with respect to both elements at entry
is worth doing when possible.

> **Annotation:** This is the macro filter that precedes every LEAPS call purchase in the
> playbook. Low implied volatility AND low interest rates: both inflate LEAPS call prices
> independently. When both are elevated, the buyer is paying a double premium unrelated
> to the stock thesis. Check both before entering.

---

## 3. Interest Rates and Dividends: Hugely Amplified for LEAPS

For short-term options, interest rates and dividends are minor pricing factors. For
LEAPS, they are major ones. The cumulative effect of an interest rate or dividend change
over a 2-year period magnifies in terms of absolute option price to a degree that would
not occur in a 3-month option.

**TABLE: Comparing LEAPS and Short-Term Calls — Change in Price per Unit**

| Variable | Increment | 3-mo. 20% OTM | 2-yr. 20% OTM | 3-mo. ATM | 2-yr. ATM | 3-mo. 20% ITM | 2-yr. 20% ITM |
|---|---|---|---|---|---|---|---|
| Stock Price | +1 pt | .03 | .41 | .54 | .70 | .97 | .89 |
| Volatility | +1% | .03 | .43 | .21 | .48 | .04 | .33 |
| Int. Rate | +½% | .01 | .27 | .08 | .55 | .14 | .72 |
| Dividend | +$.25/qtr | 0 | −.62 | −.08 | −1.18 | −.14 | −1.50 |

The trader accustomed to short-term options might ordinarily ignore a ½% rate change,
a $0.25/quarter dividend change, or a 1% volatility move. The LEAPS trader will gain
or suffer substantially on any of these. In almost every case, the LEAPS call will gain
or lose approximately ½ point of value on each increment.

**On interest rates specifically:** A 3% shift in rates produces a price difference of over
2 points in the ATM 2-year LEAPS, and over 4 points for ITM LEAPS. Any trader
considering in-the-money LEAPS should have a view on the direction of short-term
interest rates.

**On dividends:** A $1 increase in dividends over two years can cause an ITM LEAPS
call to lose approximately 1½ points of value. The reverse applies to LEAPS puts —
a dividend increase causes LEAPS put prices to increase.

**The moderating qualifier:** These figures tend to exaggerate the effects for two reasons.
First, they depict 2-year LEAPS — effects are diminished for options with 10–23 months
remaining. Second, the figures assume instantaneous changes in rates or dividends.
In practice, rate changes occur gradually (typically in increments of 0.25%–0.50%) and
dividend increases do not typically occur immediately after LEAPS are purchased. The
core point stands: interest rates and dividends matter much more for LEAPS than for
short-term options — but investors should not be paralyzed by what looks like
unmanageable sensitivity. The effects unfold over time.

> **Annotation:** The dividend effect on LEAPS calls deserves specific attention for the
> value investor holding dividend-paying names. A company that raises its dividend during
> the life of a long LEAPS call will cause that call to lose additional value — a headwind
> absent from short-term positions. For LEAPS puts used as protection, a dividend
> increase is a tailwind. When choosing between call substitution (sell stock, buy LEAPS
> call) and put protection (keep stock, buy LEAPS put), this asymmetry is a further
> argument in favor of keeping the stock and buying the put.

---

## 4. LEAPS Time Decay: Slow at First, Then Rapidly Accelerating — With Precise Roll Triggers

**TABLE: Daily Percent Time Value Decay**

| Months Remaining | At-the-Money | 20% Out-of-the-Money |
|---|---|---|
| 24 | .12% | .18% |
| 18 | .14% | .27% |
| 12 | .19% | .55% |
| 9 | .22% | .76% |
| 6 | .27% | 1.18% |
| 3 | .60% | 3.57% |
| 2 | .73% | 4.43% |
| 1 | 1.27% | — |
| 2 weeks | 3.33% | — |

Most LEAPS, even OTM ones, lose less than ¼ of one percent of their value daily —
a pittance compared with a 6-month equity option that is 20% OTM, which loses well
over 1% of its value daily while still having 6 months of life remaining.

**The "25% in 6 months" concrete warning:** Do not be deluded into believing that
LEAPS don't decay meaningfully. Although the daily rate of decay is small, cumulative
decay is real. Example: XYZ at 60; 18-month ATM LEAPS call at $8. Daily decay is
minuscule — barely an eighth of a point per week. But if the stock remains at 60 for
6 months, the LEAPS call will be worth approximately $6. That is a 25% loss of value
from time decay alone, even though the daily number seems trivial.

Investors accustomed to short-term options expect 25% losses in 4–5 weeks. In LEAPS,
the same 25% loss takes 6 months. The advantage is obvious from a timing tolerance
standpoint — but the loss is real and must be accounted for.

**Roll trigger rule — ATM:** The ATM option's decay curve bends dramatically upward
soon after the 6-month time barrier is passed. Sell the long ATM call when approximately
6 months remain and simultaneously buy a 2-year LEAPS call. This keeps time decay
exposure on the flat part of the curve.

**Roll trigger rule — OTM:** The 20% OTM call begins to decay much more rapidly
at sometime just before 1 year until expiration. Sell the long OTM call when
approximately 1 year remains and reestablish the position by buying a 2-year LEAPS
call at the same time.

> **Annotation:** Two hard roll triggers: roll ATM LEAPS calls at 6 months remaining;
> roll OTM LEAPS calls at 1 year remaining. These are the inflection points where the
> decay curve bends sharply upward and the position begins to behave like a normal
> short-term option. For the value investor with a thesis that may take longer than
> expected to play out, buy 18–24 month LEAPS to stay on the flat part of the decay
> curve. If the thesis remains intact at the roll trigger, roll forward rather than watch
> premium erode at an accelerating rate.

---

## 5. Volatility Expansion as a Second Source of Profit When Buying Cheap LEAPS

When LEAPS are purchased at historically low implied volatility and low interest rates,
rising volatility can preserve or increase the call's value even if the stock is flat or
slightly down.

**Setup:** XYZ: 100; January 2-year LEAPS call, strike 100: 14; rates at a historically
low 3%; volatility below historical average.

**TABLE: Factors necessary for the 2-year LEAPS call to remain at 14**

| Stock Price | After 1 Month | After 6 Months |
|---|---|---|
| 100 (unchanged) | r = 3.4% OR v + 5% | r = 6% OR v + 20% |
| 95 | r = 6% OR v + 20% | r = 9.4% OR v + 45% |
| 90 | r = 8.5% OR v + 45% | r = 12.6% OR v + 70% |

If XYZ is unchanged after one month, a 5% relative increase in volatility (not 5
percentage points — 1/20th of the original level) is sufficient to keep the call at 14
despite one month of time decay having passed.

Volatility is the dominant factor. It is often feasible for volatilities to change by as much
as 50% from their previous level in a month, and certainly in six months. Rate changes
of the magnitude needed to offset larger stock declines are less realistic. Volatility
movements are not.

> **Annotation:** This table is one of the most practically useful in the chapter. When
> buying LEAPS at historically low implied volatility, the investor gains a second engine
> of return independent of the stock's direction: volatility expansion. Even a flat or
> mildly declining stock can return to break-even or better if implied volatility normalizes
> upward. The practical screening step: before buying any LEAPS call, check whether the
> stock's current implied volatility is at the low end of its historical range. If it is, entry
> is structurally advantaged. If implied volatility is elevated, the investor has no
> volatility tailwind and must rely entirely on the stock moving.

---

## 6. LEAPS Call Delta: Higher Than Short-Term, Flatter Across Strikes

**Directional summary:** LEAPS calls move faster than ordinary short-term equity calls
in absolute price terms (not percentage terms), unless both options are more than 5%
in-the-money. At that point the deltas are approximately equal, and more deeply ITM,
the short-term call has the higher delta.

The longer the life of an at-the-money option, the greater its delta. ATM 2-year LEAPS
calls have a delta of approximately 0.70, versus approximately 0.50 for very short-term
ATM calls.

**The flat delta curve — strike selection implication:**

Because the LEAPS delta curve is relatively flat across strikes, the usual ITM vs. OTM
selection logic from Chapter 3 is reversed:

**Example:** XYZ: 82.

| Option | Price | Delta |
|---|---|---|
| April 80 call (3-month) | 4 | 5/8 |
| April 90 call (3-month) | 1 | 1/8 |
| January 80 LEAPS call | 14 | 3/4 |
| January 90 LEAPS call | 7 | 1/2 |

Expected stock move: 3 points (82 to 85).

Short-term calls: April 80 gains ~1⅞; April 90 gains ~⅜. Large discrepancy — ITM
call wins.

LEAPS calls: January 80 gains ~2¼; January 90 gains ~1½. Much smaller discrepancy.
The January 90 sells for half the price of the January 80, but moves only 33% less.
On a percentage return basis, the January 90 LEAPS wins.

**Conclusion:** With short-term options, buy ITM for moderate expected moves. With
LEAPS, the flat delta curve means the slightly OTM call — at half the price — wins on
percentage return per dollar invested for the same expected move.

> **Annotation:** This reversal of strike selection logic applies at the first OTM strike,
> not five strikes out. The percentage advantage exists between adjacent strikes where
> the delta differential is small. Do not use this logic to justify buying deeply OTM
> LEAPS calls — the delta approaches zero at extreme strikes and the percentage
> advantage disappears. The correct application: when buying LEAPS calls, consider the
> first OTM strike as a viable alternative to ATM or slightly ITM, and compare the
> expected return per dollar invested using the delta of each.

---

## 7. LEAPS Put Delta: Low and Flat — Protective Use Yes, Speculative Use No

**Directional summary:** While short-term puts move slower than LEAPS calls, short-
term puts move faster than LEAPS puts in most cases. The put delta relationship
(put delta = call delta − 1) inverts the call relationships.

The LEAPS put delta curve is flat and not very large anywhere. Specifically: an
at-the-money 2-year LEAPS put moves only approximately 30 cents for a one-point
move in the underlying stock. It takes approximately a 3-point move in the underlying
for an ATM LEAPS put to gain 1 point of value.

**The two-way implication:**

For *speculative* put buying (expecting a stock decline): LEAPS puts are the wrong
tool. The low delta means the put does not leverage a stock decline effectively. Short-
term puts provide far more dollar participation per point of stock decline.

For *protective* put buying (hedging a long stock position): LEAPS puts are the right
tool. The investor does not need the put to move dollar-for-dollar with the stock on a
daily basis. He needs it to carry substantial intrinsic value if the stock declines
significantly over the life of the put — and it will, regardless of the low starting delta.
The low-delta warning is irrelevant for protection; what matters is the payoff at the
scenario that requires the hedge.

> **Annotation:** The speculative/protective distinction is the key dividing line. For
> bearish directional speculation, buy short-term puts. For multi-year portfolio
> protection on a long stock position, LEAPS puts are precisely right — slow daily
> movement is a feature, not a bug, because it means slow daily cost while the insurance
> remains in force.

---

## 8. LEAPS as Stock Substitute: The Full Economic Calculation

The strategy: sell existing stock, buy a deeply ITM LEAPS call, invest the difference in
a 1-year CD or Treasury bill. This provides continued upside participation with defined
downside risk.

Costs of switching: time value premium of the call, loss of dividends, commissions.
Benefits: interest earned on the freed capital, less downside risk than owning the stock.

**Example — Substitution for Stock Currently Held Long:**

XYZ at 50; 1-year LEAPS strike 40 at $12; annual dividend $0.50; rates 5%.
Call time value premium = 2 points (40 + 12 − 50).

*Step 1 — Net credit generated:*

| | |
|---|---|
| Sale of 100 XYZ at $50 | $5,000 |
| Less stock commission | −$25 |
| Net sale proceeds | $4,975 credit |
| Cost of 1 LEAPS call | $1,200 |
| Plus option commission | +$15 |
| Net cost of call | $1,215 debit |
| **Total credit balance** | **$3,760** |

*Step 2 — Costs and benefits:*

| | |
|---|---|
| Time value premium | −$200 |
| Loss of dividend | −$50 |
| Stock commission | −$25 |
| Option commission | −$15 |
| Total cost | −$290 |
| Interest on $3,760 at 5% for 1 year | +$188 |
| **Net cost of switching** | **−$102** |

Result: $102 paid to limit downside to approximately 39½. If XYZ falls dramatically and
the LEAPS expires worthless, $3,948 remains in the bank — equivalent to a floor of 39½
on the original 100 shares.

The freed capital should be placed in a 1-year CD or T-bill for two reasons: it locks in
the rate used in the calculation, and it prevents the temptation to deploy the cash
elsewhere in a way that negates the protection.

**Four caveats before executing:**
1. If the stock is currently profitable, the sale generates a taxable capital gain.
2. If the stock is at a loss, buying the call constitutes a wash sale — the loss cannot
   be taken at this time.
3. If the company declares an increased or special dividend during the LEAPS life,
   the call owner is not entitled to it.
4. At expiration, repurchasing the stock or rolling the call incurs additional
   commissions.

> **Annotation:** Run all four caveats before executing. The wash sale caveat is
> particularly dangerous — substituting into a LEAPS call on a loss position defers the
> tax loss without the investor necessarily realizing it. The comparison in Section 10
> will often reveal that simply buying a LEAPS put and keeping the stock is a cheaper,
> cleaner way to achieve the same protection.

---

## 9. Buying LEAPS as the Initial Stock Purchase: Often Superior to Buying the Stock

Rather than buying the stock, a prospective purchaser can buy a LEAPS call and place
the remainder of the planned stock capital in an interest-bearing account.

**Example — Cash account:**

XYZ at 50; 1-year LEAPS strike 40 at $12; dividend $0.50; rates 5%.

| | |
|---|---|
| Stock: $5,000 + $25 commission | $5,025 |
| LEAPS: $1,200 + $15 commission | $1,215 |
| **Net difference available for bank** | **$3,810** |

| Costs vs. savings | |
|---|---|
| Time value premium | −$200 |
| Loss of dividend | −$50 |
| Interest on $3,810 at 5% for 1 year | +$190 |
| **Net opportunity cost** | **−$60** |

For $60, the investor has all the upside appreciation (except $60 worth) and risk only
down to 40 — with $4,000 in the bank if the LEAPS expires worthless.

**Example — Margin account:**

Same facts; planned margin purchase at 50% on an 8% margin rate.

| | |
|---|---|
| Equity required for margin purchase | $2,513 |
| Cost of LEAPS | $1,215 |
| **Difference available for bank** | **$1,298** |

| Costs vs. savings | |
|---|---|
| Time value premium | −$200 |
| Dividend loss | −$50 |
| Interest on $1,298 at 5% | +$65 |
| Margin interest saved on $2,512 at 8% | +$201 |
| **Net savings** | **+$16** |

For the prospective margin buyer, there is a real net savings from buying LEAPS instead
of margin stock — before counting the downside protection benefit.

The catch-22: high interest rates make the bank deposit credit more valuable but also
inflate the LEAPS price. The two effects partially offset. The margin comparison is less
affected by this catch-22 because the margin interest saved scales with the same rate
environment.

> **Annotation:** Run this calculation before every new position where a LEAPS call
> exists on the target stock. The margin comparison is particularly compelling: at 8%
> margin rates, buying LEAPS produces a net savings versus buying on margin, with
> downside protection as a free addition. The main ongoing drawback: no participation
> in dividend increases or special dividends.

---

## 10. Protecting Existing Stock with LEAPS Puts: The Decision Rule Against the Substitution Strategy

The substitution strategy and the put protection strategy accomplish the same thing:
limited downside risk with continued upside participation. The decision between them
is mechanical.

**The decision rule:**

Step 1: Perform the substitution calculation from Section 8. Find the implied cost of
the embedded protection. In the example: net cost = $102, protecting at 39½. The
investor is in effect paying $152 for a LEAPS put with a strike of 40 (the $102 net
cost plus the $50 difference between the 40 strike and the 39½ effective floor).

Step 2: Check the actual market price of the LEAPS put at that strike.

Step 3:
- If market price < $152 → buy the put outright, keep the stock. Cheaper, cleaner,
  retains dividends, avoids the tax event of selling.
- If market price > $152 → the substitution strategy is more economical.

**Why the put almost always wins in practice:** The put preserves dividend participation,
avoids a taxable capital gain on the stock sale, requires only one commission, and
sidesteps the wash sale issue entirely. Put-call parity prevents puts from being
systematically overpriced relative to calls in liquid names. In practice, step 3 almost
always favors the put.

Because of the LEAPS' long-term nature, one does not have to keep reestablishing the
position and paying repeated commissions, as would be required with short-term options.
Run the calculation once, then reassess only at the roll trigger point.

> **Annotation:** The decision rule is clean and mechanical. Do the calculation. In most
> cases for the value investor holding a dividend-paying stock with a meaningful cost
> basis, the put wins. The substitution strategy is primarily useful when the stock is at
> a loss (no capital gains tax issue) and pays no dividend (no dividend forfeiture) — a
> less common profile in the playbook.

---

## 11. LEAPS Covered Writing: The Annualized Return Comparison and the Real Advantage

**Example:** XYZ at 50; 500 shares; July 50 call at 4 (6 months); January 50 LEAPS
call at 8½ (2 years); dividend $0.25/quarter.

**Net Investment:**

| | July 50 | January 50 LEAPS |
|---|---|---|
| Stock cost (500 @ 50) | $25,000 | $25,000 |
| Plus commission | +$300 | +$300 |
| Less premiums received | −$2,000 | −$4,250 |
| Plus option commission | +$50 | +$100 |
| **Net investment** | **$23,350** | **$21,150** |

**Return If Exercised:**

| | July 50 | January 50 LEAPS |
|---|---|---|
| Net profit if exercised | $1,600 | $4,550 |
| Return if exercised | 6.9% | 21.5% |
| **Annualized** | **13.8%** | **10.8%** |

On an annualized basis, the short-term write appears better. This is the general rule:
shorter-term calls have higher annualized returns than LEAPS calls.

**Why the annualized comparison is misleading:**

The short-term writer must regenerate his 6.9% return three more times over two years
with no guarantee that equivalent premium will be available. Additionally, LEAPS
premium does not decay linearly — one year from now, if XYZ remains at 50, the
January LEAPS 50 call will not be at 4.25 (half of 8.50); it will be closer to 5.00. The
stated 10.8% annualized LEAPS return is therefore understated.

**The real advantage — downside break-even:**

| | July 50 | January 50 LEAPS |
|---|---|---|
| Net investment | $23,350 | $21,150 |
| Less dividends | −$250 | −$1,000 |
| Stock cost to expiration | $23,100 | $20,150 |
| Break-even price | **46.2** | **40.3** |

The LEAPS covered write provides a break-even of 40.3 — a known, locked-in quantity
for two years. The short-term writer's 46.2 must be repeatedly lowered through
successive writes with no certainty of success.

**The incremental return use case:** The covered writer with a higher long-term target
price who writes calls along the way to earn incremental premium should prefer LEAPS
calls when available — they offer the largest absolute premiums. If currently short a
near-term call that is about to result in assignment, consider rolling into a LEAPS call
to retain the stock while taking in substantially more premium.

**McMillan's end-of-chapter summary on LEAPS puts vs. LEAPS covered writes:**
Selling naked LEAPS puts is probably a better strategy than LEAPS covered writing
in most cases. The covered write requires full stock capital; the naked put generates
similar premium with far less capital deployed, with the remainder available in
interest-bearing securities.

**Critical warning on rolling down into LEAPS:** If the underlying stock declines, rolling
down into a LEAPS call reduces maximum profit potential for a much longer period of
time than rolling into a short-term call would. Do not roll down into a longer-maturity
option without carefully analyzing whether a two-year commitment to a declining stock
is actually wanted.

> **Annotation:** For the value investor who is genuinely long-term bullish and wants to
> own the stock for two years, the LEAPS covered write provides a meaningfully lower
> break-even at the cost of roughly 3 annualized percentage points of return. The
> naked LEAPS put summary is noteworthy: it implies that for investors who want
> covered-write-like exposure without full stock capital commitment, selling a cash-
> secured LEAPS put is the cleaner structure — same economic exposure, less capital,
> more flexibility.

---

## 12. LEAPS Put Selling: Short-Term Puts Are Better for the Assignment Strategy

Some put writers sell puts specifically intending to be assigned — they want to buy the
stock at a net cost of strike price minus premium received. If they are not assigned, they
keep the premium as profit. This is a valid approach for stocks the investor has genuine
conviction in and would view assignment as a buying opportunity.

**This strategy does not work well with LEAPS puts.** Because LEAPS puts carry
significant time value premium, there is little or no chance the writer will be assigned
until the life of the put shortens substantially. The writer intending to become a stock
owner via assignment would have to wait until LEAPS expiration approaches — a
period of up to 2.5 years — before assignment is likely.

**Practical rule:** If the intent is to eventually own the stock through put assignment at
a favorable price, write short-term puts, not LEAPS puts. Short-term puts are more
likely to result in timely assignment when the stock trades below the strike.

Early assignment on any LEAPS option follows the same rule as for short-term options:
it is most likely when the option has no time value premium remaining — trading at
parity or at a discount. Since LEAPS retain time value even substantially in-the-money,
early assignment is rare but possible and should be monitored in the same way.

---

## 13. The LEAPS Bull Spread and the Diagonal: Full Three-Way Comparison

**Example prices in January:** XYZ: 105; April 100 call: 10.50; April 110 call: 5.50;
January 2-year 100 call: 26; January 2-year 110 call: 21.50.

| Strategy | Structure | Net Debit |
|---|---|---|
| Short-term bull spread | Buy April 100 / Sell April 110 | $500 |
| Diagonal bull spread | Buy Jan LEAPS 100 / Sell April 110 | $2,050 |
| LEAPS bull spread | Buy Jan LEAPS 100 / Sell Jan LEAPS 110 | $450 |

**Results at April expiration:**

| Stock Price | Short-Term | Diagonal | LEAPS |
|---|---|---|---|
| 80 | −$500 | −$1,100 | −$200 |
| 90 | −$500 | −$600 | −$150 |
| 100 | −$500 | +$50 | −$25 |
| 110 | +$500 | +$750 | +$50 |
| 120 | +$500 | +$550 | +$150 |
| 140 | +$500 | +$150 | +$250 |
| 160 | +$500 | −$50 | +$350 |
| 180 | +$500 | −$350 | +$450 |

**The LEAPS bull spread:** Generates very little profit or loss in only three months —
typical for long-term bull spreads when both options have significant time premium
remaining. At XYZ 120, profit is only $150. At XYZ 80, loss is only $200. For a
genuinely bullish investor willing to wait, the LEAPS spread at $450 produces similar
terminal profits to the short-term spread at $500 with dramatically less interim downside
risk.

**The diagonal — a neutral strategy in disguise:**

The diagonal spread presents an opportunity to earn more money if the underlying
stock is near the strike of the written option when the short option expires. However,
if the stock moves a great deal in either direction, the diagonal is the worst of the
three strategies. This makes the diagonal a neutral strategy — one wants the underlying
to remain near the written strike until the near-term option expires — regardless of
how it is labeled.

**The delta problem in diagonals:** When XYZ is at 120:
- Long 1 January LEAPS 100 call: delta +0.70
- Short 1 April 110 call: delta −0.90
- Net delta: −0.20

If XYZ rises by 1 point, the spread loses 20 cents. The short option's delta exceeds
the long option's delta — the spread is actually short the market above this price. A
bullish spread that loses money when the stock rises is not a bull spread in any
meaningful sense.

**The bottom-line rule on diagonal debits:** If one pays a debit greater than the
difference in the strike prices, the position may eventually lose money if the stock rises
far enough to eliminate time value premium from both options.

Many traders are fond of buying LEAPS and selling an OTM near-term call as a hedge.
Be careful. If the underlying rises too fast and/or interest rates fall and/or volatility
decreases, this is a poor strategy. There is nothing quite as psychologically damaging
as being right about the stock but being in the wrong strategy and losing money anyway.

> **Annotation:** The three-way comparison makes the correct choice clear for a
> bullish investor. The LEAPS bull spread (same expiration, two strikes) at $450 is the
> right vehicle — it maintains a genuinely bullish profile at all stock prices, with less
> interim downside than the short-term spread and dramatically better behavior than the
> diagonal if the stock moves strongly. The diagonal is a neutral strategy and should only
> be used by investors who believe the stock will be range-bound through the near-term
> expiration. If you are bullish, use the LEAPS bull spread, not the diagonal.

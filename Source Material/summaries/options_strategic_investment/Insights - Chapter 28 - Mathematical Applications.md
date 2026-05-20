# Chapter 28: Mathematical Applications —
# Extracted Insights for the Conservative Options Playbook

---

## Foundational Vocabulary: The Black-Scholes Variables

The Black-Scholes model prices a call option using six inputs. Understanding what each
variable represents is prerequisite to understanding everything else in this chapter.

**Variables:**
- p = stock price
- s = striking price
- t = time remaining until expiration, expressed as a percent of a year
- r = current risk-free interest rate
- v = volatility measured by annual standard deviation
- ln = natural logarithm
- N(x) = cumulative normal density function

---

## 1. The Black-Scholes Formula

The actual formula:

**Theoretical option price = pN(d₁) − se^(−rt)N(d₂)**

where:

$$d_1 = \frac{\ln\left(\frac{p}{s}\right) + \left(r + \frac{v^2}{2}\right)t}{v\sqrt{t}}$$

$$d_2 = d_1 - v\sqrt{t}$$

**Delta as a direct output of the model:**

An important by-product of the Black-Scholes formula is the exact calculation of
delta — the amount by which the option price can be expected to change for a small
change in the stock price. Delta is not computed separately; it falls directly out of
the model:

> **Delta = N(d₁)**

This means that any platform running Black-Scholes is simultaneously computing delta
at no additional cost. Delta is more formally known as the hedge ratio.

---

## 2. Adjusting Black-Scholes for Dividends

The base Black-Scholes model does not include dividends. Direct application to
dividend-paying stocks produces inflated call prices. Fisher Black's two-step correction:

**Step 1:** Subtract the present value of all dividends expected to be paid before option
expiration from the current stock price. Use this adjusted stock price in the formula
and calculate the theoretical call price.

**Step 2:** Assume the option expires just prior to the last ex-dividend date before actual
expiration. Adjust the stock price accordingly and calculate the theoretical call price
again.

**Rule:** Use the higher of the two resulting prices as the theoretical call price.

The dividend correction does not need to be applied for every strategy decision. In many
applications an approximate value is sufficient. However, for any strategy involving
dividend-paying stocks where the exact theoretical value matters — evaluating whether
a specific call is overpriced or underpriced — apply the correction before drawing
conclusions.

---

## 3. Historical Volatility: Definition and the Lognormal Adjustment

**Historical volatility** is computed from past stock prices. It tells you what volatility
was. It is the standard statistical definition of annual standard deviation applied to
stock price changes.

**The standard historical volatility formula:**

$$\sigma^2 = \frac{\sum_{i=1}^{n}(P_i - \bar{P})^2}{n-1}$$

$$v = \sigma / \bar{P}$$

where:
- $\bar{P}$ = average stock price of all $P_i$'s
- $P_i$ = daily stock price
- $n$ = number of days observed
- $v$ = volatility

Historical volatility has a known limitation: it encompasses too long a period of time
to accurately represent current conditions. Volatilities change over time — a large stock
split may reduce volatility; entry into a more speculative business may increase it.
Recent price action should be weighted more heavily than older action when estimating
current volatility.

**The lognormal adjustment:** The standard formula above does not give the correct
input for Black-Scholes, because the model assumes that the *logarithms* of price
changes are normally distributed — not the prices themselves.

Example: XYZ closes at 51 today, 50 yesterday.
- Arithmetic percentage change: 51/50 = 1.02, or **2.00%**
- Lognormal input: ln(51/50) = ln(1.02) = **0.0198, or 1.98%**

If the stock is down the next day from 51 back to 50:
ln(50/51) = ln(0.9804) = **−0.0198**

The correct volatility formula consistent with Black-Scholes uses lognormal price
relatives:

$$v = \sqrt{\frac{\sum_{i=1}^{n}(X_i - \bar{X})^2}{n-1}}$$

where $X_i = \ln(P_i / P_{i-1})$; $P_i$ = closing price on day $i$; and $\bar{X}$ = the
average of the $X_i$'s over the desired number of days.

In practice, any modern options analytics platform computes this automatically. The
concept matters — understand that the volatility input to Black-Scholes is based on
log-price changes, not arithmetic price changes — but manual computation is not
required.

---

## 4. Implied Volatility: Letting the Market Compute Volatility For You

**Implied volatility** is derived from current market prices. It tells you what the market
is pricing in now. For strategy decisions, implied volatility is the more useful input
because it reflects current conditions rather than historical ones.

The derivation: fix the observed market price of a liquid, near-the-money option in the
Black-Scholes equation and solve for the volatility that produces it. This is done by
iteration — trying successive volatility values until the model price matches the market
price. The result is the implied volatility for that specific option.

---

## 5. Composite Implied Volatility: The Weighted Average Across All Options on a Stock

Each option on a given stock will produce a different implied volatility when solved
individually. To derive a single composite implied volatility for the underlying stock,
these individual values must be weighted by two factors: trading volume and distance
from the current stock price.

**Why weight by volume:** Options with high trading volume are more likely to be fairly
priced. Their implied volatilities carry more information.

**Why weight by distance:** Options far in- or out-of-the-money are less reliably priced
and should receive little or no weight regardless of volume. The distance weighting
function uses a parabolic formula that assigns decreasing weight as the option moves
away from at-the-money, and zero weight beyond a chosen maximum distance (typically
25% from the current stock price). The parabola ensures that options just slightly OTM
are not arbitrarily penalized, while options far from the money are effectively excluded.

**Worked example:** XYZ is at 33. Maximum distance for weighting: 25%.

**TABLE 28-1. Implied volatilities, closing price, and volume.**

| Option | Option Price | Volume | Implied Volatility |
|---|---|---|---|
| January 30 | 4.50 | 50 | .34 |
| January 35 | 1.50 | 90 | .28 |
| April 35 | 2.50 | 55 | .30 |
| April 40 | 1.50 | 5 | .38 |

**TABLE 28-2. Volume weighting factors.**

| Option | Volume | Volume Weighting Factor |
|---|---|---|
| January 30 | 50 | .25 (50/200) |
| January 35 | 90 | .45 (90/200) |
| April 35 | 55 | .275 (55/200) |
| April 40 | 5 | .025 (5/200) |

**TABLE 28-3. Distance weighting factors (25% maximum).**

| Option | Distance from Stock Price | Distance Weighting Factor |
|---|---|---|
| January 30 | .091 (3/33) | .41 |
| January 35 | .061 (2/33) | .57 |
| April 35 | .061 (2/33) | .57 |
| April 40 | .212 (7/33) | .02 |

**TABLE 28-4. Final composite implied volatility calculation.**

| Option | Volume Factor | Distance Factor | Implied Vol |
|---|---|---|---|
| January 30 | .25 | .41 | .34 |
| January 35 | .45 | .57 | .28 |
| April 35 | .275 | .57 | .30 |
| April 40 | .025 | .02 | .38 |

Composite IV = (.25×.41×.34 + .45×.57×.28 + .275×.57×.30 + .025×.02×.38) /
(.25×.41 + .45×.57 + .275×.57 + .025×.02) = **.298**

The composite figure gives the most weight to the heavily traded, near-the-money
options (January 35 at 90 contracts, January 30 at 50 contracts) and nearly zero weight
to the lightly traded, deeply OTM April 40 call (5 contracts).

**Smoothing day-to-day noise:** On a day-to-day basis, implied volatility can fluctuate
more than is useful for strategy decisions. Two smoothing approaches:

1. Take a 20- or 30-day moving average of daily composite implied volatilities.
2. Use a momentum calculation: today's final volatility = (5% × today's implied
   volatility) + (95% × yesterday's final volatility). This requires saving only one
   prior data point and still produces a meaningful smoothing effect.

**The key application:** Once the composite implied volatility is computed, use it in
Black-Scholes to calculate the theoretical value of each individual option. Since the
composite IV will differ from any specific option's individual implied volatility, a
discrepancy will appear between the option's actual market price and its model-derived
theoretical price. This discrepancy represents the amount by which that specific option
is theoretically overpriced or underpriced *relative to other options on the same stock*.

This method is sensitive to real-time volatility changes. As markets become bullish or
bearish and option premiums expand, the composite implied volatility picks up the
change quickly.

> **Annotation:** Two direct applications to the playbook. First: tracking a stock's
> composite implied volatility over time — using a 20- or 30-day smoothed series —
> identifies when implied volatility is historically low (correct entry condition for buying
> LEAPS calls or protective puts per Chapter 25's master entry rule) vs. historically
> elevated (when writing covered calls or selling puts is more attractive). Second: the
> overpriced/underpriced differential identifies which specific strike or expiration is
> relatively cheap within a given stock's option chain. When building a LEAPS call or
> bull spread, buy the option whose individual implied volatility is lowest relative to the
> composite — not the one that simply looks cheap on absolute premium.

---

## 6. The Volatility Skew: Identifying Unusual Pricing Across Strikes

A volatility skew exists when different strikes or expirations on the same underlying
stock carry materially different implied volatilities. The skew factor quantifies this
dispersion.

**Three-step calculation:**
1. Calculate the individual implied volatility of each option. Exclude options with
   little or no remaining time value premium — they are not representative of
   normal pricing.
2. Calculate the standard deviation of those implied volatilities (unweighted —
   no volume or distance adjustment needed here).
3. Divide by the composite implied volatility from Section 5.

> **Skew factor = Standard deviation of individual IVs / Composite IV**

**Example:** XYZ at 6.50.

| Option | Implied Volatility |
|---|---|
| Mar 5 call | 85.0% |
| June 5 call | 77.5% |
| Mar 7.5 call | 75.0% |
| June 7.5 call | 70.0% |

Standard deviation of {85.0, 77.5, 75.0, 70.0} = 6.25.
Composite IV = 75.0%.
Skew factor = 6.25 / 75.0 = **8.3%**

Compute skew factors for all stocks and rank them. Those with the highest skew
factors are most likely to have a distinct, exploitable volatility skew.

**Two common skew patterns:**

- *Horizontal skew:* Options expiring just after a known event (earnings, FDA
  decision, legal verdict) carry elevated implied volatility relative to all other
  expirations.
- *Vertical skew:* Lower-strike options carry higher implied volatility than
  higher-strike options. The standard post-1987 pattern — the market prices
  downside tail risk more expensively than upside.

Build a database of daily composite IV and skew factor for every stock traded.
Computing percentiles over time — where does today's IV rank versus the past year —
enables the investor to determine whether options are genuinely cheap or expensive,
not just cheap or expensive relative to recent history.

> **Annotation:** The vertical skew is directly relevant to protective put buyers. When
> the skew is steep, OTM puts are expensive relative to ATM puts. In that environment,
> the Chapter 17 default (buy the first OTM strike) should be reconsidered — the ATM
> put may offer better value per dollar of protection. The horizontal skew is relevant
> for stocks heading into a known binary event: if near-term implied volatility is
> dramatically elevated, selling a near-term covered call harvests that elevated premium
> more efficiently than buying a near-term put for protection.

---

## 7. Converting Annual Volatility to a Sub-Period Volatility

Since the option modeler is generally interested in time periods other than one year,
the annual volatility must be converted into a volatility for the time period in question.
This is accomplished by:

$$v_t = v\sqrt{t}$$

where:
- v = annual volatility
- t = time, in years
- v_t = volatility for time t

Example: a 3-month volatility equals one-half the annual volatility.
t = 0.25 (one quarter of a year), so v₀.₂₅ = v√0.25 = **0.50v**

This formula is used in every probability calculation and in the call ranking framework.
It is simple and should be applied automatically whenever a sub-period analysis is
performed.

---

## 8. Computing the Probability of a Stock Being at a Given Price

The lognormal distribution provides a formula for computing the probability of a stock
being below a given price at the end of a fixed time period. This drives both expected
return calculations and downside protection analysis.

**Critical scope limitation:** These probabilities apply to the price at the *end* of the
time period only. They say nothing about the probability of the stock touching a given
price at any point *during* the period. Computing path-dependent probabilities requires
a substantially more complex calculation.

**The probability formula:**

$$P(\text{below}) = N\left(\frac{\ln\left(\frac{q}{p}\right)}{v_t}\right)$$

where:
- N = cumulative normal distribution
- p = current price of the stock
- q = price in question
- ln = natural logarithm for the time period in question
- v_t = volatility for the time period (from Section 7)

$$P(\text{above}) = 1 - P(\text{below})$$

For computing the probability of the stock being at a specific price x (rather than
above or below a threshold), the iterative equation is:

$$P(\text{of being at price } x) = P(\text{below } x) - P(\text{below } y)$$

where y is close to but less than x in price. Summing these incremental probabilities
across a range of prices produces the full expected return calculation.

**Worked example — evaluating a covered write:**

XYZ at 43; 6-month July 40 covered write; downside break-even at expiration: 36.
Annual volatility: 25%.

6-month volatility: v_t = 0.25 × √0.50 = **0.177**

P(below 36 in 6 months) = N(ln(36/43) / 0.177) = N(−0.178 / 0.177) = N(−1.006) = **15.8%**

Interpretation: approximately 84% probability that XYZ will be above the break-even
point at expiration. McMillan's assessment: an attractive covered write on a conservative
basis.

**Application to ranking covered writes:** Among all covered writes meeting a minimum
return threshold (e.g., 12% annualized), rank by lowest probability of loss at expiration.
This is superior to arbitrary rules like "the stock must have at least X% downside
protection" because it accounts for stock volatility — a 10% downside cushion on a
50% volatility stock carries a much higher probability of loss than the same cushion on
a 20% volatility stock.

**Application to protective puts:** Given a stock at price p and a put strike at q,
P(below q) gives the probability that the put will expire in-the-money. This is the
probability-adjusted value of the protection being purchased — a direct input to
deciding whether the put premium is worth paying.

---

## 9. Expected Return: The Probability-Weighted Framework for Strategy Evaluation

Expected return is the return a position should yield over a large number of cases,
computed by multiplying each possible outcome by its probability and summing the
results. It converts intuitive assessments of value into a single comparable number,
and formalizes the "dollar for 70 cents" language in the investment philosophy.

**Simple example:** XYZ is at 33. Assumed probability distribution for 6 months:

| XYZ Price | Probability |
|---|---|
| Below 30 | 20% |
| 31 | 10% |
| 32 | 10% |
| 33 | 10% |
| 34 | 10% |
| Above 35 | 40% |

Bull spread established: buy February 30 call, sell February 35 call, 2-point net debit
($200 investment). Maximum profit = $300 if above 35; maximum loss = $200 if below 30.

**Expected return calculation:**

| XYZ Price | Probability | Spread Result | Expected Result |
|---|---|---|---|
| Below 30 | 20% | −$200 | −$40 |
| 31 | 10% | −$100 | −$10 |
| 32 | 10% | $0 | $0 |
| 33 | 10% | +$100 | +$10 |
| 34 | 10% | +$200 | +$20 |
| Above 35 | 40% | +$300 | +$120 |
| **Total** | **100%** | | **+$100** |

Expected profit = $100. Expected return = $100 / $200 = **50%**.

A position with a 50% expected return offers approximately $1.50 of expected value
for each $1.00 invested — the formal expression of "dollar for 70 cents."

The expected return framework can also derive a theoretical option value independent
of Black-Scholes: compute the probability of the stock being at each price above the
striking price at expiration, weight each outcome by the intrinsic value at that price,
and sum. The result is a probability-based theoretical option price.

---

## 10. Ranking Call Purchases: The Volatility-Normalized Reward/Risk Framework

Evaluating call purchases based on the volatility of the underlying stock is the correct
method. Any ranking based on equal percentage moves across stocks — without
accounting for each stock's probability of making that move — is useless.

**The complete 11-step procedure:**

**Setup:**
1. Specify the stock movement assumption in standard deviations. Recommended:
   **0.7 standard deviations** (see calibration note below).
2. Fix the holding period: 30, 60, or 90 days.

**Profitability (upside):**

3. Calculate the upward stock target:

$$q = p \times e^{(a \times v_t)}$$

where p = current stock price, a = number of standard deviations, v_t = volatility
for the holding period.

4. Use Black-Scholes to price the call at the new stock price with reduced time
   remaining (original expiration minus the holding period).
5. Calculate percentage profit: (new option price − original price) / original price.
   Deduct commissions.
6. Repeat steps 4–5 for each option on the stock.

**Risk (downside):**

7. Calculate the downward stock target:

$$q = p \times e^{(-a \times v_t)}$$

Note: due to the lognormal distribution, the downward distance is slightly smaller
than the upward distance for the same number of standard deviations.

8. Price the call at the declined stock price using Black-Scholes.
9. Calculate percentage loss: (original price − new option price) / original price.
   Deduct commissions.
10. Reward/risk ratio = percentage profit (step 5) / percentage loss (step 9).
11. Repeat steps 8–10 for each option on the stock.

**Complete example:** XYZ at 41; annual volatility 30%; XYZ January 40 call at 4;
6 months to January expiration; 90-day holding period; 1.0 standard deviation
assumption.

90-day volatility: v_t = 0.30 × √0.25 = 0.30 × 0.50 = **0.15**

Upward target: q = 41 × e^0.15 = 41 × 1.16 = **47.64**
Call value at 47.64 with 90 days less remaining: approximately **8.10**
Percentage profit: (8.10 − 4.00) / 4.00 = **103%**

Downward target: q = 41 × e^(−0.15) = 41 × 0.86 = **35.39**
Call value at 35.39 with 90 days less remaining: approximately **1.10**
Percentage loss: (4.00 − 1.10) / 4.00 = **73%**

Reward/risk ratio: 103% / 73% = **1.41**

**Two output lists:**
- *Aggressive list* (ranked by percentage profit — Step 5): tends to surface ATM
  or slightly OTM calls.
- *Conservative list* (ranked by reward/risk ratio — Step 10): tends to surface
  ITM calls.

**Calibration note — the 0.7 standard deviation rule:** Using 1.0 standard deviation
as the upward assumption is probably excessive — there is only about a 16% probability
of a stock moving at least one full standard deviation over a fixed period. A more
realistic assumption is **0.7 standard deviations**, which has approximately a 25%
probability of occurring. For the conservative value investor, 0.7 standard deviations
is the correct default. It generates lower projected profits but produces more realistic
rankings across strategies.

> **Annotation:** This framework is the most rigorous call-buying tool in the playbook.
> Its key virtue is normalization: a 30% volatility stock and a 50% volatility stock are
> both evaluated on a move-of-X-standard-deviations basis, making comparisons fair
> across names with different characteristics. The reward/risk ratio directly serves the
> risk-defined mandate — it quantifies how much percentage upside is generated per
> unit of percentage downside, using model-derived prices at both extremes. The
> practical implementation: any option analytics platform that provides theoretical
> values at different stock prices and time horizons executes Steps 4 and 8 without
> manual Black-Scholes computation.

---

## 11. Put Pricing via the Arbitrage Formula

The Black-Scholes model prices calls directly. Put prices are derived from call prices
using the put-call parity relationship:

> **Theoretical put price = Theoretical call price + Strike price − Stock price
> − Carrying cost + Dividends**

Where:
- Theoretical call price = Black-Scholes output
- Carrying cost = risk-free interest rate × strike price × time to expiration
- Dividends = present value of dividends expected before option expiration

**Application to put ranking:** Put purchases can be ranked using the same 11-step
volatility-normalized framework from Section 10. The only modification: reward
opportunities occur when the stock falls in accordance with its volatility; risk is
measured by an upward stock move. Use the arbitrage formula above to price puts
at each stock price in Steps 4 and 8.

---

## 12. The Equivalent Stock Position (ESP): Net Delta Across a Combined Position

When stock and options are held simultaneously — as in a covered write, protective
put, collar, or LEAPS substitution — the net directional exposure of the entire position
collapses into a single number: the equivalent stock position.

> **ESP = Number of contracts × 100 shares per contract × Delta**

Long calls and long stock produce positive ESP (bullish). Long puts and short stock
produce negative ESP (bearish). A position with ESP near zero is approximately
delta-neutral.

**Complex position example:** XYZ at 31.75.

| Position | | Delta | ESP |
|---|---|---|---|
| Short | 4,500 XYZ stock | 1.00 | −4,500 shares |
| Short | 100 April 25 calls | 0.89 | −8,900 shares |
| Long | 50 April 30 calls | 0.76 | +3,800 shares |
| Long | 139 July 30 calls | 0.74 | +10,286 shares |
| **Total ESP** | | | **+686 shares** |

Despite the complexity of the position, it reduces to a single number: equivalent to
being long 686 shares of common stock. Essentially delta-neutral for a position of
this size.

> **Annotation:** For the playbook's core structures, ESP provides an immediate reality
> check on actual directional exposure. Long stock at delta 1.00 combined with a
> protective put at delta −0.30 produces a net ESP equivalent to 70 shares per 100
> owned: the position participates in 70% of upside moves and is partially insulated
> on the downside. As the stock declines and the put moves deeper ITM (delta rising
> toward −1.00), the ESP drops toward zero and eventually goes negative — the
> protection working as intended. Monitoring ESP as the position ages gives a live read
> on whether the hedge is still providing meaningful protection or has become so deep
> ITM that rolling the put to a higher strike makes sense.

---

## 13. Practical Monitoring Rules: Assignment Flags and Position Aging

Computer-aided monitoring of a multi-position options book should generate three
automatic flags:

1. **Early assignment risk:** Flag any short option whose remaining time value
   premium has dropped to 0.10 or less. At that level the option is trading near
   parity and early assignment is possible regardless of time remaining.

2. **Approaching expiration:** Flag any position with less than 1 month of life
   remaining in the options. These positions require active management — closing,
   rolling, or allowing expiration — and should not be left unmonitored.

3. **Ex-dividend proximity:** Flag any short call position where the underlying
   stock has an upcoming ex-dividend date within the life of the option. Call
   writers face assignment risk on the day prior to the ex-date when the call's
   time value premium has been reduced to near zero by the impending dividend.

These three flags replace the need to manually monitor every position daily. Any
position not triggering one of these flags can be reviewed on a less frequent schedule.

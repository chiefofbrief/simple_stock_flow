# Chapter 28 — Mathematical Applications:
# Extracted Insights for the Conservative Options Playbook

---

## 1. Implied Volatility: Letting the Market Compute Volatility For You

Historical volatility, computed from past stock prices, tells you what volatility *was*.
Implied volatility tells you what the market is *pricing in now*. For strategy decisions,
implied volatility is the more useful input.

"*There is, in fact, a way in which the strategist can let the market compute the volatility
for him.* This is called using the implied volatility; that is, the volatility that the market
itself is implying. This concept makes the assumption that, for options with striking prices
close to the current stock price and for options with relatively large trading volume, the
market is fairly priced... *If the actual price of an option is the fair price, it can be fixed
in the Black-Scholes equation while letting volatility be the unknown variable.*"

The implied volatility is derived by iterating the Black-Scholes equation backward: fix
the observed market price, solve for the volatility that produces it. Done for each option
on a stock, then weighted by volume and distance from the strike, a single composite
implied volatility for the underlying stock is produced.

**The weighting formula:**

The volume weight for each option is simply that option's daily volume divided by total
option volume on the stock. The distance weight uses a parabolic function that gives
decreasing weight as the option moves further from at-the-money, and zero weight beyond
a chosen maximum distance (e.g., 25% from current price):

Weighting factor = −(x − a)² / a² if x is less than a; = 0 if x is greater than a

where x is the percentage distance between stock price and strike, and a is the maximum
distance at which any weight is given.

**Example:** XYZ is at 33. Four options trade with the following data:

**TABLE 28-1. Implied volatilities, closing price, and volume.**

|Option|Option Price|Volume|Implied Volatility|
|---|---|---|---|
|January 30|4.50|50|.34|
|January 35|1.50|90|.28|
|April 35|2.50|55|.30|
|April 40|1.50|5|.38|

**TABLE 28-2. Volume weighting factors.**

|Option|Volume|Volume Weighting Factor|
|---|---|---|
|January 30|50|.25 (50/200)|
|January 35|90|.45 (90/200)|
|April 35|55|.275 (55/200)|
|April 40|5|.025 (5/200)|

With a = .25 (discarding options more than 25% from the stock price), the distance
weighting factors become:

**TABLE 28-3. Distance weighting factors.**

|Option|Distance from Stock Price|Distance Weighting Factor|
|---|---|---|
|January 30|.091 (3/33)|.41|
|January 35|.061 (2/33)|.57|
|April 35|.061 (2/33)|.57|
|April 40|.212 (7/33)|.02|

**TABLE 28-4. Option's implied volatility — final composite.**

|Option|Volume Factor|Distance Factor|Option's Implied Volatility|
|---|---|---|---|
|January 30|.25|.41|.34|
|January 35|.45|.57|.28|
|April 35|.275|.57|.30|
|April 40|.025|.02|.38|

Implied volatility = (.25×.41×.34 + .45×.57×.28 + .275×.57×.30 + .025×.02×.38) /
(.25×.41 + .45×.57 + .275×.57 + .025×.02) = **.298**

"Note that the implied volatility, .298, is not equal to any of the individual option's
implied volatilities. Rather, it is a composite figure that gives the most weight to the
heavily traded, near-the-money options, and very little weight to the lightly traded
(5 contracts), deeply out-of-the-money April 40 call."

**Smoothing day-to-day noise:** "A smoothing effect can be obtained by taking a moving
average of the last 20 or 30 days' implied volatilities. An alternative that does not require
the saving of many previous days' worth of data is to use a momentum calculation on the
implied volatility. For example, today's final volatility might be computed by adding 5%
of today's implied volatility to 95% of yesterday's final volatility."

**The key application:** "*Once this implied volatility has been computed, it can then be
used in the Black-Scholes model (or any other model) as the volatility variable.* Thus one
could compute the theoretical value of each option according to the Black-Scholes
formula, utilizing the implied volatility for the stock. Since the implied volatility for the
stock will most likely be somewhat different from the implied volatility of this particular
option, there will be a discrepancy between the option's actual closing price and the
theoretical price as computed by the model. This differential represents the amount by
which the option is theoretically overpriced or underpriced, *compared to other options
on that same stock.*"

"*This method of computing volatility is quite accurate and proves to be sensitive to
changes in the volatility of a stock.* For example, as markets become bullish or bearish
(generating large rallies or declines), most stocks will react in a volatile manner as well.
Option premiums expand rather quickly, and this method of implied volatility is able to
pick up the change quickly."

> **Annotation:** The composite implied volatility calculation is the foundation for the
> "buy cheap, sell expensive" volatility discipline referenced throughout Chapters 17 and
> 25. Two applications are directly relevant to the playbook. First, tracking a stock's
> composite implied volatility over time — maintaining a 20- or 30-day moving average —
> allows the investor to identify when implied volatility is historically low (the correct
> entry condition for buying LEAPS calls or protective puts) vs. historically elevated
> (when buying options is expensive and writing covered calls or selling puts is more
> attractive). Second, the overpriced/underpriced differential — comparing a specific
> option's implied volatility to the composite — identifies which strike or expiration is
> relatively cheap within a given stock's option chain. For the value investor building a
> LEAPS call or bull spread position, buying the option with the lowest individual implied
> volatility relative to the composite is strictly superior to buying the one that happens to
> look cheap on an absolute premium basis.

---

## 2. The Volatility Skew: Identifying Unusual Pricing Across Strikes

A volatility skew exists when different strikes or expirations on the same underlying stock
carry significantly different implied volatilities. Measuring the skew is a useful screening
tool.

The three-step process:
1. Calculate the individual implied volatility of each option.
2. Calculate the standard deviation of those implied volatilities (unweighted; exclude
   options with little or no time value premium as unrepresentative).
3. Divide that standard deviation by the composite implied volatility.

**Example:** XYZ is trading at 6.50 with four options:

|Option|Implied Volatility|
|---|---|
|Mar 5 call|85.0%|
|June 5 call|77.5%|
|Mar 7.5 call|75.0%|
|June 7.5 call|70.0%|

The standard deviation of these four numbers is 6.25. The composite implied volatility
(weighted by volume and distance) is 75.0%. Therefore:

Skew factor = 6.25 / 75.0 = **8.3%**

"Similar skew factors would be computed for all stocks, and then ranked. Those with the
highest skew factors are likely to have a distinct volatility skew. One would have to look
at the implied volatilities of the individual options on any particular stock with a large
skew factor to see what is causing the skew."

Two common skew patterns: A **horizontal skew** arises when options expiring just after
an anticipated event (earnings, FDA decision, lawsuit verdict) carry higher implied
volatility than all other options. A **vertical skew** arises in bearish markets, where
lower-strike options carry higher implied volatility than higher-strike options.

"Once the Composite Implied Volatility and the Volatility Skew Factor are computed, one
should consider keeping a database of daily values for every stock, index, ETF, and
futures contract. With this information, one would then be able to compute percentiles
of implied volatility and skew, looking back over time. These are useful statistics to help
one decide if a particular stock's options are indeed expensive or cheap, or if they are
unusually skewed."

> **Annotation:** The vertical skew — lower strikes carrying higher implied volatility than
> upper strikes — is the standard post-1987 skew pattern and is directly relevant to
> protective put buyers. When the skew is steep, OTM puts are expensive relative to
> ATM puts and the Chapter 17 rule (buy the first OTM strike) may require adjustment:
> in a steep skew environment, the ATM put may offer better value per dollar of protection
> than the OTM put does. The horizontal skew is relevant to the value investor who owns
> a stock heading into a known binary event: if the near-term implied volatility is
> dramatically elevated versus the longer-dated options, it may be worth selling a
> near-term covered call to harvest that elevated premium rather than buying protection
> through an expensive near-term put.

---

## 3. Computing the Probability of a Stock Being at a Given Price: The Core Formula

The lognormal distribution provides a straightforward formula for computing the
probability of a stock being below a given price at the end of a time period. This drives
both expected return calculations and downside protection analysis.

"The area under the distribution curve between any two points gives the probability of
being between those two points."

Note the critical scope limitation: "*These probabilities apply to the end of the time
period. They say nothing about the chances that XYZ might dip below price A at some
time during the time period.* To compute that percentage, an involved computation is
necessary."

The annual volatility must first be converted to the relevant time period:

v_t = v × √t

where v = annual volatility, t = time in years, v_t = volatility for time t.

As an example, a 3-month volatility equals one-half the annual volatility: t = .25, so
v_25 = v × √.25 = .50v.

The probability formula:

P(below q at end of period t) = N( ln(q/p) / v_t )

where N = cumulative normal distribution, p = current stock price, q = price in question,
ln = natural logarithm.

P(above q) = 1 − P(below q)

**Example applied to a covered write:** XYZ is selling for 43 and a 6-month July 40 call
is selling for 8 points. After including dividends and commission costs for a 500-share
position, the downside break-even point at expiration is 36. Annual volatility of XYZ is
25%. The 6-month volatility is 17.7% (25% times √½).

P(below 36 in 6 months) = N( ln(36/43) / .177 ) = N( −.178 / .177 ) = **0.158**

"The expected probability of XYZ being below 36 in 6 months is 15.8%. Therefore, this
would be an attractive write on a conservative basis, because it has a large probability of
making money (nearly 85% chance of not being below the break-even point at expiration)."

> **Annotation:** This formula converts the abstract concept of "downside protection" into
> a concrete, comparable probability. Two covered writes with different stocks, different
> premiums, and different break-even points can now be ranked on a common basis: which
> has the lower probability of loss at expiration? McMillan's suggested ranking criterion —
> among all writes that meet a minimum return threshold (e.g., 12% annualized), rank by
> lowest probability of being below break-even at expiration — is a superior filter to
> arbitrary rules like "the option must sell for at least 1 point" or "downside protection
> must be at least X%." Those rules cannot account for differences in stock volatility; the
> probability formula can. The same formula applies to evaluating protective puts: given a
> stock at price p and a put strike at q, P(below q) tells you the probability of the put
> expiring in-the-money. This is the probability-adjusted value of the protection being
> purchased.

---

## 4. Ranking Call Purchases: The Volatility-Normalized Reward/Risk Framework

"*Evaluating the profitability of calls based on the volatility of the underlying stock is the
correct way to analyze an option purchase.*"

The method ranks call purchases by how they would perform if the underlying stock
moved in accordance with its volatility over a fixed holding period. The complete
11-step procedure:

**Setup (Steps 1–2):** Specify the stock movement in terms of standard deviations (e.g.,
one standard deviation upward) and fix the holding period (30, 60, or 90 days).

**Profitability (Steps 3–6):**

Step 3 — Calculate the upward stock target using: q = p × e^(av_t)

where p = current stock price, a = number of standard deviations, v_t = volatility for
the holding period.

Step 4 — Use a pricing model (Black-Scholes) to price the call at the new stock price
and reduced time remaining.

Step 5 — Calculate percentage profit: (new option price − original price) / original price.

Step 6 — Repeat for each option on the stock.

**Risk (Steps 7–11):**

Step 7 — Calculate the downside stock target using: q = p × e^(−av_t)

Step 8 — Price the option after the stock's decline.

Step 9 — Calculate percentage loss: (original price − new option price) / original price.

Step 10 — Reward/risk ratio = percentage profit / percentage loss.

Step 11 — Repeat for all options.

**Complete example:** Steps 1–2: 90-day holding period, one standard deviation movement.

XYZ common: 41; XYZ volatility: 30% annually; XYZ January 40 call: 4;
time to January expiration: 6 months.

Step 3 — Upward target:
v_t = .30 × √.25 = .30 × .50 = .15
q = 41 × e^.15 = 41 × 1.16 = **47.64**

Step 4 — Using Black-Scholes, the XYZ January 40 call is worth approximately **8.10**
if XYZ is at 47.60 with 90 days less life remaining.

Step 5 — Percent profit = (8.10 − 4) / 4 = 4.10 / 4 = **103%**

"Recall again that there is only about a 16% chance of the stock actually moving at least
this far. If all options on all stocks are ranked under this same assumption, however, a
fair comparison of profitable options will be obtained."

Step 7 — Downside target:
q = 41 × e^(−.15) = 41 × .86 = **35.39**

"Note that the actual distances that XYZ could rise and fall are not the same. The upward
potential was 6.60 points, while the downward potential is about 5.75 points. This
difference is due to the use of the lognormal distribution."

Step 8 — The XYZ January 40 call would be worth approximately **1.10** if XYZ were
at 35.39 in 90 days.

Step 9 — Percent risk = (4 − 1.10) / 4 = 2.90 / 4 = **73%**

Step 10 — Reward/risk ratio = 103% / 73% = **1.41**

Step 11 — Repeat for all XYZ options and all other optionable stocks.

"The higher profitability list of option purchases will tend to be at- or slightly
out-of-the-money calls. The less aggressive list, ranked by reward/risk potential, will tend
to be in-the-money options."

**A calibration note on the standard deviation assumption:** "The assumption of ranking
the purchases after one full standard deviation movement by the underlying stock is
probably excessive. A more moderate assumption would be that the stock might be able
to move .7 standard deviation. There is about a 25% expected chance that a stock could
move up at least .7 standard deviation at the end of a fixed time period."

> **Annotation:** This framework is the most rigorous call-buying tool in the playbook.
> Its key virtue is that it normalizes across stocks with different volatilities: a 30%
> volatility stock and a 50% volatility stock both get evaluated on a move-of-X-standard-
> deviations basis, making the comparison fair. The reward/risk ratio (Step 10) directly
> serves the playbook's risk-defined mandate — it explicitly quantifies how much
> percentage upside is generated per unit of percentage downside risk, using actual model-
> derived prices at both extremes. McMillan's calibration note is important: using 1.0
> standard deviations as the upward assumption is aggressive (only 16% probability of
> occurring); using 0.7 standard deviations is more realistic (25% probability). For the
> conservative value investor, 0.7 standard deviations is the appropriate assumption —
> it generates lower projected profits but more realistic rankings. The practical
> implementation: use any option analytics platform that provides theoretical values at
> different stock prices to execute Steps 4 and 8 without manual Black-Scholes
> computation.

---

## 5. The Equivalent Stock Position (ESP): Reading Net Delta Exposure Across a Combined Position

When stock and options are held simultaneously — as in a covered write, protective put,
or LEAPS stock substitute — the net directional exposure of the entire position can be
collapsed into a single number: the equivalent stock position.

"If one owns 10 calls that have a delta of .45, his equivalent stock position from those
calls is 10 × 100 shares per call × .45 = 450. That is, owning those 10 calls is equivalent
to owning 450 shares of the underlying stock, according to the delta. All puts and calls
can be reduced to an ESP and can then, of course, be combined with any actual long or
short stock in the position to produce an ESP for the entire strategy."

The sign convention: long calls and long stock produce positive ESP (bullish); long puts
and short stock produce negative ESP (bearish). A position with ESP near zero is
delta-neutral.

**Example of a complex position with XYZ at 31.75:**

|Position||Delta|ESP|
|---|---|---|---|
|Short|4,500 XYZ|1.00|Short 4,500 shares|
|Short|100 XYZ April 25 calls|0.89|Short 8,900 shares|
|Long|50 XYZ April 30 calls|0.76|Long 3,800 shares|
|Long|139 XYZ July 30 calls|0.74|Long 10,286 shares|
|**Total ESP**|||**Long 686 shares**|

"The advantage of using the ESP is that this fairly complex position is reduced to a single
number. The entire position is equivalent to being long 686 shares of the common stock.
Essentially, this is close to delta-neutral for such a large position."

> **Annotation:** For the playbook's core structures — long stock plus protective put, or
> LEAPS call plus Treasury bill — the ESP calculation provides an immediate reality check
> on actual directional exposure. A long stock position at delta 1.00 combined with a
> protective put at delta −0.30 produces a net ESP equivalent to 70 shares per 100 owned:
> the position participates in 70% of upside moves and is partially insulated on the
> downside. As the stock declines and the put moves further in-the-money (delta rising
> toward −1.00), the ESP drops toward zero and eventually goes negative, which is the
> protection working as intended. Monitoring ESP over time as the position ages gives
> the investor a live read on whether the hedge is still providing meaningful protection or
> has become so deep in-the-money that rolling the put to a higher strike makes sense.

# USER NOTES:

- The actual formula is....need photo from page 2. The variables are: p = stock price s = striking price t = time remaining until expiration, expressed as a percent of a year r = current risk-free interest rate V = volatility measured by annual standard deviation ln = natural logarithm N(x) = cumulative normal density function 
- An important by-product of the model is the exact calculation of the delta—that is, the amount by which the option price can be expected to change for a small change in the stock price. The delta was described in Chapter 3 on call buying, and is more formally known as the hedge ratio. Delta = N(d;)
- The cumulative normal distribution function can be found in tabular form in most statistical books. However, for computation purposes, it would be wasteful to repeatedly look up values in a table. Since the normal curve is a smooth curve (it is the “bell-shaped” curve used most commonly to describe population distributions), the cumulative distribution can be approximated by a formula:...Need photo from page 2.
- Several aspects of this model are worth further discussion. First, the reader will notice that the model does not include dividends paid by the common stock. As has been demonstrated, dividends act as a negative effect on call prices. Thus, direct application of the model will tend to give inflated call prices, especially on stocks that pay relatively large dividends. There are ways of handling this. Fisher Black, one of the coauthors of the model, suggested the following method: Adjust the stock price to be used in the formula by subtracting, from the current stock price, the present worth of the dividends likely to be paid before maturity. Then calculate the option price. Second, assume that the option expires just prior to the last exdividend date preceding actual option expiration. Again adjust the stock price and calculate the option price. Use the higher of the two option prices calculated as the theoretical price....It should be pointed out that, in many of the applications that are going to be prescribed, it is not necessary to know the exact theoretical price of the call. Therefore, the dividend “correction” might not have to be applied for certain strategy decisions.
- The computation of volatility is always a difficult problem for mathematical application. In the Black-Scholes model, volatility is defined as the annual standard deviation of the stock price. This is the regular statistical definition of standard deviation:....Need photo from page 5
- When volatility is computed using past stock prices, it is called a historical volatility. The volatilities of stocks tend to change over time. Certain predictable factors, such as a large stock split increasing the float of the stock, can reduce the volatility. The entry of a company into a more speculative area of business may increase the volatility. Other, less well-defined factors can alter the volatility as well. Since the volatility is a very crucial element of the pricing model, it is important that the modeler use a reasonable estimate of the current volatility. It has become apparent that an annual standard deviation is not accurate, because it encompasses too long a period of time. Recent efforts by many modelers have suggested that one should perhaps weight the recent stock price action more heavily than older price action in arriving at a current volatility.
- The above calculation does not give the proper input for the Black-Scholes model because the model assumes that the logarithms of changes in price are normally distributed, not the prices themselves. That is, the term P, in the above formula should be changed. Example: XYZ closed at 51 today and at 50 yesterday. Thus, its percentage change for the day is 51/50 = 1.02. The natural logarithm of 1.02 is then based on the volatility formula: In (514) = In(1.02) = 0.0198 This is similar to saying that arithmetically the stock was up 2% today, but on a lognormal basis, it was only up 1.98%.
- A new equation can now be formulated using this concept. It will yield volatilities that are consistent with the Black-Scholes model:...page 6
- There is, in fact, a way in which the strategist can let the market compute the volatility for him. This is called using the implied volatility; that is, the volatility that the market itself is implying. This concept makes the assumption that, for options with striking prices close to the current stock price and for options with relatively large trading volume, the market is fairly priced. This is something like an efficient market hypothesis. If there is enough trading interest in an option that is close to the money, that option will generally be fairly priced. Once this assumption has been made, a corollary arises: If the actual price of an option is the fair price, it can be fixed in the Black-Scholes equation while letting volatility be the unknown variable. The volatility can be determined by iteration. In fact, this process of iterating to compute the volatility can be done for each option on a particular underlying stock. This might result in several different volatilities for the stock. If one weights these various results by volume of trading and by distance in- or out-of-the-money, a single volatility can be derived for the underlying stock. This volatility is based on the closing price of all the options on the underlying stock for that given day.
- Example: XYZ is at 33 and the closing prices are given in Table 28-1. Each option has a different implied volatility, as computed by determining what volatility in the Black— Scholes model would result in the closing price for each option: That is, if .34 were used as the volatility, the model would give 4% as the price of the January 30 call. In order to rationally combine these volatilities, weighting factors must be applied before a volatility for XYZ stock itself can be arrived at. The weighting factors for volume are easy to compute. The factor for each option is merely that option’s daily volume divided by the total option volume on all XYZ options (Table 28-2). The weighting functions for distance from the striking price should probably not be linear. For example, if one option is 2 points out-of-the-money and another is 4 points out-of-the-money, the former option should not necessarily get twice as much weight as the latter. Once an option is too far in- or out-of-the-money, it should not be given much or any weight at all, regardless of its trading volume. Any parabolic function of the following form should suffice:...need photo from page 8. where x is the percentage distance between stock price and strike price and a is the maximum percentage distance at which the modeler wants to give any weight at all to the option’s implied volatility.
- Example: An investor decides that he wants to discard options from the weighting criterion that have striking prices more than 25% from the current stock price. The variable, a, would then be equal to .25. The weighting factors, with XYZ at 33, could thus be computed as shown in Table 28-3. To combine the weighting factors for both volume and distance from strike, the two factors are multiplied by the implied volatility for that option. These products are summed up for all the options in question. This sum is then divided by the products of the weighting factors, summed over all the options in question. As a formula, this would read:...Page 9...In our example, this would give an implied volatility for XYZ stock of 29.8% (Table 28-4). Note that the implied volatility, .298, is not equal to any of the individual option’s implied volatilities. Rather, it is a composite figure that gives the most weight to the heavily traded, near-the-money options, and very little weight to the lightly traded (5 contracts), deeply out-of-the-money April 40 call. This implied volatility is still a form of standard deviation, and can thus be used whenever a standard deviation volatility is called for. This method of computing volatility is quite accurate and proves to be sensitive to changes in the volatility of a stock. For example, as markets become bullish or bearish (generating large rallies or declines), most stocks will react in a volatile manner as well. Option premiums expand rather quickly, and this method of implied volatility is able to pick up the change quickly. One last bit of fine-tuning needs to be done before the final volatility of the stock is arrived at. On a day-to-day basis, the implied volatility for a stock—especially one whose options are not too active—may fluctuate more than the strategist would like. A smoothing effect can be obtained by taking a moving average of the last 20 or 30 days’ implied volatilities. An alternative that does not require the saving of many previous days’ worth of data is to use a momentum calculation on the implied volatility. For example, today’s final volatility might be computed by adding 5% of today’s implied volatility to 95% of yesterday's final volatility. This method requires saving only one previous piece of data—yesterday’s final volatility—and still preserves a “smoothing” effect. Once this implied volatility has been computed, it can then be used in the BlackScholes model (or any other model) as the volatility variable. Thus one could compute the theoretical value of each option according to the Black-Scholes formula, utilizing the implied volatility for the stock. Since the implied volatility for the stock will most likely be somewhat different from the implied volatility of this particular option, there will be a discrepancy between the option’s actual closing price and the theoretical price as computed by the model. This differential represents the amount by which the option is theoretically overpriced or underpriced, compared to other options on that same stock.
- Computing a Volatility Skew There is not a single, definitive way to calculate a single number for each stock each day that represents the skew in the options, but this is one acceptable way. Essentially, the process is this: Calculate the individual implied volatility of each option. 2. Calculate the standard deviation of the series in step 1. It is not necessary to weight these individual implied volatilities as one does in the composite implied volatility calculation. Rather, merely compute the standard deviation of the set of implied volatilities. Also, note that one may want to eliminate options that are essentially trading with little or no time value premium from this standard deviation calculation, since they are not representative of the “normal” options on this stock. 3. Divide the result of step 2 by the composite implied volatility, computed as shown in the preceding section. Example: XYZ is trading at 6.50. It has several listed options, with various individual implied volatilities. Option Implied Volatility Mar 5 call 85.0% June 5 call 77.5% Mar 7.5 call 75.0% June 7.5 call 70.0% The standard deviation of these four numbers is 6.25. Note that this number does not take into account the price or the volume of the individual options. However, deeply in- or out-of-the-money options would not be included if their time value premium is extremely small. Furthermore, assuming that the composite implied volatility of the above four options (which does use volume and distance in- or out-of-the-money), is 75.0%, the “skew factor” for this stock on this day would be: Skew factor = 6.25 / 75.0 = 8.3% Similar skew factors would be computed for all stocks, and then ranked. Those with the highest skew factors are likely to have a distinct volatility skew.
- Once the Composite Implied Volatility and the Volatility Skew Factor are computed, one should consider keeping a database of daily values for every stock, index, ETF, and futures contract. With this information, one would then be able to compute percentiles of implied volatility and skew, looking back over time. These are useful statistics to help one decide if a particular stock’s options are indeed expensive or cheap, or if they are unusually skewed.
- Since options have fixed terms, they lend themselves to a more rigorous computation of expected profit than the aforementioned intuitive appraisal. This more rigorous approach consists of computing the expected return. The expected return is nothing more than the return that the position should yield over a large number of cases. A simple example may help to explain the concept. The crucial variable in computing expected return is to outline what the chances are of the stock being at a certain price at some future time. 
- Example: XYZ is selling at 33, and an investor is interested in determining where XYZ will be in 6 months. Assume that there is a 20% chance of XYZ being below 30 in 6 months, and that there is a 40% chance that XYZ will be above 35 in 6 months. Finally, assume that XYZ has an equal 10% chance of being at 31, 32, 33, or 34 in 6 months. All other prices are ignored for simplification. Table 28-5 summarizes these assumptions. Since the percentages total 100%, all the outcomes have theoretically been allowed for. Now suppose a February 30 call is trading at 4 and a February 35 call is trading at 2 points. A bull spread could be established by buying the February 30 and selling the February 35. This position would cost 2 points—that is, it is a 2-point debit. The spreader could make 3 points if XYZ were above 35 at expiration for a return of 150%, or he could lose 100% if XYZ were below 30 at expiration. The expected return for this spread can be computed by multiplying the outcome at expiration for each price by the probability of being at that price, and then summing the results. For example, if XYZ is below 30 at expiration, the spreader loses $200. It was assumed that there is a 20% chance of XYZ being below 30 at expiration, so the expected loss is 20% times $200, or $40. Table 28-6 shows the computation of the expected results at all the prices. The total expected profit is $100. This means that the expected return (profit divided by investment) is 50% ($100/$200).
- Fortunately, there is a straightforward method of computing the expected percentage chance of a given stock being at a certain price at a certain point in time. This computation involves using the distribution of stock prices.
- Figure 28-1 is a graph of a typical lognormal distribution. The peak always lies at the “mean,” or average, of the distribution. For stock price distributions, under the random walk assumption, the “mean” is generally considered to be the current stock price.
- The reader should take note of the fact that these probabilities apply to the end of the time period. They say nothing about the chances that XYZ might dip below price A at some time during the time period. To compute that percentage, an involved computation is necessary.
- Since the option modeler is generally interested in time periods other than one year, the annual volatility must be converted into a volatility for the time period in question. This is easily accomplished by the following formula: ....Page 15
- 

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

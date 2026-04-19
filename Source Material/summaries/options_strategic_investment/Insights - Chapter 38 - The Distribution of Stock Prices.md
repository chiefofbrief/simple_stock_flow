# Chapter 38 — The Distribution of Stock Prices: Extracted Insights for the Conservative Options Playbook

---

## 1. The Core Finding: Stocks Move Far More Than the Lognormal Distribution Predicts

"Much of the work that has been done in statistics and related areas regarding the stock
market has made the assumption that stock prices are distributed normally, or more
specifically, *lognormally.* In actual practice, this is usually an incorrect assumption."

The lognormal distribution "says" that stocks remain within 3 standard deviations of
their current price 99.74% of the time, and that the probability of a 3-standard deviation
move is 0.0013 — roughly 3 stocks out of 2,500 on any given day. The probability of an
8-standard deviation move under the lognormal distribution is 0.000000000000000629:
"This number is so small that one would expect to see only one such occurrence in the
known life of the universe."

In practice: "one can find several such moves on nearly any trading day."

**Table 38-1. Sample large moves on one day (April 5, 1999 — Dow up 174 points):**

| Stock | Last Sale | Change | Standard Deviations |
|---|---|---|---|
| Aspect Devt (ASDV) | 8 | −14.38 | −31.2 |
| Axent (ANT) | 8 | −12 | −11.2 |
| Ameritrade (AMTD) | 91.63 | +29.13 | +8.6 |
| CheckPoint (CHKP) | 28.75 | −10.75 | −8.4 |
| Sabre Gp. (TSG) | 55 | +8.50 | +8.0 |

"All in all, 58 stocks had moves of greater than *four* standard deviations on that day!"

As a control, the lowest-volatility period since VIX inception was tested: July 25,
1993. "On that day, *twelve* stocks had moves of more than four standard deviations.
They included some big names, like Adaptec (ADPT), Bethlehem Steel (BS), U.S. Steel
(X), Chiquita Brands (CQB), and Novell (NOVL)."

**Three 30-day studies of 2,500–2,900 optionable stocks:**

**Table 38-2. October 22 – December 7, 1999 (VIX at 23, moderate volatility):**

| | 3σ | 4σ | 5σ | >6σ | Total |
|---|---|---|---|---|---|
| Upside Moves | 309 | 116 | 44 | 47 | 516 |
| Downside Moves | 69 | 29 | 15 | 19 | 132 |
| Total stocks moving ≥3σ: 648 (22% of the stocks studied) | | | | | |

**Table 38-3. June 1 – July 18, 1999 (quieter period):**

| | 3σ | 4σ | 5σ | >6σ | Total |
|---|---|---|---|---|---|
| Upside Moves | 104 | 28 | 13 | 12 | 157 |
| Downside Moves | 54 | 19 | 7 | 14 | 94 |
| Total stocks moving ≥3σ: 251 (10% of the stocks studied) | | | | | |

**Table 38-4. July 1 – August 17, 1993 (least volatile period in the database):**

| | 3σ | 4σ | 5σ | >6σ | Total |
|---|---|---|---|---|---|
| Upside Moves | 14 | 5 | 1 | 1 | 21 |
| Downside Moves | 28 | 5 | 3 | 4 | 40 |
| Total stocks moving ≥3σ: 61 (10% of the stocks studied) | | | | | |

"Once again, this means that there is a far greater chance for large standard deviation
moves—about one in ten—than the nearly zero percent chance that the lognormal
distribution would indicate."

The methodology is robust against the objection that volatile periods skew the
results: "The *current* 20-day historical volatility was used on each day of the study in
order to determine how many standard deviations each stock moved. So, in 1999 and
2000, that historical volatility was a high number and it therefore means that the stock
would have had to move a very long way to move four standard deviations. In 1993,
however, when the market was in the doldrums, historical volatility was low, and so a
much smaller move was needed to register a 4-standard deviation move."

> **Annotation:** The 10% baseline — one in ten stocks making a 3σ+ move in any
> 30-day period, even in the calmest market environment in the database — is the
> foundational number to internalize. The option market prices calls using the lognormal
> distribution, which assigns near-zero probability to these moves. The call buyer at low
> IV is therefore systematically undercharged for the actual distribution of outcomes.

---

## 2. Fat Tails: The Quantified Gap Between Theory and Reality

The large-scale study covered over 2.5 million individual stock trading days, September
1993 to April 2000. At the extremes — moves of ±4.0 standard deviations or more — the
gap between the actual and theoretical distribution is not marginal:

**Downside fat tail:** "the 'normal' distribution expects fewer than 200 moves out of 2.5
million to be of −4.0 standard deviations or more… On the other hand, actual stock
prices… fell more than −4.0 standard deviations nearly 2,500 times out of 2.5 million.
Thus, in reality, there was really more than **12 times the chance** (2,500 vs. 200) that
stocks could suffer a severely dramatic fall, when comparing actual to theoretical
distribution."

**Upside fat tail:** "At the extreme—moves of +4.0 standard deviations or more—there
were about 2,000 such moves in actual stock prices, compared with fewer than 100
expected by the normal distribution. Again, a very large discrepancy: **twenty-to-one.**"

The inflection points: "the normal distribution is higher (i.e., is expected to occur
more often than it actually does) between −2.5 standard deviations and +0.5 standard
deviations. Outside of that range, the actual distribution is more frequent than it was
expected to be."

**The mini-crash of April 14, 2000** (Dow −617, S&P −83, NASDAQ-100 −346): "the
leftmost data point—representing all moves of −4.0 standard deviations and lower,
shows that about **750 out of the 2,984 stocks** had moves of that size! That is
unbelievable, and it really points out just how dangerous naked puts and long stock on
margin can be on days like this. No probability calculator is going to give much likelihood
to a day like this occurring, but it did occur and it **benefited those holding long puts
greatly**, while it seriously hurt others."

> **Annotation:** The 12-to-1 and 20-to-1 ratios at the tails mean that any probability
> analysis used to price an option is systematically underweighting large moves. For the
> call buyer, this is a structural tailwind: premiums reflect the lognormal world, while
> the actual world delivers large moves far more frequently. For the put buyer held as
> downside protection, the 750-out-of-2,984 stocks on a single crash day is a concrete
> illustration of what that protection actually delivers in a real crisis.

---

## 3. The Volatility Buyer's Rule: Large Moves Are Rapid and Often Include Gaps

"The point of the previous discussion is that stocks move a lot farther than you might
expect. Moreover, when they make these moves, it tends to be with rapidity, generally
including gap moves."

What this means for option selling strategies:

"For example, covered call writing is considered to be 'conservative.' However, when
the stock has the potential to make these big moves, it will either cause one to give up
large upside profits or to suffer large downside losses. (Covered call writing has limited
profit potential and relatively large downside risk, as does its equivalent strategy, naked
put selling.) When these large stock moves occur on the upside, a covered writer is often
disappointed that he gave up too much of the upside profit potential. Conversely, if the
stock drops quickly, and one is assigned on his naked put, he often no longer has much
appetite for acquiring the stock (even though he said he 'wouldn't mind' doing so when
he sold the puts to begin with)."

"Even spreading has problems along these lines. For example, a vertical spread limits
profits so that one can't participate in these relatively frequent large stock moves when
they occur."

For option sellers who persist: "he must carefully analyze his position and allow for
much larger stock movements than one would expect under the lognormal distribution.
Also, he must be careful to sell options only when they are expensive in terms of implied
volatility, so that any decrease in implied will work in his favor. Probably most judicious,
though, is that an option seller should really concentrate on indices (or perhaps certain
futures contracts), because they are statistically much less volatile than stocks."

> **Annotation:** The covered call point is directly relevant to a value investor who
> might consider writing calls against a long stock position to "reduce cost basis."
> McMillan's data makes the case that this trade is structurally unattractive precisely
> when it matters most: when the thesis plays out with a large, rapid upside move, the
> covered writer is capped out of the very outcome their research identified. The investor
> who has done the fundamental work to find an undervalued stock with a catalyst should
> not sell that catalyst away.

---

## 4. Fat Tails Vindicate Option Buying — The Expected Return Conclusions

"The most obvious thing that an option trader can learn from these distributions and
studies is that buying options is probably a lot more feasible than conventional wisdom
would have you believe. The old thinking that selling an option is 'best' because it wastes
away every day is false. In reality, when you have sold an option, you are exposed to
adverse price movements and adverse movements in implied volatility all during the life
of the option. The likelihood of those occurring is great, and they generally have more
influence on the price of the option in the short run than does time decay."

From expected return studies using the fat tail Monte Carlo simulation, McMillan
draws three conclusions:

"A bull spread is an inferior strategy when the options are fairly priced, no matter
which distribution is assumed. This more or less agrees with observations that have been
made previously regarding the disappointments that traders often encounter when using
vertical spreads."

"While covered writing might seem superior to stock ownership under the lognormal
distribution, the two are about equal under a fat tail distribution."

"Most startling, though, is the fact that **option buying strategies fare much, much
better under a fat tail distribution than a lognormal one.** This most clearly demonstrates
the 'power' of the fat tail distribution: A limited-risk investment with unlimited profit
potential can be expected to perform very well if the fat tails are allowed for."

"Using the lognormal distribution more or less represents the conventional wisdom
regarding option strategies—the one that many brokers promote: 'Don't buy options,
don't mess with spreads, either buy stocks or do covered call writes.' The fat tail
distribution column stands much of that advice on its head. In real life (as demonstrated
by the fat tail distribution), strategies with limited profit potential and unlimited or large
risk potential are inferior strategies."

> **Annotation:** This is the most strategically important passage in the chapter and the
> empirical foundation for this entire playbook. The conventional case against buying
> options is built on a distribution model that understates the probability of large moves
> by 12 to 20 times at the tails. When the correct distribution is used, three things follow
> simultaneously: bull spreads are confirmed as inferior (consistent with Chapter 37's
> vega analysis), covered writing loses its apparent edge over owning stock outright, and
> outright option buying with limited risk is the strategy that benefits most from the way
> stocks actually behave. The three conclusions together close the argument that this
> playbook has been building across the preceding chapters.

---

## 5. Out-of-the-Money Options Are Probably Underpriced — With an Important Qualification

"Does this mean that most options are underpriced, since traders and market-makers
are using the Black-Scholes model (or similar models) to price them? Without getting
too technical, the answer is that yes, some options—particularly **out-of-the-money
options**—are probably underpriced. However, one must understand that it is still a
relatively rare occurrence to experience one of these big moves—it's just not as rare as
the lognormal distribution would indicate. So, an out-of-the-money option might be
*slightly* underpriced, but often not enough to make any real difference."

The counterexample: "In fact, *futures* options in grains, gold, oil, and other markets
that often experience large and sudden rallies display a distinct volatility skew. That is,
out-of-the-money *call* options trade at significantly higher implied volatilities than do
at-the-money options. Ironically, there is far less chance of one of these
hyper-standard-deviation moves occurring in commodities than there is in stocks, at
least if history is a guide. So, the fact that some out-of-the-money futures options are
expensive is probably an incorrect overadjustment for the possibility of large moves."

> **Annotation:** The qualification — "slightly underpriced, but often not enough to
> make any real difference" — matters for strike selection. Buying deeply
> out-of-the-money calls solely because they are theoretically underpriced relative to
> fat-tail reality is not a sufficient strategy. The stronger case for option buying rests on
> the combination of low IV entry, a specific fundamental thesis with a catalyst, and the
> fat-tail distribution providing more upside probability than the market prices in. Fat
> tails are a structural tailwind for the prepared buyer, not a standalone rationale for
> buying cheap out-of-the-money lottery tickets.

---

## 6. How to Use a Volatility Estimate Conservatively When Evaluating a Position

All probability calculators require a volatility input. McMillan's rule for selecting it:

"There is no certain way to mitigate these volatility 'problems' as far as the probability
calculator is concerned, but one helpful technique is to **bias the volatility projection
*against* your objectives.** That is, be overly conservative in your volatility projections.
If things turn out to be better than you estimated, fine. However, at least you won't be
overstating things initially."

**For option buyers:** Use the *lowest* of the available historical volatility measures.
"By doing so, he is taking a conservative approach. If the straddle buy looks good under
this conservative assumption, then he can feel fairly certain that he has not overstated
the possibilities of success. If it turns out that volatility is *higher* during the life of the
position, that will be an added benefit."

**Worked example — option buyer:**

A five-month straddle on XYZ, stock at 40, straddle cost 8, break-even points 48 and
32. Historical volatility stack:

| Period | Historical Volatility |
|---|---|
| 10-day | 22% |
| 20-day | 20% |
| 50-day | 28% |
| 100-day | 33% |

"Since one is buying options in this strategy, he should use the *lowest* of the above
historical volatility measures as his volatility estimate… he should use the 20-day
historical volatility *because it is the lowest of the four choices that he has.*"

**For option sellers:** "he should use the *highest* historical volatility when making his
probability projections. By so doing, he is again being conservative. If the strategy in
question still looks good, even under an assumption of high volatility, then he can figure
that he won't be unpleasantly surprised by a higher volatility during the life of the
position."

> **Annotation:** The "bias against your objectives" rule is a practical pre-trade filter.
> For the value investor evaluating a call purchase on a quiet, low-IV stock, the rule says:
> use the *lowest* reading in the historical volatility stack as the input to any probability
> calculation. If the trade looks attractive even under that pessimistic assumption, the
> position has a genuine margin of safety. Any IV expansion that materializes on top of
> that conservative base is purely incremental benefit. This is the options analogue of
> using conservative assumptions in a DCF.

---

## 7. When the Standard Stack Is Insufficient: The Long-Lookback Median Method

When a stock has been behaving erratically for longer than 100 days — such that the
entire 100-day historical volatility is contaminated by recent unusual behavior — a
longer-lookback median approach is needed.

"Go back in a historical database of prices for the underlying and compute the 20-day,
50-day, and 100-day historical volatilities for *all* the time periods in the database, or at
least during a fairly large segment of the past prices. Then use the *median* of those
calculations for your volatility estimates."

**Worked example:**

XYZ has been chaotic for months. Current readings:

| Period | Historical Volatility |
|---|---|
| 20-day | 130% |
| 50-day | 100% |
| 100-day | 80% |

Trader looks back over the last 1,000 trading days and computes a distribution of
100-day historical volatilities:

| Percentile | 100-Day Historical |
|---|---|
| 0th | 34% |
| 10th | 37% |
| 20th | 43% |
| 30th | 45% |
| 40th | 46% |
| 50th | 48% |
| 60th | 51% |
| 70th | 58% |
| 80th | 67% |
| 90th | 75% |
| 100th | 81% |

"The *median* of the above figures is 48%—the 100-day volatility at the 50th percentile."

After computing similar analyses across all lookback periods using 1,000 days, the
trader finds:

| Period | Median Historical Volatility |
|---|---|
| 100-day | 48% |
| 50-day | 49% |
| 20-day | 52% |
| 10-day | 49% |

"If these were all the data that one had, then he would probably use a volatility
estimate of 48% or so in his option models or probability calculators. Of course, this is
starkly different from the current levels of historical volatility."

"There is nothing magical about using 1,000 trading days. Perhaps something like 600
trading days would be better. The idea is to use enough trading days to bring in some
historic data to counterbalance the recent, erratic behavior of the stock."

"Among other things, this example also shows that volatilities are unstable, no matter
how much work and mathematics one puts into calculating them. Therefore, they are at
best a fragile estimate of what might happen in the future."

> **Annotation:** This method is particularly useful for the value investor targeting
> beaten-down, high-volatility situations where recent price behavior reflects distress
> rather than permanent character. When a stock has been in freefall — earnings
> implosion, sector crisis, accounting restatement — the current 100-day HV will be
> inflated by the episode, overstating the stock's true long-term volatility. The median
> lookback gives a more realistic baseline for two questions: Is current IV genuinely high
> relative to long-term norms? And what is a realistic expectation for movement over the
> life of the position once the distress normalizes? If current IV is at the 90th percentile
> of a 1,000-day distribution with a median of 48%, that is an expensive entry. If current
> IV is near the 20th percentile because the stock has been quiet for a prolonged period,
> that is the entry condition the playbook targets.

---

## 8. Delta as a Quick Probability Estimate — and Its Limitations

"The delta of an option is actually a fairly good estimate of the probability of the option
being in-the-money at its expiration date… the delta is a quick and dirty way of
estimating the probability of the stock being above the strike price (in the case of call
options) or below the strike price (in the case of put options) at expiration."

The limitation: delta estimates the probability of being in-the-money *at expiration*,
not the probability of the option *ever* being in-the-money during its life. The "ever"
probability is materially higher.

**Worked example illustrating the gap:**

OEX at 600, naked puts sold at strike 550, 30 days to expiration, volatility 25%:

| Scenario | Actual Probability |
|---|---|
| 1. OEX never falls below 550 | 67% |
| 2. OEX falls below 550 and remains there | 19% |
| 3. OEX falls below 550 but rallies back above it | 14% |

Simple endpoint calculator (the delta approximation) would show only:

| | |
|---|---|
| Probability of OEX above 550 at expiration | 81% |
| Probability of OEX below 550 at expiration | 19% |

"So, with the simple calculator, it looks like there's an 81% chance of a worry-free
trade. Just sit back and relax and let the option expire worthless. However, in real
life… there's only a **67% chance** of a worry-free trade. The difference—the other
14%—is the probability of the third scenario occurring (OEX falls below 550, but rallies
back above it by expiration). The simple probability calculator doesn't account for that
scenario at all."

For the fat-tail distribution, the gap between endpoint and "ever" probabilities is
even wider:

| Calculator | Probability XYZ ever trades < 60 |
|---|---|
| Simple endpoint | 10% |
| "Ever" calculator (lognormal) | 20% |
| "Ever" calculator (fat tail) | 22% |

"If the true probability that the put will need attention is 22%, then he might *not*
take the trade. Many naked option sellers try to sell options that have only probabilities
of 15% or less of potentially becoming troublesome. Hence, the choice of which
probability calculation he uses can make a difference in whether or not a trade is
established."

> **Annotation:** For the call buyer, the delta-as-probability shorthand is useful but
> conservative in a favorable direction: delta understates the probability of the call ever
> reaching the strike during the option's life. A 30-delta call has roughly a 30% chance
> of expiring in-the-money, but a meaningfully higher chance of trading in-the-money
> at some point before expiration — which is the relevant scenario for an investor who
> intends to sell the option before expiry. The fat-tail distribution widens this gap
> further. Treating delta as a floor estimate of eventual profitability probability, rather
> than the full picture, is the correct conservative interpretation.

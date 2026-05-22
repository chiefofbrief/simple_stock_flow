# Chapter 38: The Distribution of Stock Prices —
# Extracted Insights for the Conservative Options Playbook

---

## Foundational Observation: Almost All Estimates of Stock Price Movement
## Are Overly Conservative

Before any data is presented, McMillan states this directly: almost all estimates of
stock price movement are overly conservative. The statistical models used to price
options assume a distribution that systematically understates how far stocks actually
move. The consequence for the option trader is that certain strategies — particularly
option buying — are more favorable than conventional wisdom suggests, and certain
strategies — particularly option selling against individual stocks — are more dangerous.

---

## 1. Why the Lognormal Distribution Is Used — and Why It Fails

The lognormal distribution is used to describe stock prices because its shape is
intuitively similar to how stocks behave:
- Stocks cannot fall below zero.
- Stocks can rise to infinity.
- Most of the time, stocks don't move much in any direction.
- The distribution's shape is based on the historical volatility of the underlying.

In a lognormal (or normal) distribution, outcomes remain within 3 standard deviations
99.74% of the time. The probability of a 3-standard deviation move is 0.0013 —
approximately one tenth of one percent.

**The concrete daily implication:** With 2,500 optionable stocks, the lognormal model
predicts approximately 3 stocks will move 3 standard deviations on any given day. In
reality, there are routinely five to ten moves of 5 standard deviations or more per day —
events the lognormal model says should occur perhaps once in a lifetime.

The probability of an 8-standard deviation move under the lognormal distribution is
0.000000000000000629. In practice, such moves occur on nearly any trading day.

**The mechanism of failure:** The lognormal distribution does not allow for the
occasional wild days that many stocks undergo. Large moves happen, they happen
regularly, and they tend to happen rapidly — often including gap moves that provide
no opportunity to exit at intermediate prices. This rapidity is as important as the
magnitude: the large move arrives before most participants can react.

---

## 2. The Data: Fat Tails Quantified

**Table 38-1. Sample large moves on one day (April 5, 1999):**

| Stock | Last Sale | Change | Standard Deviations |
|---|---|---|---|
| Aspect Devt (ASDV) | 8 | −14.38 | −31.2 |
| Axent (ANT) | 8 | −12 | −11.2 |
| Ameritrade (AMTD) | 91.63 | +29.13 | +8.6 |
| CheckPoint (CHKP) | 28.75 | −10.75 | −8.4 |
| Sabre Gp. (TSG) | 55 | +8.50 | +8.0 |

On that day, 58 stocks had moves greater than 4 standard deviations. Even on the
lowest-volatility day since VIX inception (July 25, 1993), 12 stocks moved more than
4 standard deviations.

**30-day studies of 2,500–2,900 optionable stocks:**

**Table 38-2. October 22 – December 7, 1999 (VIX ~23, moderate volatility):**

| | 3σ | 4σ | 5σ | >6σ | Total |
|---|---|---|---|---|---|
| Upside | 309 | 116 | 44 | 47 | 516 |
| Downside | 69 | 29 | 15 | 19 | 132 |
| **Total ≥3σ: 648 stocks = 22% of stocks studied** | | | | | |

**Table 38-3. June 1 – July 18, 1999 (quieter period):**

| | 3σ | 4σ | 5σ | >6σ | Total |
|---|---|---|---|---|---|
| Upside | 104 | 28 | 13 | 12 | 157 |
| Downside | 54 | 19 | 7 | 14 | 94 |
| **Total ≥3σ: 251 stocks = 10% of stocks studied** | | | | | |

**Table 38-4. July 1 – August 17, 1993 (least volatile period in the database):**

| | 3σ | 4σ | 5σ | >6σ | Total |
|---|---|---|---|---|---|
| Upside | 14 | 5 | 1 | 1 | 21 |
| Downside | 28 | 5 | 3 | 4 | 40 |
| **Total ≥3σ: 61 stocks = 10% of stocks studied** | | | | | |

**The baseline number to internalize:** Even in the calmest market environment in
the database, 1 in 10 stocks made a 3σ+ move in any 30-day period. The lognormal
model assigns near-zero probability to these events.

**Methodology note:** The current 20-day historical volatility was used each day of
the study to define how many standard deviations each stock moved. In 1993, low
historical volatility meant a smaller absolute move was needed to register 4σ. The
results are not inflated by using a single low-volatility baseline.

---

## 3. The Quantified Gap: 12-to-1 and 20-to-1 at the Tails

The large-scale study covered over 2.5 million individual stock trading days,
September 1993 to April 2000.

**Downside fat tail (−4σ or worse):**
- Lognormal expectation: fewer than 200 occurrences out of 2.5 million
- Actual occurrence: nearly 2,500 times
- **Ratio: more than 12 times the theoretically expected frequency**

**Upside fat tail (+4σ or better):**
- Lognormal expectation: fewer than 100 occurrences
- Actual occurrence: approximately 2,000 times
- **Ratio: approximately 20 times the theoretically expected frequency**

The lognormal distribution overpredicts outcomes between −2.5σ and +0.5σ relative
to actual experience. Outside that range, actual frequency exceeds theoretical
frequency — and the discrepancy grows rapidly at the extremes.

**The mini-crash of April 14, 2000** (Dow −617, S&P −83, NASDAQ-100 −346):
approximately 750 out of 2,984 stocks had moves of −4σ or worse on a single day.
This event benefited those holding long puts greatly, while it caused severe damage
to naked put sellers and leveraged stock owners.

> **Annotation:** The 12-to-1 and 20-to-1 ratios mean that any probability analysis
> used to price an option systematically underweights large moves. The call buyer at
> low IV is therefore undercharged for the actual distribution of outcomes. For the
> put buyer held as downside protection, the 750-out-of-2,984 stocks on a single crash
> day illustrates what that protection actually delivers in a real crisis.

---

## 4. What Fat Tails Mean for Option Selling Strategies

Large moves are rapid and often include gaps. This creates specific problems for
strategies with limited upside and meaningful downside:

**Covered call writing:** When the stock makes a large upside move, the covered
writer is capped at the strike and misses the full appreciation. When the stock drops
sharply, the covered writer suffers the full downside loss offset only by the small
premium received. In both tail scenarios — the ones that actually occur far more
frequently than the lognormal model suggests — the covered writer is at a structural
disadvantage.

**Vertical spreads:** A spread limits profit potential. When the large moves that
actually occur in practice materialize, the spread holder cannot participate in the
full extent of the favorable move. The spread was established to reduce cost; the
fat tails mean the full move is precisely what was worth owning.

**Naked put selling:** When an investor sells a naked put saying "I wouldn't mind
owning the stock at that price," the large, rapid downside move arrives before they
can exit. By the time assignment occurs, the stock has moved far beyond the strike
on a gap — and the appetite for ownership has typically evaporated with the price.

**For option sellers who persist:** Sell only when implied volatility is expensive
relative to historical norms, so any subsequent IV decrease works in the seller's
favor. More importantly: concentrate on **indices rather than individual stocks**.
Indices are statistically much less volatile than individual stocks because the
diversification effect dampens the impact of individual stock fat-tail moves on the
index level.

---

## 5. The Monte Carlo Simulation: What It Is and Why It Matters

The simple probability calculator (the endpoint formula from Chapter 28) has two
limitations: it assumes constant volatility and it assumes the lognormal distribution.
Both assumptions are demonstrably wrong.

A Monte Carlo simulation addresses both. The intuitive description: let the computer
run through the simulation many times and count how many times a certain outcome
occurs. If the number of trials is large enough and the model is good enough, the
resulting count divided by the number of trials is a reliable probability estimate.

For a stock probability calculator, the Monte Carlo simulation proceeds as follows:
1. Build the actual distribution of daily stock price moves into the computer —
   including fat tails. A 2.5-million-point dataset produces an empirical distribution
   where, for example, 3.68% of days result in no change and 0.10% result in a
   move of −4σ or worse.
2. Allow the stock to move randomly each day in accordance with the user's
   volatility input, drawing from the actual distribution rather than the lognormal.
3. Track each simulated path through the full number of trading days. Record
   whether the target price (upside or downside) was reached at any point during
   the path.
4. After 100,000 trials, divide the number of paths that hit the target by 100,000.
   The result is the probability estimate.

The fat-tail Monte Carlo simulation is the correct tool for probability analysis
because it reflects what actually happens — not what a smooth, thin-tailed
mathematical model says should happen.

---

## 6. Fat Tails Vindicate Option Buying: The Expected Return Conclusions

From expected return studies using the fat-tail Monte Carlo simulation, McMillan
draws three conclusions — stated here in order of increasing surprise:

**First:** A bull spread is an inferior strategy when options are fairly priced, regardless
of which distribution is assumed. This is consistent with the negative position vega
findings in Chapter 37 and the general disappointment traders experience with
vertical spreads.

**Second:** Covered writing, which appears superior to outright stock ownership under
the lognormal distribution, is approximately equal to stock ownership under the fat-tail
distribution. The apparent edge of covered writing evaporates when the actual
frequency of large moves is incorporated.

**Third — most startling:** Option buying strategies fare much, much better under the
fat-tail distribution than under the lognormal. A limited-risk investment with unlimited
profit potential performs very well when fat tails are allowed for — because the large,
favorable moves that the market underprices are precisely what the option buyer
captures.

**McMillan's summary verdict, stated as a rule:**

> *In real life, strategies with limited profit potential and unlimited or large risk
> potential are inferior strategies.*

The conventional wisdom — promoted by many brokers — says: "Don't buy options,
don't mess with spreads, either buy stocks or do covered call writes." The fat-tail
distribution stands this advice on its head. The correct conclusion from the data is
the opposite: the strategy that benefits most from how stocks actually behave is
buying options with defined risk and unlimited profit potential.

> **Annotation:** This is the empirical foundation for the entire playbook. The case
> against buying options is built on a distribution model that understates the probability
> of large moves by 12 to 20 times at the tails. When the correct distribution is used,
> bull spreads are confirmed inferior (consistent with Chapter 37), covered writing loses
> its edge over stock ownership, and outright option buying is the strategy that benefits
> most from actual stock behavior. The three conclusions close the argument the playbook
> has been building across the preceding chapters.

---

## 7. Out-of-the-Money Options Are Probably Slightly Underpriced — With a Qualification

Because the market prices options using the lognormal model, and the actual
distribution has fatter tails, out-of-the-money options are probably underpriced to
some degree — the market assigns too low a probability to the large moves that would
bring them in-the-money.

However: the underpricing is modest. Large moves are more frequent than the model
predicts but still relatively rare in absolute terms. An OTM option may be slightly
underpriced, but often not enough to make a material difference in practice.

The counterexample: out-of-the-money call options on grain, gold, and oil futures
often trade at significantly higher implied volatilities than at-the-money options —
a market correction for the possibility of large moves. Ironically, such large moves
are less common in commodities than in stocks historically. Those options are likely
overpriced relative to the actual fat-tail risk they are compensating for.

**The practical conclusion:** Fat tails are a structural tailwind for the prepared option
buyer — not a standalone rationale for buying deeply OTM lottery tickets. The full
case for option buying rests on: (1) low IV entry, (2) a specific fundamental thesis
with a catalyst, and (3) the fat-tail distribution providing more probability of a large
favorable move than the market prices in. All three together, not fat tails alone.

---

## 8. The Conservative Volatility Rule: Bias Against Your Objectives

All probability calculators require a volatility input, and the output is only as reliable
as that input. The governing rule:

**Bias the volatility estimate against your objectives.**

- **For option buyers** (positive vega positions): use the *lowest* reading in the
  available historical volatility stack. If the position looks attractive under this
  pessimistic assumption, it has genuine margin of safety. Any IV expansion above
  the conservative base is incremental benefit.

- **For option sellers** (negative vega positions): use the *highest* reading in the
  available historical volatility stack. If the position still looks attractive under
  an assumption of elevated volatility, it will not be unpleasantly surprised by
  higher-than-expected realized volatility.

**Worked example — option buyer:**

Five-month straddle on XYZ at 40, straddle cost 8, break-evens at 48 and 32.

| Period | Historical Volatility |
|---|---|
| 10-day | 22% |
| 20-day | 20% |
| 50-day | 28% |
| 100-day | 33% |

Use the 20-day reading of 20% — the lowest of the four — as the volatility input.
If the straddle still shows an acceptable probability of reaching a break-even point
under this conservative assumption, the trade has a genuine basis. If actual volatility
turns out to be higher during the life of the position, that is additional benefit beyond
what was modeled.

> **Annotation:** This is the options analogue of using conservative assumptions in
> a valuation. The value investor who builds a DCF with below-consensus growth
> estimates is doing the same thing: biasing assumptions against the conclusion. If the
> investment still passes at conservative inputs, the margin of safety is real.

---

## 9. The Long-Lookback Median Method for Distressed Stocks

When a stock has been behaving erratically for longer than 100 days — so that the
entire standard volatility stack is contaminated by recent unusual behavior — the
short-term readings overstate the stock's true long-term volatility. A longer-lookback
median approach provides a more realistic baseline.

**The method:** Go back in a historical database and compute the 20-day, 50-day, and
100-day historical volatilities for all time periods in the database (or at least a large
segment of past prices). Use the median of those calculations as the volatility estimate.

**Worked example:**

XYZ has been in distress for months. Current readings:

| Period | Historical Volatility |
|---|---|
| 20-day | 130% |
| 50-day | 100% |
| 100-day | 80% |

Long-lookback analysis over the last 1,000 trading days:

| Percentile | 100-Day Historical Volatility |
|---|---|
| 0th | 34% |
| 10th | 37% |
| 20th | 43% |
| 30th | 45% |
| 40th | 46% |
| **50th (median)** | **48%** |
| 60th | 51% |
| 70th | 58% |
| 80th | 67% |
| 90th | 75% |
| 100th | 81% |

Median across all lookback periods: approximately **48–52%**. The correct volatility
input for probability analysis is roughly 48–52%, not the current 80–130%.

There is nothing magical about 1,000 trading days. Approximately 600 trading days
may be preferable in some cases. The goal is to bring in enough historical data to
counterbalance recent, episodic behavior.

**The honest caveat:** Volatilities are unstable no matter how carefully they are
computed. They are at best a fragile estimate of what might happen in the future. The
long-lookback median mitigates the problem; it does not solve it.

> **Annotation:** This method is directly applicable to beaten-down, high-IV situations
> that the playbook targets — stocks in distress where recent volatility reflects an
> episode, not permanent character. The question it answers: is current IV genuinely
> high relative to long-term norms, or does it just look high because it is being compared
> to other recent distress readings? A stock at the 90th percentile of a 1,000-day
> distribution with a median of 48% is genuinely expensive to hedge. A stock near
> the 20th percentile of the same distribution is not — it is in the entry zone the
> playbook targets regardless of the absolute current IV number.

---

## 10. Delta as a Probability Estimate — and the "Ever" vs. "Endpoint" Gap

Delta is a reasonable quick estimate of the probability of an option expiring
in-the-money. It is widely used as a shortcut:

- A call with delta 0.30 has approximately a 30% chance of expiring in-the-money.
- A put with delta −0.20 has approximately a 20% chance of expiring in-the-money.

**The limitation:** Delta estimates the probability at the *endpoint* only — where the
stock is at expiration. It says nothing about the probability of the option being
in-the-money at any point *during* its life. The "ever" probability is materially higher.

**Worked example:** OEX at 600, naked puts at strike 550, 30 days to expiration,
volatility 25%.

Simple endpoint calculator (delta approximation):
- Probability OEX above 550 at expiration: 81%
- Probability OEX below 550 at expiration: 19%

Actual three-scenario breakdown:
| Scenario | Probability |
|---|---|
| OEX never falls below 550 | 67% |
| OEX falls below 550 and stays there | 19% |
| OEX falls below 550 but rallies back above it | 14% |

The endpoint calculator shows an 81% probability of a worry-free trade. The actual
probability of a worry-free trade is only 67%. The 14% difference — the probability
that the option goes in-the-money during its life but recovers by expiration — is
invisible to the endpoint calculator but very real to the position holder who must
manage the position through that period.

**Fat-tail comparison for a put on XYZ at 70, put strike 60:**

| Calculator | Probability XYZ ever trades < 60 |
|---|---|
| Simple endpoint | 10% |
| "Ever" calculator (lognormal) | 20% |
| "Ever" calculator (fat tail) | 22% |

A naked put seller targeting 15% or less "probability of becoming troublesome" would
accept the trade using the simple endpoint calculator (10%) but reject it using the
correct "ever" probability (22%). The choice of calculator determines whether the
trade is entered.

**For call buyers:** Delta is a conservative floor estimate of eventual profitability
probability. A 30-delta call has roughly a 30% chance of expiring in-the-money but
a materially higher chance of trading in-the-money at some point before expiration —
which is the relevant scenario for an investor who intends to sell the option before
expiry. The fat-tail distribution widens this gap further. Treat delta as a minimum
probability estimate, not the complete picture.

---

## 11. Summary: Using a Probability Calculator Correctly

Before taking any option position — including an outright call purchase — use a
probability calculator. In doing so, be aware of three limitations:

1. **Volatility input dependency:** The output is heavily biased by the volatility
   estimate. Use the conservative volatility rule from Section 8 — bias against
   your objectives.

2. **Distribution assumption:** The lognormal distribution understates large moves
   by 12 to 20 times at the tails. Where possible, use a fat-tail Monte Carlo
   simulation rather than the simple endpoint formula.

3. **Endpoint vs. "ever":** The simple calculator gives the probability at expiration
   only. The probability of the option touching a price at any point during its life
   is materially higher — use the "ever" calculator when managing positions where
   interim drawdowns matter, not just the final expiration outcome.

Run the analysis under multiple distribution assumptions — lognormal, fat-tail, and
the historical distribution specific to the underlying. The range of results gives a
realistic picture of what could happen during the life of the position. No single
number from any model should be treated as a precise forecast; the goal is a
calibrated sense of the range of outcomes and whether the position's risk/reward
is genuinely attractive across scenarios.

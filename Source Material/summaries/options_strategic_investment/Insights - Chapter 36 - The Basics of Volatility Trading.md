# Chapter 36: The Basics of Volatility Trading —
# Extracted Insights for the Conservative Options Playbook

---

## Foundational Definitions: Two Types of Volatility

Volatility is the term used to describe how fast a stock, future, or index changes in
price. When volatility is discussed in connection with options, two types matter:

**Historical volatility** is a measure of how fast the underlying instrument has been
changing in price. It is a backward-looking, exact calculation — the standard deviation
formula applied to past stock price changes, expressed as an annualized percentage.
There is little debate about how to compute it.

**Implied volatility** is the option market's prediction of the volatility of the underlying
over the life of the option. It is forward-looking and derived by working backward from
the current market price of the option. It is the only input to the Black-Scholes model
that is not directly observable.

One backward-looking, one forward-looking. Both are expressed as annualized
percentages, making them directly comparable to each other.

---

## 1. Implied Volatility: The Sole Unknown in the Option Pricing Equation

At any point in time, a trader knows with certainty five of the six inputs that determine
an option's price: stock price, strike price, time to expiration, interest rate, and
dividends. The only remaining factor is volatility — specifically, implied volatility.
It is the single degree of freedom in the pricing equation — the "big fudge factor" in
option trading.

If implied volatility is too high, options are overpriced — relatively expensive. If
implied volatility is too low, options are underpriced — relatively cheap. In modern
practice, traders no longer use "overpriced" and "underpriced" because those terms
imply knowing what an option *should* be worth. The correct framing: options are
trading with "high implied volatility" or "low implied volatility," meaning the current
reading is high or low relative to where it has historically been.

**Worked example:**

XYZ price: 52; April 50 call price: 6; time to April expiration: 36 days;
dividends: $0.00; risk-free rate: 5%.

The question: what volatility must be plugged into Black-Scholes to produce the
observed price of 6?

6 = f(52, 50, 36 days, 5%, Volatility, $0.00)

The answer in this case: **implied volatility = 75.4%**. Whatever volatility makes the
model yield the current market price is the implied volatility for that option.

Implied volatility is the option market's estimate of forthcoming actual volatility of the
underlying over the life of the option. If traders believe the underlying will be volatile,
they bid up the option. If they envision a quiet period, they bid lower. Critically,
traders do not know the future — implied volatility is a guess, and it can be wrong.

---

## 2. Why Volatility Estimates Are Necessary for Strategy Decisions

We need to be able to make volatility estimates in order to determine whether a strategy
might be successful and whether the current option price is relatively cheap or expensive.
One cannot simply say "I think XYZ is going to rise at least 18 points by February
expiration" without a statistical basis for that statement. Absent inside information,
that basis must come from volatility projections.

Volatility estimates answer three practical questions:
1. Is the current option cheap or expensive relative to what the stock is likely to do?
2. What is a realistic price target and over what time period?
3. What is the probability of the position being profitable given the current premium?

Without volatility estimates, strategy decisions rest on intuition rather than probability.
The machinery of Chapter 28 — historical volatility, composite implied volatility,
expected return calculations — exists to answer these three questions rigorously.

---

## 3. Implied Volatility Trades in a Range — and That Range Is Predictable

The implied volatility chart of nearly every stock, index, or futures contract shows a
similar pattern: a trading range. Implied volatility oscillates within recognizable bounds
rather than trending indefinitely in one direction.

The only time implied volatility will totally break out of its normal range is if something
material happens to change the fundamentals of how the stock moves — a takeover bid,
a major acquisition, or other significant structural change to the underlying business.

The practical implication: options on a given stock have a characteristic IV range, and
positions entered when implied volatility is near the bottom of that range are
structurally advantaged relative to positions entered near the top.

> **Annotation:** A stock that is depressed, under-followed, and quiet will typically
> also have depressed implied volatility. Buying calls in that environment captures two
> potential tailwinds simultaneously — stock price appreciation and IV expansion. The
> range-bound nature of IV means that the entry point within the IV cycle is not a
> random variable; it can be assessed and optimized.

---

## 4. Historical Volatility: Benchmarks and the Multi-Period Stack

Historical volatility is an exact, formula-based calculation expressed as an annualized
standard deviation percentage. Its primary use is comparative.

**Benchmark anchors:**
- Broad stock market historical volatility: typically 15%–20%
- Very volatile individual stock: may exceed 100%
- A stock at 80% historical volatility is approximately four times as volatile as the
  broad market

These anchors allow immediate contextualization of any volatility reading. A stock
does not need to be labeled "volatile" or "quiet" subjectively — the number places it
on a scale relative to known benchmarks.

**The multi-period stack:** Historical volatility is commonly computed at four horizons
simultaneously — 10-day, 20-day, 50-day, and 100-day — all annualized so they can
be compared directly. The 20-day reading is the most commonly used single measure.
The shape of the stack tells the investor the direction of current volatility momentum.

**Slowing down (stock that has been quieting):**

| Period | Historical Volatility |
|---|---|
| 10-day | 20% |
| 20-day | 23% |
| 50-day | 35% |
| 100-day | 45% |

Stack slopes downward from longer to shorter periods — the stock has been less
extreme in price movement recently than in the past.

**Heating up (stock that has recently become more volatile):**

| Period | Historical Volatility |
|---|---|
| 10-day | 80% |
| 20-day | 75% |
| 50-day | 60% |
| 100-day | 55% |

Stack slopes upward from longer to shorter periods — the stock has been more
volatile recently than in the more distant past.

Note: violent back-and-forth action can produce a higher historical volatility reading
than a straight-line move of the same magnitude, simply due to how the standard
deviation formula works.

> **Annotation:** The stack shape is a quick pre-entry screen. A downward-sloping
> stack (20% at 10-day, 45% at 100-day) means the stock has been quieting — implied
> volatility has likely followed historical volatility down and options are cheap. An
> upward-sloping stack (80% at 10-day, 55% at 100-day) means volatility is currently
> elevated — a caution flag for call buyers entering into an IV spike rather than a
> trough. Checking the stack costs nothing and takes seconds.

---

## 5. Smoothing Implied Volatility: The Exponential Moving Average

As noted in Chapter 28, a smoothing effect on daily implied volatility is obtained by
taking a moving average of recent readings. The recommended approach is an
exponential moving average (EMA) rather than a simple moving average, for a specific
practical reason: the EMA does not require storing 20–30 days of prior data. Only the
most recent EMA value is needed to compute the next one.

The formula: today's smoothed IV = (5% × today's raw implied volatility) +
(95% × yesterday's smoothed implied volatility).

This preserves the smoothing effect while requiring only one prior data point. In
practice, any options analytics platform will compute this automatically.

---

## 6. Implied Volatility Is a Poor Predictor of Actual Volatility — and That Bias Works in the Call Buyer's Favor

McMillan's firm opinion, stated directly: implied volatility is a poor predictor of actual
volatility. The data consistently shows that implied volatility over- or underestimates
actual subsequent volatility by wide margins, rather than hovering near zero difference.

**The structural reason:** Option traders and market-makers make predictions when they
price options, and tend toward "middle of the road" estimates because extreme
predictions are more likely to be wrong. When the market collapses, implied volatilities
rise only modestly. The result: implied volatility fluctuates less than actual volatility.
Large moves — in either direction — are systematically underpriced by implied
volatility.

**Worked example from the text:** In early 1999, a stock's implied volatility was at or
near its lowest historical levels. Within weeks, the stock tripled in value in just over a
month. Implied volatility had been a completely inadequate predictor of what was about
to happen. In a second example, after implied volatility had been elevated relative to
actual volatility and traders had pushed it back down to its lowest daily reading, the
stock made a sequence of sharp moves and ultimately doubled — with implied volatility
remaining low throughout.

The operating conclusion: all that can be said with certainty is that implied and
historical volatility tend to trade within a range. Neither predicts the future reliably.

> **Annotation:** The "middle of the road" forecasting bias is the key structural finding
> for the value investor. Because market participants systematically anchor IV toward
> the center of the historical range, options are chronically underpriced ahead of large
> moves — precisely the moves that value investors are positioned to anticipate through
> fundamental research. The investor buying calls on a depressed, low-IV stock is not
> simply hoping for IV expansion as a bonus; the structural bias of the market means
> that if the thesis plays out with a large price move, implied volatility will have been
> an inadequate reflection of what actually occurred. The premiums paid at entry will,
> in retrospect, have been too low. This is a systematic edge available to anyone who
> does the fundamental work to identify the move before the market prices it into IV.

---

## 7. Percentile of Implied Volatility: The Range Behind the Rank Matters

The percentile of implied volatility ranks the current IV reading against past readings
for the same underlying. A reading at the 10th percentile means options are cheaper
than 90% of historical observations.

However, knowing the percentile is not enough without also knowing the width of the
range over which that percentile was computed.

**Tight range — percentile nearly meaningless:**

If the entire historical IV range for XYZ stretched only from 39% to 45%, a current
reading of 40% is at the low percentile but practically unremarkable. Even if IV rose
to its historical maximum of 45%, individual options would gain very little value from
the 5-point absolute move.

**Wide range — low percentile is genuinely cheap:**

If the historical IV range for XYZ stretched from 35% to 90%, a current reading of
40% represents genuine cheapness. IV could expand by 50 percentage points on an
absolute basis — a move that would substantially inflate option prices.

**The operating rule:** Know the current percentile of implied volatility AND the
absolute width of the historical range. If the range is wide, an extreme percentile
truly represents a cheap or expensive option. If the range is tight, the percentile is
not practically meaningful and should not drive the decision.

> **Annotation:** For a value investor screening calls across several names, the
> two-step check is: (1) What is the current IV percentile? (2) What is the absolute
> width of the historical IV range? A stock at the 10th percentile with a range of
> 35%–90% offers far more IV expansion potential than a stock at the 10th percentile
> with a range of 39%–45%. The second piece of information converts "cheap by
> percentile" into "cheap in a way that actually matters for call value."

---

## 8. LEAPS Implied Volatility Has a Narrower Range — With Important Consequences

The range of implied volatility narrows substantially as time to expiration increases.
OEX scatter diagram data shows near-term options ranging from approximately 14%
to 40% in implied volatility, while options with 24 or more months remaining range
only from approximately 17% to 32%.

LEAPS implied volatilities simply do not change nearly as much as those of short-term
options. This has two consequences:

**First — LEAPS will rarely appear cheap on a percentile basis:** When LEAPS IV is
evaluated against a composite that includes short-term options, the narrow range of
LEAPS IV means it almost never reaches the extreme low percentiles that short-term
options occasionally hit. A LEAPS at the 20th percentile of its own range may look
normal, but that range only spans 15 percentage points while the short-term range
spans 26.

**Second — holding a LEAPS through its life exposes the investor to widening vol
range:** As time shrinks and a long-dated LEAPS becomes a shorter-dated option, the
volatility range it is subject to widens. IV can swing more violently — both up and
down — as expiration approaches. An initially stable LEAPS position can experience
increasing IV turbulence in its final months.

The governing principle: the volatility range expands as time shrinks.

> **Annotation:** For the value investor buying LEAPS as the primary vehicle for a
> multi-month fundamental thesis, the primary profit driver is stock price appreciation,
> not IV expansion. Do not expect a large IV windfall from LEAPS — the absolute range
> of LEAPS IV movement is small, and "cheap by percentile" LEAPS rarely produce
> large vega gains. The IV expansion benefit is more relevant for shorter-dated calls
> where the range is wider and a move from the 10th to the 90th percentile produces a
> meaningful absolute change in option value.

---

## 9. When Low Implied Volatility Is Genuinely Exploitable vs. Structurally Justified

Low IV is exploitable when it reflects market complacency — option sellers have grown
aggressive in a quiet period, option buyers have become timid after watching their
purchases decay, and prices have been pushed down by supply/demand dynamics with
no fundamental basis.

Low IV is structurally justified — and should not be bought on a volatility basis alone —
when it reflects a genuine permanent reduction in the stock's future price movement.
A company being acquired and absorbed into a larger, more stable entity will legitimately
have lower future volatility. A maturing company with a growing, predictable earnings
stream may legitimately be less volatile than it was in its early growth phase.

The contrarian framing: volatility buying is a contrarian strategy. When everyone else
thinks the underlying will be nonvolatile, when option sellers are aggressive and buyers
are hard to find, the volatility buyer steps in. The reflexive dynamic — sellers pushing
IV down, buyers becoming timid, IV falling further — creates the best entry conditions.

**The asymmetry of error between buyers and sellers:**

Buyers of volatility who miscalculate occasionally will not be fatally harmed. Buying
an option that appears cheap but turns out not to be results in a loss limited to the
premium paid. Sellers of volatility must be much more careful — a seller who is wrong
faces losses that can be very large. An occasional mistake in buying volatility is
survivable; an occasional mistake in selling volatility can be devastating.

> **Annotation:** The value investor's standard research process maps directly onto
> McMillan's test for whether low IV is justified. If the stock is cheap because of a
> temporary sentiment overhang, a mistaken market reaction to a non-recurring event,
> or a catalyst the market hasn't yet recognized — low IV is not structurally justified
> and buying calls is structurally advantaged. If the stock is cheap because the business
> has permanently deteriorated and future price movement will genuinely be smaller —
> low IV may be correct and should not be bought on a volatility basis alone. The
> fundamental work the investor already does to assess the stock also answers
> McMillan's IV question. The asymmetry of error is a further argument for the
> playbook's bias toward buying rather than selling volatility: mistakes in buying
> are survivable; mistakes in selling may not be.

---

## 10. Warning Signs That an IV Spike Reflects Inside Information

For the call buyer, a sudden IV spike accompanied by the following signals suggests
the market is pricing in a corporate event — meaning entry at that point means buying
peak IV just before resolution:

**Two warning signals:**
1. Dramatic increase in option volume propagating across multiple strikes and
   expirations (not just one series)
2. Sudden jump in implied volatility combined with a rising stock price

The combination of expensive options AND a rising stock price is the key tell.
When market-makers react to aggressive call buying by buying stock to reduce their
negative delta exposure, both option IV and stock price rise together. If the options
are active and expensive AND the stock is rising, someone likely knows something.

**The illiquid-options edge case:** In thinly traded options, implied volatility can
explode in a short period — even in a single day — with market-makers repeatedly
raising their offering price on small transactions. A sudden IV explosion in illiquid
options is itself a warning sign, even without high volume.

**When high IV following a known public event is safe to act on:** If a company has
announced poor earnings and the stock has dropped while implied volatility rose, the
information is public and symmetric. The situation can be analyzed clearly. This is
not insider-driven IV — it is a known event being priced in, and the investor can
assess whether the market's reaction is an overreaction worth trading against.

> **Annotation:** For the value investor, the primary use of these warning signals is
> as an entry timing guide. The better entry was before the spike — when IV was low
> and the fundamental thesis was already in place. If the investor finds himself looking
> at calls after a simultaneous IV spike and stock price rise, the opportunity has likely
> already passed. If the spike follows a known public event — an earnings miss, a broad
> market selloff, a sector rotation — IV can still be acted on because the information
> is symmetric and the situation is analyzable. The key distinction: insider-driven spikes
> should be avoided; sentiment-driven or news-driven spikes on public information may
> represent entry opportunities.

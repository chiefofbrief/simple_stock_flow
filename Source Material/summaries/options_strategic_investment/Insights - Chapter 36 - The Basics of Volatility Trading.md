# Chapter 36 — The Basics of Volatility Trading: Extracted Insights for the Conservative Options Playbook

---

## 1. Implied Volatility Trades in a Range — and That Range Is Predictable

The foundational observation of the chapter is that implied volatility, unlike stock prices,
tends to oscillate within a recognizable trading range rather than trend indefinitely.
McMillan illustrates this with a chart of IBM's implied volatility — presented without
scale or label, so that the reader sees only a clean oscillating pattern before being told
what it depicts. The point: "The implied volatility chart of nearly every stock, index, or
futures contract has a similar pattern — a trading range. The only time that implied
volatility will totally break out of its 'normal' range is if something material happens to
change the fundamentals of the way the stock moves — a takeover bid, for example, or
perhaps a major acquisition or other dilution of the stock."

The practical implication for any option buyer: options on a given stock have a
characteristic IV range, and positions entered when implied volatility is near the bottom
of that range are structurally advantaged relative to positions entered near the top.

> **Annotation:** This is the single most important framing concept in the chapter for a
> value investor buying calls. A stock that is depressed, under-followed, and quiet will
> typically also have depressed implied volatility. Buying calls in that environment captures
> two potential tailwinds simultaneously — stock price appreciation and IV expansion —
> as was noted in Chapter 3. The range-bound nature of IV means that the entry point
> within the IV cycle is not a random variable; it can be assessed and optimized.

---

## 2. Implied Volatility Defined: The Only Unknown in the Option Pricing Equation

"At any one point in time, a trader knows for certain the following items that affect an
option's price: stock price, strike price, time to expiration, interest rate, and dividends.
The only remaining factor is volatility — in fact, *implied* volatility. It is the big 'fudge
factor' in option trading. If implied volatility is too high, options will be overpriced. That
is, they will be relatively expensive. On the other hand, if implied volatility is too low,
options will be cheap or underpriced."

McMillan provides the worked example directly:

XYZ price: 52  
April 50 call price: 6  
Time remaining to April expiration: 36 days  
Dividends: $0.00  
Risk-free interest rate: 5%  

"So what volatility would one have to plug in the Black-Scholes model (or whatever model
one is using) to make the model give the answer 6 (the current price of the option)? That
is, what volatility is necessary to solve the equation? 6 = f(52, 50, 36 days, 5%, Volatility,
$0.00). Whatever volatility is necessary to make the model yield the current market price
(6) as its value, is the implied volatility for the XYZ April 50 call. In this case, if you're
interested, the implied volatility is 75.4%."

The modern framing: "The terms 'overpriced' and 'underpriced' are not really used by
theoretical option traders much anymore, because their usage implies that one knows what
the option *should* be worth. In the modern vernacular, one would say that the options are
trading with a 'high implied volatility' or a 'low implied volatility,' meaning that one has
some sense of where implied volatility has been in the past, and the current measure is
thus high or low in comparison."

"Essentially, implied volatility is the option market's *guess* at the forthcoming statistical
volatility of the underlying over the life of the option in question. If traders believe that
the underlying will be volatile over the life of the option, then they will bid up the option,
making it more highly priced. Conversely, if traders envision a nonvolatile period for the
stock, they will not pay up for the option, preferring to bid lower; hence the option will be
relatively low-priced. The important thing to note is that traders normally do *not* know
the future. They have no way of knowing, for sure, how volatile the underlying is going to
be during the life of the option."

---

## 3. Historical Volatility: How to Read the Multi-Period Stack

Historical volatility is the exact, formula-based calculation of how fast a stock has been
changing in price — expressed as an annualized standard deviation percentage. The
20-day historical volatility is cited as "commonly the most popular measure." Its primary
strategic use is comparative: a stock with historical volatility over 100% is five times more
volatile than the broad market's typical 15%–20%.

The diagnostic value of the multi-period stack — comparing 10-day, 20-day, 50-day, and
100-day readings simultaneously — is illustrated with two examples.

**Slowing down (stock that has been quieting):** At point A in McMillan's Figure 36-2,
after a stock has been meandering in a tight range:

| Period | Historical Volatility |
|---|---|
| 10-day | 20% |
| 20-day | 23% |
| 50-day | 35% |
| 100-day | 45% |

"A pattern of historical volatilities of this sort describes a stock that has been slowing
down lately. Its price movements have been less extreme in the near term."

**Heating up (stock that has recently become more volatile):** At the far right edge of the
same chart, after the stock has made a sharp move followed by rapid back-and-forth action:

| Period | Historical Volatility |
|---|---|
| 10-day | 80% |
| 20-day | 75% |
| 50-day | 60% |
| 100-day | 55% |

"With this alignment of historical volatilities, one can see that the stock has been more
volatile recently than in the more distant past."

McMillan also notes: "Violent action in a back-and-forth manner can often produce a
higher historical volatility reading than a straight-line move can; it's just the way the
numbers work out."

> **Annotation:** The shape of the volatility stack tells the value investor the direction
> of current volatility momentum. A stack that slopes downward from longer to shorter
> periods (20% at 10-day, 45% at 100-day) means the stock has been quieting — a
> favorable entry condition for call buying, because implied volatility has likely followed
> historical volatility down and options are cheap. A stack that slopes upward from longer
> to shorter periods (80% at 10-day, 55% at 100-day) means volatility is currently
> elevated — a caution flag for call buyers, who would be buying into an IV spike rather
> than a trough. Checking the historical volatility stack is a quick pre-entry screen that
> costs nothing.

---

## 4. Implied Volatility Is Not a Reliable Predictor of Actual Volatility — and That Structural Bias Works in the Call Buyer's Favor

"The important thing to note from these figures is that they clearly show that implied
volatility is really not a very good predictor of the actual volatility that is to follow. If it
were, the difference line would hover near zero most of the time. Instead, it swings back
and forth wildly, with implied volatility over- or underestimating actual volatility by quite
wide levels. Thus, the current estimates of volatility by traders (i.e., implied volatility) can
actually be quite wrong."

McMillan illustrates with a concrete stock example (Figures 36-5 and 36-6): "In February
and early March 1999, implied volatility was at or near the lowest levels on these charts.
Yet, by the end of March, a major price explosion had begun in the stock, one that tripled
its value in just over a month. Clearly, implied volatility was a poor predictor of
forthcoming actual volatility in this case."

A second stock example (Figures 36-7 and 36-8) shows the same failure: after implied
volatility had been high relative to actual volatility and traders "made an adjustment"
downward to its lowest daily point, the stock made a rapid sequence of large moves —
first from 15 down to 11, then back to 17, then ultimately doubling — with "implied
volatility remained low at the right-hand side of the charts (January 2000) even though
the stock doubled in the course of a month."

The structural reason why IV systematically underestimates large moves: "Implied
volatility seems to fluctuate *less* than actual volatility. That seems to be a natural function
of the volatility predictive process. For example, when the market collapses, implied
volatilities of options rise only modestly. In other words, option traders and market-makers
are predicting volatility when they price options, and one tends to make a prediction that
is somewhat 'middle of the road,' since an extreme prediction is more likely to be wrong."

The conclusion: "All we can say for sure is that implied and historical volatility tend to
trade within a range."

> **Annotation:** The "middle of the road" forecasting bias is the key structural finding
> here. Because market participants systematically anchor their IV estimates toward the
> center of the historical range, options are chronically underpriced ahead of large moves
> — precisely the moves that value investors are positioned to anticipate through
> fundamental research. The investor buying calls on a depressed, low-IV stock is not
> simply hoping for IV expansion as a bonus; the structural bias of the market guarantees
> that if the thesis plays out with a large price move, implied volatility will have been an
> inadequate reflection of what actually occurred. The premiums paid at entry will, in
> retrospect, have been too low. This is a systematic edge available to anyone who does
> the fundamental work to identify the move before the market prices it into IV.

---

## 5. Percentile of Implied Volatility: The Range Behind the Rank Matters

"It is often conventional to talk about the *percentile of implied volatility*. That is a way
to rank the current implied volatility reading with past readings for the same underlying
instrument."

However, McMillan introduces a critical qualification: knowing the percentile is not
enough without also knowing the width of the range over which that percentile was
computed.

"One can't really tell if 'cheap' options are cheap as a practical matter. That's because
one doesn't know how tightly packed together the past implied volatility readings are."

**Tight range — percentile nearly meaningless:** If the entire past range of implied
volatility for XYZ stretched only from 39% to 45%, then a current reading of 40%, "while
low, might not seem all that attractive. That is, if the first percentile of XYZ options were
at an implied volatility reading of 39% and the 100th percentile were at 45%, then a
reading of 40% is really quite mundane. There just wouldn't be much room for implied
volatility to increase on an absolute basis. Even if it rose to the 100th percentile, an
individual XYZ option wouldn't gain much value, because its implied volatility would
only be increasing from about 40% to 45%."

**Wide range — low percentile is genuinely cheap:** "Suppose, rather than the tight range
described above, that the range of past implied volatilities for XYZ instead stretched from
35% to 90% — that the first percentile for XYZ implied volatility was at 35% and the
100th percentile was at 90%. Now, if the current reading is 40%, there is a large range
above the current reading into which the options could trade, thereby potentially
increasing the value of the options if implied volatility moved up to the higher percentiles."

The operating rule: "What this means, as a practical matter, is that one not only needs to
know the current percentile of implied volatility, but he also needs to know the *range* of
numbers over which that percentile was derived. If the range is wide, then an extreme
percentile truly represents a cheap or expensive option. But if the range is tight, then one
should probably not be overly concerned with the current percentile of implied volatility."

> **Annotation:** For a value investor screening calls across several names, the
> two-step check is: (1) What is the current IV percentile? and (2) What is the absolute
> width of the historical IV range? A stock at the 10th percentile with a range of 35%–90%
> offers far more IV expansion potential than a stock at the 10th percentile with a range
> of 39%–45%. The second piece of information is what converts "cheap by percentile"
> into "cheap in a way that actually matters for call value."

---

## 6. LEAPS Implied Volatility Has a Narrower Range Than Short-Term Options — With Important Consequences

McMillan presents OEX scatter diagram data (Figure 36-3) charting implied volatility
against time to expiration across several years. The key finding: the range of implied
volatility narrows substantially as time to expiration increases.

"For example, the implied volatility readings on the far left of the scatter diagram range
from about 14% to nearly 40% (ignore the one outlying point). However, for longer-term
options of 24 months or more, the range is about 17% to 32%."

"One conclusion that we can draw from this is that LEAPS option implied volatilities just
don't change nearly as much as those of short-term options. That can be an important
piece of information for a LEAPS option trader especially if he is comparing the LEAPS
implied volatility with a *composite* implied volatility or with the *historical* volatility of the
underlying."

**The consequence for IV-cheapness assessments:** "Consequently, LEAPS options will
rarely appear 'cheap' when one looks at their percentile of implied volatility, including all
the short-term options, too."

McMillan then addresses the seemingly logical response — evaluating LEAPS only
against the historical range of other LEAPS — and explains why even that is flawed:
"First, if one holds the option for any long period of time, the volatility range will widen
out and there is a chance that implied volatility could drop substantially. Second, the
long-term volatility range might be so small that, even though the options are initially
cheap, quick increase in implied volatility over several deciles might not translate into
much of a gain in price in the short term."

The principle: "It's important for anyone using implied volatility in his trading decisions
to understand that the range of past implied volatilities is important, and to realize that
the volatility range *expands as time shrinks.*"

> **Annotation:** For the value investor who buys LEAPS as the primary vehicle for a
> multi-month fundamental thesis (per Chapter 3's "uncertain timing" guidance), this has
> two practical implications. First, do not expect a large IV expansion windfall from LEAPS
> — the absolute range of movement in LEAPS IV is small (17%–32% for 24-month OEX
> options vs. 14%–40% for near-term), and a "cheap" LEAPS by IV percentile rarely
> translates into large vega gains. The LEAPS buyer's primary profit driver is stock price
> appreciation, not IV expansion. Second, as the thesis plays out and time shrinks, the
> volatility range of the now-shorter-dated option widens, meaning IV can swing more
> violently — both up and down — as expiration approaches.

---

## 7. When Low Implied Volatility Is Genuinely Exploitable (vs. Justified)

McMillan distinguishes between implied volatility that is low for an identifiable, durable
structural reason versus IV that is low simply because market participants have become
complacent — option sellers have grown aggressive and option buyers timid in a quiet
period, pushing prices down reflexively.

"When implied volatilities are decreasing, option sellers are generally happy (and may
often become more aggressive), while option buyers, who probably have been seeing their
previous purchases decaying with time, become more timid. As a result, option prices
drop. Alternatively stated, implied volatility drops."

The contrarian framing: "Volatility trading is also a contrarian theory of investing. That
is, when everyone else thinks the underlying is going to be nonvolatile, the volatility
trader buys volatility. When everyone else is selling options and option buyers are hard to
find, the volatility trader steps up to buy options."

**When low IV is justified and should be avoided:** A company being taken over, or
maturing significantly (issuing more shares, building a strong earnings stream), will
legitimately have lower future volatility. "If the decrease in implied volatility seems
justified, a buyer of volatility should ignore it and look for other opportunities."

**When low IV is just sentiment and should be bought:** "In some cases, the supply and
demand of the public just pushes the options to extreme levels; there is nothing more
involved than that. Those are the best volatility trading situations."

**Asymmetry of error between buyers and sellers:** "Buyers of volatility really have
little to fear if they miscalculate and thus buy an option that appears inexpensive but
turns out not to be, in reality. The volatility buyer might lose money if he does this, and
overpaying for options constantly will lead to ruin, but an occasional mistake will
probably not be fatal."

> **Annotation:** The value investor's standard research process — identifying why a
> stock is depressed, whether the cause is temporary or permanent — maps directly onto
> McMillan's test for whether low IV is justified. If the stock is cheap because of a
> temporary sentiment overhang, a mistaken market reaction to a non-recurring charge,
> or a catalyst the market hasn't yet recognized, then the low IV is not structurally
> justified and buying calls in that environment is structurally advantaged. If the stock is
> cheap because the business has permanently deteriorated and future price movement
> will genuinely be smaller, the low IV may be correct and should not be bought on a
> volatility basis alone. The fundamental work the investor already does to assess the
> stock also answers McMillan's IV question.

---

## 8. Warning Signs That Expensive IV Reflects Inside Information — Relevant to Entry Timing

McMillan identifies conditions under which a sudden IV spike should be treated as a
potential news event in the making rather than a volatility-selling opportunity. For the
call buyer, the same signals are relevant as an entry timing warning — chasing calls into
a spike means buying elevated IV on the eve of resolution.

"The seller of volatility can watch for two things as warning signs that perhaps the options
are 'predicting' a corporate event. Those two things are a dramatic increase in option
volume or a sudden jump in implied volatility of the options."

On distinguishing insider-driven volume from normal hedging activity: "What
distinguishes these arbitrage and hedging activities from the machinations of insider
trading is: (1) There is little propagation of option volume into other series in the 'benign'
case, and (2) the stock price itself may languish. However, when true insider activity is
present, the market-makers react to the aggressive nature of the call buying… the way
they reduce their negative position delta is to buy stock. Thus, if the options are active
and expensive, and if the stock is rising too, you probably have a reasonably good
indication that 'someone knows something.'"

On the illiquid-options edge case: "Implied volatility *exploded* in a short period of time
(one day, or actually less time), and that alone should be enough warning" — even in the
absence of high volume, because market-makers in illiquid contracts repeatedly raise
their offering price on small transactions without significant volume actually trading.

The market-maker's rule of thumb: "A major market-maker once said he believed that
*most* increases in implied volatility were eventually justified — that is, some corporate
news item was released that made the stock jump."

**When high IV is the result of known, public information and is safe to act on:** "Perhaps
the company has announced poor earnings and the stock has taken a beating while implied
volatility rose. In this situation, one can assess the information and analyze it clearly; he
is not dealing with some hidden facts known to only a few insider traders."

> **Annotation:** For the value investor who is a buyer rather than a seller of volatility,
> the primary use of this section is as an entry timing guide. A sudden IV spike accompanied
> by rising stock price and broad-series volume propagation suggests the market is pricing
> in an event — which may mean the thesis is beginning to play out, or the stock is being
> taken over at a premium. In either case, chasing calls into that spike means paying peak
> IV just before resolution compresses it. The better entry was before the spike, when IV
> was low — which is precisely when the investor with a completed fundamental thesis
> should already be positioned. If the spike follows a known, public event (earnings miss,
> market selloff), IV can still be acted on because the information is symmetric and the
> situation analyzable.

# Chapter 37: How Volatility Affects Popular Strategies —
# Extracted Insights for the Conservative Options Playbook

---

## Foundational Definition: Vega

**Vega is the amount by which an option's price changes when implied volatility
changes by one percentage point.**

It is one of the "greeks" — the partial derivatives of the option pricing model — and
it measures the sensitivity of an option's price to changes in implied volatility
specifically.

**Worked example — call:**

XYZ at 50; July 50 call at 7.25; no dividend; rates 5%; three months to expiration.
Implied volatility = 70%.

If IV rises to 71%: call is worth 7.35. If IV falls to 69%: call is worth 7.15.

> Vega = 0.10

The option price changed by 10 cents for each one-percentage-point move in IV.
There is a direct relationship: IV up → option price up; IV down → option price down.

**Put vega equals call vega for the same terms:**

| Stock Price | July 50 Call | July 50 Put | Implied Volatility |
|---|---|---|---|
| 50 | 7.15 | 6.54 | 69% |
| 50 | 7.25 | 6.64 | 70% |
| 50 | 7.35 | 6.74 | 71% |

A call and a put with the same terms have the same vega. This follows from the
conversion arbitrage equation: if the call increases in price and stock price, strike,
and interest rates are unchanged, the put must increase by the same amount.

> **Annotation:** The symmetry of vega between calls and puts matters for the investor
> who uses both — a long call for upside leverage and a long put for downside protection
> are equally sensitive to IV changes per dollar of vega. Both benefit from buying when
> IV is depressed.

---

## 1. Position Vega: Measuring the Entire Position's IV Exposure

Just as one can compute a position delta for an entire position, one can compute a
position vega — the vega of the entire position.

> **Position vega = Number of contracts × 100 shares per contract × Individual vega**

**Sign convention:**
- **Positive position vega:** the position profits when IV increases. This is the
  profile of an option buyer — long calls, long puts, long calendar spreads.
- **Negative position vega:** the position profits when IV decreases. This is the
  profile of an option seller — covered calls, bull spreads, short straddles.

**Application:** If one identifies expensive options and expects IV to decrease toward
historical norms, construct a position with negative position vega. If one identifies
underpriced options and expects IV to expand, construct a position with positive
position vega.

**Critical warning:** An explosion in implied volatility is a boon to an option owner
but can be a devastating detriment to an option seller — especially a naked option
seller. Position vega quantifies exactly how large that detriment will be.

---

## 2. The Five Factors Affecting Excess Value — and the Greeks That Measure Them

An option's price has two components:
1. **Intrinsic value** — the real part; the distance by which the option is
   in-the-money.
2. **Excess value** — often called time value premium; the remainder.

There are five factors that affect excess value, each stated as a change or movement:

| Factor | Greek | Direction of Effect |
|---|---|---|
| Stock price movements | Delta | Direct (OTM calls) / Inverse on excess value (ITM calls) |
| Changes in implied volatility | Vega | Direct — IV up → excess value up |
| Passage of time | Theta | Inverse — time passes → excess value decreases |
| Changes in dividends | (none) | Dividend increase → call excess value decreases |
| Changes in interest rates | Rho | Minor for short-term options |

"If everything remains static, then time decay will eventually wipe out all of the
excess value of an option. That's why it's called time value premium. But things don't
ever remain static, and on a daily basis, time decay is small, so it is the remaining two
factors that are most important" — stock price movements and changes in implied
volatility.

**The delta-and-excess-value relationship — stated precisely:**

- **Out-of-the-money call:** 100% of the delta affects the excess value. A stock
  price increase brings the stock closer to the strike, increasing the excess value
  directly.
- **In-the-money call:** (1.00 − delta) affects the excess value. A deeply ITM
  call with delta = 0.95 has only 0.05 of delta working on its small remaining
  excess value. This is why deeply ITM calls behave like stock — almost all their
  value is intrinsic and almost none is excess.

**The direct relationship between vega and excess value:** If IV increases, excess
value increases. If IV decreases, excess value decreases. The two move together
directly and proportionally.

---

## 3. How Vega Changes With Stock Price

**Table 37-1** — Stock price varies; IV held at 70%, time 3 months, strike 50:

| Stock Price | July 50 Call Price | Vega |
|---|---|---|
| 30 | 0.47 | 0.028 |
| 40 | 2.62 | 0.073 |
| 50 | 7.25 | 0.098 |
| 60 | 14.07 | 0.092 |
| 70 | 22.35 | 0.091 |

Vega is highest at-the-money and drops as the stock moves away from the strike in
either direction — though it drops more sharply on the downside.

**The real-world panic offset:** In practice, when the underlying drops quickly in
a panic, implied volatility typically increases dramatically at the same time. This IV
spike may be of great benefit to a call holder, partially or fully mitigating losses that
the theoretical vega table — which assumes static IV — would not show. The
combination of falling stock and rising IV is one of the most important real-world
dynamics for an options holder to understand.

---

## 4. How Vega Changes With Time Remaining

**Table 37-2** — Time varies; stock at 50, strike 50, IV 70%, rates 5%:

| Time Remaining | Call Price | Vega |
|---|---|---|
| One year | 14.60 | 0.182 |
| Six months | 10.32 | 0.135 |
| Three months | 7.25 | 0.098 |
| Two months | 5.87 | 0.080 |
| One month | 4.16 | 0.058 |
| Two weeks | 2.87 | 0.039 |
| One week | 1.96 | 0.028 |
| One day | 0.73 | 0.010 |

Vega decreases as time shrinks. A very short-term option cannot benefit much from
an increase in IV; a long-term option can benefit substantially.

> **Annotation:** The one-year option has a vega of 0.182 — nearly double the
> three-month option's 0.098, and more than six times the one-week option's 0.028.
> Buying longer-dated options gives the position substantially more sensitivity to any
> IV expansion that accompanies the stock move. Every week of time lost is a week of
> vega shrinkage that cannot be recovered.

---

## 5. Vega Is Stable Across a Wide Range of IV Levels

**Table 37-3** — IV varies; stock at 50, strike 50, three months, rates 5%:

| Implied Volatility | Call Price | Vega |
|---|---|---|
| 10% | 1.34 | 0.097 |
| 30% | 3.31 | 0.099 |
| 50% | 5.28 | 0.099 |
| 70% | 7.25 | 0.098 |
| 100% | 10.16 | 0.096 |
| 150% | 14.90 | 0.093 |
| 200% | 19.41 | 0.088 |

Vega is surprisingly constant over a wide range of implied volatilities. It begins to
decline only when IV becomes extremely high — a relatively rare occurrence.

**Practical implication:** Vega is a portable, reliable comparison tool across names at
very different IV levels. When screening calls on stocks with different IVs, the vega
sensitivity per percentage point of IV movement is roughly comparable for at-the-money
options at the same expiration, regardless of current IV regime.

---

## 6. The Cost of Buying Into a High-IV Environment

At very high implied volatility, the delta of an option becomes surprisingly stable
across a wide range of stock prices. A 6-month at-the-money call at 170% IV has a
delta of approximately 0.70 whether the stock is at 80 or 150. This means:

1. OTM options with extremely high IV have high deltas and mirror stock
   movements more closely than expected.
2. A change in IV (vega effect) can produce a significant change in delta —
   the two are not independent.

**The 9-point stock move offset example:** If implied volatility drops from 170% to
140% while the stock is unchanged, the call loses a measurable amount of value. To
compensate for that IV decline and keep the call's value constant, the stock must rise
approximately 9 points. The stock rose 9 points and the call holder made nothing —
because IV fell 30 percentage points simultaneously.

This runs in reverse for the low-IV buyer: IV expansion while the stock rises means
both forces work simultaneously in the position's favor.

---

## 7. IV Can Overcome Time Decay — With Concrete Numbers

An increase in IV can overcome days, even weeks, of time decay.

**Table 37-4. IV required to maintain call value over time:**

| Initial Implied Volatility | IV Required After One Month | IV Required After Two Months |
|---|---|---|
| 20% | 26% | 38% |
| 80% | 99% | 141% |

*Setup: ATM call, 3-month initial life, stock unchanged throughout.*

For the 20% IV starting case: maintaining the call's value after one month requires
IV to rise from 20% to 26% — a 30% relative increase that happens routinely. Many
stocks have IVs that fluctuate in the 20%–40% range easily.

For the 80% IV starting case: maintaining the call's value after one month requires
IV to rise from 80% to 99% — followed by a further rise to 141% in month two. These
are crisis-level IV readings that are rare and unsustainable.

For a 12-month option starting at 20% IV: maintaining value over six months requires
only a rise from 20% to 27% — an ordinary move.

> **Annotation:** Table 37-4 is a direct entry decision tool. At low IV entry, time
> decay is not the primary enemy it is often portrayed to be — ordinary IV normalization
> offsets it. At high IV entry, offsetting time decay requires extraordinary IV expansion
> that is rare and requires a crisis. The entry point in the IV cycle is not a style
> preference; it determines whether time is working for or against the position.

---

## 8. Low IV Entry Provides a Built-In Crash Cushion

**Table 37-5** — How much IV must rise when the stock price falls, for the call to
maintain its initial value of 4.64 (3-month ATM call, stock at 100, IV at 20%):

| Stock Price | IV Required to Maintain Call Value |
|---|---|
| 100 | 20% |
| 95 | 33% |
| 90 | 44% |
| 85 | 55% |
| 80 | 67% |
| 75 | 78% |
| 70 | 89% |

Even if the stock drops 20 points in one day, if IV simultaneously rises from 20% to
67%, the call's value is unchanged. This is not purely theoretical: in the Crash of 1987,
the market dropped 22% in one day while the VIX rose from approximately 36% to 150%.
Some OEX call buyers at low IV actually broke even or made a small profit despite the
worst single-day market decline on record.

Buying calls when IV is low builds in structural crash protection that is absent when
buying at high IV. In a crash, IV spikes — that spike directly benefits the long call
holder. The same spike devastates the position that was entered at high IV, because
the crash causes the stock to fall AND the option to decay simultaneously from its
already-elevated IV level.

---

## 9. "Time Value Premium" Is a Misnomer — Volatility and Stock Movement Dominate

**Worked example showing the daily hierarchy:**

XYZ at 82 in late November; January 80 call at 8; intrinsic value 2; excess value 6;
IV just over 50%.

Greeks at 3+ months remaining:

| Greek | Value | Daily Impact |
|---|---|---|
| Delta | 0.60 | Primary driver of excess value change |
| Vega | 0.13 | Secondary driver — 13 cents per 1% IV move |
| Theta | −0.06 | Only 6 cents per day |

Same call with only one week remaining (IV would be 155%):

| Greek | Value | Daily Impact |
|---|---|---|
| Delta | 0.59 | Still primary |
| Vega | 0.044 | Only 4.4 cents per 1% IV move |
| Theta | −0.51 | 51 cents per day — now dominant |

"In fact, all of this calls into question just exactly what *time value premium* is. That
part of an option's value that is not intrinsic value is really affected much more by
volatility than it is by time decay, yet it carries the term 'time value premium.'"

At 3+ months remaining: theta = 0.06/day, vega = 0.13. Time decay is minor; a 1%
IV move has more than double the daily effect of time passage.

At one week remaining: theta = 0.51/day, vega = 0.044. The relationship inverts
entirely.

**Conclusion:** The "excess value" paid for a longer-dated option is predominantly
volatility value. Volatility value can be recovered or amplified if IV expands. Only
near expiration does excess value become unrecoverable time value.

---

## 10. Put TVP Formula and the ITM Put / IV Interaction

**Put TVP formula:**

> Put TVP = Put price − Strike price + Stock price

Equivalently: the time value premium of an in-the-money put equals the price of
the corresponding out-of-the-money call, plus dividends to be earned until expiration,
less carrying costs over that period.

**The ITM put and IV — a specific non-obvious rule:**

An increase in IV increases the value of a call directly. For a put, the same is true
when the put is at-the-money or slightly in-the-money. However, for a deeply ITM
put, IV must increase enough to push the put's value above parity — above the level
at which carrying costs would make arbitrageurs exercise. Until that threshold is
crossed, the deeply ITM put remains at parity and the short put remains at risk of
early assignment, regardless of IV changes.

**Implication:** A put can be assigned well in advance of expiration — even a LEAPS
put — as soon as there is no time value premium left. An increase in IV helps the
deeply ITM put only if the increase is large enough to overcome the carrying costs
and push the put above parity. A modest IV increase will not move a deeply ITM put
at all.

---

## 11. Call Bull Spreads Have Negative Position Vega — An IV Spike Hurts Them

**The counterintuitive result:** If the stock is unchanged and IV increases
dramatically, a call bull spread loses value. The spread shrinks when IV rises;
it expands when IV falls.

**Why:** In a call bull spread, the long call has higher vega than the short call
(the long call has more time value to expand). But because the short call is sold,
its vega is negative in the position. The net position vega = long call vega − short
call vega = a small negative number. IV up = spread worth less.

**Table 37-6. 90–110 call bull spread, stock at 100, 4 months remaining:**

| Implied Volatility | Spread Value | Position Vega |
|---|---|---|
| 20% | 10.54 | −0.67 |
| 30% | 9.97 | −0.48 |
| 40% | 9.54 | −0.38 |
| 50% | 9.18 | −0.33 |
| 60% | 8.87 | −0.30 |
| 70% | 8.58 | −0.28 |
| 80% | 8.30 | −0.26 |

**The slow-widening problem at high IV:** On a volatile stock, a 4-month bull spread
will not expand much during the first month even if the stock makes a substantial move.
If the stock rose from 100 to 130 in 30 days, any reasonable 4-month call purchase
would make a substantial profit. The bull spread would barely eke out a 5-point gain.

**The fundamental incompatibility with the catalyst thesis:**

The call purchase and the bull spread have opposite position vegas. A rise in IV helps
the call purchase and harms the bull spread. They are not similar positions. When a
thesis resolves quickly and violently — the scenario where the investor's fundamental
work pays off most rapidly — the call purchase captures the IV spike as a bonus; the
bull spread is hurt by it.

"High or increasing implied volatility is not a friend of the bull spread, while it is a
friendly ally of the outright call purchase."

> **Annotation:** The value investor whose thesis involves a catalyst that resolves
> quickly should not use a bull spread. Bull spreads are structurally appropriate when
> IV is already high and expected to fall — the opposite of the low-IV entry conditions
> this playbook targets. If the playbook's master entry rule is followed (buy when IV is
> low), the call purchase is almost always the correct vehicle over the bull spread.

---

## 12. When Bull Spreads Are Appropriate: Two Mitigations and the Better Alternative

**Mitigation 1 — Widen the strikes:** Wide strikes give the spread more room to
expand even before expiration, partially offsetting the slow-widening problem. The
spread still has negative position vega, but wider strikes reduce how tightly the two
legs offset each other on an absolute price change basis.

**Mitigation 2 — Both strikes OTM:** If both strikes are out-of-the-money, a strong
rally produces a greater percentage gain. The spread is still negative vega but is
positioned for a larger absolute move.

**The better alternative when the call is overpriced: the "bullish spread"**

Rather than using a call bull spread to reduce the cost of an expensive call, buy the
call and simultaneously sell an OTM put credit spread (bull put spread). This reduces
the call's net cost while preserving the call's positive vega:

**Worked example:** XYZ at 100; July 100 call at 10 (IV = 59%, near the top of the
40%–60% historical range).

| Position | Price |
|---|---|
| Buy 1 July 100 call | 10 |
| Buy 1 July 80 put | 2 |
| Sell 1 July 90 put | 5 |
| **Net debit** | **7 points** |

The long call dominates the position's vega — the IV benefit is preserved. The short
put spread adds a small negative vega component but reduces net premium paid by
3 points.

**Risk profile:**
- Maximum risk = 17 points if XYZ is below 80 at expiration (vs. 10 points for
  the outright call).
- Below 87 at expiration: combined position has a loss of 10 points — same as
  the outright call. Above 87: the combined position has less risk than the call.
- After 30 days: combined position outperforms the outright call if XYZ is above
  approximately 95.

**Rate of return caveat:** The outright call requires $1,000. The bullish spread
requires $1,700 ($1,000 for the call plus $700 for the put spread margin). The rate
of return may favor the outright call purchase depending on how far the stock rallies.

**Precondition:** A downside stop must be used. The structure introduces additional
downside risk below the short put's strike — without a stop, the maximum loss of
17 points substantially exceeds the call-only loss of 10 points.

> **Annotation:** The bullish spread is specifically appropriate when IV is near the
> top of its historical range and the investor wants call exposure but is unwilling to
> pay full elevated premium. It is not appropriate when IV is at or near the low end
> of its range — in that environment, simply buy the call. The rate of return caveat is
> real: size both positions at the same dollar risk before comparing, not at the same
> number of contracts.

---

## 13. Put Credit Spreads (Bull Put Spreads): IV Behavior and the Early Assignment Trap

A put credit spread (sell higher-strike put, buy lower-strike put) also has negative
position vega — it makes money when IV decreases and loses money when IV increases.

**Table 37-8. Stock at 100, sell 110 put, buy 90 put, 4 months remaining:**

| Implied Volatility | Put Bull Spread Value |
|---|---|
| 20% | 9.15 cr* |
| 30% | 9.70 cr |
| 40% | 10.12 cr |
| 50% | 10.46 cr |
| 60% | 10.78 cr |
| 70% | 11.05 cr |
| 80% | 11.33 cr |

*\*Short option trading at parity — immediate assignment risk*

**The early assignment trap:**

If the stock falls and IV falls simultaneously, the short ITM put approaches parity
and assignment risk materializes. After assignment, the investor is left with only the
long side of the spread — and if the underlying then moves sharply in the other
direction, the loss can exceed the original defined maximum risk of the spread.

**The double whammy for OTM put credit spreads in a crash:** Even when both puts
are OTM at establishment, a rapid stock decline drives the underlying toward the
strike while simultaneously spiking IV — expanding the spread's value at the same
moment the short seller wants it to stay narrow. Both the underlying move and the
IV move work against the position simultaneously.

**The lesson:** If using a bull spread where at least one option is at- or in-the-money,
a call bull spread is superior to a put bull spread — early assignment is not a
meaningful risk for call spreads. For OTM put credit spreads, the double whammy
risk in a crash is real and must be acknowledged even if the strikes appear safely
distant at entry.

---

## 14. Calendar Spreads Are a "Long Volatility" Play — Not a Time Decay Play

A calendar spread — buy the longer-term option, sell the shorter-term option at the
same strike — has positive position vega. It benefits from IV increases and is harmed
by IV decreases.

**Worked example:** XYZ at 100. Buy August (5-month) 100 call; sell May (2-month)
100 call. IV at 40%.

| Option | Price | Vega |
|---|---|---|
| Short May 100 call | 6.91 | 0.162 |
| Long August 100 call | 11.22 | 0.251 |
| **Spread** | **4.31** | **+0.089** |

Positive position vega of 0.089 means the spread widens when IV rises.

**Table — spread value one week after establishment (stock still at 100):**

| Implied Volatility | Spread Value |
|---|---|
| 20% | 2.58 |
| 30% | 3.52 |
| 40% | 4.46 |
| 50% | 5.40 |
| 60% | 6.33 |
| 80% | 8.16 |
| 100% | 12.92 |

With IV unchanged at 40%, one week's time decay produces only a 0.15 widening
(4.31 to 4.46). An IV expansion from 40% to 80% produces a 3.85 widening in the
same week. IV is the dominant force; time decay is minor in comparison.

**The common mistake — buying a calendar at high IV:**

If IV is already at 80% when the calendar is established, and IV then mean-reverts
to 40% by the time the short option expires, the spread has made nearly nothing
despite the stock ending exactly at the strike. The spread was entered as a long-vega
position at the worst possible time — IV was about to fall.

**The correct framing:** A calendar spread is a long-volatility play. Evaluate it the
same way as a long call: buy when IV is at the low end of its historical range. A
calendar spread on a stock at low IV that is expected to experience a catalyst is
structurally attractive — it is long vega and directly benefits from the IV expansion
that accompanies catalyst resolution.

> **Annotation:** The same IV entry criterion that governs call purchases governs
> calendar spreads. Both are positive position vega strategies and both are harmed
> by buying into elevated IV. The calendar spread moving from 2.58 to 12.92 as IV
> moves from 20% to 100% illustrates the magnitude of the IV tailwind when entry
> conditions are correct. The calendar spread's advantage over the outright call in
> this context: it costs less (the short near-term option reduces the net premium) and
> the positive vega is somewhat smaller, so the position is less sensitive to IV
> reversals if the thesis takes longer than expected to play out.

---

## 15. Summary: IV Sensitivity Across the Playbook's Core Strategies

| Strategy | Position Vega | IV Rises | IV Falls | Best Entry Condition |
|---|---|---|---|---|
| Long call | Positive | Profits | Hurts | Low IV |
| Long put (protective) | Positive | Profits | Hurts | Low IV |
| Bull call spread | Negative | Hurts | Profits | High IV expected to fall |
| Bull put spread (credit) | Negative | Hurts | Profits | High IV expected to fall |
| Calendar spread | Positive | Profits | Hurts | Low IV |
| Covered call (short call) | Negative | Hurts | Profits | High IV |

"Volatility and the price of the underlying are the two major components affecting
profitability for most option positions. Time decay is only most pertinent as expiration
approaches. Yet, many traders concentrate greatly on potential price movements of the
underlying, often while ignoring what changes in implied volatility could do."

The practical discipline: before establishing any position, compute the position vega.
If an adverse IV move would be harmful and current IV is already low relative to
historical norms, the risk is real and the position should be reconsidered or adjusted.

# USER NOTES:
- Technically speaking, the term that one uses to quantify the impact of volatility changes on the price of an option is called the vega of the option.
- Simply stated, vega is the amount by which an option’s price changes when volatility changes by one percentage point.
- Example: XYZ is selling at 50, and the July 50 call is trading at 7.25. Assume that there is no dividend, that short-term interest rates are 5%, and that July expiration is exactly three months away. With this information, one can determine that the implied volatility of the July 50 call is 70%. That’s a fairly high number, so one can surmise that XYZ is a volatile stock. What would the option price be if implied volatility were to rise to 71%? Using a model, one can determine that the July 50 call would theoretically be worth 7.35 if that happened. Hence, the vega of this option is 0.10 (to two decimal places). That is, the option price increased by 10 cents, from 7.25 to 7.35, when volatility rose by one percentage point. (Note that “percentage point” here means a full point increase in volatility, from 70% to 71%.)
- This example points out an interesting and important aspect of how volatility affects a call option: If implied volatility increases, the price of the option will increase, and if implied volatility decreases, the price of the option will decrease. Thus, there is a direct relationship between an option’s price and its implied volatility.
- It is interesting to note, though, that in the real world, when the underlying drops in price—especially if it does so quickly, in a panic mode—implied volatility can increase dramatically. Such an increase may be of great benefit to a call holder, serving to mitigate his losses, perhaps.
- Figure 37-1 shows another rather unusual effect: When implied volatility gets very high, the delta of the option doesn’t change much.
- Among other things, this means that an out-of-the-money option that has extremely high implied volatility has a fairly high delta—and can be expected to mirror stock price movements more closely than one might think, were he not privy to the delta.
- That data is interesting enough by itself, but it becomes even more thought-provoking when one considers that a change in the implied volatility of his option (vega) also can mean a significant change in the delta of the option.
- As can be done with delta or with any other of the partial derivatives of the model, one can compute a position vega—the vega of an entire position, The position vega is determined by multiplying the individual option vegas by the quantity of options bought or sold. The “position vega” is merely the quantity of options held, times the vega, times the shares per options (which is normally 100).
- For example, suppose that one identifies expensive options, and he figures that implied volatility will decrease, eventually becoming more in line with its historical norms. Then he would want to construct a position with a negative position vega. A negative position vega indicates that the position will profit if implied volatility decreases. Conversely, a buyer of volatility—one who identifies some underpriced situation—would want to construct a position with a positive position vega, for such a position will profit if implied volatility rises. In either case, other factors such as delta, time to expiration, and so forth will have an effect on the position’s actual dollar profit, but the concept of position vega is still important to a volatility trader.
- An explosion in implied volatility is a boon to an option owner, but can be a devastating detriment to an option seller, especially a naked option seller.
- One should understand the notion that an increase in implied volatility can overcome days, even weeks, of time decay.
- What makes the top line of Table 37-4 appear more likely than the bottom line is merely the fact that an experienced option trader knows that many stocks have implied volatilities that can fluctuate in the 20% to 40% range quite easily. However, there are far fewer stocks that have implied volatilities in the higher range. In fact, until the Internet stocks got hot in the latter portion of the 1990s, the only ones with volatilities like those were very low-priced, extremely volatile stocks.
- Finally, it was mentioned earlier that implied volatility often explodes during a market crash. In fact, one could determine just how much of an increase in implied volatility would be necessary in a market crash in order to maintain the call’s value.
- If nothing else, these examples should impart to the reader how important it is to be aware of implied volatility at the time an option position is established. If you are buying options, and you buy them when implied volatility is “low,” you stand to benefit if implied volatility merely returns to “normal” levels while you hold the position. Of course, having the underlying increase in price is also important.
- In a similar manner, a decrease in implied volatility can be just as important. Thus, if the call buyer purchases options that are “too costly,’ ones in which implied volatility is “too high,” then he could lose money even if the underlying makes a modest move in his favor.
- Many (perhaps novice) option traders seem to think of time as the main antagonist to an option buyer. However, when one really thinks about it, he should realize that the portion of an option that is not intrinsic value is really much more related to stock price movement and/or volatility than anything else, at least in the short term.
- An option’s price is composed of two parts: (1) intrinsic value, which is the “real” part of the option’s value—the distance by which the option is in-the-money, and (2) “excess value”—often called time value premium. There are actually five factors that affect the “excess value” portion of an option. Eventually, time will dominate them all, but the longer the life of the option, the more the other factors influence the “excess value.” The five factors influencing excess value are: l. stock price movements, 2. changes in implied volatility, 3. the passage of time, 4. changes in the dividend (if any exist), and 5 changes in interest rates. Each is stated in terms of a movement or change; that is, these are not static things. In fact, to measure them one uses the “greeks”: delta, vega, theta (there is no “greek” for dividend change), and rho. Typically, the effect of a change in dividend or a change in interest rate is small (although a large dividend change or an interest rate change on a very long-term option can produce visible changes in the prices of options). If everything remains static, then time decay will eventually wipe out all of the excess value of an option. That’s why it’s called time value premium. But things don’t ever remain static, and on a daily basis, time decay is small, so it is the remaining two factors that are most important.
- From the above figures, one can see—and this should be intuitively appealing—that the biggest factor influencing the price of the option is stock price movement (delta). It’s a little unfair to say that, because it’s conceivable (although unlikely) that volatility could jump by a large enough margin to become a greater factor than delta for one day’s move in the option. Furthermore, since this option is composed mostly of excess value, these more dominant forces influence the excess value more than time decay does. There is a direct relationship between vega and excess value. That is, if implied volatility increases, the excess value portion of the option will increase and, if implied volatility decreases, so will excess value. The relationship between delta and excess value is not so straightforward. The farther the stock moves away from the strike, the more this will have the effect of shrinking the excess value. If the call is in-the-money (as in the above example), then an increase in stock price will result in a decrease of excess value. That is, a deeply in-the-money option is composed primarily of intrinsic value, while excess value is quite small. However, when the call is out-of-the-money, the effect is just the opposite: Then, an increase in call price will result in an increase in excess value, because the stock price increase is bringing the stock closer to the option’s striking price. For some readers, the following may help to conceptualize this concept. The part of the delta that addresses excess value is this: Out-of-the-money call: 100% of the delta affects the excess value. In-the-money call: “1.00 minus delta” affects the excess value. (So, if a call is very deeply in-the-money and has a delta of 0.95, then the delta only has 1.00—0.95, or 0.05, room to increase. Hence it has little effect on what small amount of excess value remains in this deeply in-the-money call.)
- 


# Chapter 37 — How Volatility Affects Popular Strategies: Extracted Insights for the Conservative Options Playbook

---

## 1. Vega Defined: The Price Change Per One Percentage Point of IV Movement

"Simply stated, vega is the amount by which an option's price changes when volatility
changes by one percentage point."

**Worked example — call:**

XYZ is selling at 50, and the July 50 call is trading at 7.25. No dividend, short-term
interest rates 5%, July expiration exactly three months away. The implied volatility of the
July 50 call is 70%.

"What would the option price be if implied volatility were to rise to 71%? Using a
model, one can determine that the July 50 call would theoretically be worth 7.35 if that
happened. Hence, the vega of this option is 0.10 (to two decimal places). That is, the
option price increased by 10 cents, from 7.25 to 7.35, when volatility rose by one
percentage point."

The same call at 69% IV would be worth 7.15 — again a 0.10 change, this time a
decrease.

"This example points out an interesting and important aspect of how volatility affects
a call option: *If implied volatility increases, the price of the option will increase, and if
implied volatility decreases, the price of the option will decrease.* Thus, there is a direct
relationship between an option's price and its implied volatility."

**Worked example — put (same terms):**

| Stock Price | July 50 call | July 50 put | Implied Volatility | Put's Vega |
|---|---|---|---|---|
| 50 | 7.15 | 6.54 | 69% | 0.10 |
| 50 | 7.25 | 6.64 | 70% | 0.10 |
| 50 | 7.35 | 6.74 | 71% | 0.10 |

"In fact, it can be stated that a call and a put with the same terms have the same
vega. To prove this, one need only refer to the arbitrage equation for a conversion. If the
call increases in price and everything else remains equal—interest rates, stock price, and
striking price—then the put price must increase by the same amount."

> **Annotation:** The symmetry of vega between calls and puts matters for the investor
> who uses both — a long call for upside leverage and a long put for downside protection
> are equally sensitive to IV changes per dollar of vega. Both benefit from buying when IV
> is depressed.

---

## 2. How Vega Changes With Stock Price

**Table 37-1** — Stock price varies; IV held at 70%, time at 3 months, strike at 50:

| Stock Price | July 50 Call Price | Vega |
|---|---|---|
| 30 | 0.47 | 0.028 |
| 40 | 2.62 | 0.073 |
| 50 | 7.25 | 0.098 |
| 60 | 14.07 | 0.092 |
| 70 | 22.35 | 0.091 |

"In these cases, vega drops when the stock price does, too, but it remains fairly
constant if the stock rises. It is interesting to note, though, that in the real world, when
the underlying drops in price—especially if it does so quickly, in a panic mode—implied
volatility can increase dramatically. Such an increase may be of great benefit to a call
holder, serving to mitigate his losses, perhaps."

> **Annotation:** The vega collapse at low stock prices (0.028 when stock is at 30 vs.
> 0.098 at-the-money) means that deep out-of-the-money calls offer diminishing sensitivity
> to any subsequent IV expansion. The table is theoretical and assumes static IV; the
> real-world consolation McMillan notes — panic drops tend to spike IV simultaneously —
> partially offsets this for the call holder in practice.

---

## 3. How Vega Changes With Time Remaining

**Table 37-2** — Time varies; stock at 50, strike at 50, IV at 70%, rate at 5%:

| Time Remaining | Theoretical Call Price | Vega |
|---|---|---|
| One year | 14.60 | 0.182 |
| Six months | 10.32 | 0.135 |
| Three months | 7.25 | 0.098 |
| Two months | 5.87 | 0.080 |
| One month | 4.16 | 0.058 |
| Two weeks | 2.87 | 0.039 |
| One week | 1.96 | 0.028 |
| One day | 0.73 | 0.010 |

"Table 37-2 clearly shows that the passage of time results not only in a decreasing
call price, but in a decreasing vega as well. This makes sense, of course, since one cannot
expect an increase in implied volatility to have much of an effect on a very short-term
option—certainly not to the extent that it would affect a LEAPS option."

> **Annotation:** This table is one of the most practically useful in the chapter for a
> value investor with a 3–12 month thesis. The one-year option has a vega of 0.182 —
> nearly double the three-month option's 0.098, and more than six times the one-week
> option's 0.028. Buying longer-dated options not only gives the thesis more time to play
> out; it also gives the position substantially more sensitivity to any IV expansion that
> accompanies the move. Every week of time lost is a week of vega shrinkage that cannot
> be recovered.

---

## 4. Vega Is Surprisingly Stable Across a Wide Range of IV Levels

**Table 37-3** — IV varies; stock at 50, strike at 50, three months, rate at 5%:

| Implied Volatility | Theoretical Call Price | Vega |
|---|---|---|
| 10% | 1.34 | 0.097 |
| 30% | 3.31 | 0.099 |
| 50% | 5.28 | 0.099 |
| 70% | 7.25 | 0.098 |
| 100% | 10.16 | 0.096 |
| 150% | 14.90 | 0.093 |
| 200% | 19.41 | 0.088 |

"Thus, Table 37-3 shows that vega is surprisingly constant over a wide range of
implied volatilities. That's the real reason why no one bothers with 'vega of the vega.'
Vega begins to decline only if implied volatility gets exceedingly high, and implied
volatilities of that magnitude are relatively rare."

> **Annotation:** When screening calls across names at very different IV levels, vega as
> a sensitivity measure is roughly comparable for at-the-money options at the same
> expiration. The dollar price difference between a 10% IV call and a 70% IV call is large,
> but the sensitivity per percentage point of IV movement is nearly identical. Vega is a
> portable, reliable comparison tool across names regardless of current IV regime.

---

## 5. The Cost of Buying Into a High-IV Environment: How Much Must the Stock Rise Just to Break Even on IV

Figure 37-1 shows the theoretical price of a 6-month call at differing implied
volatilities. McMillan uses it to pose a direct question: if you buy an at-the-money call
(stock price = 100) when implied volatility is 170%, and then implied volatility drops to
140%, how much must the stock rise just to keep the option's value constant?

"The horizontal line from point A to point B shows that the option value is the same
on each line. Then, dropping a vertical line from B down to point C, we see that point C
is at a stock price of about 109. Thus, the stock would have to rise 9 points just to keep
the option value constant, *if implied volatility drops from 170% to 140%.*"

The same chart shows a second property: "When implied volatility gets very high, the
delta of the option doesn't change much… the delta (which is the slope) *barely changes
for such an expensive option—whether the stock is trading at 60 or it's trading at 150!*
That fact alone is usually surprising to many."

"In addition, the value of this delta can be measured: It's 0.70 or higher from a stock
price of 80 all the way up to 150. Among other things, this means that an out-of-the-money
option that has extremely high implied volatility has a fairly high delta—and can be
expected to mirror stock price movements more closely than one might think."

"That data is interesting enough by itself, but it becomes even more thought-provoking
when one considers that a change in the implied volatility of his option (vega) also can
mean a significant change in the delta of the option. In one sense, it explains why, in the
first chart (Figure 37-1), the stock could rise 9 points and yet the option holder made
nothing, because implied volatility declined from 170% to 140%."

> **Annotation:** The 9-point stock move needed to offset a 30-percentage-point IV
> decline (170% → 140%) is the clearest single illustration of the headwind facing a call
> buyer who enters at a high-IV point. For the value investor who enters at low IV, this
> relationship runs in reverse: IV expansion while the stock rises means both forces work
> simultaneously in the position's favor. The high-delta stability at high IV is a secondary
> point worth knowing — very expensive options on volatile stocks track the underlying
> more linearly than the standard convexity of option pricing suggests.

---

## 6. IV Can Overcome Time Decay — The Numbers That Prove It

"One should understand the notion that an increase in implied volatility can overcome
days, even weeks, of time decay."

**Case 1 — Starting IV = 20%:**

| | |
|---|---|
| Stock Price | 100 |
| Strike Price | 100 |
| Time Remaining | 3 months |
| Implied Volatility | 20% |
| Theoretical Call Value | 4.64 |

After one month passes at static IV, the call loses nearly a point to time decay. But
if IV rises to 25.9%, the call holds its value:

| | |
|---|---|
| Stock Price | 100 |
| Strike Price | 100 |
| Time Remaining | 2 months |
| Implied Volatility | 25.9% |
| Theoretical Call Value | 4.64 |

After another month (one month remaining), if IV rises further to 38.1%, the call
still holds its value:

| | |
|---|---|
| Stock Price | 100 |
| Strike Price | 100 |
| Time Remaining | 1 month |
| Implied Volatility | 38.1% |
| Theoretical Call Value | 4.64 |

"So, if implied volatility increases from 20% to 26% over the first month, then this
call option would still be trading at the same price—4.64. That's not an unusual increase
in implied volatility; increases of that magnitude, 20% to 26%, happen all the time. For it
to then increase from 26% to 38% over the next month is probably less likely, but it is
certainly not out of the question."

**Case 2 — Starting IV = 80%:**

| | |
|---|---|
| Stock Price | 100 |
| Strike Price | 100 |
| Time Remaining | 3 months |
| Implied Volatility | 80% |
| Theoretical Call Value | 16.45 |

To maintain 16.45 after one month:

| | |
|---|---|
| Stock Price | 100 |
| Strike Price | 100 |
| Time Remaining | 2 months |
| Implied Volatility | 99.4% |
| Theoretical Call Value | 16.45 |

To maintain 16.45 after two months:

| | |
|---|---|
| Stock Price | 100 |
| Strike Price | 100 |
| Time Remaining | 1 month |
| Implied Volatility | 140.9% |
| Theoretical Call Value | 16.45 |

**Table 37-4. Summary:**

| Initial Implied Volatility | IV Required After One Month | IV Required After Two Months |
|---|---|---|
| 20% | 26% | 38% |
| 80% | 99% | 141% |

"Note that the increase in volatility from 20% to 26% is a 30% increase. That is,
20% times 1.30 equals 26%. That's what's required to maintain the call's value for the
lower volatility over the first month—an increase in the magnitude of implied volatility
of 30%. At the *higher* volatility, though, an increase in magnitude of only about 25% is
required (from 80% to 99%). Thus, in *those* terms, the two appear on more equal footing."

"What makes the top line of Table 37-4 *appear* more likely than the bottom line is
merely the fact that an experienced option trader knows that many stocks have implied
volatilities that can fluctuate in the 20% to 40% range quite easily. However, there are far
fewer stocks that have implied volatilities in the higher range."

For a 12-month option starting at 20% IV: "all it takes to maintain the call's value
over a 6-month time period is an increase in implied volatility to 27%." From the option
seller's perspective: "If you sell a one-year (LEAPS) option and six months pass, during
which time implied volatility increases from 20% to 27%—certainly quite possible—you
will have made nothing!"

> **Annotation:** Table 37-4 is a direct entry decision tool. Starting at 20% IV, only a
> modest and common IV increase (20% → 26%) is needed to offset the first month's time
> decay entirely. Starting at 80% IV, an IV increase from 80% to nearly 141% is needed
> to do the same — an event that requires a crisis or takeover. For the value investor
> targeting depressed, low-IV stocks, time decay is not the primary enemy it is often
> portrayed to be: ordinary IV normalization offsets it. For the investor who buys options
> on high-IV names, time decay requires extraordinary IV expansion to offset — expansion
> that is rare and unsustainable.

---

## 7. Low IV Combined With a Falling Stock: The Call Holder's Built-In Cushion

**Table 37-5** — How much IV must rise when the stock price falls, for the call to maintain
its initial value of 4.64 (3-month call, stock originally at 100, IV originally at 20%,
strike 100):

| Stock Price | Implied Volatility Necessary for Call to Maintain Value |
|---|---|
| 100 | 20% (the initial parameters) |
| 95 | 33% |
| 90 | 44% |
| 85 | 55% |
| 80 | 67% |
| 75 | 78% |
| 70 | 89% |

"Thus, from Table 37-5, one could say that even if the underlying stock dropped 20
points (which is 20% in this case) in one day, yet implied volatility exploded from 20% to
67% at the same time, the call's value would be unchanged! Could such an outrageous
thing happen? It has: In the Crash of '87, the market plummeted 22% in one day, while
the Volatility Index (VIX) theoretically rose from 36% to 150% in one day. In fact, call
buyers of some OEX options actually broke even or made a little money due to the
explosion in implied volatility, despite the fact that the worst market crash in history had
occurred."

"If nothing else, these examples should impart to the reader how important it is to be
aware of implied volatility at the time an option position is established. If you are buying
options, and you buy them when implied volatility is 'low,' you stand to benefit if implied
volatility merely returns to 'normal' levels while you hold the position. Of course, having
the underlying increase in price is also important."

> **Annotation:** Table 37-5 quantifies the crash cushion that low-IV entry provides.
> Crashes are precisely the environments where IV spikes most violently — the same
> mechanism that damages the stock position partially offsets the option's loss. The
> Crash of '87 example is not theoretical; it is a verified historical instance where call
> holders at low IV were protected from the worst single-day market drop on record. The
> value investor buying calls at depressed IV has structural crash protection built in that
> is absent when buying at high IV.

---

## 8. "Time Value Premium" Is a Misnomer — Volatility Dominates Excess Value

"Many (perhaps novice) option traders seem to think of time as the main antagonist
to an option buyer. However, when one really thinks about it, he should realize that the
portion of an option that is not intrinsic value is really much more related to stock price
movement and/or volatility than anything else, at least in the short term."

The five factors influencing excess value are:
1. stock price movements
2. changes in implied volatility
3. the passage of time
4. changes in the dividend (if any exist)
5. changes in interest rates

**Worked example showing the hierarchy:**

XYZ is trading at 82 in late November. The January 80 call is trading at 8. Intrinsic
value is 2 (82 minus 80); excess value is 6 (8 minus 2). Implied volatility is just over 50%.
The call's greeks are:

| Greek | Value |
|---|---|
| Delta | 0.60 |
| Vega | 0.13 |
| Theta | −0.06 |

"This means, for example, that time decay is only 6 cents per day. It would increase
as time went by, but even with a day or so to go, theta would not increase above about 20
cents unless volatility increased or the stock moved closer to the strike price."

McMillan then shows the same January 80 call on the same stock at 82, but with
only **one week remaining** until expiration — IV would then be 155%. The greeks shift
dramatically:

| Greek | Value |
|---|---|
| Delta | 0.59 |
| Vega | 0.044 |
| Theta | −0.51 |

"This very short-term option has about the same delta as its counterpart in the
previous example (the delta of an at-the-money option is generally slightly above 0.50).
Meanwhile, vega has shrunk. The effect of a change in volatility on such a short-term
option is actually about a third of what it was in the previous example. However, time
decay in this example is huge, amounting to half a point per day in this option."

"There is a direct relationship between vega and excess value. That is, if implied
volatility increases, the excess value portion of the option will increase and, if implied
volatility decreases, so will excess value."

"In fact, all of this calls into question just exactly what *time value premium* is. That
part of an option's value that is not intrinsic value is really affected much more by
volatility than it is by time decay, yet it carries the term 'time value premium.'"

> **Annotation:** The direct comparison between the November example (theta =
> −0.06/day, vega = 0.13) and the one-week example (theta = −0.51/day, vega = 0.044)
> shows concretely why expiration selection matters. At 3+ months out, time decay barely
> registers on a daily basis while vega is near its functional maximum. With one week
> remaining, the relationship inverts entirely. The "excess value" paid for a longer-dated
> option is predominantly volatility value — and volatility value can be recovered or
> amplified if IV expands. Only near expiration does excess value become unrecoverable
> time value.

---

## 9. Call Bull Spreads Have Negative Position Vega — An IV Spike Hurts Them

"Ask yourself this simple question: If the stock remains unchanged at 100, and
implied volatility increases dramatically, will the price of the 90–110 call bull spread
grow or shrink? Answer before reading on. The truth is that, if implied volatility
*increases*, the price of the spread will *shrink*."

**Table 37-6 / Table 37-7.** Assumptions: Stock at 100, 4 months to expiration, long
call struck at 90, short call struck at 110:

| Implied Volatility | 90–110 Call Bull Spread (Theoretical Value) | Position Vega |
|---|---|---|
| 20% | 10.54 | −0.67 |
| 30% | 9.97 | −0.48 |
| 40% | 9.54 | −0.38 |
| 50% | 9.18 | −0.33 |
| 60% | 8.87 | −0.30 |
| 70% | 8.58 | −0.28 |
| 80% | 8.30 | −0.26 |

"Since these vegas are all negative, they indicate that the spread will shrink in value
if implied volatility rises and that the spread will expand in value if implied volatility
decreases. Again, these statements may seem contrary to what one would expect from a
bullish call position."

"In a call bull spread, one would subtract the vega of the call that is sold from that
of the call that is bought in order to arrive at the position vega of the call bull spread."

*The high-IV problem for intra-period profit:* "For volatile stocks, one cannot expect
a 4-month bull spread to expand or contract much during the first month of life, even if
the stock makes a substantial move. Longer-term spreads have even less movement."

*Direct comparison — call buy vs. bull spread at IV = 80%, 30 days later:* "if the
stock rose from 100 to 130 in 30 days, *any* reasonable four-month call purchase (i.e.,
with a strike initially near the current stock price) would make a nice profit, while the
bull spread barely ekes out a 5-point gain."

"The bull spread and the call purchase have opposite position vegas, too. That is, a
rise in implied volatility will help the call purchase but will harm the bull spread (and vice
versa). *Thus, the call purchase and the bull spread are not very similar positions at all.*"

"Sound familiar? Every option trader has probably done himself in with this line of
thinking at one time or another. At least, now you know the reason why: High or
increasing implied volatility is not a friend of the bull spread, while it is a friendly ally
of the outright call purchase."

> **Annotation:** The value investor whose thesis involves a catalyst that resolves with a
> quick, violent move should not use a bull spread. A sharp stock move combined with an
> IV spike — which almost always accompanies sudden catalyst resolution — will help the
> outright call and hurt the spread. The spread's appeal (lower upfront cost) becomes a
> trap precisely in the scenario where the fundamental work pays off most rapidly. Bull
> spreads are structurally appropriate only when IV is already high and expected to
> fall — the opposite of the low-IV entry conditions this playbook targets.

---

## 10. When Bull Spreads Are Appropriate: Wide Strikes, or the "Bullish Spread" Alternative

McMillan offers limited remediation for the bull spread:

"If one wants to use the bull spread to effectively reduce the cost of buying an
expensive at-the-money option, then at least make sure the striking prices are quite wide
apart. That will allow for a reasonable amount of price appreciation in the bull spread if
the underlying rises in price. Also, one might want to consider establishing the bull spread
with striking prices that are *both* out-of-the-money. Then, if the stock rallies strongly, a
greater percentage gain can be had by the spreader. Still, though, the facts described
above cannot be overcome; they can only possibly be mitigated by such actions."

A more attractive alternative when the target call is expensive is the **"bullish
spread"** — buying the call and simultaneously selling an out-of-the-money put credit
spread:

"Buy the call and simultaneously sell a credit put spread (bull spread) using slightly
out-of-the-money puts. This strategy reduces the call's net cost and maintains upside
potential (although it increases downside risk, but at least it is still a fixed risk)."

**Worked example:**

XYZ at 100. July 100 calls expire in two months, trading at 10 — IV of 59%, near the
top of the historical range of 40%–60%. "If he buys them now and implied volatility
returns to its median range near 50%, he will suffer from the decrease in implied
volatility."

| Option | Price |
|---|---|
| XYZ | 100 |
| July 100 call | 10 |
| July 90 put | 5 |
| July 80 put | 2 |

The entire bullish position:
- Buy 1 July 100 call at 10
- Buy 1 July 80 put at 2
- Sell 1 July 90 put at 5
- **Net expenditure: 7 point debit (plus commission)**

"First, one can see that the bullish spread position has a total risk of 17 points, if
XYZ is below 80 (the lower striking price of the put spread) at expiration. That, of course,
is more than the 10-point cost of the July 100 call by itself, but if one is using a trading
stop of any sort, he probably would not be at risk for the entire 17 points."

"Note also that the bullish spread position would have a loss of 10 points (the same
as the call) at a price of 87 for the common at expiration. Hence, the combined position
actually has *less* risk than the outright call purchase as long as XYZ is 87 or higher at
expiration."

After 30 days: "the crossover point between the two curves is at about a price of 95.
That is, if XYZ is above 95 in 30 days, the bullish spread position will outperform the
call buy."

Investment comparison: The outright call purchase requires $1,000. The bullish
spread position requires that $1,000 plus $700 for the spread (10-point difference in the
strikes, less the 3-point credit received for selling the spread), a total of $1,700. "Hence,
the *rate of return* might favor the outright call purchase, depending on how far the stock
rallies."

"Overall, the bullish spread position is an attractive alternative to an outright call
purchase, especially when the call is overpriced. The spread does risk a greater amount
of money if the underlying stock should collapse heavily. Still, if one is truly bullish, and
if one employs a reasonably tight downside stop on his entire position, this spread can
perform better than the outright purchase of an overpriced call."

> **Annotation:** The "bullish spread" (long call + short OTM put credit spread) is
> meaningfully different from the plain call bull spread. The long call dominates the
> position's vega and preserves the IV tailwind; the short put spread adds only a small
> negative vega component while reducing the net premium paid. The specific application:
> when a value investor wants call exposure but IV is near the top of its historical range
> (as in McMillan's example with IV at 59% near the 40%–60% ceiling), this structure
> reduces cost without surrendering the IV benefit on the long call. The tradeoff is
> increased total dollar risk if the stock collapses below the short put's strike — which is
> why McMillan specifies a downside stop as a precondition.

---

## 11. Put Credit Spreads (Bull Put Spreads): IV Behavior and the Early Assignment Trap

**Table 37-8.** Stock at 100, sell put at 110 strike, buy put at 90 strike, four months
remaining — a put credit (bull) spread:

| Implied Volatility | 90–110 Put Bull Spread (Theoretical Value) |
|---|---|
| 20% | 9.15 cr* |
| 30% | 9.70 cr |
| 40% | 10.12 cr |
| 50% | 10.46 cr |
| 60% | 10.78 cr |
| 70% | 11.05 cr |
| 80% | 11.33 cr |

*\*Short option trading at parity*

"One would not rationally sell this credit spread if implied volatility were as low as
20%, because at that low level of volatility, the in-the-money December 110 put is trading
for 10 dollars—parity—and thus would immediately be at risk of early assignment. But
one can see that an increase in implied volatility increases the value of the spread. Now,
if one had sold this spread to begin with, he would thus be *losing* money when implied
volatility increased." and conversely, "the put credit spread *makes* money when implied
volatility decreases."

**The early assignment trap in falling-stock scenarios:** "If implied volatility falls and
the stock falls too, the risk of early assignment materializes quickly… After thirty days,
if implied volatility is 30%, the 110 put (the short put) would be trading at parity for
stock prices of 94 and below. Thus, it would be at risk of early assignment."

With cash-settled index options, early assignment creates a specific additional
danger: "one is left with only the long side of the spread. If that option happens to have
substantial value, then there is considerable risk if the underlying should quickly move
higher. In fact, by the time one unwinds the spread, he might actually end up losing more
than his original limited risk amount—all due to the early assignment. (This could happen
if the underlying first plunges in price, placing both options deeply in-the-money, after
which one gets assigned on the short put option, followed by the underlying then
dramatically rising in price.)"

**The lesson:** "If one is considering using bull spreads in which at least one of the
options is at- or in-the-money, then a call bull spread is a superior choice over a put bull
spread. Early assignment is not really a consideration for most call spreads."

"Note that these effects are similar, but much less pronounced, for out-of-the-money
put credit spreads. Still, it should be noted that an increase in implied volatility will harm
an out-of-the-money put credit spread, too. Hence, if the underlying goes into a rapid fall
(crash, plunge), then implied volatility usually increases quickly and dramatically. So an
out-of-the-money credit spreader is hit with the double whammy of expanding implied
volatility and the fact that the underlying is fast approaching the strike price of his
options, thereby expanding the price of the spread."

> **Annotation:** The "double whammy" is the key risk for any strategy that sells put
> credit spreads — including as the cost-reduction component of the "bullish spread"
> structure in Section 10. In that structure the short put spread is OTM and sized to
> reduce premium; the risk McMillan describes is real but manageable if the strikes are
> well out-of-the-money and a stop is in place. For at- or in-the-money put spreads used
> as standalone bullish positions, the lesson is unambiguous: use a call bull spread
> instead, and early assignment risk disappears.

---

## 12. Calendar Spreads Are a "Long Volatility" Play — Misunderstood by Most Traders

"An increase in implied volatility will cause a calendar spread to widen out. Both
options will become more expensive, of course, since the increase in implied volatility
affects both of them, but the *absolute* price change will be greatest in the long-term
option. Therefore, the calendar spread will widen."

**Worked example:**

XYZ at 100. August (5-month) call bought, May (2-month) call sold. Both at-the-money.
Implied volatility at 40%:

| Option | Theoretical Price | Vega |
|---|---|---|
| Sell May 100 call | 6.91 | 0.162 |
| Buy August 100 call | 11.22 | 0.251 |

"In theory, this spread should be worth 4.31—the difference in the theoretical
values. Perhaps more important, it has volatility exposure of 0.089—the difference
between the vega of the long call and that of the short call. Since vega is positive, this
means that an *increase* in implied volatility will be beneficial to the spread. In other
words, one can expect the spread to widen if implied volatility rises, and can expect the
spread to shrink if implied volatility declines."

**Table — theoretical spread value one week after establishment (stock still at 100):**

| Implied Volatility | Theoretical Spread Value |
|---|---|
| 20% | 2.58 |
| 30% | 3.52 |
| 40% | 4.46 |
| 50% | 5.40 |
| 60% | 6.33 |
| 80% | 8.16 |
| 100% | 12.92 |

"From the above data, it is quite obvious that implied volatility levels have a huge
effect on the value of a calendar spread. The actual initial contribution of time decay is
rather small in comparison. For example, note that if volatility remains unchanged at
40%, then the spread will have widened only slightly—to 4.46 from 4.31—after the
passage of one week's time. That is small in comparison to the changes dictated by
volatility expansion or contraction."

**The common mistake — buying a calendar at high IV:**

Stock at 100, IV skyrockets to 80% (perhaps a takeover rumor):

| Call | Theoretical Value |
|---|---|
| May 100 call | 12.55 |
| June 100 call | 16.81 |

Spread is trading at 4.36. Appears attractive. But if the stock is at 100 at May
expiration and IV has returned to its normal 40%, the June 100 call with one month
remaining would be worth only 4.77. "Thus the spread would only have made a profit of
a few cents (4.36 to 4.77), and if the underlying stock were farther from the strike price
at expiration, there would probably be a loss rather than a profit."

"The point to be remembered is that a calendar spread is a 'long volatility' play (and
a reverse calendar spread is just the opposite). Evaluate the position's risk with an eye to
what might happen to implied volatility, and not just to where the stock price might go or
how much time decay there might be in the position."

> **Annotation:** A calendar spread on a stock currently at low IV and expected to
> experience a catalyst is structurally attractive for this playbook: it is long vega and
> directly benefits from the IV expansion that typically accompanies catalyst resolution.
> The spread moving from 2.58 to 12.92 as IV moves from 20% to 100% illustrates the
> magnitude of that potential. The trap McMillan describes — buying a calendar at 80%
> IV hoping the stock drifts to the strike — is the inverse scenario: a long-vega position
> entered when IV is already high and likely to mean-revert down. The IV entry criterion
> established in Chapter 36 for call buying applies equally here.

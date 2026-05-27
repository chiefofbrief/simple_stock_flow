# Reddit Post — r/ValueInvesting

_Drafted: 2026-05-27_

---

**Title:** I built an AI workflow for fundamental analysis. Here's what actually works.

---

I've seen posts here asking whether AI is useful for stock research. The skeptic replies are usually the same: it hallucinates, it's unreliable, it makes up numbers. Those criticisms are valid for the way most people are using it. Prompting ChatGPT for a DCF or asking Claude to summarize an earnings call isn't a workflow. That's outsourcing your thinking.

I've been building something more structured for about a year. Here's what it actually looks like.

**The foundation: codify your investing philosophy first**

This is where most people fail before they even start. If you haven't articulated your own analytical framework in enough detail for a model to follow it, you're going to get generic output. I spent real time writing out my philosophy: what investment types I look for, how I classify candidates, what financial metrics I use and how I interpret them, how I think about margin of safety, how I handle GAAP vs. adjusted figures, what epistemic standards I hold my own analysis to. All of it lives in a file the model reads before doing any work. That file is the difference between a tool that produces boilerplate and one that reasons the way you do.

**The structure**

Sequential phases: Context (sentiment, price/earnings framing, preliminary hypothesis) → Numbers (financial statements and footnotes) → Projection (earnings call analysis, catalyst check) → final synthesis with an expected value conclusion.

**Four things that make it trustworthy:**

**1. Source the data properly.** A setup step fetches everything first: financial statements via APIs, SEC filing extracts, MD&A sections, earnings call transcripts, analyst data. Multiple sources, all pulled into structured local files before analysis begins. The model reads from those files. It never searches during analysis. Citations point at real documents, not training data.

**2. Don't skip the qualitative work.** This is what most AI stock tools can't do. The model reads footnotes, MD&A, and earnings call transcripts the same way it reads financials: flagging accounting policy changes, revenue recognition shifts, non-GAAP definitions, management commentary on guidance. The qualitative layer is where the real signals hide and it's fully integrated into the workflow, not an afterthought.

**3. Force it to cite everything.** Every factual claim is tagged `[CONFIRMED: source]`, `[ESTIMATED: source + derivation]`, or `[INFERRED: source + logic]`. If it can't tag a claim, it removes it. The model can't assert a forward growth rate without labeling it INFERRED and showing the reasoning. This is what eliminates the hallucination problem in practice.

**4. Define the output structure explicitly.** Not "analyze this company" but a precise specification of every section, every question that gets answered, and what format the conclusions take. You decide what data goes in, how it gets analyzed, and exactly what comes out. The model builds the case. You decide what to do with it.

The model builds the case. You decide what to do with it. I read the thesis files and make the final call myself; this is human-in-the-loop research, not automated trading.

Most people haven't done that work. That's the real reason AI doesn't perform for them on this, not the hallucination problem.

Happy to share more on any part of this.

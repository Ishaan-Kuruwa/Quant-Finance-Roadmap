# Calculus (and the Math Around It) for the Quant Roadmap

Where each math topic actually shows up in your projects, in what order to learn it, and where to learn it. Keep this next to your roadmap and project plan.

**The key insight first:** You can *build* almost every project with algebra, probability, and code. Calculus is what turns "I can implement this" into "I understand exactly why every term is here." So learn it in the order that unlocks the most understanding — which happily lines up well with your Calc AB → BC sequence next year.

Topics are grouped into three tiers by when you'll realistically learn them.

---

## Tier 1 — Calculus AB (learn first; most reused)

These are the highest-leverage topics and they're exactly what AB covers, so your class and this roadmap reinforce each other.

**Limits**
- *The foundation.* Everything else (derivatives, integrals, continuity) is built on limits.
- *Where it shows up:* Conceptual bedrock — you won't call it directly, but you can't understand derivatives or integrals without it.

**Derivatives**
- Rates of change; the slope of a function; finding maxima and minima.
- *Where it shows up:* **Optimization** — finding the maximum-Sharpe portfolio (Project 3) and minimizing a loss function in ML (Project 6, gradient descent) are both "set the derivative to zero" problems. Also the foundation for the option **Greeks** (Project 5), which are derivatives of the option price.
- Make sure you nail: the **chain rule**, and the derivatives of **e^x** and **ln(x)** specifically.

**Integrals**
- Accumulation and area under a curve.
- *Where it shows up:* **Probability.** The probability of a continuous outcome is the *area under a probability density curve* — i.e., an integral. This is the bridge from "coin-flip probability" to the continuous distributions underneath Monte Carlo (Project 2) and Black–Scholes (Project 5). The `N(d1)`, `N(d2)` terms in Black–Scholes are integrals of the normal curve.

**Exponential & logarithmic calculus**
- The behavior, derivatives, and integrals of **e^x** and **ln(x)**.
- *Where it shows up:* **Continuous compounding** (the `e^(-rT)` discount factor in Project 5), **log returns** (Project 1), and the exponential in Geometric Brownian Motion (Project 2).

**Resources for Tier 1:**
- **Khan Academy — AP Calculus AB.** Free, aligned to your class, perfect for learning alongside school. Your main workhorse.
- **3Blue1Brown — "Essence of Calculus"** (YouTube series). Not for procedures — for *intuition*. Watch this to understand what derivatives and integrals really *mean*. Pairs perfectly with Khan Academy's mechanics.
- **Professor Leonard** (YouTube). Full-length, thorough lectures if you like the "sitting in a great class" format.
- **Paul's Online Math Notes.** Excellent free written notes and lots of practice problems.

---

## Tier 2 — Calculus BC (the next layer)

BC extends AB with a few things that matter specifically for finance.

**Improper integrals / integration techniques**
- Integrating over infinite ranges.
- *Where it shows up:* Continuous probability distributions (like the normal) are defined over all real numbers, so their probabilities and expected values are improper integrals. This makes the probability behind Projects 2 and 5 rigorous rather than just simulated.

**Taylor / Maclaurin series**
- Approximating functions with polynomials.
- *Where it shows up:* This is quietly one of the most important ideas for a quant. It's the basis of **delta–gamma approximations** for options, and — importantly — the intuition behind **Itô's lemma** (the source of that 🔜 `-0.5σ²` term in Project 2). Understanding Taylor series is the single best preparation for eventually understanding stochastic calculus.

**Sequences & series (geometric series)**
- Sums of infinite sequences and when they converge.
- *Where it shows up:* The **present value of a stream of cash flows** (and the formula for a perpetuity) is a geometric series. Directly relevant to the "time value of money" concept in the main roadmap.

**Resources for Tier 2:**
- **Khan Academy — AP Calculus BC.** Continues seamlessly from AB.
- **3Blue1Brown — "Taylor series"** video specifically. One of the best explanations of the idea anywhere; watch it a couple of times.
- **Paul's Online Math Notes** again for series practice.

---

## Tier 3 — Beyond BC (self-study when you're ready)

These go past what you'll cover next year. **Don't rush them** — tackle each one when a specific 🔜 item makes you curious. Learning math to answer a question you already have is far more effective than learning it in the abstract.

**Multivariable calculus** (partial derivatives, gradients, Lagrange multipliers)
- *Where it shows up:* The option **Greeks** are *partial* derivatives (price change per input, holding others fixed). The **closed-form Markowitz solution** (Project 3's 🔜) uses Lagrange multipliers. **Gradient descent** in higher dimensions (Project 6) is multivariable calculus.
- *Resources:* **MIT OpenCourseWare 18.02** (full free course with problem sets); **Khan Academy Multivariable Calculus**; **3Blue1Brown** for gradient/partial-derivative intuition.

**Calculus-based probability** (continuous random variables, PDFs/CDFs, expected value as an integral)
- *Where it shows up:* This is the real bridge between your stats and genuine quant work — it makes Monte Carlo and Black–Scholes rigorous. Arguably the most important item in this tier.
- *Resources:* **Harvard Stat 110 (Joe Blitzstein)** — free lectures on YouTube plus a free textbook, "Introduction to Probability." Famous, beloved, and extremely quant-relevant; a lot of quant hires have worked through it. **MIT OCW 18.05** is a lighter alternative.

**Stochastic calculus** (Brownian motion, Itô's lemma, SDEs) — *the deep end*
- *Where it shows up:* This is what finally explains the `-0.5σ²` term (Project 2) and lets you *derive* Black–Scholes (Project 5). It's genuinely advanced-undergrad / graduate material.
- *Honest advice:* This is a **destination, not a next step.** It needs solid multivariable calculus and calculus-based probability first. Note it as where you're headed; don't dive in during these 3–5 months. The standard text (for much later) is **Shreve, "Stochastic Calculus for Finance," Vols I & II** — bookmark it, don't buy it yet.

---

## The other essential pillar: Linear Algebra

Not calculus, but you asked for "all of this," and quant finance leans on it as heavily as calculus.

- *Where it shows up:* The **covariance matrix** at the heart of Project 3, **regression** (Projects 3 & 6), and later PCA and factor models. Matrices are how quants handle *many assets at once*.
- *Resources:*
  - **3Blue1Brown — "Essence of Linear Algebra."** Start here. The best intuition-builder for the subject, full stop.
  - **MIT OpenCourseWare 18.06 (Gilbert Strang).** The legendary free linear algebra course when you want depth.
  - **Khan Academy Linear Algebra** for mechanics and practice.

You already have enough (matrix operations in NumPy) to *build* Project 3. Learn the theory when you want to understand *why* it works.

---

## A sensible sequence given your timeline

You take AB/BC next year, so here's how to layer it without overload:

1. **Now → next few months (project phase):** You don't *need* new calculus to build the six projects. If you want to get ahead, watch **3Blue1Brown's Essence of Calculus and Essence of Linear Algebra** for intuition — low effort, high payoff, no procedures required.
2. **During Calc AB (next year):** Your class handles Tier 1. Use Khan Academy to stay ahead and reinforce. As each topic lands, revisit the project where it shows up — you'll suddenly understand something you'd only implemented before.
3. **During Calc BC:** Tier 2. Pay special attention to **Taylor series** — it's your on-ramp to the advanced quant math.
4. **After BC / summers:** Pick off Tier 3 in this order — **calculus-based probability (Stat 110)** first, then **multivariable calculus**, then **linear algebra depth**, and only much later **stochastic calculus**. Let the 🔜 items in your projects tell you what to learn next.

---

## The shortest possible resource list

If you want just a few things to start with rather than a menu:

- **Khan Academy** — for learning calculus mechanics alongside your class (Tier 1 & 2).
- **3Blue1Brown** (Essence of Calculus + Essence of Linear Algebra) — for intuition, watch these regardless of anything else.
- **Harvard Stat 110** — when you're ready for real calculus-based probability (the most quant-relevant single resource here).
- **MIT OpenCourseWare** — free full courses (18.02 multivariable, 18.06 linear algebra) for when you want to go deep and do problem sets.

Everything above is free. Search each name plus the topic and you'll find it quickly.

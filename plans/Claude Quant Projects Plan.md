# Your 3–5 Month Quant Project Plan

Built for your exact situation: **strong coder, some ML, precalc done (calculus next year).** Every project below is fully buildable and explainable *right now* without calculus. Where calculus would later deepen your understanding, I've marked it with 🔜 so you know what to revisit after Calc BC.

---

## The core principle: build to explain

Your goal is projects you can *explain thoroughly*. So the rule for this plan is:

> **Every project ships with a written explainer (a README or notebook) where you explain the concept as if teaching a smart friend who doesn't know finance.**

This is the whole game. Writing the explanation is how you find the gaps in your understanding. If you can't write it clearly, you don't understand it yet — and that's useful information, not a failure. This habit is also *exactly* what quant interviews test: not "did you build it" but "can you explain why every piece is there."

**Practical setup:**
- One GitHub repo per project (or one repo with clean subfolders).
- Each has a README explaining the **finance concept**, the **math**, and the **design choices**.
- Use Jupyter notebooks so your explanation, math, code, and charts live together.

---

## What you need to learn alongside (just-in-time, not upfront)

You don't need to front-load a statistics course. Learn each concept *when a project needs it*. Across these projects you'll naturally pick up:

- **Returns** (arithmetic vs. log returns, and why log returns are nicer)
- **Volatility** as the standard deviation of returns, and annualizing with the √time rule
- **Normal & log-normal distributions** and random walks
- **Covariance & correlation** (and matrices as a way to hold them)
- **Sharpe ratio, drawdown, and other performance metrics**
- **The classic mistakes**: look-ahead bias, survivorship bias, overfitting, data leakage

That's most of the probability/statistics backbone of entry-level quant work — learned by using it.

---

## Project 1 — Financial Data & Returns Toolkit
**~1.5 weeks · foundation for everything else**

Build a small library that pulls price data and computes the basic quantities everything else depends on.

**Build:**
- Pull historical prices (the `yfinance` library is free and easy).
- Compute daily **simple returns** and **log returns**.
- Compute **rolling volatility** and **moving averages**.
- Compute a **correlation matrix** across several stocks and plot it as a heatmap.

**To fully explain, master:**
- What a return actually is, and why quants usually prefer **log returns** (they add across time, and they're roughly symmetric).
- Why volatility is just the **standard deviation of returns**, and why we multiply by √252 to annualize (the √time rule — a direct consequence of variance adding over independent periods).
- What correlation means and why it's central to everything later.

**Why it matters:** This is the vocabulary of the field. Get it airtight and every later project is easier.

---

## Project 2 — Monte Carlo Stock Price Simulator
**~2 weeks · your probability showcase**

Simulate thousands of possible future price paths for a stock and analyze the range of outcomes.

**Build:**
- Simulate price paths using **Geometric Brownian Motion** in its discrete form:
  `S_next = S * exp((mu - 0.5*sigma²)*dt + sigma*√dt * Z)`, where `Z` is a standard normal draw.
- Run 10,000+ paths; plot them; build a histogram of final prices.
- Estimate things like "probability the price ends above X."

**To fully explain, master:**
- **Random walks** and why stock prices are often modeled as one.
- The **normal distribution** and where the random `Z` comes from.
- **Drift (`mu`)** vs. **volatility (`sigma`)** — the two forces in the model.
- The **log-normal** shape of the outcome distribution and why prices can't go negative here.

**🔜 Calculus later:** The `-0.5*sigma²` correction term comes from Itô's lemma in stochastic calculus. For now, understand it *empirically* — simulate with and without it and watch what happens to the average. After Calc BC + a stochastic calculus intro, you'll be able to derive exactly why it's there. Being able to say *"I understand what it does and I know the derivation requires tools I'm learning next"* is a completely honest, strong answer.

---

## Project 3 — Portfolio Optimizer (Markowitz)
**~2 weeks · your linear-algebra showcase**

Given several assets, find the mix that gives the best risk-return tradeoff. This is a Nobel-Prize-winning idea and very explainable.

**Build:**
- Compute expected returns and the **covariance matrix** for a set of stocks.
- Generate thousands of **random portfolios**, plot them in risk-vs-return space, and watch the **efficient frontier** appear.
- Find the **maximum-Sharpe-ratio portfolio** (start with the random-search approach; then optionally use `scipy.optimize`).

**To fully explain, master:**
- **Diversification**: why combining imperfectly-correlated assets reduces risk — this is the single most beautiful idea in the project.
- The **covariance matrix** as the object that encodes how assets move together (a great, concrete use of matrices — no proofs needed, just matrix operations in NumPy).
- The **Sharpe ratio** as return per unit of risk.

**🔜 Calculus later:** The *closed-form* solution for the optimal weights uses Lagrange multipliers (multivariable calculus). You don't need it — the random-search and `scipy` approaches give the same answer and are arguably more intuitive. Revisit the analytic version after calculus for a satisfying "oh, that's why" moment.

---

## Project 4 — Backtesting Engine + a Trading Strategy
**~2.5 weeks · the classic quant project**

Build your own engine to test how a trading strategy *would have* performed historically. This is where you learn the rigor that separates real quants from people who fool themselves.

**Build:**
- A backtester that takes a strategy, applies it to historical data, and tracks a simulated portfolio over time.
- Implement a simple strategy (e.g., **moving-average crossover** or **momentum**).
- Report **CAGR, Sharpe ratio, and maximum drawdown**, and plot the equity curve vs. buy-and-hold.
- Add **transaction costs** and watch profits shrink.

**To fully explain, master:**
- **Look-ahead bias**: accidentally using information from the future (e.g., today's closing price to make today's trade). This is the #1 way backtests lie.
- **Overfitting**: tweaking parameters until the backtest looks amazing on past data but fails going forward.
- **Survivorship bias**: testing only on companies that still exist today.
- Performance metrics: what **drawdown** and **Sharpe** actually tell you.

**Why it matters:** Being able to explain *why a strategy that looks like free money is probably a bug* is one of the most impressive things a young quant can demonstrate. This project is where you learn intellectual honesty about markets.

---

## Project 5 — Options Pricer: Black–Scholes vs. Monte Carlo
**~2 weeks · your "two methods that agree" showcase**

Price an option two independent ways and show they converge. Deeply impressive, and fully doable without deriving anything.

**Build:**
- Implement the **Black–Scholes formula** for European call/put prices (it's a plug-in formula — you provide spot, strike, time, interest rate, and volatility).
- Independently price the *same* option with **Monte Carlo**: simulate many price paths (reusing Project 2!), compute each path's payoff, average them, and discount to today.
- Show the two methods agree as the number of simulations grows.
- Plot **payoff diagrams** for calls and puts.

**To fully explain, master:**
- What **options** are: calls, puts, strikes, expiration, and payoff at expiry.
- The **five inputs** to Black–Scholes and, intuitively, how each moves the price (especially volatility).
- The idea of **pricing by expected discounted payoff** — the logic behind the Monte Carlo approach.

**🔜 Calculus later:** *Deriving* Black–Scholes requires stochastic calculus and partial differential equations — genuinely a college-and-beyond topic. Don't fake it. You can *implement it, explain what it does, explain every input, and verify it with an independent method* — which is a strong, honest place to be. Flag the derivation as something you'll appreciate fully after more math. **This is a case where "fully understand" honestly means "understand and can use and verify," not "derive from first principles" — and that's the right expectation for now.**

---

## Project 6 — ML on Markets, Done Honestly
**~2.5 weeks · plays to your ML background**

Use your ML skills — and, more importantly, learn *why markets are brutally hard for ML*. A project that honestly documents "here's why the naive approach fails" is far more impressive than one claiming to beat the market.

**Build:**
- Engineer features from price data (past returns, volatility, moving averages, etc.).
- Train a model to predict next-day direction or return (start with logistic regression or a random forest).
- Evaluate it **honestly** with a **time-respecting split** (train on the past, test on the future — *never* shuffle time-series data) and ideally **walk-forward validation**.

**To fully explain, master:**
- **Data leakage in time series** and why shuffling or standard cross-validation is invalid here — this is the core lesson.
- **Signal-to-noise**: financial returns are mostly noise, so accuracy barely above 50% can still be meaningful (or just luck).
- **Non-stationarity**: market behavior changes over time, so a pattern that worked can vanish.
- Why "it got 95% accuracy" almost always means a bug, not a discovery.

**Why it matters:** This is the single best project for demonstrating maturity. Anyone can call `model.fit()`. Being able to explain *why the obvious approach is a trap* shows you actually understand both ML and markets.

---

## Suggested cadence

Roughly one project every ~2 weeks gets you through all six in about 12 weeks (3 months), leaving buffer within your 3–5 month window to go deeper, add features, or write better explainers.

| Weeks | Project |
|-------|---------|
| 1–2   | Data & Returns Toolkit |
| 3–4   | Monte Carlo Simulator |
| 5–6   | Portfolio Optimizer |
| 7–9   | Backtesting Engine |
| 10–11 | Options Pricer |
| 12–14 | ML on Markets |
| 15+   | Buffer: polish, extend, write blog posts, or combine projects into a portfolio site |

**Dependencies worth noting:** Do them roughly in order — Project 2 (Monte Carlo) feeds directly into Project 5 (options pricing), and Project 1's toolkit gets reused everywhere. Projects 4 and 6 both live off the "avoid fooling yourself" mindset.

---

## How to make these interview-gold (not just "done")

- **Write the explainer before you consider a project finished.** The code isn't the deliverable — your understanding is.
- **Know the failure modes.** For each project, be ready to answer "how could this be wrong?" (look-ahead bias, overfitting, leakage). Naming your own project's weaknesses is a green flag.
- **Verify things two ways** where you can (Project 5 is the model for this). Independent confirmation is what real quant research feels like.
- **Keep a running "what I don't fully understand yet" list.** The 🔜 items go here. Knowing the edge of your knowledge is more impressive than pretending it doesn't exist.

---

## After these 3–5 months

Once Calc AB/BC is under way, circle back to the 🔜 items — the Itô correction term, the Markowitz closed-form, and eventually the Black–Scholes derivation. They'll click, and revisiting your *own* projects with new math is one of the most satisfying ways to learn. That loop — build, hit the edge of your math, learn the math, go deeper — is basically what becoming a quant *is*.

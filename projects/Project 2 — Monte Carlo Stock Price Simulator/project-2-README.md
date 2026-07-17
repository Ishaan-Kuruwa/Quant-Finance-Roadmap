# Project 2 — Monte Carlo Stock Price Simulator

Simulate thousands of possible future price paths for a stock and analyze the range of outcomes.

**Every metric is implemented by hand.**

**Verification target**: The closed-form GBM solution.
E[S_T] = S₀·exp(μT) and median[S_T] = S₀·exp((μ − σ²/2)T)

## What this project is really about**

Understand how to predict stock prices through math and statistics.

- What's the difference between arithmetic drift (μ) and log drift (ν = μ − σ²/2)?
- Where does the −σ²/2 term come from, and why is it there?
- Why is the terminal price distribution log-normal, and why can't prices go negative?
- Why is the median path below the mean path?
- Why is σ estimable but μ essentially not?

## Libraries

- Pandas
- Numpy
- Yfinance
- Matplotlib
- Seaborn

## The concepts
- Random Walks
-     A model that describes a path of random steps, our model to predict stock prices has this as our "volatlity" piece of the GBM Equation.
- GBM discrete form
-     𝑆𝑡+Δ𝑡=𝑆𝑡exp(𝜇−12𝜎2)Δ𝑡+𝜎Δ𝑡√𝑍𝑡
-     We can split the equation up into two pieces, drift and volatility.
- Drift vs. Volatility
-     We are taking the avg returns over a year and annualizing that for drift, and volatility uses the std deviation of the stock's price.
-     Drift is the overall return of the stock, while volatility is the sharp moves.
- The log-normal terminal distribution
-     We can see that the dstribution of prices is skewed right, mean > median because of skew

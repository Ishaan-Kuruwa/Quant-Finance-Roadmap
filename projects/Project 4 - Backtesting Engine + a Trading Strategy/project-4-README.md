
# Project 3 - Portfolio Optimizer (Markowitz)

Build an engine to test how a trading strategy would have performed historically.

**Every metric is implemented by hand.**

**Verification target**: Hand-compute the P&L of a 5-day toy price series with 2 trades on paper.

## What this project is really about**

Understand how actual backtests work, how to compute basic quant metrics like Sharpe ratio, how to make sure backtests don't lie to you and create realistic results.

- What is look-ahead bias, and exactly which line of code introduces it?
- Why does a strategy that looks like free money almost certainly have a bug?
- What's the difference between in-sample and out-of-sample performance?
- Why does max drawdown matter more than Sharpe for whether a strategy is usable?
- How much do transaction costs change the answer?

## Libraries

- Pandas
- Numpy
- Yfinance
- Matplotlib
- Seaborn
- Scipy

## The concepts
- Signal → position → returns pipeline
-     Once you create signals using your desired strategy, you create positions by moving those signals back 1 day, and can then judge your returns based on the positions you have created.
- .Shift(1)
-     This function moves our signals back one day, without it, our strategies would be trading using the prices they have to predict.
- Equity curves
-     Track the cumulative price of a portfolio, multiplying consecutive returns together.
- CAGR
-     The compounded annual growth rate: how much your portfolio grew each year on average.
- Sharpe
-     A metric quants use to quantify how much a portfolio varies for how much return it produces.
- Max drawdown
-     The worst peak to trough loss you had, highest point -> lowest point.
-     May not be a realized loss, but happened.
- Transaction costs
-     How much you are forced to pay for each buy or sell you make with the asset, some strategies that trade frequently have large turnover and large costs without any gains.

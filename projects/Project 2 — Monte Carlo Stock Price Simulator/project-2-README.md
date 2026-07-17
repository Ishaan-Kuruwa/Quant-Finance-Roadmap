# Project 1 — Financial Data & Returns Toolkit

Build small library that pulls data and computes basic quantities

**Every metric is implemented by hand.**

**Verification target**: pandas built-ins (pct_change, rolling, ewm, std, corr)

## What this project is really about**

Understand how to work with financial data and the basic quantities to calculate.

- Why is volatility the std of returns, not prices?
- Why divide by n−1, not n?
- Why annualize with √252, not 252?
- Why do quants use log returns?
- Why does standard deviation require two passes?

## Libraries

- Pandas
- Numpy
- Yfinance
- Matplotlib
- Seaborn

## The concepts

- Returns (Simple & Log) - Finding difference in price today vs price yesterday in percent
-   Simple Returns
-     (pt - p(t-1)) / p(t-1)
-   Log Returns 
-     log (pt/p(t-1))
  
- Rolling Volatility - Finds volatility of a stock over a time period
-     std deviation = sqrt (summation (mean - return)**2 / (n-1))
-     std deviation of returns * sqrt(252) (only for annualization)

- Moving Averages - Finds average price of a stock over a time period
-   Simple Moving Average
-     sum of prices / n
-   Exponential Moving Average
-     Recursive - (a * price(t)) + ((1-a) * price(t-1))
-     a = 2 / n+1
  
- Correlation Matrix
-     cov (x, y) / ox * oy
-     Check out notes for full equation.

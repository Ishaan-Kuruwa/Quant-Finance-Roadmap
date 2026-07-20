# Project 3 - Portfolio Optimizer (Markowitz)

Simulate thousands of possible portfolios for a set of assets and analyze the most optimal weights.

**Every metric is implemented by hand.**

**Verification target**: Two-fold — (a) your nested-loop ΣᵢΣⱼ wᵢwⱼσᵢⱼ must equal the matrix form wᵀΣw; (b) scipy.optimize frontier.

## What this project is really about**

Understand how to use linear algebra to compute the weights for a portfolio, and choose the least variable and most optimized portfolios.

- What is a covariance matrix, and why is it the central object?
- Why is portfolio risk NOT the weighted average of individual risks? (the big one)
- What does the efficient frontier represent? What does "below the frontier" mean?
- What does Sharpe measure, and why maximize it?
- Why do the optimal weights swing so wildly when you shift the date range?

## Libraries

- Pandas
- Numpy
- Yfinance
- Matplotlib
- Seaborn
- Scipy

## The concepts
- Portfolio return as a dot product
-     Calculated by taking the dot product of the weight of an asset and it's mean return and adding it up for each asset.
-     \(E(R_p) = \sum_{i=1}^{n} w_i \times E(R_i)\)
- Portfolio variance as wᵀΣw
-     Calculated by taking the dot product of two assets and their covariance matrix for each pair of assets in the portfolio.
-     𝜎2𝑝=𝑤𝑇⋅Σ * w
- Covariance matrix
-     Calculated by taking the deviations of all pairs of assets and taking the average of this into a nxn grid.
-     \(C=\frac{1}{N-1}\sum _{i=1}^{N}(X_{i}-\={X})(X_{i}-\={X})^{T}\)   
- Efficient frontier
-     Finding the most efficient portfolios based on sharpe ratio and volatility/variance.
- Sharpe maximization
-     Finding the highest sharpe ratio portfolio.
-     Sharpe = (Portfolio return - risk free rate) / (Volatility)
- Min-variance portfolio
-     Finding the portfolio with the least variance.
-     Use calculations of portfolio variance and choose lowest one

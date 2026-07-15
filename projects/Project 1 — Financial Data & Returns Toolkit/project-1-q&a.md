**Target**: Learn how to manipulate and use financial data, and compute basic quantities. Verify findings with built-in functions, understand basic theory behind moving averages, log vs simple returns, standard deviations, and correlation.

**Questions**:
1. What are the differences between simple and log returns?
- Simple returns are taking the price difference between two time periods specifically, while log returns are additive
- Log returns are easier to use because you can add them over time due to the principle:
-     log (a) + log (b) = log (a * b)
- Log returns also have a more symmetrical similar distribution
- Simple returns are better for calculating portfolio returns, but log returns can’t
- Specifically use euler’s number, e, because you can easily take the inverse of it with ln, etc.
- Log returns are also continuous, not discrete like simple returns
2. How do you calculate rolling volatility, why does it work?
- Measures risk and movement of a stock up and down
- Standard deviation of returns over a time period that updates
- Uses standard deviation since this calculates the spread of data and follows a normal distribution
- Standard Deviation - Squared distance of each data point from mean of dataset (Ex: For each number in dataset, (mean - data point) **2, then divide by n-1, and take square root to “undo” squared deviations
- You can annualize rolling volatility by multiplying by sqrt(252), trading days, this is because volatility is the sqrt of variance
- Standard deviation is the square root of variance and variance scales linearly with time, so we also take sqrt(252)

3. How do you calculate simple and exponential moving averages, why does it work?
- Moving averages are like rolling volatility but for a stock’s actual price, we are taking the average stock price over a period of time that updates
- Simple - Each day is weighted equally, Exponential - Days closer to current day are weighted more
- Simple moving average is just sum of stock prices in time divided by n days in the time period, updates when we move forward a day (add that new day, subtract the old one and recompute)
- Exponential moving averages have a recursive equation -
-     (a * price) + (1-a * previous ema), a = 2 / (n + 1)
- Start with the first day price, or a starting sma, and use the equation
- You are weighing each new day as a (alpha) and the rest as the old ema

4. What is a correlation matrix, how do you calculate it, and what does it mean?
- A correlation matrix is a nxn grid of stocks, where each box has the correlation between those assets
- Equation:
-     ρij=∑t=1T(Ri,t−R̄i)(Rj,t−R̄j) / ∑t=1T(Ri,t−R̄i)2
- Close to 1 means the stocks move in a similar direction, 0 means no correlation, -1 means opposite directions
- Calculate numerator by taking the returns and calculating the daily deviations (mean - return) for both stocks, and then multiply those, and sum them at the end
- We see that if both move the same direction we get a positive number, but opposite directions becomes negative number
- Calculate denominator by adding up all of the squares of the deviations for both stocks separately, and then multiplying the two total sums and taking the square root
- We are calculating volatility with the numerator
- We finally divide both to get a number from -1 to 1

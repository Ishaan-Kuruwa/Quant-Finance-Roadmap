**Build small library that pulls data and computes basic quantities**
- **Steps**
  - Pull historical price data
  - Compute daily simple and log returns
  - Compute rolling volatility and moving averages
  - Compute a correlation matrix among several stocks and plot as heat map
- Data - Yfinance (sandp 500)
- **Simple Returns**
-     (pt - p(t-1))/p(t-1)
- **Log Returns**
-     log(pt/pt-1)
- Log returns are lower than simple
- Why Log returns are better:
  - To find total return over multiple days you can just add individual log returns together instead of recomputing with complex returns
  -     Log (a x b) = log a + log b
  - Simple returns have max -100% loss but infinite upside however log returns are more symmetrical since a gain/loss of any percent cancel each other out when added
  - Log returns are continuous (assume continuous compounding)
- Why they are worse:
  - They don’t aggregate across multiple assets and you cannot add the weighted averages of them together.
  -     Log (a + b) =/ log a + log b
  - You can fix this by getting simple returns of assets, then getting weighted avgs to get overall simple return and then converting to log return by taking ln (1 + return)
- All based on log rules
- Use e/ln to undo/redo anything and bc it is very close to acc return
-     (ex: ln(1.02)=0.0198)

- **Moving averages** calculate avg of stock returns over specific amount of time
-     (ex: 20 day sma)
  - Simple - Each day is weighted equally
  - Exponential - Days closer to recent are weighted more
  - Calculate - Take avg of prices in a time frame/window, move forward each time
- **Rolling volatility** is std deviation over period of time
  - Calculate - 
    - Find daily percent returns ((todays price - yesterday price)/yesterday price) x 100
    - Find average of returns in window
    - Subtract avg from each individual return and square results
    - Add them up and divide by n-1 days
    - Take the square root of the result
- Both measure risk and spot trends

- **Correlation Matrix**
  - Calculating the relationship between stocks and how they move
  - 1 = move same way, 0 = no correlation, -1 = move opposite ways
  - Calculate - 
    - Get daily percentage returns
    - Find the average returns for each stock
    - Calculate deviations daily - mean - price on day
    - Calculate top of covariance eqn - multiply daily deviations for each day, add up all of the daily deviations for each day
      - If both stocks were above average on the same day, the result is positive.
      - If both were below average, the result is also positive (negative × negative).
      - If one was up and the other was down, the result is negative.
    - Standardize numbers on bottom of eqn - Square daily deviations from step 4, Sum the squared value for each deviation for both stocks, multiply the sums together, take the sqrt of that number
    - Divide result from step 5 by step 6 result which shows correlation
    - Make grid by listing all of stocks vertically and horizontally

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

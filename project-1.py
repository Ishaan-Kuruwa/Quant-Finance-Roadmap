# Import Libraries
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Download SPY Data for 5 Years
spy = yf.download ("SPY", start="2021-01-01", end="2026-01-01")
# Cleans out "Close"
spy.columns = spy.columns.get_level_values(0)
# Converts to float already
spy["Close"] = spy["Close"].astype(float)

# See Data
# RUN THIS -> print (spy.head())

# NOTE: There are much better ways to calculate many of these, for example: spy.pct_change() gets you the full simple daily returns or .moving_average(), etc.
# However, for learning purposes, computing yourself is more beneficial.

# Daily Returns are change in price over a day
# 1. Compute Simple Daily Returns (Use Vectorization for efficiency and no loops needed)
# Take (curr close - prev close) / prev close
spy["Simple Daily Returns"] = spy["Close"].pct_change()

# 2. Compute Log Daily Returns (Use Vectorization, no loops)
# Take natural log of difference in curr close and prev close
spy["Log Daily Returns"] = np.log (spy["Close"] / spy["Close"].shift(1))

# Log Returns allow you to find total returns over multiple days by just adding individual logs instead of recomputing with Simple Returns
# Log Returns are also more symmetrical unlike Simple Returns which have maximum loss of -100% but infinite upside
# Log Returns are also continous


# Moving Averages
# Average price of stock over amount of time 
# 1. Simple  50-day SMA Example
# Add up all prices for last 50 days / 50
# Have to use loop because of complex logic
# NOTE: I used one-liner after writing loop successfully
spy["Simple 50-day SMA"] = spy["Close"].rolling(50).mean()

# 2. Exponential  10-day SMA Example
# Each day before is 1/2 weighted avg (Ex: 1/2, 1/4...)
# Weighs days that are closer to current date as more important
# No division because summation of 1/2 + 1/4.. is close enough to 1
# NOTE: There is a 1-liner: spy["EMA 50"] = spy["Close"].ewm(span=50, adjust=False).mean()
spy["Exponential 10-day SMA"] = np.nan
for i in range (10, len(spy)):
    weight = 1
    total = 0
    for j in range (i-9, i+1):
        weight *= 1/2
        total += (spy["Close"].iloc[j] * weight)
    spy.at [spy.index[i], "Exponential 10-day SMA"] = total

# Rolling Volatility. 50-day Example
# Daily Percent Returns, Avg returns of window, (In 50-day SMA)
# Subtract avg from each individual return and square
# Add up and divide by n-1 days
# Take the SQRT of result
# NOTE: One-liner: built = spy["Simple Daily Returns"].rolling(50).std() * np.sqrt(252)
spy["Rolling Volatility 50-day"] = np.nan
for i in range (50, len(spy)): # 51 instead of 50 because first percent change is blank
    avg = 0
    for k in range (i-49, i+1):
        avg += spy["Simple Daily Returns"].iloc[k]
    avg /= 50
    
    tot = 0
    for j in range (i-49, i+1):
        res = (avg - spy["Simple Daily Returns"].iloc[j]) ** 2
        tot += res
    tot /= (50-1)
    tot = np.sqrt(tot) * np.sqrt(252)
    spy.at[spy.index[i], "Rolling Volatility 50-day"] = tot

# Compute Correlation Matrix for total 5 years of data among 3 Stocks and Plot as heatmap
# Get daily returns, find avg returns for each stock
# Calculate deviations daily (mean - price on day)
# Covariance Eqn: (Summation (X-X^)*(Y-Y^)) / sqrt (summation (X-X^2) * summation (Y-Y^2))
# NOTE: use .corr() to easily calculate (AT bottom of code)

# Download Data
aapl = yf.download ("AAPL", start="2021-01-01", end="2026-01-01")
# Cleans out "Close"
aapl.columns = aapl.columns.get_level_values(0)
# Converts to float already
aapl["Close"] = aapl["Close"].astype(float)

msft = yf.download ("MSFT", start="2021-01-01", end="2026-01-01")
msft.columns = msft.columns.get_level_values(0)
msft["Close"] = msft["Close"].astype(float)

xom = yf.download ("XOM", start="2021-01-01", end="2026-01-01")
xom.columns = xom.columns.get_level_values(0)
xom["Close"] = xom["Close"].astype(float)

# 1. Calculate avg returns across 5-yr data
aapl["returns"] = aapl["Close"].pct_change()
msft["returns"] = msft["Close"].pct_change()
xom["returns"] = xom["Close"].pct_change()
avgs = np.array ([0, 0, 0]).astype (float)
for i in range (1, len(spy)):
    avgs[0] += aapl["returns"].iloc[i]
    avgs[1] += msft["returns"].iloc[i]
    avgs[2] += xom["returns"].iloc[i]

avgs = avgs / (len(spy)-1)

deviations = []
# 2. Calculate Deviations
for i in range (1, len(spy)):
    deviation = np.array([avgs[0] - aapl["returns"].iloc[i], avgs[1] - msft["returns"].iloc[i], avgs[2] - xom["returns"].iloc[i]])
    deviations.append (deviation)

# 3. Calculate numerator
# Loop each possible row/column, and get mean - dev * mean - dev
stocks = ["aapl", "msft", "xom"]
numer = np.array ([])
for i in range (3):
    for j in range (3):
        tot = 0
        for dev in deviations:
            tot += (dev[i] * dev[j])
        numer = np.append (numer, tot)

# 4. Calculate squared deviations
sq_devs = []
for i in range (3):
    tot = 0
    for dev in deviations:
        tot += (dev[i])**2
    sq_devs.append (tot)

# 5. Find denominator
denom = np.array ([])
for i in range (3):
    for j in range (3):
        tot = np.sqrt(sq_devs[i] * sq_devs[j])
        denom = np.append (denom, tot)

# 6. Divide Equation
matr = numer / denom
print (matr)

# 7. Plot Correlation Matrix
np.random.seed(42)
matr = matr.reshape (3, 3) # Reshape Data to fit 3x3 grid
data = pd.DataFrame(matr, columns=["AAPL", "MSFT", "XOM"])

corr_matrix = data

plt.figure(figsize=(8, 6))
sns.heatmap(
    corr_matrix,
    xticklabels=stocks, 
    yticklabels=stocks, 
    annot=True,  # Show correlation coefficients inside cells
    cmap="coolwarm",
    fmt=".2f",  # Round values to 2 decimal places
)

plt.title("Correlation Matrix Heatmap")
plt.show()

# Fast Solution
returns = pd.concat ([aapl["returns"], msft["returns"], xom["returns"]], axis=1)
corr_matrix = returns.corr()
print (corr_matrix)
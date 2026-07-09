# Import libraries
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Download 10-yr data
aapl = yf.download ("AAPL", start="2016-01-01", end="2026-01-01")
# Cleans out words
aapl.columns = aapl.columns.get_level_values(0)
# Convert to float
aapl["Close"] = aapl["Close"].astype(float)

# Simulate price paths using Geometric Brownian Motion in its discrete form:
# S_next = S * exp((mu - 0.5*sigma²)*dt + sigma*√dt * Z), where Z is a standard normal draw.
# Predict next 5 years of price data by month = 60 months

# Decide variables into equation
                                        # dt = time change (every month) or 1/12 year
                                        # exp = exponential function (e^x)
starting_price = aapl["Close"].iloc[-1] # Initial stock Price
drift_rate = None                       # mu
annualized_volatility = None            # sigma
time = 5                                # years
Z = None                                # Z = random number

# Already have historical data and returns
# 1. Determine Volatility
# Find standard deviation of returns and mutliply by sqrt 252 to annualize
# std deviation formula - sqrt (summation of mean - deviation squared) / n-1
# NOTE: One-liner: aapl["returns"].std()

aapl["returns"] = np.log (aapl["Close"] / aapl["Close"].shift(1))
mean = aapl["returns"].mean()
total = 0
for i in range (1, len(aapl)):
    deviation = (mean - aapl["returns"].iloc[i]) ** 2
    total += deviation

total /= (len(aapl)-2) # have to do -2 for n-1 and extra first row
std_dev = np.sqrt (total)
annualized_volatility = std_dev * np.sqrt(252)

# 2. Determine Drift
# Use the stock's historical average annualized return.
# Calculated by: Daily Log returns, finding mean, annualizing (x252)
drift_rate = mean * 252

# 3. Simulate random shocks using Z
Z = np.random.normal (0, 1) # Bell Curve distribution

# Run 10,000+ paths; plot them; build a histogram of final prices.
final_prices = []
for i in range (10000): # 10,000 paths
    starting_price = aapl["Close"].iloc[-1] # Initial stock Price
    path = []
    for j in range (60): # 60 months for 5 years
        Z = np.random.normal (0, 1)
        # Full equation below
        next_price = starting_price * np.exp ( ((drift_rate - (annualized_volatility ** 2) / 2) * (1/12)) + (annualized_volatility * np.sqrt(1/12) * Z))
        path.append (next_price)

        starting_price = next_price
    final_prices.append (starting_price)
    # plt.plot (path) # Plot Path

# plt.hist (final_prices, bins=50) # Histogram of final prices

# Estimate things like "probability the price ends above X."
price_target = 300
final_prices = np.array (final_prices)
probability = np.mean (final_prices > price_target)
print (probability)
print (np.median (final_prices))
print (np.mean (final_prices))

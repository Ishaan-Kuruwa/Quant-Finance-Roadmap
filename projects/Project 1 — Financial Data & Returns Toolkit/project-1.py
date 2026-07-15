# Import Libraries
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Data_Analysis:
    def __init__ (self):
        # Download SPY Data for 5 Years
        self.spy = yf.download ("SPY", start="2021-01-01", end="2026-01-01")
        # Cleans out "Close"
        self.spy.columns = self.spy.columns.get_level_values(0)
        # Converts to float already
        self.spy["Close"] = self.spy["Close"].astype(float)

        # NOTE: There are much better ways to calculate many of these, for example: spy.pct_change() gets you the full simple daily returns or .moving_average(), etc.
        # However, for learning purposes, computing yourself is more beneficial.
    
    def see_data (self):
        # See Data
        return (self.spy)

    def collect_returns (self):
        # Daily Returns are change in price over a day
        # 1. Compute Simple Daily Returns (Use Vectorization for efficiency and no loops needed)
        # Take (curr close - prev close) / prev close
        self.spy["Simple Daily Returns"] = self.spy["Close"].pct_change()

        # 2. Compute Log Daily Returns (Use Vectorization, no loops)
        # Take natural log of difference in curr close and prev close
        self.spy["Log Daily Returns"] = np.log (self.spy["Close"] / self.spy["Close"].shift(1))

        # Log Returns allow you to find total returns over multiple days by just adding individual logs instead of recomputing with Simple Returns
        # Log Returns are also more symmetrical unlike Simple Returns which have maximum loss of -100% but infinite upside
        # Log Returns are also continous
    
    def log_additive (self):
        # We can verify that log returns are actually additive
        # We can recreate a 30-day log return
        # NOTE: We can understand this idea via telescoping:
        # Eqn: ln (P1 / P0) + ln (P2 / P1)... ln(Pn / Pn-1)
        # Using Log rules we get = ln (P1 / P0 * P2 / P1.... Pn / Pn-1)
        # Using telescoping cancellation we get = ln (Pn / P0)
        actual_return = (self.spy["Close"].iloc[31] / self.spy["Close"].iloc[1]) - 1
        log_return = 0
        simple_return = 0
        for i in range (2, 32):
            log_return += np.log (self.spy["Close"].iloc[i] / self.spy["Close"].iloc[i-1])
            simple_return += (self.spy["Close"].iloc[i] / self.spy["Close"].iloc[i-1]) - 1
        
        log_return = np.exp (log_return) - 1

        print (actual_return, log_return, simple_return)

    def moving_average (self):
        # Moving Averages
        # Average price of stock over amount of time 
        # 1. Simple  50-day SMA Example
        # Add up all prices for last 50 days / 50
        # Have to use loop because of complex logic
        # NOTE: I used one-liner after writing loop successfully
        self.spy["Simple 50-day SMA"] = self.spy["Close"].rolling(50).mean()

        # 2. Exponential  10-day SMA Example
        # Each day before is 1/2 weighted avg (Ex: 1/2, 1/4...)
        # Weighs days that are closer to current date as more important
        # No division because summation of 1/2 + 1/4.. is close enough to 1
        # NOTE: There is a 1-liner: spy["EMA 50"] = spy["Close"].ewm(span=50, adjust=False).mean()
        self.spy["Exponential 10-day SMA"] = np.nan
        for i in range (10, len(self.spy)):
            weight = 1
            total = 0
            for j in range (i, i-10, -1):
                weight *= 1/2
                total += (self.spy["Close"].iloc[j] * weight)
            self.spy.at [self.spy.index[i], "Exponential 10-day SMA"] = total
        
        # ALSO Recursive Form: EMA = alpha * P_t + (1 - alpha) * EMA (t-1) a = alpha - 2 / (span + 1)
        self.prices = self.spy["Close"]
        a = 2 / (10 + 1)
        self.spy["Recursive Exponential SMA"] = np.nan
        self.spy.at [self.spy.index[0], "Recursive Exponential SMA"] = self.prices.iloc[0]
        for i in range (1, len(self.spy)):
            ema = ((a * self.prices.iloc[i]) + (1-a) * self.spy["Recursive Exponential SMA"].iloc[i-1])

            self.spy.at [self.spy.index[i], "Recursive Exponential SMA"] = ema

        plt.title ("Moving Averages")
        plt.plot (self.spy["Recursive Exponential SMA"])
        plt.plot (self.spy["Close"])
        plt.plot (self.spy["Simple 50-day SMA"])
        plt.plot (self.spy["Exponential 10-day SMA"])
        plt.show()

    def rolling_volatility (self):
        # Rolling Volatility. 50-day Example
        # Daily Percent Returns, Avg returns of window, (In 50-day SMA)
        # Subtract avg from each individual return and square
        # Add up and divide by n-1 days
        # Take the SQRT of result
        # NOTE: One-liner: built = spy["Simple Daily Returns"].rolling(50).std() * np.sqrt(252)
        self.spy["Rolling Volatility 50-day"] = np.nan
        for i in range (50, len(self.spy)): # 51 instead of 50 because first percent change is blank
            avg = 0
            for k in range (i-49, i+1):
                avg += self.spy["Simple Daily Returns"].iloc[k]
            avg /= 50
            
            tot = 0
            for j in range (i-49, i+1):
                res = (avg - self.spy["Simple Daily Returns"].iloc[j]) ** 2
                tot += res
            tot /= (50-1)
            tot = np.sqrt(tot) * np.sqrt(252)
            self.spy.at[self.spy.index[i], "Rolling Volatility 50-day"] = tot
        
        plt.title ("Rolling Volatility")
        plt.plot (self.spy["Rolling Volatility 50-day"])
        plt.show()
    
    def get_data (self):
        # Compute Correlation Matrix for total 5 years of data among 3 Stocks and Plot as heatmap
        # Get daily returns, find avg returns for each stock
        # Calculate deviations daily (mean - price on day)
        # Covariance Eqn: (Summation (X-X^)*(Y-Y^)) / sqrt (summation (X-X^2) * summation (Y-Y^2))
        # NOTE: use .corr() to easily calculate (AT bottom of code)

        # Download Data
        self.aapl = yf.download ("AAPL", start="2021-01-01", end="2026-01-01")
        # Cleans out "Close"
        self.aapl.columns = self.aapl.columns.get_level_values(0)
        # Converts to float already
        self.aapl["Close"] = self.aapl["Close"].astype(float)

        self.msft = yf.download ("MSFT", start="2021-01-01", end="2026-01-01")
        self.msft.columns = self.msft.columns.get_level_values(0)
        self.msft["Close"] = self.msft["Close"].astype(float)

        self.xom = yf.download ("XOM", start="2021-01-01", end="2026-01-01")
        self.xom.columns = self.xom.columns.get_level_values(0)
        self.xom["Close"] = self.xom["Close"].astype(float)
    
    def avg_returns (self):
        # 1. Calculate avg returns across 5-yr data
        self.aapl["returns"] = self.aapl["Close"].pct_change()
        self.msft["returns"] = self.msft["Close"].pct_change()
        self.xom["returns"] = self.xom["Close"].pct_change()
        self.avgs = np.array ([0, 0, 0]).astype (float)
        for i in range (1, len(self.spy)):
            self.avgs[0] += self.aapl["returns"].iloc[i]
            self.avgs[1] += self.msft["returns"].iloc[i]
            self.avgs[2] += self.xom["returns"].iloc[i]

        self.avgs = self.avgs / (len(self.spy)-1)
        
    def deviations (self):
        self.devs = []
        # 2. Calculate Deviations
        for i in range (1, len(self.spy)):
            self.deviation = np.array([self.avgs[0] - self.aapl["returns"].iloc[i], self.avgs[1] - self.msft["returns"].iloc[i], self.avgs[2] - self.xom["returns"].iloc[i]])
            self.devs.append (self.deviation)
    
    def calc_numer (self):
        # Loop each possible row/column, and get mean - dev * mean - dev
        self.stocks = ["aapl", "msft", "xom"]
        self.numer = np.array ([])
        for i in range (3):
            for j in range (3):
                tot = 0
                for dev in self.devs:
                    tot += (dev[i] * dev[j])
                self.numer = np.append (self.numer, tot)
    
    def squared_devs (self):
        self.sq_devs = []
        for i in range (3):
            tot = 0
            for dev in self.devs:
                tot += (dev[i])**2
            self.sq_devs.append (tot)
    
    def calc_denom (self):
        # 5. Find denominator
        self.denom = np.array ([])
        for i in range (3):
            for j in range (3):
                tot = np.sqrt(self.sq_devs[i] * self.sq_devs[j])
                self.denom = np.append (self.denom, tot)

    def divide (self):
        # 6. Divide Equation
        self.matr = self.numer / self.denom
    
    def calc_ratios (self):
        # Calculate Sharpe Ratio = (Annualized Return - Risk-free Rate) / (Annualized Volatility)
        # 1. Calculate Avg Annual Returns
        self.spy_avg = 0
        for i in range (1, len(self.spy)):
            self.spy_avg += self.spy["Simple Daily Returns"].iloc[i]
        
        self.spy_avg /= (len(self.spy)-1)
        self.spy_annual_avg = self.spy_avg * 252

        # 2. Calculate Annual Std Deviations by hand
        self.spy_vol = 0
        for i in range (1, len(self.spy)):
            dev = self.spy_avg - self.spy["Simple Daily Returns"].iloc[i]
            dev = dev ** 2
            self.spy_vol += dev

        self.spy_vol /= (len(self.spy) - 2) # -1 for missing first day and -1 for sample size (n-1)
        self.spy_vol = np.sqrt (self.spy_vol)
        self.spy_vol *= np.sqrt (252)

        # 3. Pull 10-yr Trasury Bill
        ten_yr_treasury = yf.Ticker ("^IRX")
        historical_yields = ten_yr_treasury.history (start="2021-01-01", end="2026-01-01")
        self.rfr = (historical_yields["Close"].iloc[-1]) / 100

        self.sharpe_ratio = (self.spy_annual_avg - self.rfr) / (self.spy_vol)
        print ("Sharpe Ratio: ", self.sharpe_ratio)

        # Calculate Max Drawdown = ((trough value - peak value) / (peak value)) * 100
        # Make sure to measure as peak is before trough comes
        peak = 0
        self.drawdown = 0
        for i in range (len (self.spy)):
            curr_price = self.spy["Close"].iloc[i]
            if curr_price > peak: peak = curr_price
            self.drawdown = min (((curr_price - peak) / (peak)) * 100, self.drawdown)
        
        print ("Max Drawdown: ", self.drawdown)
    
    def corr_matrix (self):
        # 7. Plot Correlation Matrix
        self.matr = self.matr.reshape (3, 3) # Reshape Data to fit 3x3 grid
        data = pd.DataFrame(self.matr, columns=["AAPL", "MSFT", "XOM"])

        corr_matrix = data

        plt.figure(figsize=(8, 6))
        sns.heatmap(
            corr_matrix,
            xticklabels=self.stocks, 
            yticklabels=self.stocks, 
            annot=True,  # Show correlation coefficients inside cells
            cmap="coolwarm",
            fmt=".2f",  # Round values to 2 decimal places
        )

        plt.title("Correlation Matrix Heatmap")
        plt.show()

        # Fast Solution
        returns = pd.concat ([self.aapl["returns"], self.msft["returns"], self.xom["returns"]], axis=1)
        corr_matrix = returns.corr()
        print ("Correlation Matrix: ", corr_matrix)
    
    def run (self):
        self.log_additive()
        self.collect_returns()
        self.moving_average()
        self.rolling_volatility()
        self.get_data()
        self.avg_returns()
        self.deviations()
        self.calc_numer()
        self.squared_devs()
        self.calc_denom()
        self.divide()
        self.calc_ratios()
        self.corr_matrix()
        self.see_data()

analysis = Data_Analysis()
analysis.run()

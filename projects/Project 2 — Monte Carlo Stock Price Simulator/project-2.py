# Import libraries
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Simulation:
    def __init__ (self):
        # Download 10-yr data
        self.aapl = yf.download ("AAPL", start="2016-01-01", end="2026-01-01")
        # Cleans out words
        self.aapl.columns = self.aapl.columns.get_level_values(0)
        # Convert to float
        self.aapl["Close"] = self.aapl["Close"].astype(float)

    def see_data (self):
        # See Data
        return (self.aapl)

    def variables (self):
        # Simulate price paths using Geometric Brownian Motion in its discrete form:
        # S_next = S * exp((mu - 0.5*sigma²)*dt + sigma*√dt * Z), where Z is a standard normal draw.
        # Predict next 5 years of price data by month = 60 months

        # Decide variables into equation
                                                            # dt = time change (every month) or 1/12 year
                                                            # exp = exponential function (e^x)
        self.starting_price = self.aapl["Close"].iloc[-1]   # Initial stock Price
        self.drift_rate = None                              # mu
        self.annualized_volatility = None                   # sigma
        self.time = 5                                       # years
        self.Z = None                                       # Z = random number

    def volatility (self):
        # Already have historical data and returns
        # 1. Determine Volatility
        # Find standard deviation of returns and mutliply by sqrt 252 to annualize
        # std deviation formula - sqrt (summation of mean - deviation squared) / n-1
        # NOTE: One-liner: aapl["returns"].std()

        self.aapl["returns"] = np.log (self.aapl["Close"] / self.aapl["Close"].shift(1))
        self.mean = self.aapl["returns"].mean()
        total = 0
        for i in range (1, len(self.aapl)):
            deviation = (self.mean - self.aapl["returns"].iloc[i]) ** 2
            total += deviation

        total /= (len(self.aapl)-2) # have to do -2 for n-1 and extra first row
        std_dev = np.sqrt (total)
        self.annualized_volatility = std_dev * np.sqrt(252)

    def drift (self):
        # 2. Determine Drift
        # Use the stock's historical average annualized return.
        # Calculated by: Daily Log returns, finding mean, annualizing (x252)
        self.drift_rate = self.mean * 252

    def generate_sim (self):
        # Run 10,000+ paths; plot them; build a histogram of final prices.
        self.final_prices = []
        for i in range (10000): # 10,000 paths
            starting_price = self.aapl["Close"].iloc[-1] # Initial stock Price
            path = []
            for j in range (60): # 60 months for 5 years
                self.Z = np.random.normal (0, 1)
                # Full equation below
                next_price = starting_price * np.exp ( ((self.drift_rate - (self.annualized_volatility ** 2) / 2) * (1/12)) + (self.annualized_volatility * np.sqrt(1/12) * self.Z))
                path.append (next_price)

                starting_price = next_price
            self.final_prices.append (starting_price)
            plt.plot (path) # Plot Path
        
        plt.show()
    
    def plot_hist (self):
        plt.hist (self.final_prices, bins=50) # Histogram of final prices
        plt.show()

    def probability (self):
        # Estimate things like "probability the price ends above X."
        price_target = 300
        self.final_prices = np.array (self.final_prices)
        probability = np.mean (self.final_prices > price_target)
        print (probability)
        print (np.median (self.final_prices))
        print (np.mean (self.final_prices))

    def run (self):
        self.variables()
        self.volatility()
        self.drift()
        self.generate_sim()
        self.plot_hist()
        self.probability()
        self.see_data()

simulation = Simulation()
simulation.run()

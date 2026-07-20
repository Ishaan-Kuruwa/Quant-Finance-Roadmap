# Import Libraries
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import minimize

# Define Class
class Portfolio_Optimizer:
    def __init__ (self):
        # Define Asset Tickers in portfolio
        self.tickers = ["AAPL", "GLD", "JPM", "PG", "TLT", "UNH", "XOM"]
        # Define starting and ending dates for data
        self.start_date = "2021-01-01"
        self.end_date = "2026-01-01"
        # Download last 5 years of data
        self.data = yf.download (self.tickers, start=self.start_date, end=self.end_date)["Close"]
        # Clean Data
        self.data.columns = self.data.columns.get_level_values(0)
        # Convert to float
        self.data = self.data.astype(float)
                
    def see_data (self):
        # See Data
        print (self.data)
    
    def get_returns (self):
        # Get returns in a new dataframe
        # NOTE: One-liner:  self.returns = self.data.pct_change()
        self.returns = pd.DataFrame
        self.returns = (self.data - self.data.shift (1)) / self.data.shift(1) # Vectorization to create returns
        print (self.returns)
    
    def expected_returns (self):
        # Calculate annual expected returns
        # For each ticker and returns value, add it and take the mean, then annualize by multiplying by 252
        # NOTE: One-liner:  ev = self.returns.mean() * 252
        tot = [0] * len (self.tickers)
        self.mean = [0] * len (self.tickers)
        for i in range (len(self.tickers)):
            for j in range (1, len (self.data)):
                tot[i] += self.returns[self.tickers[i]].iloc[j]
            
            tot[i] /= (len(self.data)-1)
            self.mean[i] = tot[i]
        
        self.annual_mean = np.array (self.mean) * 252
        print (self.annual_mean)
    
    def covariance_matrix (self):
        # Calculate annual Covariance Matrix
        # NOTE: One-liner:  self.cov = self.returns.cov() * 252
        # For each pair of tickers, for each return, calculate product of deviations for each return, 
        # divide by # of returns, annualize by multiplying by 252
        self.cov_matr = []        
        for i in range (len (self.tickers)):
            for j in range (len (self.tickers)):
                tot = 0
                for k in range (1, len (self.data)):
                    tot += ((self.mean[i] - self.returns[self.tickers[i]].iloc[k]) * (self.mean[j] - self.returns[self.tickers[j]].iloc[k]))
                tot /= (len (self.data)-2)
                tot *= 252
                self.cov_matr.append (tot)
        
        self.cov_matr = np.asarray (self.cov_matr).reshape (len (self.tickers), len (self.tickers))

        # Plot covariance matrix as a grid
        plt.figure (figsize=(8, 6))
        sns.heatmap(
            self.cov_matr,
            annot=True,
            fmt=".4f",
            cmap="coolwarm",
            vmax=None,
            square=True,
            xticklabels=self.tickers,
            yticklabels=self.tickers,
        )
        plt.title ("Covariance Matrix")
        plt.show()
        # Check if covariance matrix is correct
        diff = np.abs(self.cov_matr - self.cov.to_numpy()).max()
        print(f"manual vs pandas: {diff:.3e}")     # want ~1e-16
    
    def portfolio_return (self):
        # Calculate portfolio's return
        # Steps:
        # Create random weights
        # Get mean of weights
        # Calculate the dot product of mean returns and weights
        self.weights = np.random.random (len (self.tickers))
        weight_sum = 0
        for i in range (len (self.weights)):
            weight_sum += self.weights[i]
        self.weights /= weight_sum
        print (np.dot (self.weights, self.annual_mean))
        self.portfolio_returns = 0
        for i in range (len (self.weights)):
            self.portfolio_returns += (self.weights[i] * self.annual_mean[i])
        
        print ("Portfolio Returns: ", self.portfolio_returns)
    
    def portfolio_volatility (self):
        # Calculate portfolio's volatility
        # Calculate variance by taking dot product of weights and covariance matrix for each pair,
        # Take sqrt of variance for volatility
        self.portfolio_variance = 0
        for i in range (len (self.weights)):
            for j in range (len (self.weights)):
                tot = self.weights[i] * self.weights[j] * self.cov_matr[i, j]
                self.portfolio_variance += tot

        self.portfolio_variance = np.sqrt (self.portfolio_variance)
        
        print ("Portfolio Variance: ", self.portfolio_variance)
        print("Manual vs Pandas: ", abs(self.portfolio_variance - (self.weights.T @ self.cov_matr @ self.weights)))   # ~1e-16

    def test_case (self):
        # Practice test case to test volatility dot product
        w1 = 0.5
        w2 = 0.5
        vol1 = 0.20
        vol2 = 0.20

        t1 = (w1**2 * vol1**2)
        t2 = (w2**2 * vol2**2)
        t3 = (2*w1*w2*vol1*vol2)
        p_neg1 = np.sqrt (t1 + t2 + t3 * -1)
        p_0 = np.sqrt (t1 + t2 + t3 * 0)
        p_plus1 = np.sqrt (t1 + t2 + t3 * 1)
        print ("Test Cases: ", p_neg1, p_0, p_plus1)
    
    def simulation (self):
        # Simulate 10,000 portfolios
        # Calculate weights, return, volatility, and sharpe ratio
        self.portfolios = []
        rfr = 0.04
        for i in range (10000):
            w = np.random.random (len (self.tickers))
            w /= np.sum (w)
            ret = w @ self.annual_mean
            vol = np.sqrt (w.T @ self.cov_matr @ w)
            sharpe = (ret - rfr) / vol

            self.portfolios.append ({"Weights": w, "Returns": ret, "Volatility": vol, "Sharpe": sharpe})
        
        self.portfolios = pd.DataFrame (self.portfolios)
        print (self.portfolios)
    
    def analyze_sim (self):
        # Find best sharpe ratio and lowest volatility portfolios
        self.best = self.portfolios.loc[self.portfolios["Sharpe"].idxmax()]
        self.minvar = self.portfolios.loc[self.portfolios["Volatility"].idxmin()]
        print ("Best Sharpe: ", self.best)
        print ("Lowest Volatility: ", self.minvar)
    
    def plot_portfolios (self):
        # Plot portfolios with best portfolios in legend
        # NOTE: Should look like a bullet shape
        plt.figure(figsize=(10, 6))
        plt.scatter(self.portfolios["Volatility"], self.portfolios["Returns"],
                    c=self.portfolios["Sharpe"], cmap="viridis", s=5, alpha=0.5)
        plt.colorbar(label="Sharpe ratio")
        plt.scatter(self.best["Volatility"], self.best["Returns"], marker="*", s=500,
                    c="red", label="Max Sharpe")
        plt.scatter(self.minvar["Volatility"], self.minvar["Returns"], marker="*", s=500,
                    c="orange", label="Min variance")
        plt.xlabel("Annualized volatility")
        plt.ylabel("Annualized return")
        plt.title("Efficient Frontier — 10,000 random portfolios")
        plt.legend()
        plt.show()

    def run (self):
        # Run each function
        self.see_data()
        self.get_returns()
        self.expected_returns()
        self.covariance_matrix()
        self.portfolio_return()
        self.portfolio_volatility()
        self.test_case()
        self.simulation()
        self.analyze_sim()
        self.plot_portfolios()

# Define instance
optim = Portfolio_Optimizer()
optim.run()

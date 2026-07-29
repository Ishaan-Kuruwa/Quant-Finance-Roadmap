# Import Libraries
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Define Class
class Backtesting_Engine:
    def __init__ (self):
        # Stock
        self.ticker = "SPY"
        # 10 Years of Data
        self.start_date = "2016-01-01"
        self.end_date = "2026-01-01"
        self.data = yf.download (self.ticker, start=self.start_date, end=self.end_date)["Close"]
        self.data = self.data.squeeze().astype(float)
        # Calculate Returns
        self.returns = self.data.pct_change()
        self.n = len (self.data)

        # Define Trading Cost
        self.t_cost = 0.0005
    
    def see_data (self):
        # See Data
        print (self.data)

    def backtest (self, strategy):
        # Move all signals back 1 day
        position = strategy.shift(1).fillna(0)

        # Calculate transaction costs total
        turnover = position.diff().abs().fillna(0)
        costs = turnover * self.t_cost

        # Calculate Strategy Returns and overall equity
        strategy_returns = position * self.returns - costs
        equity = (1 +  strategy_returns).cumprod()

        # Return Data Frame of Backtest
        return pd.DataFrame({
            "returns": self.returns,
            "signal": strategy,
            "position": position,
            "strategy_returns": strategy_returns,
            "equity": equity
        })

    def eval_strategy (self, strategy):
        # CAGR (returns for 10 yrs scaled down to annual)
        # SHARPE - (returns - rfr) / (volatility)
        # MAX DRAWDOWN - worst peak to trough drop
        # TURNOVER - # of trades completed (affects with transaction costs)
        # TIME IN MARKET - # of days invested
        backtest = self.backtest(strategy)

        # Plot Equity Value
        plt.plot (backtest["equity"])
        plt.show()

        # Hold backtest results
        sr = backtest["strategy_returns"]
        equity = backtest["equity"]
        yrs = len (sr) / 252

        # Calculate CAGR & SHARPE using formulas
        cagr = equity.iloc[-1] ** (1/yrs) - 1 
        sharpe = (cagr - 0.04) / (sr.std() * np.sqrt(252)) # can also use mean returns * 252 instead of cagr

        # Calculate MAX DD
        peak = equity.cummax()
        max_dd = ((equity - peak) / peak).min()

        # Full Code for MAX DD
        max_dd2 = 0
        peak = equity.iloc[0]
        for i in range (len (equity)):
            peak = max (peak, equity.iloc[i])
            max_dd2 = min (max_dd2, (equity.iloc[i] - peak)/peak)

        # Calculate Turnover and Time in Market
        turnover = backtest["position"].diff().abs().sum() / yrs
        time_in_market = (backtest["position"] != 0).mean()

        # Print Results
        print ({
            "CAGR": cagr,
            "SHARPE": sharpe,
            "MAX_DD": max_dd,
            "TURNOVER": turnover,
            "TIME IN MARKET": time_in_market
        })
        
    def moving_average_crossover (self):
        # Define Moving Average Crossover Strategy
        mas_signals = [0]*self.n
        # Define lengths of fast and slow ma
        s_ma = 200
        f_ma = 50
        # Make loop, calc averages, then count diff as 1 or -1 for signal
        for i in range (self.n):
            if i < s_ma-1: continue
            diff = [0, 0]
            for j in range (i-s_ma+1, i+1):
                diff[0] += self.data.iloc[j]
                if j >= i-f_ma: diff[1] += self.data.iloc[j]
            
            diff[0] /= s_ma
            diff[1] /= f_ma

            if diff[1] > diff[0]: mas_signals[i] = 1
            elif diff[0] > diff[1]: mas_signals[i] = -1
        return pd.Series (mas_signals, index = self.data.index)

    def momentum (self):
        # Define Momentum Strategy
        mom_signals = [0] * self.n
        # Lookback of 6 months time
        lback = 126
        for i in range (self.n):
            if i < lback: continue
            diff = (self.data.iloc[i] - self.data.iloc[i-lback]) / (self.data.iloc[i-lback])
            # Only hold signal if change of 5% either way (-1 or 1)
            if diff > 0.05: mom_signals[i] = 1
            elif diff < -0.05: mom_signals[i] = -1
        return pd.Series (mom_signals, index = self.data.index)

    def buy_and_hold (self):
        # Define Buy and Hold Strategy
        # 1 All the way
        bandh_signal = [1] * self.n
        return pd.Series (bandh_signal, index = self.data.index)

    def leak_strategy (self):
        # Define strategy that should make perfect returns with leaky backtest
        return (self.returns > 0).astype(int)

    def run (self):
        # Run all strategies and see metrics
        self.see_data()
        self.eval_strategy(self.moving_average_crossover())
        self.eval_strategy(self.momentum())
        self.eval_strategy(self.buy_and_hold())
        self.eval_strategy(self.leak_strategy())

# Define Backtest
backtest = Backtesting_Engine()
backtest.run()

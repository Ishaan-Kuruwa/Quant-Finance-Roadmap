- Build:
  - Implement the Black–Scholes formula for European call/put prices (it's a plug-in formula — you provide spot, strike, time, interest rate, and volatility).
  - Independently price the same option with Monte Carlo: simulate many price paths (reusing Project 2!), compute each path's payoff, average them, and discount to today.
  - Show the two methods agree as the number of simulations grows.
  - Plot payoff diagrams for calls and puts.
- To fully explain, master:
  - What options are: calls, puts, strikes, expiration, and payoff at expiry.
  - The five inputs to Black–Scholes and, intuitively, how each moves the price (especially volatility).
  - The idea of pricing by expected discounted payoff — the logic behind the Monte Carlo approach.
- Calculus later: Deriving Black–Scholes requires stochastic calculus and partial differential equations — genuinely a college-and-beyond topic. Don't fake it. You can implement it, explain what it does, explain every input, and verify it with an independent method — which is a strong, honest place to be. Flag the derivation as something you'll appreciate fully after more math. This is a case where "fully understand" honestly means "understand and can use and verify," not "derive from first principles" — and that's the right expectation for now.
- Call gives you the right not the obligation to buy an asset at a fixed price on a future expiration date
- Put gives you the right to sell
- Call is only worth something if 
- Call Option Equation: C=S⋅N(d1)−K⋅e−rT⋅N(d2)
- Call is in the money if above strike price, 
- Put is in money if below strike price
- Limited downside (premium), unlimited upside
- Because downside is limited, volatility makes options more valuable, a big move in either direction can be profitable
- Black-Scholes Equation - 5 Inputs

$$
C = S \cdot N(d_1) - K \cdot e^{-rT} \cdot N(d_2)
$$

$$
d1=ln(SK)+(r+σ22)TσT
$$

- Monte Carlo
- Simulates many random paths of the underlying asset
- Calculated expected payoff of options based on that
- Discounts back to find actual value

$$
\(S_{t}=S_{0}\exp \left(\left(\mu -\frac{\sigma ^{2}}{2}\right)t+\sigma W_{t}\right)\)
$$

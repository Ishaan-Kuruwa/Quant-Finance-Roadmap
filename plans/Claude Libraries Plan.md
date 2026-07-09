# Learning the Libraries You'll Need (pandas & friends)

How to actually learn the Python libraries behind your six projects — without drowning. Keep this with your roadmap, project plan, and calculus guide.

**The core philosophy:** Don't learn a library as a big upfront course. Learn the **mental model** of each (the one idea it's built on), then learn the **~20% of it your current project needs**, then build and look up the rest as you hit it. Reading documentation while you build is not "cheating" — it's the actual job. Get comfortable with it early.

---

## The libraries, in the order you'll need them

### 1. NumPy — *the number engine*
**Mental model:** Fast arrays of numbers you can do math on all at once (no loops). Everything else is built on top of it.
**Used in:** Every project. Especially Monte Carlo (Project 2, random number generation), portfolio math (Project 3, matrix operations), and Black–Scholes (Project 5).
**Learn just:** creating arrays, array math (vectorized operations), `np.random` for simulations, `np.log`/`np.exp`, and basic matrix operations.
**Best resource:** The official **NumPy "Absolute Beginner's Guide"** / quickstart. It's short and exactly the right scope.

### 2. pandas — *the data workhorse*
**Mental model:** A spreadsheet in code. A **Series** is one labeled column; a **DataFrame** is a whole labeled table. The magic is that operations align by label automatically — which is *why* `pct_change()` and `shift()` worked without loops in your returns problem.
**Used in:** Nearly everything — data loading and cleaning, returns (Project 1), time-series and rolling windows (Project 4), feature engineering (Project 6).
**Learn just:** Series vs. DataFrame, selecting rows/columns (`.loc`, `.iloc`), `pct_change()`, `shift()`, `rolling()`, `dropna()`, `.corr()`, and reading a CSV.
**Best resources:**
- Official **"10 minutes to pandas"** first, then the **User Guide** sections as needed.
- **Kaggle's free "Pandas" micro-course** — short, hands-on, interactive. Great for cementing it.
- **Corey Schafer's pandas series** on YouTube — clear, well-paced, widely recommended.
- The definitive book: **"Python for Data Analysis" by Wes McKinney** (he *created* pandas). Use it as a reference to reach for, not a book to read cover-to-cover.

### 3. Matplotlib — *the plotter*
**Mental model:** A **Figure** is the canvas; **Axes** are the plot(s) on it. You draw onto axes. Slightly clunky at first, then fine.
**Used in:** Every project — you'll visualize prices, returns, simulated paths, efficient frontiers, equity curves.
**Learn just:** `plt.plot()`, labels/titles/legends, histograms, and plotting multiple series. That's 90% of what you'll do.
**Best resource:** The official **pyplot tutorial**. For nicer statistical plots (like the correlation heatmap in Project 1), add **seaborn**, which sits on top of matplotlib and makes good-looking charts in one line — learn it only when you want prettier output.

### 4. yfinance — *the data source*
**Mental model:** A tiny helper that downloads historical price data into a pandas DataFrame. That's it.
**Used in:** Project 1 (and reused wherever you need real data).
**Learn just:** how to download one or several tickers over a date range. Ten minutes.
**Best resource:** Its **GitHub README** — the whole library is small enough that the README is the tutorial.

### 5. SciPy — *the specialist toolbox*
**Mental model:** A big grab-bag of scientific functions. You won't learn "SciPy" — you'll learn the one or two functions you need from a specific submodule.
**Used in:** Project 3 (`scipy.optimize` to find the optimal portfolio — though you can start with a random search and skip this) and Project 5 (`scipy.stats.norm.cdf` for the normal distribution in Black–Scholes).
**Learn just:** the specific functions each project calls, straight from the official docs. Don't study it broadly.
**Best resource:** The official **SciPy docs** for the exact submodule — read narrowly.

### 6. scikit-learn — *the ML toolkit*
**Mental model:** Every model follows the same pattern: `model.fit(X, y)` then `model.predict(X)`. Once you know the pattern, you know the whole library's shape.
**Used in:** Project 6 (the ML-on-markets project). Plays to the ML background you already have.
**Learn just:** the fit/predict pattern, train/test splitting (**with time order respected — no shuffling!**), and one or two models (logistic regression, random forest).
**Best resources:**
- Official **scikit-learn "Getting Started"** guide.
- **Kaggle's free "Intro to Machine Learning"** and **"Intermediate Machine Learning"** micro-courses — hands-on and short.

---

## How to actually learn any one of these (the repeatable process)

1. **Get the mental model** (one paragraph, above). Know what abstraction the library gives you before touching syntax.
2. **Do one focused tutorial** for the ~20% your current project needs — not the whole thing.
3. **Build the project.** You learn a library by *using* it, not by reading about it.
4. **Look things up as you hit them.** Open the official docs, search the exact method, read the example, adapt it. Do this constantly and without guilt — it's the real skill.
5. **Type it, don't copy it.** Retyping code (even from a tutorial) and then changing something to see what breaks teaches far more than pasting.

A good test that you've truly learned a piece: can you write it into your project's explainer README and describe *why* it works? (Same principle as the rest of your plan.)

---

## The learning order (it matches your project order)

You don't need all six libraries at once. They come online naturally as you move through the projects:

| Learn when you start... | You'll need |
|---|---|
| **Project 1** (data toolkit) | pandas, NumPy, matplotlib, yfinance |
| **Project 2** (Monte Carlo) | more NumPy (`np.random`) |
| **Project 3** (portfolio) | more pandas + NumPy matrix ops; optionally scipy.optimize |
| **Project 4** (backtesting) | deeper pandas (`rolling`, time series) |
| **Project 5** (options) | `scipy.stats` (just `norm.cdf`) |
| **Project 6** (ML) | scikit-learn |

So the honest answer to "how do I learn all of them": **you don't, all at once.** You learn pandas + NumPy + matplotlib solidly for Projects 1–2, and the rest arrives one project at a time. By Project 6 you'll have picked up each library exactly when you had a real reason to.

---

## Your environment

Work in **Jupyter notebooks** (via JupyterLab or VS Code's notebook support, or Google Colab if you want zero setup). Notebooks let your explanation, math, code, and charts live in one place — which is exactly what your "build to explain" goal needs.

---

## The shortest possible resource list

If you want just a few things rather than a menu:

- **Kaggle Learn** (free, interactive) — the "Pandas" and "Intro to Machine Learning" micro-courses. Best hands-on starting point.
- **Official docs** — "10 minutes to pandas," the NumPy beginner's guide, the matplotlib pyplot tutorial. Learn to live in these.
- **Corey Schafer** (YouTube) — for clear video walkthroughs of pandas and Python.
- **"Python for Data Analysis" by Wes McKinney** — the pandas reference to keep on hand.

Everything here is free (the McKinney book has a freely readable edition online). Search each name and you'll find it fast.

The through-line across all of this: **learn the least you need to build the next thing, then build it.** Repeat six times and you'll know these libraries the way people who actually use them do — by having solved real problems with them.

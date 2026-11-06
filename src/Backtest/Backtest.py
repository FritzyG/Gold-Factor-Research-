# ============================================================
# GOLD FACTOR RESEARCH
# BACKTEST ENGINE
# ============================================================

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

# ============================================================
# LOAD MODEL PREDICTIONS
# ============================================================

df = pd.read_csv(
    "../../data/processed/model_predictions.csv",
    index_col=0,
    parse_dates=True
)

print("Data Loaded")
print(df.shape)

# ============================================================
# STRATEGY SIGNAL
# ============================================================
# Buy Gold if model probability > 60%
# Stay in cash otherwise

df["signal"] = np.where(
    df["probability"] > 0.60,
    1,
    0
)

# ============================================================
# EXECUTION LAG
# ============================================================
# Shift signals 1 day to avoid look-ahead bias

df["signal"] = (
    df["signal"]
    .shift(1)
    .fillna(0)
)

# ============================================================
# STRATEGY RETURNS
# ============================================================

df["strategy_return"] = (
    df["signal"]
    *
    df["gold_return"]
)

# ============================================================
# BUY & HOLD RETURNS
# ============================================================

df["buyhold_return"] = (
    df["gold_return"]
)

# ============================================================
# EQUITY CURVES
# ============================================================

df["strategy_equity"] = (
    1 +
    df["strategy_return"]
).cumprod()

df["buyhold_equity"] = (
    1 +
    df["buyhold_return"]
).cumprod()

# ============================================================
# ANNUAL RETURN
# ============================================================

def annual_return(returns):

    cumulative_return = (
        1 + returns
    ).prod()

    years = (
        len(returns)
        / 252
    )

    return (
        cumulative_return **
        (1 / years)
        - 1
    )

# ============================================================
# SHARPE RATIO
# ============================================================

def sharpe_ratio(returns):

    return (
        returns.mean()
        /
        returns.std()
    ) * np.sqrt(252)

# ============================================================
# SORTINO RATIO
# ============================================================

def sortino_ratio(returns):

    downside_returns = (
        returns[
            returns < 0
        ]
    )

    downside_std = (
        downside_returns.std()
    )

    return (
        returns.mean()
        /
        downside_std
    ) * np.sqrt(252)

# ============================================================
# VOLATILITY
# ============================================================

def annual_volatility(returns):

    return (
        returns.std()
        *
        np.sqrt(252)
    )

# ============================================================
# MAX DRAWDOWN
# ============================================================

def max_drawdown(returns):

    equity_curve = (
        1 +
        returns
    ).cumprod()

    peak = (
        equity_curve
        .cummax()
    )

    drawdown = (
        equity_curve
        /
        peak
        - 1
    )

    return drawdown.min()

# ============================================================
# WIN RATE
# ============================================================

def win_rate(returns):

    trades = (
        returns[
            returns != 0
        ]
    )

    if len(trades) == 0:
        return 0

    return (
        trades > 0
    ).mean()

# ============================================================
# CALCULATE METRICS
# ============================================================

strategy_returns = (
    df["strategy_return"]
    .dropna()
)

performance = {
    "Annual Return":
    annual_return(strategy_returns),

    "Annual Volatility":
    annual_volatility(strategy_returns),

    "Sharpe Ratio":
    sharpe_ratio(strategy_returns),

    "Sortino Ratio":
    sortino_ratio(strategy_returns),

    "Maximum Drawdown":
    max_drawdown(strategy_returns),

    "Win Rate":
    win_rate(strategy_returns)
}

performance_df = pd.DataFrame(
    performance,
    index=["Strategy"]
)

print("\nPerformance Metrics")
print(performance_df)

# ============================================================
# SAVE PERFORMANCE REPORT
# ============================================================

performance_df.to_csv(
    "../../reports/backtest_results.csv"
)

print(
    "\nbacktest_results.csv saved."
)

# ============================================================
# EQUITY CURVE CHART
# ============================================================

plt.figure(
    figsize=(12,6)
)

plt.plot(
    df.index,
    df["strategy_equity"],
    label="Strategy"
)

plt.plot(
    df.index,
    df["buyhold_equity"],
    label="Buy & Hold Gold"
)

plt.title(
    "Strategy vs Buy & Hold"
)

plt.xlabel("Date")

plt.ylabel(
    "Portfolio Value"
)

plt.legend()

plt.tight_layout()

plt.savefig(
    "../../images/equity_curve.png"
)

plt.show()

# ============================================================
# DRAWDOWN ANALYSIS
# ============================================================

equity_curve = (
    1 +
    strategy_returns
).cumprod()

peak = (
    equity_curve
    .cummax()
)

drawdown = (
    equity_curve
    /
    peak
    - 1
)

plt.figure(
    figsize=(12,6)
)

plt.plot(
    drawdown
)

plt.title(
    "Strategy Drawdowns"
)

plt.ylabel(
    "Drawdown"
)

plt.tight_layout()

plt.savefig(
    "../../images/drawdown.png"
)

plt.show()

# ============================================================
# TRADE STATISTICS
# ============================================================

trades = (
    strategy_returns[
        strategy_returns != 0
    ]
)

print("\nTrade Statistics")

print(
    "Number of Trades:",
    len(trades)
)

print(
    "Average Trade Return:",
    trades.mean()
)

print(
    "Best Trade:",
    trades.max()
)

print(
    "Worst Trade:",
    trades.min()
)

# ============================================================
# EXPORT FULL BACKTEST
# ============================================================

df.to_csv(
    "../../data/processed/backtest_output.csv"
)

print(
    "\nbacktest_output.csv saved."
)

# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n" + "="*60)
print("BACKTEST COMPLETE")
print("="*60)


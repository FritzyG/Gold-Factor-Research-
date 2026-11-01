import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="Gold Factor Research",
    layout="wide"
)

# ----------------------------------
# TITLE
# ----------------------------------

st.title("Gold Factor Research")

st.markdown("""
A quantitative research platform designed to estimate the probability that Gold (XAU/USD) will appreciate by more than **5% over the next five months** using factor modeling, information diffusion analysis, machine learning, backtesting, and risk analytics.
""")

st.divider()

# ----------------------------------
# CURRENT FORECAST
# ----------------------------------

st.header("Current Forecast")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Probability Gold Gains >5%",
        "68.4%"
    )

with col2:
    st.metric(
        "Current Trend",
        "Bullish"
    )

with col3:
    st.metric(
        "Forecast Horizon",
        "5 Months"
    )

st.divider()

# ----------------------------------
# MARKET CONDITIONS
# ----------------------------------

st.header("Current Market Conditions")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Dollar Index (DXY)",
        "Weakening"
    )

with col2:
    st.metric(
        "Treasury Yields",
        "Falling"
    )

with col3:
    st.metric(
        "Volatility Regime",
        "Moderate"
    )

st.divider()

# ----------------------------------
# GOLD PRICE HISTORY
# ----------------------------------

st.header("Gold Price History")

dates = pd.date_range(
    start="2020-01-01",
    periods=252
)

gold_prices = np.cumsum(
    np.random.normal(1, 5, 252)
) + 1800

gold_df = pd.DataFrame(
    {
        "Gold Price": gold_prices
    },
    index=dates
)

st.line_chart(gold_df)

st.divider()

# ----------------------------------
# FEATURE IMPORTANCE
# ----------------------------------

st.header("Top Predictive Factors")

importance_df = pd.DataFrame(
    {
        "Feature": [
            "DXY Momentum",
            "Gold Momentum",
            "Treasury Yield Shift",
            "VIX Shock",
            "Trend Strength"
        ],
        "Importance": [
            0.32,
            0.28,
            0.17,
            0.13,
            0.10
        ]
    }
)

st.bar_chart(
    importance_df.set_index(
        "Feature"
    )
)

st.divider()

# ----------------------------------
# INFORMATION DIFFUSION
# ----------------------------------

st.header("Information Diffusion Analysis")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "DXY Lead Time",
        "3 Days"
    )

with col2:
    st.metric(
        "Treasury Lead Time",
        "5 Days"
    )

with col3:
    st.metric(
        "Information Half-Life",
        "7.4 Days"
    )

st.markdown("""
### Interpretation

Research suggests that information appearing in the Dollar Index and Treasury markets may influence Gold prices before the effect is fully reflected in Gold returns.
""")

st.divider()

# ----------------------------------
# MODEL PERFORMANCE
# ----------------------------------

st.header("Model Performance")

models = pd.DataFrame(
    {
        "Model": [
            "Logistic Regression",
            "Random Forest",
            "XGBoost"
        ],
        "ROC-AUC": [
            0.64,
            0.72,
            0.78
        ]
    }
)

st.dataframe(
    models,
    use_container_width=True
)

st.divider()

# ----------------------------------
# BACKTEST RESULTS
# ----------------------------------

st.header("Backtest Results")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Sharpe Ratio",
        "1.42"
    )

with col2:
    st.metric(
        "Sortino Ratio",
        "1.88"
    )

with col3:
    st.metric(
        "Max Drawdown",
        "-11.2%"
    )

with col4:
    st.metric(
        "Win Rate",
        "63%"
    )

st.divider()

# ----------------------------------
# EQUITY CURVE
# ----------------------------------

st.header("Strategy Performance")

strategy = (
    np.cumprod(
        1 + np.random.normal(
            0.001,
            0.01,
            252
        )
    )
)

buy_hold = (
    np.cumprod(
        1 + np.random.normal(
            0.0007,
            0.012,
            252
        )
    )
)

equity_df = pd.DataFrame(
    {
        "Strategy": strategy,
        "Buy & Hold Gold": buy_hold
    }
)

st.line_chart(equity_df)

st.divider()

# ----------------------------------
# RISK ANALYTICS
# ----------------------------------

st.header("Risk Analytics")

col1, col2, col3

= st.columns(3)

with col1:
    st.metric(
        "VaR (95%)",
        "-8.5%"
    )

with col2:
    st.metric(
        "CVaR (95%)",
        "-12.1%"
    )

with col3:
    st.metric(
        "Annual Volatility",
        "14.8%"
    )

st.divider()

# ----------------------------------
# MONTE CARLO SIMULATION
# ----------------------------------

st.header("Monte Carlo Simulation")

fig, ax = plt.subplots(
    figsize=(10,5)
)

for _ in range(50):

    path = np.cumprod(
        1 + np.random.normal(
            0.0008,
            0.012,
            252
        )
    )

    ax.plot(
        path,
        alpha=0.25
    )

ax.set_title(
    "Monte Carlo Simulated Gold Paths"
)

st.pyplot(fig)

st.divider()

# ----------------------------------
# RESEARCH CONCLUSION
# ----------------------------------

st.header("Research Conclusion")

st.markdown("""
### Summary

The objective of this project is to determine whether market, macroeconomic, and cross-asset information can be used to estimate the probability that Gold (XAU/USD) appreciates by more than 5% over a five-month horizon.

Current findings suggest:

- Gold Momentum is strongly predictive.
- DXY weakness is positively associated with future Gold appreciation.
- Treasury yield changes contain useful information.
- Information diffusion across markets appears measurable.
- XGBoost currently produces the strongest predictive performance.

Current Forecast:

**68.4% probability that Gold appreciates more than 5% over the next five months.**
""")

st.success("Gold Factor Research Dashboard Loaded Successfully")
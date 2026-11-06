import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Gold Factor Research",
    layout="wide"
)

# ==================================================
# TITLE
# ==================================================

st.title("Gold Factor Research")

st.markdown("""
A quantitative research platform investigating whether Gold (XAU/USD)
can appreciate more than 5% over the next five months using:

- Factor Modeling
- Information Diffusion Analysis
- Machine Learning
- Portfolio Backtesting
- Risk Analytics
""")

# ==================================================
# LOAD PROJECT FILES
# ==================================================

try:

    predictions = pd.read_csv(
        "../data/processed/model_predictions.csv",
        index_col=0
    )

except:

    predictions = None

try:

    model_results = pd.read_csv(
        "../reports/model_results.csv"
    )

except:

    model_results = None

try:

    backtest_results = pd.read_csv(
        "../reports/backtest_results.csv"
    )

except:

    backtest_results = None

# ==================================================
# CURRENT FORECAST
# ==================================================

st.divider()

st.header("Current Gold Forecast")

if predictions is not None:

    current_probability = (
        predictions["probability"]
        .iloc[-1]
        * 100
    )

    st.metric(
        label="Probability Gold Gains >5% In 5 Months",
        value=f"{current_probability:.2f}%"
    )

else:

    st.warning(
        "Run notebook 04 first to generate predictions."
    )

# ==================================================
# MARKET SIGNAL
# ==================================================

st.divider()

st.header("Current Market Signal")

if predictions is not None:

    signal = predictions["signal"].iloc[-1]

    if signal == 1:

        st.success(
            "Model Signal: LONG GOLD"
        )

    else:

        st.error(
            "Model Signal: NO POSITION"
        )

# ==================================================
# MODEL PERFORMANCE
# ==================================================

st.divider()

st.header("Machine Learning Model Performance")

if model_results is not None:

    st.dataframe(
        model_results,
        use_container_width=True
    )

else:

    st.warning(
        "model_results.csv not found."
    )

# ==================================================
# FEATURE IMPORTANCE
# ==================================================

st.divider()

st.header("Research Factors")

factor_data = pd.DataFrame({

    "Factor": [

        "6 Month Momentum",

        "3 Month Momentum",

        "Dollar Index",

        "Treasury Yields",

        "Relative Strength",

        "Volatility"

    ]
})

st.dataframe(
    factor_data,
    use_container_width=True
)

st.markdown("""
The project investigates whether these factors contain predictive information regarding future Gold returns.
""")

# ==================================================
# PROBABILITY HISTORY
# ==================================================

st.divider()

st.header("Probability Forecast History")

if predictions is not None:

    probability_chart = (
        predictions["probability"]
        * 100
    )

    st.line_chart(
        probability_chart
    )

# ==================================================
# STRATEGY VS BUY AND HOLD
# ==================================================

st.divider()

st.header("Strategy Performance")

if predictions is not None:

    if (
        "strategy_equity"
        in predictions.columns
        and
        "buyhold_equity"
        in predictions.columns
    ):

        comparison = predictions[
            [
                "strategy_equity",
                "buyhold_equity"
            ]
        ]

        st.line_chart(
            comparison
        )

# ==================================================
# BACKTEST METRICS
# ==================================================

st.divider()

st.header("Backtest Results")

if backtest_results is not None:

    cols = st.columns(
        len(backtest_results.columns)
    )

    for idx, col in enumerate(
        backtest_results.columns
    ):

        value = (
            backtest_results[col]
            .iloc[0]
        )

        cols[idx].metric(
            col,
            str(round(value,4))
        )

else:

    st.warning(
        "backtest_results.csv not found."
    )

# ==================================================
# MONTE CARLO DEMO
# ==================================================

st.divider()

st.header("Monte Carlo Simulation")

fig, ax = plt.subplots(
    figsize=(10,5)
)

for _ in range(50):

    path = np.cumprod(

        1 +
        np.random.normal(
            0.0008,
            0.015,
            252
        )
    )

    ax.plot(
        path,
        alpha=0.2
    )

ax.set_title(
    "Simulated Portfolio Paths"
)

st.pyplot(fig)

# ==================================================
# PROJECT WORKFLOW
# ==================================================

st.divider()

st.header("Project Workflow")

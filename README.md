# Project Guide for Reviewers

Thank you for reviewing this project.

This repository was developed to demonstrate quantitative research, machine learning, financial analysis, and software engineering skills through the investigation of a real-world investment hypothesis:

> Can Gold (XAU/USD) appreciate by more than 5% over the next five months, and can that probability be estimated using market, macroeconomic, and cross-asset information?

The project follows the same workflow commonly used in quantitative research, systematic investing, and financial data science.

---

# Recommended Review Order

## 1. Start with the Research Question

Location:

```text
README.md
```

This section outlines:

- The investment hypothesis
- Research objectives
- Forecast horizon
- Expected outcomes

Time Required:

```text
1 minute
```

---

## 2. Review the Data Analysis

Location:

```text
notebooks/01_eda.ipynb
```

This notebook explores:

- Historical Gold performance
- Return distributions
- Volatility
- Drawdowns
- Market correlations

Key Question:

```text
What does historical Gold behavior look like?
```

Time Required:

```text
2-3 minutes
```

---

## 3. Review Factor Research

Location:

```text
notebooks/02_factor_research.ipynb
```

This notebook examines:

- Momentum factors
- Trend indicators
- Volatility regimes
- Relative strength metrics
- Macroeconomic factors

Key Question:

```text
Which variables appear to influence future Gold returns?
```

Time Required:

```text
3-5 minutes
```

---

## 4. Review Information Diffusion Research

Location:

```text
notebooks/03_information_diffusion.ipynb
```

This section investigates how information propagates through financial markets before being reflected in Gold prices.

Topics include:

- Lead-lag relationships
- Cross-asset information flow
- Treasury yield effects
- Dollar index effects
- Granger causality testing

Key Question:

```text
Do other markets provide predictive information for Gold?
```

Time Required:

```text
3-5 minutes
```

---

## 5. Review Predictive Models

Location:

```text
src/models/

notebooks/04_model_and_backtest.ipynb
```

Models evaluated:

- Logistic Regression
- Random Forest
- XGBoost

Performance metrics include:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

Key Question:

```text
Can future Gold returns be predicted better than chance?
```

Time Required:

```text
3-5 minutes
```

---

## 6. Review Backtesting Results

Location:

```text
src/backtest/
```

This section measures how the research framework would have performed historically.

Performance metrics include:

- Total Return
- CAGR
- Sharpe Ratio
- Sortino Ratio
- Win Rate
- Maximum Drawdown

Key Question:

```text
Would the strategy have generated risk-adjusted returns?
```

Time Required:

```text
2-3 minutes
```

---

## 7. Review Risk Analytics

Location:

```text
src/risk/
```

Metrics include:

- Value at Risk (VaR)
- Conditional Value at Risk (CVaR)
- Drawdown Analysis
- Volatility Analysis
- Monte Carlo Simulation

Key Question:

```text
What risks are associated with the strategy?
```

Time Required:

```text
2 minutes
```

---

## 8. Review Dashboard

Location:

```text
dashboard/
```

The Streamlit dashboard consolidates:

- Current Forecast Probability
- Model Outputs
- Feature Importance
- Risk Metrics
- Backtest Performance
- Monte Carlo Results

Key Question:

```text
How can research results be monitored and communicated effectively?
```

Time Required:

```text
1-2 minutes
```

---

# Technical Skills Demonstrated

### Quantitative Finance

- Factor Research
- Information Diffusion Analysis
- Lead-Lag Detection
- Portfolio Analytics
- Backtesting
- Risk Management
- Statistical Modeling

### Machine Learning

- Classification Models
- Feature Engineering
- Time-Series Validation
- Predictive Analytics
- Model Interpretation

### Software Engineering

- Python Development
- Modular Project Architecture
- Data Pipelines
- Dashboard Development
- Automated Reporting

### Data Science

- Data Cleaning
- Exploratory Data Analysis
- Visualization
- Statistical Testing
- Monte Carlo Simulation

---

# Project Deliverables

The project produces:

- Historical market analysis
- Factor research findings
- Information diffusion research
- Predictive probability forecasts
- Model performance comparisons
- Strategy backtests
- Risk analysis reports
- Interactive dashboard visualizations

---

# Final Objective

The objective of this project is not simply to forecast Gold prices.

The objective is to build and evaluate a systematic quantitative research framework capable of estimating the probability that Gold (XAU/USD) appreciates by more than 5% over a five-month investment horizon using market, macroeconomic, and cross-asset information.

This repository demonstrates the complete research lifecycle from hypothesis generation and data collection to predictive modeling, risk analysis, and decision support.
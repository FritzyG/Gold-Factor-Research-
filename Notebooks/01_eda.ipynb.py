import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("ggplot")

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)
df = pd.read_csv(
    "../data/raw/market_data.csv",
    index_col=0,
    parse_dates=True
)
df.head()
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
df.info()
missing = pd.DataFrame(
    df.isnull().sum(),
    columns=["Missing Values"]
)

missing.sort_values(
    "Missing Values",
    ascending=False
)
df.describe().T
plt.figure(figsize=(14,6))

plt.plot(
    df.index,
    df["gold"],
    linewidth=2
)

plt.title("Gold Price History")
plt.xlabel("Date")
plt.ylabel("Price")

plt.show()
df["gold_return"] = df["gold"].pct_change()

df[["gold","gold_return"]].head()
print("Mean Daily Return:", df["gold_return"].mean())
print("Daily Volatility:", df["gold_return"].std())
plt.figure(figsize=(12,6))

plt.hist(
    df["gold_return"].dropna(),
    bins=50
)

plt.title("Distribution of Daily Gold Returns")
plt.xlabel("Return")
plt.ylabel("Frequency")

plt.show()
df["future_return_5m"] = (
    df["gold"].shift(-105)
    /
    df["gold"]
    - 1
)

df[["future_return_5m"]].head()
df["target"] = (
    df["future_return_5m"] > 0.05
).astype(int)

df[["future_return_5m","target"]].head()
probability = df["target"].mean()

print(
    f"Probability Gold Gains More Than 5% Within 5 Months: {probability:.2%}"
)
df["target"].value_counts()
df["target"].value_counts().plot(
    kind="bar",
    figsize=(8,5)
)

plt.title(
    "Frequency of +5% Gold Returns Within 5 Months"
)

plt.show()
plt.figure(figsize=(12,6))

plt.hist(
    df["future_return_5m"].dropna(),
    bins=40
)

plt.title(
    "Distribution of Gold 5-Month Forward Returns"
)

plt.xlabel("Forward Return")
plt.ylabel("Count")

plt.show()
df["rolling_vol_20"] = (
    df["gold_return"]
    .rolling(20)
    .std()
    *
    np.sqrt(252)
)

df[["rolling_vol_20"]].tail()
df["rolling_vol_20"] = (
    df["gold_return"]
    .rolling(20)
    .std()
    *
    np.sqrt(252)
)

df[["rolling_vol_20"]].tail()
plt.figure(figsize=(14,6))

plt.plot(
    df.index,
    df["rolling_vol_20"]
)

plt.title(
    "20-Day Annualized Gold Volatility"
)

plt.xlabel("Date")
plt.ylabel("Volatility")

plt.show()
wealth = (
    1 +
    df["gold_return"].fillna(0)
).cumprod()

wealth.head()
peak = wealth.cummax()

drawdown = (
    wealth
    /
    peak
    - 1
)

df["drawdown"] = drawdown
plt.figure(figsize=(14,6))

plt.plot(
    df.index,
    df["drawdown"]
)

plt.title("Gold Drawdowns")

plt.xlabel("Date")
plt.ylabel("Drawdown")

plt.show()

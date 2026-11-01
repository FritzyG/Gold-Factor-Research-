import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(
    "../data/raw/market_data.csv",
    index_col=0
)

# Gold Price Chart

plt.figure(figsize=(12,6))

plt.plot(df["gold"])

plt.title(
    "Gold Price History"
)

plt.savefig(
    "../images/gold_price.png"
)

plt.close()


# Correlation Heatmap

plt.figure(figsize=(10,8))

sns.heatmap(
    df.corr(numeric_only=True),
    cmap="coolwarm"
)

plt.title(
    "Correlation Heatmap"
)

plt.savefig(
    "../images/correlation_heatmap.png"
)

plt.close()

print("Images Created")
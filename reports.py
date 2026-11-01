import pandas as pd


def create_report(df):

    probability = (
        df["target"]
        .mean()
        * 100
    )

    report = f"""
# Gold Factor Research Report

## Research Question

Can Gold (XAU/USD) appreciate
more than 5% over the next
five months?

## Key Findings

Historical Probability:
{probability:.2f}%

## Assets Included

- Gold
- DXY
- SPY
- VIX
- Silver
- Treasury Yields

## Features

- Momentum
- Trend
- Volatility
- Information Diffusion

## Conclusion

Gold behavior appears linked
to momentum, treasury yields,
and dollar strength.

Further machine learning
analysis is required.
"""

    with open(
        "research_summary.md",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(report)

    print("Report Generated")


if __name__ == "__main__":

    df = pd.read_csv(
        "../data/processed/model_data.csv"
    )

    create_report(df)
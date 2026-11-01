# notebooks.py

import pandas as pd

from src.factors.momentum import add_momentum_factors
from src.factors.trend import add_trend
from src.factors.volatility import add_volatility

from src.diffusion.dxy_diffusion import add_dxy_features
from src.diffusion.treasury_diffusion import add_treasury_features


def load_data():

    df = pd.read_csv(
        "data/raw/market_data.csv",
        index_col=0,
        parse_dates=True
    )

    return df


def build_features(df):

    print("Creating Momentum Features...")
    df = add_momentum_factors(df)

    print("Creating Trend Features...")
    df = add_trend(df)

    print("Creating Volatility Features...")
    df = add_volatility(df)

    print("Creating DXY Diffusion Features...")
    df = add_dxy_features(df)

    print("Creating Treasury Features...")
    df = add_treasury_features(df)

    return df


def create_target(df):

    df["future_return_5m"] = (
        df["gold"].shift(-105)
        /
        df["gold"]
        - 1
    )

    df["target"] = (
        df["future_return_5m"] > 0.05
    ).astype(int)

    return df


def save_dataset(df):

    df.to_csv(
        "data/processed/model_data.csv"
    )

    print(
        "Dataset saved successfully."
    )


def main():

    print("Loading Data...")
    df = load_data()

    print("Engineering Features...")
    df = build_features(df)

    print("Creating Target Variable...")
    df = create_target(df)

    print("Saving Dataset...")
    save_dataset(df)

    print("Complete.")
    print(df.head())


if __name__ == "__main__":
    main()
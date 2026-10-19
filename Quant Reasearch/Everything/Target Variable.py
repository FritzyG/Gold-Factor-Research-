import pandas as pd


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
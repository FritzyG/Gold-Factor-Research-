import numpy as np


def add_volatility_features(df):

    returns = np.log(
        df["gold"] /
        df["gold"].shift(1)
    )

    df["vol_20"] = (
        returns
        .rolling(20)
        .std()
        * np.sqrt(252)
    )

    df["vol_60"] = (
        returns
        .rolling(60)
        .std()
        * np.sqrt(252)
    )

    return df
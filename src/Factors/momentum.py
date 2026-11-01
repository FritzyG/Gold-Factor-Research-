import pandas as pd


def add_momentum_factors(df):

    # 1 month momentum
    df["mom_1m"] = (
        df["gold"].pct_change(21)
    )

    # 3 month momentum
    df["mom_3m"] = (
        df["gold"].pct_change(63)
    )

    # 6 month momentum
    df["mom_6m"] = (
        df["gold"].pct_change(126)
    )

    return df


if __name__ == "__main__":

    df = pd.read_csv(
        "../../data/raw/market_data.csv",
        index_col=0
    )

    df = add_momentum_factors(df)

    print(
        df[
            [
                "mom_1m",
                "mom_3m",
                "mom_6m"
            ]
        ].tail()
    )
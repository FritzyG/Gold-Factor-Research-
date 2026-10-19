def add_momentum(df):

    df["mom_1m"] = (
        df["gold"].pct_change(21)
    )

    df["mom_3m"] = (
        df["gold"].pct_change(63)
    )

    df["mom_6m"] = (
        df["gold"].pct_change(126)
    )

    return df
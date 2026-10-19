import yfinance as yf
import pandas as pd

assets = {
    "gold": "GLD",
    "spy": "SPY",
    "silver": "SLV",
    "vix": "^VIX",
    "oil": "CL=F",
    "dxy": "DX-Y.NYB",
    "us10y": "^TNX"
}

def download_data():

    all_data = pd.DataFrame()

    for name, ticker in assets.items():

        data = yf.download(
            ticker,
            start="2010-01-01",
            auto_adjust=True
        )

        all_data[name] = data["Close"]

    return all_data


if __name__ == "__main__":

    df = download_data()

    df.to_csv(
        "data/raw/market_data.csv"
    )

    print(df.tail())
import pandas as pd
import yfinance as yf

def load_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    df = yf.download(ticker, start=start, end=end)
    df.dropna(inplace=True)
    return df
# modules/data_fetcher.py

import yfinance as yf
import pandas as pd

def fetch_stock_data(tickers, start_date='2024-12-01', end_date='2024-12-31'):
    try:
        raw_data = yf.download(tickers, start=start_date, end=end_date, group_by='ticker', auto_adjust=False)
        if isinstance(raw_data.columns, pd.MultiIndex):
            adj_close = raw_data.loc[:, pd.IndexSlice[:, 'Adj Close']]
            adj_close.columns = [ticker for ticker, _ in adj_close.columns]
        else:
            adj_close = raw_data[['Adj Close']]
            adj_close.columns = tickers  

        return adj_close.dropna()
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()

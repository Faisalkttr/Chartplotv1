import streamlit as st
import yfinance as yf
import pandas as pd

@st.cache_data(ttl=3600)  # Cache data for 1 hour to optimize performance
def get_stock_data(tickers: list, start_date: str, end_date: str) -> pd.DataFrame:
    """Fetches Adjusted Close prices and structures them into a single clean DataFrame."""
    if not tickers:
        return pd.DataFrame()
    
    try:
        data = yf.download(tickers, start=start_date, end=end_date, progress=False)
        if data.empty:
            return pd.DataFrame()
        
        # Extract 'Adj Close' safely for single or multiple tickers
        if 'Adj Close' in data.columns:
            df = data['Adj Close']
        else:
            df = data['Close']
            
        # Standardize format if downloading only one ticker
        if isinstance(df, pd.Series):
            df = df.to_frame(name=tickers[0])
            
        return df.ffill().bfill()
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()

def calculate_relative_metrics(df: pd.DataFrame, base_ticker: str, target_tickers: list):
    """
    Computes:
    1. Indexed Cumulative Return (Base 100) starting from the selected window.
    2. Ratio charts (Target Price / Base Price) to pinpoint exact structural breakouts.
    """
    metrics = {}
    
    # 1. Base 100 Performance
    indexed_df = (df / df.iloc[0]) * 100
    metrics['indexed'] = indexed_df
    
    # 2. Ratios & Outperformance (Ratio = Target / Base)
    ratio_df = pd.DataFrame(index=df.index)
    if base_ticker in df.columns:
        for ticker in target_tickers:
            if ticker in df.columns and ticker != base_ticker:
                ratio_df[f"{ticker}/{base_ticker}"] = df[ticker] / df[base_ticker]
    metrics['ratios'] = ratio_df
    
    return metrics
# dashboard.py

import streamlit as st
from modules.fetch_data import fetch_stock_data
from modules.risk_meter import (
    calculate_daily_returns,
    calculate_portfolio_returns,
    calculate_portfolio_performance,
    calculate_historical_var,
    calculate_parametric_var
)
from modules.plots import (
    plot_return_histogram,
    plot_correlation_heatmap,
    plot_cumulative_returns
)
import pandas as pd
st.set_page_config(page_title="Portfolio Risk Analyzer", layout="centered")

st.title("📊 Portfolio Risk Analyzer")

# --- Input Section ---
st.sidebar.header("Portfolio Configuration")

tickers_input = st.sidebar.text_input("Enter stock tickers (comma separated)", "AAPL,GOOG,TSLA")
weights_input = st.sidebar.text_input("Enter weights (comma separated)", "0.33,0.33,0.34")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2024-12-31"))
confidence_level = st.sidebar.slider("Confidence Level for VaR", min_value=0.90, max_value=0.99, step=0.01, value=0.95)

# --- Parse Inputs ---
tickers = [ticker.strip().upper() for ticker in tickers_input.split(",")]
weights = [float(w.strip()) for w in weights_input.split(",")]

# --- Fetch and Process Data ---
data = fetch_stock_data(tickers, start_date=start_date, end_date=end_date)

if data.empty:
    st.error("❌ Failed to fetch data. Please check tickers and try again.")
else:
    daily_returns = calculate_daily_returns(data)
    portfolio_returns = calculate_portfolio_returns(daily_returns, weights)
    performance = calculate_portfolio_performance(portfolio_returns)
    hist_var = calculate_historical_var(portfolio_returns, confidence_level)
    param_var = calculate_parametric_var(portfolio_returns, confidence_level)

    # --- Display Metrics ---
    st.subheader("📈 Performance Summary")
    st.metric("Expected Annual Return", f"{performance['Annual Return']:.2%}")
    st.metric("Annual Volatility", f"{performance['Annual Volatility']:.2%}")
    st.metric("Sharpe Ratio", f"{performance['Sharpe Ratio']:.2f}")

    st.subheader("⚠️ Value at Risk (1-Day Horizon)")
    st.markdown(f"**Historical VaR ({int(confidence_level*100)}%):** -{hist_var:.2%}")
    st.markdown(f"**Parametric VaR ({int(confidence_level*100)}%):** -{param_var:.2%}")

    # --- Plots ---
    st.subheader("🔍 Portfolio Visualizations")

    st.markdown("**Cumulative Return:**")
    plot_cumulative_returns(portfolio_returns)

    st.markdown("**Return Distribution:**")
    plot_return_histogram(portfolio_returns, hist_var, confidence_level)

    st.markdown("**Correlation Heatmap:**")
    plot_correlation_heatmap(data)

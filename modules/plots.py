# modules/visualizer.py

import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_return_histogram(portfolio_returns, var_value, confidence_level=0.95):
    """
    Plot histogram of portfolio returns with VaR marked.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(portfolio_returns, bins=50, kde=True, color='skyblue')
    plt.axvline(-var_value, color='red', linestyle='--', label=f'{int(confidence_level*100)}% VaR')
    plt.title("Histogram of Portfolio Daily Returns")
    plt.xlabel("Daily Return")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    st.pyplot(plt.gcf())
    plt.clf()

def plot_correlation_heatmap(price_data):
    """
    Plot a heatmap showing correlations between asset prices.
    """
    daily_returns = price_data.pct_change().dropna()
    corr = daily_returns.corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title("Correlation Heatmap of Stocks")
    plt.tight_layout()
    st.pyplot(plt.gcf())
    plt.clf()

def plot_cumulative_returns(portfolio_returns):
    """
    Plot cumulative return of the portfolio over time.
    """
    cumulative_returns = (1 + portfolio_returns).cumprod()

    plt.figure(figsize=(10, 5))
    plt.plot(cumulative_returns, color='green')
    plt.title("Cumulative Portfolio Return")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.grid(True)
    plt.tight_layout()
    st.pyplot(plt.gcf())
    plt.clf()

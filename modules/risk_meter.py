# modules/risk_metrics.py

import pandas as pd
import numpy as np

def calculate_daily_returns(price_df):
    """
    Calculate daily percentage returns for each stock.
    """
    daily_returns = price_df.pct_change().dropna()
    return daily_returns

def calculate_portfolio_returns(daily_returns, weights):
    """
    Calculate daily portfolio returns using weights.
    """
    weights = np.array(weights)
    portfolio_returns = daily_returns.dot(weights)
    return portfolio_returns
def calculate_portfolio_performance(portfolio_returns, risk_free_rate=0.02):
    """
    Calculate expected annual return, volatility (std dev), and Sharpe ratio.
    Assumes 252 trading days in a year.
    """
    mean_daily_return = portfolio_returns.mean()
    std_daily_return = portfolio_returns.std()

    annual_return = mean_daily_return * 252
    annual_volatility = std_daily_return * np.sqrt(252)

    sharpe_ratio = (annual_return - risk_free_rate) / annual_volatility

    return {
        "Annual Return": annual_return,
        "Annual Volatility": annual_volatility,
        "Sharpe Ratio": sharpe_ratio
    }
from scipy.stats import norm

def calculate_historical_var(portfolio_returns, confidence_level=0.95):
    """
    Calculate Historical Value at Risk (VaR).
    """
    var = -np.percentile(portfolio_returns, (1 - confidence_level) * 100)
    return var

def calculate_parametric_var(portfolio_returns, confidence_level=0.95):
    """
    Calculate Parametric (Gaussian) Value at Risk (VaR).
    """
    mean = portfolio_returns.mean()
    std_dev = portfolio_returns.std()
    z_score = norm.ppf(1 - confidence_level)
    var = -(mean + z_score * std_dev)
    return var
# app.py

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


if __name__ == "__main__":
    portfolio = ['RELIANCE.NS', 'TATAMOTORS.NS']
    weights = [0.5,0.5]

    data = fetch_stock_data(portfolio, start_date='2020-01-01', end_date='2024-12-31')

    if not data.empty:
        print("Fetched price data")

        daily_returns = calculate_daily_returns(data)
        portfolio_returns = calculate_portfolio_returns(daily_returns, weights)
        performance = calculate_portfolio_performance(portfolio_returns)
        print("\nPortfolio Performance Metrics:")
        for metric, value in performance.items():
            print(f"{metric}: {value:.4f}")
        hist_var = calculate_historical_var(portfolio_returns)
        param_var = calculate_parametric_var(portfolio_returns)

        print("\n Value at Risk (95% confidence, 1-day horizon):")
        print(f"Historical VaR: {-hist_var:.4%}")
        print(f"Parametric VaR: {-param_var:.4%}")
    else:
        print(" Failed to fetch stock data.")
    plot_return_histogram(portfolio_returns, hist_var)
    plot_correlation_heatmap(data)
    plot_cumulative_returns(portfolio_returns)


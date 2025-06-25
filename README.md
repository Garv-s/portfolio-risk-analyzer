## 🚀 Features

- ✅ Fetch historical data from Yahoo Finance
- 📈 Compute returns, volatility, Sharpe ratio
- ⚠️ Calculate Value at Risk (VaR) - Historical & Parametric
- 📊 Correlation heatmap, cumulative return, and return histogram
- 🎛️ Streamlit-based interactive dashboard

---

## 📦 Tech Stack

| Component      | Tech Used              |
|----------------|------------------------|
| Backend        | Python 3.11            |
| Dashboard UI   | Streamlit              |
| Financial Data | `yfinance`             |
| Plots          | Matplotlib, Seaborn    |
| Risk Models    | NumPy, SciPy           |

---

## 🧠 How It Works

1. **Input tickers** and **weights**
2. Fetch stock data from Yahoo Finance
3. Compute:
   - Daily returns
   - Portfolio metrics
   - Value at Risk (VaR)
4. Visualize:
   - Cumulative returns
   - Return distribution + VaR line
   - Correlation heatmap

---

## 💻 Run Locally

git clone https://github.com/yourusername/portfolio-risk-analyzer.git
cd portfolio-risk-analyzer
pip install -r requirements.txt
streamlit run dashboard.py
📝 Sample Input

Tickers: AAPL,GOOG,TSLA
Weights: 0.33,0.33,0.34
Date Range: 2020-01-01 to 2024-12-31
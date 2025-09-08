import yfinance as yf

def fetch_stock_data(ticker: str):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    if not data.empty:
        last_close = data['Close'].iloc[-1]
        return {"ticker": ticker, "last_close": last_close}
    return {"ticker": ticker, "error": "No data found"}

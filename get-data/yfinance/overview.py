import yfinance as yf

data = yf.download("MSFT", period="1mo", interval="5m")

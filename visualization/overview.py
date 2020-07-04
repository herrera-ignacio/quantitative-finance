import pandas as pdimport datetime as dtimport yfinance as yfimport pandasimport matplotlib.pyplot as pltstocks = ["AMZN", "MSFT", "INTC", "GOOG", "INFY.NS"]start = dt.datetime.today() - dt.timedelta(30)end = dt.datetime.today()closing_prices = pd.DataFrame() # empty data frame which will be filledohlcv_data = {}for ticker in stocks:    ohlcv_data[ticker] = yf.download(ticker, start, end)    closing_prices[ticker] = ohlcv_data[ticker]["Adj Close"]    # Pandas visualization    closing_prices.plot()cp_standardized = (closing_prices - closing_prices.mean())/closing_prices.std()cp_standardized.plot()closing_prices.plot(subplots=True, layout=(3,2), title="Tech Stock Price Evolution", grid=True)# Matplotlib visualizationdaily_return = closing_prices.pct_change()fig, ax = plt.subplots()plt.style.use("ggplot")ax.set(title="Daily return on tech stocks", xlabel="Tech stocks", ylabel="Daily returns")plt.bar(daily_return.columns, daily_return.mean())
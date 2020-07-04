#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 14:49:21 2020

@author: ignacioromanherrera
"""

import datetime as dt
import yfinance as yf
import pandas

stocks = ["AMZN", "MSFT", "INTC", "GOOG", "INFY.NS"]
start = dt.datetime.today() - dt.timedelta(30)
end = dt.datetime.today()
closing_price = pandas.DataFrame() # empty data frame which will be filled
ohlcv_data = {}

for ticker in stocks:
    ohlcv_data[ticker] = yf.download(ticker, start, end)
    closing_price[ticker] = ohlcv_data[ticker]["Adj Close"]
    
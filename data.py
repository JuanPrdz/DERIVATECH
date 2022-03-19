# -*- coding: utf-8 -*-


# Conegexión y manejo de información en tiempo real
from finviz.screener import Screener
import finviz
filters = Screener.load_filter_dict()

some_filters = [filters["PEG"]["Under 1"], filters["Exchange"]["AMEX"]]
stock_list = Screener(filters=some_filters, order="ticker")
print(stock_list)


stock_list = Screener()
print(type(stock_list))


stock = finviz.get_stock('TSLA')
print(stock)

stock['Price']


stock_list = Screener(tickers=['TSLA', 'SQ', 'COIN', 'TWTR'])

a = stock_list.get_charts(period='d', chart_type='c', size='l', ta='1')

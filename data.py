# -*- coding: utf-8 -*-


# Conegexión y manejo de información en tiempo real
from finviz.screener import Screener
import finviz
import pandas as pd


# Individual Stocks 
Lista = ['AAPL','TSLA','MSFT']
Clave = finviz.get_stock(Lista[0])
Clave = pd.DataFrame.from_dict(Clave,orient='index')
for i in range(1,len(Lista)):
    A = finviz.get_stock(Lista[i])
    B = pd.DataFrame.from_dict(A,orient='index',columns=(Lista[i]))
    Clave = Clave.join(B)

B.columns['A']


# finviz.get_stock(Lista[i])

# Clave = finviz.get_stock('AAPL')
# Clave = pd.DataFrame.from_dict(Clave,orient='index')





# some_filters = [filters["PEG"]["Under 1"], filters["Exchange"]["AMEX"]]
# stock_list = Screener(filters=some_filters, order="ticker")
# print(stock_list)


# stock_list = Screener()
# print(type(stock_list))


# stock = finviz.get_stock('AAPL')
# print(stock)

# stock['Price']

# stock_list= Screener(table='Performance',order='Ticker',signal='New High',fil)
# print(stock_list)

# stock_list[3]
# pd.DataFrame.from_dict(A,orient='index')
# a = stock_list.get_charts(period='d', chart_type='c', size='l', ta='1')


##-----------------------------------------------------------------------------------------------------------------------------------###
# Indicidual Stocks 
Clave = finviz.get_stock('AAPL')
Clave = pd.DataFrame.from_dict(Clave,orient='index')

pd.DataFrame(Clave)



finviz.get_insider('АAPL')

finviz.get_news('AAPL')


finviz.get_analyst_price_targets('AAPL')









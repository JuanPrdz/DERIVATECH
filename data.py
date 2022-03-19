# -*- coding: utf-8 -*-


# Conegexión y manejo de información en tiempo real
from finviz.screener import Screener
import finviz
import pandas as pd


# Consultas de Claves indiciduales 
my_dict = finviz.get_stock("AAPL")
df = pd.DataFrame(list(my_dict.items()),columns = ['column1','column2'])
indice=df["column1"]
indice=indice.values
lista = ["TSLA", "AMZN", "MSFT"]
finfn = pd.DataFrame(index=indice)

for i in range(len(lista)):
    my_dicto = finviz.get_stock(lista[i])
    dff = pd.DataFrame(list(my_dicto.items()),columns = ['column1','column2'])
    finfn[i] = dff['column2'].values
finfn.columns = lista
finfn = finfn.T



# Se genera consultas en https://finviz.com/screener.ashx
filters = ['sec_financial']
stock_list= Screener(filters=filters,table='Performance',order='Ticker',signal='New High')
Data = pd.DataFrame.from_dict(stock_list.data)













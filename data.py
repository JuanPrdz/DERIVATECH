# -*- coding: utf-8 -*-


# Conegexión y manejo de información en tiempo real
from finviz.screener import Screener
import finviz
import pandas as pd


# Consultas de Claves indiciduales 
lista = ["AAPL", "AMZN", "ES=F"]
lista
finfn = pd.DataFrame()
for i in range(len(lista)):
    my_dicto = finviz.get_stock(lista[i])
    dff = pd.DataFrame(list(my_dicto.items()),columns = ['column1','column2'])
    finfn[i] = dff.column2

indiceD = finviz.get_stock(lista[0])
indiceDF = pd.DataFrame(list(indiceD.items()),columns = ['column1','column2'])
finfn = finfn.set_index(indiceDF.column1)
finfn.columns = lista
finfn = finfn.T


# Se genera consultas en https://finviz.com/screener.ashx
filters = ['sec_financial']
stock_list= Screener(filters=filters,table='Performance',order='Ticker',signal='New High')
Data = pd.DataFrame.from_dict(stock_list.data)











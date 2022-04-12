# -*- coding: utf-8 -*-


# Conegexión y manejo de información en tiempo real
from finviz.screener import Screener
import finviz
import pandas as pd
import Pruebas1 as iv

seleccion = iv.a




librero = {'Basic Materials':'sec_basicmaterials',
           'Communication Services':'sec_communicationservices',
           'Consumer Cyclical':'sec_consumercyclical',
           'Consumer Defensive':'sec_consumerdefensive',
           'Energy':'sec_energy',
           'Financial':'sec_financial',
           'Healthcare':'sec_healthcare',
           'Industrials':'sec_industrials',
           'Real Estate':'sec_realestate',
           'Techology':'sec_technology',
           'Utilities':'sec_utilities'}


b = librero[seleccion]

# Consultas de Claves indiciduales 
# my_dict = finviz.get_stock("AAPL")
# df = pd.DataFrame(list(my_dict.items()),columns = ['column1','column2'])
# indice=df["column1"]
# indice=indice.values
# lista = ["TSLA", "AMZN", "MSFT"]
# finfn = pd.DataFrame(index=indice)

# for i in range(len(lista)):
#     my_dicto = finviz.get_stock(lista[i])
#     dff = pd.DataFrame(list(my_dicto.items()),columns = ['column1','column2'])
#     finfn[i] = dff['column2'].values
# finfn.columns = lista
# finfn = finfn.T


#-------------------------------------------------------------



sectores = ['sec_basicmaterials','sec_communicationservices','sec_consumercyclical',
            'sec_consumerdefensive','sec_energy','sec_financial','sec_healthcare',
            'sec_industrials','sec_realestate','sec_technology','sec_utilities']

# Se genera consultas en https://finviz.com/screener.ashx
filters = [b,'marketcap']
stock_list= Screener(filters=filters,table='Valuation',order='-marketcap',signal='New High')
Data = pd.DataFrame.from_dict(stock_list.data)
Data = Data[['Ticker','Market Cap']]
Tickets = Data['Ticker']

Data['Ticker'][0]
# Se generara una lista de tickets para analisis técnico 




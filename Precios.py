# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 17:48:57 2022

@author: ivana
"""

from tkinter import *
from tkinter import ttk
import numpy as np
import pandas as pd
from yahoofinancials import YahooFinancials
import plotly.express as px
import scipy.optimize as opt
import pandas_datareader.data as web
import datetime as date
import mplfinance as mpf
import yfinance as yf
from scipy.stats import norm
import matplotlib.pyplot as plt
import data as dt

tickerr = dt.Tickets[:7]

#tickerr = ["AAPL", "FB", "SHOP", "C", "AMZN", "MSFT", "EPD", "KO", "TSLA","WMT"]
prices = web.DataReader(name = tickerr, data_source = "yahoo",
              start= "2022-01-01")["Adj Close"].dropna()


resultado=np.zeros(len(tickerr))
for i in range(len(tickerr)):
    datos=yf.download(tickerr[i], period='1d', interval='1m')
    price=datos.iloc[-1,3]
    resultado[i]=price
    

prices.iloc[-1,:] = resultado


#Analisis RSI 
# data = yf.download(tickers, period='1d', interval='1m')
data = prices

RSII = pd.DataFrame()
for i in range(len(tickerr)):
    
    delta = data.iloc[:,i].diff(1)
    delta.dropna(inplace=True)

    positive = delta.copy()
    negative = delta.copy()

    positive[positive < 0 ]=0
    negative[negative > 0 ]=0
    days = 14
    avrg_gain = positive.rolling(window=days).mean()
    avrg_loss = abs(negative.rolling(window=days).mean())

    rltv_strength = avrg_gain/avrg_loss
    RSI = 100-(100/(1+rltv_strength))

    combined = pd.DataFrame()
    combined["Close"] =  data.iloc[:,i]
    combined["RSI"] = RSI
    RSII[i] = RSI

    
RSII  = pd.DataFrame(RSII)
RSII.columns = tickerr
RSI_HOY = RSII.iloc[len(RSII)-1,:]


RSI_HOY=pd.DataFrame(RSI_HOY)
RSI_HOY


ws  = Tk()
ws.title('RSI Analysis')
ws.geometry('500x500')
#ws['bg'] = '#AC99F2'
game_frame = Frame(ws)
game_frame.pack()
my_game = ttk.Treeview(game_frame)
my_game['columns'] = ('TICKER','STATUS','PRICE')

my_game.column("#0", width=0,  stretch=NO)
my_game.column("TICKER",anchor=CENTER, width=80)
my_game.column("STATUS",anchor=CENTER,width=80)
my_game.column("PRICE",anchor=CENTER,width=80)

my_game.heading("#0",text="",anchor=CENTER)
my_game.heading("TICKER",text="TICKER",anchor=CENTER)
my_game.heading("STATUS",text="STATUS",anchor=CENTER)
my_game.heading("PRICE",text="PRICE",anchor=CENTER)

for i in range(len(tickerr)-1):
    if(RSI_HOY.iloc[i,0]<30):
        my_game.insert(parent='',index='end',text='', values=(tickerr[i],'BUY',np.round((resultado[i]),4)))
    if(RSI_HOY.iloc[i,0]>70):
        my_game.insert(parent='',index='end',text='', values=(tickerr[i],'SELL',np.round((resultado[i]),4)))
    if((RSI_HOY.iloc[i,0]>=30) & (RSI_HOY.iloc[i,0]<=70)):
        my_game.insert(parent='',index='end',text='', values=(tickerr[i],'HOLD',np.round((resultado[i]),4)))

my_game.pack()

import tkinter

Etiqueta = ttk.Label(ws,text='Select your stock')
Etiqueta.pack()

n = tkinter.StringVar(ws)
n.set(tickerr[0])

seleccion = tkinter.OptionMenu(ws,n,*tickerr)
seleccion.pack()

def Close():
    a = n.get()


exit_button = tkinter.Button(ws, text="Choose", command= lambda :Close())
exit_button.pack(pady=20)

    
ws.mainloop()


activo = n.get()



resultado=np.zeros(len(activo))
datos=yf.download(activo[0], period='1d', interval='1m')
price=datos.iloc[-1,3]
st = price 

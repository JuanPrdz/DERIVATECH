# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 11:00:08 2022

@author: ivana
"""

#import tkinter

# ventana = tkinter.Tk()
# ventana.geometry('400x300')

sectores = ['sec_basicmaterials','sec_communicationservices','sec_consumercyclical',
            'sec_consumerdefensive','sec_energy','sec_financial','sec_healthcare',
            'sec_industrials','sec_realestate','sec_technology','sec_utilities']


librero = {'Basic Materials':'sec_basicmaterials',
           'Communication Services':'sec_communicationservices',
           'Consumer Cyclical':'sec_consumercyclical'}


sectores_usuario = ['Basic','Communication','Consumer']




# # etiqueta = tkinter.Label(ventana,text='Elige tu sector',bg='blue')
# # etiqueta.pack(fill=tkinter.BOTH, expand=True)


# def saludo(nombre):
#     print('Hola ' + nombre)


# # boton1 = tkinter.Button(ventana , text = 'Presiona',padx=40,pady=50,command =  lambda: saludo("python"))
# # boton1.pack()





# CajaTexto = tkinter.Entry(ventana)
# CajaTexto.pack()


# etiqueta = tkinter.Label(ventana)
# etiqueta.pack()


# def texto_caja():
#     txt20 = CajaTexto.get()
#     etiqueta['text'] = txt20

# boton1 = tkinter.Button(ventana , text = 'Presiona',padx=40,pady=50,command=texto_caja)
# boton1.pack()


# Metodo Grid

# boton1 = tkinter.Button(ventana , text = 'Presiona',padx=10,pady=5)
# boton2 = tkinter.Button(ventana , text = 'Presiona',padx=10,pady=5)
# boton3 = tkinter.Button(ventana , text = 'Presiona',padx=10,pady=5)
# boton1.grid(row=0,column=0)
# boton2.grid(row=1,column=1)
# boton3.grid(row=2,column=2)
# ventana.mainloop()



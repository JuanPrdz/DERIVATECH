# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 16:48:00 2022

@author: ivana
"""

import tkinter

ventana = tkinter.Tk()
ventana.geometry('400x300')

sectores = ['sec_basicmaterials','sec_communicationservices','sec_consumercyclical',
            'sec_consumerdefensive','sec_energy','sec_financial','sec_healthcare',
            'sec_industrials','sec_realestate','sec_technology','sec_utilities']


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


sectores_usuario = ['Basic Materials','Communication Services'
                    ,'Consumer Cyclical','Consumer Defensive',
                    'Energy','Financial','Healthcare','Industrials',
                    'Real Estate','Techology','Utilities']

ventana.config(width=10)
ventana.config(height=2)



# def display_selected(choice):
#     print(n.get())
    

    
    
etiqueta = tkinter.Label(ventana,text='Elige tu sector')
etiqueta.pack()


n = tkinter.StringVar(ventana)
n.set(sectores_usuario[0])

seleccion = tkinter.OptionMenu(ventana,n,*sectores_usuario)
seleccion.pack()

# boton1 = tkinter.Button(ventana , text = 'Seleccionar',padx=10,pady=5)
# boton1.pack()

def Close():
    a = n.get()
    print(n.get())
    ventana.destroy()




exit_button = tkinter.Button(ventana, text="Elegir", command= lambda :Close())
exit_button.pack(pady=20)

ventana.mainloop()



a = n.get()







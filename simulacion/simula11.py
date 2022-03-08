#!/usr/bin/python3
#-*-coding: utf-8 -*-
#
# Metodo para validar una tarjeta de debito, empleando el
# algoritmo de construccion de los numeros pseudoaleatorios.
#
# Kiovahn Leon
# Mar/03/22
# al20760618.at.ite.dot.edu.dot.mx
#

from tkinter import *
from tkinter import ttk
from turtle import width

class tarjeta():
    def __init__(self,root):
        self.root=root
        root.title("Pago con tarjeta de credito")
        root.geometry("530x350")

        #######################
        #Seccion para indicar texto en el programa
        ########################
        vtarjeta=Frame(root)
        vtarjeta.grid(column=0, row=0, padx=(50,50), pady=(10,10))
        ttk.Label(vtarjeta,text="Escriba su tarjeta de credito",justify=LEFT).grid(sticky=W, column=0, row=0)

        datos_tarjeta=Frame(root)
        datos_tarjeta.grid(column=1, row=0, padx=(50,50), pady=(10,10))
        #Campo1
        self.campo1=Entry(datos_tarjeta,width=4)
        self.campo1.grid(column=0,row=0)

        self.campo2=Entry(datos_tarjeta,width=4)
        self.campo2.grid(column=1,row=0)

        self.campo3=Entry(datos_tarjeta,width=4)
        self.campo3.grid(column=2,row=0)

        self.campo4=Entry(datos_tarjeta,width=4)
        self.campo4.grid(column=3,row=0)

        #Seccion para el campo de verificacion
        ttk.Label(vtarjeta,text="Indique su codigo de verificacion (CV)",justify=LEFT).grid(sticky=W, column=0, row=1)

        self.cv=Entry(datos_tarjeta,width=4)
        self.cv.grid(column=0,row=1)
        ###############
        #Boton
        ###############
        botones=Frame(root)
        botones.grid(column=0,row=2,padx=(50,50),pady=(10,10))
        ttk.Button(botones,text="Comprar").grid(row=4,column=0)
        ttk.Button(botones,text="Salir",command=root.quit).grid(row=4,column=1)




def main():
    root=Tk()
    tarjeta(root)
    root.mainloop()
    

if __name__ == '__main__':
    main()
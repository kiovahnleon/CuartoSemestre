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

import sys, math
from operacionesEV import datos_tarjeta
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
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
        ttk.Button(botones,text="Comprar",command=lambda:tarjeta.verificar(self)).grid(row=4,column=0)
        ttk.Button(botones,text="Salir",command=root.quit).grid(row=4,column=1)
    def verificar(self):
        #validacion Campo 1
        try:
            dato1=int(self.campo1.get())
            if dato1<=0:
                messagebox.showerror("Error", "La lectura del primer campo es incorrecta")
                sys.exit(2)
            if dato1>=10000:
                messagebox.showerror("Error", "La lectura del primer campo es incorrecta")
                sys.exit(2)
        except ValueError:
            messagebox.showerror("Error","Se requiere del valor de los cuatro campos")
            sys.exit(2)
        #validacion Campo 2
        try:
            dato2=int(self.campo2.get())
            if dato2<=0:
                messagebox.showerror("Error", "La lectura del segundo campo es incorrecta")
                sys.exit(2)
            if dato2>=10000:
                messagebox.showerror("Error", "La lectura del segundo campo es incorrecta")
                sys.exit(2)
        except ValueError:
            messagebox.showerror("Error","Se requiere del valor de los cuatro campos")
            sys.exit(2)
        #validacion Campo 3
        try:
            dato3=int(self.campo3.get())
            if dato3<=0:
                messagebox.showerror("Error", "La lectura del tercer campo es incorrecta")
                sys.exit(2)
            if dato3>=10000:
                messagebox.showerror("Error", "La lectura del tercer campo es incorrecta")
                sys.exit(2)
        except ValueError:
            messagebox.showerror("Error","Se requiere del valor de los cuatro campos")
            sys.exit(2)
        #validacion Campo 4
        try:
            dato4=int(self.campo1.get())
            if dato4<=0:
                messagebox.showerror("Error", "La lectura del cuarto campo es incorrecta")
                sys.exit(2)
            if dato4>=10000:
                messagebox.showerror("Error", "La lectura del cuarto campo es incorrecta")
                sys.exit(2)
        except ValueError:
            messagebox.showerror("Error","Se requiere del valor de los cuatro campos")
            sys.exit(2)
        #validacion CV
        try:
            codigo_verificacion=int(self.cv.get())
            if codigo_verificacion<=0:
                messagebox.showerror("Error", "La lectura del CV es incorrecta")
                sys.exit(2)
            if codigo_verificacion>=10000:
                messagebox.showerror("Error", "La lectura del CV es incorrecta")
                sys.exit(2)
        except ValueError:
            messagebox.showerror("Error","Se requiere tengs un codigo de verificacion")
            sys.exit(2)
        #################
        #Aqui empieza la simulacion
        #################
        valores_tarjeta=datos_tarjeta(codigo_verificacion)
        #Separar los valores del codigo de verificacion
        digito1=math.floor(dato1/1000)
        digito2=math.floor((dato1%1000)/100)
        digito3=math.floor((dato1%100)/10)
        digito4=math.floor((dato1%100)%10)
        #se inicializa el contador
        contador=0
        if valores_tarjeta[digito2]==self.campo2.get():
            contador+=1
        if valores_tarjeta[digito3]==self.campo3.get():
            contador+=1
        if valores_tarjeta[digito4]==self.campo4.get():
            contador+=1
        if contador==3:
            messagebox.showinfo("Autorizada","Su compra ha sido Autorizada")
        else:
            messagebox.showerror("Rehcazada","Sucompra no fue autorizada")


def main():
    root=Tk()
    tarjeta(root)
    root.mainloop()
    

if __name__ == '__main__':
    main()
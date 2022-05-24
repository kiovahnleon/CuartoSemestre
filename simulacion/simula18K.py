#!/usr/bin/python
#
# Método que emplea ventana gráfica, donde el usuario
# selecciona el archivo CSV correspondiente con la información,
# a su vez, el cáculo correspondiente para determinar una
# probabilidad dada.
#
#
# May/03/22
# al.at.ite.dot.edu.dot.mx
#
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
import tkinter as tk
from ast import Lambda
import re
import matplotlib.pyplot as plt
import sys
import random
from turtle import bgcolor
from numpy import mean, array
import numpy as np
from pyparsing import col, line_end

# Nuevo, parte de cambiar por get


class Analisis(ttk.Frame):
    def __init__(self, root):
        self.root = root
        root.title("Cálculo de Probabilidad")
        root.geometry("650x500")

        #Menú#
        ################################################################
        my_menu = Menu(root, bg="lightgrey", fg="black")

        # Elementos que contendrá el menú
        file_menu = Menu(my_menu, tearoff=0)
        action_menu = Menu(my_menu, tearoff=0)

        # Etiquetas para los elementos del menú
        my_menu.add_cascade(label="Archivo", menu=file_menu)
        my_menu.add_cascade(label="Acciones", menu=action_menu)

        # Subelementos para file
        file_menu.add_command(
            label="Obtener", command=lambda: self.abrir_archivo())
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=root.quit)

        # Subelementos para action
        action_menu.add_command(label="Simular", command=lambda: self.simula())

        # Se crea el elemento (se compagina)
        root.configure(menu=my_menu)

        #Frames#
        ################################################################
        datos1 = Frame(root)  # Solicitud de información
        datos2 = Frame(root)  # Solicitud de información
        datos3 = Frame(root)  # Solicitud de información
        sol = Frame(root)  # Solicitud de valores
        botonSol = Frame(root)  # Botones
        botonOpciones = Frame(root)  # Botones
        botonAB = Frame(root)  # Botones
        botonMedia = Frame(root)
        botonDesv = Frame(root)
        botonModT = Frame(root)
        datos1.grid(column=0, row=0, padx=(50), pady=(10))
        datos2.grid(column=0, row=2, padx=(50), pady=(10))
        datos3.grid(column=0, row=4, padx=(50), pady=(10))
        sol.grid(column=0, row=3, padx=(50), pady=(10))
        botonOpciones.grid(column=0, row=1, padx=(50), pady=(10))
        botonAB.grid(column=1, row=3, padx=(50), pady=(10))
        botonSol.grid(column=0, row=5, padx=(50), pady=(10))
        botonModT.grid(column=1, row=0, padx=(50), pady=(10))
        botonMedia.grid(column=1, row=1, padx=(50), pady=(10))
        botonDesv.grid(column=1, row=2, padx=(50), pady=(10))

        #Campos#
        ################################################################
        ttk.Label(datos1, text="Tipo de simulación.",
                  justify=LEFT).grid(sticky=W, column=1, row=1)
        ttk.Label(datos2, text="Valor a calcular:", justify=LEFT).grid(
            sticky=W, column=1, row=2)
        ttk.Label(datos3, text="Solución", justify=LEFT).grid(
            sticky=W, column=1, row=3)

        #Entradas#
        ################################################################
        # Tipo de simulación

        self.opcion = IntVar()

        self.forma1 = ttk.Radiobutton(botonOpciones, text="Ecuacion", variable=self.opcion,
                                      value=1).grid(column=0, row=0)
        self.forma2 = ttk.Radiobutton(botonOpciones, text="Random", variable=self.opcion,
                                      value=2, ).grid(column=1, row=0)
        self.forma3 = ttk.Radiobutton(botonOpciones, text="Numpy", variable=self.opcion,
                                      value=3, ).grid(column=2, row=0)

        # Tipo de probabilidad
        self.opciones = ttk.Combobox(
            sol, width=10, state="readonly")
        self.opciones["values"] = ("<", "<=", ">=", ">", "a<=x<=b")
        self.opciones.grid(column=0, row=1)
        self.opciones.current()

        self.repeticiones = 30

        # Valor de cálculo

        ttk.Label(botonModT, text="Modifique si desea la Media y Desviacion",
                  justify=CENTER).pack()

        ttk.Label(botonAB, text="A",
                  justify=LEFT).pack()
        self.campoA = Entry(botonAB, width=6)
        self.campoA.pack()

        ttk.Label(botonAB, text="B",
                  justify=LEFT).pack()
        self.campoB = Entry(botonAB, width=6)
        self.campoB.pack()

        # Eleccion
        ttk.Label(botonMedia, text="Media",
                  justify=LEFT).pack()
        self.botonMedia = Entry(botonMedia, width=6)
        self.botonMedia.pack()

        ttk.Label(botonDesv, text="Desviacion",
                  justify=LEFT).pack()
        self.botonDesv = Entry(botonDesv, width=6)
        self.botonDesv.pack()

        # Mostrar la solución
        self.solucion = Entry(botonSol, width=13, state="readonly")
        self.solucion.pack()

        #Botones#
        ################################################################

        self.buttonA = tk.Button(botonSol,
                                 text="Simular",
                                 bg="#138ef2",
                                 fg="white",
                                 command=lambda:
                                 self.simula())

        self.buttonA.pack(side=LEFT, padx=0, pady=0)

        self.buttonB = tk.Button(botonSol,
                                 text="Salir",
                                 bg="#138ef2",
                                 fg="white", command=root.quit)

        self.buttonB.pack(side=RIGHT, padx=15, pady=20)
        self.root.mainloop()

        #Botones#
        ################################################################

    def abrir_archivo(self):
        self.datos = []

        # Solo se aceptan archivos .csv
        # ,('Archivo JPG','*.jpg')   !]!
        filetypes = [("Archivo CSV", "*.csv")]
        csv_path_file = fd.askopenfile(mode="r", filetypes=filetypes)
        if csv_path_file is not None:
            line_count = 0
            for row in csv_path_file:
                if line_count == 0:
                    line_count += 1
                else:
                    self.datos.append(float(row))

                    self.st_dev = np.std(self.datos)
        else:
            pass
        self.data = self.datos

        self.botonMedia.insert(0, round(mean(self.datos), 3))
        self.botonDesv.insert(0, round(float(str(self.st_dev)), 3))

################################################
    def lectura1(self, combo1):
        switch = {"Ecuacion": 1, "Random": 2, "Numpy": 3}
        return switch.get(combo1, "e")
################################################

    def lectura2(self, combo2):
        switch = {"<": 1, "<=": 2, ">=": 3, ">": 4, "a<=x<=b": 5}
        return switch.get(combo2, "e")

#############################################################
    def valores_normales(self, opcion):
        valores = []  # Aqui se almacenara la solucion
        try:
            promedio = float(self.botonMedia.get())
        except:
            promedio = np.average(self.data)

        try:
            desv = float(self.botonDesv.get())
        except:
            desv = np.average(self.data)

       # CALCULOS
        if opcion == 1:
            for i in range(self.repeticiones):
                suma = 0
                for j in range(12):
                    suma += random.random()
                x = promedio + desv * (suma-6)
                valores.append(x)
        elif opcion == 2:
            for i in range(self.repeticiones):
                valores.append(random.gauss(promedio, desv))
        else:
            valores = np.random.normal(promedio, desv, self.repeticiones)

        return (valores)
#######################################################

    def simula(self):
        # Validación para el combo de tipo de simulación
        if not self.opcion.get():
            messagebox.showerror(
                "Error", "No se seleccionó un tipo de simulación.")
            sys.exit(2)

        # Validación para el combo de tipo de problema para calcular
        if not self.opciones.get():
            messagebox.showerror(
                "Error", "No se seleccionó un tipo de problema.")
            sys.exit(2)

        # Validez para el campo a calcular
        try:
            valor_inicial = float(self.campoA.get())
            if valor_inicial <= 0:
                messagebox.showerror(
                    "Error", "Los valores no pueden ser negativos")
                sys.exit(2)
        except ValueError:
            messagebox.showerror(
                "Error", "Debe indicar los valores por calcular")
            sys.exit(2)

#####################################
        metodo_simular = self.lectura1(self.opcion.get())

        tipo_problema = self.lectura2(self.opciones.get())
        if tipo_problema == 5:
            # Validacion para el campo a<x<b
            try:
                valor_final = float(self.campoB.get())
                if valor_final <= 0:
                    messagebox.showerror(
                        "Error", "La probabilidad final no puede")
                    sys.exit(2)
            except ValueError:
                messagebox.showerror("Error", "Debe declarar el valor final")
                sys.exit(2)
            if valor_final <= valor_inicial:
                messagebox.showerror(
                    "Error", "No es posible realizar el calculo")
                sys.exit(2)

        # Valores de acuerdo a la distribucion normal
        valores = self.valores_normales(metodo_simular)

        suma = 0
        for j in valores:
            if tipo_problema == 1:
                if j < valor_inicial:
                    suma += 1
            elif tipo_problema == 2:
                if j <= valor_inicial:
                    suma += 1
            elif tipo_problema == 3:
                if j > valor_inicial:
                    suma += 1
            elif tipo_problema == 4:
                if j >= valor_inicial:
                    suma += 1
            else:
                if j <= valor_final and j >= valor_inicial:
                    suma += 1

        probabilidad = round((suma/self.repeticiones)*100, 2)

        re = StringVar()
        re.set(str(probabilidad))
        self.solucion.config(textvariable=re)
        var = []
        var = self.datos, valores
        fig = plt.figure(figsize=(10, 7))
        # Creating plot
        plt.boxplot(var)
        # show plot
        plt.show()


def main():
    root = Tk()
    Analisis(root)
    root.mainloop()


if __name__ == '__main__':
    main()

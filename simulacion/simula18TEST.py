#!/usr/bin/python
#
# Método que emplea ventana gráfica, donde el usuario
# selecciona el archivo CSV correspondiente con la información,
# a su vez, el cáculo correspondiente para determinar una
# probabilidad dada.
#
# Kiovahn Leon
# May/03/22
# .at.ite.dot.edu.dot.mx
#
from ast import Lambda
import re
import sys
import random
import tkinter as tk
from turtle import bgcolor, color, left
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

from pyparsing import col, line_end


class Analisis():
    def __init__(self, root):
        self.root = root
        root.title("Cálculo de Probabilidad")
        root.geometry("430x130")

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
        datos = Frame(root)  # Solicitud de información
        sol = Frame(root)  # Solicitud de valores
        botones = Frame(root)  # Botones
        datos.grid(column=0, row=0, padx=(50), pady=(10))
        sol.grid(column=1, row=0, padx=(50), pady=(10))
        botones.grid(column=0, row=2, padx=(50), pady=(10))

        #Campos#
        ################################################################
        ttk.Label(datos, text="Tipo de simulación.",
                  justify=LEFT).grid(sticky=W, column=1, row=1)
        ttk.Label(datos, text="Valor a calcular:", justify=LEFT).grid(
            sticky=W, column=1, row=2)
        ttk.Label(datos, text="Solución", justify=LEFT).grid(
            sticky=W, column=1, row=3)

        #Entradas#
        ################################################################
        # Tipo de simulación

        self.opcion = tk.IntVar()
        tk.Radiobutton(botones, text="Ecuación",
                       variable=self.opcion, value=1).pack(side=left)
        self.opcion = tk.IntVar()
        tk.Radiobutton(botones, text="Random",
                       variable=self.opcion, value=1).pack(side=left)
        self.opcion = tk.IntVar()
        tk.Radiobutton(botones, text="Numpy",
                       variable=self.opcion, value=1).pack(side=left)

        self.forma = ttk.Combobox(
            sol, width=10, state="readonly")
        self.forma["values"] = ("Ecuación", "Random", "Numpy")
        self.forma.grid(column=0, row=0)
        self.forma.current()

        # Tipo de probabilidad
        self.opciones = ttk.Combobox(
            sol, width=10, state="readonly")
        self.opciones["values"] = ("<", "<=", ">=", ">", "a<=x<=b")
        self.opciones.grid(column=0, row=1)
        self.opciones.current()

        # Valor de cálculo
        self.campoA = Entry(sol, width=6)
        self.campoA.grid(column=1, row=1)
        self.campoB = Entry(sol, width=6)
        self.campoB.grid(column=2, row=1)

        # Mostrar la solución
        self.solucion = Entry(sol, width=13)
        self.solucion.grid(column=0, row=3)

        #Botones#
        ################################################################
        ttk.Button(botones, text="Simular",
                   command=lambda: self.simula()).grid(row=4, column=0)
        ttk.Button(botones, text="Salir").grid(row=4, column=1)

        #Botones#
        ################################################################
        self.repeticiones = 30

    def abrir_archivo(self):
        datos = []
        # Solo se aceptan archivos .csv
        filetypes = [("Archivo CSV", "*.csv")]
        csv_path_file = fd.askopenfile(mode="r", filetypes=filetypes)
        if csv_path_file is not None:
            line_count = 0
            for row in csv_path_file:
                if line_count == 0:
                    line_count += 1
                else:
                    datos.append(float(row))
        else:
            pass
        self.data = datos

    def lectura1(self, combo1):
        switch = {"Ecuación": 1, "Random": 2, "Numpy": 3}
        return switch.get(combo1, "e")

    def lectura2(self, combo2):
        switch = {"<": 1, "<=": 2, ">=": 3, ">": 4, "a<=x<=b": 5}
        return switch.get(combo2, "e")

    def valores_normales(self, opcion):
        promedio = np.average(self.data)
        #self.solucion.delete(0, "end")
        #self.solucion.insert(0, promedio)
        desv = np.std(self.data)
        if opcion == 1:
            valores = []  # Almacena la solución.
            for i in range(self.repeticiones):
                suma = 0
                for j in range(12):
                    suma += random.random()
                x = promedio+desv*(suma-6)
                valores.append(x)
        elif opcion == 2:
            valores = []  # Almacena la solución.
            for i in range(self.repeticiones):
                valores.append(random.gauss(promedio, desv))
        else:
            valores = np.random.normal(promedio, desv, self.repeticiones)
        return valores

    def simula(self):
        # Validación para el combo de tipo de simulación
        if not self.forma.get():
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

        metodo_simular = self.lectura1(self.forma.get())
        tipo_problema = self.lectura2(self.opciones.get())

        if tipo_problema == 5:
            # Validación para el campo a <= x <= b
            try:
                valor_final = float(self.campoB.get())
                if valor_final <= 0:
                    messagebox.showerror(
                        "Error", "La probabilidad no puede ser negativa.")
                    sys.exit(2)
            except ValueError:
                messagebox.showerror("Error", "Debe declarar el valor final.")
                sys.exit(2)
            if valor_final <= valor_inicial:
                messagebox.showerror(
                    "Error", "No se puede realizar el cálculo.")
                sys.exit(2)

        # Valores de acuerdo a la distribución normal.
        valores = self.valores_normales(metodo_simular)
        suma = 0
        for i in valores:
            if tipo_problema == 1:
                if i < valor_inicial:
                    suma += 1
            elif tipo_problema == 2:
                if i <= valor_inicial:
                    suma += 1
            elif tipo_problema == 3:
                if i > valor_final:
                    suma += 1
            elif tipo_problema == 4:
                if i >= valor_inicial:
                    suma += 1
            else:
                if i <= valor_final and i >= valor_inicial:
                    suma += 1
        probabilidad = round((suma/self.repeticiones)*100, 2)
        self.solucion.delete(0, "end")
        self.solucion.insert(0, probabilidad)


def main():
    root = Tk()
    Analisis(root)
    root.mainloop()


if __name__ == '__main__':
    main()

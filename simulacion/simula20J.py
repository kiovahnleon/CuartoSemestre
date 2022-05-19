#!/usr/bin/env python
# -*-coding: utf-8 -*-
#
# Graficacion con Python empleando Matplotlib
#
# .at.ite.dot.edu.dot.mx
#
from logging import root
from matplotlib.pyplot import draw
import numpy as np
from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Graficar():
    def __init__(self, root):
        self.root = root
        root.title("Graficador")
        root.geometry("450x300")
        # Se crea el frame para solicitar la informacion
        datos = Frame(root, height=2, bd=1, relief=SUNKEN)
        datos.pack(fill=X, padx=5, pady=5)
        leyenda1 = ttk.Label(datos, text="Funcion", justify=LEFT)
        leyenda1.pack(fill=BOTH, expand=TRUE)
        # Captura de la funcion
        self.funcion = Entry(datos, width=16)
        self.funcion.pack()
        # Valores del intervalo a graficar
        # Intervalo inicial
        leyenda2 = ttk.Label(datos, text="Intervalo inicial", justify=LEFT)
        leyenda2.pack(fill=BOTH, expand=TRUE)
        self.campoa = Entry(datos, width=16)
        self.campoa.pack()
        # Intervalo final
        leyenda3 = ttk.Label(datos, text="Intervalo inicial", justify=LEFT)
        leyenda3.pack(fill=BOTH, expand=TRUE)
        self.campob = Entry(datos, width=16)
        self.campob.pack()
        # Se crea el Frame para los botones
        botones = Frame(root, height=5, bd=1, relief=SUNKEN)
        botones.pack(fill=X, padx=5, pady=5)
        ttk.Button(botones, text="Graficar",
                   command=lambda: self.plot()).grid(row=4, column=0)
        ttk.Button(botones, text="Salir",
                   command=root.quit).grid(row=4, column=1)

    def plot(self):
        # Primero, se crea la figura contenedora
        fig = Figure(figsize=(5, 5), dpi=100)
        # Se crea el intervalo
        x = np.arange(float(self.campoa.get()), float(self.campob.get()))
        y = eval(self.funcion.get())
        # se crea una sub - figura
        plot1 = fig.add_subplot(111)
        # se grafica
        plot1.plot(x, y)
        # se añade a Tkinter como un elemento Canvas
        canvas = FigureCanvasTkAgg(fig, self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()


def main():
    root = Tk()
    Graficar(root)
    root.mainloop()


if __name__ == '__main__':
    main()

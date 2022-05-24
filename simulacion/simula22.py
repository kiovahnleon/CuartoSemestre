#!/usr/bin/python
#
# Graficacion con python empleando matplotlib
#
#
# May/13/22
# .at.ite.dot.edu.dot.mx
#

import sys
import numpy as np
from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
from scipy import stats
import math


class Graficar():
    def __init__(self, root):
        self.root = root
        root.title("Enfriamiento")
        root.geometry("450x250")

        datos = Frame(root, height=2, bd=1, relief=SUNKEN)
        datos.pack(fill=X, padx=5, pady=5)

        # Tiempo inicial
        leyenda2 = ttk.Label(datos, text="Tiempo Inicial", justify=LEFT)
        leyenda2.pack(fill=BOTH, expand=True)
        self.tiempoInicial = Entry(datos, width=16)
        self.tiempoInicial.pack()

        # Temperatura inicial
        leyenda2 = ttk.Label(datos, text="Temperatura Inicial", justify=LEFT)
        leyenda2.pack(fill=BOTH, expand=True)
        self.temperaturaInicial = Entry(datos, width=16)
        self.temperaturaInicial.pack()

        # Tiempo final
        leyenda3 = ttk.Label(datos, text="Tiempo final", justify=LEFT)
        leyenda3.pack(fill=BOTH, expand=True)
        self.tiempoFinal = Entry(datos, width=16)
        self.tiempoFinal.pack()

        # Temperatura final
        leyenda4 = ttk.Label(datos, text="Temperatura Final", justify=LEFT)
        leyenda4.pack(fill=BOTH, expand=True)
        self.temperaturaFinal = Entry(datos, width=16)
        self.temperaturaFinal.pack()

        # Temperatura medio ambiente
        leyenda5 = ttk.Label(
            datos, text="Temperatura Medio Ambiente", justify=LEFT)
        leyenda5.pack(fill=BOTH, expand=True)
        self.TmedioAmbiente = Entry(datos, width=16)
        self.TmedioAmbiente.pack()

        # se crea frame para los botonoes
        botones = Frame(root, height=2, bd=1, relief=SUNKEN)
        botones.pack(fill=X, padx=5, pady=5)
        ttk.Button(botones, text="Graficar",
                   command=lambda: self.resolver()).grid(row=4, column=0)
        ttk.Button(botones, text="Salir",
                   command=root.quit).grid(row=4, column=1)

    def parametro(self):
        x0 = int(self.tiempoInicial.get())
        y0 = float(self.temperaturaInicial.get())
        x1 = int(self.tiempoFinal.get())
        y1 = float(self.temperaturaFinal.get())
        x = []
        y = []
        x.append(x0)
        x.append(x1)
        y.append(math.log(y0))
        y.append(math.log(y1))
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        return (slope)

    def f(self, x, y):
        k = self.parametro()
        TA = float(self.TmedioAmbiente.get())
        return (k*(y-TA))

    def rk4(self, f, x0, y0, x1, n):
        vx = [0] * (n + 1)
        vy = [0] * (n + 1)
        h = (x1 - x0) / float(n)
        vx[0] = x = x0
        vy[0] = y = y0
        for i in range(1, n + 1):
            k1 = h * f(x, y)
            k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
            k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
            k4 = h * f(x + h, y + k3)
            vx[i] = x = x0 + i * h
            vy[i] = y = y + (k1 + k2 + k2 + k3 + k3 + k4) / 6
        return vx, vy

    def resolver(self):
        # verificar tiempo inicial
        try:
            tiempo_inicial = int(self.tiempoInicial.get())
            if tiempo_inicial < 0:
                messagebox.showerror(
                    'Error', 'El tiempo no Puede ser Negativo')
                sys.exit(2)
        except ValueError:
            messagebox.showerror(
                'Error', 'Se debe decarar el tiempo inicial')
            sys.exit(2)
        # verificar temperatura inicial
        try:
            temperatura_inicial = float(self.temperaturaInicial.get())
            if temperatura_inicial <= 0:
                messagebox.showerror(
                    'Error', 'La temperatura no Puede ser Negativo')
                sys.exit(2)
        except ValueError:
            messagebox.showerror(
                'Error', 'Se debe decarar el la temperatura inicial')
            sys.exit(2)

        # verificar tiempo final
        try:
            tiempo_final = int(self.tiempoFinal.get())
            if tiempo_final <= 0:
                messagebox.showerror(
                    'Error', 'El tiempo no Puede ser Negativo')
                sys.exit(2)
        except ValueError:
            messagebox.showerror(
                'Error', 'Se debe decarar el tiempo inicial')
            sys.exit(2)
        # verificar temperatura final
        try:
            tempearatura_final = float(self.temperaturaFinal.get())
            if tempearatura_final <= 0:
                messagebox.showerror(
                    'Error', 'La temperatura final no Puede ser Negativo')
                sys.exit(2)
        except ValueError:
            messagebox.showerror(
                'Error', 'Se debe decarar la temperatura final')
            sys.exit(2)
        ############
        # se genera el parametro

        fig = Figure(figsize=(5, 5), dpi=100)
        # manda a llamar a rhk
        vx, vy = self.rk4(self.f, tiempo_inicial, temperatura_inicial, 50, 100)
        # se crea una sub-figura
        plot1 = fig.add_subplot(111)
        # se grafica
        plot1.plot(vx, vy)
        # se aniade a tinker como elementos de canvas
        self.root.geometry("450x500")
        canvas = FigureCanvasTkAgg(fig, self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()


def main():
    root = Tk()
    Graficar(root)
    root.mainloop()


if __name__ == '__main__':
    main()

#!/usr/bin/python
#
#  Ejercicio de declaración de variables a través del teclado
#
#
import sys
import csv
import time
import numpy as np
import random
import matplotlib.pyplot as plt


class Aleatorios(object):
    def __init__(self, cantidad, **kwargs):
        self.media = 0
        self.desviacion = 1
        self.opcion = 2
        for key, value in kwargs.items():
            if float(value) <= 0:
                print('El valor de {} no puede ser negativo'.format(key))
                sys.exit(2)
            else:
                setattr(self, key, float(value))
        self.cantidad = cantidad
        if float(self.opcion) >= 5:
            print('El valor de {} no es válido para ninguna opción.'.format(key))
            sys.exit(2)


class Opciones(Aleatorios):
    """Clase para correr los métodos de generación de valores
    aleatorios de una distribución normal."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def metodos(self):
        if self.opcion == 1:
            inicio = time.perf_counter_ns()
            solucion1 = []
            for i in range(self.cantidad):
                suma = 0
                for j in range(12):
                    suma += random.random()
                x = self.media+self.desviacion*(suma-6)
                solucion1.append(round(x, 2))
            fin = time.perf_counter_ns()
            tiempo1 = fin - inicio
            return solucion1, tiempo1, self.opcion

        elif self.opcion == 2:
            inicio = time.perf_counter_ns()
            solucion2 = []
            for i in range(self.cantidad):
                x = round(random.gauss(self.media, self.desviacion), 2)
                solucion2.append(x)
            fin = time.perf_counter_ns()
            tiempo2 = fin - inicio
            return solucion2, tiempo2, self.opcion

        elif self.opcion == 3:
            inicio = time.perf_counter_ns()
            solucion3 = []
            for i in range(self.cantidad):
                valor = np.random.rand()
                if valor <= 0.006:
                    x = 20.78
                elif valor >= 0.007 and valor <= 0.067:
                    x = 23.71
                elif valor >= 0.068 and valor <= 0.309:
                    x = 26.64
                elif valor >= 0.31 and valor <= 0.692:
                    x = 29.57
                elif valor >= 0.693 and valor <= 0.934:
                    x = 32.5
                elif valor >= 0.935 and valor <= 0.995:
                    x = 35.43
                else:
                    x = 38.36
                solucion3.append(x)
            fin = time.perf_counter_ns()
            tiempo3 = fin - inicio
            return solucion3, tiempo3, self.opcion

        elif self.opcion == 4:
            inicio = time.perf_counter_ns()
            solucion1 = []
            for i in range(self.cantidad):
                suma = 0
                for j in range(12):
                    suma += random.random()
                x = self.media+self.desviacion*(suma-6)
                solucion1.append(round(x, 2))
            fin = time.perf_counter_ns()
            tiempo1 = fin - inicio
            inicio = time.perf_counter_ns()
            solucion2 = []
            for i in range(self.cantidad):
                x = round(random.gauss(self.media, self.desviacion), 2)
                solucion2.append(x)
            fin = time.perf_counter_ns()
            tiempo2 = fin - inicio
            inicio = time.perf_counter_ns()
            solucion3 = []
            for i in range(self.cantidad):
                valor = round(random.random(), 2)
                if valor <= 0.006:
                    x = 20.78
                elif valor >= 0.007 and valor <= 0.067:
                    x = 23.71
                elif valor >= 0.068 and valor <= 0.309:
                    x = 26.64
                elif valor >= 0.31 and valor <= 0.692:
                    x = 29.57
                elif valor >= 0.693 and valor <= 0.934:
                    x = 32.5
                elif valor >= 0.935 and valor <= 0.995:
                    x = 35.43
                else:
                    x = 38.36
                solucion3.append(x)
            fin = time.perf_counter_ns()
            tiempo3 = fin - inicio
            return solucion1, tiempo1, solucion2, tiempo2, solucion3, tiempo3, self.opcion


def main(**kwargs):
    cantidad = 30
    x = Opciones(cantidad, **kwargs)
    if x.opcion < 4:
        valores, tiempo, opcion = x.metodos()
        print("El tiempo en realizar el método {} fue: {}.".format(
            int(opcion), tiempo))
        data = []  # Arreglo donde estará la información que se manda a archivo
        header = ["No.", "Valores"]
        for i in range(cantidad):
            data.append([i+1, valores[i]])
        with open('salida6.csv', 'w', encoding='UTF-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
        print('El archivo ha sido generado con ese método.')
        datos = valores
        fig = plt.figure(figsize=(10, 7))
        # Creating plot
        plt.boxplot(datos)
        # show plot
        plt.show()

    if x.opcion == 4:
        valores1, tiempo1, valores2, tiempo2, valores3, tiempo3, opcion = x.metodos()
        print("El tiempo en realizar el método 1 fue: {}.\nEl tiempo en realizar el método 2 fue: {}.\nEl tiempo en realizar el método 3 fue: {}.".format(
            tiempo1, tiempo2, tiempo3))
        data = []  # Arreglo donde estará la información que se manda a archivo
        header = ["No.", "Metodo 1", "Metodo 2", "Metodo 3"]
        for i in range(cantidad):
            data.append([i+1, valores1[i], valores2[i], valores3[i]])
        print('El archivo ha sido generado con todos los métodos.')

        datos = valores1, valores2, valores3
        fig = plt.figure(figsize=(10, 7))
        # Creating plot
        plt.boxplot(datos)
        # show plot
        plt.show()

    """ dato = valores[1]
    data = [dato]

    fig = plt.figure(figsize=(10, 7))

    # Creating axes instance
    ax = fig.add_axes([0, 0, 1, 1])

    # Creating plot
    bp = ax.boxplot(data)

    # show plot

    plt.show() """


if __name__ == '__main__':
    main(**dict(arg.split('=') for arg in sys.argv[1:]))

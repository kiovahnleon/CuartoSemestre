import numpy as np
import matplotlib.pyplot as plt


def trapecio(n, x, fx, t):
    sum = 0
    for i in range(1, n):
        sum = sum+fx[i]
    I = (x[n]-x[0])*(fx[0]+2*sum+fx[n])/(2*t)
    return I


num = int(input("Numero de datos para analizar  "))
h = float(input("Ancho de los trapecios "))
n = num
x = np.zeros([n])
fx = np.zeros([n])
print("Introduce los datos")
for i in range(0, n):
    x[i] = input("x["+str(i)+"]= ")
    fx[i] = input("fx["+str(i)+"]= ")

n = num-1
t = (x[n]-x[0])/h
print("El valor de la integral: ", round(trapecio(n, x, fx, t), 6))

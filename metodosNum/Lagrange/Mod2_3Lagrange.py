# Interpolacion de Lagrange
# divisoresL solo para mostrar valores
import math
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# INGRESO , Datos de prueba
xi = np.array([0.25, 0.5, 0.75])
fi = np.array([0.8109, 0.6931, 0.5596])

# PROCEDIMIENTO
# Polinomio de Lagrange
n = len(xi)
x = sym.Symbol('x')
polinomio = 0
divisorL = np.zeros(n, dtype=float)
for i in range(0, n, 1):

    # Termino de Lagrange
    numerador = 1
    denominador = 1
    for j in range(0, n, 1):
        if (j != i):
            numerador = numerador*(x-xi[j])
            denominador = denominador*(xi[i]-xi[j])
    terminoLi = numerador/denominador

    polinomio = polinomio + terminoLi*fi[i]
    divisorL[i] = denominador

# simplifica el polinomio
polisimple = polinomio.expand()

# para evaluación numérica
px = sym.lambdify(x, polisimple)

# Puntos para la gráfica
muestras = 101
a = np.min(xi)
b = np.max(xi)
pxi = np.linspace(a, b, muestras)
pfi = px(pxi)

# Error
error = (x-xi[0])*(x-xi[2])*(-0.26)/(math.factorial(3))

# Resultado de error
xv = 0.6
errorb = np.round((xv-xi[0])*(xv-xi[1])*(xv-xi[2])
                  * (-0.26)/(math.factorial(3)), 5)

# SALIDA
print('    valores de fi: ', fi)
print('divisores en L(i): ', divisorL)
print()
print('Expresiones de Polinomio de Lagrange')
print(polinomio)
print()
print('Polinomio de Lagrange: ')
print(polisimple)
print()
print('Formula error')
print(error)
print()
print('Error')
print(errorb)

# Gráfica
plt.plot(xi, fi, 'o', label='Puntos')
plt.plot(pxi, pfi, label='Polinomio')
plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.title('Interpolación Lagrange')
plt.show()

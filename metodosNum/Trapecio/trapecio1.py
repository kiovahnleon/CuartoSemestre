# Metodo de Trapecios

import numpy as np
import matplotlib.pyplot as plt

# Declaracion de Funcion


def fx(x): return 3*(x**3) + 5*x - 1


# intervalo
a = 0
b = 1
tramos = 4

# PROCEDIMIENTO
# Regla del Trapecio
# Usando tramos equidistantes en intervalo
h = (b-a)/tramos  # formula para obtener la h
xi = a
suma = fx(xi)
for i in range(0, tramos-1, 1):
    xi = xi + h
    suma = suma + 2*fx(xi)
suma = suma + fx(b)
area = h*(suma/2)

# Ouptut
print('Tramos: ', tramos)
print('Integral(Area Bajo la Curva): ', area)

# GRAFICA
# Puntos de muestra
muestras = tramos + 1
xi = np.linspace(a, b, muestras)
fi = fx(xi)
# Linea suave
muestraslinea = tramos*10 + 1
xk = np.linspace(a, b, muestraslinea)
fk = fx(xk)

# Graficando
plt.plot(xk, fk, label='f(x)')
plt.plot(xi, fi, marker='o',
         color='#ebdb34', label='muestras')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método del trapecio')
plt.legend()

# Trapecios
plt.fill_between(xi, 0, fi, color='#00948d')
for i in range(0, muestras, 1):
    plt.axvline(xi[i], color='w')

plt.show()

# Integración: Regla Simpson 1/3
# Validar cantidad de tramos pares
import numpy as np
import matplotlib.pyplot as plt

# INGRESO


def fx(x): return 3*x**3 + 5*x - 1


# intervalo de integración
a = 0
b = 1
tramos = 3

# Validar cantidad de tramos pares
esimpar = tramos % 2
while (esimpar == 1):
    tramos = int(input('tramos es par: '))
    esimpar = tramos % 2

# PROCEDIMIENTO
# Regla de Simpson 1/3, varios tramos
h = (b-a)/tramos
xi = a
# segmento por cada dos tramos
suma = fx(xi)
for i in range(0, tramos-2, 2):
    xi = xi + h
    suma = suma + 4*fx(xi)
    xi = xi + h
    suma = suma + 2*fx(xi)
# último segmento
xi = xi + h
suma = suma + 4*fx(xi)
suma = suma + fx(b)
area = (h/3)*suma

# SALIDA
print('tramos: ', tramos)
print('Integral: ', area)

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

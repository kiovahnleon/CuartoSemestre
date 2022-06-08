# PROGRAMA PRUEBA
# Ref Rodriguez 9.1.1 p335 ejemplo.
# prueba y'-y-x+(x**2)-1 =0, y(0)=1

# INGRESO
# d1y = y' = f, d2y = y'' = f'
import numpy as np
import matplotlib.pyplot as plt
def d1y(x, y): return -y/(x+y**2)


# EDO. Método de RungeKutta 2do Orden
# estima la solucion para muestras espaciadas h en eje x
# valores iniciales x0,y0
# entrega arreglo [[x,y]]

def rungekutta2(d1y, x0, y0, h, muestras):
    tamano = muestras + 1
    estimado = np.zeros(shape=(tamano, 2), dtype=float)
    # incluye el punto [x0,y0]
    estimado[0] = [x0, y0]
    xi = x0
    yi = y0
    for i in range(1, tamano, 1):
        K1 = h * d1y(xi, yi)
        K2 = h * d1y(xi+h, yi + K1)

        yi = yi + (K1+K2)/2
        xi = xi + h

        estimado[i] = [xi, yi]
    return(estimado)


x0 = 0
y0 = 1
h = 0.5
muestras = 3

# PROCEDIMIENTO
puntosRK2 = rungekutta2(d1y, x0, y0, h, muestras)
xi = puntosRK2[:, 0]
yiRK2 = puntosRK2[:, 1]

# SALIDA
print('estimado[xi,yi]')
print(puntosRK2)

# ERROR vs solución conocida


def y_sol(x): return ((np.e)**x) + x + x**2


yi_psol = y_sol(xi)
errores = yi_psol - yiRK2
errormax = np.max(np.abs(errores))

# SALIDA
print('Error máximo estimado: ', errormax)
print('entre puntos: ')
print(errores)

# GRAFICA [a,b+2*h]
a = x0
b = h*muestras+2*h
muestreo = 10*muestras+2
xis = np.linspace(a, b, muestreo)
yis = y_sol(xis)

# Gráfica

plt.plot(xis, yis, label='y conocida')
plt.plot(xi[0], yiRK2[0],
         'o', color='r', label='[x0,y0]')
plt.plot(xi[1:], yiRK2[1:],
         'o', color='m',
         label='y Runge-Kutta 2 Orden')

plt.title('EDO: Solución con Runge-Kutta 2do Orden')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()

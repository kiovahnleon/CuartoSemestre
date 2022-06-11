# Kiovahn Leon
# 4SA
# Ecuaciones Diferenciales

import math
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('bmh')

start = -5
end = 5
step = 0.1
xpoints = np.array([])
ypoints = np.array([])


print('\n¿Cuál función quieres graficar?\n')
opFunct = int(input("1. x\n2. x^2\nOpcion: "))

if opFunct == 1:
    ysumpoints = np.zeros((int((end-start)/step)+1))
else:
    ysumpoints = np.empty((int((end-start)/step)+1))
    ysumpoints.fill(25/3)

nstr = input("Ingresa n: ")
n = int(nstr)


def f(x, n):
    return (((-1)**(n+1))/(n*math.pi))*10*math.sin((n*math.pi*x)/5)


def f2(x, n):
    return (((-1)**n)*100)/((n**2)*(math.pi**2))*math.cos((n*math.pi*x)/5)


ysum = 0
for i in range(1, n+1):
    xi = start
    j = 0
    while xi <= end:
        ypoints = np.append(ypoints, f(xi, i) if opFunct == 1 else f2(xi, i))
        xpoints = np.append(xpoints, xi)
        ysumpoints[j] = ysumpoints[j]+ypoints[len(ypoints)-1]
        xi += step
        j += 1
    if i < n:
        xpoints = np.array([])
        ypoints = np.array([])


plt.plot(xpoints, ysumpoints, color='indigo')
plt.show()

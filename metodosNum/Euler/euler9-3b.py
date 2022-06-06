import math

y = 0
z = 1
h = 0.01
a = 0
b = 5
real = -0.9589


def zprima(z, y, t):
    return math.sin(t)+0.01*math.pow(z, 2)-2*y


def euler(y, z, h, a, b):
    yprima = zres = 0
    t = a
    while t <= b:
        yprima = z
        zres = zprima(z, y, t)
        y = y + h*yprima
        z = z + h*zres
        t += h
    return y


resultado = euler(y, z, h, a, b)
print()
print("Resultado: ", resultado)
print()

error = ((real-resultado)/real)*100

print("Error: ", error, "%")
print()

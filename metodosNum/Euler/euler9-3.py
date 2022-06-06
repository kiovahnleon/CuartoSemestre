
y = 1
z = 0
h = 0.01
a = 0
b = 5
real = -0.500


def zprima(y):
    return -8*y


def euler(y, z, h, a, b):
    yprima = zres = 0
    t = a
    while t <= b:
        yprima = z
        zres = zprima(y)
        y = y + h*yprima
        z = z + h*zres
        t += h
    return y


resultado = euler(y, z, h, a, b)
print()
print('Resultado:', resultado)
print()

error = abs(((real-resultado)/real)*100)

print('Error:', error, '%')
print()

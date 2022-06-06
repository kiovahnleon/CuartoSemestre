
y = 1
z = 0
h = 0.5
parametro = 1


def zprima(z, y):
    return 0.05*z-0.15*y


def euler(y, z, h, parametro):
    yprima = zres = 0
    t = h
    while t <= parametro:
        yprima = z
        zres = zprima(z, y)
        y = y + h*yprima
        z = z + h*zres
        t += h
    return y


print()
print("y(1) = ", euler(y, z, h, parametro))

parametro = 2

print("y(2) = ", euler(y, z, h, parametro))
print()

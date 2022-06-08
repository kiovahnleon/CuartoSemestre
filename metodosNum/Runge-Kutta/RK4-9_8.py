def yprima(x, y):
    return (x*y+1)


def RK4(x0, y0, x, h):

    n = (int)((x - x0)/h)

    y = y0
    for i in range(1, n + 1):
        k1 = h * yprima(x0, y)
        k2 = h * yprima(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * yprima(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * yprima(x0 + h, y + k3)

        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)

        x0 = x0 + h
    return y


x0 = 0
y = 0
x = 1
h = 0.05
print('\ny(x) = ', RK4(x0, y, x, h), '\n')

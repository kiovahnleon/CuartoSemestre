import math


def f(x, y):
    return math.e**-x - 3*y


def euler(x0, y0, xn, n):

    h = (xn-x0)/n

    for i in range(n):
        slope = f(x0, y0)
        yn = y0 + h * slope
        print('%.4f\t%.4f\t%0.4f\t%.4f' % (x0, y0, slope, yn))
        print('------------------------------')
        y0 = yn
        x0 = x0+h

    print('\nAt x=%.4f, y=%.4f' % (xn, yn))


print('Condiciones Iniciales:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

print('Punto de calculo: ')
xn = float(input('xn = '))

print('no. de pasos:')
step = int(input('pasos = '))

euler(x0, y0, xn, step)

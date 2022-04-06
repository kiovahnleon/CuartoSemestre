# Gauss Seidel Iteration

# Defining equations to be solved
# in diagonally dominant form
f1 = lambda x,y,z: (27-2*y+z)/10
f2 = lambda x,y,z: (-61.5 + 3*x - 2*z)/-6
f3 = lambda x,y,z: (-21.5 - x - y)/5

# Initial setup
x0 = 0
y0 = 0
z0 = 0
count = 1

# Reading tolerable error
e = float(input('Ingresa Error Tolerable: '))

# Implementation of Gauss Seidel Iteration
print('\nIteracion\tx\ty\tz\n')

condition = True

while condition:
    x1 = f1(x0,y0,z0)
    y1 = f2(x1,y0,z0)
    z1 = f3(x1,y1,z0)
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' %(count, x1,y1,z1))
    e1 = abs((x1-x0)/x1)
    e2 = abs((y1-y0)/y1)
    e3 = abs((z1-z0)/z1)
    
    count += 1
    x0 = x1
    y0 = y1
    z0 = z1
    
    condition = e1>e or e2>e or e3>e

print('\nSolucion: x=%0.4f, y=%0.4f, z = %0.4f\n'% (x1,y1,z1))
print('\nErrores: e1:%0.4f, e2:%0.4f, e3:%0.4f\n'%(e1,e2,e3))
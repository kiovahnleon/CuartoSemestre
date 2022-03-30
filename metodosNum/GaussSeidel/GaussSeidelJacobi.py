# Gauss Seidel Iteration

# Defining equations to be solved
# in diagonally dominant form
f1 = lambda x,y,z: (7.85+0.1*y+0.2*z)/3
f2 = lambda x,y,z: (-19.3 -0.1*x +0.3*z)/7
f3 = lambda x,y,z: (71.4-0.3*x+0.2*y)/10

# Initial setup
x0 = 0
y0 = 0
z0 = 0
count = 1

# Reading tolerable error
e = float(input('Ingresa Error Tolerable: '))

# Implementation of Gauss Seidel Iteration
print('\nCount\tx\ty\tz\n')

condition = True

while condition:
    x1 = f1(x0,y0,z0)
    y1 = f2(x0,y0,z0)
    z1 = f3(x0,y0,z0)
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' %(count, x1,y1,z1))
    e1 = abs(x0-x1);
    e2 = abs(y0-y1);
    e3 = abs(z0-z1);
    
    count += 1
    x0 = x1
    y0 = y1
    z0 = z1
    
    condition = e1>e and e2>e and e3>e

print('\nSolucion: x=%0.3f, y=%0.3f and z = %0.3f\n'% (x1,y1,z1))
x = 0.0
y = 1.0
u = 5.0

h = 0.01

print('\n' * 2)
print('x', '\t', 'y')
print(x, '\t', y)

while(x <= 5):
    yn = y
    y = y+(h*u)
    u = u+(h*(-8*yn))
    x = x+h
    print(x, '\t', y)

#!/usr/bin/python
#
#Primer ejemplo de Python con aleatorios (metodo congruencial)
#
#Kiovahn Leon
#Feb/11/22
#al20760618.at.dot.edu.dot.mx
#
t=1168
bandera=-1
a=8*t+bandera*3
semilla=333519
m=19191916
#se declara el arreglo
x=[]
#se inicia el arreglo
x.append(semilla)
#comienza el ciclo
for i in range(1,6):
    f=(a*x[i-1]+bandera)%m
    x.append(f/m)
for r in x:
    print('{}'.format(r))

#!/usr/bin/python
#
#Primer ejemplo de Python con aleatorios (metodo congruencial)
#
#Kiovahn Leon
#Feb/11/22
#al20760618.at.dot.edu.dot.mx
#
t=4219
bandera=1
a=8*t+bandera*3
semilla=23456
m=575629
#se declara el arreglo
x=[]
#se inicia el arreglo
x.append(semilla)
#comienza el ciclo
for i in range(1,11):
    f=(a*x[i-1])%m
    x.append(f/m)
for r in x:
    print('{:0.5f}'.format(r))


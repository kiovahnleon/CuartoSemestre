#!/usr/bin/python
#
#Primer ejemplo de Python con aleatorios (metodo congruencial)
#
#Kiovahn Leon
#Feb/11/22
#al20760618.at.dot.edu.dot.mx
#
a=421
b=789
semilla=23456
m=575629
#Se declara el arreglo
x=[]
x.append(semilla)
# se crea el ciclo
for i in range(1,11):
	l=(a*x[i-1]+b)%m
	x.append(l/m)
for j in range (len(x)):
	x[j]=x[j]/m
for l in x:
	print('{:0.5f}'.format(l))

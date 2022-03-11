#/usr/bin/python
#-"- coding: utf-8 -"-
# Se declara las funcione auxiliares para los ejercicios
#
# Kiovahn Leon
#Feb 24/22
#al20760618.at.ite.dot.edu.dot.mx
#
from datetime import datetime

#Metodo que genera los numeros pseudo aleatorios
def generar(cantidad):
    t=4219 #Valor por omision en caso de no ser declarado
    bandera=1 #Valor por omisiion en caso de no ser declarado
    m=2**31-1 #valor por omision en caso de no ser declarado
    a=8*t+bandera*3
    ahora=datetime.now()
    semilla=ahora.microsecond
    #Se delcara el arreglo inicial 
    x=[]
    #Se declara el arreglo donde estaran los aleatorios
    y=[]
    #Se inicia el arreglo
    x.append(semilla)
    #comienza el ciclo
    for i in range(cantidad+1):
        f=(a*x[i])%m
        if i > 0: #Se elimnima la semilla del arrelgo x para asi obtener los aleatorios
            y.append(f/m)
    return y

#funcion que devolvera el dato de la tarjeta de debito
def datos_tarjeta(semilla):
    t=1233
    bandera=-1
    a=8*t+bandera*3
    m=2**16
    x=[]
    x.append(semilla)
    for i in range(1,10):
        n=(a*x[i-1]%m)
        x.append(n)
    for j in range(len(x)):
        #convertir a texto
        dato=str(x[j])
        #se extraen los cuatro caracteres
        x[j]=dato[:4]
    return(x)
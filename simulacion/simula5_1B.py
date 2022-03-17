#!/usr/bin/python
#-*-coding: utf-8 -*-
# Ejercicio con Python con aleatorios, donde el ingreso de
# valores es a traves de consola
#
#Kiovahn Leon
# Feb/15/22
# al20760618.at.ite.dot.edu.dot.mx
#
from datetime import datetime
import sys,getopt,argparse

class aleatorios:
    def __init__(self,datos):
        self.datos = datos
        self.t=1168  #Valor por omisión en caso de no ser declarado
        self.bandera=-1  # Valor por omisión en caso de no ser declarado
        self.m=19191916
        #2**31-1
        # Valor por omisión en caso de no ser declarado
        self.cantidad=5  #Cantidad de núm. aleatorios a generar por omisión
        try:
            opts,args=getopt.getopt(self.datos,"hn:",["help","cuantos="])
        except getopt.error:
            print('Modo de ejecutar el código: ')
            print('Simulacion5.py -h [-n cuantos]')
            print('     ')
            print('Escriba Simulacion51.py --help para más información')
            sys.exit(2)
        for opt,arg in opts:
            if opt in ("-h","--help"):
                parser=argparse.ArgumentParser(description='''
                    El programa realiza una simulación de números pseudoaleatorios
                    basandose en el método congruencial los valores t así como del módulo ya se encuentran
                    indicados dentro del código.
                    Sin embargo, se requiere que el usuario determine la cantidad de valores por generar,
                    misma que se declara en la variable <n>; así entonces, esta cantidad deberá
                    ser un entero no negativo.''',epilog='''
                    En caso de no declarar ningún valor para <n>, se tomará como valor por defaulf
                    de construir 15 números pseudoaleatorios''' 
                    )
                parser.add_argument('-n','--cuantos',help='Número de pseudoaleatorios a ser generados',type=int,required=False)
                args=parser.parse_args()
            elif opt in ("-n","--cuantos"):
                try:
                    temporal_cantidad=int(arg)
                    if temporal_cantidad <= 0:
                        print('No es posible generar la cantidad solicitada')
                        sys.exit(2)
                    self.cantidad=temporal_cantidad
                except:
                    print('No es posible generar la cantidad solicitada')
                    sys.exit(2)
                # Método que genera los números pseudoaleatorios
        aleatorios.simula(self)
    def simula(self):
        a=8*self.t+self.bandera*3
        ahora=datetime.now()
        #semilla=ahora.microsecond
        semilla=333519
        # Se declara un arreglo
        x=[]
        # Se inicia el arreglo
        x.append(semilla)
        # Comienza el ciclo
        for i in range(1,self.cantidad+1):
            f=(a*x[i-1])%self.m
            x.append(f)
        y=x[1:]
        for j in range(len(y)):
            y[j]=y[j]/self.m
        self.solucion=y

def main():
    x = aleatorios(sys.argv[1:])
    for r in x.solucion:
        print('{:0.5f}'.format(r))

if __name__ == '__main__':
    main()
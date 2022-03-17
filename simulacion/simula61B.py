#!/usr/bin/python3
#-*-coding: utf-8 -*-
#
# Ejercicio de Python con aleatorios, donde el ingreso de
# valores es a traves de consola para generar valores en un
# intervalo (a,b)
#
# Kiovahn Leon
# Feb/18/22
# al20760618.at.ite.dot.edu.dot.mx
#
from datetime import datetime
import sys,getopt,argparse
class aleatorios:
    def __init__(self,datos):
        self.datos=datos
        self.t=1168 #Valor por omisión en caso de no ser declarado
        self.bandera=1 #Valor por omisión en caso de no ser declarado
        self.m=19191916 #Valor por omisión en caso de no ser declarado
        self.cantidad=5 #Cantidad de aleatorios a generar por omisión
        self.decimales=5 #Numero de decimales por redondear, valor por omisión
        try:
            opts,args=getopt.getopt(self.datos,"hv:V:n:d:",["help","vminima=","vmaxima=","cuantos=","decimales="])
        except getopt.error:
            print('Modo de ejecutar el código: ')
            print('simula6.py -v <valor_minimo> -V <valor_maximo> [-n cuantos] [-d decimales] ')
            print(' ')
            print('escriba simula6.py --help para mayor información ')
            sys.exit(2)
        for opt,arg in opts:
            if opt in ("-h","--help"):
                parser=argparse.ArgumentParser(description='''
                    El programa realiza una simulación de números pseudoaleatorios
                    basándose en el método congruencial; los valores t así como del
                    módulo ya se encuentran indicados dentro del código.
                    El objetivo, es generar valores enteros comprendidos en el intervalo
                    (v,V) donde <v> representa al valor mínimo y <V> al valor máximo.
                    De manera adicional, el usuario podrá determinar la cantidad
                    de valores por generar, misma que se declara en la variable <n>;
                    así entonces, esta cantidad deberá ser un entero no negativo.
                    ''',epilog='''
                    En caso de no declarar ningún valor para <n>, se tomará como valor
                    por default de construir 15 números pseudoaleatorios; así mismo, la variable
                    <d> representa el número de cifras decimales por redondear, de no señalarse,
                    se tomarán dos cifras decimales.
                    '''
                    )
                parser.add_argument('-v','--vminima',help='Inicio del intervalo',type=float,required=True)
                parser.add_argument('-V','--vmaxima',help='Fin del intervalo',type=float,required=True)
                parser.add_argument('-n','--cuantos',help='Número de pseudoaleatorios a ser generados',type=int,required=False)
                parser.add_argument('-d','--decimales',help='Número de cifras decimales por redondear',type=int,required=False)
                args=parser.parse_args()
            elif opt in ("-v","--vminima"):
                try:
                    self.vminimo=float(arg)
                except:
                    print('No es posible generar la cantidad solicitada (1)')
                    sys.exit(2)
            elif opt in ("-V","--vmaxima"):
                try:
                    self.vmaximo=float(arg)
                except:
                    print('No es posible generar la cantidad solicitada (2)')
                    sys.exit(2)
            elif opt in ("-n","--cuantos"):
                try:
                    temporal_cantidad=int(arg)
                    if temporal_cantidad<=0:
                        print('No es posible generar la cantidad solicitada (3)')
                        sys.exit(2)
                    self.cantidad=temporal_cantidad
                except:
                    print('No es posible generar la cantidad solicitada (4)')
                    sys.exit(2)
            elif opt in ("-d","--decimales"):
                try:
                    temporal_decimales=int(arg)
                    if temporal_decimales<0:
                        print('No es posible generar la cantidad solicitada (5)')
                        sys.exit(2)
                    self.decimales=temporal_decimales
                except:
                    print('No es posible generar la cantidad solicitada (6)')
                    sys.exit(2)
        aleatorios.simula(self)
#Método que genera los números pseudo aleatorios
    def generar(self):
        a=8*self.t+self.bandera*3
        # ahora=datetime.now()
        semilla=333519
        # Se declara el arreglo inicial
        x=[]
        # Se declara el arreglo donde estarán los aleatorios
        y=[]
        # Se inicia el arreglo
        x.append(semilla)
        # Comienza el ciclo
        for i in range(self.cantidad+1):
            f=(a*x[i])%self.m
            x.append(f)
            if i > 0: #Se elimina la semilla del arreglo X para así obtener los aleatorios
                y.append(f/self.m)
        return y
    #Metodo para construir el intervalo
    def simula(self):
        if self.vmaximo<=self.vminimo:
            print('No es posible realizar la simulación ')
            sys.exit(2)
        numeros_aleatorios=aleatorios.generar(self)
        #Arreglo en donde se almacenarán los valores del intervalo
        valores=[]
        for j in numeros_aleatorios:
            valores.append(round((self.vmaximo-self.vminimo)*j+self.vminimo,self.decimales))
        self.solucion=valores

def main():
    x=aleatorios(sys.argv[1:])
    for r in x.solucion:
        print(r)
if __name__ == '__main__':
    main()
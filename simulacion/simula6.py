#!/usr/bin/python3
# -*-coding: utf-8 -*-
# Ejercicio de Python con aleatorios, donde el ingreso de
# valores es a traves de consola
#
# Kiovahn Leon
# 18/02/2022
# al20760618.at.ite.dot.edu.dot.mx
#

from datetime import datetime
import sys,getopt,argparse


class aleatorios:
    def __init__(self, datos):

        self.datos = datos
        self.t = 4219  # Valor por omisión en caso de no ser declarado
        self.bandera = 1  # Valor por omisión en caso de no ser declarado
        self.m = 2**31-1  # Valor por omisión en caso de no ser declarado
        self.cantidad = 15  # Cantidad de aleatorios a generar por omisión
        try:
            opts, args = getopt.getopt(self.datos, "hv:V:n:", ["help", "vminima=","vmaxima=","cuantos="])
        except getopt.error:
            print('Modo de ejecutar el código: ')
            print('simula6.py -h -v -v <valor_minimo> -V <valor_maximo>[-n cuantos] ')
            print(' ')
            print('escriba simula6.py --help para mayor información ')
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                parser = argparse.ArgumentParser(description='''
                El programa realiza una simulación de números pseudoaleatorios
                basándose en el método congruencial; los valores t así como del
                módulo ya se encuentran indicados dentro del código.
                El objetivo es generar enteros comprendidos en el intervalo (v,V)
                donde <v> representa el valor minimo  y <V> al valor maximo.
                De maner adicional, el usuario podra feterminar la cantidad de 
                valores por generar,misma que se declara en la variable <n>;
                Sin embargo, se requiere que el usuario determine la cantidad
                de valores por generar, misma que se declara en la variable <n>;
                así entonces, esta cantidad deberá ser un entero no negativo. 
                ''', epilog='''
                En caso de no declarar ningún valor para <n>, se tomará como valor
                por default de construir 15 números pseudoaleatorios'''
                                                 )
                                                 
                parser.add_argument(
                    '-v', '--vminima', help='Inicio del intervalo', type=int, required=True)
                parser.add_argument(
                    '-V', '--vmaxima', help='Fin del intervalo', type=int, required=True)
                parser.add_argument(
                    '-n', '--cuantos', help='Número de pseudoaleatorios a ser generados', type=int, required=False)
                args = parser.parse_args()
            elif opt in ("-v", "--vminima"):
                try:
                    vminimo_temporal = int(arg)
                    if vminimo_temporal <= 0:
                        print('No es posible generar la cantidad solicitada (1) vminima')
                        sys.exit(2)
                    self.vminimo = vminimo_temporal
                except:
                    print('No es porsibe generar la cantidad solicitada (2) vminima')
                    sys.exit(2)
            elif opt in ("-V", "--vmaxima"):
                try:
                    vmaximo_temporal = int(arg)
                    if vmaximo_temporal <= 0:
                        print('No es posible generar la cantidad solicitada(3)')
                        sys.exit(2)
                    self.vmaximo =vmaximo_temporal
                except:
                    print('No es porsibe generar la cantidad solicitada(4)')
                    sys.exit(2)
            elif opt in ("-n", "--cuantos"):
                try:
                    temporal_cantidad = int(arg)
                    if temporal_cantidad <= 0:
                        print('No es posible generar la cantidad solicitada (5)')
                        sys.exit(2)
                    self.cantidad = temporal_cantidad
                except:
                    print('No es porsibe generar la cantidad solicitada (6)')
                    sys.exit(2)
        aleatorios.simula(self)
        # Método que genera los números pseudo aleatorios

    def simula(self):
        a = 8*self.t+self.bandera*3
        ahora = datetime.now()
        semilla = ahora.microsecond
        # Se declara el arreglo inicial
        x = []
        # Se inicia el arreglo
        x.append(semilla)
        # Comienza el ciclo
        for i in range(1, self.cantidad+1):
            f = (a*x[i-1]) % self.m
            x.append(f)
            y = x[1:]
        for j in range(len(y)):
            aleatorio = y[j]/self.m
            y[j]=round((self.vmaximo-self.vminimo)*aleatorio+self.vminimo,0)
            self.solucion = y


def main():
    x = aleatorios(sys.argv[1:])#Se crea la instancia de la clase aleatorios, es encvia por parametro los argumentos
    for r in x.solucion:
        print(r)


if __name__ == '__main__':
    main()

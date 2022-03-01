#!/usr/bin/python3
#-*-coding: utf-8 -*-
#Quinto ejercicio de Python con aleatorios, donde el ingreso
# de valores es a traves de consola para generar valores en 
#un intervalo(a,b)
#
# Kiovahn Leon
#Feb/24/22
#al20760618.at.dot.edu.dot.mx
#
from operaciones import generar
import sys, getopt, argparse,csv

class aleatorios:
    def __init__(self,datos):
        self.datos=datos
        self.precio_venta=60 #Precio de venta por default
        self.dias=30 #Numero de dias a simular por omision
        self.decimales=2 #Numoer de deciamales por redondear, valor por omision
        try:
            opts,args=getopt.getopt(self.datos, "hv:V:n:d:",["help","vminima=","vmaxima=","precio=","dias="])
        except getopt.error:
            print('Modo de ejecutar el codigo: ')
            print('simula6.py -v <valor_minimo> -V <valor_maximo> [-n cuantos] [-d decimales]')
            print('    ')
            print('escriba simula6,py --help para mayor información ')
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("-h","--help"):
                parser=argparse.ArgumentParser(description='''
                El objetivo, es generar un archivo en donde se calcula el ingreso de
                acuerdo a las ventas en el intervalo (v,V) donde <v> representa la
                venta minima y <V> la venta maxima.
                El usuario podra deterinar la cantidad de dias por simular, misma que se declara
                en la varibale <d>; asi entonces, esta cantidad debera ser un entero no negativo.
                La varibale <p> representa el precio de venta por unidad.
                ''',epilog='''
                En caso de no declarar ningun valor para <p>, se tomara como valor 
                por default de $60/unidad; a su vez, la variable <d> de no señalarse,
                representa 30 dias.
                '''
                )

                parser.add_argument('-v','--vminima', help='Inicio del intervalo', type=float, required=True)
                parser.add_argument('-V','--vmaxima', help='Fin del intervalo', type=float, required=True)
                parser.add_argument('-p','--cuantos', help='Precio de venta', type=int, required=False)
                parser.add_argument('-d','--dias', help='Numero de dias por simularr', type=int, required=False)
                args=parser.parse_args()
            elif opt in ("-v","--vminima"):
                try:
                    vminimo_temporal=float(arg)
                except:
                    print('No es posible generar la cantidad solicitada (1)')
                    sys.exit(2)
            elif opt in ("-V","--vmaxima"):
                try:
                    vmamixo_temporal=float(arg)
                except:
                    print('No es posible generar la cantidad solicitada (2)')
                    sys.exit(2)
            elif opt in ("-p","--precio"):
                try:
                    temporal_precio=int(arg)
                    if temporal_precio<=0:
                        print('No es posible generar la cantidad solicitada(3)')
                        sys.exit(2)
                    self.precio_venta=temporal_precio
                except:
                    print('No es posible generar la cantidad solicitada(4)')
                    sys.exit(2)
            elif opt in ('-d','--dias'):
                try:
                    temporal_dias=int(arg)
                    if temporal_dias<=0:
                        print('No es posible generar la cantidad solicitada(5)')
                        sys.exit(2)
                    self.dias=temporal_dias
                except:
                    print('No es posible generar la cantidad solicitada')
                    sys.exit(2)
            aleatorios.simula(self)
        #Metodo para construir el intervalo de 
        def simula(self):
            if self.vmaximo<=self.vminimo:
                print('No es posible realizar la simulacion')
                sys.exit(2)
            numeros_aleatorios=generar(self.cantidad)
            #Arreglo en donde se almacenaran los valores del intervalo
            valores=[]
            for j in numeros_aleatorios:
                valores.append(round((self.vmaximo-self.vminimo)*j+self.vminimo,self.decimales))
            self.solucion=valores
    def main():
        x=aleatorios(sys.argv[1:])
        data=[] #Arreglo donde estara la informacion que se manda a archivo
        header=['Dia','Ingreso']
        for i in range(len(x.solucion)):
            data.append([i+1,x.solucion[i]])
        with open('salida.csv','w',encoding='utf-8',newline='')as f:
            writer=csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
        print('El archivo ha sido generado')

    if __name__=='__main__':
        main() 
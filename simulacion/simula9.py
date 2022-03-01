#!/usr/bin/python3
#-*-coding: utf-8 -*-
#
# Ejercicio de Python con aleatorios, para estimar la utilidad promedio
#
# Kiovahn Leon
# Feb/24/22
#al20760618.at.dot.edu.dot.mx
#

from operaciones import generar
import sys,getopt,argparse,csv,math

class aleatorios:
    def __init__(self,datos):
        self.datos=datos
        self.precio_venta=60 #Precio de venta por default
        self.dias=30 #Número de días a simular por omisión
        self.decimales=2 #Numero de decimales por redondear, valor por omisión
        try:
            opts,args=getopt.getopt(self.datos,"hv:V:c:C:p:d:",["help","vminima=","vmaxima=","cminimo=","cmaximo=","precio=","dias="])
        except getopt.error:
            print('Modo de ejecutar el código: ')
            print('simula9.py -v <venta_minima> -V <venta_maxima> -c <costo_minimo> -C <costo_maximo> [-p precio] [-d dias] ')
            print(' ')
            print('escriba simula9.py --help para mayor información ')
            sys.exit(2)
        for opt,arg in opts:
            if opt in ("-h","--help"):
                parser=argparse.ArgumentParser(description='''
                    El objetivo, es generar un archivo en donde se calcula la utilidad
                    de acuerdo a las ventas en el intervalo (v,V) donde <v> representa la
                    venta mínima y <V> la venta máxima, así como (c,C) son los costos mínimo y máximo a gastar/unidad, de acuerdo a una distribución triangular.
                    El usuario podrá determinar la cantidad de días por simular, misma que
                    se declara en la variable <d>; así entonces, esta cantidad deberá ser un
                    entero no negativo.
                    La variable <p> representa el precio de venta por unidad.
                    ''',epilog='''
                    En caso de no declarar ningún valor para <p>, se tomará como valor
                    por default de $60/unidad; a su vez, la variable <d> de no señalarse,
                    representará 30 días.
                    '''
                    )
                parser.add_argument('-v','--vminima',help='Venta mínima',type=float,required=True)
                parser.add_argument('-V','--vmaxima',help='Venta máxima',type=float,required=True)
                parser.add_argument('-c','--cminimo',help='Costo mínimo',type=float,required=True)
                parser.add_argument('-C','--cmaximo',help='Costo maximo',type=float,required=True)
                parser.add_argument('-p','--precio',help='Precio de venta',type=float,required=False)
                parser.add_argument('-d','--dias',help='Número de dias por simular',type=int,required=False)
                args=parser.parse_args()
            elif opt in ("-v","--vminima"):
                try:
                    self.vminima=float(arg)
                except:
                    print('No es posible generar la cantidad solicitada (1)')
                    sys.exit(2)
            elif opt in ("-V","--vmaxima"):
                try:
                    self.vmaxima=float(arg)
                except:
                    print('No es posible generar la cantidad solicitada (2)')
                    sys.exit(2)
            elif opt in ("-c","--cminimo"):
                try:
                    self.cminimo=float(arg)
                except:
                    print('No es posible generar la cantidad solicitada (3)')
                    sys.exit(2)
            elif opt in ("-C","--cmaximo"):
                try:
                    self.cmaximo=float(arg)
                except:
                    print('No es posible generar la cantidad solicitada (4)')
                    sys.exit(2)
            elif opt in ("-p","--precio"):
                try:
                    temporal_precio=float(arg)
                    if temporal_precio<=0:
                        print('No es posible generar la cantidad solicitada (5)')
                        sys.exit(2)
                    self.precio_venta=temporal_precio
                except:
                    print('No es posible generar la cantidad solicitada (6)')
                    sys.exit(2)
            elif opt in ("-d","--dias"):
                try:
                    temporal_dias=int(arg)
                    if temporal_dias<=0:
                        print('No es posible generar la cantidad solicitada (7)')
                        sys.exit(2)
                    self.dias=temporal_dias
                except:
                    print('No es posible generar la cantidad solicitada (8)')
                    sys.exit(2)
        aleatorios.simula(self)

        #Metodo para construir el intervalo
    def simula(self):
        if self.vmaxima<=self.vminima:
            print('No es posible realizar la simulación ')
            sys.exit(2)
        if self.cmaximo<=self.cminimo:
            print('No es posible realizar la simulación (1)')
            sys.exit(2)
        numeros_aleatorios=generar(self.dias)
        #Arreglos en donde se almacenarán los valores del intervalo
        ingreso_diario=[]
        costo_diario=[]
        utilidad_diaria=[]
        costo_medio=0.5*(self.cmaximo+self.cminimo)
        for j in numeros_aleatorios:
            unidades=round((self.vmaxima-self.vminima)*j+self.vminima,0)
            ##Para el cálculo del ingreso
            ingreso_dia=unidades*self.precio_venta
            ##Para el cálculo del costo
            if j <=0.5:
                costo_dia=(self.cminimo+math.sqrt(j*(self.cmaximo-self.cminimo)*(costo_medio-self.cminimo)))*unidades
            else:
                costo_dia=(self.cmaximo-math.sqrt((1-j)*(self.cmaximo-self.cminimo)*(self.cmaximo-costo_medio)))*unidades
            #Calculo de la utilidad
            utilidad_dia=ingreso_dia-costo_dia
            #Almacenar en los arreglos
            ingreso_diario.append(round(ingreso_dia,2))
            costo_diario.append(round(costo_dia,2))
            utilidad_diaria.append(round(utilidad_dia,2))
        self.ingreso=ingreso_diario
        self.costo=costo_diario
        self.utilidad=utilidad_diaria

def main():
    x=aleatorios(sys.argv[1:])
    data=[] #Arreglo donde estará la información que se manda a archivo
    header=['Dia','Ingreso','Costo','Utilidad']
    for i in range(x.dias):
        data.append([i+1,x.ingreso[i],x.costo[i],x.utilidad[i]])
    with open('salida.csv','w',encoding='UTF-8',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
    print('El archivo ha sido generado')

if __name__ == '__main__':
    main()
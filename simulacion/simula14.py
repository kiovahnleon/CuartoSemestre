#!/usr/bin/env python
#-*-coding: utf-8 -*-
#
# Ejemplo para el calculo de pago de una aseguradora
#
# Kiovahn Leon
# Mar/22/22
# al20760547.at.ite.dot.edu.dot.mx
#
import random, csv


def main():
    pagos=[]
    for i in range(300):
        rnd=round(random.random(),2)
        if rnd<=.60:
            pagos.append(0)
        elif rnd<=.80 and rnd>=.61:
            pagos.append(500)
        elif rnd<=.90 and rnd>=.81:
            pagos.append(1000)
        elif rnd<=.95 and rnd>=.91:
            pagos.append(2000)
        else:
            pagos.append(5000)

    data=[] #Arreglo donde estará la información que se manda a archivo
    header=['Pago']
    for i in range(len(pagos)):
        data.append([i+1,pagos[i]])
    with open('salida2.csv','w',encoding='UTF-8',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
    print('El archivo ha sido generado')

if __name__=='__main__':
    main()
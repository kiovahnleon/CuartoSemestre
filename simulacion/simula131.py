#!/usr/bin/env python 
#-*-coding: utf-8 -*-
#
#Ejemplo para el calculo de  la demanda de una revista
#
#Fernanda Flores Monroy
# Mar/17/22
# al20760259.at.ite.dot.edu.dot.mx
#

import random 
from operaciones import intervalo_confianza

def main():
    demandas=[]
    for j in range(12):
        suma_demanda=0
        for i in range(30):
            rnd=round(random.random(),2)
            if rnd<=0.05:
                suma_demanda+=5
            elif rnd<=0.1 and rnd>=0.06:
                suma_demanda+=6
            elif rnd<=0.2 and rnd>=0.11:
                suma_demanda+=7
            elif rnd<=0.35 and rnd>=0.21:
                suma_demanda+=8
            elif rnd<=0.6 and rnd>=0.36:
                suma_demanda+=9
            elif rnd<=0.85 and rnd>=0.61:
                suma_demanda+=10
            else:
                suma_demanda+=11
        promedio_demanda=round(suma_demanda/30,2)
        demandas.append(promedio_demanda)
    demanda_promedio,demanda_minima,demanda_maxima=intervalo_confianza(demandas)
    print('La demanda estara entre: {} y {}'.format(round(demanda_minima,2),round(demanda_maxima,2)))

if __name__ == '__main__':
    main()


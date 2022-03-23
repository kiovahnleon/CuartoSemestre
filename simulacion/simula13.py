#!/usr/bin/python3
#-*-coding: utf-8 -*-
#
# Ejemplo para el calculo de una revista.
#
# Kiovahn Leon
# Mar/17/22
# al20760618.at.ite.dot.edu.dot.mx
#

import random, numpy as np, scipy.stats

def intervalo_confianza(data,confianza=0.95):
    n=len(data)
    m,se=np.mean(data), scipy.stats.sem(data)
    h=se*scipy.stats.t.ppf((1+confianza)/2,2-1)
    return m,m-h,m+h

def main():
    indice_demanda=[]
    for i in range(300):
        rnd=round(random.random(),2)
        if rnd<=0.05:
            indice_demanda.append(5)
        elif rnd<=0.1 and rnd>=0.06:
            indice_demanda.append(6)
        elif rnd <= 0.2 and rnd >= 0.11:
            indice_demanda.append(7)
        elif rnd <= 0.35 and rnd >= 0.21:
            indice_demanda.append(8)
        elif rnd <= 0.6 and rnd >= 0.36:
            indice_demanda.append(9)
        elif rnd <= 0.85 and rnd >= 0.61:
            indice_demanda.append(10)
        elif rnd <= 1 and rnd >= 0.86:
            indice_demanda.append(11)
    demanda_promedio,demanda_minima,demanda_maxima=intervalo_confianza(indice_demanda)
    print('La demanda estara entre {} y {}'.format(demanda_minima,demanda_maxima))

if __name__ == '__main__':
    main()



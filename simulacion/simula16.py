#!/usr/bin/env python
#-*-coding: utf-8 -*-
#
# Ejemplo1 para el calculo
#
# Jared Zaragoza Rosales
# Mar/22/22
# al20760547.at.ite.dot.edu.dot.mx
#

import numpy as np, csv


def main():
    pagando=0
    for i in range(300):
        t = round(np.random.exponential(0.0024),3)
        if t > 0.60:
            pagando+=1
    pagado=round(2125*(pagando/300),2)
    print('Se pagaron {} ocasiones con monto promedio de ${}'.format(pagando,pagado))


if __name__ == '__main__':
    main()

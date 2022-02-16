#!/usr/bin/python
#_*_coding: utf-8 _*_
#Ejercicio de Python con aletorios, donde el ingreso de 
#valores es a traves de consola
#
#Kiovahn Leon
#Feb/15/22
#al20760618.at.dot.edu.dot.mx
#

import sys

class aleatorios:
    def _init_(self, datos):
        self.datos=datos

def main():
    aleatorios(sys.argv[1:])


if __name__ == '_main_':
    main()
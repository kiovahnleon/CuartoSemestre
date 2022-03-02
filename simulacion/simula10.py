#!/usr/bin/python3
#-*-coding: utf-8 -*-
#
# Generador de contraseñas seguras
#
# Kiovahn Leon
# March/1/22
#al20760618.at.dot.edu.dot.mx
#

import sys,random

def realizar_contrasenia(cuantos):
    may=["A","B","C","D","E","F","G"]
    minu=["a","b","c","d","f","g"]
    num=["0","1","2","3","4","5","6","7","8","9"]
    sig=["!","@","#","$","%"]
    contra=''
    for i in range (cuantos):
        opcion=random.randint(1,4)
        if opcion==1:
            valor=may[random.randint(0,len(may)-1)]
            contra=contra+valor
        elif opcion==2:
            valor=minu[random.randint(0,len(minu)-1)]
            contra=contra+valor
        elif opcion==3:
            valor=num[random.randint(0,len(num)-1)]
            contra=contra+valor
        elif opcion==4:
            valor=sig[random.randint(0,len(sig)-1)]
            contra=contra+valor
    return(contra)

def valorar(num_caracteres):
    if num_caracteres<=0:
        print('Intente otro valor')
        sys.exit(2)
    else:
        contrasenia=realizar_contrasenia(num_caracteres)
        print(contrasenia)

def main():
    while True:
        try:
            n=int(input("Numero de caracteres para la contrasenia: "))
            break
        except:
            print("Indica otro valor")
    valorar(n)

if __name__ == '__main__':
    main()
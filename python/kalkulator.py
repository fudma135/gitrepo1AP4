#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kalkulator.py
#  

wynik = 0

def pobierzLiczbe():
    licz1=int(input("podaj liczbe:"))
    return licz1
    
def dodaj(licz1,licz2):
    global wynik
    wynik=licz1+licz2
    return suma
    
def odejmij(licz1,licz2):
    wynik=licz1-licz2
    return różnica
    
def pomnoz(licz1,licz2):
    wynik=licz1*licz2
    
def podziel(licz1,licz2):
    wynik=licz1/licz2

def drukujWynik():

    
def main(args):
    znak=input("podaj znak(+,-,*,/):")
    licz1=pobierzLiczbe()
    licz2=pobierzLiczbe()
    if znak== '+':
        dodaj(licz1,licz2)
    elif znak== '-':
        odejmij(licz1,licz2)
    elif znak== '/':
        podziel(licz1,licz2)
    elif znak=='*':
        pomnoz(licz1,licz2)
    else:
        print('błędny znak działania')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

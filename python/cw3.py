#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  

def main(args):
    start = 0
    stop = int(input("podaj koniec zakresu :"))
    if stop <0:
        print("o kurka")
    for i in range(start,stop+1):
        print(i*i)
   
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

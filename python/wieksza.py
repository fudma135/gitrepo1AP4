#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    # a = 10
    a = int(input ("podaj liczbę: "))
    # b = 5
    b = int(input ("podaj liczbę: "))
    if a > b:
        print("a > b")
    elif b > a:
        print("b > a")
    else:
        print("a = b")
        
        
        print(a + b)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

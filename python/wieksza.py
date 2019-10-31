#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
   # a = 10
   a = input ("podaj liczbę: ")
   # b = 5
   b = input ("podaj liczbę: ")
   if a > b:
       print(a)
       else:
           print(b)
    print("suma:", a + b)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

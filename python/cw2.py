#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


def main(args):
    start = int(input("podaj początek zakresu:"))
    stop = int(input("podaj koniec zakresu:")
    for i in range(start,stop+1):
        print(i)

    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

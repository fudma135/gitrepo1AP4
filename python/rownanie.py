#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# a * x + b = 0

def main(args):
    
    a=int(input("podaj a:"))
    b=int(input("podaj b:"))
    
    if a==0: 
        if b==0:
            print('nieskończenie wiele rozwiązań')
        else:
            print('równanie sprzeczne')
    else:
        x = -b / a
        print (x)
        
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

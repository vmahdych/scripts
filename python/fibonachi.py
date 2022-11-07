#!/usr/bin/env python3

n = int(input("Give me the number: "))
n = n-1

def fibonachi(x):
    if x == 0: 
        return 0
    elif x == 1:
        return 1
    else:
        return fibonachi(x-1) + fibonachi(x-2)
while n >= 0:
    print(fibonachi(n))
    n = n-1

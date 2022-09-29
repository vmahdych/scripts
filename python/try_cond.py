#!/usr/bin/env python3

n = input('Would you be so kind to give me a nomber? ')

try:
    newn = int(n)
except:
    newn = -1

if newn > 0:
    print('I thinks this is the', newn, 'number =)')
else:
    print('It does not look like a number')

#!/usr/bin/env python3

w = int(input('What`s your weight (kg)?: '))
h = float(input('How tall are you (m)?: '))

#try :
#    w = int(w) and h = float(h)
#except :
#    print('Should be numbers')
#    continue

btype = w / (h**2)
print(btype)

if btype < 18.5 :
    print('Underweight')
elif btype < 25 :
    print('Normal')
elif btype < 30 :
    print('Overweight')
else :
    print('Obesity')


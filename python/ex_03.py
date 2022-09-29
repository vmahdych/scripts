#!/usr/bin/env python3

hr=input('Print hours: ')
try:
    fhr=float(hr)
except:
    print('Enter a numeric values')
    quit()

wr=input('Print work rate: ')
try:
    fwr=float(wr)
except:
    print('Enter a numeric values')
    quit()


spr=fhr*fwr #to count simple price

if fhr > 40:

    ohr=fhr%40 #to count how many hours overworked
    opr=fwr*ohr*0.5 #to count price for overworked hours
    pr=spr+opr #result

    print('Price:',pr)

else:
    print('Price:', spr)



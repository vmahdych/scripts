#!/usr/bin/env python3

def computepay(hours, rate) :
#    print('In computepay', hours, rate)
    if hours > 40 :
        spr = hours * rate #to count simple price
        opr = (rate * 0.5) * (hours - 40) #to count price for overworked hours
        pay = spr + opr #result
    else:
        pay = hours * rate
#        print('Returting:', pay)
    return pay

hr = input('Print hours: ')
wr = input('Print work rate: ')
fhr = float(hr)
fwr = float(wr)

xp = computepay(fhr,fwr)

print('Pay: ', xp)



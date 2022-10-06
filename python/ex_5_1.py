#!/usr/bin/env python3

count = 0
sum = 0

while True:
    n = input('Give me a number: ')
    if n == 'done' :
        break
    
    try :
        fn = float(n)
    except :
        print('Invalid input!')
        continue

    count = count + 1
    sum = sum + fn 
    mv = sum / count

#try : 
#    x = int(n)
#except :
#    x is None
print('All done!')
print(count, sum, mv)

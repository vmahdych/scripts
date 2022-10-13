#!/usr/bin/env python3

total = 0
n = 1
while n <= 5 :
    age = input('Give me the passenger age: ')
    try:
        age = int(age)
    except:
        print('give me fucking age!')
        continue

    n = n + 1
    if age > 3 : 
        total = total +100
    else :
        total = total

print('Total:', total)

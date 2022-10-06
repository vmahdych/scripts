#!/usr/bin/env python3

count = 0
sum = 0

print("№ | i | S")
for i in [1, 2, 4, 8, 16, 32, 64]:
    count = count + 1
    sum = sum + i
    print(count,"|",i,"|",sum)


#!/usr/bin/env python3

str = 'X-DSPAM-Confidence: 0.8475 '

h = str.find(' ')

#h2 = str.find(' ',h1)

#print(h1, h2)
number = str[h:]

result = float(number)
print(result)

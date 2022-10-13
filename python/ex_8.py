#!/usr/bin/env python3

inp = input("Would you be so kind to give me a file name? ")

file = open(inp)

for line in file:
    line = line.rstrip()
    wds = line.split()
#    if len(wds) < 1 :
#        continue
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    print(wds[2])

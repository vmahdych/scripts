#!/usr/bin/env python3

new = input('Enter a file name: ')

    file = open(new)

for ln in file:
    line = ln.rstrip()
    print(line.upper())

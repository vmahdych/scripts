#!/usr/bin/env python3

test = input('Give me a file: ')

text = open(test)
counts = dict()

for line in text :
    line = line.rstrip()
    wds = line.split()

    for word in wds :
        counts[word] = counts.get(word, 0) + 1
        
        for key in counts:
            print(key, counts[key])


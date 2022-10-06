#!/usr/bin/env python3

smallest = None 

for the_n in [12, 145, 0, 1, 124, 555]:
    if smallest is None or the_n < smallest :
        smallest = the_n

print(smallest)

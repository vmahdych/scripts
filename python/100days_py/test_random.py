#!/usr/bin/env python3

import random

random_int = random.randint(0, 1)

print(random_int)

if random_int == 0:
    print("Heads")
else:
    print("Tails")

#!/usr/bin/env python3
import random
n = random.randint(1, 2*10**2)
s = ""
for _ in range(n):
    s += str(random.randint(0, 9))
print(s)

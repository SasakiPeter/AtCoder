#!/usr/bin/env python3
import random
n = random.randint(1, 10)
print(n)
for _ in range(n):
    s_len = random.randint(1, 5)
    s = ''
    for _ in range(s_len):
        s += random.choice(['(', ')'])
    print(s)

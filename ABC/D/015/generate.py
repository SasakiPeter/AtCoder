#!/usr/bin/env python3
import random
w = random.randint(1, 10000)
n = random.randint(6, 10)
k = random.randint(1, n)
print(w)
print(n, k)
for _ in range(n):
    a = random.randint(1, 1000)
    b = random.randint(1, 100)
    print(a, b)

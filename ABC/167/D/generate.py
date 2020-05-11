#!/usr/bin/env python3
import random
n = random.randint(2, 100)
A = []
for _ in range(n):
    a = random.randint(1, n)
    A.append(a)
k = random.randint(1, 100)
print(n, k)
print(*A)

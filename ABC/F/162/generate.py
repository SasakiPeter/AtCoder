#!/usr/bin/env python3
import random
n = random.randint(2, 10)
A = []
for _ in range(n):
    a = random.randint(-10**9, 10**9)
    A.append(a)
print(n)
print(*A)

#!/usr/bin/env python3
import random
Q = random.randint(1, 10**5)
print(Q)
for _ in range(Q):
    L = random.randint(1, 10**5)
    R = random.randint(1, 10**5)
    if L > R:
        L, R = R, L
    print(L, R)

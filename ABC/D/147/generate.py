#!/usr/bin/env python3
import random
n = random.randint(2, 3*10**5)
a = [random.randint(0, 2**60-1) for _ in range(n)]
print(n)
print(*a)

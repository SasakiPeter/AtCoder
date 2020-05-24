#!/usr/bin/env python3
import random
r = random.randint(2, 20)
c = random.randint(2, 20)
d = random.randint(1, 2000)
print(r, c, d)
for _ in range(r):
    A = [random.randint(1, 999)for _ in range(c)]
    print(*A)

#!/usr/bin/env python3
import random
N = random.randint(1, 20)
print(N)
s = ""
for _ in range(N):
    s += random.choice(["#", "."])
print(s)

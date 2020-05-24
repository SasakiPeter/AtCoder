#!/usr/bin/env python3
import random
n = random.randint(1, 5)
m = random.randint(1, 5)
print(n, m)
As = ['S', 'G']
for _ in range(n*m-2):
    a = random.randint(1, 9)
    As.append(str(a))
random.shuffle(As)

for i in range(n):
    print(''.join(As[i*m:i*m+m]))

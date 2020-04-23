import itertools
from functools import reduce


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


k = int(input())
ans = 0
for abc in itertools.product([i for i in range(1, k+1)], repeat=3):
    ans += reduce(gcd, abc)

print(ans)

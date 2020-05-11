from functools import reduce


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n, X = map(int, input().split())
A = list(map(lambda x: abs(int(x)-X), input().split()))
print(reduce(gcd, A))

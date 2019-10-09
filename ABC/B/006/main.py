# from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())


def memoize(f):
    # dd = defaultdict()
    dd = {}

    def memoized(*args):
        if args not in dd.keys():
            dd[args] = f(*args) % 10007
        return dd[args]
    return memoized


# @memoize
# def tribo(n):
#     if n < 3:
#         return 0
#     elif n <= 3:
#         return 1
#     return tribo(n-1) + tribo(n-2) + tribo(n-3)

# def tribo(n, a=0, b=0, c=1):
#     if n < 3:
#         return 0
#     elif n <= 3:
#         return c
#     return tribo(n-1, b, c, a+b+c)


# 確かif使わないでかけたはず
def fibo(n):
    a, b = 0, 1
    if n == 1:
        return a
    else:
        # range(0)はからの配列を返す []
        for _ in range(n-2):
            a, b = b, a+b
        return b


# こうする
def fibo(n, a=0, b=1):
    for _ in range(n-1):
        a, b = b, a+b
    return a


# 再帰


# @memoize
# def fibo(n):
#     if n < 2:
#         return 0
#     elif n <= 2:
#         return 1
#     return fibo(n-1) + fibo(n-2)


# def tribo(n):
#     a, b, c = 0, 0, 1
#     if n in (1, 2):
#         return 0
#     for _ in range(n-3):
#         a, b, c = b, c, (a+b+c) % 10007
#     return c


def tribo(n):
    a, b, c = 0, 0, 1
    for _ in range(n-1):
        a, b, c = b, c, (a+b+c) % 10007
    return a


print(tribo(n))

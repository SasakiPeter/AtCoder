from collections import defaultdict
MOD = 10**9+7
n = int(input())
A = list(map(int, input().split()))


# 閉区間での実装 関数化してある方が早い
def sieve(n):
    n += 1
    res = [i for i in range(n)]
    for p in range(2, int(n**.5)+1):
        if res[p] < p:
            continue
        for q in range(p**2, n, p):
            if res[q] == q:
                res[q] = p
    return res


U = 10**6+1
min_factor = sieve(U)


def prime_factor(n):
    res = defaultdict(lambda: 0)
    while 1 < n:
        res[min_factor[n]] += 1
        n //= min_factor[n]
    return res


pf = defaultdict(lambda: 0)

for a in A:
    for p, q in prime_factor(a).items():
        if pf[p] < q:
            pf[p] = q

x = 1
for p, q in pf.items():
    x *= pow(p, q, MOD)
x %= MOD

print(sum(x*pow(a, MOD-2, MOD) for a in A) % MOD)


# # LCM直接求める
# from functools import reduce
# MOD = 10**9+7
# n = int(input())
# A = list(map(int, input().split()))


# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)


# def lcm(a, b):
#     return a*(b//gcd(a, b))


# x = reduce(lcm, A) % MOD
# print(sum(x*pow(a, MOD-2, MOD) for a in A) % MOD)


# # 素因数分解してLCM求める
# from collections import defaultdict
# MOD = 10**9+7
# n = int(input())
# A = list(map(int, input().split()))


# def factorization(n):
#     retval = []
#     tmp = n
#     for i in range(2, int(-(-n**.5//1))+1):
#         if tmp % i == 0:
#             cnt = 0
#             while tmp % i == 0:
#                 cnt += 1
#                 tmp //= i
#             retval.append((i, cnt))
#     if tmp != 1:
#         retval.append((tmp, 1))
#     return retval


# x = defaultdict(int)
# for a in A:
#     for p, q in factorization(a):
#         if x[p] < q:
#             x[p] = q

# mod_x = 1
# for p, q in x.items():
#     mod_x *= pow(p, q, MOD)
# mod_x %= MOD

# B = [mod_x*pow(a, MOD-2, MOD) % MOD for a in A]
# print(sum(B) % MOD)

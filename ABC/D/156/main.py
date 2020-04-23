# n, a, b = map(int, input().split())
# MOD = 10**9+7
# ans = pow(2, n, MOD)-1
# X = Y = 1
# for i in range(1, b+1):
#     Y = Y*i % MOD
#     X = X*(n-i+1) % MOD
#     if i == a or i == b:
#         ans -= X*pow(Y, MOD-2, MOD)

# print(ans % MOD)

n, a, b = map(int, input().split())
MOD = 10**9+7


def COM(n, r):
    X = Y = 1
    if n-r < r:
        r = n-r
    for i in range(1, r+1):
        Y = Y*i % MOD
        X = X*(n-i+1) % MOD
    Y = pow(Y, MOD-2, MOD)
    return X*Y
    # for i in range(1, r+1):
    #     Y = Y*i % MOD
    # Y = pow(Y, MOD-2, MOD)
    # while 0 < r:
    #     X = X*n % MOD
    #     n -= 1
    #     r -= 1


ans = pow(2, n, MOD)-1 - COM(n, a)-COM(n, b)
ans %= MOD

print(ans)


# from collections import defaultdict
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)
# n, a, b = map(int, input().split())
# MOD = 10**9+7
# MAX = 2*10**5
# fac = [0]*MAX
# finv = [0]*MAX
# inv = [0]*MAX


# def COMinit():
#     fac[0] = fac[1] = 1
#     finv[0] = finv[1] = 1
#     inv[1] = 1
#     for i in range(2, MAX):
#         fac[i] = fac[i-1]*i % MOD
#         inv[i] = MOD-inv[MOD % i]*(MOD//i) % MOD
#         finv[i] = finv[i-1]*inv[i] % MOD


# def COM(n, k):
#     if n < k:
#         return 0
#     if n < 0 or k < 0:
#         return 0
#     return fac[n]*(finv[k]*finv[n-k] % MOD) % MOD


# COMinit()

# memo = defaultdict(int)


# def RECOM(n, k):
#     if memo[(n, k)] != 0:
#         return memo[(n, k)]
#     if MAX < n:
#         return n*RECOM(n-1, k-1)//k
#         # return RECOM(n-1, k)+RECOM(n-1, k-1)
#     else:
#         memo[(n, k)] = COM(n, k)
#         return memo[(n, k)]


# # ans = pow(2, n, MOD)-COM(n, a)-COM(n, b)-1
# ans = pow(2, n, MOD)-RECOM(n, a)-RECOM(n, b)-1
# print(ans)
# # print(n, a, b)
# # print(pow(2, n, MOD), COM(n, a), COM(n, b))

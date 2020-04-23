L, R = map(int, input().split())
MOD = 2019
INF = 10**5
ans = INF


if MOD <= R-L:
    print(0)
else:
    x = L % MOD
    y = R % MOD
    if x < y:
        # print(x, y)
        for i in range(x, y):
            for j in range(i+1, y+1):
                ans = min(ans, (i*j) % MOD)
            if ans == 0:
                break
        print(ans)
    else:
        print(0)

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
#     if not retval:
#         retval.append((n, 1))
#     return retval

# print(factorization(MOD))

# # if MOD <= R-L:
# #     print(0)
# if R//MOD - L//MOD == 1:
#     print(0)
# else:
#     x = min(L % MOD, R % MOD)
#     # print(x)
#     print(x*(x+1))
# # L %= MOD
# # R = min(L+1, R % MOD)
# # print(L*R)


# x = L % MOD
# y = R % MOD

# if -(-L//MOD) == (R-1)//MOD:
#     print(0)
# elif x <= 3 and 693 <= y:
#     print(0)
# else:
#     # print(-(-L//MOD),  (R-1)//MOD)
#     # print(L/MOD, R/MOD)
#     # print(divmod(L, MOD), divmod(R, MOD))
#     print(x*(x+1) % MOD)

# print(divmod(L, MOD), divmod(R, MOD))

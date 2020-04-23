#!/usr/bin/env python3

# 考察ちゃんとできれば簡単な問題だったーーーショック！！！
# DPにこだわりすぎたのが敗因
# これが多分LP
n, h = map(int, input().split())
a, b, c, d, e = map(int, input().split())
print(min(a*x+c*max(0, (n*e-h-(b+e)*x)//(d+e)+1) for x in range(n+1)))

# n, h = map(int, input().split())
# a, b, c, d, e = map(int, input().split())
# INF = 10**18
# ans = INF
# for x in range(n+1):
#     y = (n*e-h-(b+e)*x)//(d+e)+1
#     y = max(0, y)
#     # y = (n*e-h-(b+e)*x)/(d+e)
#     # if y < 0:
#     #     y = 0
#     # else:
#     #     y = int(-(-y//1))
#     # yde = n*e-h-(b+e)*x
#     # if yde > 0:
#     #     y = -(-yde//(d+e))
#     # else:
#     #     y = 0
#     # z = n-y-x
#     # print(x, y, z)
#     # if z < 0:
#     #     continue
#     # if h+b*x+d*y-z*e > 0:
#     ans = min(ans, a*x+c*y)
# print(ans)

# for x in range(n+1):
#     for y in range(n+1):
#         z = n-x-y
#         if z < 0:
#             continue
#         if h+b*x+d*y-z*e > 0:
#             ans = min(ans, a*x+c*y)
# print(ans)


# # 部分点40点
# import itertools
# n, h = map(int, input().split())
# a, b, c, d, e = map(int, input().split())
# INF = 10**18
# if n <= 10:
#     ans = INF
#     for schedule in itertools.product(['普通', '質素', '抜き'], repeat=n):
#         cost = 0
#         health = h
#         starved = 0
#         for menu in schedule:
#             if menu == '普通':
#                 cost += a
#                 health += b
#             elif menu == '質素':
#                 cost += c
#                 health += d
#             else:
#                 health -= e
#             if health <= 0:
#                 starved = 1
#                 break
#         if not starved:
#             ans = min(ans, cost)
#     print(ans)
# else:
#     HMAX = h+b*n
#     dp = [[INF]*(HMAX+1) for _ in range(n+1)]
#     dp[0][h] = 0
#     for i in range(1, n+1):
#         for j in range(1, HMAX+1):
#             if j+e <= HMAX:
#                 dp[i][j] = min(dp[i][j], dp[i-1][j+e])
#             if 0 <= j-b:
#                 dp[i][j] = min(dp[i][j], dp[i-1][j-b]+a)
#             if 0 <= j-d:
#                 dp[i][j] = min(dp[i][j], dp[i-1][j-d]+c)
#     # for row in dp:
#     #     print(row)
#     print(min(dp[-1]))

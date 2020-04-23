#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

m = n//2
INF = 10**18
# defaultdictにするかしないかで、10倍以上速度が違う
# pythonでも通る　遷移の種類が少ない時は、dictでDPすると早い
# dp = [[-INF]*(m+1) for _ in range(n+1)]
dp = [defaultdict(lambda: -INF) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(i//2-1, (i+1)//2+1):
        if j == 1:
            dp[i][j] = max(dp[i-1][j], A[i-1])
        elif 0 <= i-2 and 0 <= j <= m:
            dp[i][j] = max(dp[i-1][j], dp[i-2][j-1]+A[i-1])
# for row in dp:
#     print(row)
print(dp[-1][m])


# なぜか、この偶数分岐を行うとバグる
# それは100 0 0 100 みたいな時に、うまくいかないから
# if n % 2 == 0:
#     print(n, A)
#     print(max(sum(A[::2]), sum(A[1::2])))
#     # print(sum(A[::2]), sum(A[1::2]))
# else:
#     m = n//2
#     INF = 10**18
#     dp = [[-INF]*(m+1) for _ in range(n+1)]
#     # dp = [[-INF]*(m+1) for _ in range(2)]
#     for i in range(1, n+1):
#         for j in reversed(range(1, m+1)):
#             if j == 1:
#                 dp[i][j] = max(dp[i-1][j], A[i-1])
#                 # dp[i % 2][j] = max(dp[i % 2-1][j], A[i-1])
#                 continue
#             if 0 <= i-2:
#                 dp[i][j] = max(dp[i-1][j], dp[i-2][j-1]+A[i-1])
#                 # dp[i % 2][j] = max(dp[i % 2-1][j], dp[i % 2][j-1]+A[i-1])
#     for row in dp:
#         print(row)
#     print(dp[-1][m])

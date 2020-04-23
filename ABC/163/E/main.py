n = int(input())
A = list(map(int, input().split()))
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = abs(i-j)*A[i-1]
for row in dp:
    print(row)

# import itertools
# n = int(input())
# A = list(map(int, input().split()))
# dp = [[0]*(n+1) for _ in range(n+1)]
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         dp[i][j] = abs(i-j)*A[i-1]
# # for row in dp:
# #     print(row)

# # n!が通るわけない
# ans = 0
# for x in itertools.permutations(range(1, n+1), n):
#     # print(i)
#     cnt = 0
#     for i, j in enumerate(x):
#         cnt += dp[i+1][j]
#     ans = max(ans, cnt)
# print(ans)

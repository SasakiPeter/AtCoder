# 1次元にすると、すごい早い
n, w = map(int, input().split())
weights, values = zip(*[tuple(map(int, input().split())) for _ in range(n)])
UV = 10**5
INF = 10**10
dp = [INF]*(UV+1)
dp[0] = 0

# 貰うDP
for i in range(1, n+1):
    for j in reversed(range(1, UV+1)):
        if j-values[i-1] < 0:
            continue
        dp[j] = min(dp[j], dp[j-values[i-1]]+weights[i-1])

# DPテーブル全てに値を入れているわけではない
ans = 0
for j in reversed(range(UV+1)):
    if dp[j] <= w:
        ans = j
        break
print(ans)


# n, w = map(int, input().split())
# weights, values = zip(*[tuple(map(int, input().split())) for _ in range(n)])
# UV = 10**5
# # 遅そうなので書き直して
# # INF = float('inf')
# INF = 10**10
# # dp = [[0]+[INF]*UV for _ in range(n+1)]
# dp = [[INF]*(UV+1) for _ in range(n+1)]
# for i in range(n+1):
#     dp[i][0] = 0

# # 貰うDP
# for i in range(1, n+1):
#     for j in range(1, UV+1):
#         dp[i][j] = dp[i-1][j]
#         if 0 <= j-values[i-1]:
#             dp[i][j] = min(dp[i][j], dp[i-1][j-values[i-1]]+weights[i-1])

# # DPテーブル全てに値を入れているわけではない
# ans = 0
# for i in reversed(range(UV+1)):
#     if dp[-1][i] <= w:
#         ans = i
#         break
# print(ans)

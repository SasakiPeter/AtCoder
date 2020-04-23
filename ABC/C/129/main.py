n, m = map(int, input().split())
a = [int(input()) for _ in range(m)]
MOD = 10**9+7
# INF = MOD-1
# dp = [INF]*(n+1)
dp = [-1]*(n+1)
dp[0] = dp[1] = 1

# 0は踏んではいけない階段
# これをforの中で行うとTLEする
for x in a:
    dp[x] = 0

for i in range(2, n+1):
    if dp[i] == 0:
        continue
    dp[i] = (dp[i-1]+dp[i-2]) % MOD

# print(dp)

print(dp[n])
# print(dp[n] if dp[n] != INF else 0)

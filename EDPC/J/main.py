# 期待値DP
from collections import Counter
n = int(input())
c = Counter(map(int, input().split()))
dp = [[[0]*(n+1) for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1-i):
        for k in range(n+1-i-j):
            non_zero = i+j+k
            if non_zero == 0:
                continue
            dp[i][j][k] = n/non_zero
            if 0 <= i-1 and j+1 <= n:
                dp[i][j][k] += dp[i-1][j+1][k]*i/non_zero
            if 0 <= j-1 and k+1 <= n:
                dp[i][j][k] += dp[i][j-1][k+1]*j/non_zero
            if 0 <= k-1:
                dp[i][j][k] += dp[i][j][k-1]*k/non_zero
            # 割り算をまとめても、早くなるのは64msくらい
            # dp[i][j][k] /= non_zero
# for row in dp[0]:
#     print(row)

print(dp[c[3]][c[2]][c[1]])

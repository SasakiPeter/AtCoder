n = int(input())
A = list(map(int, input().split()))
m = -~n//2
dp = [[0]*m for _ in range(m)]
for L in range(m+1):
    for R in range(m+1):
        dp[L][R]

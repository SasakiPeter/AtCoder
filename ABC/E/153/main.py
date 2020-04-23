h, n = map(int, input().split())
A, B = zip(*[tuple(map(int, input().split()))for _ in range(n)])
INF = 10**18
dp = [INF]*(h+1)
dp[0] = 0
for j in range(h):
    for i in range(n):
        if h < j+A[i]:
            dp[-1] = min(dp[-1], dp[j]+B[i])
        else:
            dp[j+A[i]] = min(dp[j+A[i]], dp[j]+B[i])
print(dp[-1])

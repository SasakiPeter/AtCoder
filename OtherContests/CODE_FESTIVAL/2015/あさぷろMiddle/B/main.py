N = int(input())
s = input()

# LCSを組んで、それを拡張すれば良さそう
cnt = 0
for k in range(1, N):
    a = s[:k]
    b = s[k:]
    n = len(a)
    m = len(b)
    dp = [[0]*(m+1) for _ in range(n+1)]

    # もらう
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = max(dp[i][j], dp[i-1][j])

            if a[i-1] == b[j-1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
            else:
                dp[i][j] = max(dp[i][j], dp[i][j-1])

    if cnt < dp[-1][-1]:
        cnt = dp[-1][-1]

    # for row in dp:
    #     print(row)
print(N-2*cnt)

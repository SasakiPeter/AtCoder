n = int(input())
A = list(map(int, input().split()))
dp = [0]*n
dp[1] = abs(A[1]-A[0])
for i in range(2, n):
    dp[i] = min(dp[i-1]+abs(A[i-1]-A[i]), dp[i-2]+abs(A[i-2]-A[i]))
print(dp[-1])

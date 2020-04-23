# dpむずい
n = int(input())
A = list(map(int, input().split()))
INF = 10**5
dp = [[-INF, -INF] for _ in range(n+1)]

dp[0][0] = 0

for i in range(n):
    dp[i+1][0] = max(dp[i][0]+A[i], dp[i][1]-A[i])
    dp[i+1][1] = max(dp[i][0]-A[i], dp[i][1]+A[i])

print(dp)
print(dp[n][0])

# n = int(input())
# A = list(map(int, input().split()))
# cnt = sum(1 for a in A if a < 0)
# # print(cnt)
# ls = list(map(abs, A))
# ans = sum(ls)
# if cnt % 2 == 0:
#     print(ans)
# else:
#     print(ans-2*min(ls))

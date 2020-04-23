# よく考えたら？LISだねー
# O(N**2)はきついのでにぶたんする
import bisect
n = int(input())
A = [int(input())for _ in range(n)]
# print(A)
INF = 10**18
dp = [INF]*n
dp[0] = A[0]
for i in range(1, n):
    j = bisect.bisect_left(dp, A[i])
    dp[j] = min(dp[j], A[i])
print(n-(bisect.bisect_left(dp, INF)))


# n = int(input())
# A = [int(input())for _ in range(n)]
# # print(A)
# dp = [1]*n
# for i in range(1, n):
#     for j in range(i):
#         if A[j] < A[i]:
#             dp[i] = max(dp[i], dp[j]+1)
# print(n-max(dp))

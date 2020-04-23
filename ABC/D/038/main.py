import bisect
import sys
input = sys.stdin.readline
n = int(input())
wh = [tuple(map(int, input().split()))for _ in range(n)]
wh.sort()
w, h = wh[0]
A = [h]
prev = w
for w, h in wh[1:]:
    if prev == w:
        continue
    prev = w
    A.append(h)

INF = 10**18
m = len(A)
dp = [INF]*m
dp[0] = A[0]
for i in range(1, m):
    j = bisect.bisect_left(dp, A[i])
    dp[j] = min(dp[j], A[i])
print(bisect.bisect_left(dp, INF))

# m = len(A)
# dp = [1]*m
# for i in range(1, m):
#     for j in range(i):
#         if A[j] < A[i]:
#             dp[i] = max(dp[i], dp[j]+1)
# print(max(dp))

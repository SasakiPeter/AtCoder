# DPしたい...
n = int(input())
t = [int(input())for _ in range(n)]
TLIM = 200
dp = [0]*(TLIM+1)
dp[0] = 1
for i in range(n):
    for j in reversed(range(TLIM)):
        if dp[j] and j+t[i] < TLIM+1:
            dp[j+t[i]] = 1
# print(dp)
for i in range(-~sum(t)//2, TLIM+1):
    if dp[i]:
        print(i)
        break

# import itertools
# n = int(input())
# t = [int(input())for _ in range(n)]
# sum_t = sum(t)
# half_t = sum_t/2
# ans = sum_t
# for x in itertools.product([0, 1], repeat=n):
#     t1 = 0
#     for i in range(n):
#         if x[i]:
#             t1 += t[i]
#     if abs(t1-half_t) < abs(ans-half_t):
#         ans = t1
# print(max(ans, sum_t-ans))

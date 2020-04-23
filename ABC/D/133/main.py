n = int(input())
A = list(map(int, input().split()))
SUM = sum(A)

# 計算すれば、初期値は求められる
# X1 = S - 2(A2 + A4 + An-1)

init = SUM - 2*sum(A[1::2])
dp = [0]*n
dp[0] = init
for i in range(1, n):
    dp[i] = 2*A[i-1]-dp[i-1]
print(*dp)


# n = int(input())
# A = list(map(int, input().split()))
# SUM = sum(A)

# dp = [0]*n
# dp[0] = cnt = 0
# for i in range(1, n):
#     dp[i] = 2*A[i-1]-dp[i-1]
#     cnt += dp[i]

# # 補完システム
# # print(SUM, cnt)
# init = SUM-cnt
# dp = [0]*n
# dp[0] = cnt = init
# for i in range(1, n):
#     dp[i] = 2*A[i-1]-dp[i-1]
#     cnt += dp[i]

# print(*dp)

# for x in dp[:-1]:
#     print(x+init, end=' ')
#     init *= -1
# else:
#     print(dp[-1]+init)


# n = int(input())
# A = list(map(int, input().split()))
# SUM = sum(A)
# MIN = min(A)
# start = A.index(MIN)

# dp = [0]*n
# dp[start] = cnt = 0
# # dp[0] = cnt = 0
# for i in range(start+1, n):
#     # for i in range(1, n):
#     dp[i] = 2*A[i-1]-dp[i-1]
#     cnt += dp[i]
# else:
#     for i in range(start):
#         dp[i] = 2*A[i-1]-dp[i-1]
#         cnt += dp[i]

# # 補完システム
# # print(SUM, cnt)
# odd = SUM-cnt
# dp = [0]*n
# dp[start] = cnt = odd
# for i in range(start+1, n):
#     dp[i] = 2*A[i-1]-dp[i-1]
#     cnt += dp[i]
# else:
#     for i in range(start):
#         dp[i] = 2*A[i-1]-dp[i-1]
#         cnt += dp[i]

# print(*dp)

# for odd in range(0, 10**9+1, 2):
#     dp = [0]*n
#     dp[start] = cnt = odd
#     for i in range(start+1, n):
#         dp[i] = 2*A[i-1]-dp[i-1]
#         cnt += dp[i]
#     else:
#         for i in range(start):
#             dp[i] = 2*A[i-1]-dp[i-1]
#             cnt += dp[i]
#     # 補完システム
#     # print(SUM, cnt)
#     odd = SUM-cnt
#     dp = [0]*n
#     dp[start] = cnt = odd
#     for i in range(start+1, n):
#         dp[i] = 2*A[i-1]-dp[i-1]
#         cnt += dp[i]
#     else:
#         for i in range(start):
#             dp[i] = 2*A[i-1]-dp[i-1]
#             cnt += dp[i]

#     if cnt == SUM:
#         break
# print(*dp)

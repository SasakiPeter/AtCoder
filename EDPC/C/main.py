import sys
input = sys.stdin.readline
n = int(input())
dp = [[0]*3 for _ in range(n+1)]

# 配る
for i in range(n):
    a, b, c = map(int, input().split())
    dp[i+1][0] = max(dp[i][1], dp[i][2])+a
    dp[i+1][1] = max(dp[i][0], dp[i][2])+b
    dp[i+1][2] = max(dp[i][0], dp[i][1])+c
print(max(dp[-1]))

# import sys
# input = sys.stdin.readline
# n = int(input())
# abc = [tuple(map(int, input().split()))for _ in range(n)]
# # 再帰DP書いてみる
# ans = 0
# dp = [0]*n
# dp[0] = abc[0][0]
# not_turn = 0
# for i in range(1, n):
#     a, b, c = abc[i]
#     if not_turn == 0:
#         if b < c:
#             dp[i] = dp[i-1]+c
#             not_turn = 2
#         elif c < b:
#             dp[i] = dp[i-1]+b
#             not_turn = 1
#         else:
#             dp[i] = dp[i-1]+b
#             not_turn = -1
#     elif not_turn == 1:
#         if a < c:
#             dp[i] = dp[i-1]+c
#             not_turn = 2
#         elif c < a:
#             dp[i] = dp[i-1]+a
#             not_turn = 0
#         else:
#             dp[i] = dp[i-1]+a
#             not_turn = -1
#     elif not_turn == 2:
#         if a < b:
#             dp[i] = dp[i-1]+b
#             not_turn = 1
#         elif b < a:
#             dp[i] = dp[i-1]+a
#             not_turn = 0
#         else:
#             dp[i] = dp[i-1]+a
#             not_turn = -1
#     else:
#         dp[i] = dp[i-1] + max([a, b, c])
#         # 処理が雑
#         not_turn = [a, b, c].index(max([a, b, c]))
# ans = max(ans, dp[-1])
# dp = [0]*n
# dp[0] = abc[0][1]
# not_turn = 0
# for i in range(1, n):
#     a, b, c = abc[i]
#     if not_turn == 0:
#         if b < c:
#             dp[i] = dp[i-1]+c
#             not_turn = 2
#         elif c < b:
#             dp[i] = dp[i-1]+b
#             not_turn = 1
#         else:
#             dp[i] = dp[i-1]+b
#             not_turn = -1
#     elif not_turn == 1:
#         if a < c:
#             dp[i] = dp[i-1]+c
#             not_turn = 2
#         elif c < a:
#             dp[i] = dp[i-1]+a
#             not_turn = 0
#         else:
#             dp[i] = dp[i-1]+a
#             not_turn = -1
#     elif not_turn == 2:
#         if a < b:
#             dp[i] = dp[i-1]+b
#             not_turn = 1
#         elif b < a:
#             dp[i] = dp[i-1]+a
#             not_turn = 0
#         else:
#             dp[i] = dp[i-1]+a
#             not_turn = -1
#     else:
#         dp[i] = dp[i-1] + max([a, b, c])
#         # 処理が雑
#         not_turn = [a, b, c].index(max([a, b, c]))
# ans = max(ans, dp[-1])
# dp = [0]*n
# dp[0] = abc[0][2]
# not_turn = 0
# for i in range(1, n):
#     a, b, c = abc[i]
#     if not_turn == 0:
#         if b < c:
#             dp[i] = dp[i-1]+c
#             not_turn = 2
#         elif c < b:
#             dp[i] = dp[i-1]+b
#             not_turn = 1
#         else:
#             dp[i] = dp[i-1]+b
#             not_turn = -1
#     elif not_turn == 1:
#         if a < c:
#             dp[i] = dp[i-1]+c
#             not_turn = 2
#         elif c < a:
#             dp[i] = dp[i-1]+a
#             not_turn = 0
#         else:
#             dp[i] = dp[i-1]+a
#             not_turn = -1
#     elif not_turn == 2:
#         if a < b:
#             dp[i] = dp[i-1]+b
#             not_turn = 1
#         elif b < a:
#             dp[i] = dp[i-1]+a
#             not_turn = 0
#         else:
#             dp[i] = dp[i-1]+a
#             not_turn = -1
#     else:
#         dp[i] = dp[i-1] + max([a, b, c])
#         # 処理が雑
#         not_turn = [a, b, c].index(max([a, b, c]))
# ans = max(ans, dp[-1])

# print(ans)

# 違うわこれ、各日について

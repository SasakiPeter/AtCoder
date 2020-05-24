# pythonのための高速化→1981msというギリギリで間に合う
n = int(input())
s = input()
C = list(map(int, input().split()))
D = list(map(int, input().split()))
INF = 10**18
dp = [[INF]*(n//2+2) for _ in range(n+1)]
dp[0][0] = 0

# 配る
for i, (cur, c, d) in enumerate(zip(s, C, D)):
    end = i+1
    if n//2+1 < i+1:
        end = n-i+1
    for j in range(end):
        val = dp[i][j]
        valc = val+c
        # 削除
        if val+d < dp[i+1][j]:
            dp[i+1][j] = val+d

        if cur == ')':
            val, valc = valc, val
        if val < dp[i+1][j+1]:
            dp[i+1][j+1] = val
        if 0 <= j-1 and valc < dp[i+1][j-1]:
            dp[i+1][j-1] = valc


print(dp[n][0])


# n = int(input())
# s = input()
# C = list(map(int, input().split()))
# D = list(map(int, input().split()))
# INF = 10**18
# dp = [[INF]*(n+1)for _ in range(n+1)]
# dp[0][0] = 0

# # 配る
# for i in range(n):
#     cur = s[i]
#     c = C[i]
#     d = D[i]
#     for j in range(n):
#         if cur == '(':
#             # 何もしない
#             dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j])
#             # 変換
#             if 0 <= j-1:
#                 dp[i+1][j-1] = min(dp[i+1][j-1], dp[i][j]+c)
#             # 削除
#             dp[i+1][j] = min(dp[i+1][j], dp[i][j]+d)
#         else:
#             if 0 <= j-1:
#                 dp[i+1][j-1] = min(dp[i+1][j-1], dp[i][j])
#             # わざわざ変換する遷移
#             dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]+c)
#             # わざわざ削除する遷移
#             dp[i+1][j] = min(dp[i+1][j], dp[i][j]+d)

# # for row in dp:
# #     print(row)
# print(dp[n][0])

# 実は１次元でもできる　これやると早い
n, w = map(int, input().split())
weights, values = zip(*[tuple(map(int, input().split()))for _ in range(n)])
dp = [0]*(w+1)
for i in range(1, n+1):
    for j in reversed(range(1, w+1)):
        if j-weights[i-1] < 0:
            continue
        dp[j] = max(dp[j], dp[j-weights[i-1]]+values[i-1])
print(dp[-1])

# # 実はこれ、並行世界線DPか？
# # そのアイテムを選んだ世界線と、まだ選んでない世界線
# # C問題との違いは、Cは前回とったやつだけ見ればよかったけど
# # 今回は、今まで全ての中ですでに選んだものは選べないという点
# N, W = map(int, input().split())
# wv = [tuple(map(int, input().split()))for _ in range(N)]
# dp = [[0]*(W+1) for _ in range(N+1)]

# # 貰う方がきれいにかけそう
# for i in range(1, N+1):
#     for j in range(1, W+1):
#         if 0 <= j-wv[i-1][0]:
#             # print(j, wv[i-1])
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-wv[i-1][0]]+wv[i-1][1])
#         dp[i][j] = max(dp[i-1][j], dp[i][j])

# print(dp[-1][-1])

# # 配る
# for i in range(N):
#     # i = 0
#     for j in range(W):
#         w, v = wv[i]
#         if N < i+1:
#             continue
#         dp[i+1][j] = max(dp[i+1][j], dp[i][j])
#         if W < j+w:
#             continue
#         dp[i+1][j+w] = max(dp[i][j+w], dp[i][j]+v)
# print(dp[-1][-1])


# 基本的には、３を選べばいいんだど、障害物を飛び越すのに
# １か２を使って、０に１００回以内にできるかみたいな問題に似ている
# このときは、

# # 同じアイテムがいくらでもあるときは、
# # 適当にDAG書いたら書けたのでとけそうな気がする
# # いくらでもあるときはO(NW)でとけそう

# N, W = map(int, input().split())
# wv = [tuple(map(int, input().split()))for _ in range(N)]
# dp = [0]*(W+1)
# # 配る
# for i in range(W):
#     for w, v in wv:
#         if W < i+w:
#             continue
#         dp[i+w] = max(dp[i+w], dp[i]+v)
# print(dp[-1])
# print(dp)

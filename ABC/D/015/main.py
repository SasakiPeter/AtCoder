# widthでやる場合　2次元に落とし込む
# これ、相当早い
w = int(input())
n, K = map(int, input().split())
widths, imps = zip(*[tuple(map(int, input().split()))for _ in range(n)])
UI = 5*10**3
INF = 10**9
dp = [[INF]*(UI+1) for _ in range(K+1)]
for k in range(K+1):
    dp[k][0] = 0

for i in range(1, n+1):
    for k in reversed(range(1, K+1)):
        for j in range(1, UI+1):
            if j-imps[i-1] < 0:
                continue
            dp[k][j] = min(dp[k][j], dp[k-1][j-imps[i-1]]+widths[i-1])

ans = 0
for j in reversed(range(1, UI+1)):
    if dp[-1][j] <= w:
        ans = j
        break
print(ans)

# # 2次元に落とし込むことに成功した！！！
# # 逆順に回すことにより、重複して緩和しないということができる
# # 空間計算量は変わらないけど、メモリの使用量が大幅に落とすことができた
# w = int(input())
# n, K = map(int, input().split())
# widths, imps = zip(*[tuple(map(int, input().split()))for _ in range(n)])
# INF = 10**9
# dp = [[0]*(w+1) for _ in range(K+1)]

# for i in range(1, n+1):
#     for k in reversed(range(1, K+1)):
#         # ここ、逆に回す必要ない　普段はここを逆にするけど
#         for j in range(1, w+1):
#             if j-widths[i-1] < 0:
#                 continue
#             dp[k][j] = max(dp[k][j], dp[k-1][j-widths[i-1]]+imps[i-1])
# print(dp[-1][-1])

# # widthでやる場合　pypyでなんとか３次元DP
# # これは割と早いけど、ちゃんと書かないとMLEとかTLEとかひどい
# w = int(input())
# n, K = map(int, input().split())
# widths, imps = zip(*[tuple(map(int, input().split()))for _ in range(n)])
# UI = 5*10**3
# # pypyだとこれは重い上に遅い
# # INF = float('inf')
# INF = 10**9
# # [0]+[INF]*(UI+1) みたいな配列の結合も遅い
# dp = [[[INF]*(UI+1) for _ in range(K+1)] for _ in range(n+1)]
# for i in range(n+1):
#     for j in range(K+1):
#         dp[i][j][0] = 0

# for i in range(1, n+1):
#     for k in range(1, K+1):
#         for j in range(1, UI+1):
#             dp[i][k][j] = dp[i-1][k][j]
#             if j-imps[i-1] < 0:
#                 continue
#             dp[i][k][j] = min(dp[i][k][j], dp[i-1][k-1]
#                               [j-imps[i-1]]+widths[i-1])

# ans = 0
# for j in reversed(range(1, UI+1)):
#     if dp[-1][-1][j] <= w:
#         ans = j
#         break
# print(ans)

# # 価値でやる場合　pypyでなんとか３次元DP
# w = int(input())
# n, K = map(int, input().split())
# widths, imps = zip(*[tuple(map(int, input().split()))for _ in range(n)])
# dp = [[[0]*(w+1) for _ in range(K+1)] for _ in range(n+1)]

# for i in range(1, n+1):
#     for k in range(1, K+1):
#         for j in range(1, w+1):
#             dp[i][k][j] = dp[i-1][k][j]
#             if j-widths[i-1] < 0:
#                 continue
#             dp[i][k][j] = max(dp[i][k][j], dp[i-1][k-1]
#                               [j-widths[i-1]]+imps[i-1])

# # print(dp[-1])
# print(dp[-1][-1][-1])


# 重さでやっても重いものは重い
# w = int(input())
# n, K = map(int, input().split())
# widths, imps = zip(*[tuple(map(int, input().split()))for _ in range(n)])
# UI = 5*10**3
# INF = float('inf')
# dp = [[[0]+[INF]*UI for _ in range(K+1)] for _ in range(n+1)]
# # ls = [[0]*(K+1)]
# # for _ in range(UI):
# #     ls.append([INF]*(K+1))
# # dp = [ls for _ in range(n+1)]

# # print(len(dp))
# # print(len(dp[0]))
# # print(len(dp[0][0]))
# # print(dp[0])

# # 貰う
# for i in range(1, n+1):
#     for j in range(1, UI+1):
#         for k in range(1, K+1):
#             # dp[i][j][k] = dp[i-1][j][k]
#             dp[i][k][j] = dp[i-1][k][j]
#             if j-imps[i-1] < 0:
#                 continue
#             dp[i][k][j] = min(dp[i][k][j], dp[i-1][k-1]
#                               [j-imps[i-1]]+widths[i-1])
#             # dp[i][j][k] = min(dp[i][j][k], dp[i-1]
#             #                   [j-imps[i-1]][k-1]+widths[i-1])

# ans = 0
# for j in range(UI+1):
#     if dp[-1][-1][j] <= w:
#         # print(dp[-1][j], j)
#         ans = j
# print(ans)

# #!/usr/bin/env python3
# # 価値でやる場合
# w = int(input())
# n, K = map(int, input().split())
# widths, imps = zip(*[tuple(map(int, input().split()))for _ in range(n)])
# dp = [[[0]*(K+1) for _ in range(w+1)] for _ in range(n+1)]

# # 貰う
# for i in range(1, n+1):
#     for j in range(1, w+1):
#         for k in range(1, K+1):
#             # さらに並行世界線を分岐！？！？
#             dp[i][j][k] = dp[i-1][j][k]
#             if j-widths[i-1] < 0:
#                 continue
#             dp[i][j][k] = max(dp[i][j][k], dp[i-1]
#                               [j-widths[i-1]][k-1]+imps[i-1])

# print(dp[-1][-1][-1])


# 頑張ってやってみたけど、重複して数えちゃってダメだった
# #!/usr/bin/env python3
# # これ、３次元DPでは？
# w = int(input())
# n, k = map(int, input().split())
# widths, imps = zip(*[tuple(map(int, input().split()))for _ in range(n)])
# UV = 5*10**3
# # UV = 100*17
# INF = float('inf')
# # dp = [[(0, set())]+[(INF, set())]*UV for _ in range(n+1)]
# dp = [[(0, 0)]+[(INF, 0)]*UV for _ in range(n+1)]

# # 貰う
# for i in range(1, n+1):
#     for j in range(1, UV+1):
#         dp[i][j] = dp[i-1][j]
#         if j-imps[i-1] < 0:
#             continue
#         if dp[i][j][0] <= dp[i-1][j-imps[i-1]][0]+widths[i-1]:
#             continue

#         # これ、カウントしすぎ
#         dp[i][j] = dp[i-1][j-imps[i-1]][0] + \
#             widths[i-1], dp[i-1][j-imps[i-1]][1]+1
#         # widths[i-1], dp[i-1][j-imps[i-1]][1] | {i}

# ans = 0
# for i in range(n+1):
#     for j in range(UV+1):
#         # if dp[i][j][0] <= w and len(dp[i][j][1]) <= k:
#         if dp[i][j][0] <= w and dp[i][j][1] <= k:
#             if ans < j:
#                 print(i, j)
#             ans = max(ans, j)
# print(ans)
# # print(dp[1])

# # kが６になってる！！
# print(dp[8][327])

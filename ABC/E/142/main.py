# いわゆるbitDP pypyで　空間計算量削減ver
# from itertools import product
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
can_open = []
cost = []
for _ in range(m):
    a, b = map(int, input().split())
    cost.append(a)
    can_open.append(sum(1 << (c-1) for c in map(int, input().split())))

n_bit = 1 << n
INF = 10**18
dp = [INF]*n_bit
dp[0] = 0

# # productを使うのは、配列の参照を減らすため
# for j, (x, y) in product(range(n_bit), zip(can_open, cost)):
#     m = j | x
#     # ここを、min使わないでかくと、代入する回数が減って、高速になる
#     # →結果pythonでも通るように
#     z = dp[j]+y
#     if dp[m] > z:
#         dp[m] = z
#     # dp[m] = min(dp[m], dp[j]+y)

# pythonなら、これが一番早い
for x, y in zip(can_open, cost):
    for j in range(n_bit):
        m = j | x
        z = dp[j]+y
        if dp[m] > z:
            dp[m] = z

# これ、めっちゃ配列参照するからpythonだと遅い
# for i in range(m):
#     for j in range(n_bit):
#         m = j | can_open[i]
#         dp[m] = min(dp[m], dp[j]+cost[i])

print(dp[-1] if dp[-1] != INF else -1)


# # いわゆるbitDP pypyで　空間計算量削減ver
# n, m = map(int, input().split())
# can_open = []
# cost = []
# for _ in range(m):
#     a, b = map(int, input().split())
#     cost.append(a)
#     it = map(int, input().split())
#     x = 0
#     for c in it:
#         x += 1 << (c-1)
#     can_open.append(x)

# n_bit = 1 << n
# INF = 10**18
# dp = [INF]*n_bit
# dp[0] = 0

# # 配る
# # for j in range(n_bit):
# # どっちからやっても変わらない
# for i in range(m):
#     for j in range(n_bit):
#         dp[j | can_open[i]] = min(dp[j | can_open[i]], dp[j]+cost[i])

# print(dp[-1] if dp[-1] != INF else -1)


# # いわゆるbitDP
# n, m = map(int, input().split())
# can_open = []
# cost = []
# for _ in range(m):
#     a, b = map(int, input().split())
#     cost.append(a)
#     it = map(int, input().split())
#     x = 0
#     for c in it:
#         x += 1 << (c-1)
#     can_open.append(x)

# n_bit = 1 << n
# INF = 10**18
# dp = [[INF]*n_bit for _ in range(m+1)]
# # dp = [[INF]*(m+1) for _ in range(n_bit)]
# dp[0][0] = 0

# # # 配る
# # for j in range(n_bit):
# #     for i in range(m):
# #         dp[j][i+1] = min(dp[j][i+1], dp[j][i])
# #         dp[j | can_open[i]][i +
# #                             1] = min(dp[j | can_open[i]][i+1], dp[j][i+1]+cost[i])

# # 配る
# for i in range(m):
#     for j in range(n_bit):
#         dp[i+1][j] = min(dp[i+1][j], dp[i][j])

#         # bit演算|だから超えることない
#         # if (j | can_open[i]) < n_bit:
#         dp[i+1][j | can_open[i]] = min(dp[i+1]
#                                        [j | can_open[i]], dp[i+1][j]+cost[i])

# # for row in dp:
# #     print(row)

# print(dp[-1][-1] if dp[-1][-1] != INF else -1)

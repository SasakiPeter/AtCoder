# topological sortしてみる←別に早くならなかった
# 頂点の入力次数を記録する
# 頂点の入力次数が0のものをqueueに追加
# queueから取り出したノードをソート列に追加
# そこに隣接するノードの次元を下げて、0になったら、queueに追加
# grid上でこれを行うのはむりすぎるので、一度隣接リストに変換した
# 方がいい
import sys
input = sys.stdin.readline
h, w = map(int, input().split())
grid = []
for _ in range(h):
    a = list(map(int, input().split()))
    grid.extend(a)
n = h*w
MOD = 10**9+7
edges = [[]for _ in range(n)]
in_d = [0]*n
for v in range(n):
    dirc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for di, dj in dirc:
        i, j = divmod(v, w)
        x, y = i+di, j+dj
        if x < 0 or h <= x or y < 0 or w <= y:
            continue
        v2 = w*x+y
        if grid[v2] <= grid[v]:
            continue
        edges[v].append(v2)
        in_d[v2] += 1

# topological sort
next_v = []
for v in range(n):
    if in_d[v] == 0:
        next_v.append(v)
inv_exploring_order = []
while next_v:
    v = next_v.pop()
    inv_exploring_order.append(v)
    for v2 in edges[v]:
        in_d[v2] -= 1
        if in_d[v2] == 0:
            next_v.append(v2)

dist = [0]*n
for v in reversed(inv_exploring_order):
    cnt = 1
    for v2 in edges[v]:
        cnt += dist[v2] % MOD
    dist[v] = cnt % MOD
print(sum(dist) % MOD)

# 2dをconvert
# for i in range(h):
#     for j in range(w):
#         dirc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#         for di, dj in dirc:
#             x, y = i+di, j+dj
#             if x < 0 or h <= x or y < 0 or w <= y:
#                 continue
#             if grid[x][y] <= grid[i][j]:
#                 continue
#             v, v2 = w*i+j, w*x+y
#             edges[v].append(v2)
#             in_d[v2] += 1


# DFS
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)
# h, w = map(int, input().split())
# grid = [list(map(int, input().split()))for _ in range(h)]
# MOD = 10**9+7

# # for row in grid:
# #     print(row)

# # 1,1~h-2,w-2
# # 尋ねていない点がなくなるまで、全ての点から探索していって、
# # visited = [[0]*w for _ in range(h)]
# # DFSで経路を記録していく
# dist = [[-1]*w for _ in range(h)]


# def dfs(pos):
#     i, j = pos
#     dirc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#     cnt = 1
#     for di, dj in dirc:
#         x, y = i+di, j+dj
#         if x < 0 or h <= x or y < 0 or w <= y:
#             continue
#         if grid[x][y] <= grid[i][j]:
#             continue
#         if dist[x][y] == -1:
#             dfs((x, y))
#         cnt += dist[x][y]
#         # print(x, y, visited)
#     dist[i][j] = cnt % MOD


# for i in range(h):
#     for j in range(w):
#         if dist[i][j] != -1:
#             continue
#         dfs((i, j))

# # 最後に、その経路を合計する
# ans = 0
# for row in dist:
#     ans += sum(row) % MOD
#     ans %= MOD
# print(ans % MOD)


# # 探す方が手間
# roots = []
# for i in range(h):
#     for j in range(w):
#         dirc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#         for di, dj in dirc:
#             x, y = i+di, j+dj
#             if x < 0 or h <= x or y < 0 or w <= y:
#                 continue
#             if grid[i][j] > grid[x][y]:
#                 break
#         else:
#             roots.append((i, j))


# for i, j in roots:
#     dfs((i, j))

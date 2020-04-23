#!/usr/bin/env python3
# Coins Respawnやって、実装おかしくね？って思ったのでまたきた
n, m = map(int, input().split())
edges = []
forward_edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a, b, -c))
    forward_edges[a].append(b)

stack = [0]
can_reach = [0]*n
while stack:
    v = stack.pop()
    if can_reach[v]:
        continue
    can_reach[v] = 1
    for v2 in forward_edges[v]:
        if can_reach[v2]:
            continue
        stack.append(v2)

INF = 10**18
dist = [INF]*n
dist[0] = 0
# 理論上、N-1回の更新でうまくいくはずなんや
for _ in range(n-1):
    for v, v2, c in edges:
        if dist[v2] <= dist[v]+c:
            continue
        dist[v2] = dist[v]+c

negative = [0]*n
# プラスでN回回せば、確実に伝播するんや！！
for i in range(n):
    for v, v2, c in edges:
        if dist[v2] <= dist[v]+c:
            continue
        if not can_reach[v2]:
            continue
        dist[v2] = -INF
        negative[v2] = 1

if negative[-1]:
    print('inf')
else:
    print(-dist[-1])

# # 負の閉路には２種類あって、最短経路を含む負の閉路と、含まない負の閉路がある
# # これを区別できないと意味がないので、自前でbellman-fordを実装するか、
# # 最短経路に関係しない負の閉路を取り除いてから、bellman-fordにかけるしかない
# # 負の閉路を取り除くには、強連結分解とかするんじゃね？

# # もしくは、閉路がゴールを含むかどうかで判断してもいい

# n, m = map(int, input().split())
# edges = []
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     a -= 1
#     b -= 1
#     edges.append((a, b, -c))

# init_v = 0
# INF = float('inf')
# dist = [INF]*n
# dist[init_v] = 0
# # negative_cycle = 0

# # 経路復元
# prev = [INF]*n

# for i in range(n):
#     # for i in range(2*n):
#     for v, v2, c in edges:
#         if dist[v2] <= dist[v]+c:
#             continue
#         dist[v2] = dist[v]+c
#         prev[v2] = v
#         # if i >= n-1 and v2 == n-1:
#         #     negative_cycle = 1
# # print(dist)

# goal = n-1
# x = goal
# path = [x]
# while x != 0:
#     x = prev[x]
#     path.append(x)

# # print(path[::-1])

# negative = [0]*n
# for i in range(n):
#     for v, v2, c in edges:
#         if dist[v2] <= dist[v]+c:
#             continue
#         dist[v2] = dist[v]+c
#         negative[v2] = 1

# # print(negative)

# # if negative_cycle:
# if negative[-1]:
#     print('inf')
# else:
#     print(-dist[-1])


# print(dist)

# from scipy.sparse.csgraph import csgraph_from_dense, bellman_ford
# from scipy.sparse.csgraph._shortest_path import NegativeCycleError

# n, m = map(int, input().split())
# GRAPH = [[0]*n for _ in range(n)]

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     a -= 1
#     b -= 1
#     GRAPH[a][b] = -c

# try:
#     sp = bellman_ford(csgraph_from_dense(GRAPH), indices=0)
# # AtCoder環境だと、変なエラーが出る
# except NegativeCycleError:
#     print('inf')
# else:
#     print(-int(sp[-1]))

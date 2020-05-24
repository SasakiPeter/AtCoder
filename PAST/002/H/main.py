#!/usr/bin/env python3
# S-1-2-3-4-5-6-7-8-9-Gを連結するようなMSTを考える
# 結論として、このアルゴリズムは間違っていそうだが、なぜかよく分からない
# ↑dijkstraならいける？←ダメでした
# ↑辺の貼り方がおかしいだけだった。
# 数字が同じでも頂点を区別してあげないといけないので、
# MSTでは求めることができない。
from collections import defaultdict
from itertools import product
import heapq
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

# 頂点ごとに座標を集計
start = None
goal = None
cnt = defaultdict(list)
for i in range(n):
    A = input()
    for j in range(m):
        cnt[A[j]].append((i, j))
        if A[j] == 'S':
            start = (i, j)
        elif A[j] == 'G':
            goal = (i, j)


def to_v(i, j):
    return i*m+j


INF = 10**18
route = 'S123456789G'
# 同じ数字でも座標が違ったら、別の頂点
N = n*m
edges = [[]for _ in range(N)]

# 辺を生やす
for v, v2 in zip(route, route[1:]):
    if not cnt[v] or not cnt[v2]:
        print(-1)
        exit()
    # 座標からマンハッタン距離を計算する
    for (i, j), (i2, j2) in product(cnt[v], cnt[v2]):
        edges[to_v(i, j)].append((abs(i-i2)+abs(j-j2), to_v(i2, j2)))
        edges[to_v(i2, j2)].append((abs(i-i2)+abs(j-j2), to_v(i, j)))


def dijkstra(init_v):
    next_v = [(0, init_v)]
    dist = [INF]*N
    dist[init_v] = 0
    while next_v:
        d, v = heapq.heappop(next_v)
        if dist[v] < d:
            continue
        for d, v2 in edges[v]:
            if dist[v2] <= dist[v]+d:
                continue
            dist[v2] = dist[v]+d
            heapq.heappush(next_v, (dist[v2], v2))
    return dist


# print(edges)
# スタート地点が間違っている？
dist = dijkstra(to_v(*start))
# print(dist)
print(dist[to_v(*goal)])


# MST
# s-1-2-3-4-5-6-7-8-9-Gの順に最短路の辺をはっていく
# そのときに、各頂点に、どの数字が書かれているかを記録しておく
# その後に、各頂点から頂点の距離を求めて、辺をはる
# そしてkruscalで終わり

# # S-1-2-3-4-5-6-7-8-9-Gを連結するようなMSTを考える
# # 結論として、このアルゴリズムは間違っていそうだが、なぜかよく分からない
# from collections import defaultdict
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)
# n, m = map(int, input().split())

# # 頂点ごとに座標を集計
# cnt = defaultdict(list)
# for i in range(n):
#     A = input()
#     for j in range(m):
#         cnt[A[j]].append((i, j))

# route = 'S123456789G'
# N = 11
# edges = []


# def to_idx(r):
#     if r == 'S':
#         return 0
#     elif r == 'G':
#         return 10
#     else:
#         return int(r)


# # 辺を生やす
# for v, v2 in zip(route, route[1:]):
#     if not cnt[v] or not cnt[v2]:
#         print(-1)
#         exit()
#     # 座標からマンハッタン距離を計算する
#     for i, j in cnt[v]:
#         for i2, j2 in cnt[v2]:
#             edges.append((abs(i-i2)+abs(j-j2), to_idx(v), to_idx(v2)))
# edges.sort()


# class UnionFind:
#     def __init__(self, n):
#         self.p = [-1]*n
#         self.r = [1]*n

#     def find(self, x):
#         if self.p[x] < 0:
#             return x
#         else:
#             self.p[x] = self.find(self.p[x])
#             return self.p[x]

#     def union(self, x, y):
#         rx, ry = self.find(x), self.find(y)
#         if rx != ry:
#             if self.r[rx] > self.r[ry]:
#                 rx, ry = ry, rx
#             if self.r[rx] == self.r[ry]:
#                 self.r[ry] += 1
#             self.p[ry] += self.p[rx]
#             self.p[rx] = ry

#     def same(self, x, y):
#         return self.find(x) == self.find(y)


# # kruscal
# uf = UnionFind(N)
# ans = 0
# for w, v, v2 in edges:
#     if uf.same(v, v2):
#         continue
#     uf.union(v, v2)
#     ans += w
# print(ans)

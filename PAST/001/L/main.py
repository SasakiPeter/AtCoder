# MST最小全域木を考える　prim
import heapq
from itertools import product
import sys
from copy import deepcopy
input = sys.stdin.readline
n, m = map(int, input().split())
xyc_L = [tuple(map(int, input().split()))for _ in range(n)]
xyc_S = [tuple(map(int, input().split()))for _ in range(m)]

INF = 10**18
ans = INF
for bit in product((0, 1), repeat=m):
    xyc = deepcopy(xyc_L)
    for i in range(m):
        if bit[i]:
            xyc.append(xyc_S[i])
    N = len(xyc)
    edges = [[]for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1, N):
            x1, y1, c1 = xyc[i]
            x2, y2, c2 = xyc[j]
            elen = ((x1-x2)**2+(y1-y2)**2)**.5
            if c1 != c2:
                elen *= 10
            edges[i].append((elen, j))
            edges[j].append((elen, i))

    visited = [0]*N
    mincost = [INF]*N
    mincost[0] = 0
    cost = 0
    next_v = [(0, 0)]
    while next_v:
        w, v = heapq.heappop(next_v)
        if visited[v]:
            continue
        visited[v] = 1
        cost += w
        for w, v2 in edges[v]:
            if visited[v2]:
                continue
            if mincost[v2] <= w:
                continue
            mincost[v2] = w
            heapq.heappush(next_v, (w, v2))
    if cost < ans:
        ans = cost
print(ans)

# # MST最小全域木を考える　kruscal
# from itertools import product
# import sys
# from copy import deepcopy
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)
# n, m = map(int, input().split())
# xyc_L = [tuple(map(int, input().split()))for _ in range(n)]
# xyc_S = [tuple(map(int, input().split()))for _ in range(m)]


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


# INF = 10**18
# ans = INF
# for bit in product((0, 1), repeat=m):
#     xyc = deepcopy(xyc_L)
#     for i in range(m):
#         if bit[i]:
#             xyc.append(xyc_S[i])
#     edges = []
#     N = len(xyc)
#     for i in range(N-1):
#         for j in range(i+1, N):
#             x1, y1, c1 = xyc[i]
#             x2, y2, c2 = xyc[j]
#             elen = ((x1-x2)**2+(y1-y2)**2)**.5
#             if c1 != c2:
#                 elen *= 10
#             edges.append((elen, i, j))
#     edges.sort()
#     uf = UnionFind(N)
#     cost = 0
#     for w, v, v2 in edges:
#         if uf.same(v, v2):
#             continue
#         uf.union(v, v2)
#         cost += w
#     if cost < ans:
#         ans = cost
# print(ans)


# ↓ダメだった
# # ノードの数が少ないので、考えられる全ての辺をはった後に
# # dijkstraすればいい
# # そうすると、次の問題は、多数ある大きい塔の頂点を
# # 結んだときに、どのへんが必要か？が欲しい
# # これはtrackすれば良さそう
# import heapq
# n, m = map(int, input().split())
# N = n+m
# edges = [[]for _ in range(N)]
# # xyc_L = [tuple(map(int, input().split()))for _ in range(n)]
# # xyc_S = [tuple(map(int, input().split()))for _ in range(m)]
# # xyc = xyc_L+xyc_S
# xyc = [tuple(map(int, input().split()))for _ in range(n)]
# xyc.extend([tuple(map(int, input().split()))for _ in range(m)])


# def euclid_len(i, j):
#     x1, y1, c1 = xyc[i]
#     x2, y2, c2 = xyc[j]
#     elen = ((x1-x2)**2+(y1-y2)**2)**.5
#     if c1 != c2:
#         elen *= 10
#     return elen


# for i in range(N-1):
#     for j in range(i+1, N):
#         elen = euclid_len(i, j)
#         edges[i].append((elen, j))
#         edges[j].append((elen, i))

# # print(edges)


# def dijkstra(init_v):
#     next_v = [(0, init_v)]
#     INF = 10**18
#     dist = [INF]*N
#     prev = [-1]*N
#     dist[init_v] = 0
#     while next_v:
#         d, v = heapq.heappop(next_v)
#         if dist[v] < d:
#             continue
#         for d, v2 in edges[v]:
#             if dist[v2] <= dist[v]+d:
#                 continue
#             dist[v2] = dist[v]+d
#             prev[v2] = v
#             heapq.heappush(next_v, (dist[v2], v2))
#     return dist, prev


# # 全ての大きな塔からの最短経路を求める
# # 中継地を全探索して、

# dist, prev = dijkstra(0)

# # n-1までが大きい塔なので、そこまでを遡ってtrackする
# # trackするときに、頂点のペアを保持して
# # その辺のコストを合計すればいい
# track = set()
# for v in range(n):
#     while prev[v] != -1:
#         track.add((v, prev[v]))
#         v = prev[v]
# # print(track)

# ans = 0
# for i, j in track:
#     ans += euclid_len(i, j)
# print("{:.7f}".format(ans))

# 高速化?
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
NV = 3*n
edges = [[]for _ in range(NV)]


def to_v(i, j):
    return 3*i+j


for _ in range(m):
    u, v = list(map(lambda x: int(x)-1, input().split()))
    for j in range(3):
        edges[to_v(u, j)].append(to_v(v, (j+1) % 3))
s, t = list(map(lambda x: int(x)-1, input().split()))
init_v = to_v(s, 0)
INF = 10**18
dist = [INF]*NV
dist[init_v] = 0
next_v = deque([init_v])
while next_v:
    v = next_v.popleft()
    for v2 in edges[v]:
        if dist[v2] <= dist[v]+1:
            continue
        dist[v2] = dist[v]+1
        next_v.append(v2)

print(dist[to_v(t, 0)]//3 if dist[to_v(t, 0)] != INF else -1)


# # kenとkenとpa(最初はpa)の３つの遷移状態を作ればO(V+E)
# from collections import deque
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# UV = [[]for _ in range(n)]
# for _ in range(m):
#     u, v = list(map(lambda x: int(x)-1, input().split()))
#     UV[u].append(v)
# s, t = list(map(lambda x: int(x)-1, input().split()))

# NV = 3*n
# edges = [[]for _ in range(NV)]


# def to_v(i, j):
#     return 3*i+j


# for i in range(n):
#     for i2 in UV[i]:
#         for j in range(3):
#             edges[to_v(i, j)].append(to_v(i2, (j+1) % 3))

# init_v = to_v(s, 0)
# INF = 10**18
# dist = [INF]*NV
# dist[init_v] = 0
# next_v = deque([init_v])
# while next_v:
#     v = next_v.popleft()
#     for v2 in edges[v]:
#         if dist[v2] <= dist[v]+1:
#             continue
#         dist[v2] = dist[v]+1
#         next_v.append(v2)

# print(dist[to_v(t, 0)]//3 if dist[to_v(t, 0)] != INF else -1)


# TLE解
# from collections import deque
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# UV = [[] for _ in range(n)]
# for _ in range(m):
#     u, v = list(map(lambda x: int(x)-1, input().split()))
#     UV[u].append(v)
# s, t = list(map(lambda x: int(x)-1, input().split()))

# edges = [set()for _ in range(n)]

# # ここ重すぎわろたんご
# # 冷静にO(VEEE)
# for v in range(n):
#     for v2 in UV[v]:
#         for v3 in UV[v2]:
#             for v4 in UV[v3]:
#                 edges[v].add(v4)

# INF = 10**18
# dist = [INF]*n
# dist[s] = 0
# next_v = deque([s])
# while next_v:
#     v = next_v.popleft()
#     for v2 in edges[v]:
#         if dist[v2] <= dist[v]+1:
#             continue
#         dist[v2] = dist[v]+1
#         next_v.append(v2)
# print(dist[t]if dist[t] != INF else -1)

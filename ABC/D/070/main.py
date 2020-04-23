# DFS再帰
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n = int(input())
edges = [[]for _ in range(n)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append((c, b))
    edges[b].append((c, a))
INF = float('inf')


def dfs(v, parent, distance):
    dist[v] = distance
    for d, v2 in edges[v]:
        if parent == v2:
            continue
        dfs(v2, v, distance+d)


q, k = map(int, input().split())
dist = [INF]*n
dfs(k-1, -1, 0)
for _ in range(q):
    x, y = map(lambda x: int(x)-1, input().split())
    print(dist[x]+dist[y])


# # Dijkstra
# import sys
# import heapq
# input = sys.stdin.readline
# n = int(input())
# edges = [[]for _ in range(n)]
# for _ in range(n-1):
#     a, b, c = map(int, input().split())
#     a -= 1
#     b -= 1
#     edges[a].append((c, b))
#     edges[b].append((c, a))
# INF = float('inf')


# def dijkstra(init_v):
#     dist = [INF]*n
#     dist[init_v] = 0
#     tasks = [(0, init_v)]
#     while tasks:
#         # print(tasks)
#         d, v = heapq.heappop(tasks)
#         if dist[v] < d:
#             continue
#         for d2, v2 in edges[v]:
#             if dist[v2] <= dist[v]+d2:
#                 continue
#             dist[v2] = dist[v]+d2
#             heapq.heappush(tasks, ((dist[v2], v2)))
#     # print(dist)
#     return dist


# q, k = map(int, input().split())
# dist = dijkstra(k-1)
# for _ in range(q):
#     x, y = map(lambda x: int(x)-1, input().split())
#     print(dist[x]+dist[y])

# # BFS
# import sys
# from collections import deque
# input = sys.stdin.readline
# n = int(input())
# edges = [[]for _ in range(n)]
# for _ in range(n-1):
#     a, b, c = map(int, input().split())
#     a -= 1
#     b -= 1
#     edges[a].append((c, b))
#     edges[b].append((c, a))
# INF = float('inf')


# def bfs(init_v):
#     dist = [INF]*n
#     dist[init_v] = 0
#     tasks = deque([(0, init_v)])
#     while tasks:
#         # print(tasks)
#         d, v = tasks.popleft()
#         for d2, v2 in edges[v]:
#             if dist[v2] <= dist[v]+d2:
#                 continue
#             dist[v2] = dist[v]+d2
#             tasks.append((dist[v2], v2))
#     # print(dist)
#     return dist


# q, k = map(int, input().split())
# dist = bfs(k-1)
# for _ in range(q):
#     x, y = map(lambda x: int(x)-1, input().split())
#     print(dist[x]+dist[y])


# # DFS
# import sys
# input = sys.stdin.readline
# # sys.setrecursionlimit(10**7)
# n = int(input())
# edges = [[]for _ in range(n)]
# for _ in range(n-1):
#     a, b, c = map(int, input().split())
#     a -= 1
#     b -= 1
#     edges[a].append((c, b))
#     edges[b].append((c, a))
# INF = float('inf')


# def dfs(init_v):
#     dist = [INF]*n
#     dist[init_v] = 0
#     tasks = [(0, init_v)]
#     while tasks:
#         # print(tasks)
#         d, v = tasks.pop()
#         for d2, v2 in edges[v]:
#             if dist[v2] <= dist[v]+d2:
#                 continue
#             dist[v2] = dist[v]+d2
#             tasks.append((dist[v2], v2))
#     # print(dist)
#     return dist


# q, k = map(int, input().split())
# dist = dfs(k-1)
# for _ in range(q):
#     x, y = map(lambda x: int(x)-1, input().split())
#     print(dist[x]+dist[y])


# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)
# INF = 10**9+1
# n = int(input())

# graph = [[] for _ in range(n+1)]
# # d = [[INF]*(n+1) for _ in range(n+1)]
# # d = {}

# for _ in range(n-1):
#     a, b, c = map(int, input().split())
#     # メモリ食いすぎる
#     # d[a][b] = d[b][a] = c

#     # ダサい
#     # d["{},{}".format(a, b)] = c
#     # d["{},{}".format(b, a)] = c
#     # graph[a].append(b)
#     # graph[b].append(a)

#     graph[a].append((b, c))
#     graph[b].append((a, c))

# q, k = map(int, input().split())
# dist = [INF]*(n+1)

# # print(graph)


# def dfs(v1, parent, add):
#     dist[v1] = add
#     # for v2 in graph[v1]:
#     for v2, d in graph[v1]:
#         if v2 == parent:
#             continue
#         dfs(v2, v1, add + d)
#         # dfs(v2, v1, add + d["{},{}".format(v1, v2)])
#         # dfs(v2, v1, add + d[v1][v2])


# dfs(k, -1, 0)
# # print(dist)

# for _ in range(q):
#     x, y = map(int, input().split())
#     print(dist[x]+dist[y])

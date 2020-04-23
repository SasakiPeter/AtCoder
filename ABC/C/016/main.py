# 解法
# DFS再帰, DFS, BFS, Dijkstra, Warshall-Floyd, 単純に探索setでまとめなど

# # Bellman-ford
# # from scipy.sparse.csgraph import csgraph_from_dense, bellman_ford
# n, m = map(int, input().split())
# # sns = [[]for _ in range(n)]
# # sns = [[0]*n for _ in range(n)]
# edges = []
# for _ in range(m):
#     a, b = list(map(lambda x: int(x)-1, input().split()))
#     # sns[a][b] = sns[b][a] = 1
#     # sns[a].append(b)
#     # sns[b].append(a)
#     edges.append((a, b, 1))
#     edges.append((b, a, 1))
# n, m = 6, 8
# edges = [(0, 1, 2), (0, 3, 4), (1, 2, 3), (2, 3, -2),
#          (3, 5, 4), (3, 4, 2), (4, 5, 1), (2, 5, 2), (3, 2, -2)]
# INF = float('inf')


# def bellman_ford(init_v):
#     # O(V*E)
#     dist = [INF]*n
#     dist[init_v] = 0
#     for i in range(n):
#         for v1, v2, d in edges:
#             # 更新してるかをみる
#             if dist[v2] <= dist[v1]+d:
#                 continue
#             dist[v2] = dist[v1]+d
#             if i == n-1:
#                 print('negative loop')
#                 print(dist)
#                 return dist
#     print(dist)
#     return dist


# for i in range(n):
#     # sp = bellman_ford(csgraph_from_dense(sns), indices=i)
#     print(sum(1 for x in bellman_ford(i) if x == 2))


# DFS再帰
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n, m = map(int, input().split())
sns = [[]for _ in range(n)]
for _ in range(m):
    a, b = list(map(lambda x: int(x)-1, input().split()))
    sns[a].append(b)
    sns[b].append(a)
INF = 10**9


def make_dfs():
    dist = [INF]*n

    def dfs(v, parent, distance):
        dist[v] = distance
        for v2 in sns[v]:
            # 来た道戻るの禁止
            if v2 == parent:
                continue
            # 閉路スルー
            if dist[v2] <= distance+1:
                continue
            dfs(v2, v, distance+1)
        return dist
    return dfs


for i in range(n):
    dfs = make_dfs()
    print(sum(1 for x in dfs(i, -1, 0)if x == 2))

# # DFS
# n, m = map(int, input().split())
# sns = [[]for _ in range(n)]
# for _ in range(m):
#     a, b = list(map(lambda x: int(x)-1, input().split()))
#     sns[a].append(b)
#     sns[b].append(a)
# INF = 10**9


# def dfs(init_v):
#     tasks = [init_v]
#     dist = [INF]*n
#     dist[init_v] = 0
#     while tasks:
#         v = tasks.pop()
#         for v2 in sns[v]:
#             if dist[v2] <= dist[v]+1:
#                 continue
#             dist[v2] = dist[v]+1
#             tasks.append(v2)
#     return dist


# for i in range(n):
#     print(sum(1 for x in dfs(i)if x == 2))

# # BFS
# from collections import deque
# n, m = map(int, input().split())
# sns = [[]for _ in range(n)]
# for _ in range(m):
#     a, b = list(map(lambda x: int(x)-1, input().split()))
#     sns[a].append(b)
#     sns[b].append(a)
# INF = 10**9


# def bfs(init_v):
#     tasks = deque([init_v])
#     dist = [INF]*n
#     dist[init_v] = 0
#     # visited = [0]*n
#     while tasks:
#         v = tasks.popleft()
#         # if visited[v]:
#         #     continue
#         # visited[v] = 1
#         for v2 in sns[v]:
#             # if visited[v2]:
#             #     continue
#             # dist[v2] = min(dist[v2], dist[v]+1)
#             # tasks.append(v2)

#             # 戻り防止
#             if dist[v2] <= dist[v]+1:
#                 continue
#             dist[v2] = dist[v]+1
#             tasks.append(v2)
#     # print(dist)
#     return dist


# for i in range(n):
#     print(sum(1 for x in bfs(i)if x == 2))

# # 全点からのdijkstra 全然重みがあるグラフじゃないけど
# import heapq
# n, m = map(int, input().split())
# sns = [None]+[[] for _ in range(n)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     sns[a].append((1, b))
#     sns[b].append((1, a))
# INF = 10**9


# def dijkstra(init_v):
#     # init_v = (0, 0)
#     tasks = [(0, init_v)]
#     dist = [INF]*(n+1)
#     dist[init_v] = 0
#     while tasks:
#         d, v = heapq.heappop(tasks)
#         if dist[v] < d:
#             continue
#         for d2, v2 in sns[v]:
#             if dist[v2] <= dist[v]+d2:
#                 continue
#             dist[v2] = dist[v]+d2
#             heapq.heappush(tasks, (dist[v2], v2))
#     # print(dist)
#     return dist[1:]


# for i in range(1, n+1):
#     print(sum(1 for x in dijkstra(i) if x == 2))


# # 距離が２のやつを探す
# from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
# n, m = map(int, input().split())
# GRAPH = [[0]*n for _ in range(n)]
# for i in range(m):
#     a, b = list(map(lambda x: int(x)-1, input().split()))
#     GRAPH[a][b] = GRAPH[b][a] = 1
# sp = floyd_warshall(csgraph_from_dense(GRAPH))
# for i in range(n):
#     print(sum(1 for x in sp[i]if x == 2))
#     # 倍くらい遅い
#     # print(sum(x == 2 for x in sp[i]))

# n, m = map(int, input().split())
# sns = [None]+[[]for _ in range(n)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     sns[a].append(b)
#     sns[b].append(a)

# for i in range(1, n+1):
#     friends_id = sns[i]
#     ans = set()
#     for friend_id in friends_id:
#         ans |= set(sns[friend_id])
#     ans -= set(friends_id) | {i}
#     print(len(ans))

# n, m = map(int, input().split())
# d = {i: [] for i in range(n)}
# for _ in range(m):
#     a, b = map(lambda x: int(x)-1, input().split())
#     d[a].append(b)
#     d[b].append(a)


# def count_friends_friends(x):
#     friend_idx = d[x]
#     ls = [0]*n
#     for idx in friend_idx:
#         for i in d[idx]:
#             if i in friend_idx:
#                 continue
#             ls[i] = 1
#     ls[x] = 0
#     return sum(ls)


# ans = [count_friends_friends(i) for i in range(n)]
# print(*ans, sep='\n')


# n, m = map(int, input().split())
# GRAPH = [[0]*n for _ in range(n)]

# for _ in range(m):
#     a, b = map(lambda x: int(x)-1, input().split())
#     GRAPH[a][b] = GRAPH[b][a] = 1


# def count_friends_friends(x):
#     friends = GRAPH[x]
#     friend_idx = []
#     ls = [0]*n
#     for i, f in enumerate(friends):
#         if f:
#             friend_idx.append(i)

#     for idx in friend_idx:
#         for j, ff in enumerate(GRAPH[idx]):
#             if j in friend_idx:
#                 continue
#             if ff:
#                 ls[j] = 1
#     ls[x] = 0
#     return sum(ls)


# ans = [count_friends_friends(i) for i in range(n)]
# print(*ans, sep='\n')

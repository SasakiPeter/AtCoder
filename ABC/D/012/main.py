# dijkstra書き直し
import heapq
import sys
input = sys.stdin.readline
INF = 10**9
# INF = float('inf')
n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, t = map(lambda x: int(x)-1, input().split())
    edges[a].append((t+1, b))
    edges[b].append((t+1, a))


def dijkstra(start_v):
    next_nodes = [(0, start_v)]
    dist = [INF]*n
    dist[start_v] = 0
    while next_nodes:
        # print(next_nodes)
        d, v = heapq.heappop(next_nodes)
        # print(d, v, dist, 'hello')
        if dist[v] < d:
            continue
        for d, v2 in edges[v]:
            # ここ、変数をおくと、めっちゃ遅くなるので注意
            # dist_v2 = dist[v]+d

            # まだ確定していないノードであっても、
            # すでにより最短な経路が見つかっていれば
            # 探索しないので、無駄な探索が減らせる

            if dist[v2] <= dist[v]+d:
                continue
            dist[v2] = dist[v]+d
            heapq.heappush(next_nodes, (dist[v]+d, v2))
    return dist

# def dijkstra(start_v):
#     next_nodes = [(0, start_v)]
#     dist = [INF]*n
#     dist[start_v] = 0
#     visited = [0]*n
#     while next_nodes:
#         print(next_nodes)
#         d, v = heapq.heappop(next_nodes)
#         if visited[v]:
#             continue
#         visited[v] = 1
#         dist[v] = d
#         for d, v2 in edges[v]:
#             # これだけだと、まだ尋ねてないことをいいことに
#             # 同じノードへのパスをいっぱい追加しちゃう
#             if visited[v2]:
#                 continue
#             heapq.heappush(next_nodes, (dist[v]+d, v2))
#     return dist


ans = INF
for i in range(n):
    ans = min(ans, max(dijkstra(i)))
print(ans)


# # 入力的に隣接行列より隣接リスト想定してるんだから、Dijkstra使えという話
# import heapq
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# INF = 10**9
# # BN = 10**7
# edges = [[] for _ in range(n)]

# for _ in range(m):
#     a, b, t = map(int, input().split())
#     a -= 1
#     b -= 1
#     # edges[a].append(t*BN+b)
#     # edges[b].append(t*BN+a)
#     edges[a].append((t, b))
#     edges[b].append((t, a))


# def dijkstra(init_node):
#     next_nodes = [(0, init_node)]
#     # next_nodes = [(init_node)]
#     # visited = [0]*n
#     # visited[init_node] = 1
#     # dist = [-1]*n
#     dist = [INF]*n
#     dist[init_node] = 0
#     while next_nodes:
#         d, v = heapq.heappop(next_nodes)
#         # d, v = divmod(heapq.heappop(next_nodes), BN)
#         # if visited[v]:
#         #     continue
#         # visited[v] = 1
#         # dist[v] = d
#         if dist[v] < d:
#             continue
#         for d, v2 in edges[v]:
#             # for e in edges[v]:
#             # d, v2 = divmod(e, BN)
#             if dist[v2] <= dist[v]+d:
#                 continue
#             dist[v2] = dist[v]+d
#             heapq.heappush(next_nodes, (dist[v]+d, v2))
#             # heapq.heappush(next_nodes, ((dist[v]+d)*BN + v2))
#     # print(dist)
#     return dist


# ans = INF
# for i in range(n):
#     ans = min(ans, max(dijkstra(i)))
# print(ans)


# scipyは早い
# from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall

# n, m = map(int, input().split())
# INF = 10**9
# MAP = [[INF]*n for _ in range(n)]

# for i in range(n):
#     MAP[i][i] = 0

# for _ in range(m):
#     a, b, t = map(int, input().split())
#     a -= 1
#     b -= 1
#     MAP[a][b] = MAP[b][a] = t

# MAP = floyd_warshall(csgraph_from_dense(MAP))

# ans = INF
# for i in range(n):
#     ans = min(ans, max(MAP[i]))

# # print(*MAP)
# print(int(ans))

# # 普通のwarshall-floydはpythonだとTLEする
# # n頂点Dijkstraなら通る
# n, m = map(int, input().split())
# INF = 10**9
# MAP = [[INF]*n for _ in range(n)]

# for i in range(n):
#     MAP[i][i] = 0

# for _ in range(m):
#     a, b, t = map(int, input().split())
#     a -= 1
#     b -= 1
#     MAP[a][b] = MAP[b][a] = t

# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             MAP[i][j] = min(MAP[i][j], MAP[i][k]+MAP[k][j])
# ans = INF
# for i in range(n):
#     ans = min(ans, max(MAP[i]))

# # print(*MAP)
# print(ans)

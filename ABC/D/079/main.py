# warshall-floyd
h, w = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(10)]

# 中継地に使われるループが、一番外じゃないといけない
for k in range(10):
    for i in range(10):
        for j in range(10):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

shortest_path = list(zip(*graph))[1]
ans = 0
for _ in range(h):
    for a in map(int, input().split()):
        if a == -1:
            continue
        ans += shortest_path[a]
print(ans)


# # dijkstra自力実装してみる
# import heapq
# h, w = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(10)]
# # print(*graph)

# trans_graph = list(zip(*graph))
# next_nodes = []
# for idx, d in enumerate(trans_graph[1]):
#     heapq.heappush(next_nodes, ((d, idx)))
# #     next_nodes.append((d, idx))
# # heapq.heapify(next_nodes)

# INF = 10**9
# decided = [0]*10
# decided[1] = 1
# dist = [INF]*10
# dist[1] = 0

# # while 0 in decided:
# while next_nodes:
#     distance, v = heapq.heappop(next_nodes)
#     if decided[v]:
#         continue
#     decided[v] = 1
#     dist[v] = distance
#     # 確定したノードから見える新たな最短経路をqueueに追加する
#     for v2, x in enumerate(trans_graph[v]):
#         if decided[v2]:
#             continue

#         heapq.heappush(next_nodes, (dist[v]+x, v2))
# # print(next_nodes)
# # print(dist)
# # print(dist)

# ans = 0
# for _ in range(h):
#     for x in map(int, input().split()):
#         if x == -1:
#             continue
#         ans += dist[x]

# print(ans)

# # from scipy.sparse import csr_matrix
# # from scipy.sparse.csgraph import shortest_path
# from scipy.sparse.csgraph import dijkstra, csgraph_from_dense
# from collections import defaultdict
# h, w = map(int, input().split())
# table = [list(map(int, input().split())) for _ in range(10)]
# dd = defaultdict(int)
# for _ in range(h):
#     for x in map(int, input().split()):
#         if x == -1:
#             continue
#         dd[x] += 1

# # transposition
# trans_table = list(zip(*table))
# # AtCoderの実行環境だと動かない
# # scores = shortest_path(csr_matrix(trans_table), indices=1)
# # scores = dijkstra(csr_matrix(trans_table), indices=1)
# # csr_matrixよりcsgraph_from_denseの方が倍くらい早い
# scores = dijkstra(csgraph_from_dense(trans_table), indices=1)


# ans = 0
# for k, v in dd.items():
#     ans += int(scores[k])*v
# print(ans)

# 自力で解けたの偉すぎる
# from collections import defaultdict, deque

# h, w = map(int, input().split())
# table = [list(map(int, input().split())) for _ in range(10)]
# dd = defaultdict(int)
# for _ in range(h):
#     for x in map(int, input().split()):
#         if x == -1:
#             continue
#         dd[x] += 1
# # print(dd)
# INF = 10**9
# scores = [INF]*10
# decided = [0]*10
# queue = deque()

# # transposition
# trans_table = list(zip(*table))
# for i in range(10):
#     # 1に到達できる経路
#     x = trans_table[1][i]
#     scores[i] = x

# MIN = min(set(scores) ^ {0})

# while 0 in decided:
#     for idx, score in enumerate(scores):
#         if score <= MIN:
#             decided[idx] = 1

#     for i in range(10):
#         if i == 1:
#             continue
#         if decided[i]:
#             for j in range(10):
#                 if not decided[j]:
#                     queue.append((i, j))

#     while queue:
#         i, j = queue.popleft()
#         x = trans_table[i][j]
#         scores[j] = min(scores[j], scores[i]+x)

#     # 確定させたい
#     MIN += 1


# # print(scores)
# # print(decided)

# ans = 0
# for k, v in dd.items():
#     ans += scores[k]*v
# print(ans)

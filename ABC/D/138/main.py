import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**7)
n, q = map(int, input().split())
edges = [[]for _ in range(n)]
for _ in range(n-1):
    a, b = list(map(lambda x: int(x)-1, input().split()))
    edges[a].append(b)
    edges[b].append(a)

counts = [0]*n
for _ in range(q):
    p, x = map(int, input().split())
    counts[p-1] += x


euler_tour = []

# v, parentだけでよかった


def dfs(v, parent):
    euler_tour.append(v)
    for v2 in edges[v]:
        if v2 == parent:
            continue
        counts[v2] += counts[v]
        dfs(v2, v)
        euler_tour.append(v)


dfs(0, -1)
print(*counts)
# print(euler_tour)


# # DFS stackで実装する DFSより早い　pypyも使えるし
# import sys
# input = sys.stdin.readline
# n, q = map(int, input().split())
# edges = [[] for _ in range(n)]
# for _ in range(n-1):
#     a, b = list(map(lambda x: int(x)-1, input().split()))
#     edges[a].append(b)
#     edges[b].append(a)

# values = [0]*n
# for _ in range(q):
#     p, x = map(int, input().split())
#     values[p-1] += x

# stack = [0]
# visited = [0]*n
# while stack:
#     v = stack.pop()
#     if visited[v]:
#         continue
#     visited[v] = 1
#     for v2 in edges[v]:
#         if visited[v2]:
#             continue
#         values[v2] += values[v]
#         stack.append(v2)
# print(*values)


# # 2020/4/14 前と全く同じコードでビビった
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)

# n, q = map(int, input().split())
# edges = [[] for _ in range(n)]
# for _ in range(n-1):
#     a, b = list(map(lambda x: int(x)-1, input().split()))
#     edges[a].append(b)
#     edges[b].append(a)

# nodes = [0]*n
# for _ in range(q):
#     p, x = map(int, input().split())
#     nodes[p-1] += x


# def dfs(v, parent, add):
#     nodes[v] += add
#     for v2 in edges[v]:
#         if v2 == parent:
#             continue
#         dfs(v2, v, nodes[v])


# dfs(0, -1, 0)
# print(*nodes)

# # 回帰の上限解放と、入力高速化がないと間に合わない
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)

# # DFSで更新する
# n, q = map(int, input().split())

# # 隣接行列で管理するのは、閉路を探索するときくらいでいいかも
# # それか、結構処理を回してもいい時
# # graph = [[0]*(n) for _ in range(n)]
# # for _ in range(n-1):
# #     a, b = map(lambda x: int(x)-1, input().split())
# #     graph[a][b] = graph[b][a] = 1

# graph = [[] for _ in range(n)]
# for _ in range(n-1):
#     a, b = map(lambda x: int(x)-1, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# values = [0]*n
# for _ in range(q):
#     p, x = map(int, input().split())
#     values[p-1] += x

# # print(graph)
# # print(values)


# # 遅延評価DFS　上のノードから順番に伝播していけばいいので
# # DFSが向いている
# def dfs(v1, parent, add):
#     values[v1] += add

#     # だが、graphを全て探索すると重すぎる
#     # for v2 in range(n):
#     #     if not graph[v1][v2]:
#     #         continue
#     for v2 in graph[v1]:

#         # 閉路を探索するような場合は、尋ねたノードを
#         # 全て記録しておく必要があるが、木の場合は、
#         # 前のノードを記録するだけで、戻ることは防げる→有向木として
#         # DAGとして扱えるようになる
#         if v2 == parent:
#             continue
#         # ここでもいい
#         # values[v2] += values[v1]

#         dfs(v2, v1, values[v1])


# dfs(0, 0, 0)

# print(*values)

# # topological sortはされているのだ。←いない
# # DAGなのでDPできる

# n, q = map(int, input().split())

# rank = {i: 0 for i in range(n)}
# nodes = [[] for _ in range(n)]
# for _ in range(n-1):
#     a, b = map(lambda x: int(x)-1, input().split())
#     # この時点で追えなくなってる　根からの深さを
#     nodes[a].append(b)
#     rank[b] += 1

# # print(nodes)

# dp = [0]*n

# for _ in range(q):
#     p, x = map(int, input().split())
#     dp[p-1] += x


# # print(dp)
# # 伝播 配るDP
# # 根に近いノードから更新しないとだめ
# # it = [x for x, y in sorted(rank.items(), key=lambda x: x[1])]
# print(n, q, dp, nodes)

# # for i in range(n):
# for i in (0, 2, 1):
#     for idx in nodes[i]:
#         dp[idx] += dp[i]

# print(*dp)

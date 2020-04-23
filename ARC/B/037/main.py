# 2020/4/19 昔のコードが無駄が多いので、書き直す
n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = list(map(lambda x: int(x)-1, input().split()))
    edges[a].append(b)
    edges[b].append(a)


def dfs(v, parent):
    global not_tree
    visited[v] = 1
    for v2 in edges[v]:
        if v2 == parent:
            continue
        if visited[v2]:
            not_tree = 1
            continue
        dfs(v2, v)


ans = 0
visited = [0]*n
for i in range(n):
    if visited[i]:
        continue
    not_tree = 0
    dfs(i, -1)
    ans += 1-not_tree
print(ans)


# # DFSで閉路探索をするのを、探索してないノードがなくなるまで繰り返すコード
# # 閉路があったら木でないと言う特性を利用している
# n, m = map(int, input().split())
# GRAPH = [[0]*n for _ in range(n)]
# for _ in range(m):
#     v1, v2 = list(map(lambda x: int(x)-1, input().split()))
#     GRAPH[v1][v2] = GRAPH[v2][v1] = 1

# # print(GRAPH)


# # 連結成分を列挙する
# visited = [0]*n


# def dfs(v, parent):
#     global closed_circuit
#     if visited[v]:
#         return 0
#     visited[v] = 1
#     for v2 in range(n):
#         if not GRAPH[v][v2]:
#             continue
#         if v2 != parent and visited[v2]:
#             closed_circuit = 1
#             continue
#         dfs(v2, v)


# cnt = 0
# closed_circuit_cnt = 0
# while 0 in visited:
#     cnt += 1
#     closed_circuit = 0
#     nxt = visited.index(0)
#     dfs(nxt, -1)
#     closed_circuit_cnt += closed_circuit


# # print(closed_circuit_cnt, cnt, visited)

# print(cnt - closed_circuit_cnt)


# 最初に実装したUFを模したコード
# 木の条件がエッジの数−１==ノードの数であることを利用している
# from collections import defaultdict, Counter
# # nは100
# n, m = map(int, input().split())

# ls = [-1]*(n+1)
# max_group_num = 1
# dd = defaultdict(int)
# for _ in range(m):
#     v1, v2 = map(int, input().split())
#     x, y = ls[v1], ls[v2]
#     if x == -1 and y == -1:
#         ls[v1] = ls[v2] = max_group_num
#         dd[max_group_num] += 1
#         max_group_num += 1
#     elif x == -1 or y == -1:
#         if x < y:
#             x, y = y, x
#         ls[v1] = ls[v2] = x
#         dd[x] += 1
#     else:
#         if x > y:
#             x, y = y, x
#         ls[v1] = ls[v2] = x
#         dd[x] += 1
#         dd[y] = 0
#         for i in range(1, n+1):
#             if ls[i] == y:
#                 ls[i] = x
#                 dd[x] += 1

#     # ls.append((1, {v1, v2}))

# # nodeの数
# c = Counter(ls[1:])
# # print(c)
# # # edgeの数
# # print(dd)

# ans = 0
# for k, n_nodes in c.items():
#     # if k < 0:
#     #     continue
#     if k == -1:
#         ans += n_nodes
#         continue
#     n_edges = dd[k]
#     if n_edges+1 == n_nodes:
#         ans += 1
# print(ans)

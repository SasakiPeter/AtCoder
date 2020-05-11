# 結構驚きだが、pythonでも間に合う
import heapq
n, m, s, t = map(int, input().split())
edges_yen = [[]for _ in range(n)]
edges_snuuk = [[]for _ in range(n)]
for _ in range(m):
    u, v, a, b = map(int, input().split())
    edges_yen[u-1].append((a, v-1))
    edges_yen[v-1].append((a, u-1))
    edges_snuuk[u-1].append((b, v-1))
    edges_snuuk[v-1].append((b, u-1))


def dijkstra(init_v, edges):
    next_v = [(0, init_v)]
    INF = 10**18
    dist = [INF]*n
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


dist_yen = dijkstra(s-1, edges_yen)
dist_snuuk = dijkstra(t-1, edges_snuuk)
# print(dist_yen, dist_yen[t-1])
# print(dist_snuuk, dist_snuuk[t-1])

# ans = []
# INF = 10**18
# min_c = INF
# for x, y in zip(dist_yen[::-1], dist_snuuk[::-1]):
#     if x+y < min_c:
#         min_c = x+y
#     ans.append(10**15-min_c)
# print(*ans[::-1], sep='\n')

# iで両替したときの、最小コスト
dist = [x+y for x, y in zip(dist_yen, dist_snuuk)]
# print(dist)
ans = []
INF = 10**18
MIN = INF
for x in dist[::-1]:
    if x < MIN:
        MIN = x
    ans.append(MIN)
for x in ans[::-1]:
    print(10**15-x)


# 全ての状態でdijkstraするとN**2になっちゃう
# import heapq
# n, m, s, t = map(int, input().split())


# def to_v(i, j):
#     return 2*i+j


# # 0,1
# N = 2*n
# edges = [[]for _ in range(N)]

# # 辺をはる
# for _ in range(m):
#     u, v, a, b = map(int, input().split())
#     # u0→v0に円の辺を生やす
#     # u1→v1にsnuukの辺を生やす
#     u -= 1
#     v -= 1
#     edges[to_v(u, 0)].append((a, to_v(v, 0)))
#     edges[to_v(v, 0)].append((a, to_v(u, 0)))
#     edges[to_v(u, 1)].append((b, to_v(v, 1)))
#     edges[to_v(v, 1)].append((b, to_v(u, 1)))

# # snuukに変換する距離0の辺を追加
# # 注意！！　円→snuukはいいが、逆はできない
# for u in range(n):
#     edges[to_v(u, 0)].append((0, to_v(u, 1)))
#     # edges[to_v(u, 1)].append((0, to_v(u, 0)))


# def dijkstra(init_v):
#     next_v = [(0, init_v)]
#     INF = 10**18
#     dist = [INF]*N
#     dist[init_v] = 0
#     # prev = [-1]*N
#     while next_v:
#         d, v = heapq.heappop(next_v)
#         if dist[v] < d:
#             continue
#         for d, v2 in edges[v]:
#             if dist[v2] <= dist[v]+d:
#                 continue
#             dist[v2] = dist[v]+d
#             # prev[v2] = v
#             heapq.heappush(next_v, (dist[v2], v2))
#     # print(prev)
#     return dist

# # 辺を取り除くのどうする？


# for i in range(n):
#     # 年を経るにしたがって、i番目の両替路が閉鎖
#     if i != 0:
#         i -= 1
#         edges[to_v(i, 0)].pop()
#         # edges[to_v(i, 1)].pop()
#     # print(edges)
#     dist = dijkstra(to_v(s-1, 0))
#     print(10**15-dist[to_v(t-1, 1)])

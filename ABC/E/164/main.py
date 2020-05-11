import heapq
n, m, s = map(int, input().split())
s = min(s, 2499)
UV = [[] for _ in range(n)]
for i in range(m):
    u, v, a, b = map(int, input().split())
    u -= 1
    v -= 1
    UV[u].append((v, a, b))
    UV[v].append((u, a, b))

# C_income = []
# D_dist = []
# for _ in range(n):
#     c, d = map(int, input().split())
#     C_income.append(c)
#     D_dist.append(d)

CD = [tuple(map(int, input().split()))for _ in range(n)]

# ここから、新しいグラフを作成する
MAXS = 2500
NV = MAXS*n
edges = [[] for _ in range(NV)]


def to_v(i, j):
    return MAXS*i+j


# まず、交換所の辺を生やす
# for i in range(n):
#     # 頂点iのレート
#     c = C_income[i]
#     d = D_dist[i]
for i, (c, d) in enumerate(CD):
    # dの有向な辺を生やす
    for j in range(MAXS-c):
        edges[to_v(i, j)].append((d, to_v(i, j)+c))

# 次に、頂点間の辺を生やす
for i in range(n):
    for i2, a, b in UV[i]:
        # i~jに距離bの辺を生やす
        # v = i*2500+x(0~2499)
        # v2 = j*2500+x-a
        for j in range(MAXS-a):
            edges[to_v(i, a+j)].append((b, to_v(i2, j)))


# 頂点と辺を増やしてdijkstraすればいい
# 頂点は、その時持っている銀貨の枚数分だけ増やす
# 最大で2500枚持っている頂点が存在すれば、全てのノードに
# 最短経路で行けるので、v<=2500になるので、十分高速な
# dijkstraが組める


def dijkstra(init_v):
    next_v = [(0, init_v)]
    INF = 10**18
    dist = [INF]*NV
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


INF = 10**18
dist = dijkstra(s)
for i in range(1, n):
    # 0が最小とは限らない
    ans = INF
    for j in range(MAXS):
        ans = min(ans, dist[to_v(i, j)])
    print(ans)

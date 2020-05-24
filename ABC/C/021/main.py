from collections import deque
MOD = 10**9+7
n = int(input())
a, b = map(lambda x: int(x)-1, input().split())
m = int(input())
edges = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(lambda x: int(x)-1, input().split())
    edges[x].append(y)
    edges[y].append(x)


def bfs(init_v):
    next_v = deque([init_v])
    INF = 10**18
    dist = [INF]*n
    dist[init_v] = 0
    routes = [0]*n
    routes[init_v] = 1
    while next_v:
        v = next_v.popleft()
        for v2 in edges[v]:
            if dist[v2] == dist[v]+1:
                # print(v+1, v2+1)
                routes[v2] += routes[v]
                routes[v2] %= MOD
            if dist[v2] <= dist[v]+1:
                continue
            dist[v2] = dist[v]+1
            # print(v+1, v2+1)
            routes[v2] += routes[v]
            routes[v2] %= MOD
            next_v.append(v2)
    return dist, routes


dist, routes = bfs(a)
# print(dist, b)
print(routes[b] % MOD)

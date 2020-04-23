import heapq
import sys
input = sys.stdin.readline
INF = float('inf')
n, m, k = map(int, input().split())
t = [0]+[int(input()) for _ in range(n-2)]+[0]
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append((c, b, d))
    edges[b].append((c, a, d))

dist = [INF]*n
dist[0] = 0
next_nodes = [(0, 0)]
while next_nodes:
    # print(next_nodes)
    cost_v, v = heapq.heappop(next_nodes)
    if dist[v] < cost_v:
        continue
    for cost_v2, v2, dv2 in edges[v]:
        if dist[v2] <= -(-(dist[v]+t[v])//dv2)*dv2+cost_v2:
            continue
        dist[v2] = -(-(dist[v]+t[v])//dv2)*dv2+cost_v2
        heapq.heappush(next_nodes, (dist[v2], v2))
# print(dist)

ans = dist[-1]
print(ans if ans <= k else -1)

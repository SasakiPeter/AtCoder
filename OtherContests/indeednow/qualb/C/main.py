import heapq
n = int(input())
edges = [[]for _ in range(n)]
for _ in range(n-1):
    a, b = list(map(lambda x: int(x)-1, input().split()))
    edges[a].append(b)
    edges[b].append(a)

next_v = [0]
ans = []
visited = [0]*n
while next_v:
    v = heapq.heappop(next_v)
    visited[v] = 1
    ans.append(v+1)
    for v2 in edges[v]:
        if visited[v2]:
            continue
        heapq.heappush(next_v, v2)
print(*ans)

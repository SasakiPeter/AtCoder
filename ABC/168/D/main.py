from collections import deque

n, m = map(int, input().split())
edges = [[]for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    edges[a].append(b)
    edges[b].append(a)

next_v = deque([0])
history = [-1]*n
INF = 10**18
dist = [INF]*n
dist[0] = 0
while next_v:
    v = next_v.popleft()

    for v2 in edges[v]:
        if dist[v2] <= dist[v]+1:
            continue
        dist[v2] = dist[v]+1
        history[v2] = v
        next_v.append(v2)

# print(dist)
# print(history)

print('Yes')
for x in history[1:]:
    print(x+1)

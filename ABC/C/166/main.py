n, m = map(int, input().split())
h = list(map(int, input().split()))
edges = [[]for _ in range(n)]
for _ in range(m):
    a, b = list(map(lambda x: int(x)-1, input().split()))
    edges[a].append(b)
    edges[b].append(a)

ans = 0
for v in range(n):
    for v2 in edges[v]:
        if h[v] <= h[v2]:
            break
    else:
        ans += 1
print(ans)

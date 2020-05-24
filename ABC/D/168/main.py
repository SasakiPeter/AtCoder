from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
edges = [[]for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    edges[a].append(b)
    edges[b].append(a)

next_v = deque([0])
prev = [-1]*n
while next_v:
    v = next_v.popleft()
    for v2 in edges[v]:
        if prev[v2] != -1:
            continue
        prev[v2] = v+1
        next_v.append(v2)
print('Yes')
for x in prev[1:]:
    print(x)

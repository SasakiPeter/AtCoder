import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n, m = map(int, input().split())
H = list(map(int, input().split()))
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = list(map(lambda x: int(x)-1, input().split()))
    edges[a].append(b)
    edges[b].append(a)


ans = [0]*n


def dfs(v, parent):
    if visited[v]:
        return 0
    visited[v] = 1
    # hight = H[v]
    if not edges[v]:
        ans[v] = 1
    elif all(H[v2] < H[v] for v2 in edges[v]):
        ans[v] = 1
    for v2 in edges[v]:
        # print(v, v2, H[v], H[v2])
        # if H[v] <= H[v2]:
        #     break
        if v2 == parent:
            continue
        dfs(v2, v)
    # else:
    #     ans[v] = 1


visited = [0]*n

for v in range(n):
    if visited[v]:
        continue
    dfs(v, -1)
    # print(visited)
    # print(ans)

print(sum(ans))

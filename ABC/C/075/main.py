n, m = map(int, input().split())
# edges = sorted(sorted(map(int, input().split())) for _ in range(m))
# GRAPH = sorted(sorted(map(lambda x: int(x)-1, input().split()))
#                for _ in range(m))


# 連結判定には、DFS、BFS、Union find、ワーシャルフロイド法などがある

# DFS
# LIMIT = 50
GRAPH = [[0]*n for _ in range(n)]
# VISITED = [False]*LIMIT
EDGES = []

for _ in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    GRAPH[a][b] = GRAPH[b][a] = 1
    EDGES.append((a, b))


def make_dfs():
    visited = [0]*n

    def inner(v):
        visited[v] = 1
        for v2 in range(n):
            if not GRAPH[v][v2]:
                continue
            if visited[v2]:
                continue
            inner(v2)
        return visited
    return inner


ans = 0
# 全探索で、辺を削除していく
for a, b in EDGES:
    GRAPH[a][b] = GRAPH[b][a] = 0
    dfs = make_dfs()
    if sum(dfs(0)) != n:
        ans += 1
    GRAPH[a][b] = GRAPH[b][a] = 1

print(ans)


# VISITED = [0]*n
# def dfs(v):
#     VISITED[v] = 1
#     for v2 in range(n):
#         if not GRAPH[v][v2]:
#             continue
#         if VISITED[v2]:
#             continue
#         dfs(v2)

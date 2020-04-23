# import numpy as np
# from scipy.sparse.csgraph import shortest_path
# from scipy.sparse import csr_matrix
n, x, y = map(int, input().split())
# n, x, y = 2*10**3, 2*10**3, 2*10**3
x -= 1
y -= 1
# GRAPH = [[0]*n for _ in range(n)]
# for i in range(n-1):
#     GRAPH[i][i+1] = GRAPH[i+1][i] = 1
# GRAPH[x][y] = GRAPH[y][x] = 1

# G = csr_matrix(GRAPH)
# sp = shortest_path(G, method='FW')


def shortest_path(i, j):
    # O1で求まるはず
    # if i <= x <= y <= j:
    #     return min(j-i, x-i+j-y+1)
    # elif x <= i <= y <= j:
    #     return min(j-i, i-x+j-y+1)
    # elif x <= i <= j <= y:
    #     return min(j-i, i-x+y-j+1)
    # elif i <= x <= j <= y:
    #     return min(j-i, x-i+y-j+1)
    # else:
    #     return j-i
    return min(j-i, abs(x-i)+abs(y-j)+1)


# DFSでも良い

ans = [0]*(n-1)
# n個の頂点
for i in range(n):
    for j in range(i+1, n):
        # print(i, j)
        # path = int(sp[i][j])-1
        path = shortest_path(i, j)-1
        # print(path, i, j)
        ans[path] += 1
print(*ans, sep="\n")

# shortest_path = [[0]*n for _ in range(n)]

# INF = 10**5
# visited = [0]*n
# shortest_path = [INF]*n


# def dfs(v, cnt):
#     # i番目の頂点から入る
#     # print(i)
#     # visited[v] = 1
#     shortest_path[v] = min(cnt, shortest_path[v])
#     for v2 in range(n):
#         if not GRAPH[v][v2]:
#             continue
#         # if visited[v2]:
#         #     continue
#         print(v, v2, cnt)
#         dfs(v2, cnt+1)


# print(dfs(0, 0))
# print(shortest_path)

# # 0からxまでの最短経路
# start = 0
# for i in range(n):
#   if i == start:
#     continue
#   if not GRAPH[start][i]:
#     continue

from collections import defaultdict
n, x, y = map(int, input().split())
x -= 1
y -= 1
dd = defaultdict(int)
for i in range(n-1):
    for j in range(i+1, n):
        sp = min(j-i, abs(i-x)+abs(j-y)+1)
        dd[sp] += 1
for i in range(1, n):
    print(dd[i])


# # pypyなら通る
# from collections import deque, defaultdict
# n, x, y = map(int, input().split())
# x -= 1
# y -= 1
# edges = [[] for _ in range(n)]
# edges[x].append(y)
# edges[y].append(x)
# for i in range(n-1):
#     edges[i].append(i+1)
#     edges[i+1].append(i)


# def bfs(init_v):
#     queue = deque([init_v])
#     INF = 10**10
#     dist = [INF]*n
#     dist[init_v] = 0
#     while queue:
#         v = queue.popleft()
#         for v2 in edges[v]:
#             if dist[v2] <= dist[v]+1:
#                 continue
#             dist[v2] = dist[v]+1
#             queue.append(v2)
#     return dist


# dd = defaultdict(int)
# for i in range(n):
#     sp = bfs(i)
#     for x in sp:
#         dd[x] += 1

# for i in range(1, n):
#     print(dd[i]//2)

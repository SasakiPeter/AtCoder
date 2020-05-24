# 中継地を全探索するが、出発するのは３隅から
# そうすれば３回だけのBFSで十分
from collections import deque
h, w = map(int, input().split())
INF = 10**18
MAP = [[INF]*(w+2)]
for _ in range(h):
    A = [INF]
    A.extend(list(map(int, input().split())))
    A.append(INF)
    MAP.append(A)
else:
    MAP.append([INF]*(w+2))


def bfs(init_v):
    next_v = deque([init_v])
    dist = [[INF]*(w+2)for _ in range(h+2)]
    i, j = init_v
    dist[i][j] = 0
    while next_v:
        i, j = next_v.popleft()
        dirc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for di, dj in dirc:
            x, y = i+di, j+dj
            if dist[x][y] <= dist[i][j]+MAP[x][y]:
                continue
            dist[x][y] = dist[i][j]+MAP[x][y]
            next_v.append((x, y))
    return dist


dist_LD = bfs((h, 1))
dist_RD = bfs((h, w))
dist_RU = bfs((1, w))

ans = INF
for i in range(1, h+1):
    for j in range(1, w+1):
        tmp = dist_LD[i][j]+dist_RD[i][j]+dist_RU[i][j]-2*MAP[i][j]
        if tmp < ans:
            ans = tmp
print(ans)


# # 経路復元してあげて、重なったところまでのコストで
# # 計算する
# from collections import deque
# h, w = map(int, input().split())
# # INFパディングする
# INF = 10**18
# MAP = [[INF]*(w+2)]
# for _ in range(h):
#     A = list(map(int, input().split()))
#     MAP.append([INF]+A+[INF])
# else:
#     MAP.append([INF]*(w+2))


# def bfs(init_v):
#     dist = [[INF]*(w+2)for _ in range(h+2)]
#     prev = [[0]*(w+2)for _ in range(h+2)]
#     i, j = init_v
#     next_v = deque([init_v])
#     dist[i][j] = MAP[i][j]
#     while next_v:
#         i, j = next_v.popleft()
#         dirc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#         for di, dj in dirc:
#             x, y = i+di, j+dj
#             if dist[x][y] <= dist[i][j]+MAP[x][y]:
#                 continue
#             dist[x][y] = dist[i][j]+MAP[x][y]
#             prev[x][y] = (i, j)
#             next_v.append((x, y))
#     return dist, prev


# dist, prev = bfs((h, 1))
# track = [[0]*(w+2)for _ in range(h+2)]
# track[1][w] = 1
# x = prev[1][w]
# while x != 0:
#     i, j = x
#     track[i][j] = 1
#     x = prev[i][j]

# ans = dist[1][w]
# tmp = INF
# for i in range(1, h+1):
#     for j in range(1, w+1):
#         if track[i][j] == 0:
#             continue
#         dist, prev = bfs((i, j))
#         d = dist[h][w]-MAP[i][j]
#         if d < tmp:
#             tmp = d

# # ans = 0
# # for i in range(1, h+1):
# #     for j in range(1, w+1):
# #         if track[i][j]:
# #             ans += MAP[i][j]
# print(ans+tmp)

# # 中継地を全探索する
# # 中継地から、スタートと２つのゴールへの最短コストを求めて
# # それを合計する
# # import heapq
# h, w = map(int, input().split())
# # INFパディングする
# INF = 10**18
# MAP = [[INF]*(w+2)]
# for _ in range(h):
#     A = list(map(int, input().split()))
#     MAP.append([INF]+A+[INF])
# else:
#     MAP.append([INF]*(w+2))


# def dijkstra(init_v):
#     dist = [[INF]*(w+2)for _ in range(h+2)]
#     i, j = init_v
#     next_v = [(MAP[i][j], init_v)]
#     dist[i][j] = MAP[i][j]
#     while next_v:
#         cost, (i, j) = heapq.heappop(next_v)
#         if dist[i][j] < cost:
#             continue
#         dirc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#         for di, dj in dirc:
#             x, y = i+di, j+dj
#             if dist[x][y] <= dist[i][j]+MAP[x][y]:
#                 continue
#             dist[x][y] = dist[i][j]+MAP[x][y]
#             heapq.heappush(next_v, (dist[x][y], (x, y)))
#     return dist

# def bfs(init_v):
#     dist = [[INF]*(w+2)for _ in range(h+2)]
#     i, j = init_v
#     next_v = deque([init_v])
#     dist[i][j] = MAP[i][j]
#     while next_v:
#         i, j = next_v.popleft()
#         dirc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#         for di, dj in dirc:
#             x, y = i+di, j+dj
#             if dist[x][y] <= dist[i][j]+MAP[x][y]:
#                 continue
#             dist[x][y] = dist[i][j]+MAP[x][y]
#             next_v.append((x, y))
#     return dist


# ans = INF
# for i in range(1, h+1):
#     for j in range(1, w+1):
#         dist, prev = bfs((i, j))
#         x = dist[h][1]+dist[1][w]+dist[h][w]-MAP[i][j]*2
#         if x < ans:
#             if x == 246:
#                 # for row in dist:
#                 #     print(row[1:-1])

#                 # i,jまでtrack
#                 track = [[0]*(w+2)for _ in range(h+2)]
#                 track[i][j] = 1
#                 x = prev[1][w]
#                 while x != (i, j):
#                     a, b = x
#                     track[a][b] = 1
#                     x = prev[a][b]

#                 x = prev[h][1]
#                 while x != (i, j):
#                     a, b = x
#                     track[a][b] = 1
#                     x = prev[a][b]

#                 x = prev[h][w]
#                 while x != (i, j):
#                     a, b = x
#                     track[a][b] = 1
#                     x = prev[a][b]

#                 for row in track:
#                     print(row)

#             ans = x
# print(ans)

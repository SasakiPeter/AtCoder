from collections import deque
h, w = map(int, input().split())
start = tuple(map(lambda x: int(x)-1, input().split()))
goal = tuple(map(lambda x: int(x)-1, input().split()))
maze = [input()for _ in range(h)]

INF = 10**18
dist = [[INF]*w for _ in range(h)]
i, j = start
dist[i][j] = 0

next_v = deque([start])
# next_v = [start]
# O(h*w+h*w*4)
# O(V+E)
# O(VlogE)
while next_v:
    i, j = next_v.popleft()
    # i, j = next_v.pop()
    dirc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for di, dj in dirc:
        x, y = i+di, j+dj
        if maze[x][y] == '#':
            continue
        if dist[x][y] <= dist[i][j]+1:
            continue
        dist[x][y] = dist[i][j]+1
        next_v.append((x, y))
i, j = goal
print(dist[i][j])


# for row in dist:
#     print(row)


# r, c = map(int, input().split())
# start = list(map(lambda x: int(x)-1, input().split()))
# goal = list(map(lambda x: int(x)-1, input().split()))
# maze = [list(input()) for _ in range(r)]

# # 最短経路を記録していくパターン
# INF = 10**5
# q = [start]
# routes = [[INF]*c for _ in range(r)]
# routes[start[0]][start[1]] = 0

# cnt = 0
# while q:
#     cnt += 1
#     next_q = []
#     for i, j in q:
#         for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
#             a, b = i+x, j+y
#             if maze[a][b] != '.':
#                 continue
#             if routes[a][b] != INF:
#                 continue
#             routes[a][b] = cnt
#             next_q.append((a, b))
#     q = next_q

# i, j = goal
# print(routes[i][j])

# マスを記録していくパターン
# routes = [[], [start]]
# while goal not in routes[-1]:
#     ls = []
#     for grid in routes[-1]:
#         # gridから次にいける可能性のあるマスを探す
#         # その中で、まだ探索していない場所を追加する
#         i, j = grid
#         for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
#             # 戻ってこないように、通ってきた経路は記録しておく
#             if maze[i+x][j+y] == '.' and ([i+x, j+y] not in routes[-2]+ls):
#                 # if [i+x, j+y] not in ls:
#                 ls.append([i+x, j+y])
#     routes.append(ls)
# print(len(routes)-2)

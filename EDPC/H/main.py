# 記述量がちょっと多いけど、こっちの方が遷移数が少ないので早い
h, w = map(lambda x: int(x)+2, input().split())
MOD = 10**9+7
MAZE = ['#'*w]
for _ in range(h-2):
    MAZE.append('#'+input()+'#')
else:
    MAZE.append('#'*w)

route = [[0]*w for _ in range(h)]
for j in range(1, w):
    if MAZE[1][j] == '.':
        route[1][j] = 1
        continue
    break
for i in range(1, h):
    if MAZE[i][1] == '.':
        route[i][1] = 1
        continue
    break

for i in range(1, h-1):
    for j in range(1, w-1):
        x = i+1
        y = j+1
        if MAZE[x][y] == '#':
            continue
        route[x][y] = route[x-1][y]+route[x][y-1]
# for row in route:
#     print(row)
print(route[-2][-2] % MOD)


# # 実はもうちょっと簡単にかける
# h, w = map(lambda x: int(x)+2, input().split())
# MOD = 10**9+7
# MAZE = ['#'*w]
# for _ in range(h-2):
#     MAZE.append('#'+input()+'#')
# else:
#     MAZE.append('#'*w)

# route = [[0]*w for _ in range(h)]
# route[1][1] = 1
# for i in range(1, h-1):
#     for j in range(1, w-1):
#         for x, y in [(i+1, j), (i, j+1)]:
#             if MAZE[x][y] == '#':
#                 continue
#             route[x][y] += route[i][j]
#             # route[x][y] %= MOD
# # for row in route:
# #     print(row)
# print(route[-2][-2] % MOD)

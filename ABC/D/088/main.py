from collections import deque
h, w = map(int, input().split())
maze = ["#"*(w+2)]
white_cnt = 0
for _ in range(h):
    row = input()
    white_cnt += row.count('.')
    maze.append("#"+row+"#")
else:
    maze.append("#"*(w+2))

# 最小でゴールまで行った数を、初期の白の数から引いたものが答え
w += 2
h += 2
INF = 10**9
dist = [[INF]*w for _ in range(h)]
dist[1][1] = 0
next_block = deque([(1, 1)])
dirc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 0
while next_block:
    i, j = next_block.popleft()
    for x, y in dirc:
        if maze[i+x][j+y] == '#':
            continue
        if dist[i+x][j+y] <= dist[i][j]+1:
            continue
        dist[i+x][j+y] = dist[i][j]+1
        next_block.append((i+x, j+y))

        # これは変　あってるんだけど、普通こう書かない
        # if dist[i+x][j+y] != INF:
        #     continue
        # next_block.append((i+x, j+y))
        # dist[i+x][j+y] = min(dist[i+x+v][j+y+w] for v, w in dirc)+1


if dist[-2][-2] == INF:
    print(-1)
else:
    print(white_cnt-dist[-2][-2]-1)

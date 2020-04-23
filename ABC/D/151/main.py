# from queue import Queue
# Queueよりdequeの方が圧倒的に早い
from collections import deque

# h, w = 20, 20
# MAZE = ['#'*(w+2)]
# for _ in range(h):
#     MAZE.append("#"+"."*(w)+"#")
# else:
#     MAZE.append('#'*(w+2))
h, w = map(int, input().split())
MAZE = ['#'*(w+2)]
for _ in range(h):
    MAZE.append("#"+input()+"#")
else:
    MAZE.append('#'*(w+2))

INF = 10**3
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs(init_x, init_y):
    dist = [[INF]*(w+2) for _ in range(h+2)]
    # resisterd = [[0]*(w+2) for _ in range(h+2)]
    # q = Queue()
    # q.put((init_x, init_y))
    q = deque([(init_x, init_y)])
    dist[init_x][init_y] = 0
    MAX = 0
    # while not q.empty():
    while q:
        # x, y = q.get()
        x, y = q.popleft()
        for i, j in directions:
            if MAZE[x+i][y+j] == '#':
                continue
            # これだと重複しまくっちゃう
            # if dist[x+i][y+j] != INF:
            #     continue

            # 予約したやつを再記録しないようにする
            # if resisterd[x+i][y+j]:
            #     continue
            # resisterd[x+i][y+j] = 1

            # print(x+i, y+j, x, y)
            if dist[x+i][y+j] <= dist[x][y]+1:
                continue
            dist[x+i][y+j] = dist[x][y]+1
            # q.put((x+i, y+j))
            q.append((x+i, y+j))

        # ここで更新を行うのは効率が悪い
        # dist[x][y] = min(dist[x][y], min(dist[x+v][y+w]+1 for v, w in directions))
        MAX = max(MAX, dist[x][y])
    return MAX


ans = 0
for i in range(1, h+1):
    for j in range(1, w+1):
        if MAZE[i][j] == '#':
            continue
        ans = max(ans, bfs(i, j))
        # dp = bfs(i, j)
        # ans = max(
        #     ans,  max(max([x for x in row if x < INF]+[0]) for row in dp))
print(ans)


# start = time.time()
# bfs(1, 1)
# end = time.time() - start
# print(end*10**3, 'ms')

# bfsは来た道は戻らない
# def bfs(pos):
#     x, y = pos
#     # 次に探索するのは、通ることができて
#     # かつ、まだ未踏の地で、
#     # かつ、他に
#     # can_go = []
#     for i, j in directions:
#         if MAZE[x+i][y+j] == '.':
#             if dp[x+i][y+j] != INF:
#                 continue
#             dp[x+i][y+j] = min(dp[x+i+v][y+j+w]+1 for v, w in directions)
#             # can_go.append((x+i, y+j))
#             # ここが全然BFSじゃない
#             # ここで再帰するとDFSになっちゃう
#     # print(*dp, sep='\n')
#     # 次に探索するのは、dpの中でINFを除いた最大値を持つセル
#     next_idx = []
#     MAX = max(max([x for x in row if x < INF]+[0]) for row in dp)
#     for i in range(1, h+1):
#         for j in range(1, w+1):
#             if dp[i][j] == MAX:
#                 next_idx.append((i, j))

#     for x, y in next_idx:
#         bfs((x, y))


# dp[1][1] = 0
# bfs(start_idx)
# for row in dp:
#     print(row)

# cnt = defaultdict(int)
# ans = 0
# for i in range(1, h+1):
#     for j in range(1, w+1):
#         if MAZE[i][j] == '#':
#             continue
#         start_idx = (i, j)
#         dp = [[INF]*(w+2) for _ in range(h+2)]
#         dp[i][j] = 0
#         bfs(start_idx)
#         print(*dp, sep='\n')
#         break
#         ans = max(ans, max(max([x for x in row if x < INF]+[0]) for row in dp))
#     break
# print(ans)

# numpy使わないと辛そうです><
import sys
input = sys.stdin.readline
h, w = map(lambda x: int(x)+2, input().split())
MAZE = ['#'*w]
for _ in range(h-2):
    MAZE.append('#'+input()+'#')
else:
    MAZE.append('#'*w)

L = [[0]*w for _ in range(h)]
R = [[0]*w for _ in range(h)]
U = [[0]*w for _ in range(h)]
D = [[0]*w for _ in range(h)]

LAMP = [[0]*w for _ in range(h)]

for i in range(1, h-1):
    for j in range(1, w-1):
        if MAZE[i][j] == '.':
            L[i][j+1] = L[i][j]+1
            U[i+1][j] = U[i][j]+1
        if MAZE[i][w-j] == '.':
            R[i][w-j-1] = R[i][w-j]+1
        if MAZE[h-i][j] == '.':
            D[h-i-1][j] = D[h-i][j]+1

ans = 0
for i in range(1, h-1):
    for j in range(1, w-1):
        if MAZE[i][j] == '#':
            continue
        LAMP[i][j] = L[i][j]+R[i][j]+U[i][j]+D[i][j]+1
        ans = max(ans, LAMP[i][j])

print(ans)


# for i in range(1, h-1):
#     for j in reversed(range(1, w-1)):
#         if MAZE[i][j] == '#':
#             continue
#         R[i][j-1] = R[i][j]+1


# for j in range(1, w-1):
#     for i in reversed(range(1, h-1)):
#         if MAZE[i][j] == '#':
#             continue
#         D[i-1][j] = D[i][j]+1


# for j in range(1, w-1):
#     for i in range(1, h-1):
#         if MAZE[i][j] == '.':
#             U[i+1][j] = U[i][j]+1
#         if MAZE[h-i][j] == '.':
#             D[h-i-1][j] = D[h-i][j]+1

#!/usr/bin/env python3
n, m = map(int, input().split())
BOARD = [list(map(int, list(input())))for _ in range(n)]
dirc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ans = [[0]*m for _ in range(n)]
INF = float('inf')
for i in range(1, n-1):
    for j in range(1, m-1):
        MIN = INF
        for x, y in dirc:
            MIN = min(MIN, BOARD[i+x][j+y])
        # ans[i][j] = max(ans[i][j], MIN)
        if MIN == 0:
            continue
        ans[i][j] = MIN
for row in ans:
    print(*row, sep='')

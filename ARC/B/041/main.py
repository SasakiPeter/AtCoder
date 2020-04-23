n, m = map(int, input().split())
BOARD = [list(map(int, list(input())))for _ in range(n)]
ans = [[0]*m for _ in range(n)]
for i in range(n-2):
    for j in range(1, m-1):
        x = BOARD[i][j]
        ans[i+1][j] = x
        BOARD[i+1][j+1] -= x
        BOARD[i+1][j-1] -= x
        BOARD[i+2][j] -= x

for row in ans:
    print(*row, sep='')

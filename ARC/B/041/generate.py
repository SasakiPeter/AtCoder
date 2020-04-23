#!/usr/bin/env python3
import random
n = random.randint(3, 10)
m = random.randint(3, 10)
print(n, m)

# いや、ランダムだと、いつになってもテスト生成できない


def solver(n, m, out_matrix):
    BOARD = []
    for row in out_matrix:
        BOARD.append(list(map(int, list(row))))
    ans = [[0]*m for _ in range(n)]
    for i in range(n-2):
        for j in range(1, m-1):
            x = BOARD[i][j]
            ans[i+1][j] = x
            BOARD[i+1][j+1] -= x
            BOARD[i+1][j-1] -= x
            BOARD[i+2][j] -= x
    is_solvable = True
    for row in ans:
        if any(x < 0 for x in row):
            is_solvable = False
            break
    return is_solvable


is_solvable = False
while not is_solvable:
    out_matrix = []
    for i in range(n):
        out = []
        for j in range(m):
            if j == 0 or j == m-1:
                out.append(0)
            else:
                out.append(random.randint(0, 9))

        if i == 0 or i == n-1:
            out[0] = 0
            out[n-1] = 0
        out_matrix.append(''.join(map(str, out)))
    is_solvable = solver(n, m, out_matrix)
else:
    for row in out_matrix:
        print(row)

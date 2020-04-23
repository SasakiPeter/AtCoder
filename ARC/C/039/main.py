# dancing linksを使う問題

k = int(input())
s = input()
CENTER = 10**3
GRID = [[0]*(2*CENTER+1)for _ in range(2*CENTER+1)]

init_pos = (CENTER, CENTER)
dirc = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
x, y = init_pos
GRID[x][y] = 1
for c in s:
    i, j = dirc[c]
    # print(x, y, i, j, c)
    while True:
        x += i
        y += j
        if not GRID[x][y]:
            GRID[x][y] = 1
            break
# for row in GRID:
#     print(row)
# print(x, y)
print(y-CENTER, CENTER-x)

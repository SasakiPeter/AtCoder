n = int(input())
MAP = [list(input())for _ in range(n)]

for i in reversed(range(n-1)):
    for j in range(1, 2*n-2):
        if MAP[i][j] != '#':
            continue
        for di, dj in [(1, -1), (1, 0), (1, 1)]:
            x, y = i+di, j+dj
            if MAP[x][y] == 'X':
                MAP[i][j] = 'X'
                break
for row in MAP:
    print(''.join(row))

*a1, = map(int, input().split())
*a2, = map(int, input().split())
*a3, = map(int, input().split())
a = [a1, a2, a3]


n = int(input())
for _ in range(n):
    b = int(input())
    for i, row in enumerate(a):
        for j, x in enumerate(row):
            if x == b:
                a[i][j] = 0

is_bingo = False
for row in a:
    if sum(row) == 0:
        is_bingo = True

for col in zip(*a):
    if sum(col) == 0:
        is_bingo = True

if all(a[i][i] == 0 for i in range(3)):
    is_bingo = True

if a[0][2] == 0 and a[1][1] == 0 and a[2][0] == 0:
    is_bingo = True

print('Yes' if is_bingo else 'No')

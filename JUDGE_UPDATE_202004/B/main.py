n = int(input())
R = []
B = []
for _ in range(n):
    x, c = input().split()
    x = int(x)
    if c == 'R':
        R.append(x)
    else:
        B.append(x)
R.sort()
B.sort()
if R:
    print(*R, sep='\n')
if B:
    print(*B, sep='\n')

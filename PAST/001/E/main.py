n, q = map(int, input().split())
ans = [["N"]*n for _ in range(n)]

for _ in range(q):
    com, *query = map(int, input().split())
    if com == 1:
        a, b = map(lambda x: int(x)-1, query)
        ans[a][b] = 'Y'
    elif com == 2:
        a = query[0]-1
        for i in range(n):
            if ans[i][a] == 'Y':
                ans[a][i] = 'Y'
    else:
        a = query[0]-1
        x = [i for i in range(n) if ans[a][i] == 'Y']
        for i in x:
            for j in range(n):
                if a == j:
                    continue
                if ans[i][j] == 'Y':
                    ans[a][j] = 'Y'


for row in ans:
    print(*row, sep='')

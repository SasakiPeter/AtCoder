h, w = map(int, input().split())
INF = 10**5
MAP = ["."*(w+2)]
for _ in range(h):
    MAP.append("."+input()+".")
MAP.append("."*(w+2))
ROUTE = [[0]*(w+2) for _ in range(h+2)]
for i in range(2, w+1):
    ROUTE[0][i] = INF
for i in range(2, h+1):
    ROUTE[i][0] = INF

for i in range(1, h+1):
    # print(MAP[i])
    for j in range(1, w+1):
        if MAP[i][j] == ".":
            x1 = ROUTE[i][j-1]
            x2 = ROUTE[i-1][j]
        else:
            if MAP[i][j-1] == "#":
                x1 = ROUTE[i][j-1]
            else:
                x1 = ROUTE[i][j-1]+1

            if MAP[i-1][j] == "#":
                x2 = ROUTE[i-1][j]
            else:
                x2 = ROUTE[i-1][j]+1
        ROUTE[i][j] = min(x1, x2)


# print(*ROUTE, sep='\n')
print(ROUTE[h][w])

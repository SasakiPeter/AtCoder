# O(10**8)間に合うのか？→pypyなら
h, w = map(int, input().split())

board = [[0]*(w+1) for _ in range(h+1)]
for i in range(h):
    C = list(map(int, input().split()))
    for j in range(w):
        if i % 2 ^ j % 2:
            board[i+1][j+1] = C[j]
        else:
            board[i+1][j+1] = -C[j]


for i in range(1, h+1):
    for j in range(w):
        board[i][j+1] += board[i][j]

for i in range(h):
    for j in range(1, w+1):
        board[i+1][j] += board[i][j]

ans = 0
for i in range(h):
    for j in range(w):
        for i2 in range(i+1, h+1):
            for j2 in range(j+1, w+1):
                S = board[i2][j2]+board[i][j]-board[i][j2]-board[i2][j]
                if S != 0:
                    continue
                cnt = (i2-i)*(j2-j)
                if ans < cnt:
                    ans = cnt
print(ans)


# # O(10**8)間に合うのか？
# h, w = map(int, input().split())

# black = [[0]*(w+1) for _ in range(h+1)]
# white = [[0]*(w+1) for _ in range(h+1)]
# for i in range(h):
#     C = list(map(int, input().split()))
#     for j in range(w):
#         if i % 2 ^ j % 2:
#             white[i+1][j+1] = C[j]
#         else:
#             black[i+1][j+1] = C[j]


# for i in range(1, h+1):
#     for j in range(w):
#         black[i][j+1] += black[i][j]
#         white[i][j+1] += white[i][j]

# for i in range(h):
#     for j in range(1, w+1):
#         black[i+1][j] += black[i][j]
#         white[i+1][j] += white[i][j]

# for i in range(h):
#     for j in range(w):
#       for i2 in range(i,h+1):
#         for j2 in range(j,w+1):

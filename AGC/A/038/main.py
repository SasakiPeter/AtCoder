h, w, a, b = map(int, input().split())
ans = [[0]*w for _ in range(h)]

for i in range(h-b):
    for j in range(a):
        ans[i][j] = 1

for i in range(h-b, h):
    for j in range(a, w):
        ans[i][j] = 1

# for i in range(b):
#     i += h-b
#     for j in range(w-a):
#         j += a
#         ans[i][j] = 1

for row in ans:
    print(*row, sep='')

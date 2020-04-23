h, w = map(int, input().split())
n = int(input())
A = list(map(int, input().split()))

ans = [[0]*w for _ in range(h)]

# ans = [[1, 4, 4, 4, 3],
#        [2, 5, 4, 5, 3],
#        [2, 5, 5, 5, 3]]

# 条件を満たすか これはむずい
# for i in range(h):
#     for j in range(w):
#         x = ans[i][j]

# idx_ls = [(0, 0)]
idx_ls = []

flip = 0
for i in range(h):
    if not flip:
        for j in range(w):
            idx_ls.append((i, j))
    else:
        for j in range(w-1, -1, -1):
            idx_ls.append((i, j))
    flip ^= 1

# idx_ls = idx_ls[::-1]

# i = j = 0
# flip = 0
# flag = 1
# for _ in range(h*w-1):
#     # ここの条件がおかしい
#     # しょっぱなから改行が必要なパターンが実装されていない
#     if (j == w-1 or j == 0)and not flag:
#         i += 1
#         flip ^= 1
#         flag = 1
#         idx_ls.append((i, j))
#         continue
#     flag = 0
#     j = j+[1, -1][flip]
#     idx_ls.append((i, j))

# print(idx_ls)
# print(idx_ls)
# print(h, w)
# print(ans)

for color, a in enumerate(A):
    color += 1
    for _ in range(a):
        i, j = idx_ls.pop()
        ans[i][j] = color

for x in ans:
    print(*x)

*xy, w = input().split()
x, y = map(lambda x: int(x)-1, xy)
TABLE = [input() for _ in range(9)]
idx_ls = [(y, x)]
d = {"R": (0, 1), "L": (0, -1), "D": (1, 0), "U": (-1, 0)}
for _ in range(3):
    # i, j = idx_ls[-1]
    ij = idx_ls[-1]
    for k in w:
        ij = [x+coef for x, coef in zip(ij, d[k])]
    # if "R" in w:
    #     j += 1
    # if "L" in w:
    #     j -= 1
    # if "D" in w:
    #     i += 1
    # if "U" in w:
    #     i -= 1
    idx_ls.append(ij)
    # idx_ls.append((i, j))

for i, j in idx_ls:
    i, j = map(abs, (i, j))
    if 8 < i:
        i = -i % 8
    if 8 < j:
        j = -j % 8
    print(TABLE[i][j], end='')
print()


# for _ in range(3):
#     i, j = idx_ls[-1]

#     # di, dj = 1, 1
#     # if i+di < 0:
#     #     di *= -1
#     # if i+dj < 0:
#     #     dj *= -1
#     # if 8 < i+di:
#     #     di *= -1
#     # if 8 < i+dj:
#     #     dj *= -1

#     # nxt = (i+di, j+dj)

#     if "R" in w:
#         if 9 <= j+1:
#             # nxt = (i, -(j+1) % 8)
#             j = -(j+1) % 8
#         else:
#             # nxt = (i, j+1)
#             j += 1

#     if "L" in w:
#         # nxt = (i, abs(j-1))
#         j = abs(j-1)

#     if "U" in w:
#         # nxt = (abs(i-1), j)
#         i = abs(i-1)
#     if "D" in w:
#         if 9 <= i+1:
#             # nxt = (-(i+1) % 8, j)
#             i = -(i+1) % 8, j
#         else:
#             # nxt = (i+1, j)
#             i -= 1
#     nxt = (i, j)
#     # if w == "RU":
#     #     if 9 <= j+1:
#     #         nxt = (abs(i-1), -(j+1) % 8)
#     #     else:
#     #         nxt = (abs(i-1), j+1)

#     idx_ls.append(nxt)

# print(idx_ls)
# print(*(TABLE[i][j] for i, j in idx_ls), sep='')

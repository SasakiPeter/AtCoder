# 経路を追わないDFS
A, B, C = map(int, input().split())
ls = []
ans = 0


def dfs(num, a, b, c):
    global ans
    if A < a or B < b or C < c:
        return 0
    if a < b and a != A:
        return 0
    if b < c and b != B:
        return 0
    if num == 0:
        ans += 1
        return 0
    dfs(num-1, a+1, b, c)
    dfs(num-1, a, b+1, c)
    dfs(num-1, a, b, c+1)


dfs(A+B+C, 0, 0, 0)
print(ans)

# x += 1
# y += 1
# z += 1


# # 遷移を追っていくのはあまりうまい方法ではない
# def dfs(num, pos, figure):
#     i, j = pos
#     print(pos, num, figure, abc)
#     figure[i][j] = num
#     if num == sum(abc):
#         ls.append(figure)
#         return 0
#     else:

#         # if i+1 < 3 and j < abc[i+1]:
#         #     dfs(num+1, (i+1, j), figure)
#         # if j+1 < abc[i]:
#         #     # print(i, j)
#         #     dfs(num+1, (i, j+1), figure)


# dfs(1, (0, 0), [[0]*x for x in abc])
# print(ls)

# def dfs(num, a, b, c):
#     if num == x+y+z:
#         ls.append((a, b, c))
#         return 0
#     else:
#         if not a:
#             dfs(num+1, a+str(num), b, c)
#         elif not b:
#             if len(a) < x:
#                 dfs(num+1, a+str(num), b, c)
#             dfs(num+1, a, b+str(num), c)
#         elif not c:
#             if len(a) < x:
#                 dfs(num+1, a+str(num), b, c)
#             if len(b) < y:
#                 dfs(num+1, a, b+str(num), c)
#             dfs(num+1, a, b, c+str(num))
#         else:
#             #
#             if len(a) < x:
#                 if int(a[-1]) < num:
#                     dfs(num+1, a+str(num), b, c)
#             if len(b) < y:
#                 if int(b[-1]) < num:
#                     dfs(num+1, a, b+str(num), c)
#             if len(c) < z:
#                 if int(c[-1]) < num:
#                     dfs(num+1, a, b, c+str(num))

# if len(a) < x:
#     if int(a[-1]) < num:
#         dfs(num+1, a+str(num), b, c)
# if len(b) < y:
#     if int(b[-1]) < num:
#         dfs(num+1, a, b+str(num), c)
# if len(c) < z:
#     if int(c[-1]) < num:
#         dfs(num+1, a, b, c+str(num))


# dfs(1, "0", "0", "0")
# dfs(1, "", "", "")

# print(ls)
# print(len(ls))

# hook長の公式
# a, b, c = map(int, input().split())


# def fact(a):
#     if a == 1:
#         return 1
#     return a*fact(a-1)


# # hook length
# length = []
# for i in range(1, a+1):
#     x = a-i+1
#     if i <= b:
#         x += 1
#     if i <= c:
#         x += 1
#     length.append(x)

# for i in range(1, b+1):
#     x = b-i+1
#     if i <= c:
#         x += 1
#     length.append(x)

# for i in range(1, c+1):
#     x = c-i+1
#     length.append(x)

# tmp = 1
# for x in length:
#     tmp *= x

# ans = fact(a+b+c)//tmp
# print(ans)

# 割と全探索
# from itertools import permutations

# a, b, c = map(int, input().split())
# ans = 1
# SUM = a+b+c
# MAX = max([a, b, c])
# it = [i for i in range(1, SUM+1)]
# ans = 0
# for i in permutations(it):
#     i = list(i)
#     col = []
#     col.append(i[:a])
#     col.append(i[a:a+b])
#     col.append(i[a+b:])
#     # print(col)
#     is_ok = 1
#     for c in col:
#         for x, y in zip(c, c[1:]):
#             if x <= y:
#                 continue
#             is_ok = 0
#     # print(is_ok)
#     for i in range(3):
#         if len(col[i]) < MAX:
#             for _ in range(MAX-len(col[i])):
#                 col[i].append(10)

#     row = list(zip(*col))
#     for c in row:
#         for x, y in zip(c, c[1:]):
#             if x <= y:
#                 continue
#             is_ok = 0
#     # print(is_ok)
#     ans += is_ok
#     # print(col, row)
#     # break
# print(ans)

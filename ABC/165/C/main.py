# 19C10 →10**5
n, m, q = map(int, input().split())
abcd = [tuple(map(int, input().split()))for _ in range(q)]


# # 0~9で作って、あとで1たす
# def generate_a(x, s):
#     if len(s) == n:
#         yield tuple(map(lambda x: int(x)+1, list(s)))
#     else:
#         for y in range(x, m):
#             generate_a(y, s+str(y))

ls = []
# 0~9で作って、あとで1たす


def dfs(x, s):
    if len(s) == n:
        ls.append(s)
        return 0
    else:
        for y in range(x, m):
            dfs(y, s+str(y))


dfs(0, "")
ans = 0
for x in ls:
    x = tuple(map(lambda x: int(x)+1, list(x)))
    cnt = 0
    for a, b, c, d in abcd:
        a -= 1
        b -= 1
        if x[b]-x[a] == c:
            cnt += d
    if ans < cnt:
        ans = cnt
print(ans)

# from itertools import product
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)
# n, m, q = map(int, input().split())
# abcd = [tuple(map(int, input().split()))for _ in range(q)]


# ls = []


# def dfs(x, s):
#     if len(s) == n-1:
#         ls.append(s)
#         return 0
#     for y in range(x, m):
#         dfs(y, s+str(y))


# dfs(0, "")
# print(ls)

# ans = 0
# # nこの配列をそれぞれの値が1~10で作成する
# for x in product(range(1, m+1), repeat=n):
#     # 条件を満たすか判定して、得点を調べる
#     cnt = 0
#     for a, b, c, d in abcd:
#         a -= 1
#         b -= 1
#         if x[b]-x[a] == c:
#             cnt += d
#     if cnt < ans:
#         continue
#     # print(x)
#     cnt = 0
#     for a, b, c, d in abcd:
#         a -= 1
#         b -= 1
#         if x[b]-x[a] == c:
#             cnt += d
#             # print(a, b, c, d)
#     ans = cnt
# print(ans)

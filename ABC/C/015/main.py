# BFS?
# from collections import deque
n, k = map(int, input().split())
choices = [list(map(int, input().split())) for _ in range(n)]

# d = deque(choices)
# その階層で取りうる値を記録していく
dp = [set() for _ in range(n)]
dp[0] |= set(choices[0])

# while d:
for i in range(1, n):
    choice = choices[i]
    s = set()
    for x in dp[i-1]:
        for y in choice:
            s |= {x ^ y}
    dp[i] |= s
# print(dp)

print("Found" if 0 in dp[-1] else "Nothing")


# # DFS
# n, k = map(int, input().split())
# choices = [list(map(int, input().split())) for _ in range(n)]
# ans = 0


# def dfs(depth, val):
#     global ans
#     if depth == n:
#         if val == 0:
#             ans = 1
#         return 0
#     else:
#         for choice in choices[depth]:
#             if val is None:
#                 dfs(depth+1, choice)
#             else:
#                 dfs(depth+1, val ^ choice)


# dfs(0, None)
# print("Found" if ans else "Nothing")

# # 真っ先に思いつた方法
# from itertools import product
# from functools import reduce
# # こんなパッケージあったのか！？
# from operator import xor
# n, k = map(int, input().split())
# choices = [list(map(int, input().split())) for _ in range(n)]

# for i in product(*choices):
#     val = reduce(xor, i)
#     if val == 0:
#         print("Found")
#         break
# else:
#     print("Nothing")


# # 真っ先に思いつた方法
# from itertools import product
# from functools import reduce
# n, k = map(int, input().split())
# choices = [list(map(int, input().split())) for _ in range(n)]

# for i in product(*choices):
#     val = reduce(lambda x, y: x ^ y, i)
#     if val == 0:
#         print("Found")
#         break
# else:
#     print("Nothing")

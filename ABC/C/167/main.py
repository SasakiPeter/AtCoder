# 再帰
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n, m, x = map(int, input().split())
ca = [tuple(map(int, input().split()))for _ in range(n)]
INF = 10**18
ans = INF
proficiency = [0]*m


def dfs(i, cost):
    if i == n:
        global ans
        if cost < ans and all(x <= proficiency[j]for j in range(m)):
            ans = cost
        return 0
    c, *A = ca[i]
    for j in range(m):
        proficiency[j] += A[j]
    dfs(i+1, cost+c)
    for j in range(m):
        proficiency[j] -= A[j]

    dfs(i+1, cost)


dfs(0, 0)
print(ans if ans != INF else -1)

# # bit
# n, m, x = map(int, input().split())
# ca = [tuple(map(int, input().split()))for _ in range(n)]
# INF = 10**18
# ans = INF
# for bit in range(1 << n):
#     cost = 0
#     proficiency = [0]*m
#     for i in range(n):
#         if bit >> i & 1:
#             c, *A = ca[i]
#             cost += c
#             for j in range(m):
#                 proficiency[j] += A[j]
#     if cost < ans and all(x <= proficiency[j]for j in range(m)):
#         ans = cost
# print(ans if ans != INF else -1)


# # itertools
# from itertools import product
# n, m, x = map(int, input().split())
# ca = [tuple(map(int, input().split()))for _ in range(n)]
# INF = 10**18
# ans = INF
# for bit in product((0, 1), repeat=n):
#     proficiency = [0]*m
#     cost = 0
#     for i in range(n):
#         if bit[i]:
#             c, *A = ca[i]
#             cost += c
#             for j in range(m):
#                 proficiency[j] += A[j]
#     if cost < ans and all(x <= proficiency[j] for j in range(m)):
#         ans = cost
# print(ans if ans != INF else -1)

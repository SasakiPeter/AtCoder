# 全部調べられるから全部調べる
from itertools import permutations
from collections import Counter
n, c = map(int, input().split())
A = [int(input())for _ in range(n)]
even = Counter(A[::2])
odd = Counter(A[1::2])
saved = max(even[x]+odd[y]
            for x, y in permutations([i for i in range(1, 11)], 2))
print(c*(n-saved))

# # 全部調べられるから全部調べる
# from itertools import permutations
# n, c = map(int, input().split())
# A = [int(input())for _ in range(n)]
# INF = 10**18
# ans = INF
# for x in permutations([i for i in range(1, 11)], 2):
#     # print(x)
#     cost = 0
#     for i in range(n):
#         if x[i % 2] != A[i]:
#             cost += c
#     ans = min(ans, cost)
# print(ans)

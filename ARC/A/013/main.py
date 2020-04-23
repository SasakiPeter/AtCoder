# maspy iter
from itertools import permutations
N, M, L = map(int, input().split())
*PKG, = map(int, input().split())

answer = 0
for P, Q, R in permutations(PKG, 3):
    answer = max(answer, (N//P) * (M//Q) * (L//R))
print(answer)

# N, M, L = map(int, input().split())
# PKG = list(map(int, input().split()))

# answer = 0

# for i in range(3):
#     for j in range(3):
#         if i == j:
#             continue
#         k = 3 - i - j
#         P, Q, R = PKG[i], PKG[j], PKG[k]
#         if P <= N and Q <= M and R <= L:
#             x = (N//P) * (M//Q) * (L//R)
#             if answer < x:
#                 answer = x

# print(answer)

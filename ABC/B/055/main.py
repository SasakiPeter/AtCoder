import math as m
n = int(input())

# TLE
# p = 1
# for i in range(1, n+1):
#     p *= i
# print(p % (10**9+7))

# 最速
# p = 1
# for i in range(1, n+1):
#     p *= i
#     # 余剰分は、結局i倍しても徐せるからここで割っておいて問題ない
#     # そうすると、数が大きくならないから計算が早い
#     p = p % (10**9+7)
# print(p)

print(m.factorial(n) % (10**9+7))

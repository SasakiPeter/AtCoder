# k = int(input())
# d = [0]*(k+1)
# for i in range(1, k+1):
#     d[i] = pow(k//i, 3)

# for i in reversed(range(1, k+1)):
#     for j in range(2*i, k+1, i):
#         d[i] -= d[j]

# ans = 0
# for i in range(1, k+1):
#     ans += i*d[i]
# print(ans)


from math import gcd
k = int(input())
double = [gcd(i, j) for i in range(1, k+1) for j in range(1, k+1)]
triple = [gcd(i, j) for i in range(1, k+1) for j in double]
print(sum(triple))


# from itertools import product
# from functools import reduce

# ans = 0
# it = [i for i in range(1, k+1)]
# for abc in product(it, repeat=3):
#     ans += reduce(gcd, abc)
# print(ans)

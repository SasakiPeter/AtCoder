# 君はベクトルを知っているか？
import math as m
from operator import sub
*ab, c = sorted(map(int, input().split()))
r = sum(ab)+c
r2 = [abs(c - sum(ab)), 0][c < sum(ab)]
print(sub(*map(lambda r: m.pi*r**2, [r, r2])))


# if c < sum(ab):
#     print(m.pi*r**2)
# else:
#     r2 = abs(c - sum(ab))
#     print(sub(*map(lambda r: m.pi*r**2, [r, r2])))


# import math as m
# a, b, c = map(int, input().split())
# r = a+b+c
# # 三角形作れるか判定
# if c < a+b and a < b+c and b < a+c:
#     # *xy, z = sorted([a, b, c])
#     # if z < sum(xy):
#     print(m.pi*r**2)
# else:
#     r2 = min(abs(a+b-c), abs(a-b-c), abs(a-b+c))
#     # print(r, r2)
#     print(m.pi*r**2 - m.pi*r2**2)

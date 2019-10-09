# import math as m

# n = int(input())
# s = sorted(int(input()) for _ in range(n))[::-1]
# ans = 0
# for x, y in zip(s[::2], s[1::2]+[0]):
#     ans += (x**2 - y**2)*m.pi

# print(ans)

# このくらいのオーダーだと、こっちの方が早いらしい
# print((sum(x**2 for x in s[::2])-sum(y**2 for y in s[1::2]))*m.pi)


# 頭よす
import math as m
r2 = sorted(int(input())**2 for _ in range(int(input())))[::-1]
print((sum(r2[::2]) - sum(r2[1::2]))*m.pi)

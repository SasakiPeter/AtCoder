# n, m, x = map(int, input().split())
# l = list(map(int, input().split()))
# # 位置Xからみて、右と左どっちに多く料金所があるかを判定して
# # 少ない方の個数を出せばいい

# # 値がx未満のl内の数
# c = sum(1 if y < x else 0 for y in l)

# # ダサい len(l) == c だし
# # print(c if c < len(l)-c else len(l)-c)
# print(min(c, m-c))

# 926
# from bisect import bisect_left
# n, m, x = map(int, input().split())
# a = list(map(int, input().split()))
# p = bisect_left(a, x)
# print(min(m-p, p))

# もしくは
n, m, x = map(int, input().split())
*a, = map(int, input().split())
c = len([1 for y in a if y < x])
print(min(c, m-c))

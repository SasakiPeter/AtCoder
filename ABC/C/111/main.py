from collections import Counter
from itertools import product
n = int(input())
*v, = map(int, input().split())
o = Counter(v[1::2])
e = Counter(v[::2])
o[0] = 0
e[0] = 0
# こんな便利なメソッドがあったなんて。
o_ls = o.most_common(2)
e_ls = e.most_common(2)


# ここまで条件分けなくてもええねん　全部試せばがmaspy流
# if o_ls[0][0] != e_ls[0][0]:
#     ans = n - o_ls[0][1] - e_ls[0][1]
# else:
#     a = n - o_ls[0][1] - e_ls[1][1]
#     b = n - e_ls[0][1] - o_ls[1][1]
#     ans = min(a, b)

ans = n
for (k1, v1), (k2, v2) in product(o_ls, e_ls):
    if k1 == k2:
        continue
    x = n - v1 - v2
    if ans > x:
        ans = x

print(ans)


# from collections import Counter
# n = int(input())
# *v, = map(int, input().split())

# odds = v[1::2]
# evens = v[::2]
# o = Counter(odds)
# e = Counter(evens)
# omx, *ol = sorted(o.items(), reverse=True, key=lambda x: x[1])
# emx, *el = sorted(e.items(), reverse=True, key=lambda x: x[1])

# if omx[0] != emx[0]:
#     ans = n - omx[1] - emx[1]
# else:
#     if ol:
#         ol = ol[0]
#     else:
#         ol = (0, 0)

#     if el:
#         el = el[0]
#     else:
#         el = (0, 0)

#     a = n - omx[1] - el[1]
#     b = n - emx[1] - ol[1]
#     ans = min(a, b)

# print(ans)

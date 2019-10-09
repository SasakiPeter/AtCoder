# n, m = map(int, input().split())

# # 空のp*xの行列を定義して、そこに、それぞれ
# # {12:1, 32:2} みたいな情報を保持していけばいい
# d = [[] for _ in range(n + 1)]
# # print(d)
# m = [tuple(map(int, input().split())) for _ in range(m)]
# # sorted_m = sorted(m, key=lambda x: (x[0], x[1]))
# # sorted_m = {py: i for i, py in enumerate(
# #     sorted(m, key=lambda x: (x[0], x[1])))}
# # print(m)
# # print(sorted_m)

# for p, y in m:
#     d[p].append(y)
# d = [sorted(s) for s in d]
# # print(d)

# for p, y in m:
#     print('{:06}{:06}'.format(p, d[p].index(y)+1))


# データの持ち方が下手くそ

# last_p = 0
# last_y = 0
# c = 0
# for p, y in m:
#     if last_p != p:
#         c = 0
#         last_p = p
#     c += 1
#     print('{:06}{:06}'.format(p, c))
# print(str(p).zfill(6))

from bisect import bisect_left, insort_left, bisect_right
from collections import defaultdict
n, m = map(int, input().split())
# d = [[] for _ in range(n + 1)]
m = [tuple(map(int, input().split())) for _ in range(m)]

d = defaultdict(list)
# ただのsortedはいい感じに昇順にしてくれる
for p, y in sorted(m):
    # appendの代わり
    # d[p] += [y]
    d[p].append(y)

for p, y in m:
    # print('{:06}{:06}'.format(p, bisect_left(d[p], y)+1))
    print('{:06}{:06}'.format(p, bisect_right(d[p], y)))

# .index はdictに集計しておくことでO(1)で取り出せるが、
# bisectを使ってO(logn)で簡単に操作できることも知っておくべき

# bisect2回は厳しいものがある
# for p, y in m:
#     insort_left(d[p], y)

# for p, y in m:
#     # ここのindexがだめ
#     print('{:06}{:06}'.format(p, bisect_left(d[p], y)+1))

from bisect import bisect_right
from collections import defaultdict
n, m = map(int, input().split())
py = [tuple(map(int, input().split())) for _ in range(m)]

# ソートして識別番号を作ったあと、入力順に出力する
# spy = sorted(py)

# signate = {}
# cnt = 0
# last_p = 0
# for p, y in spy:
#     pref = "{:06}".format(p)
#     if last_p == p:
#         cnt += 1
#     else:
#         last_p = p
#         cnt = 1
#     year = "{:06}".format(cnt)
#     signate["{}-{}".format(p, y)] = pref+year

# for p, y in py:
#     print(signate['{}-{}'.format(p, y)])

# bisectを使うと、集計の操作が不要になる
# リストとして、データを保存しておきさえすれば、そこから取り出すのはO(logn)


dd = defaultdict(list)

for p, y in sorted(py):
    dd[p] += [y]

for p, y in py:
    print("{:06}{:06}".format(p, bisect_right(dd[p], y)))

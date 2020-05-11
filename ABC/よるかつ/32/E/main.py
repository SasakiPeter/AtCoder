# どう考えても、Tは関係ない
# 差が最大になる区間がいくつあるかをカウントする問題
from collections import defaultdict
n, t = map(int, input().split())
A = list(map(int, input().split()))

MAX_S = []
max_tmp = 0
for a in A[::-1]:
    if max_tmp < a:
        max_tmp = a
    MAX_S.append(max_tmp)
MAX_S = MAX_S[::-1]
# print(MAX_S)
cnt = defaultdict(int)
for a, s in zip(A, MAX_S):
    cnt[s-a] += 1

c = [(k, v) for k, v in cnt.items()]
c.sort(reverse=True)
print(c[0][-1])

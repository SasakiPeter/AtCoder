# n = int(input())
# l = [input().split() for _ in range(n)]
# sum_p = sum(int(p) for s, p in l)
# t = [s for s, p in l if int(p) > sum_p//2]
# print('atcoder' if len(t) == 0 else t[0])

# こういうR行C列の入力の時は、上記のように2次元配列に格納するか、
# 複数の一次元配列に格納する方法が取れる

# どちらを用いるかは、常に行で計算するなら2次元入れがいいが、
# 行での計算が求められる場合は、一次元２つの方が扱いやすそう

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
s, p = [], []
for _ in range(n):
    s_, p_ = input().split()
    s.append(s_)
    p.append(int(p_))

# この記述賢い
print('atcoder' if max(p) <= sum(p)/2 else s[p.index(max(p))])

# a = [x for x, y in zip(s, p) if y > sum(p)/2]
# print('atcoder' if a == [] else a[0])

# n = int(input())
# S, P = [], []
# for _ in range(n):
#     s, p = input().split()
#     S.append(s)
#     P.append(int(p))

# for i, p in enumerate(P):
#     if p > sum(P)/2:
#         print(S[i])
#         break
# else:
#     print('atcoder')

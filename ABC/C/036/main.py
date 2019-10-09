# from collections import defaultdict

# indexはO(n)かかるからだめだが、普通に実装するとこうなる
# n = int(input())
# a = [int(input()) for _ in range(n)]
# s = sorted(set(a))
# for x in a:
#     print(s.index(x))

# a = defaultdict(int)
# for _ in range(n):
#     a[int(input())] += 1

# 出してくる時には、集計が終わっていて、どの数字が0で〜って
# 決まっていないといけない
# index使わなければ勝ちゲーなので、こんなんでOK

# n = int(input())
# a = [int(input()) for _ in range(n)]
# s = {x: i for i, x in enumerate(sorted(set(a)))}
# for x in a:
#     print(s[x])


# bisectを習った
# 順序を維持したまま、値を挿入するのがbisect
# 内部的に二分探索を用いているので、通常のソート0(nlogn)よりも
# 早い 二分探索はO(logn)


# 923
# 復習として、普通の実装する
# n = int(input())
# # 入力を圧縮する
# # 順番は保つ必要がある
# # 欲しい情報は、どの数字が何番目に大きいかってこと
# # ２重ループ必須な気がする
# a = [int(input()) for _ in range(n)]
# s = {x: i for i, x in enumerate(sorted(set(a)))}
# print(*(s[x] for x in a), sep="\n")

# 復習として、bisectを用いた実装を行う
# bisectは二分探索によって、効率よく順序を保ったまま値を挿入できる
# ライブラリ。
# そうだっけ？


# bisectを使う方が、メモリのムラが少ない
from bisect import bisect_left

# ls = [*range(10)][::2]
# print(ls)
# # 値を適切な位置に挿入できる
# insort_left(ls, 3)
# print(ls)
# # bisect_leftで何番目に大きいかが得られる
# print(bisect_left(ls, 5))

n = int(input())
a = [int(input()) for _ in range(n)]
b = sorted(set(a))
# for x in a:
#     print(bisect_left(b, x))
print(*(bisect_left(b, x) for x in a), sep='\n')

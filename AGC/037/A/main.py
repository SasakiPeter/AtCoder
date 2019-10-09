from collections import Counter

s = input()

# aabbaa
# a ab ba a

# aaaccacabaababc
# a aa c ca c a b a ab a b c

c = 0
# 前回のやつ　カウント済み
last = ''
# キャッシュはカウントしてないやつ
cache = ''
for x in s:
    if last != cache+x:
        c += 1
        last = cache+x
        cache = ''
    elif last != x:
        c += 1
        last = x
    elif last != cache+x:
        c += 1
        last = cache+x
        cache = ''
    else:
        cache += x
    # print(x, last, cache, cache+x, last != cache+x)

print(c)


# c2 = 0
# cache2 = ''
# for x in s[::-1]:
#     if cache2 != x:
#         c2 += 1
#         cache2 = x
#     else:
#         cache2 += x

# for i in range(1, len(s) + 1)[::-1]:
#     # ここのforは幾つのペアにするかの数
#     # 最初に15分割する
#     ls = list(s)
#     # その時の分割の仕方は、全部１つに区切る
#     # その場合、区切った文字が全て異なるかを判定しないチケない
#     # 区切った文字はリストで出力する

#     if i > len(s):
#         # 14分割だった時
#         # 14通りある
#         for

#         # 13分割だった場合 15C2 a a a a a a a a a a
#         # len(s)-i

#         # 区切った文字が、全て異なるかは、Counterで集計して、その長さが、
#     d = Counter(ls)
#     if len(d) == i:
#         ans = i
#         break
#     # iと同じかを確かめる
#     # 該当していたら、break

# print(max(c, c2))

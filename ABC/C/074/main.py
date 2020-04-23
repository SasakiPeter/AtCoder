#!/usr/bin/env python3
# 0 0 が出ちゃうのは、濃度計算できないからだめ　これに注意
# DPを使うと、うまく取りうる値を列挙できる
import itertools
A, B, C, D, E, F = map(int, input().split())
# U = 3000
U = F
water = [0]*(U+1)
water[0] = 1
for i in range(U+1):
    if water[i]:
        if i+100*A <= U:
            water[i+100*A] = 1
        if i+100*B <= U:
            water[i+100*B] = 1

water_val = [val for val in range(1, U+1) if water[val]]
# print(water_val)

suger = [0]*(U+1)
suger[0] = 1
for i in range(U+1):
    if suger[i]:
        if i+C <= U:
            suger[i+C] = 1
        if i+D <= U:
            suger[i+D] = 1

suger_val = [val for val in range(U+1) if suger[val]]
# print(suger_val)
# ans = (0, 0)
max_c = -1
for w, s in itertools.product(water_val, suger_val):
    # print(w, s)
    if E*w < 100*s:
        continue
    if F < w+s:
        continue

    if max_c < 100*s/(w+s):
        max_c = 100*s/(w+s)
        ans = (w+s, s)

print(*ans)


# sugerの取りうる値をうまく列挙できなかった（結構重くなっちゃう）
# A, B, C, D, E, F = map(int, input().split())

# # 濃度nの砂糖水が作れるか計算して、
# # もっとも高濃度のやつを出せばいいんじゃね？
# # ↑それは難しそう
# # 濃度の上限がなかったとしたら？
# # 入れられるアイテムをあらかじめ生成したナップサックをとけばいいんじゃね？

# # 例えば、上限濃度を超えないように設定する
# items = []


# # cとdの順番は正直どっちがどっちとか関係ないので、最初にありえる
# # 配合パターンを列挙しておく
# water = list(set([100*(A*w+B*x) for w in range(16)
#                   for x in range(16) if A*w+B*x <= 30]))
# # water.sort()

# # print(water)

# # suger = list(set([C*w+D*x for w in range(1501)
# #                   for x in range(1501) if C*w+D*x <= 3000]))
# # suger.sort()
# # print(suger)

# # 砂糖のパターンが多すぎるので、ここは考える
# # 水が少ない方が濃度は濃い
# for w in water:
#     for x in range(1501):
#         c = C*x
#         # これに対応するdは簡単に求まる
#         i = (F-w-c)//D
#         for y in reversed(range(i+1)):
#             d = D*y
#             if 0 < w+c+d <= F and w*E >= 100*(c+d):
#                 items.append((100*(c+d)/(w+c+d), w+c+d, c+d))
#                 break

# items.sort(reverse=True)
# print(items[0][1], items[0][2])


# # もっと高濃度砂糖水が作れる
# for w in range(16):
#     a = 100*A*w
#     for x in range(16):
#         if w == x == 0:
#             continue
#         b = 100*B*x
#         if F-a-b < 0:
#             continue
#         for y in range(1501):
#             c = C*y
#             i = (F-(a+b+c))//D
#             for z in reversed(range(i+1)):
#                 d = D*z
#                 if a+b+c+d <= F and (a+b)*E >= (c+d)*100:
#                     items.append((100*(c+d)/(a+b+c+d), a+b, c+d))
#                     break

# items.sort(reverse=True)
# print(items)

# print(items[0][1]+items[0][2], items[0][2])


# ACパック
# for x in range(1, 16):
#     for y in range(1, 1501):
#         a = 100*A*x
#         b = 100*B*x
#         c = C*y
#         d = D*y
#         if a+c <= F and a*E >= 100*c:
#             items.append((100*c/(a+c), a, c))
#         if a+d <= F and a*E >= 100*d:
#             items.append((100*d/(a+d), a, d))
#         if b+c <= F and b*E >= 100*c:
#             items.append((100*c/(b+c), b, c))
#         if b+d <= F and b*E >= 100*d:
#             items.append((100*d/(b+d), b, d))

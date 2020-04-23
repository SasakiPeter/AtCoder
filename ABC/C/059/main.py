n = input()
a = list(map(int, input().split()))


def chk(a, positive):
    ans = tmp = 0
    for x in a:
        tmp += x
        # 偶数番目をpositiveにした時
        if positive and tmp < 1:
            # 1になるように補正
            ans += 1-tmp
            tmp = 1
        elif not positive and tmp > -1:
            # -1になるように補正
            ans += abs(-1-tmp)
            tmp = -1

        positive = not positive
    return ans


# スタートが、正の場合か、負の場合かで場合わけして、
# それらの切り替えを内部で行ってループしているっていう実装
print(min((chk(a, True), chk(a, False))))


# 自分でやってみたけど、結局いまく行かなかったなぜだーーー

# n = int(input())
# a = list(map(int, input().split()))

# ruisekiwa = []
# tmp = 0
# for x in a:
#     tmp += x
#     ruisekiwa.append(tmp)

# # 最初がposiの時
# # even = ruisekiwa[::2]
# # odds = ruisekiwa[1::2]

# print(ruisekiwa)

# ans = tmp = cnt = 0
# for x, y in zip(ruisekiwa, ruisekiwa[1:]):
#     x += tmp
#     y += tmp
#     # print(x, y, tmp)
#     if (x == abs(x) and y != abs(y)) or (x != abs(x) and y == abs(y)) and y != 0:
#         cnt += 1
#     else:
#         # 累積和が、符号反転できるように補正しないといけない
#         hoge = 0
#         if y > 0:
#             hoge += -1-y
#         elif y < 0:
#             hoge += 1-y
#         else:
#             if x > 0:
#                 hoge = -1
#             else:
#                 hoge = 1
#         tmp += hoge
#         ans += abs(hoge)
#         # print(ans, 'ans hoge')
#     print(x, y, ans)

# if len(ruisekiwa) - 1 == cnt:
#     print('0')
# else:
#     print(ans)

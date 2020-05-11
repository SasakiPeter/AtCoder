n, m = map(int, input().split())

if n % 2 == 1:
    a = [i for i in range(1, m+1)]
    b = [i for i in reversed(range(m+1, 2*m+1))]
    ab = [(x, y) for x, y in zip(a, b)]
else:
    # # 偶数の時、差がn//2と同じになるようなペアはダメ
    # # 差が1,3,5パターン
    # x = (n-1)//2
    # a = [i+1 for i in range(x//2)]
    # b = [i+1 for i in reversed(range(x//2+1, x))]
    # ab_ev = [(x, y) for x, y in zip(a, b)]
    # print(a, b)
    # # 差が2,4,6パターン
    # y = n//2
    # a = [i for i in range(x+2, y//2+1)]
    # b = [i for i in reversed(range(y//2+2, n))]
    # ab_od = [(x, y) for x, y in zip(a, b)]
    # ab = ab_ev+ab_od
    # ab = ab[:m]
    ab = []
    x, y = (n-1)//2, n//2
    if x % 2 != 0:
        x, y = y, x

    evenl = 1
    evenr = x
    while evenl < evenr:
        ab.append((evenl, evenr))
        evenl += 1
        evenr -= 1

    oddl = x+1
    oddr = n-1
    while oddl < oddr:
        ab.append((oddl, oddr))
        oddl += 1
        oddr -= 1

    ab = ab[:m]


# # b = [i for i in reversed(range(m+2, 2*m+2))]
# # b = [i for i in range(n, n-m-1, -1)]


# # print(ab)
for a, b in ab:
    print(a, b)

# for x, y in zip(a, b):
#     print(x, y)

# 条件を満たしているか確認
# Aさんになりきる
# 記録していく処理重い
if n*m < 10**4:
    opponent = []
    for i in range(n):
        x = i+n//2
        # 出場する会場を見つける
        for a, b in ab:
            if x % n+1 == a:
                # 対戦相手は
                opp = (b-i) % n
                if opp == 0:
                    opp = n
                opponent.append(opp)
                break
            if x % n+1 == b:
                # 対戦相手は
                opp = (a-i) % n
                if opp == 0:
                    opp = n
                opponent.append(opp)
                break
    # print(ab, n, m)
    # print(opponent)
    assert len(set(opponent)) == len(opponent)

# # Bさんの場合
# opponent = []
# for i in range(n):
#     x = i+1
#     # 出場する会場を見つける
#     for a, b in ab:
#         if x % n+1 == a:
#             # 対戦相手は
#             opp = (b-i) % n
#             if opp == 0:
#                 opp = n
#             opponent.append(opp)
#             break
#         if x % n+1 == b:
#             # 対戦相手は
#             opp = (a-i) % n
#             if opp == 0:
#                 opp = n
#             opponent.append(opp)

#             break

# print(ab, n, m)
# print(opponent)
# assert len(set(opponent)) == len(opponent)

# # nが偶数のときおかしい
# assert len(ab) == m

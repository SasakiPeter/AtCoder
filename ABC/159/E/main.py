# import itertools
# h, w, k = map(int, input().split())
# S = [list(map(int, input())) for _ in range(h)]
# S_ = tuple(itertools.chain(*zip(*S)))
# print(S_)
# print(S)
# for x in zip(*S):
#     print(x)

# ls = [1, 2, 3]
# ls2 = [4, 5, 6]
# ls3 = [7, 8, 9]
# print(itertools.chain(ls, ls2, ls3))
# print(list(itertools.chain(ls, ls2, ls3)))

from itertools import product
h, w, k = map(int, input().split())
CHOCO = [list(map(int, input())) for _ in range(h)]
# h, w, k = 10, 1000, 2
# CHOCO = [list(map(int, "11010"*200)) for _ in range(h)]
INF = 10**5

# print(h, w, k)
# for row in CHOCO:
#     print("".join(map(str, row)))

# 水平方向の切れ込み全探索
it = ["01"]*(h-1)
ans = INF
for x in product(*it):
    # print("".join(x))
    # 貪欲に垂直方向に切れ込みをいれる
    cnt = sum(map(int, x))

    # 切れ込みを入れた方向に集約する
    # この集約は、sample3が通らない
    # pieceごとに集約して、それぞれで貪欲に切る
    agg = [[0]*(w) for _ in range(cnt+1)]
    # ここ、浅くしたい ここが重い
    *ls, = map(int, x+('1',))
    for i in range(w):
        prev = c = 0
        for j, split in enumerate(ls):
            if split:
                agg[c][i] = prev+CHOCO[j][i]
                prev = 0
                c += 1
            else:
                prev += CHOCO[j][i]
    # print(agg)

    # 集約した配列を貪欲に切っていく
    # 切れない場合がある continue
    tmp = [0]*(cnt+1)
    for xyz in zip(*agg):
        cannot_split = False
        can_continue = True
        for i, x in enumerate(xyz):
            if x > k:
                cannot_split = True
                break
            if x+tmp[i] > k:
                can_continue = False
                break

        if cannot_split:
            break

        # ここが深い
        if can_continue:
            for i, x in enumerate(xyz):
                tmp[i] += x
                continue
        else:
            for i, x in enumerate(xyz):
                tmp[i] = x
            cnt += 1

    if cannot_split:
        continue
    # print(ans, cnt, tmp)
    ans = min(ans, cnt)
print(ans)

#!/usr/bin/env python3
r, g, b = map(int, input().split())


def sigma(a, b):
    if a == b:
        return a
    elif b < a:
        return 0
    else:
        return (a+b)*(b-a+1)//2


# ls = [
#     sigma(1, (r-1)//2),
#     sigma(1, r//2),
#     sigma(1, (g-1)//2),
#     sigma(1, g//2),
#     sigma(1, (b-1)//2),
#     sigma(1, b//2),
# ]
# # for item in ls:
# # #     print(item)
# print(sum(ls))


# 境界を探索してみる (半開半閉)
INF = 10**18
ans = INF
for L in range(-300, 301):
    for R in range(L, 302):
        if R-L < g:
            continue

        # 左に移動する時のパターン
        if R < 0:
            gcost = (-L-g)*g
            gcost += sigma(1, g)
        # 右に移動する時のパターン
        elif 0 < L:
            gcost = (L-1)*g
            gcost += sigma(1, g)
        # 両方に分ける時のパターン
        else:
            gr = R-1
            gl = g-gr-1
            gcost = sigma(1, gr)+sigma(1, gl)

        # 全体が右に移動
        if 101 < R:
            bcost = (R-100-1)*b+sigma(1, b)
        else:
            # 左右にうまくふりたい
            bl = (b-1)//2
            br = b//2
            # 右に多めにふる
            if 100-R < bl:
                bl = 100-R
                br = b-bl-1
            bcost = sigma(1, br)+sigma(1, bl)

        # 全体が左に移動
        if L < -99:
            rcost = (-L-100)*r+sigma(1, r)
        else:
            rr = (r-1)//2
            rl = r//2
            # 右少なめ左多め
            if L+100-1 < rr:
                rr = L+100-1
                rl = r-rr-1
            rcost = sigma(1, rr)+sigma(1, rl)

        cost = rcost+gcost+bcost
        # if cost < ans:
        #     print(L, R, rr, rl, br, bl, gr, gl, r, g, b)
        ans = min(ans, cost)
print(ans)

# print(sigma(1, r-1), sigma(1, g-1), sigma(1, b-1))
# print(sum([sigma(1, r-1), sigma(1, g-1), sigma(1, b-1)]))

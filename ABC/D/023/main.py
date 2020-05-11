# 解を仮定したにぶたん
n = int(input())
HS = [tuple(map(int, input().split()))for _ in range(n)]

L = 1
INF = 10**14
R = INF
while L != R-1:
    # for cnt in range(45):
    M = (L+R)//2
    limit = sorted(map(lambda hs: (M-hs[0])/hs[1], HS))
    # print(limit)
    # if 40 < cnt:
    #     print(L, R, M, limit)
    # for i in range(n):
    #     if i <= limit[i]:
    for i, lim in enumerate(limit):
        if i <= lim:
            continue
        L = M
        break
    else:
        R = M

print(R)

# これ貪欲にはいけない無理そう
# n = int(input())
# hs = sorted([tuple(map(int, input().split()))
#              for _ in range(n)], key=lambda x: x[1], reverse=True)
# print(hs)
# ans = 0
# for idx, (h, s) in enumerate(hs):
#     ans = max(ans, h+idx*s)
# print(ans)

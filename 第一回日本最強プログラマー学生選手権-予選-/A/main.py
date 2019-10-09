import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

M, D = map(int, input().split())

ans = 0
# for m in range(1, M+1):
#     for d in range(20, D + 1):
#         a, b = map(int, str(d))
#         if b < 2:
#             continue
#         elif m == a*b:
#             ans += 1


# ループが少ない方を外側にするのが定石やったな
for d in range(20, D + 1):
    for m in range(1, M+1):
        # 普通は割ったやつとそのあまりを取得するらしい
        # その方が早いし
        a, b = d//10, d % 10
        # a, b = divmod(d, 10)
        if m == a*b and b >= 2:
            ans += 1


print(ans)

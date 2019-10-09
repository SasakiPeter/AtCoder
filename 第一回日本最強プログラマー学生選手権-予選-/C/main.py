import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


n = int(input())
s = input().rstrip()
MOD = 10**9+7

cnt = 0
point = 1
for i, x in enumerate(s):
    # if (x == 'B' and i % 2 == 0) or (x == 'W' and i % 2 != 0):
    # 排他的論理和XORを用いることもできる
    if (x == 'W') ^ (i % 2 == 0):
        cnt += 1
    else:
        point *= cnt
        cnt -= 1
        point %= MOD


# LとRの個数が同じか確かめる
if cnt != 0:
    print(0)
else:
    # factorial
    for x in range(1, n+1):
        point *= x
        point %= MOD

    print(point)


# # lr = ''
# cnt = 0
# point = 1
# for i, x in enumerate(s):
#     # if i % 2 == 0:
#     if (x == 'B' and i % 2 == 0) or (x == 'W' and i % 2 != 0):
#         # lr += 'L'
#         cnt += 1
#     else:
#         # lr += 'R'
#         point *= cnt
#         cnt -= 1
#     # else:
#     #     if x == 'B':
#     #         # lr += 'R'
#     #         point *= cnt
#     #         cnt -= 1
#     #     else:
#     #         # lr += 'L'
#     #         cnt += 1

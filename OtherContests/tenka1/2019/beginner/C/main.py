#!/usr/bin/env python3
n = int(input())
s = input()
INF = 10**9
white_cnt = s.count('.')
black_cnt = 0
ans = INF
for c in s:
    ans = min(ans, black_cnt + white_cnt)
    if c == '#':
        black_cnt += 1
    else:
        white_cnt -= 1
else:
    ans = min(ans, black_cnt + white_cnt)

print(ans)

# if x+y == '#.':
# print(black_cnt, white_cnt)

# if black_cnt < white_cnt:
#     ans += black_cnt
#     black_cnt = 0
# else:
#     # ans = min(ans, white_cnt)
#     ans += white_cnt
#     # break
# n = int(input())
# s = input()
# # 矛盾点の前にある黒石の数と、後ろにある白石の数の小さい方＋１をカウント
# ans = 0
# black_cnt = 0
# prev = ""

# for i in range(n):
#     if prev+s[i] == '#.':
#         white_cnt = 0
#         for j in range(i+1, n):
#             if s[j] != '.':
#                 break
#             white_cnt += 1
#         ans += min(black_cnt, white_cnt)+1
#     if s[i] == '#':
#         black_cnt += 1
#     else:
#         black_cnt = 0
#     prev = s[i]
# print(ans)


# # L = R = 0
# # while L < n:
# #     if prev+s[L] == "#.":
# #         white_cnt = 0
# #         while R < n-1:
# #             R += 1
# #             if s[R] != '.':
# #                 break
# #             white_cnt += 1
# #         ans += min(black_cnt, white_cnt)+1
# #         L = R = R+1
# #         continue
# #     if s[L] == "#":
# #         black_cnt += 1
# #     else:
# #         black_cnt = 0
# #     prev = s[L]
# #     L += 1
# #     R += 1
# # print(ans)

# この問題の肝は、取りうる値の範囲を考察すること。
# なかなか難しい
from collections import Counter
s = input()
n = len(s)
s1 = Counter(s)
s2 = Counter(input())
s3 = Counter(input())
min_s1 = max_s1 = 0
for k, v in s3.items():
    v1, v2 = s1[k], s2[k]
    if v1+v2 < v:
        min_s1 = max_s1 = 0
        break
    min_s1 += v-min(v2, v)
    max_s1 += min(v1, v)
    # val = []
    # for i in range(v+1):
    #     if v1 < i:
    #         break
    #     if v2 < v-i:
    #         continue
    #     val.append(i)
    # min_s1 += val[0]
    # max_s1 += val[-1]
print('YES' if min_s1 <= n//2 <= max_s1 else 'NO')


# # from itertools import product
# from collections import Counter, defaultdict
# s1 = Counter(input())
# s2 = Counter(input())
# s3 = input()
# n = len(s3)//2
# s3 = Counter(s3)
# # print(s1, s2)
# # print(s3)

# # s3を作るときに、必要なパーツごとのありうる組みを列挙する
# dd = defaultdict(list)
# for k, v in s3.items():
#     v1 = s1[k]
#     v2 = s2[k]
#     if v1+v2 < v:
#         print('NO')
#         exit()
#     # vこのパーツをs1からいくつ使うか
#     for i in range(v+1):
#         if v1 < i:
#             break
#         if v2 < v-i:
#             continue
#         dd[k].append((i, v-i))
# # print(dd)

# # # 全探索いける？←むり 爆発的に組み合わせが多くなってしまう
# # # print(dd.values())
# # for z in product(*dd.values()):
# #     cnt_1 = 0
# #     cnt_2 = 0
# #     for x, y in z:
# #         cnt_1 += x
# #         cnt_2 += y
# #     if cnt_1 == cnt_2 == n:
# #         print('YES')
# #         break
# # else:
# #     print('NO')


# # DPしないとダメ？←DPというか、頭を使えばいい
# MIN = 0
# MAX = 0
# for v in dd.values():
#     v.sort()
#     MIN += v[0][0]
#     MAX += v[-1][0]
# # print(MIN, MAX, n)

# print('YES' if MIN <= n <= MAX else 'NO')

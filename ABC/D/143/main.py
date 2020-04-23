from bisect import bisect_left

n = int(input())
l_ls = sorted(map(int, input().split()))

ans = 0

for i in range(n):
    for j in range(i+1, n):
        a, b = l_ls[i], l_ls[j]
        # 実は、このleftっていう範囲は、用をなしていない
        # むしろこれがあると、重複してカウントしてしまう
        # 探索する範囲は、j番目の物よりも後ろでいい
        # そして、この条件は下の条件よりも厳しい
        # left = bisect_left(l_ls, max(a-b, b-a)+1)
        left = j+1
        right = bisect_left(l_ls, a+b)
        # print(ls, a, b, left, right)
        # print(right-left)
        ans += right-left

print(ans)

# in list を使うよりもindexでとっておいたほうが、便利な時もある
# for i, a in enumerate(l_ls):
#     for j, b in enumerate(l_ls):
#         if i >= j:
#             continue

#         # 条件に一致するものが入っているかで判定できるはず
#         # a-b < c and b-a < c and c < a+b
#         # max(a-b, b-a) < c and c < a+b
#         # この区間に収まる整数cがl_lsにいくつ含まれているか
#         # (max(a-b, b-a), a+b)
#         # indexを取得すればいい
#         # bisectで条件を満たすindexを取得し、個数を数える
#         # if i < j:
#         #     ls = l_ls[:i] + l_ls[i+1:j] + l_ls[j+1:]
#         # else:
#         #     ls = l_ls[:j] + l_ls[j+1:i] + l_ls[i+1:]
#         ls = l_ls[:i] + l_ls[i+1:j] + l_ls[j+1:]

#         left = bisect_left(ls, max(a-b, b-a)+1)
#         right = bisect_left(ls, a+b)
#         # print(ls, a, b, left, right)
#         # print(right-left)
#         ans += right-left

#         # for k, c in enumerate(l_ls):
#         #     if i == k or j == k:
#         #         continue

#         #     if sorted([a, b, c]) in memo:
#         #         continue

#         #     if a < b+c and b < c+a and c < a+b:
#         #         ans += 1
#         #         memo.append(sorted([a, b, c]))

# print(ans//3)

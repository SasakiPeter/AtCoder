# s = input().split('+')
# ans = 0

# # +の数+1個の項がある
# # +で区切られた数式の中に、0がなければ+1
# for x in s:
#     if '0' not in x:
#         ans += 1
# print(ans)

print(sum(1 if '0' not in x else 0 for x in input().split('+')))

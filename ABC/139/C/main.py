# n = int(input())
# h = list(map(int, input().split()))

# # 10**9
# cnt = 0
# cache = 0
# last = h[0]
# for x in h[1:]:
#     if last >= x:
#         cnt += 1
#     else:
#         cnt = 0
#     if cache < cnt:
#         cache = cnt
#     last = x

# print(cache)

n = int(input())
h = list(map(int, input().split()))

cnt = 0
ans = 0
for x, y in zip(h, h[1:]):
    if x >= y:
        cnt += 1
    else:
        cnt = 0
    # これでも良さそう
    # ans = max(ans, cnt)
    if ans < cnt:
        ans = cnt
print(ans)

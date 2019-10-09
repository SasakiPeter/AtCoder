# k, s = map(int, input().split())
# cnt = 0
# # ls = [z for z in range(k+1)]
# for x in range(k+1):
#     for y in range(k+1):
#         if 0 <= s-x-y <= k:
#             # if s - x - y in ls:
#             cnt += 1
# print(cnt)

k, s = map(int, input().split())
# print(sum(0 <= s-x-y <= k for x in range(k+1) for y in range(k+1)))

# lenの方が圧倒的に早い
print(len([1 for x in range(k+1) for y in range(k+1) if 0 <= s-x-y <= k]))

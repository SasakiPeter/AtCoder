
# from itertools import combinations_with_replacement
k, s = map(int, input().split())
ans = 0
for x in range(k+1):
    for y in range(k+1):
        z = s-x-y
        if z < 0:
            break
        if k < z:
            continue
        # if x+y+z == s:
        ans += 1
        # print(x, y, z)
print(ans)
# print((2500+1)**2)


# ans = 0
# for x in combinations_with_replacement(range(k+1), 3):
#     if sum(x) == s:
#         ans += 1
# print(ans)

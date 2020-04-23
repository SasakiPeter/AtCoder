n = int(input())
h = list(map(int, input().split()))


# 最小ずつ区間で水やり
def dfs(left, right):
    if left >= right:
        return 0
    idx = left + h[left: right].index(min(h[left: right]))
    x = h[idx]
    for i in range(left, right):
        h[i] -= x
    return dfs(left, idx) + x + dfs(idx+1, right)


print(dfs(0, n))

# 1ずつ水やり
# ans = 0
# while sum(h) > 0:
#     prev = 0
#     split = 0
#     for v in h:
#         if prev == 0 and v != 0:
#             split += 1
#         prev = v

#     ans += split
#     h = [v-1 if v > 0 else 0 for v in h]

# print(ans)


# 天才的発想
# ans = 0
# prev = 0
# for v in h:
#     if prev < v:
#         ans += v - prev
#     prev = v

# print(ans)

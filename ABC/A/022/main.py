# n, s, t = map(int, input().split())
# l = [int(input()) for _ in range(n)]

# c = 0
# w = 0

# # これでいいらしい
# # c = w = 0

# for x in l:
#     w += x
#     # Trueを追加すると+1と同じらしい
#     # c += s <= w <= t
#     if s <= w <= t:
#         c += 1
# print(c)

# 926
n, s, t = map(int, input().split())
w = c = 0
for _ in range(n):
    w += int(input())
    c += s <= w <= t

print(c)

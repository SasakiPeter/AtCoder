n, k = map(int, input().split())
r = sorted(map(int, input().split()))[-k:]
c = 0
for x in r:
    c = (c+x)/2
print(c)

# n, k = map(int, input().split())
# R = list(map(int, input().split()))
# c = 0

# # 貪欲？
# r = sorted(R)[-k:]
# # print(r)

# for x in r:
#     c = (c+x)/2
# print(c)

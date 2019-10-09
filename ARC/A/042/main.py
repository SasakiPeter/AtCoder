# setを使った実装
# n, m = map(int, input().split())
# a = [int(input()) for _ in range(m)]
# # これ、シンタックス的にダメらしい
# # b = {*range(1, n+1)}
# b = set(range(1, n+1))
# c = set()
# while a:
#     s = a.pop()
#     if s not in c:
#         print(s)
#     c.add(s)
# print(*sorted(b-c), sep='\n')

# 愚直に実装
n, m = map(int, input().split())
t = list(range(1, n+1))[::-1]
for _ in range(m):
    t.append(int(input()))

c = set()
for x in t[::-1]:
    if x not in c:
        print(x)
    c.add(x)

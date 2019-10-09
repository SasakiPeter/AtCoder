# # from queue import deque
# from collections import deque

# q = deque()

# n = int(input())
# *a, = map(int, input().split())
# for i, x in enumerate(a):
#     if i % 2 == 0:
#         q.append(x)
#     else:
#         q.appendleft(x)

# if n % 2:
#     print(*reversed(q))
# else:
#     print(*q)

# IQ200 戦略
n = int(input())
a = list(map(int, input().split()))
# print(*(a[::-2]+a[int(n % 2)::2]))

# if n % 2:
#     print(*(a[::-2]+a[1::2]))
# else:
#     print(*(a[::-2]+a[::2]))

# これでも通るらしい
print(*a[::-2], *a[n % 2::2])

# 全探索できる

import itertools
n = int(input())
statements = [[]for _ in range(n)]
for i in range(n):
    a = int(input())
    for _ in range(a):
        x, y = map(int, input().split())
        statements[i].append((x-1, y))

# print(statements)
can_be = []
# for i in itertools.product('01', repeat=n):
for people in itertools.product([0, 1], repeat=n):
    # people = tuple(map(int, i))
    contradiction = 0
    for j in range(n):
        if people[j] == 0:
            continue
        for k, x in statements[j]:
            # print(people, k, x)
            if people[k] == x:
                continue
            contradiction = 1
            break
        if contradiction:
            break
    else:
        can_be.append(people)

# print(can_be)

ans = 0
for p in can_be:
    ans = max(ans, p.count(1))

print(ans)

# # 矛盾点の数を数える
# # 不親切な人のいうことは無視できる
# n = int(input())
# ls = [None]*(n+1)
# ans = n
# for _ in range(n):
#     a = int(input())
#     for _ in range(a):
#         x, y = map(int, input().split())
#         if ls[x] == -1:
#             continue
#         if ls[x] is None:
#             # iさんがxさんに0出してたり、
#             # 1出されてて、0だししたら、
#             # これ考えるのだるい

#             ls[x] = y
#         elif ls[x] != y:
#             ans -= 1
#             ls[x] = -1
# print(ans)

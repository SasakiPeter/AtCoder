# maspy指向
import itertools
from collections import defaultdict
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
# vectors = []
dd = defaultdict(int)
for xy1, xy2 in itertools.combinations(xy, 2):
    x1, y1 = xy1
    x2, y2 = xy2
    unit_vect = (x1-x2, y1-y2)
    # vectors.append(unit_vect)
    dd[unit_vect] += 1
    unit_vect = (x2-x1, y2-y1)
    dd[unit_vect] += 1
    # vectors.append(unit_vect)

# print(vectors)

# print(dd)
if n == 1:
    ans = 1
else:
    ans = n-max(dd.values())
print(ans)


# ただ実装しただけ
# n = int(input())
# xy = [list(map(int, input().split())) for _ in range(n)]
# xy.sort()
# vectors = set()
# for i in range(n-1):
#     for j in range(i+1, n):
#         xi, yi = xy[i]
#         xj, yj = xy[j]
#         if xj-xi == 0 and yj-yi == 0:
#             continue
#         unit_vector = (xj-xi, yj-yi)
#         vectors |= {unit_vector}
# # print(vectors)
# ans = n
# for vector in vectors:
#     cnt = 0
#     for i in range(n-1):
#         for j in range(i+1, n):
#             xi, yi = xy[i]
#             xj, yj = xy[j]
#             if vector == (xj-xi, yj-yi):
#                 cnt += 1
#     # print(cnt)
#     ans = min(ans, n-cnt)
# print(ans)


# 問題の意味よくわかってなかった
# n = int(input())
# # 初期値に近いものから順に探索して行ったらうまくいく？
# nodes = []
# for _ in range(n):
#     x, y = map(int, input().split())
#     nodes.append((x, y))

# nodes.sort(reverse=True)
# # print(nodes)
# ans = 0
# while nodes:
#     ans += 1
#     x, y = nodes.pop()
#     for i, j in nodes[::-1]:
#         if x-i != 0 and y-j != 0:
#             vect = (i-x, j-y)
#             break
#     p, q = vect
#     rm_list = []
#     for i, j in nodes:
#         if i-x == 0 or j-y == 0:
#             continue
#         if (i-x) % p == 0 and (j-y) % q == 0:
#             rm_list.append((i, j))
#     for item in rm_list:
#         nodes.remove(item)
#     # print(vect, nodes)
# print(ans)

# pythonには、便利なitertoolsがある
from itertools import combinations
n = int(input())
xy = [tuple(map(int, input().split()))for _ in range(n)]
ans = 0
for pqr in combinations(xy, 3):
    p, q, r = pqr
    s = abs((q[0]-p[0])*(r[1]-p[1])-(r[0]-p[0])*(q[1]-p[1]))
    # if s != 0 and s % 2 == 0:
    if s != 0 and not s & 1:
        ans += 1
print(ans)


# n = int(input())
# xy = [list(map(int, input().split()))for _ in range(n)]
# ans = 0
# for i in range(n-2):
#     for j in range(i+1, n-1):
#         for k in range(j+1, n):
#             xi, yi = xy[i]
#             xj, yj = xy[j]
#             xk, yk = xy[k]
#             s = abs((xj-xi)*(yk-yi)-(yj-yi)*(xk-xi))
#             if s == 0:
#                 continue
#             if s % 2 == 0:
#                 ans += 1

# print(ans)

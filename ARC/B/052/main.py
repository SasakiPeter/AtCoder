# 累積和で解き直し
import math as m
n, q = map(int, input().split())
cones = []
for _ in range(n):
    x, r, h = map(int, input().split())
    cones.append((x, r, h))

# print(cones)
U = 2*10**4
S = [0]*(U+1)
A = [0]*U

for x, r, h in cones:
    # x~x+hの座標に該当する範囲の面積を、
    # １座標ごとに求めて、配列に格納する
    v = m.pi*r**2*h/3
    for i in range(h):
        # x+i~x+i+1までの区間の面積
        A[x+i] += v*(((h-i)/h)**3-((h-i-1)/h)**3)


for i in range(U):
    S[i+1] = S[i]+A[i]

# # i以下の座標の面積の合計 これは重すぎる
# for i in range(1, U):
#     for cone in cones:
#         x, r, h = cone
#         if i <= x:
#             continue
#         elif x+h <= i:
#             v = m.pi*r**2*h/3
#             S[i] += v
#         else:
#             v = m.pi*r**2*h/3
#             v2 = v*((x+h-i)/h)**3
#             S[i] += v-v2

# print(S[:5])

for _ in range(q):
    a, b = map(int, input().split())
    print(S[b]-S[a])

# import math as m
# n, q = map(int, input().split())
# cones = []
# for _ in range(n):
#     x, r, h = map(int, input().split())
#     cones.append((x, r, h))

# for _ in range(q):
#     a, b = map(int, input().split())
#     ans = 0
#     for x, r, h in cones:
#         v = m.pi*r**2*h/3
#         if a < x:
#             v2 = v
#         elif x+h <= a:
#             v2 = 0
#         else:
#             v2 = v*((x+h-a)/h)**3
#         if b < x:
#             v3 = v
#         elif x+h <= b:
#             v3 = 0
#         else:
#             v3 = v*((x+h-b)/h)**3
#         ans += v2-v3
#     print(ans)

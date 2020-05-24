# 座圧よく分からん
import bisect
import sys
input = sys.stdin.readline
n, q = map(int, input().split())

x1 = []
y1 = []
x2 = []
y2 = []
cs = []

for _ in range(n):
    x, y, d, c = map(int, input().split())
    x1.append(x)
    x2.append(x+d+1)
    y1.append(y)
    y2.append(y+d+1)
    cs.append(c)


# x1-x2は線の始点と終点
def compress(x1, x2):
    xs = set()
    for i in range(n):
        for j in range(-1, 2):
            tx1, tx2 = x1[i]+j, x2[i]+j
            xs.add(tx1)
            xs.add(tx2)
    xs = sorted(xs)
    for i in range(n):
        x1[i] = bisect.bisect_left(xs, x1[i])
        x2[i] = bisect.bisect_left(xs, x2[i])
    return len(xs), xs


# print(x1)
# print(x2)

MAX_X, XS = compress(x1, x2)
MAX_Y, YS = compress(y1, y2)
# print(x1, y1)
# print(x2, y2)

fld = [[0]*MAX_Y for _ in range(MAX_X)]


for i in range(n):
    fld[x1[i]][y1[i]] += cs[i]
    fld[x2[i]][y2[i]] += cs[i]
    fld[x1[i]][y2[i]] -= cs[i]
    fld[x2[i]][y1[i]] -= cs[i]

for i in range(MAX_X-1):
    for j in range(MAX_Y-1):
        fld[i][j+1] += fld[i][j]

for j in range(MAX_Y-1):
    for i in range(MAX_X-1):
        fld[i+1][j] += fld[i][j]

# for row in fld:
#     print(row)

for _ in range(q):
    a, b = map(int, input().split())
    x = bisect.bisect_left(XS, a)
    y = bisect.bisect_left(YS, b)
    print(fld[x][y])

# # 2次元累積和を求めれば終わり
# # ただし、座標空間が広いので、座圧imosが必要
# import bisect
# from collections import defaultdict
# n, q = map(int, input().split())

# xy = defaultdict(int)
# for _ in range(n):
#     x, y, d, c = map(int, input().split())
#     xy[(x, y)] += c
#     xy[(x+d+1, y+d+1)] += c
#     xy[(x, y+d+1)] -= c
#     xy[(x+d+1, y)] -= c
# # print(xy)

# # print(sorted(xy.items()))
# # 出現した座標を圧縮してみる
# x_decom = defaultdict(int)
# y_decom = defaultdict(int)
# INF = 10**18
# x_decom[-INF] = 0
# y_decom[-INF] = 0


# x_origin, y_origin = zip(*xy.keys())
# x_origin, y_origin = map(lambda x: sorted(set(x)), (x_origin, y_origin))
# x_cnt = 1
# for x in x_origin:
#     x_decom[x] = x_cnt
#     x_cnt += 1
#     x_decom[x+1] = x_cnt
#     x_cnt += 1

# y_cnt = 1
# for y in y_origin:
#     y_decom[y] = y_cnt
#     y_cnt += 1
#     y_decom[y+1] = y_cnt
#     y_cnt += 1

# # print(x_decom, y_decom)

# MAP = [[0]*y_cnt for _ in range(x_cnt)]

# for (x, y), c in xy.items():
#     MAP[x_decom[x]][y_decom[y]] += c

# for i in range(x_cnt-1):
#     for j in range(y_cnt-1):
#         MAP[i][j+1] += MAP[i][j]

# for j in range(y_cnt-1):
#     for i in range(x_cnt-1):
#         MAP[i+1][j] += MAP[i][j]

# for row in MAP:
#     print(row)

# x_val = sorted(x_decom.keys())
# y_val = sorted(y_decom.keys())


# def decom(x, y):
#     xi = bisect.bisect_left(x_val, x)-1
#     yi = bisect.bisect_left(y_val, y)-1
#     x = x_decom[x_val[xi]]
#     y = y_decom[y_val[yi]]
#     print(xi, yi, x, y)
#     return x, y


# for _ in range(q):
#     a, b = map(int, input().split())
#     x, y = decom(a, b)
#     print(x, y)
#     print(MAP[x][y])

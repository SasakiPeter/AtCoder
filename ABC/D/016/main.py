class P:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __sub__(self, q):
        return P(self.x-q.x, self.y-q.y)

    def cross(self, q):
        return self.x*q.y-self.y*q.x


# ax, ay, bx, by = map(int, input().split())
# a, b = P(ax, ay), P(bx, by)
a, b = [P(x, y) for x, y in zip(*[map(int, input().split())]*2)]

n = int(input())
Points = [P(*map(int, input().split()))for _ in range(n)]
Points.append(Points[0])
cnt = 0
for p, q in zip(Points, Points[1:]):
    # 外積の正負を用いた線分の左右判定
    s = (q-p).cross(a-p)
    t = (q-p).cross(b-p)
    u = (b-a).cross(p-a)
    v = (b-a).cross(q-a)
    if s*t < 0 and u*v < 0:
        cnt += 1

    # s = (p.y-a.y)*(b.x-a.x)-(b.y-a.y)*(p.x-a.x)
    # t = (q.y-a.y)*(b.x-a.x)-(b.y-a.y)*(q.x-a.x)
    # u = (a.y-p.y)*(q.x-p.x)-(q.y-p.y)*(a.x-p.x)
    # v = (b.y-p.y)*(q.x-p.x)-(q.y-p.y)*(b.x-p.x)
    # # 両方確かめないとダメ
    # if s*t < 0 and u*v < 0:
    #     cnt += 1

print(cnt//2+1)

# ax, ay, bx, by = map(int, input().split())

# n = int(input())
# XY = [tuple(map(int, input().split()))for _ in range(n)]
# XY.append(XY[0])
# cnt = 0
# for xy1, xy2 in zip(XY, XY[1:]):
#     x1, y1 = xy1
#     x2, y2 = xy2
#     s = (y1-ay)*(bx-ax)-(by-ay)*(x1-ax)
#     t = (y2-ay)*(bx-ax)-(by-ay)*(x2-ax)
#     u = (ay-y1)*(x2-x1)-(y2-y1)*(ax-x1)
#     v = (by-y1)*(x2-x1)-(y2-y1)*(bx-x1)
#     # 両方確かめないとダメ
#     if s*t < 0 and u*v < 0:
#         cnt += 1

# print(cnt//2+1)


# ax, ay, bx, by = map(int, input().split())
# # 分母が負の時困る
# a = (by-ay)/(bx-ax)
# b = ay-a*ax
# # print('y=', a, 'x+', b)
# # x0, y0 = bx-ax, by-ay


# n = int(input())
# XY = [tuple(map(int, input().split()))for _ in range(n)]
# XY.append(XY[0])
# cnt = 0
# for xy1, xy2 in zip(XY, XY[1:]):
#     # print(xy1, xy2)
#     x1, y1 = xy1
#     x2, y2 = xy2
#     # # aを原点に平行移動
#     # x1, x2 = map(lambda x: x-ax, [x1, x2])
#     # y1, y2 = map(lambda y: y-ay, [y1, y2])

#     # if (0 < (x0*y1-x1*y0)) ^ (0 < (x0*y2-x2*y0)):
#     #     cnt += 1

#     y_1 = a*x1+b
#     y_2 = a*x2+b

#     # 反対も行うが、分母が負の時困る
#     a1 = (y2-y1)/(x2-x1)
#     b1 = y1-a1*x1
#     y_3 = a1*ax+b1
#     y_4 = a1*bx+b1

#     if (y_1-y1 < 0 and y_2-y2 > 0 or y_1-y1 > 0 and y_2-y2 < 0) and (y_3-ay < 0 and y_4-by > 0 or y_3-ay > 0 and y_4-by < 0):
#         cnt += 1

# print(cnt//2+1)

# import math as m
# ax, ay, bx, by = map(int, input().split())
# # 直線を求める
# a = (by-ay)/(bx-ax)
# b = ay-a*ax
# theta = m.atan(a)
# # print(a, b, theta)
# n = int(input())
# XY = []
# for _ in range(n):
#     x, y = map(int, input().split())
#     # 切片の分だけ平行移動
#     y -= b
#     # 回転
#     x, y = m.cos(-theta)*x-m.sin(-theta)*y, m.sin(-theta)*x+m.cos(-theta)*y
#     XY.append((x, y))
# # print(XY)


# # 頭とお尻をつなげる
# XY.append(XY[0])

# cnt = 0
# is_posi = (0 <= XY[0][1])+0
# for x, y in XY[1:]:
#     if is_posi ^ (0 <= y)+0:
#         cnt += 1
#     # print(is_posi, y, 0 <= y, cnt)
#     is_posi = (0 <= y)+0
# print(cnt//2+1)

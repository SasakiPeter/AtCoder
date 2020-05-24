import math


class P:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __sub__(self, q):
        return P(self.x-q.x, self.y-q.y)

    def length(self):
        return (self.x**2+self.y**2)**.5


a, b, h, m = map(int, input().split())
minutes = 60*h+m
h_deg = minutes/2 % 360
m_deg = minutes*6 % 360
v1 = P(a*math.cos(math.radians(h_deg)), a*math.sin(math.radians(h_deg)))
v2 = P(b*math.cos(math.radians(m_deg)), b*math.sin(math.radians(m_deg)))
print("{:.10f}".format((v1-v2).length()))


# import math
# a, b, h, m = map(int, input().split())
# minutes = 60*h+m
# h_deg = minutes/2 % 360
# m_deg = minutes*6 % 360
# deg = h_deg-m_deg
# print((a**2+b**2-2*a*b*math.cos(math.radians(deg)))**.5)

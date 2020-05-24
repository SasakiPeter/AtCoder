import math as m
a, b, h, min = map(int, input().split())

minutes = 60*h+min

degree_long = minutes*.5
degree_short = minutes*6 % 360


class P:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __sub__(self, q):
        return P(self.x-q.x, self.y-q.y)

    def length(self):
        return m.sqrt(self.x**2+self.y**2)


v1 = P(a*m.cos(m.radians(degree_long)), a*m.sin(m.radians(degree_long)))
v2 = P(b*m.cos(m.radians(degree_short)), b*m.sin(m.radians(degree_short)))

v3 = v1-v2
print(v3.length())

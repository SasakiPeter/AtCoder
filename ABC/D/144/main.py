import math as m
a, b, x = map(int, input().split())
h = 2*(b - x/(a**2))
# print(h)
# print(x/(a**2))
if h < b:
    print(m.degrees(m.atan(h/a)))
else:
    w = 2*x/(a*b)
    print(90 - m.degrees(m.atan(w/b)))

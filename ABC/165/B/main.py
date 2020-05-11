# import math as m
x = int(input())
# t = (m.log10(x)-2) // m.log10(1.01)
# print(t)
y = 100
cnt = 0
while y < x:
    y = 101*y//100
    cnt += 1
print(cnt)

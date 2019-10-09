x, y, z = map(int, input().split())
# x >= a*y + (a+1)*z　を満たす最大のa
# (x-z)/(y+z) >= a
print((x-z)//(y+z))

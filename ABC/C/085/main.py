n, Y = map(int, input().split())
Y //= 1000

for x in range(n+1):
    y = (Y-n-9*x)//4
    z = n-x-y
    if z < 0 or y < 0 or x+y+z != n:
        continue
    if 10*x+5*y+z == Y:
        print(x, y, z)
        exit()
else:
    print(-1, -1, -1)

# n, Y = map(int, input().split())
# a = 10000
# b = 5000
# c = 1000

# for x in range(n+1):
#     for y in range(n+1):
#         z = n-x-y
#         if z < 0:
#             continue
#         if a*x+b*y+c*z == Y:
#             print(x, y, z)
#             exit()
# else:
#     print(-1, -1, -1)

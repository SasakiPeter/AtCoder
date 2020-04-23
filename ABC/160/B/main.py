x = int(input())
y, r = divmod(x, 500)
z, r = divmod(r, 5)
print(y*1000+z*5)

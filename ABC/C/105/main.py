n = int(input())
s = ''
while n != 0:
    div, mod = divmod(n, 2)
    s = str(mod)+s
    n = -div
print(s or 0)

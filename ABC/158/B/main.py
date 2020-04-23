n, a, b = map(int, input().split())
div, mod = divmod(n, (a+b))
print(div*a + [mod, a][mod > a])

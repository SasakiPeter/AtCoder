a, b, c, d = map(int, input().split())
n = -(-c//b)
m = -(-a//d)
if n <= m:
    print('Yes')
else:
    print('No')

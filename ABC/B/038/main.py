# h, w = map(int, input().split())
# h2, w2 = map(int, input().split())
# print('YES' if h == h2 or h == w2 or w == h2 or w == w2 else 'NO')

r1 = input().split()
r2 = input().split()

print('YES' if any(x == y for x in r1 for y in r2) else 'NO')

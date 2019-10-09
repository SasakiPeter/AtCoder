l, h = map(int, input().split())
n = int(input())
a = [int(input()) for _ in range(n)]
# b = (-1 if x > h else 0 if l <= x <= h else l-x for x in a)
# for y in b:
#     print(y)

print(*(-1 if x > h else 0 if l <= x <= h else l-x for x in a), sep='\n')

n, l = map(int, input().split())
s = sorted(input() for _ in range(n))
print(''.join(s))
# s = [input() for _ in range(n)]
# print(''.join(sorted(s)))
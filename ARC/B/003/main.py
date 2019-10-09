n = int(input())
s = sorted(input()[::-1] for _ in range(n))
print(*(x[::-1] for x in s), sep='\n')

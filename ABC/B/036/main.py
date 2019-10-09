# n = int(input())
# m = [input() for _ in range(n)][::-1]
# for row in zip(*m):
#     print(*row, sep='')


n = int(input())
print(*(''.join(r) for r in zip(*[input() for _ in range(n)][::-1])), sep='\n')

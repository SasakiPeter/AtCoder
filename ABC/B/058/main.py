o, e = [input() for _ in range(2)]
print(''.join(x+y for x, y in zip(o, e+" ")))

s, t = [input() for _ in range(2)]
print(sum(x==y for x, y in zip(s, t)))

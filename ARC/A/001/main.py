n = int(input())
c = input()
ls = sorted(c.count(s) for s in '1234')
# print(ls[-1], ls[0])

# お前は天才か？
print(*ls[::-3])

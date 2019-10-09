s = input()
a, b, c, d = map(int, input().split())
ls = [s[0:a], s[a:b], s[b:c], s[c:d], s[d:]]
print('"'.join(ls))

# お尻から順番に挿入していくのもあり
# s = list(input())
# ls = list(map(int, input().split()))
# [s.insert(x, '"') for x in ls[::-1]]
# print(*s, sep="")

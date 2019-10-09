l, h = map(int, input().split())
# ans = 0
# for x in range(l, h+1):
#     x = str(x)
#     ans += [0, 1][x == x[::-1]]
# print(ans)


# print(sum(1 if str(x) == str(x)[::-1] else 0 for x in range(l, h+1)))


# sumでTrue扱えるんだ！！！
# strは無理なのに
print(sum(x == x[::-1] for x in map(str, range(l, h+1))))

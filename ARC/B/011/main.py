n = int(input())
*s, = map(lambda s: s.lower(), input().split())
# print(s)
table = "zrbcdwtjfqlvsxpmhkng"
ans = []
for w in s:
    num = ""
    for c in w:
        if c in table:
            num += str(table.index(c)//2)
    if num:
        ans.append(num)

if ans:
    print(*ans)
else:
    print()

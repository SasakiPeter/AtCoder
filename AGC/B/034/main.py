s = input().replace('BC', 'o').replace('B', 'x').replace('C', 'x')
# print(s)

ans = cnt = 0
for c in s[::-1]:
    if c == 'x':
        cnt = 0
        continue
    elif c == 'o':
        cnt += 1
    else:
        ans += cnt
print(ans)

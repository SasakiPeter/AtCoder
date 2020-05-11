n, L = map(int, input().split())
s = input()
cnt = 1
ans = 0
for c in s:
    if c == '+':
        cnt += 1
    else:
        cnt -= 1
    if L < cnt:
        ans += 1
        cnt = 1
print(ans)

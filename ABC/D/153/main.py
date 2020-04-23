h = int(input())
ans = 0
cnt = 1
while h:
    h = h//2
    ans += cnt
    cnt *= 2
print(ans)

s = input()

ans = ""
prev = ""
cnt = 1
for c in s:
    if prev != c:
        ans += prev + str(cnt)
        prev = c
        cnt = 1
    else:
        cnt += 1
ans += prev + str(cnt)

print(ans[1:])

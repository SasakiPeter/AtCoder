s = input().split('+')
cnt = 0
for c in s:
    if "0" not in c:
        cnt += 1
print(cnt)

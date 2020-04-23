n = int(input())
ans = 0

for i in range(n+1):
    if i % 15 == 0:
        pass
    elif i % 3 == 0 or i % 5 == 0:
        pass
    else:
        ans += i
print(ans)

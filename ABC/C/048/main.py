n, x = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(n):
    if i != 0:
        y = A[i-1]+A[i]
    else:
        y = A[i]
    if y <= x:
        continue
    ans += y-min(x, y)
    A[i] -= y-min(x, y)
print(ans)

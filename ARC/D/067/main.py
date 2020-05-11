n, a, b = map(int, input().split())
X = list(map(int, input().split()))
ans = 0
for x, y in zip(X, X[1:]):
    ans += min((y-x)*a, b)
print(ans)

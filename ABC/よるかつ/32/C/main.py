n = int(input())
X = list(map(int, input().split()))
X_sort = sorted(X)
L, R = X_sort[n//2-1], X_sort[n//2]
M = (L+R)/2
for x in X:
    if x < M:
        print(R)
    else:
        print(L)

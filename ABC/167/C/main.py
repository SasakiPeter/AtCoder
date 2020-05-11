from itertools import product
n, m, X = map(int, input().split())
ca = [tuple(map(int, input().split()))for _ in range(n)]
INF = 10**18
ans = INF
for x in product([0, 1], repeat=n):
    cost = 0
    ms = [0]*m
    for i in range(n):
        if x[i] == 0:
            continue
        c, *a = ca[i]
        cost += c
        for j in range(m):
            ms[j] += a[j]

    if all(X <= y for y in ms) and cost < ans:
        ans = cost


print(ans if ans != INF else -1)

from itertools import product
n = int(input())
As = {}
for i in range(n-1):
    A = map(int, input().split())
    for j, a in enumerate(A):
        As[(i, j+i+1)] = a
INF = 10**18
ans = -INF
for bit in product((0, 1, 2), repeat=n):
    cnt = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if bit[i] == bit[j]:
                cnt += As[(i, j)]
    if ans < cnt:
        ans = cnt
print(ans)

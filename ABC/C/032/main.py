# 尺取
n, k = map(int, input().split())
A = []
for _ in range(n):
    s = int(input())
    A.append(s)
    if s == 0:
        print(n)
        exit()

ans = R = 0
X = 1
for L in range(n):
    # 尺取っていって、伸ばせなくなって、Rを増やすまでが尺取
    if R < L:
        R += 1
    while R < n and X*A[R] <= k:
        X *= A[R]
        R += 1
    ans = max(ans, R-L)
    # print(L, R, X)
    if L != R:
        X //= A[L]
print(ans)

n = int(input())
A = [tuple(map(int, input().split()))for _ in range(2)]

# どこで曲がるかを全探索
ans = 0
for k in range(1, n+1):
    cnt = sum(A[0][:k])+sum(A[1][k-1:])
    if ans < cnt:
        ans = cnt
print(ans)

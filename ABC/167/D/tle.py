n, k = map(int, input().split())
A = list(map(lambda x: int(x)-1, input().split()))

ans = 0
for _ in range(k):
    ans = A[ans]
print(ans+1)

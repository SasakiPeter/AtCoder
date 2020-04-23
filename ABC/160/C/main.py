k, n = map(int, input().split())
A = list(map(int, input().split()))

# 最も距離が離れているところを見ればいい

dist = 0
for x, y in zip(A, A[1:]):
    dist = max(dist, y-x)

dist = max(dist, A[0]+k-A[-1])

print(k-dist)

k, t = map(int, input().split())
*A, MAX = sorted(map(int, input().split()))
print(max(MAX-sum(A)-1, 0))

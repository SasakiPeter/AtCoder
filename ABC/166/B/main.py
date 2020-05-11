n, k = map(int, input().split())
s = set()
for _ in range(k):
    d = int(input())
    A = list(map(int, input().split()))
    s |= set(A)

print(n-len(s))

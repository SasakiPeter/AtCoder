from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))
L = defaultdict(int)
R = defaultdict(int)
for i, a in enumerate(A):
    L[a+i] += 1
    R[i-a] += 1
ans = 0
for k, v in L.items():
    ans += v*R[k]
print(ans)

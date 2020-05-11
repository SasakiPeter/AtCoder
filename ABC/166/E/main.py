from collections import Counter
n = int(input())
A = list(map(int, input().split()))
B = [i+a for i, a in enumerate(A)]
C = [j-a for j, a in enumerate(A)]

bc = Counter(B)
cc = Counter(C)

ans = 0
for k, v in bc.items():
    ans += v*cc[k]
print(ans)

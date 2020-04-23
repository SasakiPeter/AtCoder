from collections import Counter
from operator import mul
n = int(input())
s = input()
c = Counter(s)
# print(c)
if n < 3:
    print(0)
    exit()
elif len(c.keys()) < 3:
    print(0)
    exit()
ans = 0
for i in range(n):
    x = s[i]
    ans += mul(*[v for k, v in c.items()if k != x])
    c[x] -= 1
    for j in range(i+1, n):
        y = s[j]
        if x == y:
            continue
        idx_diff = j-i
        if n <= j+idx_diff:
            continue
        z = s[j+idx_diff]
        if x != z and y != z:
            ans -= 1
print(ans)

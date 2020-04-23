from collections import Counter
n = int(input())
A = list(map(int, input().split()))
c = Counter(A)
s = sum(v*(v-1)//2 for v in c.values())
# print(s)
# ans = 0
for a in A:
    x = c[a]
    ans = s-x*(x-1)//2+(x-1)*(x-2)//2
    print(ans)

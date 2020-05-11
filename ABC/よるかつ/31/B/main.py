from collections import Counter
n = int(input())
A = list(map(int, input().split()))
c = Counter(A)
ans = 0
for i in range(10**5):
    cnt = c[i-1]+c[i]+c[i+1]
    if ans < cnt:
        ans = cnt
print(ans)

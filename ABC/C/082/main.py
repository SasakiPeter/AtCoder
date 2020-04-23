from collections import Counter

n = int(input())
c = Counter(map(int, input().split()))
ans = 0
for k, v in c.items():
    if k <= v:
        ans += v-k
    else:
        ans += v
print(ans)

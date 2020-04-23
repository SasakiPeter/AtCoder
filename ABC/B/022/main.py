from collections import defaultdict
n = int(input())
dd = defaultdict(int)
for _ in range(n):
    a = int(input())
    dd[a] += 1
print(sum(v-1 for v in dd.values()))

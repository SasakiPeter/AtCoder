from collections import defaultdict

n, k = map(int, input().split())


dd = defaultdict(int)

for _ in range(n):
    a, b = map(int, input().split())
    dd[a] += b

cnt = 0
for key, v in sorted(dd.items()):
    cnt += v
    if k <= cnt:
        print(key)
        break

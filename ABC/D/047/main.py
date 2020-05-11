from collections import defaultdict
n, _ = map(int, input().split())
A = list(map(int, input().split()))

MAX_S = []
max_s = 0
for a in A[::-1]:
    if max_s < a:
        max_s = a
    MAX_S.append(max_s)
MAX_S = MAX_S[::-1]
cnt = defaultdict(int)
for a, s in zip(A, MAX_S):
    cnt[s-a] += 1

print(sorted(cnt.items(), reverse=True)[0][1])

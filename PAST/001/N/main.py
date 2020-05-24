from collections import defaultdict
n, w, c = map(int, input().split())
# 座圧imos
cnt = defaultdict(int)
for _ in range(n):
    L, R, P = map(int, input().split())
    cnt[max(L-c+1, 0)] += P
    if w-c < R:
        continue
    cnt[R] -= P

INF = 10**18
ans = INF
tmp = 0
cnt[0] += 0
# cnt[w-c+1] += INF
for k, v in sorted(cnt.items()):
    tmp += v
    if tmp < ans:
        ans = tmp
print(ans)

from itertools import combinations_with_replacement
n, m, q = map(int, input().split())
abcd = [tuple(map(int, input().split()))for _ in range(q)]
ans = 0
for x in combinations_with_replacement(range(1, m+1), n):
    cnt = 0
    for a, b, c, d in abcd:
        if x[b-1]-x[a-1] == c:
            cnt += d
    if ans < cnt:
        ans = cnt

print(ans)

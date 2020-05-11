from itertools import product
n = int(input())

F = [tuple(map(int, input().split()))for _ in range(n)]
# i番目の店と、お姉ちゃんの店がやっている個数に対応して利益
P = [tuple(map(int, input().split()))for _ in range(n)]
INF = 10**18
ans = -INF
for schedule in product([0, 1], repeat=10):
    if 1 not in schedule:
        continue
    p_sum = 0
    for i, f in enumerate(F):
        cnt = 0
        for x, y in zip(schedule, f):
            if x == y == 1:
                cnt += 1
        p_sum += P[i][cnt]
    if ans < p_sum:
        ans = p_sum
print(ans)

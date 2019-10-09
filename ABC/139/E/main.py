import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
a = {i+1: list(map(int, input().split())) for i in range(n)}

ans = 1
while all(val != [] for val in a.values()):
    cache = []
    for i in range(1, n+1):
        if i in cache or a[i][0] in cache:
            continue
        if a[i] == []:
            continue
        if a[a[i][0]] == []:
            continue
        if i == a[a[i][0]][0]:
            r = a[i].pop(0)
            cache.append(r)
            cache.append(a[r].pop(0))
    if cache == []:
        ans = -1
        break
    else:
        cache = []
    ans += 1

print(ans)

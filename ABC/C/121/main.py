import sys
input = sys.stdin.readline
n, m = map(int, input().split())
# ab = [(a, b) for a, b in map(int, input().split()) for _ in range(n)]
# ab.sort()
# ab = []
# for _ in range(n):
#     a, b = map(int, input().split())
#     ab.append((a, b))
# ab.sort()

ab = [tuple(map(int, input().split())) for _ in range(n)]
ab.sort()

# print(ab)
ans = 0
for a, b in ab:
    # buy = [m, b][0 <= m-b]
    buy = min(m, b)
    m -= buy
    ans += a*buy
print(ans)

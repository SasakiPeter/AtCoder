n, t = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
ls = [a for a, b in s if b <= t]
print('TLE' if len(ls) == 0 else min(ls))

import bisect
n, m = map(int, input().split())
Ps = [[]for _ in range(n)]
PY = []
for _ in range(m):
    p, y = map(int, input().split())
    Ps[p-1].append(y)
    PY.append((p, y))

for ls in Ps:
    ls.sort()

for p, y in PY:
    pid = "{:06}".format(p)
    cid = "{:06}".format(bisect.bisect_right(Ps[p-1], y))
    print(pid+cid)

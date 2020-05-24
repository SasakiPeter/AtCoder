s, t = map(lambda x: int(x.replace('B', '-').replace('F', '')), input().split())

if s < 0:
    s += 1
if t < 0:
    t += 1
if t < s:
    s, t = t, s
print(t-s)

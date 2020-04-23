X, Y, a, b, c = map(int, input().split())
p = sorted(map(int, input().split()))
q = sorted(map(int, input().split()))
r = sorted(map(int, input().split()))

at = p.pop()
bt = q.pop()
ct = r.pop()
ans = 0
x = y = 0
z = 0
while True:
    if X == x and Y == y or (x+y+z == X+Y):
        break
    if X == x:
        continue
    else:
        if at >= ct:
            ans += at
            if p:
                at = p.pop()
            else:
                at = -1
            x += 1
            continue
        else:
            ans += ct
            if r:
                ct = r.pop()
            else:
                ct = -1
            z += 1
            continue
    if Y == y:
        continue
    else:
        if bt >= ct:
            ans += bt
            if q:
                bt = q.pop()
            else:
                bt = -1
            x += 1
            continue
        else:
            ans += ct
            if r:
                ct = r.pop()
            else:
                ct = -1
            z += 1
            continue

print(ans)

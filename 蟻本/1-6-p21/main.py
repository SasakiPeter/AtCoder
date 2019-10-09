n = int(input())
a = sorted(map(int, input().split()))[::-1]
# 計算量 nC3が最小 O(n**3)
ans = 0
for x in a:
    if not ans == 0:
        break
    for y in a:
        if not ans == 0:
            break
        if not x > y:
            continue
        for z in a:
            if not y > z:
                continue
            if x < y+z:
                ans = x+y+z
                break

print(ans)

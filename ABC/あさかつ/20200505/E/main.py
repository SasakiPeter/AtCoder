a, b, c, d, e, f = map(int, input().split())

water = [0]*(f+1)
suger = [0]*(f+1)
water[0] = 1
suger[0] = 1
for i in range(f+1):
    if water[i]:
        if i+100*a <= f:
            water[i+100*a] = 1

        if i+100*b <= f:
            water[i+100*b] = 1
    if suger[i]:
        if i+c <= f:
            suger[i+c] = 1
        if i+d <= f:
            suger[i+d] = 1

water_ls = [i for i in range(f+1) if water[i]]
suger_ls = [i for i in range(f+1) if suger[i]]

suger_water = []
# max_c = 100*e/(100+e)
# productしてええんやで
for w in water_ls:
    for s in suger_ls:
        if f < w+s:
            continue
        if w+s == 0:
            continue
        if s*(100+e) <= e*(w+s):
            c = 100*s/(w+s)
            suger_water.append((c, w, s))

suger_water.sort(reverse=True)
max_c, w, s = suger_water[0]
print(w+s, s)

import itertools

A, B, C, D, E, F = map(int, input().split())

WF = F//100+1

water = [False] * (WF+1+30)
sugar = [False] * (F+1+30)

water[0] = True
sugar[0] = True

for n in range(WF):
    if water[n]:
        water[n+A] = True
        water[n+B] = True
for n in range(F):
    if sugar[n]:
        sugar[n+C] = True
        sugar[n+D] = True

water = set(100*x for x in range(1, 1+WF) if water[x])
sugar = set(x for x in range(1+F) if sugar[x])

# at most 30 * 3000なので全てやる
ans_per = -1
for w, s in itertools.product(water, sugar):
    if w//100*E < s:
        continue
    if w+s > F:
        continue
    x = s/(w+s)
    if x > ans_per:
        ans_per = x
        ans_w = w
        ans_s = s

print(ans_w + ans_s, ans_s)

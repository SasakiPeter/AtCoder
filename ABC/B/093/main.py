a, b, k = map(int, input().split())
# ここを[x for x in range(a, b+1)]にするとTLE
r = range(a, b + 1)
for x in sorted(set(r[:k]) | set(r[-k:])):
    print(x)

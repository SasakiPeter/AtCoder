n, q = map(int, input().split())
s = [0 for _ in range(n)]
for _ in range(q):
    l, r, t = map(int, input().split())
    # これだと汎用性がない
    # s[l-1:r] = [t for _ in range(r-l+1)]

    for i in range(l-1, r):
        s[i] = t

# for x in s:
#     print(x)

# この方がかっこい
print(*s, sep='\n')

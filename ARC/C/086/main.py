from collections import Counter
n, k = map(int, input().split())
*a, = map(int, input().split())

c = Counter(a)
# kv = sorted(c.items(), key=lambda x: x[1], reverse=True)

if n <= k:
    print(0)
else:
    ls = c.most_common(k)
    ans = n
    for k, v in ls:
        ans -= v

    print(ans)


# from collections import Counter
# n, k = map(int, input().split())
# A = list(map(int, input().split()))
# d = Counter(A)

# ls = sorted(d.values())
# ans = 0
# for v in ls[:len(ls)-k]:
#     ans += v
# print(ans)

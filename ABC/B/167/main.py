a, b, c, k = map(int, input().split())
ans = min(a, k)
k -= min(a, k)

ans += min(b, k)*0
k -= min(b, k)

ans += min(c, k)*(-1)
k -= min(c, k)

print(ans)


# a, b, c, k = map(int, input().split())
# if k <= a+b:
#     print(min(k, a))
# else:
#     print(2*a-k+b)

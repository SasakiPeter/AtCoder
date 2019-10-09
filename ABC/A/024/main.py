a, b, c, k = map(int, input().split())
s, t = map(int, input().split())
# print(s*a+t*b-min(1, (s+t)//k)*c*(s+t))

# これでもいい
print(s*a+t*b-(s+t >= k)*c*(s+t))

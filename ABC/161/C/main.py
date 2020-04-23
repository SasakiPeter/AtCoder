n, k = map(int, input().split())
a = abs(n % k)
a = min(a, k-a)
print(a)

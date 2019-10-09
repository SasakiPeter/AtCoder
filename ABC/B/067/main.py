n, k = map(int, input().split())
s = sorted(map(int, input().split()))[::-1]
print(sum(s[:k]))

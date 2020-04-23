n, m = map(int, input().split())
s = sum(map(int, input().split()))
if n-s < 0:
    print(-1)
else:
    print(n-s)

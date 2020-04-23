n = int(input())

if n == 0:
    print(0)
elif n % 2 != 0:
    print(0)
else:
    ans = 0
    for i in range(1, 100):
        ans += n//((5**i)*2)
    print(ans)

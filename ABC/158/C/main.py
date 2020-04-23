a, b = map(int, input().split())

INF = 10**4

for i in range(INF):
    x = i*8//100
    y = i*10//100

    if x == a and y == b:
        print(i)
        break
else:
    print(-1)

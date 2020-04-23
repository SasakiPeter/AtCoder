n, k = map(int, input().split())
d = list(map(int, input().split()))

for i in range(n, 10*n+1):
    for x in d:
        if str(x) in str(i):
            break
    else:
        print(i)
        break

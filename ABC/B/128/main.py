n = int(input())
s = {i+1: tuple(input().split()) for i in range(n)}
for k, v in sorted(s.items(), key=lambda x: (x[1][0], -int(x[1][1]))):
    print(k)

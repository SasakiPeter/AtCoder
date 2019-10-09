n = int(input())
a = sorted(set(int(input()) for _ in range(n)))
print(a[-2])

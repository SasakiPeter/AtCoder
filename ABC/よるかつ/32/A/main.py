n = int(input())
SP = []
for i in range(n):
    s, p = input().split()
    SP.append((s, int(p), i+1))
SP.sort(key=lambda x: x[1], reverse=True)
SP.sort(key=lambda x: x[0])
for s, p, i in SP:
    print(i)

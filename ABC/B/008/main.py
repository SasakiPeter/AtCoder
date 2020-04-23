from collections import defaultdict
n = int(input())
dd = defaultdict(int)
for _ in range(n):
    s = input()
    dd[s] += 1
print(sorted(dd.items(), key=lambda ls: ls[1], reverse=True)[0][0])

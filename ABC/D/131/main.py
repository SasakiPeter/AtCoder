import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]
ab.sort(key=lambda x: x[1])
# print(ab)

time = 0
for a, limit in ab:
    time += a
    if limit < time:
        print("No")
        break
else:
    print("Yes")

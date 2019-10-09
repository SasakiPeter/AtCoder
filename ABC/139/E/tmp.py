from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())

# O(n**3)までOK
# a = {i+1: list(map(int, input().split())) for i in range(n)}
a = [deque(int(x) - 1 for x in row.split()) for row in sys.stdin.readlines()]

for i in range(n):
    a[i].append(-1)
a.append([-1])
print(a)


def f():
    # 相思相愛な対戦を検索
    can_use = [i for i in range(n) if a[a[i][0]][0] == i]
    for x in can_use:
        a[x].popleft()
    return len(can_use)
# if i == a[a[i][0]][0]


answer = 0

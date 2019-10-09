import sys
from math import floor
from heapq import heappush, heappop, heappushpop
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


# 10**5
n, m = map(int, input().split())
# 10**9
a = sorted(map(lambda s: -int(s), input().split()))


for _ in range(m):
    x = heappop(a)
    heappush(a, x/2)

print(sum(map(lambda x: floor(-x), a)))


# popするときは、先頭のを取り出す
# pushするときは、ソートを行う

import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, k, q = map(int, input().split())
dd = defaultdict(int)
for _ in range(q):
    dd[int(input())] += 1
# a = [int(input()) for _ in range(q)]

border = q-k+1
for i in range(1, n+1):
    if dd[i] >= border:
        print('Yes')
    else:
        print('No')

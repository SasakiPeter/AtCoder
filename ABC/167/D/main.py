#!/usr/bin/env python3
from collections import Counter
import sys
sys.setrecursionlimit(10**7)
n, k = map(int, input().split())
A = list(map(lambda x: int(x)-1, input().split()))

# A[0]から出発して何回でループするか数える

visited = [0]*n


def dfs(v):
    if visited[v]+1 == 3:
        return 0
    visited[v] += 1
    dfs(A[v])


dfs(0)

c = Counter(visited)
loop_cnt = c[2]
init_cnt = c[1]
k_ = k-init_cnt
k_ %= loop_cnt
# print(n, k)
# for i in range(n):
#     print(i, A[i])


cnt = 0
visited = [0]*n


ans = 0
loop = k if k < init_cnt else k_+init_cnt
# print(loop)
for _ in range(loop):
    ans = A[ans]
print(ans+1)

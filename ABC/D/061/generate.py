#!/usr/bin/env python3
import random
try_again = 1
while try_again:
    n = random.randint(2, 1000)
    m = min(n*(n-1), random.randint(1, 2000))
    ab = set([])
    cnt = 0
    while len(ab) == m:
        if cnt:
            a = 1
        else:
            a = random.randint(1, n)
        if not cnt:
            b = n
        else:
            b = random.randint(1, n)
        if a == b:
            continue
        ab |= {(a, b)}
        cnt ^= 1

    edges = [[] for _ in range(n)]
    for a, b in ab:
        edges[a-1].append(b-1)

    stack = [0]
    visited = [0]*n
    while stack:
        v = stack.pop()
        if visited[v]:
            continue
        visited[v] = 1
        for v2 in edges[v]:
            if visited[v2]:
                continue
            stack.append(v2)

    if visited[-1]:
        try_again = 0

print(n, m)
for a, b in ab:
    c = random.randint(-10**9, 10**9)
    print(a, b, c)

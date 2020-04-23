import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


class UnionFind:
    def __init__(self, n):
        self.p = [-1]*n

    def find(self, x):
        if self.p[x] == -1:
            return x
        else:
            self.p[x] = self.find(self.p[x])
            return self.p[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.p[rx] = ry


n, q = map(int, input().split())
uf = UnionFind(n)

for _ in range(q):
    p, a, b = map(int, input().split())
    if p == 0:
        uf.union(a, b)
    else:
        print("Yes" if uf.find(a) == uf.find(b) else "No")

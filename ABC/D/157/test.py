import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n, m, k = map(int, input().split())


class UnionFind:
    def __init__(self, n):
        self.p = [-1]*n
        self.r = [1]*n

    def find(self, x):
        if self.p[x] < 0:
            return x
        else:
            self.p[x] = self.find(self.p[x])
            return self.p[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            if self.r[rx] > self.r[ry]:
                rx, ry = ry, rx
            if self.r[rx] == self.r[ry]:
                self.r[ry] += 1
            self.p[ry] += self.p[rx]
            self.p[rx] = ry

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def count_member(self, x):
        return -self.p[self.find(x)]


uf = UnionFind(n)
ab = []
cd = []

for _ in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    ab.append((a, b))
    uf.union(a, b)

for _ in range(k):
    c, d = map(lambda x: int(x)-1, input().split())
    cd.append((c, d))

ans = [uf.count_member(i)-1 for i in range(n)]

for a, b in ab:
    if uf.same(a, b):
        ans[a] -= 1
        ans[b] -= 1

for c, d in cd:
    if uf.same(c, d):
        ans[c] -= 1
        ans[d] -= 1

print(*ans)

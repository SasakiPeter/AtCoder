import sys
input = sys.stdin.readline
n, m = map(int, input().split())
P = list(map(int, input().split()))


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


uf = UnionFind(n)
for _ in range(m):
    x, y = list(map(lambda x: int(x)-1, input().split()))
    uf.union(x, y)

ans = 0
for i in range(n):
    p = P[i]
    # p-1とiが同じ親ならカウント
    if uf.same(p-1, i):
        ans += 1
print(ans)

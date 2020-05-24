import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n, m = map(int, input().split())
edges_origin = []
edges_adj = [[]for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges_origin.append((c, a, b))
    edges_adj[a].append((c, b))
    edges_adj[b].append((c, a))
edges = sorted(edges_origin)


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
used_edge = defaultdict(int)
mw = 0
for w, v, v2 in edges:
    if uf.same(v, v2):
        continue
    uf.union(v, v2)
    mw += w
    if v2 < v:
        v, v2 = v2, v
    used_edge[(v, v2)] = w

# print(used_edge)

for w, v, v2 in edges_origin:
    if v2 < v:
        v, v2 = v2, v
    if used_edge[(v, v2)]:
        print(mw)
    else:
        # print(v, v2)
        heavy_w = 0
        for v_ in (v, v2):
            for w2, v_to in edges_adj[v_]:
                # きれないへんが存在する
                # それは、v3へのへんが、v_からしか
                # 伸びていないとき
                v_from = v_
                is_ok = True
                for i in range(n):
                    if i == v_from:
                        continue
                    if used_edge[(v_from, i)]:
                        break
                    if used_edge[(i, v_from)]:
                        break
                else:
                    is_ok = False

                if not is_ok:
                    break

                if v_to < v_from:
                    v_from, v_to = v_to, v_from
                if used_edge[(v_from, v_to)]:
                    if heavy_w < w2:
                        heavy_w = w2

        print(mw-heavy_w+w)

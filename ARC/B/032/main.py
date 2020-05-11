# Unionfind
import sys
input = sys.stdin.readline
n, m = map(int, input().split())


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

    def count_members(self, x):
        return -self.p[self.find(x)]

    def count_roots(self):
        return sum(p < 0 for p in self.p)


uf = UnionFind(n)

for _ in range(m):
    a, b = list(map(lambda x: int(x)-1, input().split()))
    uf.union(a, b)


print(uf.count_roots() - 1)

# # 閉路の数-1
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)
# n, m = map(int, input().split())
# edges = [[] for _ in range(n)]
# for _ in range(m):
#     a, b = list(map(lambda x: int(x)-1, input().split()))
#     edges[a].append(b)
#     edges[b].append(a)


# visited = [0]*n


# def dfs(v, parent):
#     if visited[v]:
#         return
#     visited[v] = 1
#     for v2 in edges[v]:
#         if visited[v2]:
#             continue
#         dfs(v2, v)


# cnt = 0
# for v in range(n):
#     if visited[v]:
#         continue
#     dfs(v, -1)
#     cnt += 1
# print(cnt-1)

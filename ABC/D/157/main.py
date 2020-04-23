import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m, k = map(int, input().split())
# FRIENDS = [[0]*n for _ in range(n)]


# 案として、rootの値が集合の数に-1かけたものになるように管理すると強い
class UnionFind:
    def __init__(self, n):
        self.p = [-1]*n
        self.c = None

    def find(self, x):
        if self.p[x] < 0:
            return x
        else:
            self.p[x] = self.find(self.p[x])
            return self.p[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.p[ry] += self.p[rx]
            self.p[rx] = ry

    def count_member(self, x):
        return -self.p[self.find(x)]


uf = UnionFind(n)

ab = []
for i in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    # FRIENDS[a][b] = FRIENDS[b][a] = 1
    ab.append((a, b))
    uf.union(a, b)

cd = [list(map(lambda x: int(x)-1, input().split())) for _ in range(k)]

ans = [uf.count_member(i)-1 for i in range(n)]


for a, b in ab:
    if uf.find(a) == uf.find(b):
        ans[a] -= 1
        ans[b] -= 1

for c, d in cd:
    if uf.find(c) == uf.find(d):
        ans[c] -= 1
        ans[d] -= 1

print(*ans)


# for i in range(n):
#     # ここがO(N**2)になってる
#     c_friends = sum(FRIENDS[i])
#     c_member = uf.count_member(i)
#     ans.append(c_member - c_friends - 1)

# for i in range(n):
#     # この時点ですでにO(n**2)
#     c_friends = sum(FRIENDS[i])
#     blocks = BLOCKS[i]
#     c_member = uf.count_member(i)
#     # print(c_friends, c_member)
#     # print(blocks)
#     # # blockの人と同じ親を持つか判定
#     # # これ、もっと短くできる
#     c_blocks = 0
#     for j, b in enumerate(blocks):
#         if b:
#             # print(uf.find(i), uf.find(j), "hello", i, j)
#             if uf.find(i) == uf.find(j):
#                 c_blocks += 1
#     ans.append(c_member - 1 - c_friends - c_blocks)

# print(*ans)


# DFS
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)

# n, m, k = map(int, input().split())

# FRIEND = [[0]*n for _ in range(n)]
# BLOCK = [[0]*n for _ in range(n)]

# for _ in range(m):
#     a, b = map(lambda x: int(x)-1, input().split())
#     FRIEND[a][b] = FRIEND[b][a] = 1

# for _ in range(k):
#     a, b = map(lambda x: int(x)-1, input().split())
#     BLOCK[a][b] = BLOCK[b][a] = 1

# # FRIENDが連結しているかつ、BLOCKにないかつ、直接つながっていない


# def make_dfs():
#     visited = [0] * n

#     def inner(v):
#         visited[v] = 1
#         for v2 in range(n):
#             if not FRIEND[v][v2]:
#                 continue
#             if visited[v2]:
#                 continue
#             inner(v2)
#         return visited
#     return inner


# ans = [-1]*n

# for i in range(n):
#     # i番目の人の直接の友達リスト
#     friends = FRIEND[i]

#     # 友達の友達を含めたリスト
#     dfs = make_dfs()
#     possibly_friends = dfs(i)

#     # i番目の人のブロックリスト
#     blocks = BLOCK[i]
#     # print(possibly_friends, friends, blocks)

#     # possibly friends かつblock
#     blocks = [pf and b for pf, b in zip(possibly_friends, blocks)]
#     ans[i] = sum(possibly_friends) - sum(friends) - sum(blocks) - 1

#     # for f, pf, b in zip(friends, possibly_friends, blocks):
#     #     if pf and (not f) and (not b):
#     #         ans[i] += 1

# print(*ans)

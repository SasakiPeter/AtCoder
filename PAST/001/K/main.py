# オイラーツアーして、部分木に対して高速アクセスする
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n = int(input())
edges = [[]for _ in range(n)]
for i in range(n):
    p = int(input())-1
    if p == -2:
        init_v = i
        continue
    edges[i].append(p)
    edges[p].append(i)


tour_time = [[-1, -1]for _ in range(n)]
cnt = 0


def dfs(v, parent):
    global cnt
    cnt += 1
    tour_time[v][0] = cnt
    for v2 in edges[v]:
        if v2 == parent:
            continue
        dfs(v2, v)
    tour_time[v][1] = cnt


dfs(init_v, -1)


q = int(input())
for _ in range(q):
    a, b = map(lambda x: int(x)-1, input().split())
    sta, eda = tour_time[a]
    stb, edb = tour_time[b]
    if stb < sta and eda <= edb:
        print('Yes')
    else:
        print('No')

# # なぜかLCA重くてTLEしちゃう
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)


# class Tree:
#     def __init__(self, n):
#         self.n = n
#         self.edges = [[]for _ in range(n)]
#         self.max_logn = (n-1).bit_length()
#         self.depth = [0]*n
#         self.parent = [[-1]*self.max_logn for _ in range(n)]

#     def add_edge(self, u, v):
#         self.edges[u].append(v)
#         self.edges[v].append(u)

#     def init_lca(self, v=0, p=-1, d=0):
#         self.parent[v][0] = p
#         self.depth[v] = d

#         for k in range(d.bit_length()-1):
#             self.parent[v][k+1] = self.parent[self.parent[v][k]][k]

#         for v2 in self.edges[v]:
#             if v2 == p:
#                 continue
#             self.init_lca(v2, v, d+1)

#     def is_boss(self, u, v):
#         # vの方が上
#         # uからvと同じところまで、登る
#         diff = self.depth[v]-self.depth[u]
#         for k in range(diff.bit_length()):
#             if diff >> k & 1:
#                 v = self.parent[v][k]
#         if u == v:
#             return True
#         else:
#             return False


# n = int(input())
# tree = Tree(n)
# for i in range(n):
#     p = int(input())
#     if p == -1:
#         v = i
#     else:
#         tree.add_edge(i, p-1)
# tree.init_lca(v)

# q = int(input())
# for _ in range(q):
#     a, b = map(lambda x: int(x)-1, input().split())
#     if tree.is_boss(b, a):
#         print('Yes')
#     else:
#         print('No')

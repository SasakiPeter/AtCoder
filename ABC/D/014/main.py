# RMQ
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n = int(input())
edges = [[]for _ in range(n)]
for _ in range(n-1):
    x, y = map(lambda x: int(x)-1, input().split())
    edges[x].append(y)
    edges[y].append(x)
for edge in edges:
    edge.sort()

# euler tourをしてLCAして、閉路に含まれる
# ノードの数を数える

vs = [0]*(n*2-1)
depth = [0]*(n*2-1)
ID = [0]*n


def dfs(v, p, d):
    global k
    ID[v] = k
    vs[k] = v
    depth[k] = d
    k += 1
    for v2 in edges[v]:
        if v2 == p:
            continue
        dfs(v2, v, d+1)
        vs[k] = v
        depth[k] = d
        k += 1


k = 0
dfs(0, -1, 0)
# print(vs)
# print(ID)
# print(depth)


INF = (1 << 31) - 1
SEG_LEN = n*2-1
# print(SEG_LEN)
# SEG_LEN = 1 << 4
SEG = [(-1, INF)]*(SEG_LEN*2)


def update(i, x):
    i += SEG_LEN
    SEG[i] = (i-SEG_LEN, x)
    while i > 0:
        i //= 2
        if SEG[i*2][1] < SEG[i*2+1][1]:
            SEG[i] = SEG[i*2]
        elif SEG[i*2][1] == SEG[i*2+1][1]:
            SEG[i] = (min(SEG[i*2][0], SEG[i*2+1][0]), SEG[i*2][1])
        else:
            SEG[i] = SEG[i*2+1]

        # SEG[i] = min(SEG[i*2], SEG[i*2+1])


def find(left, right):
    left += SEG_LEN
    right += SEG_LEN
    ans = (-1, INF)
    while left < right:
        if left % 2 == 1:
            if SEG[left][1] < ans[1]:
                ans = SEG[left]
            # ans = min(SEG[left], ans)
            left += 1
        left //= 2
        if right % 2 == 1:
            if SEG[right-1][1] < ans[1]:
                ans = SEG[right-1]
            # ans = min(SEG[right-1], ans)
            right -= 1
        right //= 2
    return ans[0]


for i in range(n*2-1):
    update(i, depth[i])


# print(SEG)


def lca(u, v):
    idu = ID[u]
    idv = ID[v]
    if idu > idv:
        idu, idv = idv, idu
    # index返す
    return find(idu, idv)


q = int(input())
for _ in range(q):
    a, b = map(lambda x: int(x)-1, input().split())
    # print(lca(a, b))
    print(depth[ID[a]]+depth[ID[b]]-2*depth[lca(a, b)]+1)


# # 二分探索でO(nlogn)　pythonでぎり間に合う
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

#     def lca(self, u, v):
#         if self.depth[v] < self.depth[u]:
#             u, v = v, u
#         diff = self.depth[v]-self.depth[u]
#         for k in range(diff.bit_length()):
#             if diff >> k & 1:
#                 v = self.parent[v][k]
#         if u == v:
#             return u
#         for k in reversed(range(self.depth[u].bit_length())):
#             if self.parent[u][k] != self.parent[v][k]:
#                 u = self.parent[u][k]
#                 v = self.parent[v][k]
#         return self.parent[u][0]


# n = int(input())
# tree = Tree(n)
# for _ in range(n-1):
#     x, y = map(lambda x: int(x)-1, input().split())
#     tree.add_edge(x, y)

# tree.init_lca()
# q = int(input())
# for _ in range(q):
#     a, b = map(lambda x: int(x)-1, input().split())
#     print(tree.depth[a]+tree.depth[b]-2*tree.depth[tree.lca(a, b)]+1)

# # 二分探索でO(nlogn)　pythonでぎり間に合う
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)
# n = int(input())
# edges = [[]for _ in range(n)]
# for _ in range(n-1):
#     x, y = map(lambda x: int(x)-1, input().split())
#     edges[x].append(y)
#     edges[y].append(x)

# MAX_LOGV = 18
# depth = [0]*n
# # これをダブリングという
# # 本当は中が軽い方がいい
# # parent = [[-1]*n for _ in range(MAX_LOGV)]
# # pythonで通すには、ここを逆にして軽くしないとキツそう
# parent = [[-1]*MAX_LOGV for _ in range(n)]


# def init_lca(v=0, p=-1, d=0):
#     parent[v][0] = p
#     depth[v] = d

#     for k in range(d.bit_length()-1):
#         parent[v][k+1] = parent[parent[v][k]][k]

#     for v2 in edges[v]:
#         if v2 == p:
#             continue
#         init_lca(v2, v, d+1)


# init_lca()
# # print(parent)


# def lca(u, v):
#     # uとv同じ深さまで浮上する

#     if depth[v] < depth[u]:
#         u, v = v, u
#     # vの方が深い
#     for k in range(MAX_LOGV):
#         if (depth[v]-depth[u]) >> k & 1:
#             v = parent[v][k]

#     if u == v:
#         return u

#     for k in reversed(range(MAX_LOGV)):
#         if parent[u][k] != parent[v][k]:
#             u = parent[u][k]
#             v = parent[v][k]

#     return parent[u][0]


# q = int(input())
# for _ in range(q):
#     a, b = map(lambda x: int(x)-1, input().split())
#     print(depth[a]+depth[b]-2*depth[lca(a, b)]+1)

# かえって遅い
# query = [map(lambda x: int(x)-1, input().split()) for _ in range(q)]
# print(*[depth[a]+depth[b]-2*depth[lca(a, b)]+1 for a, b in query], sep='\n')


# # 二分探索でO(nlogn)　pythonだとぎり間に合わない
# import sys
# # import math as m
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)
# n = int(input())
# edges = [[]for _ in range(n)]
# for _ in range(n-1):
#     x, y = map(lambda x: int(x)-1, input().split())
#     edges[x].append(y)
#     edges[y].append(x)


# # pypyにlog2 moduleはない
# # MAX_LOGV = int(m.log2(10**5))
# # MAX_LOGV = int(m.log2(n))+1
# MAX_LOGV = 18
# depth = [0]*n
# # これをダブリングという
# parent = [[0]*n for _ in range(MAX_LOGV)]


# def dfs(v, p, d):
#     parent[0][v] = p
#     depth[v] = d
#     for v2 in edges[v]:
#         if v2 == p:
#             continue
#         dfs(v2, v, d+1)


# dfs(0, -1, 0)
# # print(parent)
# # print(depth)
# for k in range(MAX_LOGV-1):
#     for v in range(n):
#         if parent[k][v] < 0:
#             parent[k+1][v] = -1
#         else:
#             parent[k+1][v] = parent[k][parent[k][v]]
# # print(parent)


# def lca(u, v):
#     # uとv同じ深さまで浮上する
#     cnt = 2
#     if depth[v] < depth[u]:
#         u, v = v, u
#     # vの方が深い
#     for k in range(MAX_LOGV):
#         if (depth[v]-depth[u]) >> k & 1:
#             v = parent[k][v]
#             cnt += 1 << k

#     if u == v:
#         return cnt-1

#     for k in reversed(range(MAX_LOGV)):
#         if parent[k][u] != parent[k][v]:
#             u = parent[k][u]
#             v = parent[k][v]
#             # cnt += 2*(k+1)
#             cnt += 1 << (k+1)
#             # print(k, u, v, 'hoge')
#     # 最後、根っこの分足す
#     return cnt+1


# q = int(input())
# for _ in range(q):
#     a, b = map(lambda x: int(x)-1, input().split())
#     print(lca(a, b))

# 計算量O（n**2）
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)
# n = int(input())
# edges = [[]for _ in range(n)]
# for _ in range(n-1):
#     x, y = map(lambda x: int(x)-1, input().split())
#     edges[x].append(y)
#     edges[y].append(x)


# depth = [0]*n
# parent = [0]*n


# def dfs(v, p, d):
#     parent[v] = p
#     depth[v] = d
#     for v2 in edges[v]:
#         if v2 == p:
#             continue
#         dfs(v2, v, d+1)


# dfs(0, -1, 0)
# # print(parent)
# # print(depth)


# def lca(u, v):
#     # uとv同じ深さまで浮上する
#     cnt = 2
#     while depth[u] < depth[v]:
#         v = parent[v]
#         cnt += 1
#     while depth[v] < depth[u]:
#         u = parent[u]
#         cnt += 1
#     while u != v:
#         u = parent[u]
#         v = parent[v]
#         cnt += 2
#     else:
#         cnt -= 1
#     return cnt


# q = int(input())
# for _ in range(q):
#     a, b = map(lambda x: int(x)-1, input().split())
#     print(lca(a, b))

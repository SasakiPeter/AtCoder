from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dinp = [0]*n
edges = [[]for _ in range(n)]
for _ in range(m):
    x, y = list(map(lambda x: int(x)-1, input().split()))
    edges[x].append(y)
    dinp[y] += 1


next_v = deque([])
dist = [-1]*n
for i in range(n):
    if dinp[i] == 0:
        next_v.append(i)
        dist[i] = 0
ans = 0
while next_v:
    v = next_v.popleft()
    for v2 in edges[v]:
        dinp[v2] -= 1
        if dinp[v2] != 0:
            continue
        next_v.append(v2)
        if dist[v]+1 <= dist[v2]:
            continue
        dist[v2] = dist[v]+1
        ans = max(ans, dist[v2])
print(ans)


# # トポロジカルソートして、DP
# from collections import deque
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# edges = [[]for _ in range(n)]
# dinp = [0]*n
# for _ in range(m):
#     x, y = list(map(lambda x: int(x)-1, input().split()))
#     edges[x].append(y)
#     dinp[y] += 1


# # 入次数が0の頂点があれば、その頂点をソート後の結果に追加し
# # その頂点と隣接した頂点の入次数をマイナス1する（すでにソートしたので削除）

# next_v = deque([])
# for i in range(n):
#     if dinp[i] == 0:
#         next_v.append(i)
# toposorted = []
# while next_v:
#     v = next_v.pop()
#     toposorted.append(v)
#     for v2 in edges[v]:
#         dinp[v2] -= 1
#         if dinp[v2] != 0:
#             continue
#         next_v.append(v2)

# # 実質O(E)
# dist = [0]*n
# for i in range(n):
#     v = toposorted[i]
#     for v2 in edges[v]:
#         if dist[v]+1 <= dist[v2]:
#             continue
#         dist[v2] = dist[v]+1
# print(max(dist))


# # DFSっぽくトポソしながらDPするパターン
# # memoizeっていうデコレータ使わない方が早い
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)
# n, m = map(int, input().split())
# edges = [[] for _ in range(n)]
# for _ in range(m):
#     x, y = list(map(lambda x: int(x)-1, input().split()))
#     edges[x].append(y)

# # memo　デコレータより早い
# dist = [-1]*n


# def longest_path(v):
#     if dist[v] != -1:
#         return dist[v]
#     retval = 0
#     for v2 in edges[v]:
#         retval = max(retval, longest_path(v2)+1)
#     dist[v] = retval
#     return dist[v]


# ans = 0
# for i in range(n):
#     ans = max(ans, longest_path(i))
# print(ans)

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)
# n, m = map(int, input().split())
# edges = [[] for _ in range(n)]
# for _ in range(m):
#     x, y = list(map(lambda x: int(x)-1, input().split()))
#     edges[x].append(y)


# # う〜ん、デコレータはそんなに早くない
# def memoize(f):
#     memo = [-1]*n

#     def memoized(args):
#         if memo[args] != -1:
#             return memo[args]
#         else:
#             memo[args] = f(args)
#             return memo[args]
#     return memoized


# @memoize
# def longest_path(v):
#     retval = 0
#     for v2 in edges[v]:
#         retval = max(retval, longest_path(v2)+1)
#     return retval


# ans = 0
# for i in range(n):
#     ans = max(ans, longest_path(i))
# print(ans)


# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)
# n, m = map(int, input().split())
# edges = [[] for _ in range(n)]
# for _ in range(m):
#     x, y = list(map(lambda x: int(x)-1, input().split()))
#     edges[x].append(y)


# def memoize(f):
#     memo = dict()

#     def memoized(*args):
#         if args in memo.keys():
#             return memo[args]
#         else:
#             memo[args] = f(*args)
#             return memo[args]
#     return memoized


# # memo
# # dist = [-1]*n


# # def longest_path(v):
# #     if dist[v] != -1:
# #         return dist[v]
# #     retval = 0
# #     for v2 in edges[v]:
# #         retval = max(retval, longest_path(v2)+1)
# #     dist[v] = retval
# #     return dist[v]


# @memoize
# def longest_path(v):
#     retval = 0
#     for v2 in edges[v]:
#         retval = max(retval, longest_path(v2)+1)
#     return retval


# ans = 0
# for i in range(n):
#     # ans = max(ans, longest_path(i))
#     ans = max(ans, longest_path(i))
# print(ans)
# # print(dist)


# if dist[v2]<=dist[v]-1:
#   continue


# # 冷静に、普通にbellman-fordでは？
# # bellman-fordだと、node分更新しないといけなくて、
# # とても大変だから、更新すべきエッジを、上流の方から順番に
# # 並び替えたい→トポロジカルソート
# # なんと、再帰で実装すると、内部的にトポロジカルソートしてくれる

# from collections import defaultdict
# n, m = map(int, input().split())
# edges = []
# dd = defaultdict(int)
# for _ in range(m):
#     x, y = list(map(lambda x: int(x)-1, input().split()))
#     edges.append((x, y))
#     dd[y] += 1

# # print(dd)

# edges.sort(key=lambda x: dd[x[1]])

# dist = [0]*n
# # for _ in range(n-1):
# for v, v2 in edges:
#     if dist[v2] <= dist[v]-1:
#         continue
#     dist[v2] = dist[v]-1

# print(-min(dist))
# # print(dist)

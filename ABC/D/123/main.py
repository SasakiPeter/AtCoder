# そう、heap使えないかなって思ってたんだよね〜
import heapq
from collections import defaultdict
x, y, z, K = map(int, input().split())
A = sorted(map(int, input().split()), reverse=True)
B = sorted(map(int, input().split()), reverse=True)
C = sorted(map(int, input().split()), reverse=True)
visited = defaultdict(bool)
Q = [(-(A[0]+B[0]+C[0]), 0, 0, 0)]

for _ in range(K):
    S, i, j, k = heapq.heappop(Q)
    print(-S)
    if i+1 < x and not visited[i+1, j, k]:
        heapq.heappush(Q, (-(A[i+1]+B[j]+C[k]), i+1, j, k))
        visited[i+1, j, k] = True

    if j+1 < y and not visited[i, j+1, k]:
        heapq.heappush(Q, (-(A[i]+B[j+1]+C[k]), i, j+1, k))
        visited[i, j+1, k] = True

    if k+1 < z and not visited[i, j, k+1]:
        heapq.heappush(Q, (-(A[i]+B[j]+C[k+1]), i, j, k+1))
        visited[i, j, k+1] = True


# # にぶたんでとく pypyなら　微妙
# x, y, z, K = map(int, input().split())
# A = sorted(map(int, input().split()), reverse=True)
# B = sorted(map(int, input().split()), reverse=True)
# C = sorted(map(int, input().split()), reverse=True)


# def check(P):
#     cnt = 0
#     for i in range(x):
#         for j in range(y):
#             for k in range(z):
#                 if A[i]+B[j]+C[k] < P:
#                     break
#                 cnt += 1
#                 if K <= cnt:
#                     return True
#     return False


# L = 1
# R = 10**14
# while L != R-1:
#     M = (L+R)//2
#     if check(M):
#         L = M
#     else:
#         R = M
# # print(L, R)

# ans = []
# for i in range(x):
#     for j in range(y):
#         for k in range(z):
#             if A[i]+B[j]+C[k] <= L:
#                 break
#             ans.append(A[i]+B[j]+C[k])

# ans.sort(reverse=True)
# for i in range(K):
#     if i < len(ans):
#         print(ans[i])
#     else:
#         print(L)


# # 10**5くらい
# x, y, z, K = map(int, input().split())
# A = sorted(map(int, input().split()), reverse=True)
# B = sorted(map(int, input().split()), reverse=True)
# C = sorted(map(int, input().split()), reverse=True)
# ans = []
# for i in range(x):
#     for j in range(y):
#         for k in range(z):
#             if (i+1)*(j+1)*(k+1) <= K:
#                 ans.append(A[i]+B[j]+C[k])
#                 continue
#             break
# ans.sort(reverse=True)
# # print(ans)
# for i in range(K):
#     print(ans[i])


# # pypyじゃないと厳しい
# from itertools import product
# x, y, z, k = map(int, input().split())
# A = map(int, input().split())
# B = map(int, input().split())
# C = map(int, input().split())
# AB = [sum(ab) for ab in product(A, B)]
# AB.sort(reverse=True)
# AB = AB[:k]
# ABC = [sum(abc) for abc in product(AB, C)]
# ABC.sort(reverse=True)
# for i in range(k):
#     print(ABC[i])

# print(AB)


# # 10**9が通るなら、DFSしてソートが楽
# from itertools import product
# x, y, z, k = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))
# ALL = []
# for a, b, c in zip(A, B, C):
#     ALL.append((a, 0))
#     ALL.append((b, 1))
#     ALL.append((c, 2))
# ALL.sort(reverse=True)

# # いくつ使うかを計算する
# cnt = [0]*3
# for x, label in ALL:
#     cnt[label] += 1
#     if k <= cnt[0]*cnt[1]*cnt[2]:
#         break

# ABC = [[]for _ in range(3)]
# for x, label in ALL[:sum(cnt)]:
#     ABC[label].append(x)

# print(ABC)

# ans = []
# for x in product(*ABC):
#     ans.append(sum(x))
# ans.sort(reverse=True)

# for i in range(k):
#     print(ans[i])

# numpy
# 複数添字アクセスが一番早い
import numpy as np
import sys
input = sys.stdin.readline
n, m, q = map(int, input().split())
cnt = [[0]*(n+1)for _ in range(n+1)]
for _ in range(m):
    L, R = map(int, input().split())
    cnt[L][R] += 1

# # ↓むしろ遅い
# cnt = np.zeros((n+1, n+1), dtype=np.int32)
# L, R = map(np.array, zip(*[map(int, input().split()) for _ in range(m)]))
# # cnt[L, R] += 1 ←これはできない
# np.add.at(cnt, (L, R), 1)

S = np.cumsum(cnt, axis=0).cumsum(axis=1)

# L, R = map(np.array, zip(*[map(int, input().split()) for _ in range(q)]))
# tupleにした方が早い
L, R = map(np.array, zip(
    *[tuple(map(int, input().split())) for _ in range(q)]))

ans = S[R, R]-S[R, L-1]-S[L-1, R]+S[L-1, L-1]
print(*ans, sep='\n')

# # numpy
# # 累積だけnumpyで処理して、添字アクセスはリストが早い
# import numpy as np
# n, m, q = map(int, input().split())
# cnt = [[0]*(n+1)for _ in range(n+1)]
# for _ in range(m):
#     L, R = map(int, input().split())
#     cnt[L][R] += 1

# S = np.cumsum(cnt, axis=0).cumsum(axis=1).tolist()

# for _ in range(q):
#     L, R = map(int, input().split())
#     ans = S[R][R]-S[R][L-1]-S[L-1][R]+S[L-1][L-1]
#     print(ans)


# # ２次元累積和
# n, m, q = map(int, input().split())
# edges = [[0]*(n+1) for _ in range(n+1)]

# for _ in range(m):
#     L, R = map(int, input().split())
#     edges[L][R] += 1

# for i in range(1, n+1):
#     for j in range(n):
#         edges[i][j+1] += edges[i][j]

# for i in range(n):
#     for j in range(1, n+1):
#         edges[i+1][j] += edges[i][j]

# for _ in range(q):
#     p, q = map(int, input().split())
#     ans = edges[q][q]-edges[q][p-1]-edges[p-1][q]+edges[p-1][p-1]
#     print(ans)

# # ２次元平面上に落とし込む
# n, m, q = map(int, input().split())
# edges = [[0]*n for _ in range(n)]

# for _ in range(m):
#     L, R = map(lambda x: int(x)-1, input().split())
#     edges[L][R] += 1

# # for row in edges:
# #     print(row)

# S = [[0]*(n+1)for _ in range(n+1)]
# for i in range(n):
#     for j in range(n):
#         S[i][j+1] = S[i][j] + edges[i][j]

# for _ in range(q):
#     p, q = map(int, input().split())
#     # print(p, q)
#     lines = S[p-1:q]
#     ans = 0
#     for row in lines:
#         ans += row[q]-row[p-1]
#     print(ans)

# lines = edges[p-1:q]
# print(sum(sum(row[p-1:q]) for row in lines))

# import bisect
# n, m, q = map(int, input().split())
# edges = []
# for i in range(m):
#     L, R = map(int, input().split())
#     edges.append((L, R, i))

# L_sorted = sorted(edges)
# L_sorted_bi = [L for L, R, i in L_sorted]
# L_cum_set = [set()for _ in range(m+1)]
# for i in reversed(range(m)):
#     L_cum_set[i] = L_cum_set[i+1] | {L_sorted[i][2]}


# R_sorted = sorted(edges, key=lambda x: x[1])
# R_sorted_bi = [R for L, R, i in R_sorted]
# R_cum_set = [set()for _ in range(m+1)]
# for i in range(m):
#     R_cum_set[i+1] = R_cum_set[i] | {R_sorted[i][2]}


# for _ in range(q):
#     p, q = map(int, input().split())
#     # Lがp以上
#     idx = bisect.bisect_left(L_sorted_bi, p)
#     s = L_cum_set[idx]

#     idx = bisect.bisect_left(R_sorted_bi, q+1)
#     t = R_cum_set[idx]
#     # ここが重い
#     print(len(s & t))

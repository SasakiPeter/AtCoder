# これ、よく考えると、探索したらダメなやつ
# 探索するとしたら、ダブリング？
h, w, d = map(int, input().split())
As = [list(map(int, input().split()))for _ in range(h)]

ans = 0
for i in range(h):
    A = As[i]
    start = d & 1 ^ i & 1
    end = min(d-i+1, w)
    if end <= start:
        continue
    x = A[start:end:2]
    tmp = max(x)
    if ans < tmp:
        ans = tmp
print(ans)


# # これだと重すぎる しかも間違ってる
# h, w, D = map(int, input().split())
# MAP = [['#']*(w+2)]
# for _ in range(h):
#     A = list(map(int, input().split()))
#     MAP.append(['#']+A+['#'])
# else:
#     MAP.append(['#']*(w+2))


# visited = [[0]*(w+2)for _ in range(h+2)]

# # d回の操作で到達できる頂点をあらいたい
# # BFSで探索して、到達できる点を記録する
# ans = 0
# next_v = [(1, 1, 0)]
# while next_v:
#     i, j, d = next_v.pop()
#     if d == D:
#         visited[i][j] = 1
#         if ans < MAP[i][j]:
#             ans = MAP[i][j]
#         continue
#     dirc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#     for di, dj in dirc:
#         x, y = i+di, j+dj
#         if MAP[x][y] == '#':
#             continue
#         if visited[x][y] and d+1 == D:
#             continue
#         next_v.append((x, y, d+1))

# # print(h, w, D)

# # for row in visited:
# #     print(row)

# print(ans)

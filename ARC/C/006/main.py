# 実は貪欲やで
# bisectを使って、O(nlogn)で計算できる
import bisect
n = int(input())
# 10**7で９秒くらい
# n = 10**7
# weights = [i for i in range(n)]
INF = 10**9
boxes = [INF]*n

for _ in range(n):
    w = int(input())
# for w in weights:
    idx = bisect.bisect_left(boxes, w)
    boxes[idx] = w
print(bisect.bisect_left(boxes, INF))


# # 実は貪欲やで
# # n = int(input())
# # 10**4で６秒くらい
# n = 10**4
# weights = [i for i in range(n)]
# INF = 10**9
# boxes = [INF]

# # O(n**2)でちょっと重い
# # for _ in range(n):
# #     w = int(input())
# for w in weights:
#     target_idx = -1
#     min_diff = INF
#     for idx, box in enumerate(boxes):
#         if box - w < 0:
#             continue
#         if box-w < min_diff:
#             target_idx = idx
#             min_diff = box-w
#     if target_idx == -1:
#         boxes.append(w)
#     else:
#         boxes[target_idx] = w

# print(len(boxes))


# DFSだとどう頑張ってもTLEみたいですね！！！
# n = int(input())
# w = [int(input()) for _ in range(n)]
# # n = 50
# # w = [i for i in range(n, 0, -1)]
# INF = 10**9
# ans = INF


# def dfs(idx, top_box_weight):
#     global ans
#     if idx == n:
#         ans = min(ans, len(top_box_weight))
#         return 0
#     else:
#         # if ans < len(top_box_weight):
#         #     return 0

#         for i in range(len(top_box_weight)+1):
#             flag = False
#             if len(top_box_weight) < i+1:
#                 flag = True
#                 # if ans > len(top_box_weight):
#                 #     dfs(idx+1, top_box_weight+[w[idx]])

#             # ここ探索しすぎでは？
#             elif top_box_weight[i] >= w[idx] and ans > len(top_box_weight):
#                 top_box_weight[i] = w[idx]
#                 dfs(idx+1, top_box_weight)

#             if flag and ans > len(top_box_weight)+1:
#                 dfs(idx+1, top_box_weight+[w[idx]])


# dfs(0, [])
# print(ans)


# def dfs(idx, n_group, group_min):
#     global ans
#     if idx == n:
#         ans = min(ans, n_group)
#         return 0
#     else:
#         for i in range(n_group+1):
#             if len(group_min) < i+1:
#                 dfs(idx+1, max(n_group, i+1), group_min+[w[idx]])
#             elif group_min[i] >= w[idx]:
#                 group_min[i] = w[idx]
#                 dfs(idx+1, n_group, group_min)
# dfs(idx+1, max(n_group, i+1), group_min)


# dfs(0, 0, [])
# print(ans)

# def dfs(idx, group, n_group, group_min):
#     # groups = [[INF] for _ in range(n_group)]
#     # for i in range(idx):
#     #     if groups[group[i]][-1] >= w[i]:
#     #         groups[group[i]].append(w[i])
#     #     else:
#     #         return 0
#     # groups = [INF]*n_group
#     # for i in range(idx):
#     #     if groups[group[i]] >= w[i]:
#     #         groups[group[i]] = w[i]
#     #     else:
#     #         return 0

#     if idx == n:
#         return ls.append((group, n_group))
#     else:
#         for i in range(n_group+1):
#             if len(group_min) < i+1:
#                 dfs(idx+1, group+[i], max(n_group, i+1), group_min+[w[idx]])
#             elif group_min[i] >= w[idx]:
#                 group_min[i] = w[idx]
#                 dfs(idx+1, group+[i], max(n_group, i+1), group_min)


# dfs(1, [0], 1)
# dfs(0, [], 0, [])
# print(ls)

# ans = INF
# for state, v in ls:
#     ans = min(ans, v)
# print(ans)

# num = 1

# ls = [[] for _ in range(num)]


# def dfs(idx, ls):
#     global num
#     # if sum(len(x) for x in ls) == n:
#     #     return ls
#     if idx == n-1:
#         return ls
#     else:
#         for j in range(num):
#             ls[j].append(w[i])
#             dfs(idx+1, ls[j]+)


# # DFSかけないマンになってる！！！
# # どの情報を保持すればいいのかわからない
# ls = [[w[0]] for _ in range(1)]

# for i in range(1, n):
#     x = w[i]
#     if ls[0] <= x:
#         ls[0].append(x)
#     else:
#         print("error")

# # わかった、wっていう要素を、０、１、２、っていう番号に変えていけばいい
# # それは、どこの山に属するかっていうのを示す標識で、
# # 左から順番に積み重なっているっていう設定
# # それだと容易に全探索できる
# # でも、全探索は間に合わない
# # うまいことDFS書かないとダメだこれ


# boxes = [-1]*w
# boxes[0] = 0


# def dfs(color, idx, boxes):
#     if idx == n-1:
#         if
#     else:
#         for c in range(color):

#             boxes[idx] = c
#             dfs(color, idx+1)


# dfs()

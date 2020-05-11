lunlun = []


def dfs(x):
    lunlun.append(x)
    if x > 3234566667:
        return 0
    d = x % 10
    if d != 0:
        dfs(10*x+d-1)
    dfs(10*x+d)
    if d != 9:
        dfs(10*x+d+1)


for i in range(1, 10):
    dfs(i)

lunlun.sort()
k = int(input())
print(lunlun[k-1])

# from collections import deque
# k = int(input())


# def generate_lunlun(x):
#     d = int(x) % 10
#     if d != 0:
#         yield x+str(d-1)
#     yield x+str(d)
#     if d != 9:
#         yield x+str(d+1)


# d = deque([str(i) for i in range(1, 10)])
# for _ in range(k):
#     x = d.popleft()
#     for y in generate_lunlun(x):
#         d.append(y)
# print(x)


# # DFSで実装する
# # ただし、DFSだとソートした状態になっていないので
# # あとでソートしてあげる必要がある
# k = int(input())
# ans = []

# def dfs(x):
#     # if x > 10**10:
#     if x > 3234566667:
#         return 0
#     else:
#         ans.append(x)
#         y = x % 10
#         for i in range(10):
#             if abs(y-i) <= 1:
#                 dfs(10*x+i)

# for i in range(1, 10):
#     dfs(i)

# ans.sort()
# print(ans[k-1])
# # print(len(ans[:k]))

# # # generater使ってとく
# # k = int(input())

# # ans = [i for i in range(1, 10)]

# # def generate_lunlun(x):
# #     y = x % 10
# #     if 0 <= y-1:
# #         yield 10*x + y-1
# #     yield 10*x + y
# #     if y+1 < 10:
# #         yield 10*x + y+1

# # idx = 0
# # while len(ans) < k:
# #     x = ans[idx]
# #     for i in generate_lunlun(x):
# #         ans.append(i)
# #     idx += 1

# # print(ans[k-1])
# # # print(ans)

# # # generater使ってとく
# # # idx参照する方が強いけど、dequeで要素を取り出しちゃう
# # # 倍くらい遅くなる
# # from collections import deque
# # k = int(input())

# # ans = deque([i for i in range(1, 10)])

# # def generate_lunlun(x):
# #     y = x % 10
# #     if 0 <= y-1:
# #         yield 10*x + y-1
# #     yield 10*x + y
# #     if y+1 < 10:
# #         yield 10*x + y+1
# # cnt = 0
# # while True:
# #     x = ans.popleft()
# #     for i in generate_lunlun(x):
# #         ans.append(i)
# #     cnt += 1
# #     if cnt == k:
# #         print(x)
# #         break

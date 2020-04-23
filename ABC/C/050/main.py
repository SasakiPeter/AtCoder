# from collections import defaultdict
# n = int(input())
# a = list(map(int, input().split()))

# # まず、実現可能な並びかを判定する
# # a を集計してみる
# d = defaultdict(int)
# for x in a:
#     d[x] += 1
# # print(d)

# # nの値から、配列を生成する
# b = [i for i in range(n)[::-1]]
# # c = b[::2] + b[::2][::-1][n % 2:]
# # print(c)

# # ↑これする意味なかった

# e = all(d[i] == 2 if n % 2 == 0 else d[i] ==
#         1 if i == 0 else d[i] == 2 for i in b[::2])
# if not e:
#     print(0)
#     exit()
# ans = 1
# for v in d.values():
#     ans = ans * v % (10**9+7)
# print(ans)


# refactor
# from collections import defaultdict
# n = int(input())
# a = list(map(int, input().split()))
# d = defaultdict(int)
# for x in a:
#     d[x] += 1
# b = [i for i in range(n)[::-1]]
# if not all([d[i] == 2, d[i] == 1][n % 2 and i == 0] for i in b[::2]):
#     print(0)
# else:
#     ans = 1
#     for v in d.values():
#         ans = ans * v % (10**9+7)
#     print(ans)


# なんかよくわからんけど、めちゃ速い
N = int(input())
A = list(map(int, input().split()))
flag = True
if N % 2 == 0:
    if 0 in A or len(set(A)) != N//2:
        flag = False
else:
    if len([0 for a in A if a == 0]) != 1 or len(set(A)) != N//2+1:
        flag = False
if flag:
    print(2**(N//2) % (10**9+7))
else:
    print(0)

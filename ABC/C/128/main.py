# DFS
n, m = map(int, input().split())
ls = []
for _ in range(m):
    k, *s, = map(lambda x: int(x)-1, input().split())
    ls.append(s)
p = list(map(int, input().split()))
ans = 0


def dfs(x, s):
    global ans
    if x == n:
        for j in range(m):
            switchs = ls[j]
            cond = p[j]
            on_cnt = 0
            for switch in switchs:
                if int(s[switch]):
                    on_cnt += 1
            if on_cnt % 2 != cond:
                break
        else:
            ans += 1
    else:
        for c in "01":
            dfs(x+1, s+c)


dfs(0, "")
print(ans)


# from itertools import product
# n, m = map(int, input().split())
# ls = []
# for _ in range(m):
#     k, *s, = map(lambda x: int(x)-1, input().split())
#     ls.append(s)
# p = list(map(int, input().split()))
# it = ["01"]*n

# ans = 0
# for b in product(*it):
#     base_2 = "".join(b)
#     for j in range(m):
#         switchs = ls[j]
#         cond = p[j]
#         on_cnt = 0
#         for switch in switchs:
#             if int(base_2[switch]):
#                 on_cnt += 1
#         if on_cnt % 2 != cond:
#             break
#     else:
#         ans += 1
# print(ans)


# n, m = map(int, input().split())
# ls = []
# for _ in range(m):
#     k, *s, = map(lambda x: int(x)-1, input().split())
#     ls.append(s)
# p = list(map(int, input().split()))

# # print(ls)


# def base_n(x, n, zero_padding=8):
#     retval = [[], ['0']][x == 0]
#     while x > 0:
#         x, r = divmod(x, n)
#         retval.append(str(r))
#     cnt = zero_padding - len(retval)
#     pad = ['', '0'*cnt][cnt > 0]
#     return pad+''.join(retval[::-1])


# ans = 0
# for i in range(2**n):
#     base_2 = base_n(i, 2, n)
#     for j in range(m):
#         # j番目のライトにつながってるスイッチがオンか調べて、光るかどうか判定
#         # j番目のライトにつながってるスイッチの一覧が欲しい
#         switchs = ls[j]
#         cond = p[j]

#         on_cnt = 0
#         for switch in switchs:
#             if int(base_2[switch]):
#                 on_cnt += 1
#         if on_cnt % 2 != cond:
#             break
#     else:
#         ans += 1
# print(ans)

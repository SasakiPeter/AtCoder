# DFS
n = int(input())
ans = []


def dfs(x, s):
    if x == 0:
        ans.append(s)
    else:
        for c in ['a', 'b', 'c']:
            dfs(x-1, s+c)


dfs(n, "")
print(*ans, sep='\n')


# bit全探索（n進数だけど）
# n = int(input())


# def base_n(x, n, zero_padding=8):
#     retval = [[], ['0']][x == 0]
#     while x > 0:
#         x, r = divmod(x, n)
#         retval.append(str(r))
#     cnt = zero_padding - len(retval)
#     pad = ['', '0'*cnt][cnt > 0]
#     return pad+''.join(retval[::-1])


# for i in range(3**n):
#     base_3 = base_n(i, 3, n)
#     print(base_3.replace("0", "a").replace("1", "b").replace("2", "c"))


# 洗い出し
# from itertools import product
# n = int(input())
# abc = ['abc']*n
# for x in product(*abc):
#     print("".join(x))

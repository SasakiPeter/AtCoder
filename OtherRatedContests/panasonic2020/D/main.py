import sys
sys.setrecursionlimit(10**7)
n = int(input())
# n = 10
# ls = []


def dfs(s):
    if len(s) == n:
        print(s)
        # ls.append(s)
        # return 0
    else:
        for x in map(chr, range(97, ord(max(s))+2)):
            dfs(s+x)


dfs("a")
# ls.sort()
# for x in ls:
#     print(x)

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)

# # これ、何も見ずにかけたの凄くない？
# # ABC29C BruteForceと119CのSyntheticKadomatsu解いたら、発想できた
# n = int(input())
# char = "".join(chr(97+i) for i in range(n))
# # print(char)
# # ans = []


# def dfs(s, idx):
#     if len(s) == n:
#         # ans.append(s)
#         print(s)
#     else:
#         for i in range(idx):
#             # if i+1 != idx:
#             #     dfs(s+char[i], idx)
#             # else:
#             #     dfs(s+char[i], idx+1)

#             dfs(s+char[i], idx if i+1 != idx else idx+1)


# dfs("a", 2)
# # print(*ans, sep='\n')


# from itertools import product

# n = int(input())
# # n = 3
# # # print(chr(n))
# # print(ord("a"))
# # print(chr(97))
# abc = "".join(chr(97+i) for i in range(n))
# abc_l = [abc]*n

# for ls in product(*abc_l):
#     s = "".join(ls)
#     if s[0] != "a":
#         continue
#     for i in range(n-1):
#         if s[i] > s[i+1]:
#             break
#     else:
#         print(s)

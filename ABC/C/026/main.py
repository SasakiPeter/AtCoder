# 隣接行列でなくても良い
n = int(input())

sub = [[]*n for _ in range(n)]

for i in range(1, n):
    b = int(input())-1
    sub[b].append(i)


def dfs(x):
    sub_ls = sub[x]
    if not sub_ls:
        return 1
    salary_ls = [dfs(sub) for sub in sub_ls]
    return max(salary_ls) + min(salary_ls) + 1


print(dfs(0))

# # n<=20
# n = int(input())

# GRAPH = [[0]*n for _ in range(n)]

# for i in range(1, n):
#     b = int(input())-1
#     GRAPH[b][i] = 1


# def dfs(x):
#     if 1 not in GRAPH[x]:
#         return 1
#     salary_ls = []
#     for index, is_subordinate in enumerate(GRAPH[x]):
#         if is_subordinate:
#             salary_ls.append(dfs(index))
#     return max(salary_ls) + min(salary_ls) + 1


# print(dfs(0))

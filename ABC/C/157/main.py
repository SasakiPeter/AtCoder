# 全探索
n, m = map(int, input().split())
sc_ls = [list(map(int, input().split())) for _ in range(m)]

for num in range(10**n):
    if len(str(num)) != n:
        continue

    for s, c in sc_ls:
        if str(num)[s-1] != str(c):
            break
    else:
        print(num)
        break
else:
    print(-1)


# # 解法２
# n, m = map(int, input().split())

# # n桁
# num = [-1]*n

# # こいつがまじで戦犯
# # num = [0]*n

# for _ in range(m):
#     s, c = map(int, input().split())
#     if num[s-1] == c:
#         continue
#     elif num[s-1] == -1:
#         num[s-1] = c
#     else:
#         print(-1)
#         exit()

# if num[0] == 0:
#     if n == 1:
#         print(0)
#         exit()
#     else:
#         print(-1)
#         exit()
# elif num[0] == -1:
#     if n == 1:
#         print(0)
#         exit()
#     else:
#         num[0] = 1
# for i in range(1, n):
#     if num[i] == -1:
#         num[i] = 0

# print(*num, sep='')
